#!/usr/bin/env python3
"""VG-MATH gate: independent analytic verification of power_sim.py.

Route A (this file): closed-form-ish power via variance decomposition + noncentral t.
  Var(d_i) = Var_worlds(Delta_i) + E[sampling variance | world]   (independent runs given
  latents), all moments computed by Gauss-Hermite/MC-free quadrature over (u, v_j).
Route B (power_sim.py): direct Monte-Carlo of the full design.
Agreement across the grid within MC error => PASS for the power claim.

Also: delta-solver check by plain Monte-Carlo (independent of Gauss-Hermite), and
budget re-derivation by hand.
"""
import numpy as np
from scipy import stats
from power_sim import solve_mu_for_rate, marginal_rate, simulate_power, MODELS_OFFSETS


def sig(x):
    return 1.0 / (1.0 + np.exp(-x))


def analytic_power(n_worlds, base_rate, mme, sigma_w, sigma_wm, f, k, alpha=0.05):
    gh_x, gh_w = np.polynomial.hermite.hermgauss(60)
    wnorm = gh_w / np.sqrt(np.pi)
    sigma_tot = float(np.sqrt(sigma_w**2 + sigma_wm**2 + np.var(MODELS_OFFSETS)))
    mu0 = solve_mu_for_rate(base_rate, sigma_tot, gh_x, gh_w)
    mu1 = solve_mu_for_rate(base_rate + mme, sigma_tot, gh_x, gh_w)

    u = np.sqrt(2) * sigma_w * gh_x            # world nodes
    v = np.sqrt(2) * sigma_wm * gh_x           # world-x-model nodes
    J = len(MODELS_OFFSETS)
    q = 1.0 - f                                # malformed -> failure => success prob * q

    # per (u, model j): E_v[p], E_v[p^2], for both arms
    def moments(mu):
        # p over grid (u_nodes, models, v_nodes)
        z = mu + u[:, None, None] + MODELS_OFFSETS[None, :, None] + v[None, None, :]
        p = sig(z) * q
        Ep = np.tensordot(p, wnorm, axes=([2], [0]))       # (u, j)
        Ep2 = np.tensordot(p**2, wnorm, axes=([2], [0]))
        return Ep, Ep2

    Ep0, Ep0sq = moments(mu0)
    Ep1, Ep1sq = moments(mu1)

    # Delta_i = mean_j sigma-diff; E over v already taken; E over worlds via u-weights
    D_u = (Ep1 - Ep0).mean(axis=1)                          # E_v[Delta | u]
    mean_D = float(np.dot(wnorm, D_u))
    # Var over worlds: Var_u(E_v[Delta|u]) + E_u[Var_v(Delta|u)]/J
    var_between_u = float(np.dot(wnorm, D_u**2) - mean_D**2)
    # per model: Var_v(p1 - p0 | u, j) = Var_v(p1) + Var_v(p0)  (v indep across arms? NO —
    # v_ij is SHARED between arms within a world-model cell). Redo with shared v:
    z0 = mu0 + u[:, None, None] + MODELS_OFFSETS[None, :, None] + v[None, None, :]
    z1 = z0 + (mu1 - mu0)
    dpv = (sig(z1) - sig(z0)) * q                           # (u, j, v)
    Edp = np.tensordot(dpv, wnorm, axes=([2], [0]))         # (u, j)
    Edp2 = np.tensordot(dpv**2, wnorm, axes=([2], [0]))
    var_v_given_u = (Edp2 - Edp**2)                         # per (u, j)
    e_var_v = float(np.dot(wnorm, var_v_given_u.mean(axis=1))) / J
    # correct between-world variance: use shared-v Delta
    D_u_shared = Edp.mean(axis=1)
    mean_D = float(np.dot(wnorm, D_u_shared))
    var_between = float(np.dot(wnorm, D_u_shared**2) - mean_D**2) + e_var_v

    # sampling variance: p_hat_c = (1/(Jk)) sum Bern; Var = (1/(Jk)^2) * sum k p(1-p)
    def samp_var(Ep, Ep2):
        # E[p(1-p)] per (u,j) = Ep - Ep2 ; average over u,j
        e_pq = float(np.dot(wnorm, (Ep - Ep2).mean(axis=1)))
        return e_pq * J * k / (J * k) ** 2                  # = e_pq/(J*k)
    var_samp = samp_var(Ep1, Ep1sq) + samp_var(Ep0, Ep0sq)

    var_d = var_between + var_samp
    ncp = mean_D / np.sqrt(var_d / n_worlds)
    tcrit = stats.t.ppf(1 - alpha / 2, df=n_worlds - 1)
    power = 1 - stats.nct.cdf(tcrit, df=n_worlds - 1, nc=ncp) \
              + stats.nct.cdf(-tcrit, df=n_worlds - 1, nc=ncp)
    return float(power), mean_D


def main():
    rng = np.random.default_rng(99)
    print("== (1) power cross-check: analytic (Route A) vs Monte-Carlo (Route B), N=60, MME=0.15")
    worst_gap, rows = 0.0, 0
    for b in (0.20, 0.35, 0.50):
        for sw in (0.5, 1.0, 1.5):
            for swm in (0.25, 0.5):
                for f in (0.05, 0.15):
                    pa, da = analytic_power(60, b, 0.15, sw, swm, f, 3)
                    pm, dm = simulate_power(60, b, 0.15, sw, swm, f, 3, 800,
                                            np.random.default_rng(rng.integers(1e9)))
                    gap = abs(pa - pm)
                    worst_gap = max(worst_gap, gap)
                    rows += 1
    print(f"   cells={rows}  max |P_analytic - P_MC| = {worst_gap:.4f}")
    print("== also at the power-sensitive point (MME=0.08, N=60) where saturation can't mask errors")
    for (b, sw, swm, f) in [(0.20, 1.5, 0.5, 0.15), (0.35, 1.0, 0.5, 0.05), (0.50, 0.5, 0.25, 0.05)]:
        pa, _ = analytic_power(60, b, 0.08, sw, swm, f, 3)
        pm, _ = simulate_power(60, b, 0.08, sw, swm, f, 3, 3000,
                               np.random.default_rng(rng.integers(1e9)))
        print(f"   cell(base={b},sw={sw},swm={swm},f={f}): analytic={pa:.3f} MC={pm:.3f} gap={abs(pa-pm):.3f}")

    print("== (2) delta-solver check by plain MC (independent of Gauss-Hermite)")
    gh_x, gh_w = np.polynomial.hermite.hermgauss(40)
    for base, s in [(0.20, 1.2), (0.35, 1.0), (0.50, 1.6)]:
        mu0 = solve_mu_for_rate(base, s, gh_x, gh_w)
        mu1 = solve_mu_for_rate(base + 0.15, s, gh_x, gh_w)
        zs = rng.normal(0, s, size=2_000_000)
        mc0, mc1 = sig(mu0 + zs).mean(), sig(mu1 + zs).mean()
        print(f"   base={base}: MC rates {mc0:.4f}->{mc1:.4f} (targets {base:.2f}->{base+0.15:.2f}); "
              f"errs {abs(mc0-base):.4f}/{abs(mc1-base-0.15):.4f}")

    print("== (3) budget re-derivation by hand")
    runs = 60 * 3 * 3
    tot = runs * 6
    tokens = runs * 3 * 45_000 + runs * 3 * 20_000
    usd = tokens / 1000 * 0.008
    print(f"   runs/cond={runs} total={tot} tokens={tokens/1e6:.1f}M usd={usd:.0f} +15% pilot={usd*1.15:.0f}")
    print(f"   sensitivity: 2x token overrun -> ${usd*2*1.15:.0f} (still within $1-2k burst)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Design-sensitivity power analysis for the ABDUCTION-BENCHMARK factorial simulator experiment.

Primary contrast: C4 (action-controllable) vs C6 (yoked passive control), binary primary
outcome (mechanism recovery = rubric level 1-2), analyzed as a PAIRED, WORLD-LEVEL test:
per world, the success proportion in each condition (pooled over models x repeats) is
computed, and a two-sided paired t-test is run on the world-level differences.

Rationale (recorded in PREREGISTRATION_DRAFT.md sec.3): with a balanced design, the
summary-statistics (per-cluster proportion) approach is the classical equivalent of the
mixed-effects analysis for the treatment contrast; it respects world clustering exactly
and is fast enough to simulate. The confirmatory analysis remains the mixed-effects
logistic model; this simulation powers the design.

Data-generating process (logit scale):
    logit P(success) = mu + u_i + m_j + v_ij + delta * 1[condition=C4]
    u_i  ~ N(0, sigma_w^2)   world random effect
    m_j                       model fixed offsets (3 models)
    v_ij ~ N(0, sigma_wm^2)  world-x-model random effect (drives within-cell repeat corr.)
    malformed runs occur with prob f and are scored as failure (primary analysis rule).

delta is chosen per grid cell so that the marginal (population-average) success-rate
difference equals the target MME at the given baseline; solved numerically by
Gauss-Hermite integration over the random effects.

Deterministic under --seed. No wall-clock, no network.
"""

import argparse
import json
import numpy as np
from scipy import stats

MODELS_OFFSETS = np.array([0.0, -0.3, 0.3])  # three models, mild capability spread


def marginal_rate(mu, sigma, gh_x, gh_w):
    """Population-average success prob for logit ~ N(mu, sigma^2), by Gauss-Hermite."""
    z = mu + np.sqrt(2.0) * sigma * gh_x
    return float(np.sum(gh_w * (1.0 / (1.0 + np.exp(-z)))) / np.sqrt(np.pi))


def solve_mu_for_rate(target, sigma, gh_x, gh_w, lo=-8.0, hi=8.0):
    """Invert marginal_rate in mu (monotone) by bisection."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if marginal_rate(mid, sigma, gh_x, gh_w) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def simulate_power(n_worlds, base_rate, mme, sigma_w, sigma_wm, f_malformed,
                   k_repeats, n_sims, rng, alpha=0.05):
    """Return (power, mean_realized_diff) for the paired world-level t-test."""
    gh_x, gh_w = np.polynomial.hermite.hermgauss(40)
    # total random-effect sd seen by a run (worlds + world-x-model; model offsets average out
    # approximately for rate-solving purposes -- fold their spread in quadrature)
    sigma_tot = float(np.sqrt(sigma_w ** 2 + sigma_wm ** 2 + np.var(MODELS_OFFSETS)))
    mu0 = solve_mu_for_rate(base_rate, sigma_tot, gh_x, gh_w)
    mu1 = solve_mu_for_rate(base_rate + mme, sigma_tot, gh_x, gh_w)
    delta = mu1 - mu0  # log-odds effect giving the target marginal MME

    n_models = len(MODELS_OFFSETS)
    # latent effects: (sims, worlds) and (sims, worlds, models)
    u = rng.normal(0.0, sigma_w, size=(n_sims, n_worlds))
    v = rng.normal(0.0, sigma_wm, size=(n_sims, n_worlds, n_models))
    base_logit = mu0 + u[:, :, None] + MODELS_OFFSETS[None, None, :] + v

    def cell_successes(logit):
        p = 1.0 / (1.0 + np.exp(-logit))
        succ = rng.random(size=logit.shape + (k_repeats,)) < p[..., None]
        # malformed runs -> scored as failure
        malformed = rng.random(size=succ.shape) < f_malformed
        return np.where(malformed, False, succ)

    s_c6 = cell_successes(base_logit)          # passive recipient
    s_c4 = cell_successes(base_logit + delta)  # interactive chooser
    # per-world proportions pooled over models x repeats
    p4 = s_c4.mean(axis=(2, 3))
    p6 = s_c6.mean(axis=(2, 3))
    d = p4 - p6                                # (sims, worlds)
    mean_d = d.mean(axis=1)
    sd_d = d.std(axis=1, ddof=1)
    t = mean_d / (sd_d / np.sqrt(n_worlds))
    crit = stats.t.ppf(1.0 - alpha / 2.0, df=n_worlds - 1)
    return float(np.mean(np.abs(t) > crit)), float(mean_d.mean())


def budget_table(n_worlds, k_repeats, n_models=3):
    """Cost arithmetic for the full 6-condition experiment (C7 excluded, secondary)."""
    runs_per_cond = n_worlds * n_models * k_repeats
    conds = 6  # C1,C2,C3,C4,C5,C6 (C6 reuses C4's evidence but is a separate model run)
    total_runs = runs_per_cond * conds
    # token assumptions [inputs, recorded in prereg]: interactive arms (C3,C4,C5) avg 45k
    # tok/run; static arms (C1,C2,C6-replay) avg 20k tok/run; blended $/1k tok ~ $0.008
    # (mix of frontier input/output pricing, open-weight ~free on RunPod rental).
    tok_interactive, tok_static, usd_per_1k = 45_000, 20_000, 0.008
    tokens = runs_per_cond * 3 * tok_interactive + runs_per_cond * 3 * tok_static
    usd = tokens / 1000.0 * usd_per_1k
    return {"runs_per_condition": runs_per_cond, "total_runs": total_runs,
            "est_tokens_M": round(tokens / 1e6, 1), "est_usd": round(usd),
            "est_usd_with_pilot_15pct": round(usd * 1.15)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20260804)
    ap.add_argument("--n-sims", type=int, default=500)
    ap.add_argument("--mme", type=float, default=0.15)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)

    grid = {
        "base_rate": [0.20, 0.35, 0.50],
        "sigma_w": [0.5, 1.0, 1.5],
        "sigma_wm": [0.25, 0.5],
        "f_malformed": [0.05, 0.15],
        "n_worlds": [40, 60, 80],
        "k_repeats": [3],
    }
    rows = []
    for b in grid["base_rate"]:
        for sw in grid["sigma_w"]:
            for swm in grid["sigma_wm"]:
                for f in grid["f_malformed"]:
                    for nw in grid["n_worlds"]:
                        for k in grid["k_repeats"]:
                            pw, md = simulate_power(nw, b, args.mme, sw, swm, f, k,
                                                    args.n_sims, rng)
                            rows.append({"base_rate": b, "sigma_w": sw, "sigma_wm": swm,
                                         "f_malformed": f, "n_worlds": nw, "k_repeats": k,
                                         "power": round(pw, 3),
                                         "realized_diff": round(md, 3)})
    out = {"seed": args.seed, "n_sims": args.n_sims, "mme": args.mme,
           "analysis": "paired world-level t-test, two-sided alpha=0.05",
           "grid_results": rows,
           "budget": {f"worlds={nw}": budget_table(nw, 3) for nw in grid["n_worlds"]}}
    text = json.dumps(out, indent=1)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text)
    # console summary: worst/median/best power per n_worlds
    for nw in grid["n_worlds"]:
        ps = [r["power"] for r in rows if r["n_worlds"] == nw]
        print(f"N_worlds={nw}: min={min(ps):.2f} median={sorted(ps)[len(ps)//2]:.2f} "
              f"max={max(ps):.2f}  ({len(ps)} cells)")
    print(json.dumps(out["budget"], indent=1))


if __name__ == "__main__":
    main()

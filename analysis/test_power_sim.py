#!/usr/bin/env python3
"""Unit tests for power_sim.py. Run: python3 test_power_sim.py"""
import numpy as np
from power_sim import simulate_power, marginal_rate, solve_mu_for_rate, budget_table


def test_determinism():
    a = simulate_power(40, 0.35, 0.15, 1.0, 0.5, 0.05, 3, 200,
                       np.random.default_rng(7))
    b = simulate_power(40, 0.35, 0.15, 1.0, 0.5, 0.05, 3, 200,
                       np.random.default_rng(7))
    assert a == b, "not deterministic under identical seed"


def test_null_calibration():
    # MME = 0 -> rejection rate should be ~alpha (0.05); MC tolerance for 2000 sims
    p, d = simulate_power(60, 0.35, 0.0, 1.0, 0.5, 0.05, 3, 2000,
                          np.random.default_rng(11))
    assert 0.03 <= p <= 0.07, f"null rejection rate {p} outside [0.03, 0.07]"
    assert abs(d) < 0.01, f"null mean realized diff {d} not ~0"


def test_monotonic_in_n_and_effect():
    rng = np.random.default_rng
    p_small = simulate_power(30, 0.35, 0.15, 1.0, 0.5, 0.05, 3, 600, rng(3))[0]
    p_big = simulate_power(90, 0.35, 0.15, 1.0, 0.5, 0.05, 3, 600, rng(3))[0]
    assert p_big > p_small, "power not increasing in N_worlds"
    p_lo = simulate_power(60, 0.35, 0.08, 1.0, 0.5, 0.05, 3, 600, rng(5))[0]
    p_hi = simulate_power(60, 0.35, 0.20, 1.0, 0.5, 0.05, 3, 600, rng(5))[0]
    assert p_hi > p_lo, "power not increasing in effect size"


def test_rate_solver_inverts():
    gh_x, gh_w = np.polynomial.hermite.hermgauss(40)
    for target in (0.2, 0.35, 0.5, 0.7):
        for s in (0.3, 1.0, 1.8):
            mu = solve_mu_for_rate(target, s, gh_x, gh_w)
            back = marginal_rate(mu, s, gh_x, gh_w)
            assert abs(back - target) < 1e-6, (target, s, back)


def test_realized_diff_matches_mme():
    # the delta solver should deliver ~the target marginal difference before malformed
    # attrition; with f=0 the realized world-level mean diff should be close to MME
    _, d = simulate_power(200, 0.35, 0.15, 1.0, 0.5, 0.0, 3, 400,
                          np.random.default_rng(13))
    assert abs(d - 0.15) < 0.015, f"realized diff {d} deviates from MME 0.15"


def test_budget_arithmetic():
    b = budget_table(60, 3)
    assert b["runs_per_condition"] == 60 * 3 * 3 == 540
    assert b["total_runs"] == 540 * 6 == 3240
    # 540*3 interactive * 45k + 540*3 static * 20k = 105.3M tokens
    assert b["est_tokens_M"] == 105.3
    assert b["est_usd"] == round(105_300_000 / 1000 * 0.008) == 842


if __name__ == "__main__":
    for fn in [test_determinism, test_null_calibration, test_monotonic_in_n_and_effect,
               test_rate_solver_inverts, test_realized_diff_matches_mme,
               test_budget_arithmetic]:
        fn()
        print(f"PASS {fn.__name__}")
    print("all tests pass")

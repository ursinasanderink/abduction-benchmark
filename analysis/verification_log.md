# Verification log

Every load-bearing number in the registration is verified by a process **independent of the one
that produced it**. This file records those checks. Entries are append-only.

---

## 2026-08-04 — Design-sensitivity (power) analysis

**Claim gated:** "N_worlds = 60, k = 3 repeats, 3 models gives ≥ 0.99 power across the full
assumption grid for a 15-percentage-point minimum meaningful effect on the C4-vs-C6 primary
contrast at two-sided α = 0.05, at ≈$1k estimated cost."

**Process independence.** Route A: an analytic noncentral-t power calculation built from a
Gauss-Hermite variance decomposition (`verify_power_sim.py`), modeling the world×model effect as
*shared* between yoked arms — as it is by construction, since a yoked pair lives in the same
world–model cell. Route B: direct Monte-Carlo simulation of the full design (`power_sim.py`). The
effect-size solver (marginal effect → log-odds) was checked separately by a plain 2-million-draw
Monte Carlo, independent of the quadrature. The budget was re-derived by hand.

| Check | Outcome |
|---|---|
| Route A vs Route B, 36 grid cells @ 15pp | max abs. difference **0.0058** |
| Route A vs Route B, 3 deliberately unsaturated cells @ 8pp | ≤ **0.014** (0.858/0.873, 0.804/0.813, 0.724/0.724) |
| Effect-size solver vs independent Monte Carlo | ≤ **2 × 10⁻⁴** |
| Budget arithmetic | exact match by hand |
| Unit tests | **6/6 pass** — determinism under seed, null calibration inside [0.03, 0.07], monotonicity in N and in effect size, rate-solver inversion ≤ 1e-6, realized effect ≈ target, budget arithmetic |

**Assumptions the estimate inherits** (declared, not hidden):

- Pairing correlation between an active run and its yoked twin is taken as **0** given world
  latents. Positive correlation is plausible — informative evidence helps both arms — and would
  make the analysis *conservative*. The calibration pilot estimates it.
- Model-offset spread fixed at ±0.3 log-odds; not varied across the grid.
- Malformed runs scored as failures, applied symmetrically across arms.
- Token and price inputs are assumptions, re-measured in the pilot before the scored run.

**A modeling error this gate caught.** The first draft of the analytic route treated the
world×model random effect as *independent* between the active and yoked arms. It is not — a yoked
pair by construction shares that cell. With the shared-effect correction, the two routes agree to
≤ 0.006. The independent re-derivation earned its cost through its initial divergence, not
through its final agreement.

**Verdict: PASS**, conditional on the published data-generating model in `power_sim.py`. See
registration §3 for the declared worst case (near-perfect within-world correlation, where power at
15pp falls to 0.38–0.45) and the pilot-measured escalation rule that addresses it.

---

## 2026-08-04 — Adversarial review of the registration text

**Process:** a full end-to-end adversarial re-read of the draft registration after several rounds
of layered edits, hunting specifically for over-claims, internal inconsistencies between sections,
post-hoc escape hatches, undefined terms, and analysis steps that could not be executed as
written.

**Findings, all fixed before this record was written:**

1. *(major)* **Yoked-arm computation slack.** The yoked arm does not spend tokens choosing
   interventions, so an equal token budget left it surplus reasoning capacity. Fixed with a
   structured per-step "state what you would want to observe next, then revise" slot, plus
   recording realized per-arm token consumption as a descriptive covariate.
2. *(major)* **An adjudication gray zone.** A "5–15pp suggestive" band would have left a
   significant 12-point result spinnable in either direction. Replaced with the five-class
   adjudication rule.
3. *(major)* **Calibration band exceeded the powered grid.** The informative band was
   [0.15, 0.70] while the power grid covered baseline rates 0.20–0.50. Tightened to [0.20, 0.60]
   and explicitly pinned to the grid.
4. *(minor)* "C4 ≈ C6" was used without definition → now defined as adjudication class (iii).
5. *(minor)* Primary/secondary precedence was ambiguous → precedence rule added (the primary
   contrast adjudicates; secondaries characterize).
6. *(minor)* Yoked round-count inheritance was unstated → "rounds inherited from the paired
   active run" added.
7. *(minor)* A null result was pre-interpreted with wording belonging to a different comparison →
   reworded to the yoked-correct interpretation.

**Residual risks accepted and documented:** the pairing-correlation assumption (above); token and
price inputs pending pilot measurement; the mechanism-equivalence rubric's final wording freezes
with the Phase-2 task materials (checklist box intentionally left open).

**Verdict after fixes:** no remaining over-claims or escape hatches found. The document is
signable once the outstanding §9 checklist items are complete.

---

## 2026-08-04/05 — Prior-art verification

Every claim this project makes about neighbouring work was verified against the source, because
an earlier draft asserted — wrongly — that no published direct test of this kind existed.

| Claim | Status |
|---|---|
| Geng et al. (2505.17968) ran a yoked condition; it underperformed active "across all three black-box types"; the recipient received data "without the verbalization and analysis that are used to construct such data" | **Verified from their §4.3** |
| Samiei et al. (2606.06464) ran a Passive Proposer condition **with humans only**; their LLMs ran active-only | **Verified from full text** |
| Samiei et al. conjunctive object-identification accuracy: proposers 0.12, passive observers 0.45, active explorers 0.69; rule selection 0.57 / 0.69 / 0.82 | **Verified, quotes on file** |
| Samiei et al.'s statement that LLMs "do not consistently gain from choosing their own interventions" is an interpretive remark with **no within-paper LLM comparison** behind it | **Verified** — cited as interpretation, never as a finding |
| CausaLab (2605.26029): 92% task accuracy vs 0.471 all-edge F1 in a six-node observational setting | **Verified** |
| Transition-card benchmark (2605.14033): incumbent/replacement/distractor structure, but no LLM evaluation, no interventions, selection-from-menu rather than formulation | **Verified** — the three differentiators our module must preserve |
| Einstein–Besso 1913 *Entwurf* calculation recovered ~18 of the 43 arcseconds/century | **Verified** |

**Process lesson recorded:** the original novelty sweep searched benchmark and discovery
vocabulary only, and missed directly relevant work filed under "reverse-engineering black-box
systems" and cognitive-science "active exploration." Novelty claims now require searches across
shape-translated vocabularies, citation-chasing from every confirmed neighbour, and an explicit
adversarial pass whose goal is to find the paper that kills the claim. Categorical negatives
("no such work exists") are not used; the strongest permitted phrasing is "not found under the
documented queries."

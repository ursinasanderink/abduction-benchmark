# ABDUCTION-BENCHMARK

**Does choosing an experiment contribute anything beyond the evidence that experiment produces?**

A preregistered experiment testing whether an LLM that *selects its own interventions* recovers
hidden mechanisms better than an identical model that receives **the exact same
intervention–outcome sequence** — online, in the same order, with matched update turns and token
budgets — without having chosen it.

This repository exists so the protocol can be attacked **before** any data exists.

The benchmark is one study inside a larger program — see [`PROGRAM_OVERVIEW.md`](PROGRAM_OVERVIEW.md)
for the questions the program is trying to answer, in order, and where this experiment sits.

---

## Status: pre-registration **signed** (v1.0, 2026-08-18). Nothing has been run.

| | |
|---|---|
| **Registration** | **v1.0 — signed 2026-08-18; citable tag `prereg-v1.0-signed`.** External timestamp deposit pending (reference will be appended to the registration's foot, never edited above the tag) |
| **Data collected** | None |
| **Worlds generated** | None (generation happens *after* model snapshots are locked — see §5) |
| **Results** | None |

**What is in this repository right now:**

- [`PREREGISTRATION.md`](PREREGISTRATION.md) — the full protocol: conditions, primary contrast,
  minimum meaningful effect, five-class adjudication rule, calibration guarantee, decoy worlds and
  balanced representation-shift scoring, contamination ordering, open-materials release lists, and
  the pre-declared interpretation of every outcome class. Everything that remains unchecked in its
  §9 sign-off list either freezes with the Phase-2 task materials or requires the author's
  signature.
- [`analysis/`](analysis/) — the design-sensitivity (power) analysis, its unit tests, and an
  **independent verification implementation** that re-derives the same numbers by a different
  route, plus the verification log.

**What is not here yet** (and is therefore not being claimed):

- the world generator and its grammar specification
- the simulator interface and the active / yoked / passive-proposer harnesses
- the mechanism-description schema and blinded-scoring implementation
- baseline agents, environment lock files, and the scored-instance hash manifest

Those are built in the next phase. When they exist, they appear here **before** the scored run —
that ordering is part of the protocol, not a courtesy.

---

## The design in one paragraph

Three instances of the same locked model snapshot face the same unknown synthetic physics. The
**active chooser** selects interventions and observes their consequences. The **online yoked
recipient** receives that active run's exact intervention–outcome sequence, one step at a time,
with the same number of update opportunities and a matched token budget — but never selects
anything. The **passive proposer** must state which intervention it *would* run before each
result arrives, then receives the active twin's result instead; its proposals are logged, never
executed. Around these sits a 2×2 crossing static versus action-controllable access with the
presence or absence of an explicit abductive protocol, plus a query-only arm that can request
more observations but cannot intervene.

The primary quantity is the paired **world-level** difference in mechanism-recovery rate between
the active and yoked conditions. Models and stochastic repeats are averaged within each world;
they buy precision, and are never counted as additional independent worlds.

At least one third of scored worlds are **Vulcan traps**: an incumbent theory that explains almost
everything, a sparse anomaly, a cheap patch that fits the observed data, and a deeper replacement
mechanism that unifies more — with held-out interventions where patch and replacement disagree.
The model must *formulate* the replacement, not pick it from a menu. The family also contains **concealed decoy worlds** (§4b) in which the cheap patch, a measurement
artifact, or the unchanged incumbent is actually correct — so that "always propose a revolution"
cannot score well. Scoring is two-directional: replacement sensitivity against false-replacement
rate.

## What this is not

- **Not the first active-versus-yoked test.** The paradigm is Markant & Gureckis (2014) in human
  category learning; Geng, Chen, Arumugam & Griffiths (arXiv 2505.17968) brought it to LLMs on
  black-box systems. This is a **replication and extension** whose specific additions are the
  online, computation-matched yoke; an LLM implementation of Samiei et al.'s human
  passive-proposer decomposition (arXiv 2606.06464); and the representation-shift task family.
- **Not a test of whether AI can do science.** A positive result would show that
  hypothesis-dependent control over evidence acquisition improves mechanism recovery under this
  benchmark's operational definition. Nothing more.
- **Not a leaderboard.** The goal is to remove capabilities until one contrast is interpretable —
  the opposite of building the strongest possible agent.

## Motivation

The experiment takes its target from Tom Zahavy's ICML 2026 position paper *"LLMs can't jump"*,
which argues that language models have largely mastered induction and are increasingly capable at
deduction, but lack the mechanism for **abduction** — proposing the new explanatory premise. The
paper attributes the gap to *manipulative abduction* (Magnani): hypothesis formation through
acting on the world rather than rearranging symbols, with action-controllable world models
proposed as the route forward.

That conjecture has a **functional reading** — manipulation means choosing interventions and
integrating their consequences — which is testable, and a **phenomenological reading** —
manipulation requires embodied sensory experience — which no LLM experiment can adjudicate. We
test the functional reading and say so in advance, so that a null result cannot be quietly
redescribed as a failure of embodiment (§6 of the registration).

## Reproducing the power analysis

```bash
pip install numpy scipy
cd analysis
python test_power_sim.py      # 6 unit tests incl. null calibration
python power_sim.py           # 36-cell design-sensitivity grid
python verify_power_sim.py    # independent analytic route + budget re-derivation
```

The headline figure (power ≥ 0.99 across the assumption grid at a 15-point effect) is **stated
only conditionally on the data-generating model in `power_sim.py`**. The known worst case — near
perfect within-world correlation, where power falls to 0.38–0.45 — is declared in the
registration, and a calibration pilot measures the actual correlation before the scored sample
size is fixed.

## How to attack this

Criticism received **before** the scored run will be logged and credited. Useful targets:

- find an intervention-equivalent query that leaks through the query-only condition
- show that the active and yoked prompts differ in some way other than agency
- construct a world that is not identifiable within the permitted action budget
- find an outcome the five-class adjudication rule cannot classify
- show that the representation score would reward sophisticated paraphrase over structural
  replacement
- break the power model

Open an issue, or open a pull request against `PREREGISTRATION.md` with the amendment you think
it needs.

**Governance:** once the registration is signed and timestamped, external contributions cannot
silently alter the definitive protocol. Criticism can produce a **dated amendment before data
collection**, or motivate a subsequent benchmark version. Open source should make the experiment
easier to falsify, not easier to rewrite after the result is known.

## Collaboration

A companion study reconstructs matched historical discoveries **and failures** from primary
process evidence — notebooks, correspondence, dated reading records, intermediate theories,
documented dead ends. Neptune and Vulcan are the founding pair, because the successful case is
unintelligible without its failed twin (same inference, same author, opposite outcomes).

We are looking for **one historian or philosopher of science** to help select defensible cases,
design the coding framework, and separate documented search processes from the heroic narratives
constructed after success. Substantive intellectual contribution means co-authorship. Open an
issue or get in touch.

## Related work

| Work | Relevance |
|---|---|
| Zahavy, *Position: LLMs can't jump* (ICML 2026) | The conjecture under test |
| Markant & Gureckis (2014) | Origin of the selection-vs-reception yoked paradigm |
| Geng, Chen, Arumugam & Griffiths, arXiv 2505.17968 | Active vs passive vs yoked for LLMs on black-box systems |
| Samiei et al., arXiv 2606.06464 | Human passive-proposer decomposition (LLMs ran active-only) |
| CausaLab, arXiv 2605.26029 | Prediction/mechanism dissociation (92% accuracy, 0.471 edge-F1) |
| NewtonBench, arXiv 2510.07172 | Interactive tool access can *hurt* via premature exploitation |
| Lampinen et al., arXiv 2305.16183 | Passive learning of active causal strategies |
| Transition-card benchmark, arXiv 2605.14033 | Theory-transition structure, but no LLM, no interventions, selection not formulation |

## License

Code: MIT. Documents (registration, README): CC BY 4.0.

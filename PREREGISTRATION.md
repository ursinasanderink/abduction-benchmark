# Pre-Registration: ABDUCTION-BENCHMARK — Active vs Online-Yoked Mechanism Discovery

> ## STATUS: v0.6 — awaiting signature and external timestamp. NO DATA COLLECTED.
>
> **Design is complete and frozen pending signature.** This document is published in draft so
> that it can be attacked before it becomes binding. See [README](README.md) for how to file
> criticism.
>
> It becomes binding when the author signs §9 and the document is committed with a signed git
> commit **plus an external immutable timestamp**. The signed version is tagged
> `prereg-v1.0-signed`; that tag — not this file's moving state — is the citable registration.
>
> **v0.6.1 additions (2026-08-06, pre-signature audit — additive only, no condition/endpoint/
> power changes):** yoke-agreement and proposer-agreement rates declared as measured moderators;
> token-role asymmetry named as a bundled mechanism/limitation; trajectory measures declared as
> exploratory log-derived analyses; off-policy/DAgger vocabulary bridge added; response
> literature to the target paper noted (Balani & Panda arXiv 2608.14397; Zheng-Xin 2026;
> Farmer 2026 — all argumentative, none experimental as of signing).
>
> **v0.6 changes (2026-08-05):** the sealed private-archive tier was **split into its own future
> registration** (it is a different study on a different timetable and is not required for this
> experiment); concealed decoy worlds and balanced representation-shift scoring were **integrated
> into §4b** rather than left pending; the open-materials release lists were added (§5b); the
> sample-size rule was restated as *calibration-pilot-determines-final-N*; the applied-domain
> naming rule was relaxed to field level (§8).

**Positioning (binding for all public materials):** this study is *a preregistered replication and
extension of active-versus-yoked hidden-mechanism discovery* (Geng, Chen, Arumugam & Griffiths,
arXiv 2505.17968; paradigm lineage Markant & Gureckis 2014; cf. Samiei et al. arXiv 2606.06464,
CausaLab arXiv 2605.26029, Lampinen et al. arXiv 2305.16183), testing whether **intervention
choice contributes beyond an identical externally generated evidence stream**.

Three contribution claims, each stated at the strength an adversarial prior-art sweep left
standing:

1. **The computation-matched, online-sequential yoke.** Geng et al.'s yoke delivers bulk passive
   observations "without the verbalization and analysis that are used to construct such data"
   (their §4.3); their yoked condition underperformed active "across all three black-box types."
   Our yoke receives the same evidence *online, one step at a time, with matched update turns and
   token budgets.* No other LLM yoke of this form was found under our documented queries.
2. **The passive-proposer arm, ported to LLMs.** Samiei et al.'s Passive Proposer condition ran
   with **humans only** (their LLMs ran active-only). Design credit is theirs; the LLM
   instantiation is ours.
3. **The Vulcan-trap representation-shift module with decoys** (§4b), differentiated from the
   transition-card benchmark (arXiv 2605.14033: incumbent/replacement/distractor structure, but
   no LLM, no interventions, and selection-from-a-menu rather than formulation — **all three
   differentiators must hold in our implementation, especially formulation, never selection**).

It is **not** framed as the first active-versus-yoked test, and **not**, by itself, a decisive
test of whether LLMs can invent new scientific axioms.

**Scope (staged registrations).** This document registers the operational definition and the
factorial simulator experiment, and nothing else. Three companion studies receive **their own
registrations before their own data collection**: a historical-coding study; a protocol-ablation
study; and a **sealed private-archive evaluation tier** drawing on a process-trace archive from a
proprietary applied domain (split out of this document in v0.6 — it is a separate study with a
separate timetable, and this experiment does not depend on it).

## 1. Operational definition of abduction

We measure three separable capacities on held-out tasks, never aggregated into one "abduction
score": **(i) problem representation** (selecting productive anomalies; detecting a wrong
observable basis), **(ii) proposal** (generating candidate mechanisms, including cross-domain
transport), **(iii) evaluation** (ranking, information-gaining intervention choice, discriminating
predictions, post-falsification revision).

Separately, claims about mechanism-recovery capability (public science) are never merged with
claims about downstream research productivity in a proprietary applied domain (private) —
payoff feedback is not epistemic ground truth.

## 2. Experimental conditions

Hidden-mechanism worlds: synthetic, CPU-simulated, generated from a mechanism grammar; each world
admitted only after the §4 identifiability audit. Conditions on identical worlds:

| | No protocol | Abductive protocol |
|---|---|---|
| **Static evidence** | **C1** | **C2** |
| **Action-controllable simulator** | **C4** | **C5** |

plus these controls:

- **C3 — query-only simulator** (separates "interactive tool" from "intervention capability").
  **Allowed queries:** additional observations from the existing passive dataset; correlations,
  summaries, measurements of recorded variables. **Forbidden:** any do(X=x) intervention; any
  request for counterfactual outcomes generated by changing the environment ("what would happen
  if I changed X" is an intervention in disguise). The simulator rejects intervention-equivalent
  queries via an explicit, logged rule; rejections are recorded per run.
- **C6 — online yoked control (primary comparator):** for each C4 run, a second instance of the
  **same model snapshot** receives the *exact evidence sequence that specific C4 run obtained*,
  delivered **sequentially in the same order — never as one bulk transcript** — with the **same
  per-step opportunities to revise its hypothesis, the same token budget, the number of rounds
  inherited from the paired C4 run, and the same final-answer format**. The prompt is identical
  to C4's except the agency instructions, and each C6 step includes a structured "state what you
  would want to observe next, then revise" slot, so the per-step reasoning demand is comparable
  rather than leaving C6 surplus budget from not choosing interventions. **Per-arm realized token
  consumption is recorded and reported as a descriptive covariate**, so any budget asymmetry is
  visible rather than assumed away. Interpretation is fixed in advance: a C4 advantage over C6
  indicates value from *choosing interventions and integrating their consequences beyond
  receiving the resulting evidence* — it is not, by itself, evidence of embodiment or "genuine"
  manipulative abduction.
- **C8 — passive proposer (required):** the model formulates hypotheses and *proposes* its own
  next intervention at each step, but **receives the active twin's intervention and outcome
  instead** (its proposals are logged, never executed). Separates experiment *planning* from
  ownership of the executed experiment and from contingent feedback on one's own choice — and
  controls for the possibility that an active advantage merely reflects the extra reasoning
  involved in producing interventions.
- **C7** *(secondary, budget permitting)* — abstracted-language replication of C1/C4 on a smaller
  confirmatory subset.
- **C9 — oracle-trace yoke** *(optional secondary, budget permitting)*: yoked delivery of an
  intervention sequence selected by a near-optimal scripted policy — upper-bounds the "evidence
  quality" channel.

**Terminology:** yoked arms receive the same **external evidence**, not "the same information" —
the active agent's endogenous reasoning history is part of the treatment, by design.

Interpretable effects: interaction effect (C4−C1), protocol effect (C2−C1, C5−C4),
interaction×protocol (does the protocol help only when the model can act), intervention value
beyond question-asking (C4−C3), planning-without-control (C8−C6), coupling value (C4−C8), and
**the primary contrast below**.

## 3. Primary endpoint and analysis plan

- **Primary outcome (binary):** mechanism recovery = **rubric level 1 or 2** (§4) on held-out
  scoring — a preregistered binary threshold, not a continuous "accuracy" over ordered labels. A
  secondary ordinal analysis of the full five-level rubric uses an ordinal mixed-effects model;
  the five labels are never treated as an interval scale.
- **Primary contrast:** **C4 vs C6** — interactive chooser vs online yoked recipient of identical
  evidence, after a fixed observation budget.
- **Minimum meaningful effect:** **15 percentage points** absolute difference in primary-outcome
  rate (C4 − C6). Scientific justification, not detectability: the conjecture under test holds
  that manipulation is *the* missing mechanism of scientific invention — a mechanism claimed to
  be load-bearing, when ablated, should move mechanism recovery by a large margin; below ~15pp
  the substrate-necessity claim loses practical force (a prompting or scaffolding change could
  plausibly compensate).
- **Adjudication rule (five classes with competence floor):** the primary test is the two-sided
  α=0.05 test of the C4−C6 difference. **Competence floor:** classes (i)–(iii) can be claimed
  only if pooled performance sits inside the §3b informative band; if both arms are below floor,
  the result is class (v-a) *uninformative about the substrate claim* and triggers §3b
  re-laddering — a 5%-vs-5% tie is a too-hard task, never "the symbolic channel suffices."
  - (i) significant AND point estimate ≥ 15pp AND floor met → **supports** intervention choice as
    load-bearing;
  - (ii) significant, in (0, 15pp), floor met → **contributes but not load-bearing**;
  - (iii) **equivalence established by a formal TOST at margin ±15pp** (not mere
    failure-to-reject) AND both arms above floor AND equivalence holds on *mechanism recovery*,
    not merely prediction → **action selection unnecessary at this task level**;
  - (iv) significant negative → the pre-declared agentic-cost interpretation (§6);
  - (v-b) **prediction succeeds while mechanism recovery fails** (rubric level 4 dominant; the
    CausaLab dissociation — 92% task accuracy vs 0.471 edge-F1 in their observational setting) →
    reported as shortcut/predictive-approximation, never as discovery.

  "C4 ≈ C6" everywhere in this document means class (iii). No result is reported under a label
  other than its class.
- **Design:** **N_worlds = 60** to start, **k = 3 repeats per cell, 3 models** (2 frontier API +
  1 open-weight). Design-sensitivity result (`analysis/power_sim.py`, seed 20260804, 500
  sims/cell; grid = baseline rate {0.20, 0.35, 0.50} × world-effect SD {0.5, 1.0, 1.5} ×
  world×model SD {0.25, 0.5} × malformed rate {0.05, 0.15}): power ≥ 0.99 in every one of the 36
  grid cells at 15pp; minimum detectable effect at ≥80% power is ≈10pp even under pessimistic
  cells (≈8pp at the plausible middle). Full grid in `analysis/power_grid_results.json`.
  **This power claim is conditional on the published data-generating model — see the worst case
  below.** Budget: ≈3,780 runs, ≈121M tokens, ≈$1,115 including a 15% pilot under recorded
  token/price assumptions; 2× token-overrun sensitivity ≈ $2,230. If pilot token counts run high,
  C9 (optional) is dropped first, then C7, before any reduction in N_worlds.
- **Power worst case + escalation rule:** the ≥0.99 figure depends on within-world replication
  (3 models × 3 seeds pooled into a per-world proportion; **the unit of independence is the
  world, df = 59; models and seeds are within-world replicates and are never counted as
  additional worlds**). The uncovered extreme is near-perfect within-world correlation, where
  the design degenerates to one paired binary per world and power at 15pp falls to **0.38–0.45**.
  Therefore: a calibration pilot, completed **before any scored outcome is observed**, measures
  the within-world correlation; if the measured intraclass correlation implies effective
  information below the grid's σ_wm ≤ 0.5 assumption, N_worlds escalates along a pre-declared
  schedule (60 → 90 → 120) keyed **only to the measured correlation and pilot cost data, never to
  outcome differences**. Once selected, the scored sample size is fixed.
- **Verification:** the power analysis passed an independent verification gate — an analytic
  route (noncentral-t via quadrature variance decomposition, modeling the shared world×model
  effect between yoked arms) agrees with the Monte-Carlo to ≤0.006 across the grid and ≤0.014 at
  deliberately unsaturated cells; the effect-size solver was verified by independent plain Monte
  Carlo to ≤2e-4; the budget was re-derived by hand. Record: `analysis/verification_log.md`.
  **Declared assumptions the estimates inherit:** pairing correlation between a C4 run and its
  yoked C6 run is taken as 0 given world latents — positive correlation (plausible: informative
  evidence helps both) makes the analysis conservative; the pilot estimates this correlation.
  Power is computed on the paired world-level summary analysis, the balanced-design equivalent of
  the mixed model for this contrast; the confirmatory analysis remains the mixed-effects logistic
  model.
- **Statistical model:** mixed-effects logistic regression; random intercept per world (and per
  world×model), model identity as a covariate; runs are never treated as independent across the
  same world.
- **Stochastic output:** fixed sampling parameters (§5); k repeats per cell; per-cell success =
  mean over repeats; sensitivity analysis at temperature 0 where supported.
- **Multiple comparisons:** the primary contrast is tested alone; all secondary contrasts
  Holm-corrected within the secondary family.
- **Malformed output / failed tool calls:** a run with an unusable final answer scores as failure
  in the primary analysis; a pre-declared sensitivity analysis excludes such runs; retry policy:
  one format-only retry, never a content retry.
- **Stopping rule:** fixed-n design after the calibration pilot; no interim looks that can stop
  or extend data collection.
- **Pilot worlds are excluded from the final evaluation set.**

- **Declared moderators (v0.6.1, measured from existing logs — no new conditions):**
  (a) **yoke-agreement rate** — per step, whether C6's stated desired next observation matches the
  intervention its active twin actually executed; reported as a moderator of the primary contrast
  (predicted direction: the C4−C6 effect is larger on low-agreement worlds, where the yoke
  received evidence it would not have sought); (b) **proposer-agreement rate** — the C8 analog
  over logged proposals, which directly quantifies how "foreign" the received experiments were.
  Both use material the arms already produce; declaring them now prevents their later use from
  being post hoc.
- **Exploratory log-derived analyses (v0.6.1, labeled exploratory in all reporting):** trajectory
  measures over per-step hypothesis states — the round at which the correct mechanism (rubric
  level 1–2) first appears in any arm's candidate set, and the "held-then-abandoned" rate
  (correct mechanism appears and is later dropped; cf. premature stopping in interactive causal
  discovery). No confirmatory claims attach to these.

## 3b. Calibration and informativeness guarantee

The primary contrast is informative in several pre-declared directions (§6); the only
uninformative outcome is a *calibration* failure — uniform floor or ceiling across arms. To
guarantee the scored run cannot land there while preserving inference:

1. **Pre-scored calibration pilots** (retired worlds) must place pooled-arm performance inside
   the declared informative band: pooled primary-outcome rate in **[0.20, 0.60]** — chosen to lie
   inside the powered assumption grid — and neither floor (<0.05) nor ceiling (>0.90) in any
   single arm.
2. If calibration lands outside the band, **task difficulty moves along the pre-defined
   generator-grammar ladder** (mechanism depth, observable count, noise level) and calibration
   repeats. Ladder moves are made **blind to between-condition differences**: the calibration
   report shows pooled rates only, with condition labels withheld from the decision-maker.
3. Once the band is hit, the scored run executes at **fixed n with no outcome-contingent
   extension**.
4. If the scored run nonetheless produces uniform floor/ceiling (calibration drift), that is
   reported as a calibration failure, the tier is re-laddered, and a **new registration addendum**
   (dated, referencing this one) governs the re-run. Extension without a new addendum is
   prohibited.

## 4. World admissibility and scoring

**Identifiability audit (world admission gate):** before entering the test set, each world is
classified — (a) uniquely identifiable within the permitted intervention budget; (b) identifiable
up to an equivalence class; (c) not identifiable from available evidence. Only (a) and (b) enter
the primary evaluation ((b) scored against the equivalence class); (c) worlds are excluded or used
deliberately as calibration items, labeled as such.

**Mechanism-recovery rubric (frozen with the task materials, before the run):**

1. exact recovery of the generating mechanism;
2. recovery of a mathematically/causally equivalent mechanism;
3. partial structural recovery;
4. predictively adequate but mechanistically different explanation;
5. incorrect.

Levels 1–2 = primary success; the full distribution is reported. The rubric exists so the
benchmark does not penalize legitimate abduction for failing to match the simulator's syntax.

**Secondary outcomes:** ranking among alternatives; information-gain quality of chosen
interventions; discriminating predictions on withheld data; post-falsification revision; transfer
to a related environment.

## 4b. Vulcan-trap representation-shift module (required task family)

A declared fraction (≥ one third) of scored worlds are **Vulcan-trap worlds**, each containing:
(1) an **incumbent theory** (given to the model) that explains nearly all observations;
(2) a **sparse anomaly** the incumbent mispredicts; (3) a **cheap patch** — an incumbent
modification (extra term/entity) that fits the observed evidence; (4) a **deeper replacement
mechanism** that explains the anomaly *and* unifies additional phenomena the incumbent treated as
separate; (5) **held-out interventions on which patch and replacement diverge**.

Success requires *formulating the replacement representation* in a structured mechanism language
expressive enough to describe theories outside the incumbent family — **not** selecting from a
supplied menu, and not fitting coefficients within the incumbent's form.

This module is what connects the paradigm to the axiom-replacement claim in "LLMs can't jump."
Plain hidden-law recovery is describable as active learning / system identification, and is
labeled as such; only the Vulcan-trap module speaks to representation change.

Generator-grammar details freeze with the Phase-2 task-materials registration.

**Concealed decoys (integrated in v0.6 — required).** A benchmark containing only
replacement-warranted worlds has a fatal shortcut: a model that learns "whenever the incumbent
misses, propose a deeper ontology" scores well without abducting anything. That is performative
contrarianism. The scored representation-shift family therefore contains concealed decoys, and
the model is never told which family it faces:

| World family | Correct response |
|---|---|
| True replacement ("Vulcan") | formulate the deeper replacement mechanism |
| Patch-correct ("Neptune") | adopt the local patch / hidden entity — replacement is *wrong* here |
| Incumbent-correct | retain the incumbent; the anomaly is sampling variation |
| Measurement artifact | attribute the discrepancy to the measurement process |

**Endpoint (named secondary): balanced representation-shift accuracy** — *replacement
sensitivity* (changing representation when a change is required) reported against
*false-replacement rate* (staging a revolution when a patch, measurement account, or unchanged
incumbent is correct), per condition. The balanced combination is reported, never the raw rate of
novel-theory proposals. Neptune and Vulcan are the historical reason this control exists: the same
inference was correct once and wrong once.

Generator-grammar details freeze with the Phase-2 task-materials registration.

## 5b. Open materials — what is released, and when

**Before the scored run**, the public repository contains: the simulator interface; the active,
online-yoked and passive-proposer harnesses; toy and retired development worlds; the mechanism
schema; the blinded-scoring procedure; the power-analysis code and sensitivity grid; environment
lock files; baseline agents; the test suite; and a timestamped hash manifest of the generator,
scored instances and seeds.

**Sealed until the definitive run:** the scored worlds, their hidden mechanisms, the random seeds
and the test-instance mappings. Releasing them earlier would convert the benchmark into a
prompt-development exercise against its own holdout.

**After the definitive run**, the repository adds: the complete generator; all scored worlds; raw
model trajectories including malformed outputs and failed tool calls; adjudication records; model
configurations; and scripts that reproduce every reported table and figure.

**Governance.** The signed registration is tagged and immutable. External criticism can produce a
**dated amendment before data collection**, or motivate a subsequent benchmark version; it cannot
silently alter the definitive protocol after results exist. Open materials should make the
experiment easier to falsify, not easier to rewrite.

## 5. Execution-environment freeze (recorded before the definitive run)

Exact model + snapshot identifiers and access dates · system prompts · tool descriptions and
interface schemas · temperature/sampling parameters · token and action budgets · repeats/seeds ·
retry policy · context-window policy · whether reasoning traces are requested · browsing and
external tools disabled · **API data-retention settings (zero-retention or equivalent where
available, recorded per provider)** · open-weight checkpoint hash · simulator code hash ·
world-generator version + random seeds. A model name alone is not a reproducibility guarantee; if
a provider snapshot is silently changed mid-run, the run restarts on a fixed snapshot, or the
change is documented and the affected cells re-collected.

**Contamination ordering:** the supportable claim is — *the exact scored worlds were generated
after the evaluated model snapshots were locked, and kept sealed until evaluation.* Enforcement:
(1) model snapshots + prompts locked and hashed FIRST; (2) scored worlds generated only after that
lock, with meaningless variable/object names and structural transformations + counterfactual laws
(never renamed familiar equations alone); (3) scored instances and seeds stay private until after
evaluation, with hashes of generator, instances, and seeds externally timestamped at generation;
(4) at least one frozen open-weight model whose release predates world generation; (5) web access,
retrieval, and persistent memory disabled in all runs; (6) generator protocol published before the
run, scored worlds released after evaluation.

"Not in the training corpus" is never claimed on surface-form novelty alone — a fresh equation can
instantiate a template seen thousands of times. The claim is the ordering above, nothing stronger.

## 6. Author-supplied criteria — secondary by rule

The present protocol remains the primary pre-registration. The author of "LLMs can't jump" (ICML
2026) will be asked, after this document is timestamped: *"If the active and yoked models both
achieve high absolute performance and are statistically equivalent, would that count as evidence
against the necessity of manipulative action for abduction at this task level? If not, what
observable result would?"*

Any criterion supplied **before data collection** is added as a dated, author-attributed
**secondary** analysis; nothing supplied later alters the primary test. Declared in advance:

- **Evidence against the conjecture:** C4 ≈ C6 (class iii) and C4 ≈ C1–C3 on the primary outcome
  while performance is above the calibration floor; or static-only arms solving
  representation-change tasks at rates comparable to interactive arms.
- **Evidence for:** C4 > C6 per §3 adjudication class (i). **Precedence rule:** the primary
  contrast alone adjudicates the manipulation mechanism; the C4-vs-C1/C2/C3 comparisons
  (Holm-corrected secondaries) characterize *which access component* carries any effect and
  whether the protocol substitutes for action — they qualify the story, never overturn the
  primary classification.
- **C4 < C6 is a live, interpretable outcome (pre-declared):** NewtonBench documented a
  "paradoxical tool effect" in which interactive tool access *hurt* capable models via premature
  exploitation. A C4 < C6 result here would localize that harm to intervention *selection*
  specifically (the yoked recipient sees identical evidence without choosing it), with C5-vs-C4
  testing whether an explicit protocol repairs it. This is evidence about the cost of agency, not
  a failed experiment, and will be reported as such.
- **Ambiguous (will not be spun):** uniform failure (task too hard — re-ladder per §3b) or
  uniform success (too easy — re-ladder per §3b) across arms.

**Bundled mechanisms within the functional reading (v0.6.1, declared):** a C4 advantage over C6
is attributable to *choosing and integrating one's own interventions* as a package. Two components
of that package are named here because they cannot be separated by this design: (i) an
**off-policy/covariate-shift component** — the yoke updates on evidence generated under another
agent's evolving hypothesis, the structure formalized in imitation learning (cf. DAgger): the
received sequence may be uninformative *relative to the yoke's own current hypothesis* even though
it was informative for the chooser; (ii) a **token-role component** — part of the active arm's
evidence trail exists as its own generated tokens while the yoke receives equivalent content as
provided input, and matched token budgets do not equalize how models process self-generated versus
received context. Both components are *part of* what "intervention choice" means operationally
here; disentangling them is future work, and no result will be reported as excluding them.

**Construct disjunction (binding for interpretation):** Magnani's manipulative abduction is
defined through action on *external epistemic mediators* ("thinking through doing"; action
providing otherwise-unavailable information) — which C4 instantiates directly; Einstein's
elevator, an internal thought experiment, is in Magnani's own taxonomy closer to model-based
abduction. Two readings are therefore declared in advance:

- **Reading 1 (functional):** "manipulation" = choosing interventions and integrating their
  consequences. The C4-vs-C6 contrast tests this reading directly, in either direction.
- **Reading 2 (phenomenological):** "manipulation" requires embodied sensory experience. No
  LLM-side experiment (including ours) can bear on this reading; if the conjecture's defense
  retreats to Reading 2 after a Reading-1 null, that is a statement about the claim's
  falsifiability, not about the models.

Results will be interpreted against Reading 1; the existence of Reading 2 is stated here so that
it cannot function as a post-hoc escape route — for either side.

## 7. Separate sealed tier (split out in v0.6)

A sealed evaluation tier drawing on a private process-trace archive from a proprietary applied
domain **is not registered here**. It is a separate study with its own timetable and receives its
own registration before its own data collection. Nothing in the present experiment depends on it.

Its governing principles, recorded here so that the later registration cannot quietly weaken
them: cases are tagged *outcome-known / mechanism-known / process-known* and only the tagged
competency is scorable, since a decision can succeed for the wrong stated reason; an exposure log
records every case that has entered any model context before sealing, and exposed cases become
development data; the model family in whose sessions the archive was authored counts as
development-exposed for that tier; grading is blinded to condition and model.

## 8. Information boundary

The applied track in the proprietary domain produces **no publications**; its output is an
internal working product. Public materials may name the *field* of that applied work, but not the
archive contents, the specific program, its methods or its results.

## 9. Sign-off checklist

**Design — complete.**
[x] static-plus-protocol arm (C2) · [x] online yoked control (C6) with full yoking spec ·
[x] passive-proposer arm (C8) · [x] query-only arm (C3) with allowed/forbidden query rules ·
[x] primary endpoint and primary contrast specified (binary, C4-vs-C6) · [x] minimum meaningful
effect defined and justified (15pp) · [x] five-class adjudication rule with competence floor and
formal equivalence test · [x] design-sensitivity analysis completed and independently verified,
with the worst case declared · [x] calibration-pilot-determines-final-N rule · [x] world
identifiability audit procedure · [x] mechanism-recovery rubric (five levels) · [x] **decoy
worlds and balanced representation-shift scoring (§4b)** · [x] contamination ordering (§5) ·
[x] open-materials release lists and governance rule (§5b) · [x] construct disjunction and the
C4<C6 interpretation pre-declared (§6) · [x] author-supplied criterion designated secondary (§6) ·
[x] public redaction pass.

**Freezes with the Phase-2 task materials** (own registration, before any world is generated):
[ ] generator grammar · [ ] mechanism-language schema · [ ] final rubric wording ·
[ ] model snapshots, prompts, sampling parameters, seeds and retry policy · [ ] data-retention
settings recorded per provider · [ ] simulator and generator code hashes.

**Remaining before this registration binds — author action only:**
[ ] **signature below** · [ ] **external immutable timestamp** (deposit of this file's hash;
tag `prereg-v1.0-signed`).

---

Signature: ______________  Date: __________

Signed commit hash: *(filled on signing)* · External timestamp reference: *(filled on deposit)*

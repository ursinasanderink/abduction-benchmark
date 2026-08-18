# Abduction Atlas — Coding Manual v0

**Status:** v0 (2026-08-18; rev. 2026-08-19 per PR-1 v0.2: Lin 2007 ninth response; α value handling; segmentation-audit and hindsight-defence procedures cross-referenced), pre-pilot. Governed by [`../PREREG_ATLAS.md`](../PREREG_ATLAS.md) (PR-1).
Revised after pilots 1–2 (v0.2), validated on pilot 3 (Krebs/KEKADA), then **frozen as v1** — after
which no category engineering; defects found later are reported, not fixed mid-study. Every
category carries its source tag (literature-forced LF# / our proposal OP# per PR-1 §4). Examples are
drawn from cases **outside** the corpus (Semmelweis, Snow, Fleming, Kepler, Faraday, Michelson–
Morley) so the manual does not pre-code the corpus.

## 0. Unit, identifiers, tiers, and the "unknown" rule

- **Move** = a dated, sourced episode of ≤ 1 paragraph in which the actor does one codable thing
  (notices, proposes, tests, revises, abandons, communicates). One move may carry codes in several
  layers; it never spans two dates unless the source itself does.
- **Move id** `SET-CASE-NNN` (e.g. `S1-NEP-007`); fields: `date` (ISO or best-known range),
  `source` (edition/page/URL), `tier`, `text` (≤ 1 paragraph, quoted or closely paraphrased),
  then the layer codes.
- **Source tiers:** **T1** contemporaneous (notebook, letter, dated manuscript, lab record);
  **T2** near-contemporaneous (publication ≤ 2 years after the move; testimony ≤ 5 years);
  **T3** retrospective (memoir, later interview, secondary reconstruction). Layer-S fields are
  coded from T1/T2 only unless flagged `S_from_T3: true`; every T3-only datum is flagged.
- **`unknown` is a value, not a blank.** Every categorical field accepts `unknown`; the per-field
  count of unknowns is reported as data (PR-1 §5(i)). Do not infer what the source does not
  show; do record that it does not show it.
- **Coder-independence:** you code from the dossier alone. Do not consult other coders' files,
  the KEKADA papers (set 8), or the program's synthesis while coding. Independent coders receive
  episodes under **neutral IDs**, one episode at a time (never paired dossiers), without the A2
  directional hypothesis (PR-1 §7 hindsight defence).
- **Dossier construction** is itself audited: for ≥ 25% of public episodes two builders extract
  moves independently from the same raw sources before any category is applied; the dossier is the
  reconciled union (PR-1 §7 event-segmentation audit).
- **How codes enter reliability:** each category is scored per move present/absent; `unknown` is a
  distinct code (α reported with and without it); `not-applicable` (e.g. A-TYPE when A-TRIGGER ≠
  anomaly) is excluded from that category's α (PR-1 §7).

---

## 1. Layer L1a — Representation in use / change *(LF1)*

**R-MEDIUM** — the representational medium in which the actor is working at this move.
Values: `symbolic` (equations, formal notation), `verbal` (natural-language theory), `diagrammatic`
(drawings, maps, graphs), `physical-model` (mechanical/analog model), `apparatus` (working with an
instrument), `unknown`. Include: the medium evidenced in the source for *this* move. Exclude: the
actor's general habits. (+) Snow's 1854 dot map → `diagrammatic`. (−) A later biographer's remark
that Snow "thought spatially" → not evidence for a given move; `unknown` unless the move's source
shows it. *Sources: Nersessian; Cheng & Simon; Gooding.*

**R-CHANGE** — degree of representation change *this move introduces* (ordinal; collapsed from
Thagard's nine degrees). `0 none` (works within the current representation); `1 additive` (adds an
instance, a rule, a part/kind relation inside the existing hierarchy); `2 conceptual` (introduces a
new concept or reorganizes part of a hierarchy); `3 revolutionary` (branch jumping — an entity moved
to a different branch; or tree switching — the organizing principle replaced); `unknown`.
(+) Semmelweis proposing "cadaverous particles" carried on hands as the cause → `2 conceptual` (a
new causal entity within the existing medical ontology). (+) Lavoisier removing phlogiston and
re-describing combustion as combination with oxygen → `3 revolutionary` (tree switching).
(−) Fitting a new coefficient in an existing law → `0`. Code the *move*, not the eventual theory.

**R-TRIGGER** — was the representation change (R-CHANGE ≥ 2) triggered by an expectation-violating
event evidenced in the source? `yes` / `no` (change made without a documented violation) /
`unknown` / `n/a` (R-CHANGE < 2). *Source: Schunn & Klahr.*

## 2. Layer L1b — Anomaly intake and response *(LF1, OP1)*

**A-TRIGGER** — what prompted the move. `novelty` (a phenomenon the current theory neither
predicts nor forbids — Aliseda); `anomaly` (the current theory predicts otherwise — Aliseda);
`theory-inconsistency` (two accepted theories/commitments conflict; no new datum); `goal-
inexpressibility` (the current representation cannot state the goal/objective the actor wants —
OP1); `none` (routine continuation); `unknown`. (+) Michelson–Morley null result for an ether
theorist → `anomaly`. (+) Einstein 1907 tension between special relativity and instantaneous
Newtonian gravity → `theory-inconsistency`. (+) Fleming noticing the clear zone around the mould →
`novelty` (nothing predicted it either way). (−) A planned next experiment in a series → `none`.

**A-PRIOR** — did the actor hold a documented expectation *before* the observation? `stated`
(written expectation in T1/T2), `implied` (procedure only makes sense given an expectation),
`none`, `unknown`. *Source: KEKADA expectation-setters.* (+) Kepler's Mars work presupposing circular
orbits with documented predicted positions → `stated`.

**A-TYPE** — kind of anomaly (only if A-TRIGGER = `anomaly`). `monster` (a single odd case the
actor treats as not the theory's business), `model` (the theory's model of the phenomenon is
wrong in a part), `special-case` (holds except under specified conditions), `indicative-entity`
(the anomaly points to a missing entity), `indicative-role` (points to a wrong role/activity of a
known entity), `unknown`. *Sources: Darden 2006 ch.10; Craver & Darden 2013 ch.9.* (+) Uranus's
residual read as pointing to an unseen body → `indicative-entity`. (−) Do not code A-TYPE from
what the anomaly *turned out* to be; code the actor's evidenced reading at the move.

**A-RESPONSE** — the actor's response to the anomalous datum at this move (Chinn & Brewer
1993/1998; Lin 2007; exhaustive, one per move — multi-stage responses are coded as successive
moves). `ignore` (no engagement recorded despite documented awareness), `reject-data` (datum
treated as invalid), `uncertainty-of-data` (validity of the datum questioned, held open),
`uncertainty-of-interpretation` (datum accepted as valid but its meaning for the theory left
undecided — Lin 2007), `exclude` (datum placed outside the theory's domain), `abeyance` (accepted as valid, held
for later, theory unchanged), `reinterpret` (datum re-described so the theory stands, no change to
theory), `peripheral-change` (datum accepted; theory changed in a non-core part), `theory-change`
(core theory changed, possibly toward a rival), `unknown`. (+) Kelvin dismissing X-ray reports as
a hoax (per Chinn & Brewer) → `reject-data`. (+) Ptolemaic epicycle added to save the model →
`peripheral-change`. (−) Do not code `ignore` merely because the source is silent — that is
`unknown`; `ignore` requires evidence the actor knew of the datum.

**A-ATTENTION** — timing × centrality (Dunbar): `early-core`, `early-noncore`, `late`, `unknown`;
plus **A-ATTENDED** `yes/no/unknown`. "Early" = within the first third of the episode's dated span;
"core" = bears on the episode's declared central hypothesis. Episode span is set in the dossier
header before coding.

**A-IGNORED (episode-level list)** — anomalies documented as available to the actor at the
episode's dates (from the dossier's secondary literature) that receive no coded move; each with
source and tier. Audit-forced (PR-1 §5(ii)). If none can be established: `unknown`, not empty.

## 3. Layer L2 — Proposal policy *(LF2)*

Code one primary L2 category per proposing move (a move that generates or modifies a candidate
explanation/mechanism); secondary categories allowed with `secondary:` prefix. Then tag
**P-MODE** `selective` (chooses among candidates already available in the actor's repertoire) /
`creative` (introduces a candidate not previously in the repertoire, per the source) / `unknown`
(Magnani; Schurz).

**TRANSPORT** — bringing structure in from elsewhere.
- `analogy` + **P-DISTANCE** `within` (same system/organism/domain), `near` (neighbouring domain),
  `far` (unrelated domain), `unknown` (Dunbar). (+) Semmelweis linking Kolletschka's death from a
  scalpel wound to the ward mortality → `analogy/near`. (−) A rhetorical comparison in a lecture
  that generates no candidate → not a proposing move.
- `theory-type / schema-instantiation` — instantiating a known type of theory or mechanism schema
  in a new domain (Darden 1991 15-1 item 2; Craver & Darden). (+) Applying "germ theory" schema to
  puerperal fever.
- `interfield` — connecting two fields' theories (Darden 15-1 item 3). (+) Chromosome mechanics
  brought into breeding-ratio theory.
- `generic-abstraction` — abstracting the shared structure of source and target then transferring
  it (Nersessian). Requires evidence of the abstraction step, not just the analogy.
- `level-shift` — moving to another level of organization (Darden 15-1 item 4). (+) From organism
  to cell to explain a trait.

**IDENTIFICATION** — narrowing where the answer is.
- `localization / decomposition` — decomposing the system and locating the operation in a part
  (Bechtel & Richardson). (+) Attributing fermentation to a component of the cell (zymase).
- `scope-determination` — asking whether the phenomenon is specific or general before explaining
  it (KEKADA). (+) "Does every acid do this, or only this one?" as a documented next step.
- `delineate-and-alter` — listing the theory's separable assumptions and altering one (Darden).
- `propose-the-opposite` — negating an assumption and exploring the consequence (Darden).
- `specialize-and-add` — adding a special condition or component to cover the case (Darden).
- `uncover-implicit-assumption` (Darden). `extend-scope` — applying an existing hypothesis to new
  cases (Darden).
- `factual/existential-abduction` — positing an unobserved fact or entity of a known kind (Schurz;
  *provisional tag*). (+) "There must be another planet" → `factual/existential-abduction`.

**ASSEMBLY** — building the candidate from parts.
- `modular-subassembly` — combining known modules (Darden 2002). `forward-chaining` /
  `backward-chaining` — reasoning from known early stages forward, or from the end state
  backward (Darden 2002; Craver & Darden). `conceptual-combination` — joining two concepts into a
  new one (Thagard). `simplify-then-complicate` — start with an idealized version and add
  (Darden 15-1 item 6). `vague-then-refine` — successive refinement of a vague idea (item 7).

**MANIPULATIVE** — hypothesis-making by acting on an external epistemic mediator (Magnani; Gooding).
- `experiment-to-provoke` — an intervention made to *introduce* an inconsistency or reveal a
  hidden constraint, not to test a formed hypothesis. (+) Faraday moving the wire around the magnet
  to see what happens (Gooding's construals). (−) A test of a stated prediction → L3, not here.
- `external-model-building` — constructing a physical/diagrammatic model and reading the
  candidate off it. `action-under-incomplete-info` — acting to obtain data before any candidate
  exists. `sense-control` — instrument/prosthesis used to change what is observable.

## 4. Layer L3 — Evaluation policy *(LF3, OP2)*

Code on moves that rank, choose a test, respond to a test outcome, or abandon.

**E-CRITERIA** — assessment criteria the actor is documented as invoking (multi-select from
Darden 15-2): `internal-consistency`, `systematicity/modularity`, `clarity`, `explanatory-adequacy`,
`predictive-adequacy`, `scope/generality`, `lack-of-ad-hocness`, `extendability/fruitfulness`,
`relation-to-accepted-theories`, `metaphysical/methodological-constraint`, `relation-to-rivals`,
`unknown`. Only code criteria the source shows being used.

**E-TESTORDER** — the rule by which the next test was chosen, where evidenced (Peirce economy):
`cheapness`, `caution-one-component` (test one separable component at a time), `breadth`
(test what would settle the most), `refutability-first` (test what would kill the hypothesis
fastest), `intrinsic-plausibility`, `other` (free text), `unknown`.

**E-EXPT** — experiment-choice heuristic: `discriminating` (chosen to separate two live
candidates — Klahr, Fay & Dunbar), `examination` (probe a single hypothesis), `risk-regulation`
(complexity of the test adjusted to confidence — Schunn & Klahr), `complexity-management`,
`replication`, `unknown`.

**E-CONFIDENCE** — which of Josephson's six factors the actor's stated confidence references
(checklist, multi-select): `decisiveness-over-alternatives`, `goodness-alone`, `data-reliability`,
`search-thoroughness`, `cost-of-error`, `need-to-decide-now`, `none-stated`.

**E-OUTCOME-RESPONSE** — response to the outcome of a *predicted* test (use A-RESPONSE when the
datum arrived unpredicted): `revise`, `patch`, `abandon`, `ignore`, `hold`, `unknown`.

**E-KILL** (OP2) — was the test's kill condition stated before the test? `pre-declared` /
`post-hoc` / `none` / `unknown`; and **E-BUDGET** — evidence of a bounded budget of tests/resources
`yes/no/unknown`.

**Episode-level:** **E-TEMPORAL** — does the episode show the confirm-early / disconfirm-late
pattern (Tweney)? `yes/no/unknown` with the move ids that show it. **E-DISTRIBUTED** — were
candidates limited/expanded/replaced/discarded by interlocutors (Dunbar)? `yes/no/unknown` with
names.

## 5. Layer S — Sequence *(LF4, LF5, LF8; audit-forced fields)*

Per move (from T1/T2 unless flagged):
- **S-TRIGGER** — the move id or dated event that immediately prompted this move; `unknown`.
- **S-PRIOR** — prior expectation at this move (`stated/implied/none/unknown`; duplicates A-PRIOR
  where the move is an intake).
- **S-ALT** — alternatives evidenced as considered at this move (list; `none-evidenced`;
  `unknown`).
- **S-RULE** — the decision rule applied, free text ≤ 1 sentence + tag: `anomaly-type→redesign`
  (the kind of anomaly drove the kind of fix — Craver & Darden), `attention-rule` (Dunbar),
  `economy` (a Peirce test-order rule), `criteria` (an E-CRITERIA item decided it), `authority/
  social` (an interlocutor decided it), `other`, `unknown`.
- **S-OUTCOME** — what happened (≤ 1 sentence). **S-NEXT** — the move id that follows.
- **S-GOALSHIFT** — did the actor drop the current goal/agenda item and take up a new one? `yes/no/
  unknown` (KEKADA). **S-BACKTRACK** — return to an earlier abandoned candidate `yes/no`.
  **S-ABANDON** — candidate abandoned at this move `yes/no`. **S-ESCALATE** — the actor moved to
  a more radical class of change after lesser ones failed (Darden 1991 discussion of abandoning the
  theory / shelving the anomaly; Craver & Darden 2013) `yes/no/unknown`.
- **S-DT** — elapsed time since previous move (days; `unknown`). **S-COST** — resource cost of the
  move where evidenced `cheap/expensive/unknown` (Peirce). **S-WHO** — interlocutors named.

Per episode: **S-ENTRY** `theorist` (starts by searching memory/theory) / `experimenter` (starts by
generating data) / `unknown` (Klahr & Dunbar); **S-STRATEGY** — Paavola strategy tags evidenced
across the episode (multi-select: `search-anomalies`, `observe-clues`, `keep-hypothesising`,
`fix-kind-of-explanation`, `explainable-explanations`, `seek-unity`, `attend-to-phases`) — LF8;
**S-MEDIUM** record medium (`notebook`, `letters`, `publications`, `lab-records`, `digital-trace`)
— Tweney; **S-SOCIAL** `individual/distributed`.

## 6. Ambiguity log and manual revision

Every judgment call goes to `AMBIGUITY_LOG.md` (move id, field, options considered, choice, reason).
Pilot revisions are driven by this log only. After MANUAL_v1_FROZEN, ambiguities are logged, never
resolved by changing categories.

## 7. Worked mini-example (out-of-corpus: Semmelweis, 1847)

`SX-SEM-004` — date 1847-03 (T2, Semmelweis 1861 account of Kolletschka's death, corroborated by
contemporaries) — *text:* on learning that Kolletschka died with pathology matching puerperal
fever after a scalpel wound during autopsy, Semmelweis proposes that "cadaverous particles" carried
on the hands of physicians from the autopsy room cause the fever. — L1b: A-TRIGGER `analogy-prompted
novelty`? → code `novelty` (the death is a new datum, not predicted by miasma either way) with
A-RESPONSE `theory-change` for the miasma account; L1a: R-CHANGE `2 conceptual` (new causal
entity), R-TRIGGER `yes`; L2: primary `analogy/near`, secondary `factual/existential-abduction`,
P-MODE `creative`; L3: E-TESTORDER `refutability-first` (the chlorine hand-wash trial follows) —
code on the *next* move, not this one; S: S-TRIGGER = news of Kolletschka's death (event),
S-PRIOR `none`, S-ALT `none-evidenced`, S-RULE "the two pathologies matched" tag `other`,
S-GOALSHIFT `yes`, S-NEXT `SX-SEM-005`, S-DT `unknown`, S-COST `cheap`.

## 8. What this manual deliberately does not code

Affect and biography; institutional reception (except set 5, by declared dimension); truth of the
final theory beyond the outcome label; anything the source does not show.

## Appendix A — positive / negative examples for every remaining category (out-of-corpus)

| Category | (+) positive instance | (−) near-miss, code otherwise |
|---|---|---|
| R-MEDIUM `physical-model` | Maxwell's vortex-and-idle-wheel mechanical model of the field (Nersessian) | A verbal analogy to gears with no built or drawn model → `verbal` |
| R-MEDIUM `apparatus` | Faraday working directly with coil and magnet while forming construals | Reading another's instrument report → `verbal`/`symbolic` |
| R-CHANGE `1 additive` | Adding a new species to an existing genus in a classification | Renaming an existing entity → `0` |
| A-TRIGGER `theory-inconsistency` | Kelvin's age-of-Earth conflict between thermodynamics and geology (as posed) | A single anomalous measurement → `anomaly` |
| A-TRIGGER `goal-inexpressibility` | Wanting to optimize "purity of a subsystem" when the objective language only expresses fidelity/count rate | Wanting a better fit within the existing objective → `none` |
| A-TYPE `monster` | A single misfitting specimen set aside as freak | Repeated systematic misfit → `model` |
| A-TYPE `special-case` | Boyle's law failing at high pressure, treated as condition-bounded | Failure everywhere → `model` |
| A-TYPE `indicative-role` | A known enzyme found to act at a different step than assumed | A missing enzyme → `indicative-entity` |
| A-RESPONSE `exclude` | "Cold fusion is chemistry, not our physics" — datum placed outside domain | Datum called fraudulent → `reject-data` |
| A-RESPONSE `abeyance` | Kepler noting the 8′ discrepancy and returning to it later (per C&B) | Explaining it away immediately → `reinterpret` |
| A-RESPONSE `uncertainty` | "The instrument may be at fault; await replication" | Declaring the datum false → `reject-data` |
| A-ATTENTION `late` | An unexpected result in the final month of a project that gets full attention | Early result on the central hypothesis → `early-core` |
| TRANSPORT `interfield` | Using chromosome cytology to interpret breeding ratios | Analogy from an unrelated domain → `analogy/far` |
| TRANSPORT `generic-abstraction` | Extracting "field with tension and pressure" common to fluid and electromagnetism, then transferring | Direct one-to-one mapping without an abstraction step → `analogy` |
| TRANSPORT `level-shift` | Explaining a trait by moving from organism to cell chemistry | Staying at the same level with a new mechanism → not transport |
| IDENT `delineate-and-alter` | Listing a theory's five assumptions and dropping the fourth | Modifying without enumeration → `specialize-and-add` or `unknown` |
| IDENT `propose-the-opposite` | "Suppose acquired characters are *not* inherited" as an exploratory move | Merely doubting → not a proposing move |
| IDENT `specialize-and-add` | Adding "except at high altitude" | Removing an assumption → `delineate-and-alter` |
| IDENT `uncover-implicit-assumption` | Realizing simultaneity had been assumed absolute | Stating a known assumption → not this |
| IDENT `extend-scope` | Applying a law found for gases to liquids | Applying it to the same gases again → replication (L3) |
| ASSEMBLY `modular-subassembly` | Combining known enzyme steps into a proposed cycle | Proposing an unknown enzyme → `factual/existential-abduction` |
| ASSEMBLY `forward-chaining` | From known replication start, reasoning what must come next | From end product backward → `backward-chaining` |
| ASSEMBLY `conceptual-combination` | "Sound wave" from sound + wave (Thagard) | Applying wave theory as analogy → `analogy` |
| ASSEMBLY `simplify-then-complicate` | Frictionless first, add friction later | Never idealizing → not this |
| MANIP `external-model-building` | Building the ball-and-stick model to find the helix | Sketching a candidate already held → `diagrammatic` medium only |
| MANIP `action-under-incomplete-info` | Running an exploratory screen before any hypothesis | A test of a stated prediction → L3 |
| MANIP `sense-control` | Turning the telescope to Jupiter to see what is there | Using it to test a predicted moon position → L3 |
| E-TESTORDER `cheapness` | "Try the cheap assay first" documented | Cheap test chosen by accident → `unknown` |
| E-TESTORDER `caution-one-component` | Varying one factor at a time by stated design | Simultaneous variation → not this |
| E-EXPT `risk-regulation` | Shortening experiments while confused, lengthening when confident (documented) | Fixed protocol → `unknown` |
| E-OUTCOME-RESPONSE `hold` | "Result unclear; repeat before deciding" | Silent continuation → `unknown` |
| S-RULE `authority/social` | Adviser instructs the next step | Peer suggestion adopted after argument → `other` + S-WHO |
| S-STRATEGY `explainable-explanations` | Preferring a cause that itself has a known mechanism | Preferring the simplest → `criteria` |

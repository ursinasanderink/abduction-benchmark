# Program overview — where the benchmark sits, and what has to be true for any of it to matter

*Public summary of the research program this benchmark belongs to. Written 2026-08-18, before
any data. The benchmark's own registration is [`PREREGISTRATION.md`](PREREGISTRATION.md)
(signed v1.0). Companion studies receive their own registrations before their own data.*

## The end goal, and the order it forces

The program's aim is to understand the **process** of scientific abduction well enough to write
it down as steps a person can follow and a language model can be taught — and to find out,
honestly, whether following those steps makes any measurable difference. That aim forces an
order, and the order is binding on the program:

1. **understand the process** (what the existing literature already established; what documented
   discovery episodes show when coded as sequences, not just as taxonomies of moves);
2. **decide whether it is worth anything** (the question ladder below);
3. **write it as followable steps**;
4. **test whether a model can be taught it**;
5. only then, any application.

## The value-of-abduction question ladder

Each question is answered by a named study with named evidence, and each has a declared
consequence if the answer is *no*. A later question is not asked before the earlier ones have an
answer.

| # | Question | Answered by | If "no" |
|---|---|---|---|
| Q1 | Is abduction a *distinct, identifiable* process — or a rebranding of search/induction? Does the existing process literature (Simon & Kulkarni's KEKADA, Klahr & Dunbar's dual-space search, Langley et al., Darden, Craver & Darden, Nersessian, Thagard, Bechtel & Richardson, Schurz, Peirce's economy of research, Dunbar's in-vivo studies…) already contain the process model? | process-literature synthesis (Phase 0.9) | the program becomes consolidation + empirical test of prior models — a fine outcome, reported as such |
| Q2 | Is the process *articulable* — can documented episodes be coded reliably, and does a recurring sequential/branching structure exist across cases? | historical-coding study ("Abduction Atlas", own registration) | "the process resists articulation" is the negative result; any protocol becomes a checklist of moves with no ordering claims |
| Q3 | Do good and bad abduction differ in *what they do* or in *how they choose*? | Atlas, matched success/failure contrast sets | either answer shapes the protocol |
| Q4 | Does following an explicit process make a difference **for a human**? | Atlas (retrospective) + a small-n human self-application study (prospective, logged) | protocol is a training aid at best |
| Q5 | Does it make a difference **for an LLM** — beyond no protocol *and* beyond a matched-length generic-structure placebo? | **this benchmark** (coarse first ablation, C2/C5; optional C10) → protocol-ablation study (own registration, placebo control mandatory) | protocol has no LLM value |
| Q6 | *Which* parts can the LLM execute, and which must stay human? | **this benchmark** (capability profile by layer) + ablations | fixes the human/model division of labour |
| Q7 | Does the value survive outside clean toy worlds — representation shift, noise, transfer? | **this benchmark** (Vulcan-trap module with decoys; noise ladder; transfer secondary) | value is an artifact of clean worlds |
| Q8 | Is the effect **large enough relative to cost** — versus best-of-N sampling, self-consistency, more compute? | cost ledger in the protocol study | cheaper to sample more; not worth operationalizing |
| **G3** | **Value gate:** proceed to any application only if Q1–Q8 justify it | written gate memo | no application; the protocol remains an internal tool |
| Q9 | Does it transfer to research productivity in an applied domain? | private applied study (field-level naming only, per the registration's §8) | stops there; the public program is unaffected |

## What this benchmark is, and is not

- It is a **replication and extension of active-versus-yoked hidden-mechanism discovery**
  (Geng et al. 2025; lineage Markant & Gureckis 2014; Klahr & Dunbar 1988), with an
  online-sequential computation-matched yoke, a passive-proposer arm ported to LLMs, and a
  representation-shift module with concealed decoys.
- It contributes evidence to **Q5, Q6 and Q7**, and its logged trajectories are raw material for
  distilling protocol steps.
- It is **not** the critical path to the end goal — that runs through the process-literature
  synthesis and the historical-coding study — and it is **not**, by itself, a test of whether
  language models can invent new scientific axioms, or of whether a human can follow the
  resulting steps.

## What is public, and when

Public: the registrations, the benchmark materials on the schedule fixed in the registration's
§5b, the historical-coding manual and coded corpus, the process-literature synthesis, and the
papers and articles that come out of them. Private: an applied-domain study, named at field level
only. Nothing about the private study is required for anything public to stand.

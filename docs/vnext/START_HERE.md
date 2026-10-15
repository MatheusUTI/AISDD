# AISDD vNext — Learning & Research Source of Truth

> Status: **experimental track**  
> Branch: `docs/vnext-learning-source-of-truth`  
> Started: 2026-10-15

This directory is the canonical source of truth for the **AISDD vNext learning and research track**.

Its primary purpose is not to rush a new framework version. Its purpose is to ensure that **Anderson Matheus understands the AISDD deeply enough to explain, question, evolve, and defend its architecture consciously**.

AISDD vNext development is a consequence of that learning process.

---

## 1. Primary objective

The success criterion of this track is not:

> “AISDD vNext is finished.”

The primary success criterion is:

> **Matheus can explain how AISDD works, why each mechanism exists, what information flows through it, where its limits are, how it can fail, and why a proposed evolution is justified.**

Implementation should follow understanding, not replace it.

---

## 2. Canonical reading order

When resuming this work in a new AI session, agent, chat, or tool, read in this order:

1. `docs/vnext/START_HERE.md` — purpose and rules of this track.
2. `docs/vnext/CURRENT_STATE.md` — exact checkpoint, current lesson, decisions, and next step.
3. `docs/vnext/LEARNING_ROADMAP.md` — full curriculum and development sequence.
4. Only then consult the main AISDD repository documents needed for the current lesson.

Do **not** jump directly to REA integration or vNext implementation unless `CURRENT_STATE.md` explicitly says the prerequisite learning phase is complete.

---

## 3. Core principle

The working sequence is:

```text
UNDERSTAND AISDD
      ↓
UNDERSTAND SYSTEMS CONCEPTS THROUGH AISDD
      ↓
UNDERSTAND REA
      ↓
COMPARE MECHANISMS
      ↓
ADOPT / ADAPT / REJECT
      ↓
EXPERIMENT IN A REAL PROJECT
      ↓
MEASURE
      ↓
INCORPORATE ONLY WHAT PROVES USEFUL
```

This sequence is intentionally slower than immediately adding features.

---

## 4. Learning before implementation

For every important AISDD mechanism, study it using the same analysis frame:

1. **Problem** — Why does this mechanism exist?
2. **Mechanism** — How does it solve the problem?
3. **Input** — What information does it receive?
4. **Processing** — What happens to that information?
5. **Output** — What does it produce?
6. **State** — What must be remembered?
7. **Dependencies** — What other mechanisms does it rely on?
8. **Failure modes** — How can it break or become misleading?
9. **Trade-offs** — What do we gain and what do we pay?
10. **Limits** — At what scale or scenario does it stop being sufficient?
11. **Alternatives** — What other designs could solve the same problem?
12. **Proof** — How do we know the mechanism is actually working?

A mechanism is not considered understood merely because its description was read.

---

## 5. Active learning rule

Learning must move through this cycle:

```text
AI explains
   ↓
Matheus inspects the real mechanism
   ↓
Matheus redraws / restates it
   ↓
AI challenges with “why?”, “what if?”, “where?”, “how do you know?”
   ↓
Misunderstandings are corrected
   ↓
Understanding is recorded in CURRENT_STATE
```

Recognition is not mastery.

The target is the ability to produce the explanation without reading the README.

---

## 6. What must eventually be understood

The learning track should cover, using AISDD and its real projects as teaching material:

- architecture and separation of responsibilities;
- transient state vs persistent state;
- source of truth;
- bootstrap / initialization of an AI session;
- project memory;
- workflow and state transitions;
- contracts and invariants;
- task decomposition;
- information models;
- facts, assumptions, unknowns, and risks;
- decisions and rationale;
- handoff and continuity;
- data flow;
- APIs and boundaries;
- persistence and cache;
- validation and testing;
- observability;
- provenance and evidence;
- staleness and invalidation;
- failure modes;
- scalability;
- trade-offs;
- security and trust boundaries;
- automation boundaries;
- reading code as a system map rather than merely as syntax.

The goal is **systems literacy**, not traditional programming proficiency for its own sake.

---

## 7. Relationship with REA

REA — Reverse Engineer Anything — is an important inspiration for the vNext research track, especially around:

- investigation;
- evidence;
- provenance;
- observations vs inferences;
- limitations;
- unknowns;
- snapshots;
- reusable analysis;
- validation.

However:

- AISDD must not become a reverse-engineering framework;
- REA must not become a mandatory AISDD dependency;
- REA concepts must not be copied blindly;
- REA-specific tooling should be rejected when it does not solve an AISDD problem.

Each candidate concept must be classified as:

- **ADOPT** — principle fits AISDD with little conceptual change;
- **ADAPT** — useful idea, but must be transformed for AI-assisted software development;
- **REJECT** — not useful enough, too specific, or introduces unjustified complexity.

REA should eventually be able to act as an **optional investigation/evidence provider**, not as AISDD’s foundation.

---

## 8. Current vNext hypotheses — not yet decisions

The following ideas are research hypotheses, not accepted AISDD rules:

- Evidence Model (`OBSERVED`, `VERIFIED`, `DERIVED`, `ASSUMED`, `UNKNOWN`);
- provenance for important project claims;
- `Investigation Before MISSING INFO`;
- task-scoped Context Packs;
- a future Context Compiler;
- evidence validity and stale detection;
- source hashes / snapshots;
- Acceptance Proof linked to acceptance criteria;
- reusable evidence/context cache;
- investigation providers such as source, Git, tests, runtime, browser, database, API, and REA;
- tooling/CLI only after repeated manual workflows prove automation useful.

No item above is promoted into AISDD Core merely because it sounds elegant.

---

## 9. Dogfooding rule

New vNext concepts must be tested against real work before becoming framework rules.

Preferred experimental loop:

```text
AISDD hypothesis
      ↓
small manual experiment
      ↓
real project task
      ↓
observe friction and benefit
      ↓
measure what is practical
      ↓
KEEP / SIMPLIFY / REJECT
      ↓
promote only if justified
```

FreteOps is the preferred early laboratory because it already uses AISDD and has upcoming work involving SSW/101 investigation, API contracts, architecture boundaries, unknowns, and validation.

---

## 10. Measurement principle

Do not claim benefits without evidence.

Examples of useful future measurements:

- context characters/bytes loaded;
- approximate or exact tokens later;
- number of files read;
- number of files reread;
- reused evidence;
- invalidated evidence;
- unknowns resolved autonomously;
- questions escalated to the user;
- rework caused by incorrect assumptions;
- regressions;
- task completion continuity across agents.

Start with measurements that are reliable and cheap. Do not invent precision.

---

## 11. Anti-drift rules

If this work starts drifting, return to these rules:

- Learning is the primary objective.
- Understand the current AISDD before redesigning it.
- Understand REA before borrowing from it.
- Never introduce a mechanism whose problem cannot be clearly stated.
- Never automate a process before the manual version proves useful.
- Preserve the current stable AISDD while vNext remains experimental.
- Prefer small experiments over framework-wide rewrites.
- Separate fact from hypothesis.
- Do not treat complexity as sophistication.
- Do not optimize for impressive terminology.
- A new feature must earn its maintenance cost.
- Real project evidence outranks enthusiasm.

---

## 12. Resume command for future sessions

A future AI session can be started with:

```text
This work follows the AISDD vNext learning track.
Read docs/vnext/START_HERE.md, then docs/vnext/CURRENT_STATE.md, then docs/vnext/LEARNING_ROADMAP.md.
Resume exactly from the current checkpoint.
Learning comes before implementation.
Do not jump ahead to REA adoption or vNext coding unless the recorded state says the prerequisites are complete.
```

---

## 13. Source-of-truth ownership

This directory exists specifically so that progress does not depend on the memory of one chat or one AI model.

The repository owns the continuity.

The conversation is temporary.

# AISDD vNext — Learning Roadmap

> This document defines the curriculum and development sequence for the AISDD vNext learning track.

The roadmap is intentionally **learning-first**. AISDD vNext should emerge from understanding, comparison, experiments, and evidence — not from feature accumulation.

---

# Phase 0 — Understand the current AISDD

## Goal

Reconstruct AISDD as a system before changing it.

Matheus should be able to explain not only **what files exist**, but **what architectural responsibility each mechanism has**.

## Core question

> How does the current AISDD produce continuity, reduce hallucination, constrain execution, and preserve project knowledge across AI sessions?

## Topics

### 0.1 — Why AISDD exists

Understand the fundamental mismatch:

```text
Software project state = long-lived
AI conversation/context = temporary and bounded
```

Study:

- transient vs persistent state;
- project memory;
- source of truth;
- why chat history is an unreliable project database;
- why continuity needs to be externalized.

### 0.2 — AISDD components as mechanisms

Study the architectural role of:

- `START_HERE`;
- `PROJECT_RULES`;
- `PRODUCT_SPEC`;
- `ARCHITECTURE`;
- `CURRENT_STATE`;
- `NEXT_TASK`;
- `ACCEPTANCE_CHECKS`;
- `DECISIONS_LOG`;
- `HANDOFF`;
- `KNOWN_ISSUES`;
- `FILE_INDEX`;
- test strategy / guardrails where applicable.

For each, answer:

```text
PROBLEM
MECHANISM
INPUT
PROCESSING
OUTPUT
STATE
DEPENDENCIES
FAILURE MODES
TRADE-OFFS
LIMITS
ALTERNATIVES
PROOF
```

### 0.3 — Bootstrap and session initialization

Understand `START_HERE` as a bootstrap protocol rather than “just a Markdown file”.

Questions:

- What does a new AI know before reading it?
- What state must be reconstructed?
- Why is read order important?
- What happens if files disagree?
- How much context should be loaded?

### 0.4 — Workflow and state transitions

Model the AISDD cycle:

```text
project state
   ↓
active task
   ↓
agent execution
   ↓
validation
   ↓
updated project state
   ↓
decisions / issues / handoff
   ↓
next session
```

Learn basic state-machine reasoning through AISDD itself.

### 0.5 — Information types

Understand the difference between:

- fact;
- assumption;
- unknown;
- risk;
- requirement;
- decision;
- current state;
- task;
- acceptance criterion;
- validation result.

Questions:

- Which information is descriptive?
- Which is prescriptive?
- Which changes frequently?
- Which should be immutable/history-preserving?
- Which can become stale?

### 0.6 — Contracts and invariants

Study AISDD rules as contracts.

Examples:

- repository is source of truth;
- one executable task per cycle;
- preserve working behavior unless change is explicit;
- separate facts from assumptions;
- validate before declaring completion;
- update handoff at the end of the cycle.

Learn:

- contract;
- invariant;
- precondition;
- postcondition;
- responsibility boundary.

### 0.7 — Current limits

Stress-test the current design conceptually:

- 10 files vs 10,000 files;
- one agent vs many agents;
- one task vs parallel work;
- short-lived vs multi-year project;
- 10 decisions vs 20,000 decisions;
- small docs vs large documentation corpus;
- aligned docs vs stale/conflicting docs.

Goal: identify where AISDD’s current design becomes expensive, ambiguous, or insufficient.

## Exit criteria for Phase 0

Matheus can, without reading the README:

- explain the original AISDD problem;
- draw the main workflow;
- explain the architectural purpose of each core document;
- explain transient vs persistent state;
- explain source of truth;
- explain why `NEXT_TASK` and `HANDOFF` exist;
- identify at least three failure modes;
- identify at least three scaling limitations;
- answer “why?” questions about the current design.

Only then proceed to Phase 1.

---

# Phase 1 — Systems literacy through AISDD

## Goal

Use AISDD and FreteOps as practical material to learn the systems concepts needed to design software consciously.

This is not a generic programming course.

## Topics

### 1.1 Architecture

Learn:

- components;
- responsibilities;
- boundaries;
- coupling;
- cohesion;
- layers;
- dependencies.

Exercise: draw AISDD and FreteOps architectures at different zoom levels.

### 1.2 Data and information flow

Learn to follow:

```text
input → transformation → state → output
```

Questions:

- where did this information originate?
- who owns it?
- who changes it?
- who consumes it?
- what happens when it is missing or invalid?

### 1.3 State and persistence

Learn:

- transient state;
- persistent state;
- cache;
- durable storage;
- source of truth;
- synchronization;
- stale state.

Use AISDD docs, chat context, Git history, Android state, and future API data as examples.

### 1.4 Interfaces and contracts

Learn why systems communicate through boundaries.

Use examples such as:

- AISDD agent ↔ repository protocol;
- FreteOps ViewModel ↔ Repository;
- app ↔ backend;
- backend ↔ SSW.

### 1.5 APIs

Learn practical fundamentals:

- request/response;
- GET/POST;
- headers;
- body;
- JSON;
- status codes;
- timeout;
- retry;
- idempotency;
- authentication boundaries.

Focus on system behavior, not memorizing protocol trivia.

### 1.6 Failure reasoning

For every important flow, consider:

- happy path;
- missing data;
- malformed data;
- timeout;
- offline state;
- authentication failure;
- stale cache;
- partial success;
- concurrent actions;
- dependency failure.

### 1.7 Validation and testing

Learn the distinction between:

- assertion;
- test;
- evidence;
- acceptance criterion;
- manual validation;
- automated validation;
- regression test.

### 1.8 Observability

Learn how a system tells us what happened:

- logs;
- metrics;
- traces;
- errors;
- diagnostics;
- state inspection.

### 1.9 Reading code as a map

Minimum code literacy target:

- function;
- class;
- interface;
- input;
- output;
- condition;
- loop;
- state mutation;
- side effect;
- external call;
- error path;
- call chain.

The goal is to follow system behavior through code, not to become syntax-dependent.

## Exit criteria for Phase 1

Matheus can inspect a small feature and explain:

- components involved;
- data flow;
- state ownership;
- external boundaries;
- failure paths;
- validation strategy;
- likely architectural trade-offs.

---

# Phase 2 — Understand REA

## Goal

Study REA only after the AISDD and systems foundations are understood.

Do not study REA as “a cool tool”. Study it as a system solving concrete problems.

## Analysis frame for every REA concept

```text
REA CONCEPT
↓
WHAT PROBLEM DOES REA SOLVE WITH IT?
↓
HOW DOES THE MECHANISM WORK?
↓
WHAT INFORMATION DOES IT PRODUCE?
↓
WHAT ARE ITS LIMITATIONS?
↓
DOES AISDD HAVE AN ANALOGOUS PROBLEM?
↓
ADOPT / ADAPT / REJECT
```

## Candidate areas

- evidence;
- provenance;
- observed vs inferred claims;
- confidence / authority where useful;
- explicit limitations;
- unknowns;
- retained analysis;
- snapshots;
- invalidation;
- reusable results;
- investigation workflow;
- evidence bundles;
- provider abstraction;
- runtime vs static observations.

## Important boundary

REA-specific reverse-engineering capabilities are not automatically AISDD concepts.

The question is always:

> What underlying design principle is useful for AI-assisted software development?

---

# Phase 3 — REA → AISDD concept map

## Goal

Produce a justified map of candidate vNext mechanisms.

Each candidate must include:

| Field | Question |
|---|---|
| AISDD problem | What current limitation are we solving? |
| REA inspiration | What mechanism suggested this direction? |
| Decision | ADOPT / ADAPT / REJECT |
| Proposed AISDD form | What would it mean inside AISDD? |
| Cost | What complexity/maintenance does it add? |
| Expected benefit | What measurable improvement is expected? |
| Experiment | How will we test it? |

## Candidate hypotheses currently known

- richer Evidence Model;
- provenance;
- Investigation Before MISSING INFO;
- Context Pack;
- Context Compiler;
- evidence/source validity;
- stale detection;
- Acceptance Proof;
- retained/reusable evidence;
- optional investigation providers;
- REA as optional provider.

These remain hypotheses until this phase validates them conceptually.

---

# Phase 4 — Design AISDD vNext

## Goal

Define the smallest coherent vNext model supported by prior understanding.

Topics may include:

- evidence lifecycle;
- context lifecycle;
- task-scoped knowledge;
- investigation gate;
- verification gate;
- acceptance proof;
- stale knowledge handling;
- provider contracts;
- relationship with current PML/adoption layers;
- backward compatibility with current AISDD.

## Design requirement

For every new mechanism, Matheus must be able to answer:

```text
Why does it exist?
What problem does it solve?
How does it work?
What does it cost?
What alternative exists?
When should it NOT be used?
How will we prove it helps?
```

If these answers are weak, the mechanism is not ready.

---

# Phase 5 — Manual dogfooding in FreteOps

## Goal

Test vNext ideas before building tooling.

Potential first real scenario:

> investigate and define the minimum contract required for the operational SSW 101 integration while preserving the current FreteOps repository boundary.

Why this is useful:

- existing architecture;
- incomplete knowledge;
- real external system;
- investigation required;
- unknowns;
- API contract design;
- evidence;
- validation;
- future implementation consequences.

## Experiment loop

```text
hypothesis
↓
manual mechanism
↓
real task
↓
friction + benefit
↓
measurement
↓
KEEP / SIMPLIFY / REJECT
```

---

# Phase 6 — Measurement

## Goal

Determine whether vNext mechanisms actually improve AI-assisted work.

Possible metrics:

- baseline context size;
- task context size;
- context reduction percentage;
- files loaded;
- rereads avoided;
- evidence reused;
- stale evidence caught;
- unknowns resolved without user intervention;
- unnecessary user questions avoided;
- regressions;
- rework caused by wrong assumptions;
- handoff success across different agents.

Do not claim token savings until measured appropriately.

---

# Phase 7 — Automation

## Goal

Automate only stable, repetitive manual workflows.

Possible future tooling — not commitments:

```text
aisdd status
aisdd context
aisdd evidence
aisdd verify
aisdd handoff
```

Before implementing a command, ask:

- how often do we perform this manually?
- is the manual workflow stable?
- does automation reduce errors or cognitive load?
- is the maintenance cost justified?

No CLI for prestige.

---

# Phase 8 — Promote proven mechanisms

## Goal

Move only validated concepts into official AISDD documentation/framework rules.

For every promotion, record:

```text
problem
hypothesis
experiment
evidence
result
trade-offs
decision
```

AISDD Core should remain smaller than AISDD research.

---

# Long-term mastery target

Matheus should eventually be able to explain AISDD from a blank page in roughly this order:

```text
original problem
↓
state model
↓
source of truth
↓
architecture
↓
core mechanisms
↓
workflow
↓
contracts/invariants
↓
validation
↓
continuity
↓
current limitations
↓
vNext motivations
↓
proposed mechanisms and evidence for them
```

A useful final exercise is an architecture review where the AI repeatedly asks:

- Why?
- What if this disappears?
- What owns this state?
- What happens when sources conflict?
- How do you know this is true?
- Where does this stop scaling?
- Why this design instead of the alternative?

The goal is not memorization. The goal is **independent systems reasoning**.

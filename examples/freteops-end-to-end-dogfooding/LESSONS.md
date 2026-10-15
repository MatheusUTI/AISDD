# FreteOps Dogfooding Lessons

This file stores observations from the FreteOps case before they are promoted into AISDD framework rules.

## Rule

Do not change AISDD core behavior from one isolated project event unless the early-exception safety rule applies.

Use this file as a buffer between:

```txt
Project experience
↓
Observation
↓
Repeated evidence
↓
Framework proposal
```

## Observations

### OBS-001 — Repository memory immediately shrinks follow-up prompts

**Date:** 2026-10-15  
**Status:** early observation

The initial scaffold required a long prompt; later tasks can be started primarily through repository instructions such as `Leia docs/START_HERE.md e execute somente docs/04_NEXT_TASK.md.`

Potential value: repeated product/architecture context moves from chat into durable repository memory.

### OBS-002 — A generated project benefits from an immediate factual audit

**Date:** 2026-10-15  
**Status:** early observation

The first generated Android project had a reasonable structural boundary between UI and data, but also included prototype defaults, mock behavior, broad dependencies, and visual inconsistencies.

Potential implication: near-greenfield AISDD workflows may benefit from a small factual baseline audit before feature development.

### OBS-003 — Cross-AI role separation is naturally testable

**Date:** 2026-10-15  
**Status:** active experiment

FreteOps uses one AI environment for Android implementation and another AI for architecture/review/AISDD governance.

This makes vendor/model independence, handoff quality and review quality observable rather than theoretical.

### OBS-004 — Dogfooding evidence should not live only in the product repository

**Date:** 2026-10-15  
**Status:** adopted for this case

The product repository stores truth needed to build the product; the AISDD repository stores framework-validation evidence.

### OBS-005 — Repository-driven execution depends on synchronized workspace state

**Date:** 2026-10-15  
**Status:** verified for this environment

AI Studio/GitHub behavior:

```txt
GitHub
   ⇅ manual sync action in AI Studio
AI Studio workspace
```

Sync works in both directions but requires an explicit human click. The click is environment plumbing, not manual task context.

### OBS-006 — Manual synchronization can still support a strong shared-memory boundary

**Date:** 2026-10-15  
**Status:** positive case evidence

ChatGPT can update canonical memory in GitHub; the human synchronizes; Gemini consumes it; Gemini publishes its result; GitHub then becomes available for independent review.

### OBS-007 — Human-triggered sync acts as a visible consistency gate

**Date:** 2026-10-15  
**Status:** hypothesis

Manual sync adds friction but makes the context-transfer boundary explicit. The downside is stale-context risk if the owner forgets to synchronize.

### OBS-008 — Successful implementation can still introduce memory drift

**Date:** 2026-10-15  
**Status:** early observation

UX-001 was implemented successfully, but post-task documentation had small inconsistencies. Cycle closure therefore needs to consider project-memory consistency, not only product behavior.

### OBS-009 — Strong repository context does not eliminate semantic overreach

**Date:** 2026-10-15  
**Status:** repeated case evidence

INT-001 used strong repository context and a tiny startup prompt, yet the implementing model still introduced plausible but unsupported normalizations (series assumption, unsafe status fallback, synthetic current-unit/occurrence behavior and other overconfident defaults).

Useful distinction:

```txt
context sufficiency
≠
semantic correctness
```

The independent review gate prevented these assumptions from becoming code unchanged.

### OBS-010 — Passing tests can coexist with contract-fidelity defects

**Date:** 2026-10-15  
**Status:** repeated/important case evidence

INT-002 reportedly compiled and passed its eight required tests, but cross-AI static review still found meaningful fidelity gaps:

- factual status description/raw text was discarded when DTOs were reduced to an enum;
- public timing/cargo fields were parsed but silently dropped by the domain mapper;
- missing occurrence code became the synthetic string `EVENTO`;
- `texto - texto` could be over-parsed as `Cidade - UF`;
- timeline coherence was not enforced by the mapper;
- runtime mocks contradicted the full CTRC format and product neutrality.

The tests were not false; they simply encoded an incomplete acceptance surface.

Potential implication:

AISDD review should ask both:

```txt
Do the tests pass?
AND
Do the tests cover the semantic invariants that matter?
```

This is especially relevant for adapters/mappers, where data loss can compile perfectly.

### OBS-011 — Independent review can progressively improve the next task instead of rewriting prior work

**Date:** 2026-10-15  
**Status:** positive case evidence

Both INT-001 and INT-002 were preserved rather than reverted. Review findings were converted into explicit repository gates (`R1–R11`, then `G1–G6`) and into one singular remediation task.

Observed pattern:

```txt
Implementation
   ↓
Independent review
   ↓
Repository review gate
   ↓
Small remediation task
   ↓
Continue architecture
```

This appears compatible with AISDD's incremental philosophy and avoids losing useful generated work because a few semantic details were wrong.

### OBS-012 — Checkpoint/model fallback can preserve an AISDD cycle without prompt restatement

**Date:** 2026-10-15  
**Status:** environment-specific case evidence

During INT-002, Gemini 3.8 Flash edited most files and then hit a quota limit. AI Studio resumed from checkpoint with Gemini 3.6 Flash, which completed the remaining documentation/handoff steps without the owner re-explaining the task.

This suggests repository memory plus execution checkpointing can make model fallback less disruptive. The behavior is specific to AI Studio and should not be promoted to an AISDD rule without evidence from other environments.

## Candidate improvements

Do not promote these observations into universal requirements yet. Collect more evidence from environments with:

- automatic bidirectional repository synchronization;
- human-triggered bidirectional synchronization;
- full local Git access;
- publish-only integration;
- uploaded/static project snapshots;
- local CLI agents;
- model/checkpoint fallback behavior.

Wait for more implementation cycles before proposing changes to:

- adoption packages;
- PML definitions;
- required project documents;
- handoff rules;
- environment preflight rules;
- response format;
- dogfooding metrics;
- whether contract/mapper tasks should receive a dedicated independent review gate;
- whether test plans should explicitly include semantic-information-preservation checks.

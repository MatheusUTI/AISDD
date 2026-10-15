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

INT-001 used strong repository context and a tiny startup prompt, yet the implementing model still introduced plausible but unsupported normalizations.

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

INT-002 compiled/passed its requested tests, but static review still found meaningful fidelity gaps in status preservation, fields silently dropped, synthetic fallbacks, location parsing and timeline coherence.

Potential implication:

```txt
Do the tests pass?
AND
Do the tests cover the semantic invariants that matter?
```

This is especially relevant for adapters/mappers, where data loss can compile perfectly.

### OBS-011 — Independent review can progressively improve the next task instead of rewriting prior work

**Date:** 2026-10-15  
**Status:** positive case evidence

Review findings were converted into explicit repository gates and singular remediation tasks rather than discarding the useful implementation.

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

### OBS-012 — Checkpoint/model fallback can preserve an AISDD cycle without prompt restatement

**Date:** 2026-10-15  
**Status:** environment-specific case evidence

During INT-002, Gemini 3.8 Flash hit quota and AI Studio resumed from checkpoint with Gemini 3.6 Flash without the owner re-explaining the task.

This is environment-specific and should not be promoted to a framework rule without broader evidence.

### OBS-013 — Repository memory allows implementation ownership to move between tools

**Date:** 2026-10-15  
**Status:** strong case evidence

After Android contract work, quota pressure made Gemini less suitable for heavy development. Implementation ownership moved to ChatGPT operating directly through GitHub for backend architecture, skeleton and SSW connector work.

No new product bootstrap was needed. The new implementer reconstructed the active task from repository state and continued through INT-003, INT-004, INT-005 and INT-006 preparation.

Observed transition:

```txt
Gemini / AI Studio = primary implementer
        ↓ quota/tool constraint
GitHub canonical memory remains unchanged
        ↓
ChatGPT / GitHub = primary backend implementer
AI Studio = Android preview/build/quick-fix surface
```

Potential implication: AISDD's useful portability target is not “any model behaves identically”; it is “the project can reassign roles without reconstructing its history in prompts.”

### OBS-014 — Tool scarcity can be handled by changing role allocation instead of degrading project context

**Date:** 2026-10-15  
**Status:** positive case evidence

When premium AI Studio quotas became scarce, the response was not to compress or discard project memory. Instead, expensive/limited tooling was reserved for work where it had unique value (Android visualisation/build), while repository-native architecture/backend work moved elsewhere.

Potential value:

```txt
scarce tool
→ narrow to comparative advantage
not
→ make every task consume the scarce tool
```

This suggests AISDD can support cost-aware execution strategies without changing the source-of-truth model.

### OBS-015 — External evidence gates should separate “prepared” from “validated”

**Date:** 2026-10-15  
**Status:** important case evidence

INT-005 produced a real SSW connector from audited evidence, but live facts such as current layout, actual latency and not-found signature cannot be proven without authorised credentials and test CTRCs.

INT-006 therefore separates:

```txt
code prepared
+ offline tests green
+ CI/container green
≠
live integration validated
```

The project added a preflight, sanitised smoke helper, metrics, leak checks and runbook while keeping the task open on the external evidence.

Potential implication: AISDD acceptance states may benefit from explicit categories such as `prepared`, `validated offline`, `validated live`, and `blocked by external evidence`, rather than a single binary done/not-done state.

## Candidate improvements

Do not promote these observations into universal requirements yet. Collect more evidence from environments with:

- automatic bidirectional repository synchronization;
- human-triggered bidirectional synchronization;
- full local Git access;
- publish-only integration;
- uploaded/static project snapshots;
- local CLI agents;
- model/checkpoint fallback behavior;
- implementer/tool-role migration;
- tasks gated by private external systems or credentials.

Wait for more implementation cycles before proposing changes to:

- adoption packages;
- PML definitions;
- required project documents;
- handoff rules;
- environment preflight rules;
- response format;
- dogfooding metrics;
- whether contract/mapper tasks should receive a dedicated independent review gate;
- whether test plans should explicitly include semantic-information-preservation checks;
- whether acceptance should model external-evidence states explicitly.

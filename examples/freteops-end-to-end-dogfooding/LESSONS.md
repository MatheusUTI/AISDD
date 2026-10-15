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
**Evidence:** initial scaffold required a long prompt; later tasks can be expressed primarily through repository instructions such as `Read docs/START_HERE.md. Execute docs/04_NEXT_TASK.md.`

**What this may validate:**

- PML is understandable in a real workflow;
- project docs can absorb repeated context very early;
- AISDD may be useful even when adopted on the first development day.

**What is not proven yet:**

- that prompt size stays low as integrations become more complex;
- that documentation remains accurate over many cycles;
- that equivalent behavior repeats across other AI environments.

### OBS-002 — A generated project benefits from an immediate factual audit

**Date:** 2026-10-15  
**Status:** early observation

The first generated Android project had a reasonable structural boundary between UI and data, but also included prototype-specific defaults, mock behavior, broad dependencies, and visual inconsistencies.

**Potential implication:**

A near-greenfield AISDD workflow may benefit from a small post-generation baseline audit before feature development continues.

This is not yet proposed as a new mandatory AISDD phase.

### OBS-003 — Cross-AI role separation is naturally testable

**Date:** 2026-10-15  
**Status:** active experiment

FreteOps uses one AI environment for Android implementation and another AI for architecture/review/AISDD governance.

**Potential value:**

- makes vendor independence measurable instead of theoretical;
- exposes missing repository context quickly;
- creates a practical handoff test every cycle.

### OBS-004 — Dogfooding evidence should not live only in the product repository

**Date:** 2026-10-15  
**Status:** adopted for this case

The product repository should contain the truth needed to build the product.

The AISDD repository should contain framework-validation evidence.

This avoids contaminating the product with framework research while preserving evidence for AISDD evolution.

### OBS-005 — Repository-driven execution depends on synchronized workspace state

**Date:** 2026-10-15  
**Status:** verified for this environment

The first PML-4 startup attempt did not fail because task documentation was insufficient. Gemini correctly reported that the AISDD files were absent from its active workspace.

The actual AI Studio/GitHub behavior was later verified by the project owner:

```txt
GitHub
   ⇅ manual sync action in AI Studio
AI Studio workspace
```

Synchronization works in both directions, but requires an explicit human click. Changes made on either side are not assumed to propagate automatically.

**Immediate workflow implication for FreteOps:**

- keep GitHub as the canonical project memory;
- trigger synchronization before Gemini begins an AISDD cycle;
- let Gemini execute from the synchronized repository state;
- publish/synchronize the resulting changes back before another AI reviews them;
- do not paste repository content manually unless the normal sync mechanism fails.

**Potential framework implication:**

AISDD may benefit from an environment preflight that distinguishes:

1. repository memory exists;
2. the AI environment can receive it;
3. the working copy is actually synchronized;
4. synchronization is automatic or human-triggered.

This is not yet a universal core rule. More evidence is needed across tools.

### OBS-006 — Manual synchronization can still support a strong shared-memory boundary

**Date:** 2026-10-15  
**Status:** positive case evidence

The need for a human synchronization click did not force task context back into chat prompts.

ChatGPT can update canonical project memory in GitHub; the human owner synchronizes; Gemini consumes that state; Gemini publishes its result; GitHub then becomes available to ChatGPT for review.

This preserves the intended shared-memory pattern:

```txt
ChatGPT / architecture review
        ↓
      GitHub
        ⇅ human sync
    AI Studio / Gemini
        ↓
      GitHub
        ↓
ChatGPT / next review
```

The synchronization action is operational plumbing, not project specification.

### OBS-007 — Human-triggered sync acts as a visible consistency gate

**Date:** 2026-10-15  
**Status:** hypothesis to observe over future cycles

A manual sync step is a small friction cost, but it also makes the moment of context transfer explicit.

That may be useful because the owner can deliberately control when:

- GitHub changes enter AI Studio;
- AI Studio changes become canonical in GitHub;
- another AI is allowed to review or modify the new state.

Potential downside: forgetting to synchronize can recreate stale-context failures. The project therefore records sync preflight in `START_HERE.md`.

Do not generalize this as a preferred workflow yet; automatic synchronization may be superior in other environments.

### OBS-008 — Successful implementation can still introduce memory drift

**Date:** 2026-10-15  
**Status:** early observation

UX-001 was implemented successfully, but the first post-task documentation update contained small inconsistencies: stale commit reference, a completed task still occupying `NEXT_TASK`, incomplete general acceptance check reconciliation, and terminology drift around the AISDD name.

**Potential implication:**

Cycle closure should evaluate not only product behavior but also internal consistency of project memory.

This is currently case evidence, not a new mandatory AISDD phase.

## Candidate improvements

Do not promote these observations into universal requirements yet. Collect more evidence from environments with:

- automatic bidirectional repository synchronization;
- human-triggered bidirectional synchronization;
- full local Git access;
- publish-only integration;
- uploaded/static project snapshots;
- local CLI agents.

Wait for multiple implementation cycles before proposing changes to:

- adoption packages;
- PML definitions;
- required project documents;
- handoff rules;
- environment preflight rules;
- response format;
- dogfooding metrics.

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
**Evidence:** initial scaffold required a long prompt; the next planned implementation task can be expressed as `Read docs/START_HERE.md. Execute docs/04_NEXT_TASK.md.`

**What this may validate:**

- PML is understandable in a real workflow;
- project docs can absorb repeated context very early;
- AISDD may be useful even when adopted on the first development day.

**What is not proven yet:**

- that Gemini can complete the task safely from the short prompt;
- that documentation remains accurate after several cycles;
- that prompt size stays low as integrations become more complex.

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

### OBS-005 — Repository-driven execution has an environment-access precondition

**Date:** 2026-10-15  
**Status:** active observation

The first PML-4 startup attempt did not fail because the task documentation was insufficient. It failed before execution because Google AI Studio's active project workspace did not contain repository changes made externally.

The observed integration is asymmetric:

```txt
AI Studio workspace → GitHub
GitHub -/→ active AI Studio workspace
```

Gemini could publish what it generated to GitHub, but it could not read the AISDD files that had been added to GitHub outside the AI Studio workspace.

**Immediate workflow implication for FreteOps:**

- bootstrap the AISDD `docs/` directory into the AI Studio workspace once;
- after bootstrap, Gemini becomes the writer of FreteOps code and project-memory docs inside that workspace;
- ChatGPT audits FreteOps from GitHub and proposes changes, but should avoid directly changing FreteOps project-memory files unless a manual resynchronization into AI Studio is planned;
- ChatGPT continues to write AISDD framework/dogfooding evidence in the AISDD repository.

**Potential framework implication:**

AISDD may need to distinguish `repository is the source of truth` from `the current AI can access the source of truth`.

A future portability/workspace guide may need an explicit synchronization preflight for tools with one-way or isolated workspaces.

This is not yet a core-rule change. More evidence is needed across tools.

## Candidate improvements

Do not promote OBS-005 into a universal requirement yet. Collect more evidence from environments with:

- full Git repository access;
- one-way publish-only integration;
- uploaded/static project snapshots;
- local CLI agents.

Wait for multiple implementation cycles before proposing changes to:

- adoption packages;
- PML definitions;
- required project documents;
- handoff rules;
- response format;
- dogfooding metrics.
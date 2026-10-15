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

### OBS-005 — Repository-driven execution depends on actual repository access, not only UI integration

**Date:** 2026-10-15  
**Status:** revised observation / verification pending

The first PML-4 startup attempt did not fail because the task documentation was insufficient. Gemini correctly reported that `docs/START_HERE.md` and `docs/04_NEXT_TASK.md` were absent from its active workspace.

Our first interpretation was that AI Studio supported only:

```txt
AI Studio workspace → GitHub
GitHub -/→ active AI Studio workspace
```

A later direct capability check changed that understanding. Gemini reported that the AI Studio execution environment has `git` and `curl` available and can explicitly download/synchronize files from GitHub. For a private repository it requests authentication, such as a read-scoped GitHub token.

This means the UI-level GitHub integration may still be publish-oriented, while the execution environment itself may provide an explicit pull path:

```txt
GitHub
  ↓ explicit git/curl sync
AI Studio workspace
  ↓ implementation
GitHub
```

**Important:** this inbound path is reported by Gemini but is not yet considered validated until an actual authenticated synchronization succeeds without corrupting or replacing local project state.

**Immediate workflow implication for FreteOps:**

- keep GitHub as the canonical project memory;
- before an AISDD-controlled cycle, explicitly synchronize the required repository memory into AI Studio;
- avoid pasting long-lived credentials into prompts;
- use the narrowest practical read-only, repository-scoped authentication mechanism for inbound synchronization;
- after sync, retry the minimal PML-4 prompt without manually repeating the task.

**Potential framework implication:**

AISDD may benefit from a small environment preflight that distinguishes:

1. repository memory exists;
2. the current AI environment can read it;
3. the local working copy is synchronized with it.

This is not yet a core-rule change. More evidence is needed across tools.

### OBS-006 — Explicit sync may preserve multi-AI project ownership better than manual file copying

**Date:** 2026-10-15  
**Status:** hypothesis to test

If the reported git/curl path works, ChatGPT can continue maintaining reviewed project memory in GitHub while Gemini consumes the same memory before implementation. This would remove the need for manual `docs/` uploads and would make the repository a genuinely shared handoff boundary between AI systems.

The key risk is synchronization safety: inbound sync must not silently overwrite newer AI Studio code or local uncommitted changes.

A safe pattern should therefore inspect repository/workspace state before pulling and, initially, synchronize only the required AISDD docs rather than blindly replacing the entire project tree.

## Candidate improvements

Do not promote OBS-005 or OBS-006 into universal requirements yet. Collect more evidence from environments with:

- full Git repository access;
- publish-only UI integration plus shell/network access;
- uploaded/static project snapshots;
- local CLI agents.

Wait for multiple implementation cycles before proposing changes to:

- adoption packages;
- PML definitions;
- required project documents;
- handoff rules;
- response format;
- dogfooding metrics.

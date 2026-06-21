# AISDD Dogfooding Metrics

Use this document to validate whether AISDD works in real projects.

The goal is to measure practical friction, context savings, handoff quality, and AI portability.

## Why this exists

AISDD claims to improve long-term AI-assisted development by reducing context load, hallucinations, regressions, and vendor lock-in.

Those claims should be tested during real usage.

## Metrics summary

| Metric | What it validates |
|---|---|
| Handoff update rate | Whether continuity docs are realistic to maintain |
| Decision log update rate | Whether ADR discipline survives real work |
| Context size estimate | Whether AISDD reduces repeated context |
| Missing info friction | Whether anti-hallucination rules block too often |
| Cross-AI continuation | Whether another AI can continue from docs alone |

## 1. Handoff update rate

Track how often `docs/07_HANDOFF.md` is updated before changing sessions, tools, or tasks.

### Log format

| Date | Project | Session ended? | Handoff updated? | Notes |
|---|---|---:|---:|---|
| TODO | TODO | Yes/No | Yes/No | TODO |

### Signal

Good sign:

- Handoff is updated in most meaningful session changes.

Warning sign:

- Handoff is frequently forgotten.

Possible fix:

- Make handoff update part of the default AI response.
- Add a pre-commit or checklist reminder.

## 2. Decision log update rate

Track whether `docs/06_DECISIONS_LOG.md` is updated when structural decisions happen.

### What counts as a decision

Examples:

- choosing or changing stack;
- changing architecture;
- adding a persistent data model;
- changing API contracts;
- changing project workflow;
- accepting a known tradeoff.

### Log format

| Date | Decision made | ADR updated? | ADR ID | Notes |
|---|---|---:|---|---|
| TODO | TODO | Yes/No | ADR-XXX | TODO |

### Signal

Good sign:

- Major decisions are traceable.

Warning sign:

- Important decisions only exist in chat history.

## 3. Context size estimate

Estimate how much context is needed before and after AISDD adoption.

This does not need to be exact at first.

### Simple measurement

For comparable tasks, record:

| Date | Project | Task type | Before AISDD context | AISDD context | Result |
|---|---|---|---:|---:|---|
| TODO | TODO | Bug fix / feature / refactor | TODO | TODO | TODO |

### What to compare

Before AISDD:

- long chat recap;
- pasted files;
- repeated project explanation;
- manual reminders.

With AISDD:

- `START_HERE.md`;
- selected project docs;
- current task;
- relevant files only.

### Signal

Good sign:

- Less repeated explanation is needed for similar tasks.

Warning sign:

- The AI still requires long manual context every cycle.

## 4. Missing info friction

Track when the `MISSING INFO` rule helps and when it blocks unnecessarily.

### Categories

| Category | Meaning | Expected behavior |
|---|---|---|
| Critical | Needed to avoid wrong code or wrong product behavior | Stop with `MISSING INFO` |
| Assumable | Reasonable default can be adopted safely | Proceed with explicit assumption |
| Cosmetic | Low-risk preference | Choose simple default and document if needed |

### Log format

| Date | Task | Missing info | Category | AI behavior | Was it useful? |
|---|---|---|---|---|---|
| TODO | TODO | TODO | Critical / Assumable / Cosmetic | TODO | Yes/No |

### Calibration rule

The AI should stop only when missing information could cause:

- data loss;
- broken contracts;
- wrong architecture;
- wrong business rule;
- security or privacy risk;
- irreversible migration;
- significant rework.

The AI may proceed with explicit assumptions when the decision is low-risk and easy to change later.

## 5. Cross-AI continuation test

Test whether a different AI can continue the project using repository docs only.

### Test flow

1. Complete a task with AI-A.
2. Update affected docs and `07_HANDOFF.md`.
3. Start a new session with AI-B.
4. Give AI-B only the repository and AISDD startup prompt.
5. Ask AI-B to summarize current state and next task.
6. Compare the result with reality.

### Evaluation

| Date | Project | AI-A | AI-B | Could continue? | Problems found |
|---|---|---|---|---:|---|
| TODO | TODO | TODO | TODO | Yes/No | TODO |

### Good result

AI-B should correctly identify:

- project purpose;
- current state;
- next task;
- known risks;
- important files;
- relevant constraints.

## 6. Dogfooding report template

Use this after testing AISDD on a real project.

```txt
# AISDD Dogfooding Report

## Project

TODO

## Period

TODO

## Summary

TODO

## What worked

- TODO

## What failed or caused friction

- TODO

## Metrics

| Metric | Result |
|---|---|
| Handoff update rate | TODO |
| Decision log update rate | TODO |
| Context size estimate | TODO |
| Missing info friction | TODO |
| Cross-AI continuation | TODO |

## Changes recommended for AISDD

- TODO
```

## Main rule

AISDD should be judged by real continuity, not by how good the documentation looks.
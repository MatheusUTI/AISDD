# AISDD Dogfooding Metrics

Use this document to validate whether AISDD works in real projects.

The goal is to measure practical friction, context savings, handoff quality, AI portability, and Recovery Mode accuracy.

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
| Recovery snapshot accuracy | Whether Recovery Mode maps the real project state correctly |

## Minimum validation window

Do not change AISDD rules based on one or two tasks.

Before drawing conclusions or recalibrating core rules, collect at least:

| Requirement | Minimum |
|---|---:|
| Real tasks completed | 10 |
| Different task types | 3 |
| Session handoffs | 3 |
| Structural decisions | 2 |
| Cross-AI continuation tests | 1 |
| Recovery snapshots reviewed | 1 |

Recommended task types:

- bug fix;
- small feature;
- refactor;
- documentation update;
- test or validation task.

## Early exception rule

A rule may be changed before the minimum window only if it causes clear damage, such as:

- repeated data loss risk;
- repeated wrong architecture;
- repeated broken contracts;
- repeated security or privacy risk;
- obvious workflow deadlock.

Minor friction should be logged, not immediately used to change the framework.

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

The goal is directional honesty, not perfect token accounting.

### Simple measurement

For comparable tasks, record:

| Date | Project | Task type | Before AISDD context | AISDD context | Result |
|---|---|---|---:|---:|---|
| TODO | TODO | Bug fix / feature / refactor | TODO | TODO | TODO |

### Simple token proxy

When exact token counts are unavailable, estimate tokens from text size.

Use:

```txt
estimated_tokens = total_characters / 4
```

This is approximate, but useful for comparing similar tasks.

### What to count

Count all text sent to the AI for the task:

- task prompt;
- loaded AISDD docs;
- pasted source files;
- copied errors or logs;
- manual project explanation;
- handoff or recap text.

### Context log format

| Date | Project | Task | Prompt chars | Docs chars | Files/logs chars | Estimated tokens | Notes |
|---|---|---|---:|---:|---:|---:|---|
| TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

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

### Recalibration rule

Do not recalibrate `MISSING INFO` from isolated frustration.

Recalibrate only after the minimum validation window, unless the early exception rule applies.

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

## 6. Recovery snapshot accuracy

Recovery Mode has a different primary risk: the AI may map the existing project incorrectly.

Measure the accuracy of the first Recovery snapshot before using it as a source of truth.

### What to review

Review each factual item generated in the initial Recovery docs:

- `docs/00_PROJECT_RULES.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`

### Classification

| Classification | Meaning |
|---|---|
| Correct | Matches the real project state |
| Partially correct | Mostly true, but needs correction or nuance |
| Incorrect | Does not match the real project state |
| Unknown | Cannot be confirmed yet |

### Formulas

```txt
snapshot_accuracy = correct_items / reviewed_items
correction_rate = corrected_items / reviewed_items
corrected_items = partially_correct_items + incorrect_items
reviewed_items = correct_items + partially_correct_items + incorrect_items
```

Unknown items must be tracked separately and must not be counted as correct.

### Log format

| Date | Project | Correct | Partial | Incorrect | Unknown | Snapshot accuracy | Correction rate | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

### Signal

Good sign:

- The AI captures the real state with few corrections.

Warning sign:

- The AI invents architecture, overstates completeness, misses known bugs, or treats assumptions as facts.

## 7. Dogfooding report template

Use this after testing AISDD on a real project.

```txt
# AISDD Dogfooding Report

## Project

TODO

## Period

TODO

## Validation window

- Real tasks completed: TODO
- Different task types: TODO
- Session handoffs: TODO
- Structural decisions: TODO
- Cross-AI continuation tests: TODO
- Recovery snapshots reviewed: TODO

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
| Recovery snapshot accuracy | TODO |

## Changes recommended for AISDD

- TODO
```

## Main rule

AISDD should be judged by real continuity, not by how good the documentation looks.
# AISDD Documentation Maintenance

AISDD uses minimum necessary context during each task, but the full documentation set still needs periodic maintenance.

This document defines when and how to check documents that were not directly read during recent tasks.

## Problem

A task may only require a small set of files, such as:

- `00_PROJECT_RULES.md`
- `04_NEXT_TASK.md`
- `07_HANDOFF.md`
- `09_FILE_INDEX.md`

That keeps context small.

However, documents such as `02_ARCHITECTURE.md`, `03_CURRENT_STATE.md`, or `06_DECISIONS_LOG.md` may become stale if no task explicitly asks the AI to read them.

## Maintenance principle

AISDD separates two activities:

| Activity | Goal |
|---|---|
| Task execution | Load minimum necessary context |
| Documentation maintenance | Periodically audit consistency across docs |

Do not load every document for every task.

Instead, schedule lightweight audits.

## Required audit moments

Run a documentation maintenance audit when any of these happen:

| Trigger | What to check |
|---|---|
| Before a release | All docs relevant to current behavior |
| After architecture changes | `02_ARCHITECTURE.md`, `06_DECISIONS_LOG.md`, `09_FILE_INDEX.md` |
| After data model changes | `01_PRODUCT_SPEC.md`, `02_ARCHITECTURE.md`, `03_CURRENT_STATE.md`, `05_ACCEPTANCE_CHECKS.md` |
| After 5 completed tasks | `03_CURRENT_STATE.md`, `07_HANDOFF.md`, `09_FILE_INDEX.md` |
| After switching AI tools | `07_HANDOFF.md`, `04_NEXT_TASK.md`, `09_FILE_INDEX.md` |
| After repeated bugs | `08_KNOWN_ISSUES.md`, `10_TEST_CHECKLIST.md`, `11_TEST_STRATEGY.md` |

## Suggested audit cadence

| Project level | Cadence |
|---|---|
| Starter | Every 5 meaningful tasks |
| Standard | Every 3 to 5 meaningful tasks |
| Mature | Every release or every 3 meaningful tasks |

A meaningful task is any task that changes behavior, structure, data, tests, or documentation responsibilities.

## Audit checklist

Use this checklist during a maintenance pass:

- [ ] `04_NEXT_TASK.md` contains only one task.
- [ ] `07_HANDOFF.md` reflects the latest completed task.
- [ ] `03_CURRENT_STATE.md` matches actual project state.
- [ ] `09_FILE_INDEX.md` matches the current file structure.
- [ ] `02_ARCHITECTURE.md` matches current modules and contracts.
- [ ] `06_DECISIONS_LOG.md` includes recent structural decisions.
- [ ] `08_KNOWN_ISSUES.md` contains unresolved recurring issues.
- [ ] `10_TEST_CHECKLIST.md` covers known regression risks.
- [ ] `11_TEST_STRATEGY.md` still matches how the project is tested.

## Staleness signals

A document may be stale when:

- code changed but `07_HANDOFF.md` did not;
- architecture files changed but `02_ARCHITECTURE.md` did not;
- new files appeared but `09_FILE_INDEX.md` did not;
- a structural decision was made but no ADR was added;
- bugs repeated but `08_KNOWN_ISSUES.md` stayed unchanged;
- test expectations changed but test docs stayed unchanged.

## Automation support

Use:

```txt
scripts/check-aisdd-docs.py
```

To verify required AISDD files exist.

Use:

```txt
scripts/check-aisdd-staleness.py
```

To detect simple documentation staleness signals from Git history.

## Important limitation

Automated checks can detect signals, not truth.

A script can warn that `07_HANDOFF.md` is older than recent source changes, but a human or AI review still decides whether the document is actually stale.

## AISDD rule

Minimum context is for task execution.

Periodic audits are for documentation consistency.
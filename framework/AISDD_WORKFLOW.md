# AISDD Workflow

AISDD uses short, controlled execution cycles.

## Universal cycle

1. Read `docs/START_HERE.md`.
2. Load only the required documents.
3. Execute one task.
4. Validate acceptance checks.
5. Update affected documentation.
6. Update `docs/07_HANDOFF.md`.
7. End the cycle.

## Reading hierarchy

### Simple task

Read:

- `00_PROJECT_RULES.md`
- `07_HANDOFF.md`
- `09_FILE_INDEX.md`

### New feature

Read:

- `01_PRODUCT_SPEC.md`
- `02_ARCHITECTURE.md`
- `04_NEXT_TASK.md`
- `05_ACCEPTANCE_CHECKS.md`

### Critical change

Read:

- `00_PROJECT_RULES.md`
- `02_ARCHITECTURE.md`
- `03_CURRENT_STATE.md`
- `05_ACCEPTANCE_CHECKS.md`
- `06_DECISIONS_LOG.md`

### Testing task

Read:

- `10_TEST_CHECKLIST.md`
- `11_TEST_STRATEGY.md`

## Cycle constraints

- One task per cycle.
- No unnecessary rewrites.
- No invented contracts.
- No silent architecture changes.
- No undocumented behavior changes.
- No unrelated cleanup.

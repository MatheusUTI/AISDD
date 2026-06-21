# Getting Started with AISDD

AISDD can start simple.

You do not need perfect documentation before the first AI-assisted task.

## Fast path

For the shortest path, read:

- [`QUICK_START.md`](QUICK_START.md)

## 1. Copy the documentation template

Copy:

```txt
templates/docs/
```

Into your project as:

```txt
docs/
```

## 2. Fill only the starter files first

Start with only these files:

| File | Purpose |
|---|---|
| `docs/00_PROJECT_RULES.md` | Permanent rules and forbidden changes |
| `docs/04_NEXT_TASK.md` | One executable task |
| `docs/07_HANDOFF.md` | Short continuity summary |
| `docs/09_FILE_INDEX.md` | Map of important files |

The other documents can stay as TODOs until they are needed.

## 3. Start the first AI cycle

Use:

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

## 4. Keep cycles small

Ask for one task at a time.

Good examples:

- Add one validation rule.
- Fix one bug.
- Extract one helper.
- Add one screen.

Avoid:

- multiple features at once;
- broad refactors;
- architecture changes mixed with feature work;
- vague requests like "improve everything".

## 5. Grow documentation gradually

Fill more docs only when they become useful:

| Need | Document |
|---|---|
| Product behavior | `01_PRODUCT_SPEC.md` |
| Modules and contracts | `02_ARCHITECTURE.md` |
| Real implementation state | `03_CURRENT_STATE.md` |
| Regression control | `05_ACCEPTANCE_CHECKS.md` and `10_TEST_CHECKLIST.md` |
| Structural decisions | `06_DECISIONS_LOG.md` |
| Bugs and limitations | `08_KNOWN_ISSUES.md` |
| Testing rules | `11_TEST_STRATEGY.md` |

## 6. Continue across sessions

At the start of a new session, the AI should read:

- `docs/START_HERE.md`
- `docs/00_PROJECT_RULES.md`
- `docs/07_HANDOFF.md`
- `docs/09_FILE_INDEX.md`
- `docs/04_NEXT_TASK.md`

## Minimum habit

Before each AI task:

1. Put one task in `04_NEXT_TASK.md`.
2. Run the AI cycle.
3. Review the result.
4. Update `07_HANDOFF.md`.
5. Commit the change.
# How to Adopt AISDD in an Existing Project

Adopting AISDD should not interrupt development.

Start small, protect the project, and improve documentation as the project evolves.

## The simple adoption rule

Do not document the whole project at once.

Document only what the AI needs to safely execute the next task.

## Step 1 — Add AISDD docs

Copy:

```txt
templates/docs/
```

Into the existing project as:

```txt
docs/
```

## Step 2 — Fill the starter files

Fill only:

| File | Minimum content |
|---|---|
| `00_PROJECT_RULES.md` | Stack, conventions, forbidden changes |
| `04_NEXT_TASK.md` | One clear task |
| `07_HANDOFF.md` | Current project summary in a few lines |
| `09_FILE_INDEX.md` | Main files and responsibilities |

Leave the remaining files as TODOs at first.

## Step 3 — Define the first safe task

The first task should be small.

Good first tasks:

- fix one known bug;
- add one validation;
- document current file structure;
- extract one helper;
- add one simple feature.

Avoid first tasks that change architecture, rewrite large files, or combine many goals.

## Step 4 — Run the first controlled AI cycle

Use this prompt:

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
Do not invent missing files, contracts, endpoints, tables, or business rules.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

## Step 5 — Review before accepting

Check:

- Did the AI execute only one task?
- Did it change only necessary files?
- Did it preserve existing behavior?
- Did it list FACTS, ASSUMPTIONS, UNKNOWNS, and RISKS?
- Did it update handoff?

## Step 6 — Expand only when needed

Fill more documentation when the project demands it:

| Situation | Add detail to |
|---|---|
| Product rules become unclear | `01_PRODUCT_SPEC.md` |
| Architecture becomes relevant | `02_ARCHITECTURE.md` |
| Current state is hard to infer | `03_CURRENT_STATE.md` |
| Regressions appear | `05_ACCEPTANCE_CHECKS.md` and `10_TEST_CHECKLIST.md` |
| Decisions need traceability | `06_DECISIONS_LOG.md` |
| Bugs repeat | `08_KNOWN_ISSUES.md` |
| Tests become important | `11_TEST_STRATEGY.md` |

## Adoption promise

AISDD should reduce chaos, not create bureaucracy.
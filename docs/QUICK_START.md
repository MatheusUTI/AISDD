# AISDD Quick Start

Adopt AISDD without stopping your project.

The goal is not to document everything before coding.

The goal is to give the AI enough persistent context to work safely.

## The 5-minute path

### 1. Copy the docs template

From the AISDD repository, copy:

```txt
templates/docs/
```

Into your project as:

```txt
docs/
```

### 2. Fill only four files first

You do not need to complete every document before using AISDD.

Start with:

| File | What to write |
|---|---|
| `00_PROJECT_RULES.md` | Stack, forbidden changes, permanent conventions |
| `04_NEXT_TASK.md` | One clear task only |
| `07_HANDOFF.md` | Current short project summary |
| `09_FILE_INDEX.md` | Main files and what they do |

Leave the other files with TODOs until they become necessary.

### 3. Start the AI with one prompt

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
Do not invent missing files, contracts, endpoints, tables, or business rules.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

### 4. Keep every cycle small

Good task:

```txt
Add validation to the customer form.
```

Bad task:

```txt
Refactor the app, improve the UI, add auth, fix bugs, and optimize everything.
```

## Starter rule

AISDD Starter means:

- copy the full docs structure;
- fill only the minimum required files;
- execute one task;
- update handoff;
- improve documentation gradually.

## When to fill the remaining docs

| Document | Fill when |
|---|---|
| `01_PRODUCT_SPEC.md` | Product rules start becoming important |
| `02_ARCHITECTURE.md` | Multiple modules or contracts exist |
| `03_CURRENT_STATE.md` | The project already has meaningful implementation |
| `05_ACCEPTANCE_CHECKS.md` | Regressions start becoming risky |
| `06_DECISIONS_LOG.md` | You make a structural decision |
| `08_KNOWN_ISSUES.md` | You find recurring bugs or limitations |
| `10_TEST_CHECKLIST.md` | You need repeatable manual checks |
| `11_TEST_STRATEGY.md` | Automated tests or release checks matter |

## Minimum cycle

For every task:

1. Update `04_NEXT_TASK.md`.
2. Ask the AI to execute it.
3. Review the result.
4. Update `07_HANDOFF.md`.
5. Commit.

## Main promise

AISDD should make AI-assisted development safer without making adoption heavy.
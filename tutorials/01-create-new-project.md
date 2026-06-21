# Tutorial 01 — Create a New AISDD Project

## Goal

Create a new project using AISDD from day one.

## If the project is not clear yet

If you do not know what to put in `01_PRODUCT_SPEC.md` or `02_ARCHITECTURE.md`, do not guess.

Use the Project Definition Wizard first:

```txt
templates/prompts/PROJECT_DEFINITION_WIZARD_PROMPT.md
```

The wizard should interview you, identify unknowns, and generate the first AISDD docs before development starts.

## Steps

1. Create your software project.
2. Copy `templates/docs/` into the project as `docs/`.
3. Fill `00_PROJECT_RULES.md` with stack, conventions, and forbidden changes.
4. Fill `04_NEXT_TASK.md` with one small first task.
5. Fill `07_HANDOFF.md` with a short initial state summary.
6. Fill `09_FILE_INDEX.md` with the main files, if they already exist.
7. Fill `01_PRODUCT_SPEC.md` and `02_ARCHITECTURE.md` only with confirmed information.
8. Ask the AI to read `START_HERE.md`.

## First AI request

```txt
This project follows AISDD.
Read docs/START_HERE.md and execute docs/04_NEXT_TASK.md.
```

## Check

Before coding starts, confirm:

- `04_NEXT_TASK.md` has only one task;
- unknown product or architecture details are marked as `UNKNOWNS` or `TODO`;
- the AI is not asked to invent missing rules.
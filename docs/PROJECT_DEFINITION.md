# AISDD Project Definition

Use this flow when you have an idea but the project is not defined yet.

The goal is to let an AI interview you, identify what is missing, and produce the first AISDD documentation set.

## When to use

Use this when:

- the project does not exist yet;
- the idea is still rough;
- you do not know which docs to fill first;
- you want the AI to ask the right questions before development starts.

For an existing project, use `HOW_TO_ADOPT.md` instead.

## Flow

1. Copy the Project Definition Wizard prompt.
2. Give the AI a short description of the idea.
3. Let the AI ask questions in small groups.
4. Answer what you know.
5. Let the AI mark unknowns explicitly.
6. Generate the initial AISDD docs.
7. Start development from `docs/04_NEXT_TASK.md`.

## Required output from the AI

The AI should generate draft content for:

- `docs/START_HERE.md`
- `docs/00_PROJECT_RULES.md`
- `docs/01_PRODUCT_SPEC.md`
- `docs/02_ARCHITECTURE.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/05_ACCEPTANCE_CHECKS.md`
- `docs/06_DECISIONS_LOG.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`
- `docs/10_TEST_CHECKLIST.md`
- `docs/11_TEST_STRATEGY.md`

The docs do not need to be perfect.

They need to be clear enough to safely start the first development cycle.

## Interview areas

The AI should ask only what is needed to begin safely.

Recommended areas:

| Area | Purpose |
|---|---|
| Product | Problem, users, core value, scope |
| Features | Main flows and first usable version |
| Rules | Business rules, constraints, forbidden behavior |
| Technology | Preferred stack, platform, storage, integrations |
| Data | Main entities, fields, imports, exports |
| UX | Screens, navigation, user actions |
| Quality | Tests, acceptance checks, regression risks |
| Delivery | First milestone and next task |

## Question discipline

The AI should not ask everything at once.

It should ask questions in small groups and stop when enough information exists for a safe initial version.

## Unknowns are allowed

AISDD does not require all answers before starting.

Unknowns must be recorded explicitly in the generated docs.

Examples:

```txt
UNKNOWNS
- Final pricing model is not defined.
- Authentication provider is not selected.
- Export format needs confirmation.
```

## First task rule

The generated `04_NEXT_TASK.md` must contain only one executable task.

Good first task:

```txt
Create the initial project skeleton with the selected stack and AISDD docs.
```

Bad first task:

```txt
Build the entire product.
```

## Recommended prompt

Use:

```txt
templates/prompts/PROJECT_DEFINITION_WIZARD_PROMPT.md
```

## Main promise

The user should be able to start with only an idea.

The AI should guide the discovery and produce the first AISDD-ready project definition.
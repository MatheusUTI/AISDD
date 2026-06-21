# START_HERE

This is the entry point for every AI, developer, or automation agent working on this project.

## Required behavior

Before making changes:

1. Read this file.
2. Read `00_PROJECT_RULES.md`.
3. Read `07_HANDOFF.md`.
4. Read `09_FILE_INDEX.md`.
5. Read `04_NEXT_TASK.md` before executing any task.

## AISDD rules

- The repository is the source of truth.
- The conversation is not the source of truth.
- Execute one task per cycle.
- Do not invent missing contracts.
- Do not rewrite files unnecessarily.
- Update affected documentation.
- Update handoff before ending the cycle.

## Required AI response format

Every implementation response must contain:

- Objective
- Files changed
- Contract impact
- FACTS
- ASSUMPTIONS
- UNKNOWNS
- RISKS
- Acceptance status
- Updated handoff

## Missing information rule

If critical information is missing, answer:

```txt
MISSING INFO
```

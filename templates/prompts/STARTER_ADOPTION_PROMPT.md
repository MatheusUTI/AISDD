# AISDD Starter Adoption Prompt

Use this prompt when adopting AISDD in a new or existing project.

```txt
This project follows AISDD.

Read docs/START_HERE.md first.
Then read only the minimum starter context:

- docs/00_PROJECT_RULES.md
- docs/04_NEXT_TASK.md
- docs/07_HANDOFF.md
- docs/09_FILE_INDEX.md

Execute only docs/04_NEXT_TASK.md.

Rules:

- Do not invent missing files, contracts, endpoints, tables, schemas, or business rules.
- Do not rewrite unrelated files.
- Do not change the stack unless explicitly required.
- Preserve existing behavior.
- Update affected documentation.
- Update docs/07_HANDOFF.md before finishing.

If critical information is missing, answer only:

MISSING INFO

Return the response using this structure:

## Objective

## Files changed

## Contract impact

## FACTS

## ASSUMPTIONS

## UNKNOWNS

## RISKS

## Acceptance status

## Updated handoff
```

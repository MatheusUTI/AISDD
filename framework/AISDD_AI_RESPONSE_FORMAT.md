# AISDD AI Response Format

Every AI response that changes a project should use the following structure.

## Objective

State the task objective in one or two sentences.

## Files changed

List changed files and why each file changed.

## Contract impact

State whether the change affects public contracts, APIs, schemas, rules, file formats, routes, or user-facing behavior.

## FACTS

List information directly observed in the repository.

## ASSUMPTIONS

List assumptions adopted during the task.

## UNKNOWNS

List missing information.

If critical information is missing, do not proceed. Answer:

```txt
MISSING INFO
```

## RISKS

List possible regressions or impacts.

## Acceptance status

State whether acceptance checks passed, failed, or were not run.

## Updated handoff

Provide a short continuation summary suitable for `docs/07_HANDOFF.md`.

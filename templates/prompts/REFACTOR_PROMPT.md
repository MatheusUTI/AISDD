# AISDD Safe Refactor Prompt

Perform a safe refactor under AISDD rules.

Refactor only when it makes the next task safer, clearer, or easier to maintain.

## Rules

- Preserve behavior.
- Do not change public contracts unless explicitly required.
- Do not change persistence, schemas, APIs, or business rules unless explicitly required.
- Prefer extraction over rewrite.
- Keep changes small.
- Refactor only files required for the task.
- Update file index if responsibilities change.
- Report `FILE GROWTH RISK` if applicable.

## When not to refactor

Do not refactor when:

- the task can be completed safely without structural change;
- behavior is unclear and no acceptance checks exist;
- the file is large but stable and the requested task is unrelated;
- the refactor would require changing multiple contracts at once;
- the refactor depends on unconfirmed business rules;
- the user asked for a bug fix and refactor would increase regression risk;
- the change would become a rewrite disguised as cleanup.

If refactor is useful but too risky for the current task, report:

```txt
REFACTOR DEFERRED
```

Then explain the safer follow-up task.

## File growth guidance

If a file is near or above the recommended size limit, do not automatically rewrite it.

Instead:

1. Report `FILE GROWTH RISK`.
2. Identify the smallest safe extraction.
3. Confirm whether the extraction is required for the current task.
4. If not required, defer it as a separate task.

## Required output

## Objective

## Files changed

## Contract impact

## FACTS

## ASSUMPTIONS

## UNKNOWNS

## RISKS

## Acceptance status

## Updated handoff
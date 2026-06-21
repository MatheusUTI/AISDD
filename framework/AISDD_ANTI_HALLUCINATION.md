# AISDD Anti-Hallucination Strategy

AISDD prevents hallucinations by forcing explicit separation between known and unknown information.

## Required sections

Every AI task response must distinguish:

- FACTS
- ASSUMPTIONS
- UNKNOWNS
- RISKS

## Never invent

The AI must never invent:

- files;
- modules;
- tables;
- endpoints;
- environment variables;
- business rules;
- external contracts;
- architecture decisions;
- test results.

## Missing critical information

If critical information is missing, the AI must answer:

```txt
MISSING INFO
```

The AI may proceed only when the missing information is not critical and the assumption is explicitly documented.

## Critical vs assumable information

Not every unknown should block the task.

Use this calibration:

| Type | Meaning | AI behavior |
|---|---|---|
| Critical | Missing information could cause wrong behavior, broken contracts, data loss, security risk, or major rework | Stop with `MISSING INFO` |
| Assumable | A reasonable default can be chosen and changed later with low risk | Proceed and document the assumption |
| Cosmetic | Preference-level detail with little functional impact | Choose a simple default and document only if relevant |

## When to stop

Stop with `MISSING INFO` when the missing information affects:

- business rules;
- data model or migrations;
- public API or external contract;
- authentication, authorization, security, or privacy;
- irreversible file or data operations;
- architecture direction;
- acceptance criteria.

## When to proceed

Proceed with an explicit assumption when the missing information is:

- naming preference;
- copy text;
- visual detail;
- temporary placeholder;
- low-risk implementation detail;
- easily reversible choice.

## Evidence hierarchy

Prefer information from:

1. Current repository files.
2. Current task file.
3. Architecture documentation.
4. Product specification.
5. Explicit user instruction.
6. Clearly marked assumptions.

## Forbidden behavior

- Silently filling gaps.
- Rewriting unrelated files.
- Changing contracts without mention.
- Claiming tests passed without running or inspecting them.
- Using conversation memory as the only source of truth.
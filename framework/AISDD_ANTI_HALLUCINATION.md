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

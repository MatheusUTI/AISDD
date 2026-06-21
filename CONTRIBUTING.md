# Contributing to AISDD

AISDD is a framework for predictable AI-assisted software development.

Contributions should improve clarity, safety, repeatability, validation, or adoption.

## Contribution principles

- Keep the framework technology-independent.
- Do not bind AISDD to a specific AI vendor.
- Prefer small, traceable changes.
- Avoid unnecessary complexity.
- Preserve the anti-hallucination discipline.
- Update affected documentation when changing rules or workflow.

## Pull request checklist

Before opening a pull request, confirm:

- The change has a clear objective.
- The change does not contradict AISDD principles.
- Affected documents were updated.
- Examples still make sense.
- New concepts are explained in plain language.
- If the change affects core rules, validation evidence is included or linked.

## Core rule change policy

Core rules include changes to:

- AISDD principles;
- anti-hallucination behavior;
- `MISSING INFO` policy;
- required documentation structure;
- AI response format;
- task execution cycle;
- validation metrics;
- vendor or stack independence.

## What counts as sufficient validation

Before merging a core rule change, provide at least one of:

| Evidence type | Minimum |
|---|---|
| Dogfooding report | 10 real tasks and 3 task types |
| Cross-AI continuation test | 1 documented successful or failed test |
| Repeated failure evidence | 3 similar failures with notes |
| Safety issue | 1 clear case involving data loss, broken contract, security/privacy risk, or workflow deadlock |

For early-stage AISDD, the maintainer decides whether the evidence is sufficient.

As the project grows, this policy should evolve into a more formal governance model.

## Maintainer decision rule

A maintainer may accept small documentation improvements without full validation if they do not change framework behavior.

A maintainer should require validation evidence when a change affects how AISDD tells AIs to behave.

## Suggested contribution types

- Template improvements.
- Better onboarding docs.
- Example projects.
- Testing strategy improvements.
- Agent integration patterns.
- Translations.
- Dogfooding reports.
- Validation tooling.
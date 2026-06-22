# AISDD Core vs Advanced

AISDD should be useful without forcing users to adopt the whole framework at once.

This document separates what is essential from what is optional, advanced, or maturity-driven.

## Packages vs layers

AISDD uses two related terms:

| Term | Meaning |
|---|---|
| Package | What you copy or maintain in a project |
| Layer | Capability you add when the project needs it |

They usually match:

| Package | Corresponding layer |
|---|---|
| Core Kit | Core layer |
| Recovery Kit | Recovery layer |
| Standard Kit | Product and architecture layers |
| Mature Kit | Maturity layer |

If you are deciding what to copy, read `docs/ADOPTION_PACKAGES.md` first.

If you are deciding what capability to add next, use this document.

## Core AISDD

Use this when you want to start today.

| Artifact | Purpose |
|---|---|
| `docs/00_PROJECT_RULES.md` | Permanent rules, stack, conventions, and forbidden changes |
| `docs/04_NEXT_TASK.md` | One executable task only |
| `docs/07_HANDOFF.md` | Short continuity summary between sessions and AIs |
| `docs/09_FILE_INDEX.md` | Map of important files and responsibilities |

Core AISDD answers four questions:

1. What rules must the AI follow?
2. What is the next task?
3. What should the next AI session know?
4. Where are the important files?

## Core AI behavior

Every AI cycle should also preserve:

- one task per cycle;
- minimum necessary context;
- no silent invention;
- explicit `FACTS`, `ASSUMPTIONS`, `UNKNOWNS`, and `RISKS`;
- updated handoff before the cycle ends.

## Safety layer

Use this when regressions, hallucinations, or unclear requirements become risky.

| Artifact | Purpose |
|---|---|
| `docs/05_ACCEPTANCE_CHECKS.md` | Required checks before accepting a change |
| `docs/08_KNOWN_ISSUES.md` | Bugs, risks, limitations, and technical debt |
| `docs/10_TEST_CHECKLIST.md` | Repeatable manual regression checklist |
| `framework/AISDD_ANTI_HALLUCINATION.md` | Rules for missing information and hallucination prevention |
| `framework/AISDD_FILE_GROWTH_CONTROL.md` | File growth limits and extraction triggers |

## Product and architecture layer

Use this when the project has real business rules, modules, contracts, or integration risks.

| Artifact | Purpose |
|---|---|
| `docs/01_PRODUCT_SPEC.md` | Product scope, users, features, and business rules |
| `docs/02_ARCHITECTURE.md` | Architecture, modules, contracts, flows, and boundaries |
| `docs/03_CURRENT_STATE.md` | Real project state, not the idealized state |
| `docs/06_DECISIONS_LOG.md` | ADR-style decision history |

## Engineering guardrails layer

Use this when AI can generate code faster than the project can safely validate it.

This layer is especially important when:

- the project is moving toward production use;
- user data, business data, money, logistics, scheduling, or shared resources are involved;
- manual testing is becoming insufficient;
- performance, scale, concurrency, or security risks exist;
- the project uses an LLM at runtime;
- privacy or LGPD-like requirements may apply.

| Artifact | Purpose |
|---|---|
| `docs/ENGINEERING_GUARDRAILS.md` | Engineering, testing, security, privacy, and responsibility guardrails for AI-assisted software |
| `docs/11_TEST_STRATEGY.md` | Defines how automated and manual testing should evolve |
| `docs/05_ACCEPTANCE_CHECKS.md` | Converts expected behavior into repeatable acceptance checks |
| `docs/08_KNOWN_ISSUES.md` | Records risks, technical debt, and limitations explicitly |
| `docs/06_DECISIONS_LOG.md` | Records architecture/security trade-offs and accepted risks |

Engineering guardrails answer five questions:

1. What could break beyond the happy path?
2. What proves the change did not regress existing behavior?
3. What security, privacy, or data risks exist?
4. What assumptions may fail under scale, concurrency, or production use?
5. Who is responsible for accepting the AI-generated change?

## Recovery layer

Use this when the project already exists and was not started with AISDD.

| Artifact | Purpose |
|---|---|
| `docs/RECOVERY_MODE.md` | Recovery path for existing complex projects |
| `templates/prompts/RECOVERY_MODE_PROMPT.md` | Prompt for creating the first factual snapshot |
| `docs/DOGFOODING_METRICS.md` | Snapshot accuracy metric |

Recovery should start with a read-only factual snapshot before any code change.

## Maturity layer

Use this when the project becomes long-running, team-based, public, or heavily AI-assisted.

| Artifact | Purpose |
|---|---|
| `docs/DOCUMENTATION_MAINTENANCE.md` | Periodic audit rules and stale-doc prevention |
| `docs/DOGFOODING_METRICS.md` | Metrics for validating AISDD in practice |
| `scripts/check-aisdd-docs.py` | Checks required docs exist |
| `scripts/check-aisdd-staleness.py` | Detects simple stale-documentation signals |
| `docs/ROADMAP.md` | Framework priorities |

## Simple rule

Start with Core.

Add the next layer only when the project pain requires it.

AISDD should reduce chaos, not create ceremony.

# AISDD — AI Spec-Driven Development Framework

**AISDD** is a universal framework for building long-term software projects with AI assistance.

It is designed to be:

- language-independent;
- stack-independent;
- vendor-independent;
- reusable across projects;
- resistant to hallucinations;
- optimized for low context and token usage;
- suitable for long-running projects;
- compatible with multiple AIs working on the same repository.

Compatible AI tools include ChatGPT, Gemini, Claude, Cursor, Windsurf, Copilot, local agents, and future AI systems.

## The problem

Long AI-assisted projects often suffer from:

- excessive conversation context;
- high token consumption;
- lost continuity between sessions;
- hallucinated code;
- unnecessary rewrites;
- regressions;
- lack of traceability;
- difficulty switching between AI tools.

AISDD exists to solve these problems.

## Core idea

The AI conversation is not the source of truth.

The repository is the source of truth.

Every important project rule, decision, contract, task, known issue, and handoff must exist persistently inside the repository.

## Philosophy

More context does not automatically produce better results.

AISDD avoids giant prompts and instead uses persistent specification files that allow every task to load only the minimum required context.

## Universal documentation structure

Every AISDD project should contain:

```txt
docs/
├─ START_HERE.md
├─ 00_PROJECT_RULES.md
├─ 01_PRODUCT_SPEC.md
├─ 02_ARCHITECTURE.md
├─ 03_CURRENT_STATE.md
├─ 04_NEXT_TASK.md
├─ 05_ACCEPTANCE_CHECKS.md
├─ 06_DECISIONS_LOG.md
├─ 07_HANDOFF.md
├─ 08_KNOWN_ISSUES.md
├─ 09_FILE_INDEX.md
├─ 10_TEST_CHECKLIST.md
└─ 11_TEST_STRATEGY.md
```

## AISDD execution cycle

1. Read `docs/START_HERE.md`.
2. Load only the documents required for the current task.
3. Execute only one task.
4. Validate acceptance checks.
5. Update impacted documentation.
6. Update handoff.
7. End the cycle.

## Universal AI response format

Every AI response should contain:

- Objective
- Files changed
- Contract impact
- FACTS
- ASSUMPTIONS
- UNKNOWNS
- RISKS
- Acceptance status
- Updated handoff

## Anti-hallucination rule

The AI must never silently fill missing information.

If critical information is missing, it must answer:

```txt
MISSING INFO
```

## Repository structure

```txt
framework/    Core AISDD method and rules
templates/    Reusable project templates and prompts
examples/     Example AISDD projects
docs/         Public adoption documentation
tutorials/    Step-by-step guides
```

## Status

AISDD is currently in early development.

The goal is to evolve it into an open-source standard for predictable, traceable, long-term AI-assisted software development.

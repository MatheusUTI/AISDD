# AISDD Manifesto

AISDD — AI Spec-Driven Development Framework — exists to make AI-assisted software development predictable, traceable, and sustainable over long periods.

## Core belief

The repository must be the source of truth.

The AI conversation is temporary. The repository is persistent.

A project should not depend on a single chat history, a single AI vendor, or a single developer's memory to continue evolving safely.

## Why AISDD exists

AI can accelerate software development, but uncontrolled AI usage often creates hidden technical debt:

- hallucinated files;
- invented contracts;
- duplicated logic;
- regressions;
- oversized prompts;
- inconsistent decisions;
- unnecessary rewrites;
- fragile continuity.

AISDD turns AI-assisted development into a controlled engineering process.

## What AISDD optimizes for

AISDD optimizes for:

- continuity;
- traceability;
- context efficiency;
- incremental evolution;
- safety against hallucinations;
- compatibility with multiple AI tools;
- long-term maintainability.

AISDD does not optimize for one-shot code generation at the cost of future control.

## Main rule

AI should not guess silently.

When critical information is missing, the AI must stop and report:

```txt
MISSING INFO
```

## Project memory

AISDD moves project memory from the AI conversation into versioned files.

This allows any AI, developer, or automation agent to continue the project by reading the repository.

## Engineering stance

AISDD is not a prompt collection.

AISDD is an engineering workflow based on persistent specification, controlled execution, and documented continuity.

# Problem-First Start

AISDD can be used by developers, teams, agents, and advanced technical workflows.

But the simplest way to start is not by learning the whole framework.

The simplest way to start is by describing a real problem and letting an LLM guide the first structure using AISDD principles.

## Purpose

Problem-First Start exists for people who have a real problem to solve but do not want to carry the full cognitive load of software engineering before beginning.

This includes:

- domain experts;
- operations professionals;
- business owners;
- students;
- solo builders;
- non-programmers;
- developers starting a new project;
- teams trying to organize unclear requirements.

AISDD should not make the beginning heavier.

AISDD should help the user move from problem to structure.

```txt
You do not need to start with technology.
You can start with the problem.
```

## Two valid modes

AISDD supports two complementary usage modes.

| Mode | Best for | How it works |
|---|---|---|
| Problem-First Mode | Users who have a problem but little structure | The LLM asks questions, extracts rules, and creates the first AISDD documents |
| Developer Mode | Developers, agents, and advanced users | The user works directly with AISDD docs, templates, tasks, checks, and guardrails |

Problem-First Mode is not a weaker version of AISDD.

It is the lowest-friction entrypoint.

Developer Mode remains the deepest and most powerful way to use the framework.

## Minimal user flow

```txt
Real problem
↓
Initial questionnaire
↓
LLM organizes the answers
↓
First AISDD docs
↓
One safe next task
↓
Implementation cycle
↓
Validation
↓
Handoff
```

## What the user needs

The user does not need to know the full stack, architecture, database model, or programming language before starting.

The user does need to provide honest answers about:

- what hurts;
- who is affected;
- how the process works today;
- what must happen;
- what must never happen;
- what defines success;
- what is still unknown.

## Initial questionnaire

Use this questionnaire when starting from a problem instead of an existing project.

### 1. Problem

What problem are you trying to solve?

Describe it in normal language.

### 2. Current process

How is this problem handled today?

Mention tools, people, spreadsheets, messages, manual steps, systems, or workarounds.

### 3. Users

Who will use the software?

Who benefits from it?

Who may be affected by mistakes?

### 4. Pain

What makes the current process slow, risky, expensive, confusing, or repetitive?

### 5. Desired result

What should the software help you do?

Describe the expected outcome, not the technology.

### 6. Rules

What rules must the software respect?

Examples:

- deadlines;
- approvals;
- limits;
- statuses;
- calculations;
- required fields;
- business exceptions.

### 7. Forbidden outcomes

What must never happen?

Examples:

- losing data;
- duplicating records;
- changing past history silently;
- approving something without confirmation;
- exposing sensitive information.

### 8. Inputs

What information enters the system?

Examples:

- forms;
- spreadsheets;
- PDFs;
- emails;
- manual entries;
- API data;
- barcode scans;
- photos.

### 9. Outputs

What should the system produce?

Examples:

- screens;
- reports;
- alerts;
- exports;
- dashboards;
- histories;
- notifications.

### 10. Validation

How will you know the first version worked?

List observable checks.

### 11. Constraints

What limitations exist?

Examples:

- must work offline;
- must run on Android;
- must use Excel files;
- must be local-only;
- must avoid paid services;
- must be easy for non-technical users.

### 12. Unknowns

What do you still not know?

Unknowns are allowed.

AISDD requires them to be named instead of hidden.

## Starter prompt for an LLM

Copy this prompt into ChatGPT, Gemini, Claude, AI Studio, Cursor, or another LLM.

```txt
I want to start a software project using AISDD in Problem-First Mode.

Do not write code yet.

Your job is to interview me, one small group of questions at a time, and transform my answers into an initial AISDD project structure.

Rules:
- Start from the problem, not the technology.
- Ask concise questions.
- Do not assume business rules silently.
- Separate FACTS, ASSUMPTIONS, UNKNOWNS, and RISKS.
- If critical information is missing, ask before proceeding.
- Keep cognitive load low.
- At the end, generate the first versions of:
  - docs/00_PROJECT_RULES.md
  - docs/01_PRODUCT_SPEC.md
  - docs/03_CURRENT_STATE.md
  - docs/04_NEXT_TASK.md
  - docs/05_ACCEPTANCE_CHECKS.md
  - docs/07_HANDOFF.md
  - docs/09_FILE_INDEX.md

The first implementation task must be small, testable, and safe.
```

## What the LLM should produce

At the end of the interview, the LLM should produce:

```txt
docs/
├─ 00_PROJECT_RULES.md
├─ 01_PRODUCT_SPEC.md
├─ 03_CURRENT_STATE.md
├─ 04_NEXT_TASK.md
├─ 05_ACCEPTANCE_CHECKS.md
├─ 07_HANDOFF.md
└─ 09_FILE_INDEX.md
```

The output does not need to be perfect.

It needs to be honest, useful, and safe enough to start.

## When to move to Developer Mode

Move deeper into Developer Mode when:

- the project already has code;
- multiple features exist;
- regressions are becoming likely;
- architecture decisions matter;
- tests are needed;
- multiple LLMs or agents are being used;
- other people will contribute;
- deployment or real users are involved.

Developer Mode adds the full power of AISDD:

- complete docs structure;
- Recovery Mode;
- Prompt Maturity Levels;
- Engineering Guardrails;
- dogfooding metrics;
- staleness checks;
- stricter handoff and acceptance rules.

## Principle

AISDD is not about making non-programmers pretend to be software engineers.

AISDD is about allowing more people to participate meaningfully in software creation.

```txt
AI can help implement.
AISDD helps organize and preserve knowledge.
The human remains responsible for validation and decisions.
```

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

## Interview, not form filling

The initial questionnaire is not something the user must answer alone.

For many users, especially beginners, a formal questionnaire will be too hard at the beginning.

That is expected.

The LLM should use the questionnaire as an internal guide and interview the user gradually.

```txt
The interviewer extracts structure.
The user provides reality.
```

If the user says "I don't know", the LLM should register the answer as `UNKNOWN` and continue with a smaller question.

See: [`docs/INTERVIEW_MODE.md`](INTERVIEW_MODE.md)

## Two valid modes

AISDD supports two complementary usage modes.

| Mode | Best for | How it works |
|---|---|---|
| Problem-First Mode | Users who have a problem but little structure | The LLM asks adaptive questions, extracts rules, and creates the first AISDD documents |
| Developer Mode | Developers, agents, and advanced users | The user works directly with AISDD docs, templates, tasks, checks, and guardrails |

Problem-First Mode is not a weaker version of AISDD.

It is the lowest-friction entrypoint.

Developer Mode remains the deepest and most powerful way to use the framework.

## Minimal user flow

```txt
Real problem
↓
Guided interview
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

Partial answers are allowed.

Uncertainty is allowed.

The LLM must not force fake certainty.

## Internal questionnaire

Use this questionnaire as an internal interview guide when starting from a problem instead of an existing project.

Do not ask all questions at once.

Ask one question at a time for beginners.

Ask at most three questions at a time for experienced users.

### 1. Situation

Which option best describes the user's situation?

- only an idea;
- real problem, no software yet;
- existing prototype;
- messy or fragile project;
- developer starting a structured project;
- unsure.

### 2. Problem

What problem is the user trying to solve?

Allow normal language.

### 3. Current process or current state

For new projects: how is this handled today?

For existing projects: what exists now and what is difficult to continue?

### 4. Users

Who will use the software?

Who benefits from it?

Who may be affected by mistakes?

### 5. Pain

What makes the current process slow, risky, expensive, confusing, or repetitive?

### 6. Desired result

What should the software help the user do?

Focus on outcome, not technology.

### 7. Rules

What rules must the software respect?

Examples:

- deadlines;
- approvals;
- limits;
- statuses;
- calculations;
- required fields;
- business exceptions.

### 8. Forbidden outcomes

What must never happen?

Examples:

- losing data;
- duplicating records;
- changing past history silently;
- approving something without confirmation;
- exposing sensitive information.

### 9. Inputs

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

### 10. Outputs

What should the system produce?

Examples:

- screens;
- reports;
- alerts;
- exports;
- dashboards;
- histories;
- notifications.

### 11. Validation

How will the user know the first version helped?

List observable checks.

### 12. Constraints

What limitations exist?

Examples:

- must work offline;
- must run on Android;
- must use Excel files;
- must be local-only;
- must avoid paid services;
- must be easy for non-technical users.

### 13. Unknowns

What is still unknown?

Unknowns are allowed.

AISDD requires them to be named instead of hidden.

## Starter prompt for an LLM

Copy this prompt into ChatGPT, Gemini, Claude, AI Studio, Cursor, or another LLM.

```txt
I want to start or organize a software project using AISDD Interview Mode.

Do not write code yet.

Your job is to interview me and transform my answers into an initial AISDD project structure.

Core rules:
- Start from the problem or current project state, not from technology.
- Keep cognitive load low.
- Ask one question at a time if I sound beginner or uncertain.
- Ask at most three questions at a time if I sound technical or experienced.
- Prefer simple language and concrete examples.
- Do not use jargon unless I demonstrate technical fluency.
- Do not assume business rules silently.
- Do not ask about architecture, database, APIs, stack, or folder structure before the problem is understood.
- Do not generate code during the interview.
- Do not generate a large architecture before the problem is understood.
- Accept "I don't know" as a valid answer and register it as UNKNOWN.
- Separate FACTS, ASSUMPTIONS, UNKNOWNS, and RISKS.
- If critical information is missing, ask a smaller follow-up question.

First, classify my situation by asking:

Which option is closest to your situation?

1. I only have an idea.
2. I have a real problem, but no software yet.
3. I already have a project or prototype.
4. I have code, but it is messy or hard to continue.
5. I am a developer and want to start in a structured way.
6. I am not sure.

Then adapt the interview.

Stop the interview when you have enough information to define one safe next task.

At the end, generate the first versions of:
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

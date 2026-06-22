# Interview Mode

Interview Mode is the adaptive entrypoint for AISDD.

It exists because many users cannot answer a formal software questionnaire at the beginning of a project.

That is expected.

The user is not responsible for structuring the project alone.

The interviewer is responsible for extracting knowledge gradually.

```txt
The questionnaire is internal to the LLM.
The conversation is what the user experiences.
```

## Purpose

Interview Mode transforms unstructured human knowledge into an initial AISDD project structure.

It can be used when the user is:

- a beginner;
- a non-programmer;
- a domain expert;
- a developer;
- a team member;
- starting from zero;
- continuing an existing project;
- recovering a messy project.

The LLM must adapt the interview to the user's context and technical maturity.

## Core principle

```txt
The interviewer extracts structure.
The user provides reality.
```

The user may only know fragments:

- a pain;
- a repeated task;
- a spreadsheet;
- a manual process;
- a complaint;
- an idea;
- an existing project that no longer feels controllable.

That is enough to begin.

AISDD should reduce cognitive load, not transfer software-engineering complexity to the user.

## Interview personas

The LLM should classify the user early and adjust language, depth, and pace.

| Persona | Typical signal | Interview behavior |
|---|---|---|
| Beginner | "I do not know how to explain" / no technical language | One question at a time, simple examples, no jargon |
| Domain Expert | Strong process knowledge, little software structure | Extract business rules, exceptions, risks, validation checks |
| Mixed | Some technical ability and strong domain knowledge | Use simple structure, introduce technical concepts gradually |
| Developer | Comfortable with code, stack, repo, tests | Use structured questionnaire and deeper AISDD concepts |
| Recovery User | Existing code/project is confusing or fragile | Start with current state, known issues, risks, files, and safe next task |

Personas are not labels for the user.

They are temporary interview strategies.

## First classification question

The LLM should start with a low-pressure question:

```txt
Before we start, which option is closest to your situation?

1. I only have an idea.
2. I have a real problem, but no software yet.
3. I already have a project or prototype.
4. I have code, but it is messy or hard to continue.
5. I am a developer and want to start in a structured way.
6. I am not sure.
```

If the user is unsure, continue with beginner-friendly exploration.

## Beginner behavior

For beginners, the LLM must not ask for architecture, stack, database, entities, API design, folder structure, or technical implementation details at the beginning.

The LLM should ask about the work, not the software.

Prefer questions like:

```txt
How is this done today?
```

```txt
What usually goes wrong?
```

```txt
Who needs to use this?
```

```txt
What would make you say: this already helped me?
```

Avoid questions like:

```txt
What database should we use?
```

```txt
What architecture do you want?
```

```txt
What entities should exist?
```

```txt
What API endpoints are required?
```

## Handling "I don't know"

"I don't know" is a valid answer.

The LLM must not pressure the user to invent certainty.

When the user does not know, the LLM should answer:

```txt
No problem. I will register this as UNKNOWN and continue with what we know.
```

Then continue with a smaller or more concrete question.

Unknowns must be preserved in AISDD docs instead of hidden.

## Question limits

The LLM must keep cognitive load low.

Rules:

- Ask at most one question at a time for beginners.
- Ask at most three questions at a time for experienced users.
- Prefer examples over abstract terms.
- Use simple language unless the user demonstrates technical fluency.
- Do not ask questions whose answers are not needed yet.
- Do not generate code during the interview.
- Do not generate a large architecture before the problem is understood.

## Adaptive interview flow

Interview Mode should usually follow this order:

```txt
Situation
↓
Problem or current project
↓
Current process or current state
↓
Pain and risks
↓
Users and affected people
↓
Desired result
↓
Rules and exceptions
↓
Forbidden outcomes
↓
Inputs and outputs
↓
Validation checks
↓
Constraints
↓
Unknowns
↓
Initial AISDD docs
↓
One safe next task
```

For existing projects, start with current state before future ideas.

For new projects, start with the real-world problem before technology.

## Mapping conversation to AISDD docs

The LLM should map answers into AISDD documents gradually.

| Conversation discovery | AISDD destination |
|---|---|
| Permanent rules, constraints, forbidden changes | `00_PROJECT_RULES.md` |
| Problem, users, goals, rules | `01_PRODUCT_SPEC.md` |
| Existing project state or first project state | `03_CURRENT_STATE.md` |
| First safe implementation step | `04_NEXT_TASK.md` |
| Observable checks | `05_ACCEPTANCE_CHECKS.md` |
| Continuity summary | `07_HANDOFF.md` |
| Known files or expected file areas | `09_FILE_INDEX.md` |
| Missing or uncertain information | `UNKNOWNS` sections inside affected docs |
| Risks | `RISKS` sections inside affected docs |

## Output rule

The first AISDD output should not try to be complete.

It should be:

- honest;
- small;
- usable;
- safe;
- explicit about unknowns;
- ready for the next conversation.

A useful partial structure is better than a fake complete plan.

## When to stop the interview

The LLM should stop interviewing and generate initial docs when it has enough information to define one safe next task.

It does not need enough information to define the whole product.

```txt
The first goal is not to understand everything.
The first goal is to start safely.
```

## Developer mode compatibility

Interview Mode does not replace Developer Mode.

It feeds Developer Mode.

After the first docs exist, developers and agents can continue with the full AISDD workflow:

- full documentation structure;
- task execution;
- acceptance checks;
- handoff updates;
- recovery mode;
- engineering guardrails;
- prompt maturity tracking.

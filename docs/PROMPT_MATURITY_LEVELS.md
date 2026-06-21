# AISDD Prompt Maturity Levels

Prompt Maturity Levels, or PML, measure how much manual context a user must provide for an AI to execute a project task safely.

The goal of AISDD is to reduce manual prompt context over time.

A mature AISDD project should move from long prompts to repository-driven execution.

## Core idea

The less project context the user must repeat manually, the more mature the AISDD adoption is.

```txt
manual prompt context → should trend toward zero
```

## Levels

| Level | Name | User prompt example | What it means |
|---|---|---|---|
| PML-0 | Manual context | Long prompt with files, rules, warnings, constraints, and task details | The project memory still lives mostly in chat |
| PML-1 | Guided task | `Read START_HERE.md. Objective: refactor SettingsScreen.kt. Preserve existing behavior.` | Docs help, but the user still supplies task framing and constraints |
| PML-2 | Objective only | `Read START_HERE.md. Objective: refactor SettingsScreen.kt.` | The repository docs provide most constraints |
| PML-3 | Task ID only | `Read START_HERE.md. Objective: CR13.` | Task IDs and docs are enough for execution |
| PML-4 | Repository-driven | The AI reads `docs/04_NEXT_TASK.md` and executes without extra prompt context | The repository is the operational source of truth |

## Why PML matters

PML makes AISDD measurable.

It answers:

- how much context still needs to be repeated manually;
- whether `START_HERE.md` is useful enough;
- whether `04_NEXT_TASK.md` is precise enough;
- whether handoff is working;
- whether the project can survive switching AI tools;
- whether documentation is actually replacing chat history.

## PML-0: Manual context

Typical prompt:

```txt
Read these files.
Remember this stack.
Do not touch these areas.
Fix this bug.
Also remember this prior decision.
The app currently works like this...
```

Use PML-0 only when:

- AISDD has not been adopted yet;
- the project has no reliable docs;
- Recovery Mode has not been completed;
- the task is too risky without manual explanation.

## PML-1: Guided task

Typical prompt:

```txt
Read docs/START_HERE.md.
Objective: refactor SettingsScreen.kt.
Preserve existing behavior.
Do not change persistence.
Update handoff.
```

This is a good early AISDD stage.

The user still adds constraints, but the docs already carry part of the context.

## PML-2: Objective only

Typical prompt:

```txt
Read docs/START_HERE.md.
Objective: refactor SettingsScreen.kt.
```

At this level, the project docs should already explain:

- stack;
- conventions;
- forbidden changes;
- acceptance checks;
- relevant files;
- handoff expectations.

## PML-3: Task ID only

Typical prompt:

```txt
Read docs/START_HERE.md.
Objective: CR13.
```

At this level, task IDs must be defined in the repository.

The AI should be able to locate or infer the task from:

- `docs/04_NEXT_TASK.md`;
- `docs/07_HANDOFF.md`;
- issue tracker;
- changelog;
- acceptance checks;
- project-specific task records.

If the AI cannot resolve the task ID safely, it should answer `MISSING INFO`.

## PML-4: Repository-driven execution

Typical prompt:

```txt
Read docs/START_HERE.md.
Execute the next task.
```

Or, in an agent workflow, no user prompt is needed beyond giving the repository to the agent.

The AI reads:

```txt
docs/04_NEXT_TASK.md
```

Then executes the task according to AISDD rules.

PML-4 requires strong documentation discipline.

## PML test

To test AISDD maturity, intentionally try the smallest prompt possible.

Recommended test sequence:

1. Try PML-2.
2. If it works, try PML-3.
3. If it works, try PML-4.
4. If it fails, improve repository docs instead of making the prompt longer.

## Failure interpretation

| Failure | Likely cause |
|---|---|
| AI asks for basic project context | `START_HERE.md`, `PROJECT_RULES`, or `HANDOFF` are weak |
| AI cannot identify the task | `04_NEXT_TASK.md` is unclear or task ID is not documented |
| AI changes wrong files | `09_FILE_INDEX.md` is incomplete |
| AI breaks behavior | acceptance checks or known issues are weak |
| AI invents rules | product spec or anti-hallucination guidance is weak |

## Measuring PML

For each task, record:

| Date | Project | Task | Attempted PML | Successful PML | Notes |
|---|---|---|---:|---:|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

Successful PML is the lowest prompt level that allowed the AI to complete the task safely.

## Target by project maturity

| Project state | Target PML |
|---|---:|
| No AISDD docs | PML-0 |
| Recovery just completed | PML-1 |
| Starter adoption | PML-1 or PML-2 |
| Standard adoption | PML-2 or PML-3 |
| Mature adoption | PML-3 or PML-4 |

## Main rule

If the prompt needs to keep growing, the documentation is not carrying enough context.

Improve the repository docs instead of relying on longer chat prompts.
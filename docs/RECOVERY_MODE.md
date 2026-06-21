# AISDD Recovery Mode

Use Recovery Mode when a project already exists, has grown in complexity, and was not started with AISDD.

Recovery Mode is not a rewrite process.

It is a stabilization process.

## Core promise

AISDD should not rewrite the past.

AISDD should control the future.

For existing projects, the first goal is to capture the real current state, identify risks, and define the next safe task.

## When to use

Use Recovery Mode when:

- the project is already in progress;
- the project has little or no documentation;
- several decisions exist only in chat history or memory;
- the codebase is becoming hard to explain to an AI;
- multiple AI sessions have already modified the project;
- bugs and regressions are increasing;
- the user keeps repeating project context manually;
- there is fear that a new AI session will misunderstand the project.

## What Recovery Mode is not

Recovery Mode is not:

- a full refactor;
- a rewrite;
- an architecture redesign;
- a cleanup sprint;
- a promise that the AI will understand the whole project immediately;
- an excuse to document an idealized version of the project.

## Recovery principle

Document what is real before improving what is wrong.

The first Recovery cycle should be read-only unless the user explicitly asks otherwise.

## First Recovery cycle

The first cycle should create a factual snapshot using only the minimum required AISDD docs.

Recommended initial documents:

| Document | Purpose |
|---|---|
| `00_PROJECT_RULES.md` | Current stack, conventions, forbidden changes, non-negotiables |
| `03_CURRENT_STATE.md` | What exists, what works, what is partial, what is broken |
| `04_NEXT_TASK.md` | One safe next task only |
| `07_HANDOFF.md` | Short continuity summary for the next session or AI |
| `08_KNOWN_ISSUES.md` | Known bugs, limitations, technical debt, risks |
| `09_FILE_INDEX.md` | Main files and responsibilities |

Leave the other AISDD docs as TODO until they become useful.

## Recovery prompt rule

The AI must not modify code during the first Recovery pass unless explicitly instructed.

The first pass should focus on:

- reading the current project;
- mapping files;
- identifying known behavior;
- recording unknowns;
- finding risks;
- defining the next safe task.

## Good Recovery request

```txt
This project already exists and is adopting AISDD in Recovery Mode.
Do not refactor.
Do not modify code.
Do not invent architecture, business rules, files, schemas, endpoints, or decisions.
Analyze the current project and generate a factual first version of:

- docs/00_PROJECT_RULES.md
- docs/03_CURRENT_STATE.md
- docs/04_NEXT_TASK.md
- docs/07_HANDOFF.md
- docs/08_KNOWN_ISSUES.md
- docs/09_FILE_INDEX.md

Mark missing information as UNKNOWNS.
```

## Bad Recovery request

```txt
Read the whole project, organize everything, refactor what is wrong, and make it follow AISDD.
```

That request is too broad and likely to cause hallucinations, regressions, or idealized documentation.

## Recovery stages

| Stage | Goal | Code changes? |
|---|---|---|
| Snapshot | Capture real current state | No |
| Stabilize | Define safe next task and known risks | Usually no |
| First controlled task | Execute one small task under AISDD | Yes |
| Maintenance | Update docs and handoff | Maybe |
| Standard adoption | Gradually fill remaining docs | Maybe |

## Adoption path for existing complex projects

Recommended path:

```txt
Recovery → Starter → Standard → Mature
```

Do not jump directly to Mature.

## What to avoid

Avoid:

- filling all 12 docs with guesses;
- asking the AI to infer business rules from code alone;
- treating old decisions as confirmed facts;
- refactoring during the snapshot;
- mixing documentation recovery with feature work;
- using conversation memory as the only source of truth.

## How to handle old decisions

Old decisions can be recorded as reconstructed decisions, but they must be marked clearly.

Example:

```txt
ADR-003 — Reconstructed decision
Status: Inferred
Evidence: Existing code structure and user confirmation pending
Decision: The project currently stores reminders locally.
UNKNOWNS: Original reason for this decision is not documented.
```

## Exit criteria

Recovery Mode can end when:

- the main files are mapped;
- current state is documented;
- known issues are listed;
- the next task is clear and small;
- handoff is useful for a new session;
- the AI can continue without a long manual recap.

## Main rule

Recovery Mode should reduce chaos before adding speed.
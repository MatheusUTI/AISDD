# AISDD Adoption Packages

AISDD has many files because this repository contains the full framework.

A project adopting AISDD should not copy or use everything at once.

Use only the adoption package that matches the current project state.

## Main rule

```txt
Do not copy the whole AISDD repository into your project.
Copy only the package you need right now.
```

AISDD should feel useful before it feels complete.

## Which package should I use?

| Your situation | Use this package | Goal |
|---|---|---|
| I want to start today with minimum friction | Core Kit | Control the next AI task |
| I have an existing simple project | Starter Kit | Add AISDD without stopping development |
| I have an existing complex or messy project | Recovery Kit | Map the real current state before coding |
| I have a long-running project with real rules | Standard Kit | Keep product, architecture, state, and tasks aligned |
| I have multiple AIs, releases, or contributors | Mature Kit | Add validation, maintenance, metrics, and governance |
| I am maintaining AISDD itself | Framework Maintainer Layer | Evolve the framework without breaking users |

## Core Kit

Use this when you want to start today.

Copy or create only:

```txt
docs/
├─ START_HERE.md
├─ 00_PROJECT_RULES.md
├─ 04_NEXT_TASK.md
├─ 07_HANDOFF.md
└─ 09_FILE_INDEX.md
```

Fill only:

| File | What to write |
|---|---|
| `00_PROJECT_RULES.md` | Stack, permanent rules, forbidden changes |
| `04_NEXT_TASK.md` | One task only |
| `07_HANDOFF.md` | Short state summary for the next session |
| `09_FILE_INDEX.md` | Main files and responsibilities |

Use when:

- the project is small;
- you want immediate control;
- you do not want a documentation phase;
- you are testing AISDD for the first time.

Stop here if this is enough.

## Starter Kit

Use this for an existing simple project.

Copy:

```txt
templates/docs/ → your-project/docs/
```

Then fill only the Core files first.

Leave the rest as TODO until needed.

Use prompt:

```txt
templates/prompts/STARTER_ADOPTION_PROMPT.md
```

Use when:

- the project already exists;
- it is not too messy;
- you want continuity between AI sessions;
- you want to stop repeating the same context.

## Recovery Kit

Use this when the project already exists and is complex, undocumented, or partially confused.

Start with a read-only snapshot.

Initial docs:

```txt
docs/
├─ 00_PROJECT_RULES.md
├─ 03_CURRENT_STATE.md
├─ 04_NEXT_TASK.md
├─ 07_HANDOFF.md
├─ 08_KNOWN_ISSUES.md
└─ 09_FILE_INDEX.md
```

Use prompt:

```txt
templates/prompts/RECOVERY_MODE_PROMPT.md
```

Do not refactor during the first snapshot.

Use when:

- the project is already in progress;
- the AI keeps misunderstanding the project;
- bugs and regressions are increasing;
- context is repeated manually every session;
- the current state is not clearly documented.

Measure:

```txt
Recovery snapshot accuracy
```

## Standard Kit

Use this when the project will continue for weeks or months.

Complete the full project documentation gradually:

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

Use when:

- product rules matter;
- architecture matters;
- acceptance checks matter;
- regressions are becoming costly;
- multiple sessions or tools are touching the project.

Do not fill everything with guesses.

Unknowns are allowed.

## Mature Kit

Use this when AISDD is part of a serious long-running workflow.

Add:

| Area | Files or tools |
|---|---|
| Maintenance | `docs/DOCUMENTATION_MAINTENANCE.md` |
| Metrics | `docs/DOGFOODING_METRICS.md` |
| Prompt maturity | `docs/PROMPT_MATURITY_LEVELS.md` |
| Staleness checks | `scripts/check-aisdd-staleness.py` |
| Structure checks | `scripts/check-aisdd-docs.py` |
| Governance | `CONTRIBUTING.md`, `docs/ROADMAP.md` |

Use when:

- more than one AI works on the project;
- handoff quality matters;
- releases exist;
- contributors exist;
- you want evidence that AISDD is working.

## Framework Maintainer Layer

This is for the AISDD repository itself.

It includes:

```txt
framework/
templates/
docs/
tutorials/
examples/
scripts/
.github/
```

Most adopting projects do not need this layer.

Use this layer only when improving AISDD itself.

## Adoption path examples

### New small project

```txt
Core Kit → Starter Kit → Standard Kit if needed
```

### Existing simple project

```txt
Starter Kit → Standard Kit if needed
```

### Existing messy project

```txt
Recovery Kit → Starter Kit → Standard Kit
```

### Business-rule-heavy project

```txt
Recovery Kit → Standard Kit → Mature Kit
```

### Multi-AI or team project

```txt
Standard Kit → Mature Kit
```

## What not to do

Do not:

- copy the whole AISDD repository into an adopting project;
- fill all documents with guesses;
- use Mature Kit before Core Kit works;
- run Recovery and refactor in the same first task;
- treat examples, tutorials, and framework docs as required project files.

## Simple decision tree

```txt
Do you only have an idea?
→ Use Project Definition Wizard.

Does the project already exist and feel messy?
→ Use Recovery Kit.

Does the project already exist but is manageable?
→ Use Starter Kit.

Do rules, architecture, and tests matter now?
→ Move to Standard Kit.

Do you need metrics, governance, or multi-AI validation?
→ Move to Mature Kit.
```

## Main rule

AISDD adoption should be progressive.

Start with the smallest package that reduces the next real pain.
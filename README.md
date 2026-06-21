# AISDD — AI Spec-Driven Development Framework

**AISDD** is a universal framework for building long-term software projects with AI assistance.

It helps developers use AI tools without losing project continuity, traceability, architectural control, or context efficiency.

> The AI conversation is temporary.  
> The repository is the source of truth.

## Why AISDD exists

AI can accelerate software development, but unmanaged AI-assisted work often creates new problems:

- excessive chat context;
- high token usage;
- lost continuity between sessions;
- hallucinated files, APIs, tables, or business rules;
- unnecessary rewrites;
- regression bugs;
- undocumented decisions;
- difficulty switching between AI tools;
- fragile long-term maintenance.

AISDD turns AI-assisted development into a controlled, documentation-driven workflow.

## What AISDD is

AISDD is:

- language-independent;
- stack-independent;
- vendor-independent;
- reusable across projects;
- resistant to hallucinations;
- optimized for low context and token usage;
- suitable for long-running projects;
- compatible with multiple AIs working on the same repository.

Compatible tools include ChatGPT, Gemini, Claude, Cursor, Windsurf, Copilot, local agents, and future AI systems.

## Start here

Choose the path that matches your situation:

| Situation | Start with |
|---|---|
| You only have a rough project idea | [`docs/PROJECT_DEFINITION.md`](docs/PROJECT_DEFINITION.md) |
| You already have a project | [`docs/QUICK_START.md`](docs/QUICK_START.md) |
| You want the complete onboarding guide | [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) |
| You want to validate AISDD in real usage | [`docs/DOGFOODING_METRICS.md`](docs/DOGFOODING_METRICS.md) |
| You want to understand the core method | [`framework/AISDD_MANIFESTO.md`](framework/AISDD_MANIFESTO.md) |

## The shortest adoption path

For an existing project, copy the documentation template into your repository:

```bash
mkdir -p docs
cp -R templates/docs/* your-project/docs/
```

Then fill only these starter files first:

| File | Purpose |
|---|---|
| `docs/00_PROJECT_RULES.md` | Permanent rules, stack, conventions, forbidden changes |
| `docs/04_NEXT_TASK.md` | One executable task only |
| `docs/07_HANDOFF.md` | Short continuity summary |
| `docs/09_FILE_INDEX.md` | Map of important files and responsibilities |

Start the AI with:

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

The full starter prompt is available at:

```txt
templates/prompts/STARTER_ADOPTION_PROMPT.md
```

## Starting from only an idea

If the project does not exist yet, use the Project Definition Wizard:

```txt
templates/prompts/PROJECT_DEFINITION_WIZARD_PROMPT.md
```

The AI should ask practical questions, identify unknowns, and generate the first AISDD documentation set before development starts.

This path is documented in:

```txt
docs/PROJECT_DEFINITION.md
```

## Adoption levels

AISDD does not require perfect documentation before the first task.

| Level | Use when | Required effort |
|---|---|---|
| Definition | You only have an idea | Answer guided questions |
| Starter | You want control now | Fill 4 files |
| Standard | The project will continue for weeks or months | Fill all core docs gradually |
| Mature | Multiple AIs or contributors work on the project | Add ADRs, tests, compliance checks, examples, and validation metrics |

## Core philosophy

AISDD is based on a few simple ideas:

1. **The repository is the source of truth.**  
   The chat is temporary. Important project knowledge must live in versioned files.

2. **One task per cycle.**  
   Each AI interaction should solve one clearly defined task.

3. **Minimum necessary context.**  
   The AI should load only the documentation and files needed for the current task.

4. **Incremental evolution.**  
   Avoid large rewrites. Prefer small, safe, traceable changes.

5. **Explicit uncertainty.**  
   The AI must separate facts, assumptions, unknowns, and risks.

6. **Continuity between AIs.**  
   Any compatible AI should be able to continue the project from the repository docs.

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

## What each document does

| File | Responsibility |
|---|---|
| `START_HERE.md` | Entry point for every AI, developer, or agent |
| `00_PROJECT_RULES.md` | Permanent rules, invariants, conventions, forbidden changes |
| `01_PRODUCT_SPEC.md` | Product problem, users, features, business rules, scope |
| `02_ARCHITECTURE.md` | Architecture, modules, contracts, flows, boundaries |
| `03_CURRENT_STATE.md` | Real current state of the project |
| `04_NEXT_TASK.md` | The only executable task for the current cycle |
| `05_ACCEPTANCE_CHECKS.md` | Checklist before accepting changes |
| `06_DECISIONS_LOG.md` | Chronological ADR-style decision log |
| `07_HANDOFF.md` | Very short continuity summary between sessions and AIs |
| `08_KNOWN_ISSUES.md` | Known problems, limitations, mitigations |
| `09_FILE_INDEX.md` | Operational map of files and responsibilities |
| `10_TEST_CHECKLIST.md` | Quick regression checklist |
| `11_TEST_STRATEGY.md` | Official testing strategy |

## AISDD execution cycle

Every AI-assisted task should follow this cycle:

1. Read `docs/START_HERE.md`.
2. Load only the documents required for the current task.
3. Execute only one task.
4. Validate acceptance checks.
5. Update affected documentation.
6. Update `docs/07_HANDOFF.md`.
7. End the cycle.

## Recommended reading by task type

| Task type | Recommended context |
|---|---|
| Simple fix | `00_PROJECT_RULES.md`, `07_HANDOFF.md`, `09_FILE_INDEX.md`, `04_NEXT_TASK.md` |
| New feature | `01_PRODUCT_SPEC.md`, `02_ARCHITECTURE.md`, `04_NEXT_TASK.md`, `05_ACCEPTANCE_CHECKS.md` |
| Critical change | `00_PROJECT_RULES.md`, `02_ARCHITECTURE.md`, `03_CURRENT_STATE.md`, `06_DECISIONS_LOG.md` |
| Testing task | `10_TEST_CHECKLIST.md`, `11_TEST_STRATEGY.md` |
| Handoff | `07_HANDOFF.md`, `03_CURRENT_STATE.md`, `04_NEXT_TASK.md` |
| Audit | `05_ACCEPTANCE_CHECKS.md`, `08_KNOWN_ISSUES.md`, `09_FILE_INDEX.md`, `docs/DOGFOODING_METRICS.md` |

## Universal AI response format

Every implementation response should contain:

```md
## Objective

## Files changed

## Contract impact

## FACTS

## ASSUMPTIONS

## UNKNOWNS

## RISKS

## Acceptance status

## Updated handoff
```

This keeps AI output reviewable, traceable, and safe to hand off to another tool.

## Anti-hallucination strategy

AISDD requires the AI to distinguish:

- **FACTS** — directly observed information;
- **ASSUMPTIONS** — explicit assumptions adopted for the task;
- **UNKNOWNS** — missing information;
- **RISKS** — possible regressions or impacts.

The AI must not silently invent:

- files;
- modules;
- database tables;
- endpoints;
- schemas;
- business rules;
- external contracts;
- architecture decisions;
- test results.

## MISSING INFO calibration

If critical information is missing, the AI must answer:

```txt
MISSING INFO
```

However, not every unknown should block the task.

| Type | Meaning | AI behavior |
|---|---|---|
| Critical | Could cause wrong behavior, broken contracts, data loss, security risk, or major rework | Stop with `MISSING INFO` |
| Assumable | A reasonable default can be chosen and changed later with low risk | Proceed and document the assumption |
| Cosmetic | Preference-level detail with little functional impact | Choose a simple default and document only if relevant |

See the full policy in:

```txt
framework/AISDD_ANTI_HALLUCINATION.md
```

## File growth control

AISDD discourages files that grow indefinitely.

Suggested limits:

| File type | Suggested limit |
|---|---:|
| Screens | 300 lines |
| Components | 150 lines |
| Dialogs | 100 lines |
| Controllers / ViewModels | 400 lines |
| Helpers | 200 lines |

When a file approaches or exceeds the limit, the AI should report:

```txt
FILE GROWTH RISK
```

## Repository structure

```txt
framework/    Core AISDD method and rules
templates/    Reusable documentation and prompt templates
examples/     Example AISDD project structures
docs/         Public adoption and validation documentation
tutorials/    Step-by-step guides
scripts/      Utility scripts for AISDD projects
```

## Prompt templates

AISDD includes reusable prompts:

| Prompt | Use when |
|---|---|
| `PROJECT_DEFINITION_WIZARD_PROMPT.md` | Starting from a rough idea |
| `STARTER_ADOPTION_PROMPT.md` | Introducing AISDD into a new or existing repository |
| `UNIVERSAL_AI_START_PROMPT.md` | Starting a general AISDD session |
| `TASK_EXECUTION_PROMPT.md` | Running one AISDD task |
| `HANDOFF_PROMPT.md` | Updating continuity between sessions |
| `AUDIT_PROMPT.md` | Checking AISDD compliance |
| `REFACTOR_PROMPT.md` | Performing safe refactors |

## Scripts

AISDD currently includes lightweight utility scripts:

| Script | Purpose |
|---|---|
| `scripts/init-aisdd-project.py` | Copy AISDD docs into a project |
| `scripts/check-aisdd-docs.py` | Check whether required AISDD docs exist |

## Validation and dogfooding

AISDD should be judged by real continuity, not by how good the documentation looks.

The dogfooding guide tracks:

- handoff update rate;
- decision log update rate;
- context size estimate;
- missing info friction;
- cross-AI continuation.

Before recalibrating core rules, AISDD recommends collecting at least:

| Requirement | Minimum |
|---|---:|
| Real tasks completed | 10 |
| Different task types | 3 |
| Session handoffs | 3 |
| Structural decisions | 2 |
| Cross-AI continuation tests | 1 |

Context usage can be estimated with:

```txt
estimated_tokens = total_characters / 4
```

See:

```txt
docs/DOGFOODING_METRICS.md
```

## Example first AI request

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Then read only the minimum required context for docs/04_NEXT_TASK.md.
Execute one task only.
Do not invent missing contracts, files, schemas, endpoints, or business rules.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

## When AISDD is useful

AISDD is especially useful when:

- the project will last more than a few sessions;
- multiple AIs may work on the same project;
- you need predictable handoff between sessions;
- the project has business rules or architecture decisions;
- you want to reduce repeated prompting;
- regressions are costly;
- you want traceable AI-assisted development.

## When AISDD may be overkill

AISDD may be unnecessary for:

- tiny one-off scripts;
- throwaway prototypes;
- experiments with no maintenance plan;
- tasks where no continuity is needed.

Even then, the Starter flow can still help keep AI work controlled.

## Current status

AISDD is in early development.

The current focus is:

- making adoption extremely simple;
- testing the framework through real projects;
- improving examples;
- validating cross-AI continuity;
- collecting dogfooding metrics.

## Roadmap

Planned improvements:

- complete practical example project;
- Portuguese documentation entrypoint;
- compliance checklist;
- release and versioning policy;
- stronger automation around documentation checks;
- more real-world dogfooding reports.

## Contributing

Contributions are welcome if they improve:

- clarity;
- safety;
- adoption;
- traceability;
- AI portability;
- validation;
- long-term maintainability.

Before proposing changes, preserve these constraints:

- no AI vendor lock-in;
- no stack lock-in;
- no unnecessary complexity;
- no silent weakening of anti-hallucination rules;
- no changes to core rules without clear reason or validation.

See:

```txt
CONTRIBUTING.md
```

## License

MIT License.

See [`LICENSE`](LICENSE).
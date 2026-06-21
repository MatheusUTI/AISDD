# AISDD — AI Spec-Driven Development Framework

**AISDD** is a universal framework for building long-term software projects with AI assistance.

It helps developers use AI tools without losing project continuity, traceability, architectural control, or context efficiency.

> The AI conversation is temporary.  
> The repository is the source of truth.

## AISDD in 60 seconds

AISDD keeps AI-assisted development grounded by moving project memory out of chat and into versioned repository files.

1. Write the project rules in the repo.
2. Give the AI one task at a time.
3. Force the AI to separate facts, assumptions, unknowns, and risks.
4. Update the handoff before ending the session.
5. Continue with any compatible AI using the same repository context.

## Start today: ignore 80% of the framework

To start using AISDD today, copy the docs template and fill only four files:

```bash
mkdir -p docs
cp -R templates/docs/* your-project/docs/
```

| Core file | Purpose |
|---|---|
| `docs/00_PROJECT_RULES.md` | Stack, permanent rules, conventions, forbidden changes |
| `docs/04_NEXT_TASK.md` | One executable task only |
| `docs/07_HANDOFF.md` | Short continuity summary for the next session or AI |
| `docs/09_FILE_INDEX.md` | Important files and responsibilities |

Then start the AI with:

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

The rest of AISDD is added only when the project needs it.

See: [`docs/CORE_VS_ADVANCED.md`](docs/CORE_VS_ADVANCED.md)

## Choose your path

| Situation | Start with |
|---|---|
| You only have a rough project idea | [`docs/PROJECT_DEFINITION.md`](docs/PROJECT_DEFINITION.md) |
| You already have a simple project | [`docs/QUICK_START.md`](docs/QUICK_START.md) |
| You already have a complex or messy project | [`docs/RECOVERY_MODE.md`](docs/RECOVERY_MODE.md) |
| You want real-project usage guidance | [`docs/REAL_PROJECT_PLAYBOOKS.md`](docs/REAL_PROJECT_PLAYBOOKS.md) |
| You want the full onboarding guide | [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) |
| You want to validate AISDD in practice | [`docs/DOGFOODING_METRICS.md`](docs/DOGFOODING_METRICS.md) |
| You want to prevent stale documentation | [`docs/DOCUMENTATION_MAINTENANCE.md`](docs/DOCUMENTATION_MAINTENANCE.md) |
| You want to see priorities | [`docs/ROADMAP.md`](docs/ROADMAP.md) |

## How AISDD is different

| AISDD is not just... | Because AISDD... |
|---|---|
| A prompt kit | Stores project memory in repository docs, not chat history |
| A documentation template | Defines AI execution cycles, handoff, acceptance, and maintenance |
| A spec document | Separates facts, assumptions, unknowns, and risks every cycle |
| An agent framework | Works with ChatGPT, Claude, Gemini, Cursor, Windsurf, Copilot, local agents, and future tools |
| A greenfield-only method | Includes Recovery Mode for projects already in progress |

## Core vs Advanced

AISDD is layered.

| Layer | Use when | Main docs |
|---|---|---|
| Core | You want control today | `00_PROJECT_RULES`, `04_NEXT_TASK`, `07_HANDOFF`, `09_FILE_INDEX` |
| Safety | Regressions or hallucinations are risky | `ACCEPTANCE_CHECKS`, `KNOWN_ISSUES`, anti-hallucination policy |
| Product/Architecture | Business rules and structure matter | `PRODUCT_SPEC`, `ARCHITECTURE`, `CURRENT_STATE`, `DECISIONS_LOG` |
| Recovery | The project already exists and is messy | `RECOVERY_MODE`, Recovery prompt, snapshot accuracy |
| Mature | The project is long-running or multi-AI | dogfooding metrics, maintenance, staleness checks |

Start with Core. Add layers only when the project pain requires them.

## Recovery Mode

Use Recovery Mode when a project already exists, has grown complex, and was not started with AISDD.

Recovery Mode is not a rewrite, refactor, redesign, or cleanup sprint.

It is a stabilization process.

The first Recovery pass should be read-only unless explicitly instructed otherwise. Its goal is to map the real current state, identify risks, and create a safe AISDD starting point.

Recommended path:

```txt
Recovery → Starter → Standard → Mature
```

See:

- [`docs/RECOVERY_MODE.md`](docs/RECOVERY_MODE.md)
- [`templates/prompts/RECOVERY_MODE_PROMPT.md`](templates/prompts/RECOVERY_MODE_PROMPT.md)
- [`examples/casa-em-dia-recovery-dogfooding/README.md`](examples/casa-em-dia-recovery-dogfooding/README.md)

## Real project dogfooding

AISDD is being validated against real project types, not only theoretical examples.

Current real-project playbooks:

| Project | What it validates |
|---|---|
| Casa em Dia | Android app development, manual testing, feature fixes, AI handoff |
| Roteirizador | Existing complex internal tool, business rules, import/export workflows, regression control |

See: [`docs/REAL_PROJECT_PLAYBOOKS.md`](docs/REAL_PROJECT_PLAYBOOKS.md)

## Universal AI response format

Every implementation response should include:

| Section | Purpose |
|---|---|
| Objective | What the task tried to do |
| Files changed | What changed |
| Contract impact | Whether APIs, schemas, data, behavior, or contracts changed |
| FACTS | What was observed directly |
| ASSUMPTIONS | What was assumed explicitly |
| UNKNOWNS | What is still missing |
| RISKS | What may break or need review |
| Acceptance status | What passed, failed, or was not tested |
| Updated handoff | What the next session should know |

Full format: [`framework/AISDD_AI_RESPONSE_FORMAT.md`](framework/AISDD_AI_RESPONSE_FORMAT.md)

## Anti-hallucination policy

AISDD requires the AI to distinguish:

- **FACTS** — directly observed information;
- **ASSUMPTIONS** — explicit assumptions adopted for the task;
- **UNKNOWNS** — missing information;
- **RISKS** — possible regressions or impacts.

If critical information is missing, the AI must answer:

```txt
MISSING INFO
```

But not every unknown should block the work.

| Type | AI behavior |
|---|---|
| Critical | Stop with `MISSING INFO` |
| Assumable | Proceed and document the assumption |
| Cosmetic | Choose a simple default and document only if relevant |

Full policy: [`framework/AISDD_ANTI_HALLUCINATION.md`](framework/AISDD_ANTI_HALLUCINATION.md)

## Documentation structure

AISDD projects use this structure:

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

You do not need to fill all of them before starting.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/init-aisdd-project.py` | Copy AISDD docs into a project |
| `scripts/check-aisdd-docs.py` | Check whether required AISDD docs exist |
| `scripts/check-aisdd-staleness.py` | Detect simple stale-documentation signals from Git history |

## Languages

- [Português brasileiro](docs/pt-BR/README.md)
- [Português brasileiro — Quick Start](docs/pt-BR/QUICK_START.md)

The English documentation is currently the canonical source. Portuguese docs are summary entrypoints unless explicitly marked as full translations.

## Repository map

```txt
framework/    Core AISDD method and rules
templates/    Reusable docs and prompt templates
examples/     Example structures and dogfooding cases
docs/         Adoption, maintenance, validation, and roadmap docs
tutorials/    Step-by-step guides
scripts/      Utility scripts for AISDD projects
```

## Status

AISDD is in early development.

Current focus:

- make adoption extremely simple;
- support new and already-started projects;
- validate AISDD through Casa em Dia and Roteirizador;
- improve examples;
- reduce documentation maintenance friction;
- keep the framework vendor-independent and stack-independent.

Roadmap: [`docs/ROADMAP.md`](docs/ROADMAP.md)

## Contributing

Contributions are welcome if they improve clarity, safety, adoption, traceability, AI portability, validation, or long-term maintainability.

Before proposing changes, preserve:

- no AI vendor lock-in;
- no stack lock-in;
- no unnecessary complexity;
- no silent weakening of anti-hallucination rules;
- no changes to core rules without clear reason or validation.

See: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## License

MIT License.

See [`LICENSE`](LICENSE).
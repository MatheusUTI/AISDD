# AISDD Real Project Playbooks

This document shows how AISDD can be applied to real projects without adopting every layer at once.

The active target projects are:

- FreteOps;
- Casa em Dia;
- Roteirizador.

They represent different real AISDD dogfooding paths.

## Principle

Use the smallest AISDD mode that makes the next task safer.

Do not adopt all layers at once.

Also track Prompt Maturity Level, or PML, to see whether repeated manual context is decreasing.

## FreteOps

FreteOps is a real Android logistics-operations application being tracked from its first development day through release-oriented development.

AISDD was adopted immediately after the first AI-generated scaffold, making this a near-greenfield case rather than a Recovery case.

It is useful for validating AISDD in:

- new-product development;
- Android development with Kotlin and Jetpack Compose;
- AI-generated implementation;
- cross-AI collaboration;
- repository-driven task execution;
- prompt shrinkage over time;
- product/architecture continuity from prototype to real integrations;
- release-lifecycle continuity.

### Collaboration model

```txt
Human product owner
↓
Repository specifications and decisions
↓
Gemini / AI Studio implementation
↓
GitHub project state
↓
ChatGPT architecture / AISDD review
↓
Human validation
↓
Next repository-defined task
```

The project intentionally uses different AI systems for implementation and review so cross-AI portability can be measured continuously.

### Recommended path

```txt
Starter/Core baseline → Product/Architecture → Standard → Mature if justified
```

Do not run Recovery Mode because the project was captured before significant project-memory loss occurred.

### Initial project memory

Maintain:

- `docs/START_HERE.md`
- `docs/00_PROJECT_RULES.md`
- `docs/01_PRODUCT_SPEC.md`
- `docs/02_ARCHITECTURE.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/05_ACCEPTANCE_CHECKS.md`
- `docs/06_DECISIONS_LOG.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`

The wider set is justified early because the project already has two AI systems, product boundaries, architecture decisions, and an external-integration roadmap.

Do not add extra process documents automatically.

### Prompt maturity target

Baseline:

```txt
PML-0
```

First repository-driven experiment:

```txt
PML-4 attempt
```

Target startup prompt:

```txt
Read docs/START_HERE.md.
Execute docs/04_NEXT_TASK.md.
```

If the attempt fails, record the actual successful PML rather than pretending the shorter prompt worked.

Improve repository memory before expanding recurring manual prompt context.

### Safe first tasks

Good first tasks:

- correct one visual-system problem without changing behavior;
- document one stable architecture boundary;
- replace one mock boundary with a verified contract;
- add one acceptance check for an implemented flow;
- validate one cross-AI handoff.

Avoid:

- adding multiple integrations in one cycle;
- adopting Firebase or another service without a concrete need;
- rewriting generated architecture only because it was generated;
- placing external-system credentials or fragile integration logic in the mobile client;
- turning mock behavior into an implied production contract;
- broad refactors before the first repository-driven cycles are validated.

### Validation questions

```txt
Can Gemini execute the next task from repository memory without a long recap?
```

```txt
Can ChatGPT review the completed cycle from repository state without reading the Gemini conversation?
```

```txt
Does the product remain understandable after several incremental AI-generated changes?
```

```txt
Does prompt size continue to fall when real integrations increase complexity?
```

Track the public case at:

```txt
examples/freteops-end-to-end-dogfooding/
```

## Casa em Dia

Casa em Dia is a real Android app project developed with AI assistance.

It is useful for validating AISDD in:

- mobile app development;
- solo development;
- manual testing cycles;
- recurring feature fixes;
- handoff between AI sessions.

### Recommended path

```txt
Recovery → Starter → Standard
```

Start with Recovery if the project already has working or partially working features.

### First snapshot

Create or update only:

- `docs/00_PROJECT_RULES.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`

Do not refactor during the first snapshot.

### Prompt maturity target

Initial target:

```txt
PML-1 → PML-2
```

Near-term target:

```txt
PML-3 for CR-style tasks
```

Example prompts to test:

```txt
Read docs/START_HERE.md.
Objective: CR13.
```

```txt
Read docs/START_HERE.md.
Next task.
```

If the AI fails, improve the repository docs instead of making the prompt longer.

### Safe first tasks

Good first tasks:

- map one existing feature flow;
- document what works and what is broken;
- fix one isolated bug;
- validate one behavior manually;
- update handoff after testing.

Avoid:

- redesigning the whole app;
- rewriting the main architecture;
- implementing several features at once;
- generating complete docs from guesses.

### Validation questions

```txt
Did the AI describe the real app state correctly?
```

```txt
What was the lowest prompt maturity level that worked safely?
```

Use:

- Recovery snapshot accuracy from `docs/DOGFOODING_METRICS.md`;
- Prompt Maturity Levels from `docs/PROMPT_MATURITY_LEVELS.md`.

## Roteirizador

Roteirizador is a real business-rule-heavy project category where the earliest AISDD ideas emerged.

It is useful for validating AISDD in:

- existing complex projects;
- internal tools;
- data import and export workflows;
- business rules that cannot be invented;
- high regression risk when context is lost.

### Recommended path

```txt
Recovery → Product/Architecture → Standard → Mature
```

Start with Recovery because the project already exists.

Move to Product and Architecture documentation when the real rules and flows are confirmed.

### First snapshot

Create or update only:

- `docs/00_PROJECT_RULES.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`

Add `docs/01_PRODUCT_SPEC.md` only for confirmed product rules.

Keep uncertain rules in `UNKNOWNS`.

### Prompt maturity target

Initial target:

```txt
PML-1
```

Near-term target:

```txt
PML-2 for isolated tasks
```

Mature target:

```txt
PML-3 only after product rules and workflows are documented
```

Roteirizador should move more slowly than Casa em Dia because business rules are more dangerous to infer.

### Safe first tasks

Good first tasks:

- map one current workflow;
- document known input and output files;
- identify one known limitation;
- create acceptance checks for one flow;
- update handoff after testing.

Avoid:

- rebuilding the whole system;
- changing rules without confirmation;
- inferring rules silently;
- rewriting import or export behavior without checks;
- optimizing before documenting current behavior.

### Validation questions

```txt
Did the AI preserve the real rules and constraints?
```

```txt
Did a shorter prompt cause the AI to infer business rules incorrectly?
```

Track:

- invented rules;
- misunderstood files or fields;
- missing acceptance checks;
- repeated context that still had to be explained manually;
- successful prompt maturity level per task.

## Shared rules

For all projects:

- use the adoption path that matches the real project state;
- do not refactor during a Recovery snapshot;
- do not fill all docs with guesses;
- keep `04_NEXT_TASK.md` small;
- update `07_HANDOFF.md` every meaningful cycle;
- record unknowns instead of inventing them;
- measure whether AISDD reduced repeated explanation;
- test shorter prompts intentionally;
- improve docs when shorter prompts fail;
- preserve evidence of failed experiments instead of rewriting history.

## Main rule

AISDD should become useful before it becomes complete.

Prompt size should decrease as repository documentation becomes trustworthy.

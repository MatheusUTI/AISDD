# AISDD Real Project Playbooks

This document shows how AISDD can be applied to real projects without adopting every layer at once.

The first target projects are:

- Casa em Dia;
- Roteirizador.

They represent real AISDD dogfooding paths.

## Principle

Use the smallest AISDD mode that makes the next task safer.

Do not adopt all layers at once.

Also track Prompt Maturity Level, or PML, to see whether repeated manual context is decreasing.

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

For both projects:

- start with Recovery if the project is already in progress;
- do not refactor during the first snapshot;
- do not fill all docs with guesses;
- keep `04_NEXT_TASK.md` small;
- update `07_HANDOFF.md` every cycle;
- record unknowns instead of inventing them;
- measure whether AISDD reduced repeated explanation;
- test shorter prompts intentionally;
- improve docs when shorter prompts fail.

## Main rule

AISDD should become useful before it becomes complete.

Prompt size should decrease as repository documentation becomes trustworthy.
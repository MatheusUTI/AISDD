# Casa em Dia Recovery Dogfooding Report

## Status

Baseline report started.

This report records the first public AISDD dogfooding baseline for Casa em Dia.

It is intentionally limited to process validation. No proprietary source code is included.

## Date

2026-06-21

## Project

Casa em Dia

## Project type

Android app developed with AI assistance.

## Report type

Conversation-informed Recovery baseline.

This is not yet a source-code-audited Recovery snapshot.

## Evidence sources

This baseline uses:

- user-reported manual testing notes;
- prior AI-assisted development cycles;
- observed recurring need for handoff and context continuity;
- known AISDD goals and documentation structure.

This baseline does not yet use:

- direct source-code inspection;
- automated tests;
- build logs;
- generated Recovery docs from the real Casa em Dia repository.

## Validation goal

Test whether AISDD Recovery Mode can create and maintain a useful factual snapshot for an Android app already in progress.

Primary question:

```txt
Can the next AI session continue Casa em Dia with less manual recap and fewer invented assumptions?
```

## Project state before Recovery

### FACTS reported by the user

- Casa em Dia is an Android app.
- The project is being developed with AI assistance.
- The app already has implemented features and manual testing cycles.
- Reminder-related flows have been actively developed and tested.
- Manual testing exposed issues around viewing, editing, deleting, restoring, completion/history, recurrence, and notifications.
- At least one later cycle was reported as functional after fixes.
- The user wants development to continue with maximum daily functional progress.

### ASSUMPTIONS

- The project was not originally started with full AISDD documentation.
- Recovery Mode is appropriate because the project already has existing behavior and evolving requirements.
- Current project truth may be split between code, manual tests, and prior AI conversations.

### UNKNOWNS

- Current source tree.
- Current Android stack details.
- Current persistence implementation.
- Current notification implementation.
- Exact reminder data model.
- Current test coverage.
- Current state of recurrence behavior in code.
- Current state of restore/history behavior in code.

### RISKS

- AI may overstate feature completeness based only on user-reported outcomes.
- AI may infer architecture that is not present in the code.
- AI may treat prior bug reports as still current after later fixes.
- AI may miss regressions if only latest user testing is considered.

## Recovery snapshot plan

The first real Recovery run should create or update only:

- `docs/00_PROJECT_RULES.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`

The first Recovery run should not:

- refactor code;
- redesign architecture;
- implement new features;
- rewrite working flows;
- infer missing product rules silently.

## Initial Recovery hypotheses to verify

These are not final facts until checked against the real repository.

| Item | Hypothesis | Status |
|---|---|---|
| Project platform | Android app | User-reported |
| Development style | AI-assisted solo development | User-reported |
| Main active domain | reminders and household/task flows | User-reported |
| Risk area | reminder lifecycle and state transitions | User-reported |
| Needs AISDD | continuity across AI sessions | User-reported |
| Testing style | manual user testing first | User-reported |
| Recovery mode fit | appropriate | Assumption |

## Snapshot review

Not yet measured.

| Document | Correct | Partially correct | Incorrect | Unknown | Notes |
|---|---:|---:|---:|---:|---|
| 00_PROJECT_RULES.md | 0 | 0 | 0 | 0 | Pending real Recovery run |
| 03_CURRENT_STATE.md | 0 | 0 | 0 | 0 | Pending real Recovery run |
| 04_NEXT_TASK.md | 0 | 0 | 0 | 0 | Pending real Recovery run |
| 07_HANDOFF.md | 0 | 0 | 0 | 0 | Pending real Recovery run |
| 08_KNOWN_ISSUES.md | 0 | 0 | 0 | 0 | Pending real Recovery run |
| 09_FILE_INDEX.md | 0 | 0 | 0 | 0 | Pending real Recovery run |

## Snapshot accuracy

Not yet calculated.

```txt
snapshot_accuracy = correct_items / reviewed_items
correction_rate = corrected_items / reviewed_items
```

Current values:

| Metric | Value |
|---|---:|
| Correct items | 0 |
| Partially correct items | 0 |
| Incorrect items | 0 |
| Unknown items | 0 |
| Reviewed items | 0 |
| Snapshot accuracy | Not measured |
| Correction rate | Not measured |

## Prompt Maturity Level baseline

### Current estimated baseline

```txt
PML-1
```

Reason:

- The project still needs manual explanation from the user in many cycles.
- The AI can likely use AISDD docs once created, but the real Casa em Dia repository has not yet been proven to support PML-2 or PML-3 execution.

### Target

Near-term target:

```txt
PML-2
```

Example:

```txt
Read docs/START_HERE.md.
Objective: fix one reminder lifecycle bug.
```

Later target:

```txt
PML-3
```

Example:

```txt
Read docs/START_HERE.md.
Objective: CR13.
```

Only claim PML-3 after task IDs are documented clearly enough in `docs/04_NEXT_TASK.md` or equivalent project task records.

## PML test log

| Date | Task | Attempted PML | Successful PML | Result | Notes |
|---|---|---:|---:|---|---|
| 2026-06-21 | Baseline only | 1 | Not tested | Pending | No real Casa em Dia repo audit yet |

## Inventions or hallucinations observed

None measured in a formal Recovery run yet.

Potential hallucination risks to watch:

- invented Android architecture;
- invented database schema;
- invented notification flow;
- invented recurrence behavior;
- treating prior fixed bugs as current bugs;
- treating partially tested behavior as fully validated.

## Missing important facts

- Current file tree.
- Current app modules.
- Current data model.
- Current reminder lifecycle behavior.
- Current notification setup.
- Current manual test checklist.
- Current known issues after the latest working cycle.

## What AISDD already appears to help with

- Separating reported facts from assumptions.
- Preventing large refactors before mapping the real state.
- Defining one next task instead of several simultaneous fixes.
- Making handoff explicit between AI sessions.
- Making prompt maturity measurable through PML.

## What AISDD needs to prove next

- That Recovery Mode can map the actual Casa em Dia source tree accurately.
- That `07_HANDOFF.md` reduces repeated manual recap.
- That a later AI can continue from `START_HERE.md` and `04_NEXT_TASK.md` with minimal context.
- That PML can move from PML-1 to PML-2 or PML-3 in real development cycles.

## Next dogfooding task

Run a real Recovery pass against the Casa em Dia repository.

The next prompt should be minimal:

```txt
This project follows AISDD.
Read docs/START_HERE.md if it exists.
If AISDD docs are missing or incomplete, run Recovery Mode.
Do not modify code.
Create or update only the initial Recovery docs.
Separate FACTS, ASSUMPTIONS, UNKNOWNS, and RISKS.
```

## Acceptance status

Baseline report created.

Not yet validated against source code.

## Updated handoff

Casa em Dia dogfooding has started as a conversation-informed Recovery baseline. The next step is a source-code-audited Recovery run that creates or updates the six initial Recovery docs and measures snapshot accuracy plus PML.
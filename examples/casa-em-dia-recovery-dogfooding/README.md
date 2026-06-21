# Casa em Dia Recovery Dogfooding Case

This is a public dogfooding case for AISDD Recovery Mode.

It is based on a real Android project called **Casa em Dia**, but this example is intentionally limited to process validation.

No proprietary source code is included here.

## Purpose

Use this case to test whether AISDD can be adopted in the middle of an existing project that was not started with AISDD.

The main question is:

> Can Recovery Mode create a useful factual snapshot without inventing the project state?

## Why this case matters

Casa em Dia is useful for dogfooding because it represents a realistic solo-developer AI-assisted project:

- Android app;
- AI-assisted implementation;
- multiple development cycles;
- evolving requirements;
- features already partially implemented;
- bugs and regressions discovered during manual testing;
- need for continuity between AI sessions.

## Recovery Mode validation focus

This case should validate Recovery Mode, not normal AISDD execution.

The primary metric is snapshot accuracy.

## Snapshot accuracy metric

After the first Recovery snapshot, review each generated item and classify it:

| Classification | Meaning |
|---|---|
| Correct | Matches the real project state |
| Partially correct | Mostly true, but needs correction or nuance |
| Incorrect | Does not match the real project state |
| Unknown | Cannot be confirmed yet |

Then calculate:

```txt
snapshot_accuracy = correct_items / reviewed_items
correction_rate = corrected_items / reviewed_items
```

Where:

```txt
corrected_items = partially_correct_items + incorrect_items
reviewed_items = correct_items + partially_correct_items + incorrect_items
```

Unknown items should be tracked separately and not counted as correct.

## Suggested Recovery test

1. Run `templates/prompts/RECOVERY_MODE_PROMPT.md` against the real project.
2. Generate only the initial Recovery docs.
3. Do not refactor or modify code in the first pass.
4. Review the generated docs manually.
5. Count correct, partially correct, incorrect, and unknown items.
6. Record what the AI invented, missed, or misunderstood.
7. Update AISDD Recovery Mode if repeated issues appear.

## Initial documents to evaluate

- `docs/00_PROJECT_RULES.md`
- `docs/03_CURRENT_STATE.md`
- `docs/04_NEXT_TASK.md`
- `docs/07_HANDOFF.md`
- `docs/08_KNOWN_ISSUES.md`
- `docs/09_FILE_INDEX.md`

## Report template

```txt
# Casa em Dia Recovery Dogfooding Report

## Date

TODO

## AI tool used

TODO

## Project state before Recovery

TODO

## Snapshot review

| Document | Correct | Partially correct | Incorrect | Unknown | Notes |
|---|---:|---:|---:|---:|---|
| 00_PROJECT_RULES.md | TODO | TODO | TODO | TODO | TODO |
| 03_CURRENT_STATE.md | TODO | TODO | TODO | TODO | TODO |
| 04_NEXT_TASK.md | TODO | TODO | TODO | TODO | TODO |
| 07_HANDOFF.md | TODO | TODO | TODO | TODO | TODO |
| 08_KNOWN_ISSUES.md | TODO | TODO | TODO | TODO | TODO |
| 09_FILE_INDEX.md | TODO | TODO | TODO | TODO | TODO |

## Snapshot accuracy

- Correct items: TODO
- Partially correct items: TODO
- Incorrect items: TODO
- Unknown items: TODO
- Reviewed items: TODO
- Snapshot accuracy: TODO
- Correction rate: TODO

## Inventions or hallucinations

- TODO

## Missing important facts

- TODO

## What Recovery Mode got right

- TODO

## What Recovery Mode needs to improve

- TODO
```

## Status

This case is a planned public dogfooding report.

It should be filled after Recovery Mode is tested on the real Casa em Dia project.
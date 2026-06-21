# Tutorial 04 — Maintain a Long-Term AISDD Project

## Goal

Keep a project maintainable over months or years.

AISDD maintenance is not only calendar-based.

Run maintenance when the project changes in ways that can make documentation stale.

## Trigger-based maintenance

Run a maintenance pass when any of these happen:

| Trigger | What to check |
|---|---|
| Before a release | Current state, acceptance checks, known issues |
| After architecture changes | Architecture, decisions log, file index |
| After data model or contract changes | Product spec, architecture, acceptance checks |
| After switching AI tools | Handoff, current state, next task |
| After recurring bugs | Known issues, test checklist, acceptance checks |
| After 3 to 5 meaningful tasks | Handoff, current state, file index |

## Weekly checks

- Is `07_HANDOFF.md` short and current?
- Is `04_NEXT_TASK.md` focused on one task?
- Is `09_FILE_INDEX.md` accurate?
- Are decisions logged?
- Are known issues still current?
- Are files growing too large?
- Did prompts get shorter, or is manual context growing again?

## Monthly checks

- Review architecture.
- Review test strategy.
- Close resolved known issues.
- Clean outdated documentation.
- Add ADRs for major decisions.
- Review Prompt Maturity Level trends.

## Optional automation

Run:

```bash
python scripts/check-aisdd-docs.py
python scripts/check-aisdd-staleness.py
```

These scripts detect signals, not truth.

A human or AI review still decides whether the documentation is actually stale.

## Maintenance output

After a maintenance pass, update:

- `docs/07_HANDOFF.md`;
- `docs/03_CURRENT_STATE.md` if project state changed;
- `docs/09_FILE_INDEX.md` if file responsibilities changed;
- `docs/06_DECISIONS_LOG.md` if structural decisions were made;
- `docs/08_KNOWN_ISSUES.md` if risks changed.
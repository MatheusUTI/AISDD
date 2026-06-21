# Working with Multiple AIs

AISDD allows multiple AI tools to work on the same project safely.

## Required discipline

Every AI must start from the repository documentation.

Do not rely on previous chat history.

## Recommended startup context

Provide the AI with:

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
Do not invent missing contracts.
Update affected docs and handoff.
```

## Switching AI tools

When switching tools:

1. Ensure `07_HANDOFF.md` is updated.
2. Ensure `04_NEXT_TASK.md` contains the next task.
3. Ensure `09_FILE_INDEX.md` reflects current structure.
4. Start the new AI from `START_HERE.md`.

## Avoid

- Copying giant chat histories.
- Asking different AIs to work on overlapping tasks.
- Letting the AI invent missing project facts.

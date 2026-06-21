# AISDD Handoff Example

This is an example of a short but useful `docs/07_HANDOFF.md`.

A handoff should help the next AI session continue without a long manual recap.

It should not become a full project history.

## Example

```md
# Handoff

Project: Example Task App

Current state:
- Basic task list exists.
- Create task flow exists.
- Edit task flow exists.
- Archive flow is incomplete.

Latest completed task:
- Added validation to the edit task form.
- Preserved existing storage behavior.
- Updated file index for task form responsibilities.

Next task:
- Fix archived tasks not appearing in the archive screen.

Important files:
- `TaskListScreen` — active task list.
- `TaskFormScreen` — create and edit form.
- `TaskRepository` — task storage boundary.
- `TaskArchiveScreen` — archive display.

Known risks:
- Do not rewrite storage.
- Do not change existing task identifiers.
- Archive behavior is not fully validated.

UNKNOWNS:
- Whether archived tasks should be restorable or read-only.
- Whether deleted tasks should appear in archive.
```

## Why this is good

This handoff is useful because it says:

- what exists;
- what changed last;
- what comes next;
- which files matter;
- what not to break;
- what is still unknown.

## What to avoid

Avoid handoffs that are:

- a full changelog;
- a complete architecture document;
- longer than the current task context;
- vague about real project state;
- missing the next task.

## Size guidance

A good handoff is usually:

- 10 to 20 lines for small projects;
- 20 to 40 lines for complex projects;
- never a replacement for `03_CURRENT_STATE.md`, `09_FILE_INDEX.md`, or `06_DECISIONS_LOG.md`.

## Main rule

The next AI should be able to read the handoff and know where to continue safely.
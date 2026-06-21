# AISDD Templates

This directory contains reusable templates.

## docs/

Universal documentation structure for AISDD projects.

Use this folder when adopting AISDD in a project:

```txt
templates/docs/ → your-project/docs/
```

For the fastest adoption path, copy all docs but fill only the starter files first:

- `00_PROJECT_RULES.md`
- `04_NEXT_TASK.md`
- `07_HANDOFF.md`
- `09_FILE_INDEX.md`

For existing complex projects, use Recovery Mode before normal Starter adoption.

## prompts/

Reusable prompts for project definition, recovery, starting, executing, auditing, and handing off AISDD cycles.

Recommended prompts:

| Prompt | Use when |
|---|---|
| `PROJECT_DEFINITION_WIZARD_PROMPT.md` | Starting from a rough idea |
| `RECOVERY_MODE_PROMPT.md` | Adopting AISDD in an existing complex project |
| `STARTER_ADOPTION_PROMPT.md` | Introducing AISDD into a new or existing repository |
| `TASK_EXECUTION_PROMPT.md` | Running one AISDD task |
| `HANDOFF_PROMPT.md` | Updating continuity between sessions |
| `AUDIT_PROMPT.md` | Checking AISDD compliance |

Use the project definition wizard before coding when the project is not clear yet.

Use Recovery Mode when the project already exists and needs a factual snapshot before more development.
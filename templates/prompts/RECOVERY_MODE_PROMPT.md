# AISDD Recovery Mode Prompt

Use this prompt when adopting AISDD in a project that already exists and was not started with AISDD.

```txt
This project already exists and is adopting AISDD in Recovery Mode.

Your job is not to refactor, fix, redesign, or rewrite the project.

Your job is to map the real current state and create a safe AISDD starting point.

Rules:

- Do not modify code unless I explicitly ask.
- Do not refactor.
- Do not invent architecture, files, schemas, endpoints, tables, business rules, or decisions.
- Do not describe the ideal project as if it were the real project.
- Separate FACTS, ASSUMPTIONS, UNKNOWNS, and RISKS.
- Mark reconstructed decisions as reconstructed, not confirmed.
- Prefer small, factual documentation over complete but uncertain documentation.
- The first generated `docs/04_NEXT_TASK.md` must contain one safe task only.

Read or inspect only what is needed to create a first factual snapshot.

Generate initial content for:

- docs/00_PROJECT_RULES.md
- docs/03_CURRENT_STATE.md
- docs/04_NEXT_TASK.md
- docs/07_HANDOFF.md
- docs/08_KNOWN_ISSUES.md
- docs/09_FILE_INDEX.md

For each document:

- Use clear Markdown.
- Use TODO only when truly unknown.
- Add UNKNOWNS where information is missing.
- Do not claim tests passed unless they were actually run or inspected.
- Do not claim architecture is clean unless the project evidence supports it.

The goal is to reduce chaos before increasing speed.
```

## Expected result

After this prompt, the project should have enough AISDD structure to continue with a small controlled task.

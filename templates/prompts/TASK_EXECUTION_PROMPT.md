# AISDD Task Execution Prompt

Execute the task defined in `docs/04_NEXT_TASK.md`.

Rules:

- Execute only this task.
- Do not perform unrelated cleanup.
- Do not rewrite full files unnecessarily.
- Do not change architecture unless explicitly required.
- Preserve existing contracts.
- Update affected documentation.
- Update `docs/07_HANDOFF.md`.

Before coding, identify:

- FACTS
- ASSUMPTIONS
- UNKNOWNS
- RISKS

If critical information is missing, stop with:

```txt
MISSING INFO
```

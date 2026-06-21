# AISDD Starter Adoption Prompt

Use this prompt when adopting AISDD quickly in a new or existing project.

This is a thin Starter wrapper around the universal AISDD start behavior.

Use it when you want to start with only the Core AISDD files instead of the full documentation set.

```txt
This project follows AISDD.

Read docs/START_HERE.md first.
Then read only the minimum starter context:

- docs/00_PROJECT_RULES.md
- docs/04_NEXT_TASK.md
- docs/07_HANDOFF.md
- docs/09_FILE_INDEX.md

Execute only docs/04_NEXT_TASK.md.

Follow the universal AISDD behavior:

- one task only;
- no invented files, entities, endpoints, tables, contracts, schemas, or business rules;
- preserve existing behavior;
- update affected documentation;
- update docs/07_HANDOFF.md before finishing;
- use the standard AISDD response format.

If critical information is missing, answer only:

MISSING INFO
```

## Maintenance note

The canonical AI behavior lives in:

```txt
templates/prompts/UNIVERSAL_AI_START_PROMPT.md
```

This prompt should stay short and Starter-specific to avoid duplicated rules drifting over time.
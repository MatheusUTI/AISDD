# AISDD File Growth Control

AISDD discourages files that grow indefinitely.

## Suggested limits

- Screens: up to 300 lines.
- Components: up to 150 lines.
- Dialogs: up to 100 lines.
- Controllers/ViewModels: up to 400 lines.
- Helpers: up to 200 lines.

## Required warning

When a file exceeds or approaches the suggested limit, the AI should report:

```txt
FILE GROWTH RISK
```

## Preferred mitigation

- Extract small components.
- Extract helpers.
- Separate responsibilities.
- Preserve behavior.
- Avoid large rewrites.

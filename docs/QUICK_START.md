# AISDD Quick Start

This page has been intentionally simplified.

AISDD now has two primary starting paths:

| Situation | Start here |
|---|---|
| You have a real problem but little structure | [`PROBLEM_FIRST_START.md`](PROBLEM_FIRST_START.md) |
| You want an adaptive LLM interview | [`INTERVIEW_MODE.md`](INTERVIEW_MODE.md) |
| You are a developer or using an agent workflow | [`GETTING_STARTED.md`](GETTING_STARTED.md) |
| You already have a messy or fragile project | [`RECOVERY_MODE.md`](RECOVERY_MODE.md) |
| You want to know what to copy | [`ADOPTION_PACKAGES.md`](ADOPTION_PACKAGES.md) |

## Minimal developer path

Copy the docs template into your project:

```bash
mkdir -p docs
cp -R templates/docs/* your-project/docs/
```

Fill only these files first:

| File | Purpose |
|---|---|
| `docs/00_PROJECT_RULES.md` | Permanent rules and forbidden changes |
| `docs/04_NEXT_TASK.md` | One executable task |
| `docs/07_HANDOFF.md` | Short continuity summary |
| `docs/09_FILE_INDEX.md` | Map of important files |

Then start the AI with:

```txt
This project follows AISDD.
Read docs/START_HERE.md first.
Execute only docs/04_NEXT_TASK.md.
If critical information is missing, answer MISSING INFO.
Update affected docs and docs/07_HANDOFF.md before finishing.
```

## Main promise

AISDD turns AI conversations into lasting software project memory without forcing you to adopt the whole framework at once.

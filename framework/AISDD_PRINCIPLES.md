# AISDD Principles

## P1 — Single source of truth

Every important technical decision must exist in persistent documentation.

## P2 — One task per cycle

Each AI interaction should solve exactly one clearly defined task.

Avoid combining:

- multiple features;
- multiple refactors;
- architecture changes;
- unrelated fixes.

## P3 — Minimum necessary context

Each task should load only the documents needed to execute it safely.

More context does not automatically mean better output.

## P4 — Incremental evolution

Avoid rewriting entire systems without explicit reason.

Prefer:

- small changes;
- safe extractions;
- isolated refactors;
- preserving existing behavior.

## P5 — Continuity between AIs

Any AI should be able to continue the project by reading the repository documentation.

## P6 — Specification-driven engineering

Documentation governs development.

Conversation does not govern development.

## P7 — Explicit uncertainty

AI output must separate facts, assumptions, unknowns, and risks.

## P8 — Contract preservation

Existing public contracts must not be changed silently.

## P9 — Regression awareness

Every change must consider existing behavior.

## P10 — Documentation update discipline

Any change that affects behavior, contracts, architecture, or workflow must update the affected documentation.

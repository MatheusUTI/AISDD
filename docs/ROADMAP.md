# AISDD Roadmap

This roadmap communicates current priorities without locking the project into rigid deadlines.

AISDD should evolve through real usage, dogfooding, and validated feedback.

## Priority levels

| Level | Meaning |
|---|---|
| Short term | Should improve adoption or validation soon |
| Medium term | Important, but depends on early feedback |
| Long term | Useful after the framework matures |

## Short term

| Item | Why it matters | Status |
|---|---|---|
| Executive README | Reduces cognitive load for first-time readers | Added |
| Editorial reconciliation | Clarifies packages vs layers vs navigation paths | Added |
| Adoption packages | Makes clear what users should copy and what belongs only to the framework repo | Added |
| Core vs Advanced guide | Makes clear what is essential and what is optional | Added |
| Prompt Maturity Levels | Measures whether manual prompt context is trending toward zero | Added |
| Handoff example | Shows what a useful `07_HANDOFF.md` looks like | Added |
| Starter prompt deduplication | Reduces prompt drift against the universal prompt | Added |
| Refactor safety boundaries | Clarifies when not to refactor | Added |
| Tutorial maintenance triggers | Aligns long-term tutorial with maintenance policy | Added |
| Real project playbooks | Makes AISDD usable in Casa em Dia and Roteirizador | Added |
| Recovery Mode | Makes AISDD usable in projects that already exist and are becoming complex | Added |
| Recovery snapshot accuracy metric | Measures whether Recovery mapped the real project correctly | Added |
| Casa em Dia Recovery dogfooding baseline | Starts evidence collection without claiming code-audited accuracy | Added |
| Complete practical example project | Helps users understand AISDD by copying a real example | Planned |
| Compliance checklist | Makes adoption reviewable and repeatable | Planned |
| Documentation maintenance guide | Prevents non-loaded docs from becoming stale | Added |
| Staleness check script | Automates simple stale-doc warnings | Added |
| Portuguese Quick Start | Reduces adoption friction for Brazilian users | Added |

## Medium term

| Item | Why it matters | Status |
|---|---|---|
| Source-audited Casa em Dia Recovery report | Replaces baseline claims with real source-checked results | Planned |
| End-to-end example project | Demonstrates AISDD working through multiple cycles | Planned |
| Roteirizador dogfooding report | Validates AISDD in a business-rule-heavy internal tool | Planned |
| PML reports for Casa em Dia and Roteirizador | Shows whether prompts are actually getting smaller | Planned |
| Release and versioning policy | Defines how AISDD changes are published | Planned |
| Governance rules for core changes | Clarifies what counts as sufficient validation | Added initial policy |
| More dogfooding reports | Replaces assumptions with usage evidence | Planned |
| Better automation around docs checks | Reduces manual maintenance burden | Planned |

## Long term

| Item | Why it matters | Status |
|---|---|---|
| Agent integration patterns | Helps autonomous and semi-autonomous agents use AISDD safely | Future |
| More example project types | Shows AISDD across different stacks and domains | Future |
| Full Portuguese translation | Expands accessibility for Brazilian developers | Future |
| Tooling package | Makes setup and validation easier | Future |

## Current focus

The current focus is:

1. Make AISDD easy to adopt.
2. Make the adoption path obvious enough that users do not need explanation.
3. Support new, existing, and long-running projects.
4. Validate AISDD through Casa em Dia and Roteirizador.
5. Measure whether prompt context decreases over time.
6. Reduce documentation maintenance friction.
7. Improve examples, especially handoff and end-to-end usage.
8. Keep the framework vendor-independent and stack-independent.

## Change policy

Roadmap items may change when dogfooding evidence shows that another issue is more important.

Major framework rule changes should be supported by documented validation evidence.
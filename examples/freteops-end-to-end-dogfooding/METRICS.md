# FreteOps Dogfooding Metrics

This file applies the generic metrics from `docs/DOGFOODING_METRICS.md` to the FreteOps case.

## Validation window

Current state: baseline only.

| Requirement | Current | Minimum before core-rule conclusions |
|---|---:|---:|
| AISDD-controlled real tasks completed | 0 | 10 |
| Different task types | 0 | 3 |
| Session handoffs | 0 validated | 3 |
| Structural decisions | 0 validated | 2 |
| Cross-AI continuation tests | 0 | 1 |
| Prompt maturity attempts | 1 planned | 3 |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002 | UX-001 | 4 | Pending | Pending | Test whether repository memory is already sufficient for a single isolated UI task. |

## Prompt-size baseline

Exact token counts were not captured for C000.

Qualitative baseline:

- long natural-language project description;
- stack requirements included manually;
- feature scope included manually;
- exclusions included manually;
- architecture expectations included manually.

For subsequent tasks, record prompt characters where practical.

Suggested comparison:

```txt
prompt_reduction_ratio = current_prompt_chars / baseline_prompt_chars
```

This is a project-specific observation metric, not yet an AISDD core metric.

## Handoff tracking

| Date | Cycle | Meaningful boundary? | Handoff updated? | Accurate on review? | Notes |
|---|---|---:|---:|---:|---|
| 2026-10-15 | C001 | Yes | Yes | Pending | Initial project-memory bootstrap. |

## Decision-log tracking

| Date | Decision | Recorded in project repo? | Notes |
|---|---|---:|---|
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Planned/bootstrapped | Confirm after Gemini adopts the AISDD docs in the project repository. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Planned/bootstrapped | Architectural boundary to validate over future API work. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Planned | Add only from an explicit requirement. |

## Missing-info friction

No valid sample yet.

Record each meaningful `MISSING INFO` event using the generic AISDD classification:

- Critical;
- Assumable;
- Cosmetic.

## Cross-AI continuation plan

FreteOps is specifically suited to this test because implementation and review are already split across AI systems.

First formal test:

1. Gemini completes an AISDD-defined task.
2. Gemini updates project docs and handoff.
3. ChatGPT reads only the repository state, not the implementation conversation.
4. ChatGPT summarizes current state, changed contracts, risks, and next task.
5. Human owner scores accuracy.

Second test later:

1. ChatGPT defines and documents the next task.
2. Gemini receives only the repository and minimal startup prompt.
3. Measure whether manual recap was needed.

## Release-lifecycle evidence

Track these milestones:

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap | 2026-10-15 | C001 | Prepared |
| First repository-driven implementation | TODO | TODO | Pending |
| First real API integration | TODO | TODO | Pending |
| First installed device build | TODO | TODO | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.
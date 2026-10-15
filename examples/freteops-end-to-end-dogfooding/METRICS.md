# FreteOps Dogfooding Metrics

This file applies the generic metrics from `docs/DOGFOODING_METRICS.md` to the FreteOps case.

## Validation window

Current state: baseline plus first environment-access finding.

| Requirement | Current | Minimum before core-rule conclusions |
|---|---:|---:|
| AISDD-controlled real tasks completed | 0 | 10 |
| Different task types | 0 | 3 |
| Session handoffs | 0 validated | 3 |
| Structural decisions | 0 validated | 2 |
| Cross-AI continuation tests | 0 | 1 |
| Prompt maturity attempts | 1 environment-blocked; 1 retry planned | 3 valid attempts |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002-A | UX-001 startup | 4 | Not evaluated | None added | Environment-blocked: Gemini could not access the externally added repository docs from the active AI Studio workspace. This does not count as a PML failure. |
| 2026-10-15 | C002-B | UX-001 retry after workspace bootstrap | 4 | Pending | Pending | Retry only after the canonical AISDD docs are synchronized into the AI Studio project tree. |

## Environment access note

Prompt maturity is meaningful only when the implementing AI has access to the documented project memory.

For FreteOps, the observed tool boundary is currently:

```txt
AI Studio workspace → GitHub
GitHub -/→ active AI Studio workspace
```

Until the project docs are imported into the AI Studio workspace, a short repository-driven prompt cannot be evaluated fairly.

Track this separately from PML so tool synchronization limitations are not misclassified as documentation failures.

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
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Bootstrapped in GitHub | Must also exist in AI Studio workspace before Gemini can consume it. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Bootstrapped in GitHub | Architectural boundary to validate over future API work. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Framework-side evidence recorded | Add to product memory through Gemini after workspace bootstrap. |
| 2026-10-15 | Gemini/AI Studio owns FreteOps implementation and project-memory writes after bootstrap; ChatGPT audits GitHub and owns AISDD framework evidence | Active workflow decision | Avoid external edits to FreteOps docs that AI Studio cannot automatically pull. |

## Missing-info friction

No valid sample yet.

The C002-A response was not `MISSING INFO` friction. Gemini accurately identified unavailable required files, which is an environment/context-delivery problem.

Record future meaningful `MISSING INFO` events using the generic AISDD classification:

- Critical;
- Assumable;
- Cosmetic.

## Cross-AI continuation plan

FreteOps is specifically suited to this test because implementation and review are already split across AI systems.

First formal test:

1. Gemini completes an AISDD-defined task.
2. Gemini updates project docs and handoff.
3. Gemini publishes the workspace state to GitHub.
4. ChatGPT reads only the repository state, not the implementation conversation.
5. ChatGPT summarizes current state, changed contracts, risks, and next task.
6. Human owner scores accuracy.

Reverse-direction tests require an explicit context-delivery step when the target AI environment cannot pull repository changes.

## Release-lifecycle evidence

Track these milestones:

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap in GitHub | 2026-10-15 | C001 | Done |
| AISDD bootstrap in AI Studio workspace | TODO | C002 prerequisite | Pending |
| First repository-memory-driven implementation | TODO | C002-B | Pending |
| First real API integration | TODO | TODO | Pending |
| First installed device build | TODO | TODO | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.
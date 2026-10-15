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
| Prompt maturity attempts | 1 context-unavailable; 1 retry planned | 3 valid attempts |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002-A | UX-001 startup | 4 | Not evaluated | None added | Gemini could not find the externally added AISDD docs in its active workspace. This does not count as a PML failure. |
| 2026-10-15 | C002-B | UX-001 retry after explicit GitHub sync | 4 | Pending | Pending | Retry only after a safe inbound synchronization makes the canonical AISDD docs available in the AI Studio project tree. |

## Environment access note

Prompt maturity is meaningful only when the implementing AI has access to synchronized project memory.

Initial observation suggested a one-way boundary at the AI Studio UI level:

```txt
AI Studio workspace → GitHub
```

A later capability check showed a possible explicit reverse path: Gemini reported that the execution environment provides `git` and `curl`, allowing it to download/synchronize repository files when authentication is available.

The working hypothesis is therefore:

```txt
GitHub
  ↓ explicit authenticated git/curl sync
AI Studio workspace
  ↓ implementation/publish
GitHub
```

This inbound path must still be validated in practice. Until an actual sync succeeds safely, do not count it as proven capability.

Track environment/context delivery separately from PML so synchronization limitations are not misclassified as documentation failures.

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
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Bootstrapped in GitHub | Gemini must receive synchronized project memory before using it. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Bootstrapped in GitHub | Architectural boundary to validate over future API work. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Framework-side evidence recorded | Add to product memory only through a controlled AISDD cycle. |
| 2026-10-15 | GitHub remains canonical memory; AI Studio should explicitly sync required context before AISDD execution | Active workflow hypothesis | Validate safe inbound synchronization before treating this as established workflow. |

## Missing-info friction

No valid sample yet.

The C002-A response was not `MISSING INFO` friction. Gemini accurately identified unavailable required files, which is a context-delivery problem.

Record future meaningful `MISSING INFO` events using the generic AISDD classification:

- Critical;
- Assumable;
- Cosmetic.

## Cross-AI continuation plan

FreteOps is specifically suited to this test because implementation and review are already split across AI systems.

First formal test:

1. Gemini synchronizes the canonical project memory from GitHub.
2. Gemini completes an AISDD-defined task.
3. Gemini updates project docs and handoff.
4. Gemini publishes the workspace state to GitHub.
5. ChatGPT reads only the repository state, not the implementation conversation.
6. ChatGPT summarizes current state, changed contracts, risks, and next task.
7. Human owner scores accuracy.

The reverse direction becomes testable if explicit GitHub synchronization succeeds reliably.

## Release-lifecycle evidence

Track these milestones:

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap in GitHub | 2026-10-15 | C001 | Done |
| Inbound GitHub sync capability reported | 2026-10-15 | C002-SYNC | Reported; not yet verified |
| AISDD docs synchronized into AI Studio workspace | TODO | C002 prerequisite | Pending |
| First repository-memory-driven implementation | TODO | C002-B | Pending |
| First real API integration | TODO | TODO | Pending |
| First installed device build | TODO | TODO | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.

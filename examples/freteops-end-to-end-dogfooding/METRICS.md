# FreteOps Dogfooding Metrics

This file applies the generic metrics from `docs/DOGFOODING_METRICS.md` to the FreteOps case.

## Validation window

Current state: baseline, first completed AISDD-controlled task, and verified manual bidirectional repository synchronization.

| Requirement | Current | Minimum before core-rule conclusions |
|---|---:|---:|
| AISDD-controlled real tasks completed | 1 | 10 |
| Different task types | 1 | 3 |
| Session handoffs | 1 observed; validation still accumulating | 3 |
| Structural decisions | 2 observed | 2 |
| Cross-AI continuation tests | 1 performed; human scoring still informal | 1 |
| Prompt maturity attempts | 1 context-unavailable; 1 completed retry with exact successful PML not yet claimed | 3 valid attempts |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002-A | UX-001 startup | 4 | Not evaluated | None added | Gemini could not find the externally added AISDD docs in its active workspace. This does not count as a PML failure. |
| 2026-10-15 | C002-B | UX-001 after manual workspace sync | 4 intended | Pending exact classification | No repeated task specification observed | Gemini completed UX-001 after repository memory became available. Preserve exact retry prompt before assigning successful PML conclusively. |

## Environment access note

Prompt maturity is meaningful only when the implementing AI has access to synchronized project memory.

The verified FreteOps/AI Studio boundary is:

```txt
GitHub
   ⇅ manual sync action in AI Studio
AI Studio workspace
```

Synchronization works in both directions, but changes do not propagate automatically. The human owner must explicitly trigger synchronization.

This is materially different from both a fully automatic shared workspace and a one-way publish integration.

Operational consequence:

1. GitHub remains canonical memory.
2. Before an AISDD cycle, the human triggers synchronization into AI Studio.
3. Gemini executes from the synchronized repository state.
4. After Gemini publishes changes, the human synchronizes again before another agent relies on the new state.

The synchronization click is environment/context delivery, not task explanation. Therefore it should not reduce the PML score by itself.

Track environment/context delivery separately from PML so synchronization mechanics are not misclassified as documentation failures or prompt overhead.

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
| 2026-10-15 | C001 | Yes | Yes | Yes enough to continue | Initial project-memory bootstrap established the handoff structure. |
| 2026-10-15 | C002-B | Yes | Yes | Yes with minor documentation drift | Gemini closed UX-001 and updated handoff; ChatGPT could reconstruct project state from GitHub, while also identifying small consistency issues that were then corrected. |

## Decision-log tracking

| Date | Decision | Recorded in project repo? | Notes |
|---|---|---:|---|
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Yes | Active baseline. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Yes | Architectural boundary for future API work. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Yes | Firebase or other Google services require explicit need and decision. |
| 2026-10-15 | GitHub remains canonical project memory; AI Studio synchronization is bidirectional but manually triggered | Yes | Added to `START_HERE.md` as a preflight requirement. |

## Missing-info friction

No valid domain `MISSING INFO` sample yet.

The C002-A response was not domain missing-info friction. Gemini accurately identified unavailable required files, which was a context-delivery problem.

Record future meaningful `MISSING INFO` events using the generic AISDD classification:

- Critical;
- Assumable;
- Cosmetic.

## Cross-AI continuation evidence

FreteOps already provides a practical cross-AI boundary:

1. Gemini implemented UX-001 in AI Studio.
2. Gemini updated project docs and handoff.
3. The result reached GitHub.
4. ChatGPT reviewed repository state rather than relying on Gemini's private conversation.
5. ChatGPT correctly identified the completed UX work plus documentation drift and prepared the next contract-discovery cycle.

This is positive evidence for repository-mediated cross-AI continuation, but repeated cycles are still required before making a framework-wide claim.

## Release-lifecycle evidence

Track these milestones:

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap in GitHub | 2026-10-15 | C001 | Done |
| Bidirectional GitHub ↔ AI Studio synchronization | 2026-10-15 | C002-SYNC | Verified; manual trigger required |
| First repository-memory-driven implementation | 2026-10-15 | C002-B | Done; exact successful PML still to classify |
| First contract-discovery cycle | TODO | INT-001 | Prepared |
| First real API integration | TODO | TODO | Pending |
| First installed device build | TODO | TODO | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.

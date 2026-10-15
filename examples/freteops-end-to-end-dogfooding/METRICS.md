# FreteOps Dogfooding Metrics

This file applies the generic metrics from `docs/DOGFOODING_METRICS.md` to the FreteOps case.

## Validation window

Current state: baseline, two AISDD-controlled tasks completed, verified manual bidirectional repository synchronization, and one cross-AI semantic review gate.

| Requirement | Current | Minimum before core-rule conclusions |
|---|---:|---:|
| AISDD-controlled real tasks completed | 2 | 10 |
| Different task types | 2 | 3 |
| Session handoffs | 2 observed; validation still accumulating | 3 |
| Structural decisions | 3 observed | 2 |
| Cross-AI continuation tests | 2 performed | 1 |
| Prompt maturity attempts | 1 context-unavailable; 2 repository-driven attempts | 3 valid attempts |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002-A | UX-001 startup | 4 | Not evaluated | None added | Gemini could not find the externally added AISDD docs in its active workspace. This does not count as a PML failure. |
| 2026-10-15 | C002-B | UX-001 after manual workspace sync | 4 intended | Pending exact classification | No repeated task specification observed | Gemini completed UX-001 after repository memory became available. Preserve exact retry prompt before assigning successful PML conclusively. |
| 2026-10-15 | C003 | INT-001 API-contract specification | 4 | Not yet counted as fully safe | None beyond repository sync/start instruction | Gemini completed the requested specification cycle and handoff from repository memory, but independent review found semantic corrections that had to be gated before code generation. Prompt maturity and output correctness are tracked separately. |

## Environment access note

Prompt maturity is meaningful only when the implementing AI has access to synchronized project memory.

The verified FreteOps/AI Studio boundary is:

```txt
GitHub
   ⇅ manual sync action in AI Studio
AI Studio workspace
```

Synchronization works in both directions, but changes do not propagate automatically. The human owner must explicitly trigger synchronization.

Operational consequence:

1. GitHub remains canonical memory.
2. Before an AISDD cycle, the human triggers synchronization into AI Studio.
3. Gemini executes from the synchronized repository state.
4. After Gemini publishes changes, the human synchronizes again before another agent relies on the new state.

The synchronization click is environment/context delivery, not task explanation. Therefore it should not reduce the PML score by itself.

## Prompt-size baseline

Exact token counts were not captured for C000.

Qualitative baseline:

- long natural-language project description;
- stack requirements included manually;
- feature scope included manually;
- exclusions included manually;
- architecture expectations included manually.

Later repository-driven cycles required only startup instructions plus synchronization, demonstrating strong prompt shrinkage in this case. Exact ratio is not claimed because the original C000 token/character count was not preserved.

## Handoff tracking

| Date | Cycle | Meaningful boundary? | Handoff updated? | Accurate on review? | Notes |
|---|---|---:|---:|---:|---|
| 2026-10-15 | C001 | Yes | Yes | Yes enough to continue | Initial project-memory bootstrap established the handoff structure. |
| 2026-10-15 | C002-B | Yes | Yes | Yes with minor documentation drift | Gemini closed UX-001 and updated handoff; ChatGPT reconstructed state from GitHub and corrected documentation drift. |
| 2026-10-15 | C003 | Yes | Yes | Structurally accurate, semantically overconfident in some fallbacks | Gemini closed INT-001 and advanced INT-002, but reviewer gate was required before coding. |

## Decision-log tracking

| Date | Decision | Recorded in project repo? | Notes |
|---|---|---:|---|
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Yes | Active baseline. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Yes | Architectural boundary for future API work. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Yes | Firebase or other Google services require explicit need and decision. |
| 2026-10-15 | GitHub remains canonical project memory; AI Studio synchronization is bidirectional but manually triggered | Yes | Added to `START_HERE.md` as a preflight requirement. |
| 2026-10-15 | Cross-AI semantic review may gate implementation after a specification cycle | Case-level only | Added as `docs/12_INT001_REVIEW_GATE.md`; not yet promoted to AISDD core. |

## Missing-info friction

A meaningful domain-unknown sample now exists in INT-001:

- NF → CTRC resolution was not supported by the factual baseline;
- Gemini preserved it as `UNKNOWN` / `NF_RESOLUTION_UNSUPPORTED` rather than inventing an upstream flow.

This is positive evidence for explicit unknown handling.

## Cross-AI continuation evidence

### Test 1 — UX-001

1. Gemini implemented UX-001 in AI Studio.
2. Result and handoff reached GitHub.
3. ChatGPT reviewed repository state without relying on Gemini conversation.
4. ChatGPT identified both successful UI work and memory drift.

### Test 2 — INT-001

1. ChatGPT prepared factual baseline and task memory in GitHub.
2. Human synchronized GitHub → AI Studio.
3. Gemini produced the API contract and handoff.
4. Human synchronized result → GitHub.
5. ChatGPT independently audited the contract against source evidence.
6. Review identified semantic overreach before it reached production code and created a repository-level correction gate.

This is stronger evidence for repository-mediated multi-AI work than simple continuation alone: the second AI acted as an independent reviewer, not merely a summarizer.

## Release-lifecycle evidence

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap in GitHub | 2026-10-15 | C001 | Done |
| Bidirectional GitHub ↔ AI Studio synchronization | 2026-10-15 | C002-SYNC | Verified; manual trigger required |
| First repository-memory-driven implementation | 2026-10-15 | C002-B | Done; exact successful PML still to classify |
| First contract-discovery cycle | 2026-10-15 | C003 / INT-001 | Done; reviewer corrections gated before implementation |
| First cross-AI semantic review gate | 2026-10-15 | C003-REVIEW | Done |
| Android DTO/mapper/API boundary | TODO | INT-002 | Prepared |
| First real backend/API integration | TODO | TODO | Pending |
| First installed device build | TODO | TODO | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.

Prompt maturity and output correctness must remain separate metrics: a minimal prompt can successfully deliver project context while the model still makes a semantic mistake that an acceptance/review stage catches.

# FreteOps Dogfooding Metrics

This file applies the generic metrics from `docs/DOGFOODING_METRICS.md` to the FreteOps case.

## Validation window

Current state: baseline plus eight completed AISDD-controlled product cycles, one environment-blocked attempt, verified manual bidirectional repository synchronization, repeated cross-AI semantic review, backend implementation, and one external-data-gated live-validation cycle in progress.

| Requirement | Current | Minimum before core-rule conclusions |
|---|---:|---:|
| AISDD-controlled real tasks completed | 8 completed; INT-006 preparation complete/live gate open | 10 |
| Different task types | 6+ | 3 |
| Session handoffs | 7+ observed | 3 |
| Structural decisions | 8+ observed | 2 |
| Cross-AI continuation/review tests | 5+ performed | 1 |
| Prompt maturity attempts | 1 context-unavailable; 5 repository-driven Gemini attempts | 3 valid attempts |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task. INT-006 does not count as fully completed until live/staging acceptance closes.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002-A | UX-001 startup | 4 | Not evaluated | None added | Required repository memory was not yet available in workspace. Environment-blocked, not a PML failure. |
| 2026-10-15 | C002-B | UX-001 after manual workspace sync | 4 intended | Pending exact classification | No repeated task specification observed | Gemini completed UX-001 from repository memory; later review found only small memory drift. |
| 2026-10-15 | C003 | INT-001 API-contract specification | 4 | Not counted as fully safe | None beyond repository sync/start instruction | Specification completed, but independent review found semantic corrections before code generation. |
| 2026-10-15 | C004 | INT-002 Android contract boundary | 4 | Not counted as fully safe | None beyond repository sync/start instruction | Exact prompt preserved; implementation completed across Gemini 3.8→3.6 checkpoint fallback, then G1–G6 review gate was required. |
| 2026-10-15 | C004R | INT-002R remediation | 4 | Not counted as fully safe | None beyond repository sync/start instruction | Main fidelity gaps were fixed, but final static review still found chronology/scheduling issues. |
| 2026-10-15 | C004R2 | INT-002R2 surgical remediation | 4 | Completed with final reviewer patch | None beyond repository sync/start instruction | Gemini 3.5 handled the small task; ChatGPT then patched sequence fallback and Android API-level compatibility. |

Backend cycles C005–C008 are not counted as PML trials because ChatGPT continued inside the same long-running conversation while reading repository memory; they are useful continuity evidence, but not cold-start prompt-maturity evidence.

## Environment access note

Prompt maturity is meaningful only when the implementing AI has access to synchronized project memory.

Verified boundary:

```txt
GitHub
   ⇅ manual sync action in AI Studio
AI Studio workspace
```

Synchronization works in both directions but requires an explicit human action. The synchronization click is environment/context delivery, not task explanation.

## Model/checkpoint and tool continuity

During C004, Gemini 3.8 Flash performed most edits, hit quota, and AI Studio resumed from checkpoint with Gemini 3.6 Flash without task restatement.

Later, quota pressure changed the tool allocation entirely: Gemini was reduced to UI/build/quick-fix duty while ChatGPT continued architecture and backend implementation directly through GitHub. The project did not require re-bootstrap; repository memory and handoff documents were sufficient to preserve direction.

This is stronger evidence for **tool-role portability** than for any specific AI Studio checkpoint feature.

## Handoff tracking

| Date | Cycle | Meaningful boundary? | Handoff updated? | Accurate on review? | Notes |
|---|---|---:|---:|---:|---|
| 2026-10-15 | C001 | Yes | Yes | Yes enough to continue | Initial project-memory bootstrap. |
| 2026-10-15 | C002-B | Yes | Yes | Yes with minor documentation drift | UI work was correct; docs needed small reconciliation. |
| 2026-10-15 | C003 | Yes | Yes | Structurally accurate, semantically overconfident in some fallbacks | Cross-AI gate R1–R11 required. |
| 2026-10-15 | C004 | Yes | Yes | Structurally accurate; some DTO→domain fidelity overstated | Cross-AI gate G1–G6 required. |
| 2026-10-15 | C004R2 | Yes | Yes | Accurate after final reviewer patch | Android contract boundary closed. |
| 2026-10-15 | C005–C007 | Yes | Yes | Sufficient to continue across architecture→backend→connector | Implementer environment changed from AI Studio to GitHub/ChatGPT. |
| 2026-10-15 | C008 | Yes | Yes | Accurate; explicitly records external-data blocker | Live SSW gate remains open without inventing evidence. |

## Decision-log tracking

| Date | Decision | Recorded in project repo? | Notes |
|---|---|---:|---|
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Yes | Active baseline. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Yes | Architectural boundary. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Yes | External services require explicit need/decision. |
| 2026-10-15 | GitHub remains canonical project memory; AI Studio sync is bidirectional/manual | Yes | Preflight documented. |
| 2026-10-15 | Cross-AI semantic review may gate downstream implementation | Case-level | Demonstrated repeatedly. |
| 2026-10-15 | Backend is Python/FastAPI, container-first and provider-neutral initially | Yes | Provider selection deferred until live latency evidence. |
| 2026-10-15 | FreteOps backend owns SSW integration; Android never does | Yes | Implemented through connector boundary. |
| 2026-10-15 | Live validation is an explicit external-evidence gate | Yes | CI/offline work may complete while not-found/layout/latency remain unknown. |

## Missing-info friction

Meaningful domain-unknown evidence:

- NF → CTRC resolution remains unproven and preserved as `NF_RESOLUTION_UNSUPPORTED`;
- live SSW not-found signature remains unproven;
- current SSW layout/latency remain unverified until authorised smoke.

The project keeps these as explicit external-evidence gates instead of filling them with plausible defaults.

## Cross-AI / cross-tool continuation evidence

### Test 1 — UX-001
Gemini implemented from synchronized repository memory; ChatGPT reconstructed/reviewed from GitHub only.

### Test 2 — INT-001
ChatGPT prepared baseline/task → Gemini specified contract → GitHub → ChatGPT review → R1–R11 gate.

### Test 3 — INT-002
ChatGPT prepared gate/task → Gemini implemented via tiny repository-driven prompt → GitHub → ChatGPT review → G1–G6 gate.

### Test 4 — INT-002R/INT-002R2
Gemini models changed due quota while repository task continuity remained intact; ChatGPT applied the final compatibility patch without redesigning the task.

### Test 5 — Backend role migration
Without a new project bootstrap, implementation ownership shifted from AI Studio/Gemini to ChatGPT/GitHub for INT-003→INT-006 preparation. Architecture, contracts and handoff remained usable across the tool boundary.

## Release-lifecycle evidence

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap in GitHub | 2026-10-15 | C001 | Done |
| Bidirectional GitHub ↔ AI Studio synchronization | 2026-10-15 | C002-SYNC | Verified; manual trigger required |
| First repository-memory-driven implementation | 2026-10-15 | C002-B | Done |
| First contract-discovery cycle | 2026-10-15 | C003 / INT-001 | Done with review gate |
| Android DTO/mapper/API boundary | 2026-10-15 | C004–C004R2 | Done after reviewer remediation |
| First model/checkpoint fallback without task restatement | 2026-10-15 | C004 | Observed |
| Backend architecture | 2026-10-15 | C005 / INT-003 | Done |
| Backend contract-first skeleton | 2026-10-15 | C006 / INT-004 | Done |
| Real SSW 101 connector code | 2026-10-15 | C007 / INT-005 | Implemented offline; live gate pending |
| Backend CI + live-validation tooling | 2026-10-15 | C008 / INT-006 prep | Done; CI green |
| First authorised live SSW smoke | TODO | INT-006 | Pending external evidence |
| First staging backend | TODO | INT-006 | Pending live metrics |
| First Android→staging real lookup | TODO | INT-006 | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.

Prompt maturity, environment continuity, build/test success, semantic correctness and external-evidence closure must be tracked separately.

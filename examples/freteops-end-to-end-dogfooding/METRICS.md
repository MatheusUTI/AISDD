# FreteOps Dogfooding Metrics

This file applies the generic metrics from `docs/DOGFOODING_METRICS.md` to the FreteOps case.

## Validation window

Current state: baseline, three AISDD-controlled tasks attempted/completed, verified manual bidirectional repository synchronization, and two cross-AI semantic review gates.

| Requirement | Current | Minimum before core-rule conclusions |
|---|---:|---:|
| AISDD-controlled real tasks completed | 3 implementation/spec cycles executed | 10 |
| Different task types | 3 | 3 |
| Session handoffs | 3 observed | 3 |
| Structural decisions | 4 observed | 2 |
| Cross-AI continuation/review tests | 3 performed | 1 |
| Prompt maturity attempts | 1 context-unavailable; 3 repository-driven attempts | 3 valid attempts |

The pre-AISDD scaffold is tracked as cycle C000 but does not count as an AISDD-controlled task.

## Prompt maturity log

| Date | Cycle | Task | Attempted PML | Successful PML | Manual context required | Notes |
|---|---|---|---:|---:|---|---|
| 2026-10-15 | C000 | Initial Android scaffold | 0 | 0 | High | Most project context lived in the prompt. |
| 2026-10-15 | C002-A | UX-001 startup | 4 | Not evaluated | None added | Required repository memory was not yet available in workspace. Environment-blocked, not a PML failure. |
| 2026-10-15 | C002-B | UX-001 after manual workspace sync | 4 intended | Pending exact classification | No repeated task specification observed | Gemini completed UX-001 from repository memory; later review found only small memory drift. |
| 2026-10-15 | C003 | INT-001 API-contract specification | 4 | Not counted as fully safe | None beyond repository sync/start instruction | Gemini completed the requested specification cycle, but independent review found semantic corrections before code generation. |
| 2026-10-15 | C004 | INT-002 Android contract boundary | 4 | Not counted as fully safe yet | None beyond repository sync/start instruction | Exact prompt preserved: `Leia docs/START_HERE.md e execute somente docs/04_NEXT_TASK.md.` Implementation completed, including a model/checkpoint fallback after quota; independent review found G1–G6 fidelity gaps requiring INT-002R. |

## Environment access note

Prompt maturity is meaningful only when the implementing AI has access to synchronized project memory.

Verified boundary:

```txt
GitHub
   ⇅ manual sync action in AI Studio
AI Studio workspace
```

Synchronization works in both directions but requires an explicit human action. The synchronization click is environment/context delivery, not task explanation.

## Model/checkpoint continuity observation

During C004, Gemini 3.8 Flash performed most edits, then execution hit a quota limit. AI Studio resumed from checkpoint with Gemini 3.6 Flash and completed the handoff/next-task documentation without requiring the human to restate the project task.

This is useful case evidence that repository memory plus environment checkpointing can preserve continuity across a model fallback. It is not yet a framework-wide claim because the checkpoint behavior belongs to the AI Studio environment.

## Prompt-size baseline

Exact token counts were not captured for C000.

Qualitative baseline:

- long natural-language project description;
- stack requirements included manually;
- feature scope included manually;
- exclusions included manually;
- architecture expectations included manually.

Later repository-driven cycles required only a short startup instruction plus synchronization. Exact reduction ratio is not claimed because the original C000 token/character count was not preserved.

## Handoff tracking

| Date | Cycle | Meaningful boundary? | Handoff updated? | Accurate on review? | Notes |
|---|---|---:|---:|---:|---|
| 2026-10-15 | C001 | Yes | Yes | Yes enough to continue | Initial project-memory bootstrap. |
| 2026-10-15 | C002-B | Yes | Yes | Yes with minor documentation drift | UI work was correct; docs needed small reconciliation. |
| 2026-10-15 | C003 | Yes | Yes | Structurally accurate, semantically overconfident in some fallbacks | Cross-AI gate R1–R11 required. |
| 2026-10-15 | C004 | Yes | Yes | Structurally accurate; some DTO→domain fidelity overstated | Cross-AI gate G1–G6 required before backend. |

## Decision-log tracking

| Date | Decision | Recorded in project repo? | Notes |
|---|---|---:|---|
| 2026-10-15 | Android native with Kotlin/Compose remains the implementation baseline | Yes | Active baseline. |
| 2026-10-15 | Mobile client must not contain external-system credentials or fragile integration logic | Yes | Architectural boundary. |
| 2026-10-15 | Google services beyond AI Studio are not default dependencies | Yes | External services require explicit need/decision. |
| 2026-10-15 | GitHub remains canonical project memory; AI Studio sync is bidirectional/manual | Yes | Preflight documented. |
| 2026-10-15 | Cross-AI semantic review may gate downstream implementation | Case-level | Demonstrated in INT-001 and INT-002. |
| 2026-10-15 | Backend specification is deferred until Android contract fidelity gate G1–G6 closes | Yes | Avoids building server against lossy client mapping. |

## Missing-info friction

Meaningful domain-unknown evidence:

- NF → CTRC resolution remains unproven;
- the system preserved it as `UNKNOWN` / `NF_RESOLUTION_UNSUPPORTED` rather than inventing an upstream flow.

This remains positive evidence for explicit unknown handling.

## Cross-AI continuation evidence

### Test 1 — UX-001

Gemini implemented from synchronized repository memory; ChatGPT reconstructed and reviewed from GitHub only.

### Test 2 — INT-001

ChatGPT prepared baseline/task → Gemini specified contract → GitHub → ChatGPT independently reviewed against evidence → review gate R1–R11.

### Test 3 — INT-002

ChatGPT prepared reviewer gate/task → Gemini implemented DTO/domain/API boundary using only repository-driven prompt → GitHub → ChatGPT statically audited implementation → review gate G1–G6.

This third test is especially useful because the output compiled/tests reportedly passed yet the independent reviewer still found semantic fidelity gaps. Passing tests and successful context delivery therefore did not guarantee full contract correctness.

## Release-lifecycle evidence

| Milestone | Date | Evidence | Status |
|---|---|---|---|
| Initial generated prototype | 2026-10-15 | C000 | Done |
| AISDD bootstrap in GitHub | 2026-10-15 | C001 | Done |
| Bidirectional GitHub ↔ AI Studio synchronization | 2026-10-15 | C002-SYNC | Verified; manual trigger required |
| First repository-memory-driven implementation | 2026-10-15 | C002-B | Done |
| First contract-discovery cycle | 2026-10-15 | C003 / INT-001 | Done with review gate |
| First Android DTO/mapper/API boundary | 2026-10-15 | C004 / INT-002 | Implemented; G1–G6 remediation pending |
| First model/checkpoint fallback without task restatement | 2026-10-15 | C004 | Observed |
| First real backend/API integration | TODO | INT-003+ | Pending |
| First installed device build | TODO | TODO | Pending |
| First internal distribution build | TODO | TODO | Pending |
| First post-release task | TODO | TODO | Pending |

## Evidence quality rule

Do not convert a single successful cycle into a framework claim.

FreteOps observations should remain case evidence until the minimum validation window is reached or an early-exception safety problem is demonstrated.

Prompt maturity, environment continuity, build/test success, and semantic correctness must be tracked separately. A tiny PML-4 prompt may deliver sufficient context while the implementation still needs independent review.

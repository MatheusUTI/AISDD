# FreteOps Dogfooding Cycle Log

This log records execution cycles, not general conversation history.

A cycle should represent one meaningful project task or one AISDD workflow experiment.

## Log

| Cycle | Date | Task | Implementer | Reviewer | Attempted PML | Result | Handoff updated? | Notes |
|---|---|---|---|---|---:|---|---:|---|
| C000 | 2026-10-15 | Initial Android scaffold | Gemini / AI Studio | Human + ChatGPT | 0 | Completed | No | Long manual prompt carried product, stack, UI, and architecture context. This is the pre-AISDD baseline. |
| C001 | 2026-10-15 | AISDD project-memory bootstrap | ChatGPT | Human | N/A | Prepared | Yes | Repository docs introduced immediately after first prototype. No product code change intended. |
| C002-A | 2026-10-15 | UX-001 startup attempt | Gemini / AI Studio | Human + ChatGPT | 4 | Context unavailable before execution | N/A | Gemini correctly reported that `docs/START_HERE.md` and `docs/04_NEXT_TASK.md` were absent from its active workspace. PML was therefore not evaluated because repository memory was unavailable to the implementer. |
| C002-SYNC | 2026-10-15 | Validate GitHub ↔ AI Studio synchronization | Human + AI Studio | ChatGPT | N/A | Verified | N/A | Bidirectional synchronization is available through the AI Studio/GitHub integration, but it is manually triggered by the human owner. Changes do not propagate automatically. |
| C002-B | 2026-10-15 | UX-001 — legibility, contrast, and visual hierarchy | Gemini / AI Studio | Human + ChatGPT | 4 intended | Completed | Yes | After project memory became available in the AI Studio workspace, Gemini completed UX-001, updated project docs/handoff, and published the result to GitHub. Exact successful PML remains unclaimed until the final prompt evidence for this retry is preserved. |
| C003-PREP | 2026-10-15 | Prepare INT-001 SSW 101 contract discovery | ChatGPT | Human | N/A | Prepared | Yes | FreteOps repository received an observed SSW 101 baseline, strengthened acceptance criteria, file index updates, and a sync preflight. Gemini can consume these changes after the human manually triggers AI Studio synchronization. |
| C003 | 2026-10-15 | INT-001 — specify public SSW 101 API contract | Gemini / AI Studio | Human + ChatGPT | 4 | Completed with reviewer corrections required | Yes | Gemini executed from repository memory with a minimal startup prompt, created `11_SSW101_API_CONTRACT.md`, updated architecture/acceptance/handoff, and advanced to INT-002. No functional APK code changed. |
| C003-REVIEW | 2026-10-15 | Cross-AI audit of INT-001 | ChatGPT | Human | N/A | Review gate added | Yes | Independent review found semantic risks before implementation: wrong series assumption, unsafe `EM_TRANSITO` fallback, synthetic occurrence/current-unit fallbacks, excessive non-null assumptions, and invented backend URL example. `12_INT001_REVIEW_GATE.md` blocked direct code generation until reconciliation. |
| C004 | 2026-10-15 | INT-002 — reconcile contract and implement Android data boundary | Gemini 3.8 Flash → Gemini 3.6 Flash / AI Studio | Human + ChatGPT | 4 | Implementation completed; reviewer remediation required | Yes | Exact prompt preserved: `Leia docs/START_HERE.md e execute somente docs/04_NEXT_TASK.md.` Gemini 3.8 edited the main code/docs, hit quota, and AI Studio resumed from checkpoint with Gemini 3.6. DTOs, mapper, Retrofit API, HTTP repository, nullable domain, cache UI and tests were produced. |
| C004-REVIEW | 2026-10-15 | Cross-AI audit of INT-002 | ChatGPT | Human | N/A | Review gate G1–G6 added | Yes | Static review approved the architecture but found remaining fidelity gaps: factual status text discarded, timing/cargo fields dropped, synthetic occurrence code fallback, over-eager location parsing, timeline coherence not enforced, and mocks inconsistent with full CTRC format/product neutrality. |
| C004R | 2026-10-15 | INT-002R — remediate G1–G6 | Gemini 3.6 Flash / AI Studio | Human + ChatGPT | 4 | Completed; two final defects found in review | Yes | Repository-driven remediation fixed the main fidelity gaps. Reviewer then found two surgical issues: chronology still used `sequence` fallback and the mock contradicted the factual scheduling rule. |
| C004R2 | 2026-10-15 | INT-002R2 — final chronology/scheduling correction | Gemini 3.5 / AI Studio + ChatGPT final patch | Human + ChatGPT | 4 | Completed | Yes | Gemini corrected real-date ordering and the scheduling mock; ChatGPT then removed the remaining sequence fallback and replaced `java.time` usage with an API-24-safe parser, adding targeted tests. |
| C005 | 2026-10-15 | INT-003 — backend architecture specification | ChatGPT via GitHub | Human | N/A | Completed | Yes | Heavy development moved away from Gemini because of AI Studio quota pressure. ChatGPT read repository memory plus RCSVGA evidence and defined the FastAPI/backend/session/cache/staging architecture without changing the Android contract. |
| C006 | 2026-10-15 | INT-004 — contract-first backend skeleton | ChatGPT via GitHub | Human + automated tests | N/A | Completed | Yes | FastAPI/Pydantic backend, fake connector, in-memory cache, public error mapping, Dockerfile and offline tests were added without touching the real SSW. |
| C007 | 2026-10-15 | INT-005 — real SSW 101 connector implementation | ChatGPT via GitHub | Human + automated tests | N/A | Completed offline | Yes | Read-only connector, session factory, P1/detail/occurrence flow, parser, sanitised fixtures and concurrency guard were implemented from the documented RCSVGA evidence. Live credentials were deliberately not used. |
| C008 | 2026-10-15 | INT-006 — live-validation preparation | ChatGPT via GitHub | Human + GitHub Actions | N/A | Preparation completed; external-data gate open | Yes | Added opt-in preflight/smoke helpers, phase metrics, leak check, safe env template and backend CI. Offline suite reached 35 passing tests; GitHub Actions compile/test/container workflow passed. Live SSW evidence remains intentionally blocked on private credentials + authorised CTRCs. |

## Required fields for future cycles

When adding a cycle, record:

- task ID;
- date;
- implementing AI/tool;
- reviewing AI/person;
- prompt text or prompt class when relevant;
- attempted PML;
- successful PML;
- files/contracts changed;
- acceptance result;
- whether handoff was updated;
- any repeated context that still had to be supplied manually;
- any hallucination, scope drift, or unnecessary implementation;
- whether the next AI could continue from repository memory alone;
- whether the implementing environment actually had access to synchronized repository memory;
- whether synchronization was automatic or required a human action;
- whether execution changed model/checkpoint because of quota or environment constraints.

## Cycle closure rule

A product cycle is not considered complete for dogfooding purposes until:

1. implementation has stopped;
2. acceptance checks were performed or explicitly marked not tested;
3. current state is accurate;
4. decisions or known issues were updated if affected;
5. `07_HANDOFF.md` reflects what the next session needs;
6. the next task is singular and executable.

## Prompt evidence rule

Do not claim a PML level because the prompt was short.

Record the highest level only when the task was completed safely at that level.

If a short prompt fails and manual context must be added, record both:

```txt
Attempted PML: 4
Successful PML: 2
```

The failure is useful evidence.

If the AI cannot access or synchronize the repository memory at all, classify the attempt as context/environment-blocked rather than as a PML failure. PML measures how much manual task context is needed when the documented context is actually available.

A manual synchronization click is an environment-delivery step, not manual task context. Do not lower PML merely because the human had to synchronize the workspace before execution.

A task may use PML-4-sized prompting and still fail acceptance for semantic reasons. Record prompt maturity and output quality separately rather than hiding review findings by lowering the PML label automatically.

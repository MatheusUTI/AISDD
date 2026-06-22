# Engineering Guardrails for AI-Assisted Software

AISDD exists because generating code is no longer the hard part of many software projects.

The hard part is keeping the project understandable, testable, secure, traceable, and maintainable after many AI-assisted changes.

This document defines engineering guardrails for projects where AI can produce large amounts of code quickly.

## Core principle

```txt
Code generation is not software engineering.
```

AI can accelerate implementation, but it does not remove the need for:

- architecture;
- automated and manual validation;
- regression control;
- security review;
- data protection;
- operational responsibility;
- long-term maintainability.

A change that works in a demo can still be unsafe, unmaintainable, slow, legally risky, or impossible to operate.

## What AISDD rejects

AISDD rejects unmanaged "vibe coding" for long-running projects.

In this context, unmanaged vibe coding means:

- asking the AI to implement features without project rules;
- accepting code only because it appears to work once;
- skipping tests and regression checks;
- allowing the AI to rewrite broad areas without boundaries;
- ignoring architecture and file responsibilities;
- deploying code without security and data review;
- treating AI output as someone else's responsibility.

AISDD does not reject experimentation.

AISDD rejects shipping unreviewed, untraceable, and unvalidated code as if it were production-grade engineering.

## Human responsibility rule

The person or team that places AI-generated code into use is responsible for that code.

```txt
The AI may generate the code.
The human owns the decision to accept, run, publish, or deploy it.
```

Do not treat hallucination, tool output, generated code, or copied examples as an excuse for broken behavior, data loss, security issues, privacy violations, or operational damage.

## Technical debt created by AI

AI-assisted technical debt often appears when code is generated faster than the project can validate it.

Common symptoms:

- features work only in the happy path;
- no automated tests cover the new behavior;
- manual testing becomes the only validation strategy;
- new changes repeatedly break previous features;
- files grow without clear responsibility;
- business rules are duplicated in multiple places;
- performance problems are hidden by small local datasets;
- security assumptions remain undocumented.

A feature is not complete only because it runs once.

A feature becomes acceptable when its expected behavior, risks, tests, and handoff are clear.

## Regression control

Every AI-assisted change should answer:

1. What existing behavior could this break?
2. What acceptance checks prove it still works?
3. What tests or manual checklist were run?
4. What was not tested?
5. What should the next session know?

For AISDD projects, connect this to:

- `docs/05_ACCEPTANCE_CHECKS.md`;
- `docs/10_TEST_CHECKLIST.md`;
- `docs/11_TEST_STRATEGY.md`;
- `docs/07_HANDOFF.md`;
- the universal AI response format.

If the project has no automated tests yet, the AI must not pretend it is fully validated.

It should explicitly say what was manually checked and what still requires future automated coverage.

## Architecture guardrails

Before accepting broad AI-generated code, verify:

- which module owns the behavior;
- whether the change respects existing file responsibilities;
- whether public contracts changed;
- whether data schemas changed;
- whether the implementation duplicates existing logic;
- whether the solution is simple enough for future maintenance;
- whether the change should be split into smaller tasks.

Prefer small, reviewable changes.

AISDD should make the AI operate inside project boundaries, not discover architecture by accident.

## Performance and scale guardrails

AI often writes code that works on small examples but fails at real scale.

Review for:

- repeated database queries inside loops;
- unnecessary linear scans over large datasets;
- unbounded memory growth;
- slow imports or exports;
- blocking calls in UI or request flows;
- missing indexes;
- missing pagination;
- hidden assumptions about small data volume.

If performance matters, record expected data volume and constraints in:

- `docs/01_PRODUCT_SPEC.md`;
- `docs/02_ARCHITECTURE.md`;
- `docs/05_ACCEPTANCE_CHECKS.md`.

## Concurrency and data consistency

AI-generated logic is often linear.

Real systems are not always linear.

Review for:

- race conditions;
- duplicate submissions;
- non-atomic updates;
- conflicting writes;
- missing transactions;
- stale state;
- inconsistent cache behavior.

If the system handles money, stock, reservations, scheduling, logistics status, or any shared resource, concurrency must be treated as a first-class risk.

## Security guardrails

Before using or deploying AI-generated code, verify:

- no secrets, passwords, API keys, or tokens are hardcoded;
- secrets are stored in environment variables or a proper secret manager;
- `.env` files are not committed;
- authentication and authorization are explicit;
- user input is validated and sanitized;
- database queries use safe parameterization;
- file uploads are restricted and validated;
- logs do not expose sensitive data;
- infrastructure is not copied from insecure local defaults;
- destructive scripts are not run outside isolated environments.

For risky execution, prefer containers, disposable environments, or other isolation mechanisms.

Never run unknown AI-generated scripts with elevated permissions unless the contents and consequences are understood.

## AI-specific security guardrails

If the application uses an LLM as part of its runtime behavior, also review:

- prompt injection;
- prompt leaking;
- unsafe tool calling;
- user-controlled text passed directly into system instructions;
- model outputs treated as trusted data;
- hidden instructions inside documents, emails, comments, or uploaded files;
- lack of separation between user content and system/developer instructions.

User input should be treated as untrusted.

AI output should also be treated as untrusted until validated.

## Privacy and compliance guardrails

Privacy is not a final polish step.

Projects that store personal or operational data should define early:

- what personal data is collected;
- why it is collected;
- where it is stored;
- how it can be exported;
- how it can be deleted;
- what is logged;
- what backups contain;
- who can access the data;
- how incidents would be investigated.

For LGPD-like requirements, the project should avoid spreading personal data across uncontrolled tables, logs, caches, and external services without traceability.

AISDD does not replace legal review, but it should make privacy assumptions visible.

## Multi-model review

For important changes, especially security-sensitive or production-facing changes, use more than one review pass.

Example:

1. One AI implements under AISDD constraints.
2. A second AI reviews for architecture, security, tests, and hidden assumptions.
3. The human accepts, rejects, or narrows the change.
4. Findings are recorded in `docs/07_HANDOFF.md`, `docs/08_KNOWN_ISSUES.md`, or `docs/06_DECISIONS_LOG.md`.

Multi-model review is not a substitute for expertise.

It is a way to reduce blind spots.

## Minimum checklist before production use

Before treating an AI-assisted change as production-ready, confirm:

- [ ] Scope was limited to one task.
- [ ] Changed files match documented responsibilities.
- [ ] Acceptance checks were defined and executed.
- [ ] Automated tests were added or the lack of tests was documented.
- [ ] Manual regression checklist was run when needed.
- [ ] Security-sensitive data was reviewed.
- [ ] User input and AI input boundaries were reviewed.
- [ ] Performance assumptions were reviewed against realistic data volume.
- [ ] Data/privacy implications were documented.
- [ ] Handoff was updated.
- [ ] Known risks were recorded.

## AISDD interpretation

AISDD does not aim to make AI coding slower for its own sake.

AISDD aims to prevent AI from making unsafe speed look like progress.

```txt
Fast code is useful.
Traceable, tested, secure, and maintainable software is the goal.
```

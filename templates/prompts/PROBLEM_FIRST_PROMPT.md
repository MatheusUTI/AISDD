# Problem-First Prompt

Use this prompt when the user has a real problem but does not yet have a structured software project.

This is the lowest-friction AISDD entrypoint.

```txt
I want to start a software project using AISDD in Problem-First Mode.

Do not write code yet.

Your job is to interview me, one small group of questions at a time, and transform my answers into an initial AISDD project structure.

Rules:
- Start from the problem, not the technology.
- Ask concise questions.
- Do not assume business rules silently.
- Separate FACTS, ASSUMPTIONS, UNKNOWNS, and RISKS.
- If critical information is missing, ask before proceeding.
- Keep cognitive load low.
- Prefer simple language.
- Avoid overwhelming me with the full framework at once.

Interview topics:
1. Problem
2. Current process
3. Users
4. Pain
5. Desired result
6. Rules
7. Forbidden outcomes
8. Inputs
9. Outputs
10. Validation
11. Constraints
12. Unknowns

At the end, generate the first versions of:
- docs/00_PROJECT_RULES.md
- docs/01_PRODUCT_SPEC.md
- docs/03_CURRENT_STATE.md
- docs/04_NEXT_TASK.md
- docs/05_ACCEPTANCE_CHECKS.md
- docs/07_HANDOFF.md
- docs/09_FILE_INDEX.md

The first implementation task must be small, testable, and safe.

Do not generate a large architecture before the problem is understood.
```

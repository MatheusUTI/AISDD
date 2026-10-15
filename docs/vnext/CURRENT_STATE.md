# AISDD vNext — Current State

> Last updated: **2026-10-15**  
> Track status: **ACTIVE — learning-first**  
> Current phase: **Phase 0 — Understand the current AISDD**

This is the **living checkpoint** for the AISDD vNext learning and research track.

A future AI must read this file before proposing the next lesson or implementation step.

---

# 1. Why this track exists

A key gap was identified during AISDD development:

Matheus can identify real problems, define desired behavior, evaluate solutions, reject bad approaches, and guide AI-assisted implementation, but does not yet feel able to independently explain the internal mechanisms, architecture, limits, and technical consequences of what is being built.

The purpose of this track is to close that gap deliberately.

The objective is **not** to transform Matheus into a traditional programmer as the primary goal.

The objective is to develop enough systems and architecture literacy to:

- understand what is being built;
- explain how it works;
- follow data and state through the system;
- understand architectural boundaries;
- evaluate trade-offs;
- predict failure modes;
- reason about scalability;
- challenge AI-generated designs;
- make increasingly independent technical decisions;
- use AI as an implementation partner without outsourcing all technical understanding.

---

# 2. Current conceptual insight

AISDD originally emerged from a practical problem:

```text
AI conversations are temporary and context-bounded.
Software projects are long-lived and accumulate state.
```

When project knowledge remains primarily in chat, future agents can lose:

- decisions;
- architecture;
- progress;
- constraints;
- rationale;
- known issues;
- previous failures;
- the next intended action.

AISDD’s central current strategy is to **externalize project memory into versioned repository artifacts**.

The current high-level idea can be summarized as:

> The conversation is temporary. The repository is the source of truth.

However, this sentence is not yet considered “mastered” by Matheus. The next work must unpack exactly how the current AISDD implements this idea.

---

# 3. Current AISDD model — preliminary

The current AISDD roughly follows this flow:

```text
Problem / existing project
        ↓
Project knowledge captured in repository
        ↓
Agent/session bootstrap
        ↓
One active task
        ↓
Constrained implementation
        ↓
Validation
        ↓
State / decisions / issues updated
        ↓
Handoff
        ↓
Next session continues
```

Important: this diagram is a preliminary model to study, not the end of Phase 0.

The task is to understand why every transition and artifact exists.

---

# 4. Important distinction already identified

A major learning target is distinguishing:

```text
WHAT the system does
vs
HOW the system produces that behavior
```

Example:

```text
WHAT:
AISDD provides continuity between AI sessions.

HOW — to be studied:
Which state is persisted?
Where is it persisted?
How does a new agent find it?
Which files are loaded?
In what order?
How is the active task selected?
How is completion validated?
How does the new state replace or extend the old state?
What happens if documents and code disagree?
```

The track must keep pushing from WHAT toward HOW and WHY.

---

# 5. Learning method agreed

For each mechanism:

```text
AI explains
↓
Matheus inspects the real artifact/system
↓
Matheus explains it back without relying on the README
↓
AI challenges the explanation
↓
misunderstandings are corrected
↓
understanding is recorded here
```

The AI should not merely deliver lectures.

The AI should actively ask architectural questions once enough context has been taught.

Examples:

- Why does this component exist?
- What breaks if we remove it?
- Who owns this state?
- What is the source of truth here?
- What if two sources disagree?
- How do we know this worked?
- What alternative design exists?
- What trade-off did we accept?
- Where would this stop scaling?

---

# 6. Current development direction

There are two related but separate objectives:

## Primary objective

**Learn and deeply understand AISDD and the underlying systems/architecture concepts.**

## Secondary objective

Use that understanding to research and design **AISDD vNext**.

The secondary objective must not outrun the primary objective.

---

# 7. REA status

REA is an important inspiration, but REA study is **not the current lesson**.

REA demonstrated potentially valuable ideas around:

- investigation;
- evidence;
- provenance;
- explicit limitations;
- observed vs inferred conclusions;
- unknowns;
- snapshots;
- retained/reusable analysis;
- validation.

A key vNext insight already identified is:

> Current AISDD often tells an agent where project truth is stored. A possible vNext direction is to also make important claims explain why they are considered true, where they came from, whether they remain valid, and what limitations apply.

Another hypothesis is:

> An agent should ideally load only the portion of project truth required for the current task instead of repeatedly loading the entire relevant documentation set.

These are **research hypotheses**, not adopted framework rules.

Do not start implementing them yet.

---

# 8. Candidate vNext concepts parked for later

The following ideas must remain parked until Phase 0 and the necessary systems foundations are complete:

- richer evidence states (`OBSERVED`, `VERIFIED`, `DERIVED`, `ASSUMED`, `UNKNOWN`);
- provenance;
- Investigation Before MISSING INFO;
- task Context Packs;
- Context Compiler;
- source/evidence hashes;
- validity and stale detection;
- Acceptance Proof;
- evidence/context reuse;
- investigation providers;
- REA as an optional provider;
- possible CLI/tooling.

Do not treat this list as a committed roadmap of features.

Each concept must later earn adoption through:

```text
understanding
→ problem definition
→ comparison
→ experiment
→ measurement
→ decision
```

---

# 9. FreteOps relationship

FreteOps is expected to be an early dogfooding environment for vNext ideas.

However, immediate FreteOps product priorities may proceed independently — including getting a useful build into Google Play Console.

The learning/vNext track must not unnecessarily block real product progress.

A likely future experiment is the SSW 101/API integration because it naturally includes:

- incomplete knowledge;
- architecture boundaries;
- investigation;
- external system behavior;
- API contracts;
- evidence;
- unknowns;
- testing and validation.

But this experiment starts only when the learning track reaches the appropriate phase.

---

# 10. Current lesson

## Lesson 0.1 — Why AISDD exists

This is the **next teaching session**.

Do not start with REA.
Do not start with Evidence Model.
Do not start writing vNext code.

Start from first principles.

### Learning objective

Matheus should understand the fundamental problem AISDD solves at the systems level.

### Questions to answer

1. What is “context” for an AI agent?
2. What is project state?
3. What is transient state?
4. What is persistent state?
5. Why is chat history insufficient as the source of truth for a long-lived software project?
6. What exactly is lost between sessions?
7. Why does placing knowledge in a repository improve continuity?
8. What new problems does repository-based project memory introduce?
9. What does “source of truth” actually mean?
10. Does the repository automatically become true simply because something was written there?

### Important final question

At the end of the lesson, Matheus should be able to explain in his own words:

> Why did AISDD need to exist?

Not as marketing copy — as a systems problem.

---

# 11. Next lessons after 0.1

Do not skip ahead, but current planned order is:

```text
0.1 Why AISDD exists
↓
0.2 Transient state, persistent state, and source of truth
↓
0.3 START_HERE as bootstrap protocol
↓
0.4 NEXT_TASK as execution control / task state
↓
0.5 HANDOFF and CURRENT_STATE as continuity mechanisms
↓
0.6 FACTS / ASSUMPTIONS / UNKNOWNS / RISKS as information classification
↓
0.7 Acceptance and validation
↓
0.8 Decisions, known issues, and historical knowledge
↓
0.9 FILE_INDEX and architecture navigation
↓
0.10 Reconstruct the whole AISDD workflow
↓
0.11 Failure modes and conflicting sources
↓
0.12 Scalability and current limits
```

This sequence can be adjusted if learning reveals a better dependency order, but any change should be recorded here.

---

# 12. Current mastery status

Use these states:

- `NOT STARTED`
- `LEARNING`
- `CAN EXPLAIN WITH HELP`
- `CAN EXPLAIN INDEPENDENTLY`
- `CAN CHALLENGE / DESIGN ALTERNATIVES`

| Topic | Status |
|---|---|
| Why AISDD exists | LEARNING |
| Transient vs persistent state | NOT STARTED |
| Source of truth | NOT STARTED |
| START_HERE / bootstrap | NOT STARTED |
| NEXT_TASK / execution control | NOT STARTED |
| HANDOFF / continuity | NOT STARTED |
| Information classification | NOT STARTED |
| Acceptance / validation | NOT STARTED |
| Decisions / history | NOT STARTED |
| FILE_INDEX / navigation | NOT STARTED |
| Full AISDD workflow | NOT STARTED |
| Failure modes | NOT STARTED |
| Scalability limits | NOT STARTED |
| Systems architecture fundamentals | NOT STARTED |
| REA architecture and evidence model | BLOCKED BY PREREQUISITES |
| AISDD vNext design | BLOCKED BY PREREQUISITES |

---

# 13. Decisions already made for this track

### D-VNEXT-001 — Learning is the primary objective

AISDD vNext development is secondary to Matheus understanding the system being evolved.

### D-VNEXT-002 — Current AISDD remains stable

vNext research must not immediately rewrite or replace the current framework.

### D-VNEXT-003 — REA is inspiration/provider candidate, not foundation

REA concepts will be evaluated individually using ADOPT / ADAPT / REJECT.

### D-VNEXT-004 — Dogfooding before framework promotion

New concepts should be tested in real work before becoming official framework rules.

### D-VNEXT-005 — No premature tooling

Do not begin by building a CLI, MCP, engine, database, or large automation layer.

Manual experiment first. Automation after repetition and evidence.

### D-VNEXT-006 — Repository owns continuity

This `docs/vnext/` track exists so progress survives chat/model/session context loss.

---

# 14. Open questions — intentionally unresolved

- What is the precise architectural model of current AISDD?
- Which documents represent state versus rules versus history?
- How should conflicting repository information be resolved?
- How much context does the current bootstrap really require?
- Where does current AISDD first stop scaling?
- Which current claims are merely documented versus actually verified?
- Which REA concepts solve genuine AISDD pain rather than adding sophistication?
- What minimum evidence model would produce value without bureaucracy?
- Can task-scoped context reduce token use without hiding critical constraints?
- How should stale knowledge be detected?

These are future investigation questions, not current action items.

---

# 15. Immediate next action

**Teach Lesson 0.1 — Why AISDD exists.**

Requirements for that session:

- start from first principles;
- use concrete examples from AI-assisted project work;
- introduce systems vocabulary gradually;
- avoid jumping to REA/vNext solutions;
- ask Matheus to explain the concept back in his own words;
- challenge the explanation until the distinction between temporary conversation context and durable project state is clear;
- update this file after meaningful mastery progress.

---

# 16. Resume instruction

If context is lost, do not reconstruct the plan from memory.

Read:

```text
docs/vnext/START_HERE.md
docs/vnext/CURRENT_STATE.md
docs/vnext/LEARNING_ROADMAP.md
```

Then continue from **Immediate next action**.

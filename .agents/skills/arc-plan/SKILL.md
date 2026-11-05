---
name: arc-plan
description: Create an atomic, contract-aware, verifiable implementation plan for an ARC roadmap phase or feature.
---

# Plan a phase

1. Read `.arc/PROJECT.md`, `.arc/ROADMAP.md`, `.arc/STATE.md`, `.arc/CONTRACTS.md`; also read phase CONTEXT and CODEBASE map when present.
2. Confirm the phase goal and current state. Identify missing information; ask focused questions only when necessary.
3. Inspect relevant source code and tests to validate assumptions and file paths.
4. Break work into small tasks with one clear outcome each. Specify owner (main agent or proposed subagent), exact files, dependencies, implementation notes, risks, and verification commands.
5. Include contract changes, migration needs, observability, security considerations, and rollback strategy where applicable.
6. Avoid mandatory delegation. Mark independent tasks as parallelizable only when file ownership and dependencies allow it.
7. Save to `.arc/planning/phase-[N]-PLAN.md` using the available template.
8. Present scope, decisions, task order, risks, and verification. Wait for user approval before executing.

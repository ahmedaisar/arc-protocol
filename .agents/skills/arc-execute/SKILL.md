---
name: arc-execute
description: Execute an approved ARC plan in atomic steps with controlled delegation, contract updates, tests, and durable progress tracking.
---

# Execute an approved plan

## Preconditions
- Read the approved `.arc/planning/phase-[N]-PLAN.md`.
- Re-read PROJECT, STATE, CONTRACTS, and relevant CODEBASE/CONTEXT files.
- Confirm the plan is approved and the working tree state is understood.

## Execution
1. Execute tasks in dependency order; parallelize only independent tasks with non-overlapping write ownership.
2. Use host-native subagents when available. Give each a bounded task, exact paths, required context, expected output, and verification criteria. Otherwise work sequentially.
3. Do not claim a task is complete until its changes are inspected and verification is run.
4. Update `.arc/CONTRACTS.md` when public interfaces, schemas, environment variables, or cross-module contracts change.
5. Run the narrowest relevant tests after each task, then broader checks at integration points.
6. Preserve user changes. Never overwrite unrelated work or run destructive commands without explicit approval.
7. Update `.arc/STATE.md` after meaningful milestones with completed work, outstanding tasks, decisions, and next action.
8. Commit only when requested or when the repository workflow explicitly authorizes commits; use small, descriptive commits.

## Completion
- Summarize files changed and behavior changes.
- Report exact verification commands and pass/fail outcomes.
- List known limitations and unfinished work.
- Create `.arc/planning/phase-[N]-SUMMARY.md` from the template when available.
- Update ROADMAP only for outcomes actually completed and verified.

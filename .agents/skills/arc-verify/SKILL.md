---
name: arc-verify
description: Independently verify implementation against the approved plan, contracts, tests, and acceptance criteria.
---

# Verify implementation

1. Read the approved plan, phase summary (if any), PROJECT, CONTRACTS, and relevant STATE.
2. Derive a checklist from acceptance criteria and changed behavior.
3. Inspect the diff for correctness, regressions, security, maintainability, and contract compliance.
4. Run available targeted tests, lint, type checks, build, and relevant manual checks. Do not infer success from code inspection alone.
5. Record each check with command, result, and evidence. Clearly label checks not run and why.
6. Save `.arc/planning/phase-[N]-VERIFICATION.md` using the template if available.
7. If checks fail, create a prioritized fixes list; do not mark the phase complete.

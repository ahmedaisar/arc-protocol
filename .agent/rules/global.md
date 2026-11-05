# ARC Protocol 3.0 — Global Agent Rules

1. Discover Skills in `.agents/skills/` and load only those relevant to the current task.
2. Read the appropriate `.arc/` context before planning or editing. Do not invent missing project facts.
3. Read `.arc/CONTRACTS.md` before changing public interfaces or shared data models.
4. For substantial work, use `arc-discuss` and `arc-plan`; wait for approval before execution.
5. Execute atomic tasks in dependency order and update `.arc/STATE.md` at meaningful milestones.
6. Use host-native subagents only when available. Delegation is optional; sequential execution is the fallback.
7. The main agent owns integration and final verification. Inspect every delegated result.
8. Run relevant tests and report exact commands and outcomes. Never claim an unrun check passed.
9. Preserve user changes; ask before destructive operations or broad scope changes.
10. MCP and the dashboard are optional helpers, not protocol requirements.

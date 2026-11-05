---
name: arc-multi-agent
description: Coordinate parallel work using host-native subagents with clear task boundaries and integration checks.
---

# Multi-agent coordination

1. Read the approved plan and identify tasks that are genuinely independent.
2. Delegate only when the host exposes native subagents and the expected benefit outweighs coordination overhead.
3. Give every worker a unique task, explicit scope, write ownership, context references, deliverables, and acceptance criteria.
4. Do not assign concurrent writes to the same files unless the host provides safe isolation.
5. Keep the number of active workers within the host's practical limits and the user's preferences. There is no fixed delegation quota.
6. Continue strategic work while delegated tasks run, but do not report completion until all required outputs are returned.
7. Review each result against contracts and tests, resolve conflicts, and run integration verification.
8. If native delegation is unavailable, execute tasks sequentially. Never claim that a task ran in the background when it did not.

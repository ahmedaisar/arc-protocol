---
name: arc
description: Use ARC Protocol to maintain project context, contracts, plans, execution discipline, and verification across AI coding sessions.
---

# ARC Protocol

ARC is a host-agnostic engineering workflow. The host AI agent is the reasoning and execution runtime; ARC supplies reusable workflow instructions, persistent project artifacts, deterministic tools, and verification gates.

## Non-negotiable principles
- Read project context before planning or changing code.
- Treat `.arc/CONTRACTS.md` as the source of truth for interfaces and conventions.
- Keep plans atomic, scoped, and verifiable.
- Never claim tests passed unless they were run and observed.
- Ask for approval before destructive actions, broad scope changes, or executing a plan that has not been approved.
- Use host-native subagents when available. If unavailable, perform work sequentially; never assume a particular model, CLI, or provider.
- Load only relevant Skills and reference files (progressive disclosure).

## Project context
Read only the files relevant to the task, normally:
1. `.arc/PROJECT.md`
2. `.arc/STATE.md` (or `.arc/state/STATE.md` if that is the project convention)
3. `.arc/ROADMAP.md` for roadmap work
4. `.arc/CONTRACTS.md` before implementation
5. `.arc/CODEBASE.md` for existing-codebase work

If a file is absent, report that and continue with available evidence. Do not invent its contents.

## Workflow selection
- Initialize a project: `arc-new`
- Understand an existing repository: `arc-map`
- Discuss requirements: `arc-discuss`
- Plan a phase: `arc-plan`
- Implement an approved plan: `arc-execute`
- Verify changes: `arc-verify`
- Inspect progress: `arc-status`
- Resume a paused effort: `arc-resume`
- Small bounded change: `arc-quick`

Read the corresponding Skill before following a workflow.

## Deterministic tools
Use scripts under `.agent/tools/` for repeatable validation, structure checks, topology mapping, changelog generation, and metrics. Python scripts are optional helpers; the Skills remain usable without MCP or a dashboard.

## Delegation contract
When the host supports delegation, assign bounded tasks with explicit paths, deliverables, constraints, and verification steps. Keep shared-file ownership clear. The main agent integrates and verifies all returned work. When delegation is unavailable, do not simulate background execution; complete the tasks in the current session.

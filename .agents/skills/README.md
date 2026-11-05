# ARC Skills Catalog

Canonical portable Agent Skills for ARC Protocol v3.0 live in this directory. Each Skill is a directory containing a `SKILL.md` with YAML frontmatter (`name`, `description`) and actionable instructions.

## Core protocol
- `arc` — protocol principles, context loading, and workflow selection.

## Workflow Skills
- `arc-new` — initialize a project.
- `arc-map` — analyze an existing codebase.
- `arc-discuss` — clarify requirements and record decisions.
- `arc-add-phase` — extend the roadmap.
- `arc-plan` — create an atomic implementation plan.
- `arc-execute` — execute an approved plan.
- `arc-multi-agent` — coordinate host-native subagents safely.
- `arc-verify` — independently verify changes.
- `arc-status` — report progress and blockers.
- `arc-resume` — resume an interrupted project.
- `arc-pause` — record durable progress before stopping.
- `arc-quick` — perform a small, bounded change.
- `arc-health` — diagnose ARC project and tooling health.
- `arc-help` — explain ARC workflows and setup.

## Specialist Skills
- `arc-architect`, `arc-coder`, `arc-researcher`, `arc-auditor`, `arc-debugger`.

## Engineering domain Skills
- `async-concurrency`
- `bundle-optimization`
- `js-efficiency`
- `performance`
- `rendering-rsc`
- `security-guardian`

## Use

Configure the host agent to discover Skills from `.agents/skills/`. If the client uses another directory, follow its documented Skills discovery mechanism and create a symlink or copy from this canonical source. Do not maintain independent edited copies.

ARC does not install or authenticate an AI provider. Native delegation is used only when the host supports it; sequential execution is the fallback.

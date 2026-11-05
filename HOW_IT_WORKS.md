# How ARC Protocol 3.0 Works

ARC addresses context loss and inconsistent engineering practices in AI-assisted development by making project context, decisions, interfaces, plans, and verification durable.

## Architecture

ARC separates the **protocol** from the **execution runtime**.

- **Host AI agent:** understands the request, reads Skills, edits files, runs commands, and may delegate work using its native capabilities.
- **Agent Skills:** portable instructions that define ARC workflows and specialist roles.
- **Project context:** durable Markdown artifacts under `.arc/`.
- **Deterministic tools:** Python scripts for repeatable checks and project analysis.
- **Optional integrations:** dashboard and MCP tools. Neither is required for Skills to work.

There is no provider-specific model invocation in ARC core. ARC does not manage model credentials, choose models, or launch a vendor CLI.

## Workflow Skills

Skills are discovered by the host and invoked as workflows:

| Skill | Responsibility |
|---|---|
| `arc-new` | Initialize project vision and roadmap |
| `arc-map` | Map a brownfield codebase |
| `arc-discuss` | Capture requirements and decisions |
| `arc-plan` | Design atomic implementation tasks |
| `arc-execute` | Execute an approved plan |
| `arc-verify` | Audit behavior and test evidence |
| `arc-status` | Report progress and blockers |
| `arc-resume` | Continue from durable state |
| `arc-quick` | Handle small bounded changes |

Role Skills provide focused behavior: architect, coder, researcher, auditor, and debugger.

## Persistent context

| Artifact | Purpose |
|---|---|
| `.arc/PROJECT.md` | Product vision, goals, constraints |
| `.arc/CONTRACTS.md` | Interfaces, schemas, conventions, invariants |
| `.arc/ROADMAP.md` | Phases and outcomes |
| `.arc/STATE.md` | Current progress and next action |
| `.arc/CODEBASE.md` | Existing architecture and code conventions |
| `.arc/planning/` | Phase contexts, plans, summaries, verification |

The agent must report missing files instead of pretending they exist. Existing project files are not overwritten during setup.

## Execution and delegation

The main agent reads and approves the plan before execution. Independent tasks may be delegated through host-native subagents, provided file ownership and dependencies are explicit. If the host does not support delegation, work proceeds sequentially. ARC never claims background parallelism where none exists.

Every task must have a clear deliverable and verification method. The main agent inspects integrated output, updates contracts when public interfaces change, and records progress in STATE.

## Verification

Verification is separate from implementation. The verifier inspects the actual diff, checks acceptance criteria and contracts, and runs relevant tests, lint, type checks, or builds. Results must state exact commands and distinguish passed, failed, and not-run checks.

## Deterministic tools

The `.agent/tools/` directory contains scripts for topology mapping, contract checks, structure validation, changelog generation, and metrics. These can be invoked directly from the terminal or exposed through optional MCP integration.

## Getting started

1. Run `python3 setup_arc.py`.
2. Configure your AI host to discover Skills in `.agents/skills/`.
3. Use `arc-new` for a new project or `arc-map` for an existing codebase.
4. Discuss and plan substantial work, approve the plan, execute, then verify.
5. Use `arc-status` or `arc-resume` across sessions.

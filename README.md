# ARC Protocol v3.0

**AI Skills-native. Model-agnostic. Verification-first.**

ARC is a portable engineering workflow for AI-assisted software development. It keeps AI work grounded in persistent project context, explicit contracts, atomic plans, deterministic tools, and evidence-based verification—without requiring a particular model, provider, CLI, or background-agent runtime.

![ARC Dashboard](assets/Dashboard.png)

## What ARC provides

- **Agent Skills** — reusable workflow and role instructions under `.agents/skills/`.
- **Persistent project context** — `.arc/PROJECT.md`, `CONTRACTS.md`, `ROADMAP.md`, `STATE.md`, and planning artifacts.
- **Deterministic tools** — topology mapping, contract checks, structure validation, changelog generation, and metrics.
- **Optional dashboard** — visibility into project progress.
- **Optional MCP bridge** — deterministic local tools for hosts that prefer MCP. MCP is not an AI runtime.

The host AI coding agent supplies reasoning and execution. When it supports native subagents, ARC Skills may delegate bounded tasks to them. Otherwise the same workflow runs sequentially.

## Quick start

Requirements: Python 3.10+. No Node.js, Gemini CLI, model API key, or provider login is required by ARC core.

```bash
python3 setup_arc.py
```

Then configure your coding agent to discover Skills from `.agents/skills/` (or its documented client-specific Skills directory).

For a new project, invoke the **arc-new** Skill. For an existing repository, start with **arc-map**. Then use:

1. **arc-discuss** — capture decisions and constraints.
2. **arc-plan** — create an atomic plan with verification criteria.
3. Review and approve the plan.
4. **arc-execute** — implement in dependency order, using native delegation when available.
5. **arc-verify** — independently inspect changes and run checks.
6. **arc-status** / **arc-resume** — track or resume work across sessions.

## Skills catalog

Canonical portable Skills live in `.agents/skills/`.

| Category | Skills |
|---|---|
| Core | `arc` |
| Workflows | `arc-new`, `arc-map`, `arc-discuss`, `arc-plan`, `arc-execute`, `arc-verify`, `arc-status`, `arc-resume`, `arc-quick` |
| Roles | `arc-architect`, `arc-coder`, `arc-researcher`, `arc-auditor`, `arc-debugger` |

Each Skill is a directory containing `SKILL.md` with YAML frontmatter. See [the catalog](.agents/skills/README.md).

## Architecture

```text
AI coding host (any compatible agent)
       |
       v
.agents/skills/       Workflow + role Skills
       |
       +--------------> .arc/ project context and state
       |
       +--------------> .agent/tools/ deterministic utilities
       |
       +--------------> optional dashboard / optional MCP tools
       |
       v
Host-native execution and delegation (or sequential fallback)
       |
       v
Implementation + tests + recorded verification
```

ARC describes engineering behavior and guardrails; the host determines which model and runtime execute them. ARC does not spawn provider-specific background processes.

## Optional dashboard and tools

```bash
./dash
```

Run individual tools with the Python environment created by setup, for example:

```bash
./venv/bin/python .agent/tools/map_topology.py
./venv/bin/python .agent/tools/validate_structure.py
./venv/bin/python .agent/tools/contract_check.py
```

On Windows, use `venv\\Scripts\\python.exe` and `dash.bat`.

## Migration from v2.x

See [Migration Guide](docs/MIGRATION_V3.md). Existing `.arc/` project artifacts are preserved. Gemini authentication and model-specific worker execution are removed. The legacy workflow and role-prompt paths remain as migration pointers during v3.0.

## Integrations

See [Integrations Guide](docs/INTEGRATIONS.md) for Skills discovery and optional MCP configuration. Client discovery paths vary by product and version; ARC keeps one canonical Skills source and does not assume every client automatically discovers it.

## Design principles

1. **Context before code:** inspect project facts and contracts first.
2. **Plans before substantial execution:** define atomic tasks and acceptance criteria.
3. **Delegation is optional:** use host-native capabilities only when available and safe.
4. **Verification is evidence:** report exact commands and results.
5. **Provider independence:** no model or vendor is required by ARC core.

Open source under the MIT License.

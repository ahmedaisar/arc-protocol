# ARC Protocol v3.0.0 — Skills-First Release

ARC v3 separates its engineering protocol from the AI runtime.

## Highlights

- Introduces a canonical Agent Skills catalog under `.agents/skills/`.
- Converts core workflows and specialist roles into portable Skills.
- Removes Gemini CLI authentication, model selection, and Google generative AI dependency from setup.
- Removes AI-worker spawning from the MCP bridge.
- Keeps MCP as an optional deterministic-tools integration.
- Preserves project context, planning templates, Python utilities, and the dashboard.
- Supports native host-agent delegation when available and sequential fallback otherwise.
- Adds a Skill catalog validator and unit tests.

## Migration

See [docs/MIGRATION_V3.md](docs/MIGRATION_V3.md). Existing `.arc/` state and legacy workflow paths are retained.

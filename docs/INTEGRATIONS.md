# ARC Protocol 3.0 Integrations

ARC Skills are the primary integration surface. MCP is optional and provides deterministic tools only; it does not launch AI agents.

## Skills discovery

The canonical Skills directory is:

```text
.agents/skills/<skill-name>/SKILL.md
```

Each Skill uses YAML frontmatter with a `name` and `description`. Configure your AI coding host to discover this directory using the host's documented Skills mechanism.

Some tools automatically discover repository Skills; others use a client-specific path or setting. When a host requires a different directory, create a symlink or copy from `.agents/skills/`. Avoid editing duplicate copies independently.

Useful workflow Skills: `arc-new`, `arc-map`, `arc-discuss`, `arc-plan`, `arc-execute`, `arc-verify`, `arc-status`, `arc-resume`, and `arc-quick`.

## Optional MCP bridge

Use MCP only when your host benefits from structured tools for local file operations, shell execution, or dashboard updates.

Example stdio configuration (replace the absolute path):

```json
{
  "mcpServers": {
    "arc-tools": {
      "command": "python3",
      "args": ["/absolute/path/to/arc-protocol/.agent/mcp/arc_mcp_server.py"]
    }
  }
}
```

The bridge exposes deterministic utilities. It does not include `arc_spawn_agent` or model selection. Follow your host's documentation for the MCP configuration location and permission model.

## Dashboard

Run `./dash` (Windows: `dash.bat`) in a separate terminal. The dashboard is optional and does not control the AI host.

## Provider independence

ARC does not require Gemini, OpenAI, Anthropic, an API key, Node.js, or any model CLI. The host agent uses its own configured runtime and permissions.

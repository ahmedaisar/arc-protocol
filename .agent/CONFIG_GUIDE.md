# ARC Protocol 3.0 Configuration

## 1. Skills (primary integration)

Canonical Skills live under `.agents/skills/<name>/SKILL.md`. Configure your AI coding host to discover that directory. Some hosts require a client-specific directory; follow the host's current documentation and use a symlink or copy from the canonical source when necessary.

## 2. Optional MCP tools

The MCP server exposes deterministic local utilities. It does not spawn AI agents or select models.

Example:

```json
{
  "mcpServers": {
    "arc-tools": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/PROJECT/.agent/mcp/arc_mcp_server.py"]
    }
  }
}
```

Use absolute paths and review the tools your host grants access to. Shell execution should be disabled unless explicitly needed and permitted.

## 3. Dashboard

Run `./dash` (or `dash.bat` on Windows). The dashboard is optional.

## 4. Runtime

ARC core requires Python 3.10+. There is no Gemini CLI, Node.js, API key, model setting, or provider authentication step.

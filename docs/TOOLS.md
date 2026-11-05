# ARC Protocol 3.0 Tools

ARC's Python utilities are deterministic helpers. They do not call an AI model or launch an agent runtime.

| Tool | Purpose |
|---|---|
| `contract_check.py` | Check code against project contracts |
| `map_topology.py` | Map repository structure and relationships |
| `validate_structure.py` | Check required ARC directories and files |
| `validate_skills.py` | Validate canonical Skill names and required metadata |
| `generate_changelog.py` | Summarize Git changes |
| `velocity.py` | Calculate project progress metrics |
| `link_mcp.py` | Generate optional MCP client configuration |

Run tools with the ARC virtual environment, for example:

```bash
./venv/bin/python .agent/tools/validate_skills.py
./venv/bin/python .agent/tools/map_topology.py
./venv/bin/python .agent/tools/contract_check.py
```

Windows: use `venv\\Scripts\\python.exe`.

## Optional MCP bridge

`.agent/mcp/arc_mcp_server.py` exposes read, write, list, and dashboard-state helpers. It intentionally has no AI worker, model-selection, or command-execution capability. Use your host agent's terminal permissions for commands and its native subagent API for delegation.

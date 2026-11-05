# ARC Protocol 3.0 Setup Guide

Supports Linux, macOS, and Windows (including WSL).

## Requirements

- Python 3.10 or newer.
- An AI coding host that supports Agent Skills or can read Markdown instructions.

ARC core does not require Node.js, Gemini CLI, Google authentication, model API keys, or a provider SDK.

## Install

From the repository root:

```bash
python3 setup_arc.py
```

The setup script creates a Python virtual environment, installs local utility dependencies, scaffolds missing ARC runtime directories, and creates the dashboard launcher. Existing project context is preserved.

## Connect your AI host

Configure the host to discover Skills from `.agents/skills/`. If it expects a different path, use its documented Skills directory and link or copy the canonical Skills there.

Start with:

- `arc-new` for a new project.
- `arc-map` for an existing codebase.
- `arc-resume` for a project with existing ARC state.

## Optional dashboard

```bash
./dash
```

On Windows, run `dash.bat`.

## Optional MCP tools

See [Integrations](INTEGRATIONS.md). MCP is not needed to load Skills or use the protocol.

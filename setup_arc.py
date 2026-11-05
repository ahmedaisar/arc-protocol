#!/usr/bin/env python3
"""Install ARC Protocol's local tools without configuring an AI provider."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def print_banner() -> None:
    print("""
    █████╗ ██████╗  ██████╗
   ██╔══██╗██╔══██╗██╔════╝
   ███████║██████╔╝██║
   ██╔══██║██╔══██╗██║
   ██║  ██║██║  ██║╚██████╗
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
   ARC PROTOCOL v3.0 — SKILLS FIRST
   ANALYZE. RUN. CONFIRM.
""")


def setup_environment() -> Path:
    venv = ROOT / "venv"
    if not venv.exists():
        subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)
    python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    pip = venv / ("Scripts/pip.exe" if os.name == "nt" else "bin/pip")
    requirements = ROOT / "requirements.txt"
    if requirements.exists():
        subprocess.run([str(pip), "install", "-r", str(requirements)], check=True)
    return python


def scaffold_arc() -> None:
    for directory in (
        ".arc/archive",
        ".arc/planning",
        ".arc/state",
        ".agents/skills",
        ".agent/tools",
    ):
        (ROOT / directory).mkdir(parents=True, exist_ok=True)

    state_file = ROOT / ".arc/arc_workflow_state.json"
    if not state_file.exists():
        state_file.write_text(
            json.dumps(
                {
                    "project": "New ARC Project",
                    "phase": "Initialize",
                    "agents": {},
                    "logs": [],
                    "metrics": {"tasks_total": 0, "tasks_completed": 0},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )


def create_dashboard_launcher(python: Path) -> None:
    monitor = ROOT / ".agent/dashboard/monitor.py"
    if os.name == "nt":
        launcher = ROOT / "dash.bat"
        launcher.write_text(f'@"{python}" "{monitor}" %*\n', encoding="utf-8")
    else:
        launcher = ROOT / "dash"
        launcher.write_text(
            '#!/bin/sh\n'
            'ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"\n'
            'PY="$ROOT/venv/bin/python"\n'
            '[ -x "$PY" ] || { echo "ARC virtualenv not found; run setup_arc.py"; exit 1; }\n'
            'exec "$PY" "$ROOT/.agent/dashboard/monitor.py" "$@"\n',
            encoding="utf-8",
        )
        launcher.chmod(0o700)


def main() -> int:
    print_banner()
    if sys.version_info < (3, 10):
        print("ARC requires Python 3.10 or newer.", file=sys.stderr)
        return 1

    python = setup_environment()
    scaffold_arc()
    create_dashboard_launcher(python)

    validator = ROOT / ".agent/tools/validate_skills.py"
    if validator.is_file():
        subprocess.run([str(python), str(validator)], cwd=ROOT, check=True)

    print("\nARC Protocol 3.0 is ready.")
    print("No model CLI, API key, or provider login is required.")
    print("\nNext steps:")
    print("1. Ensure your AI coding agent discovers Skills from .agents/skills/.")
    print("2. Start an existing project with the arc-map Skill.")
    print("3. Initialize a new project with the arc-new Skill.")
    print("4. Optional dashboard: ./dash (Windows: dash.bat)")
    print("5. Optional MCP tools: see docs/INTEGRATIONS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

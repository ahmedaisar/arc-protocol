#!/usr/bin/env python3
"""Optional MCP server for deterministic ARC workspace utilities.

This server deliberately does not launch AI workers, select models, or invoke
provider CLIs. Skills are discovered and executed by the host AI application.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = SCRIPT_DIR.parents[1]


class MCPServer:
    def __init__(self) -> None:
        self.tools = [
            {
                "name": "arc_read_file",
                "description": "Read a UTF-8 file inside the ARC workspace.",
                "inputSchema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"],
                },
            },
            {
                "name": "arc_write_file",
                "description": "Write a UTF-8 file inside the ARC workspace.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                    },
                    "required": ["path", "content"],
                },
            },
            {
                "name": "arc_list_dir",
                "description": "List entries in a directory inside the ARC workspace.",
                "inputSchema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"],
                },
            },
            {
                "name": "arc_update_dashboard",
                "description": "Update a worker/status entry in ARC dashboard state.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "agent": {"type": "string"},
                        "status": {"type": "string"},
                        "task": {"type": "string"},
                    },
                },
            },
        ]

    def workspace_path(self, relative_path: str) -> Path:
        if not isinstance(relative_path, str) or not relative_path:
            raise ValueError("path must be a non-empty string")
        candidate = (WORKSPACE / relative_path).resolve()
        try:
            candidate.relative_to(WORKSPACE)
        except ValueError as exc:
            raise ValueError("path must stay inside the ARC workspace") from exc
        return candidate

    @staticmethod
    def text_result(value: str) -> dict[str, Any]:
        return {"content": [{"type": "text", "text": value}]}

    def call_tool(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        if name == "arc_read_file":
            path = self.workspace_path(args["path"])
            if not path.is_file():
                raise FileNotFoundError(args["path"])
            return self.text_result(path.read_text(encoding="utf-8"))

        if name == "arc_write_file":
            path = self.workspace_path(args["path"])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(args["content"], encoding="utf-8")
            return self.text_result(f"Written to {args['path']}")

        if name == "arc_list_dir":
            path = self.workspace_path(args["path"])
            if not path.is_dir():
                raise NotADirectoryError(args["path"])
            return self.text_result("\n".join(sorted(item.name for item in path.iterdir())))

        if name == "arc_update_dashboard":
            state_path = self.workspace_path(".arc/arc_workflow_state.json")
            state_path.parent.mkdir(parents=True, exist_ok=True)
            if state_path.exists():
                state = json.loads(state_path.read_text(encoding="utf-8"))
            else:
                state = {"agents": {}, "logs": []}
            agent = str(args.get("agent") or "Main")
            entry = state.setdefault("agents", {}).setdefault(
                agent, {"status": "IDLE", "task": ""}
            )
            if args.get("status"):
                entry["status"] = str(args["status"])
            if args.get("task"):
                entry["task"] = str(args["task"])
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            return self.text_result("Dashboard updated")

        raise ValueError(f"Unknown tool: {name}")

    def handle(self, message: dict[str, Any]) -> dict[str, Any] | None:
        method = message.get("method")
        params = message.get("params") or {}
        request_id = message.get("id")

        if method == "notifications/initialized":
            return None
        if method == "initialize":
            result = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "arc-tools", "version": "3.0.0"},
            }
        elif method == "tools/list":
            result = {"tools": self.tools}
        elif method == "tools/call":
            try:
                result = self.call_tool(params["name"], params.get("arguments") or {})
                if "content" not in result:
                    result = self.text_result(json.dumps(result))
            except Exception as exc:
                result = {
                    "isError": True,
                    "content": [{"type": "text", "text": str(exc)}],
                }
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32601, "message": f"Unknown method: {method}"},
            } if request_id is not None else None

        return {"jsonrpc": "2.0", "id": request_id, "result": result} if request_id is not None else None

    def run(self) -> None:
        for line in sys.stdin:
            try:
                response = self.handle(json.loads(line))
                if response is not None:
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
            except json.JSONDecodeError:
                continue
            except Exception as exc:  # keep the stdio transport alive
                sys.stdout.write(
                    json.dumps(
                        {
                            "jsonrpc": "2.0",
                            "error": {"code": -32603, "message": str(exc)},
                        }
                    )
                    + "\n"
                )
                sys.stdout.flush()


if __name__ == "__main__":
    MCPServer().run()

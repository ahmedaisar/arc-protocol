"""Tests for ARC's optional, deterministic-only MCP bridge."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SERVER_PATH = Path(__file__).resolve().parents[1] / ".agent/mcp/arc_mcp_server.py"
SPEC = importlib.util.spec_from_file_location("arc_mcp_server", SERVER_PATH)
assert SPEC and SPEC.loader
SERVER_MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SERVER_MODULE)


class MCPServerTests(unittest.TestCase):
    def setUp(self):
        self.server = SERVER_MODULE.MCPServer()

    def test_no_model_or_worker_tools_are_exposed(self):
        names = {tool["name"] for tool in self.server.tools}
        self.assertNotIn("arc_spawn_agent", names)
        self.assertNotIn("arc_dispatch_worker", names)
        self.assertNotIn("arc_exec", names)

    def test_workspace_path_rejects_parent_traversal(self):
        with self.assertRaises(ValueError):
            self.server.workspace_path("../outside.txt")

    def test_workspace_path_rejects_absolute_outside_path(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.server.workspace_path(str(Path(directory) / "outside.txt"))

    def test_tools_list_protocol_response(self):
        response = self.server.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
        self.assertEqual(response["id"], 1)
        self.assertIn("tools", response["result"])


if __name__ == "__main__":
    unittest.main()

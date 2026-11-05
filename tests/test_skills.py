"""Unit tests for the ARC Skills catalog validator."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from importlib.util import module_from_spec, spec_from_file_location

TOOL_PATH = Path(__file__).resolve().parents[1] / ".agent/tools/validate_skills.py"
SPEC = spec_from_file_location("validate_skills", TOOL_PATH)
assert SPEC and SPEC.loader
VALIDATOR = module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class SkillValidationTests(unittest.TestCase):
    def test_parse_frontmatter(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "SKILL.md"
            skill.write_text(
                "---\nname: arc-demo\ndescription: A demo skill.\n---\n# Demo\n",
                encoding="utf-8",
            )
            self.assertEqual(
                VALIDATOR.parse_frontmatter(skill),
                {"name": "arc-demo", "description": "A demo skill."},
            )

    def test_rejects_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "SKILL.md"
            skill.write_text("# No metadata\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                VALIDATOR.parse_frontmatter(skill)

    def test_catalog_is_valid(self):
        self.assertEqual(VALIDATOR.validate(), [])


if __name__ == "__main__":
    unittest.main()

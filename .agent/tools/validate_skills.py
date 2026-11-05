#!/usr/bin/env python3
"""Validate ARC Agent Skills directory names and required frontmatter."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2] / ".agents" / "skills"
VALID_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter opener")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing YAML frontmatter closer") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata


def validate() -> list[str]:
    errors: list[str] = []
    if not SKILLS_ROOT.is_dir():
        return [f"Skills directory not found: {SKILLS_ROOT}"]

    seen: set[str] = set()
    for skill_dir in sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        if not VALID_NAME.fullmatch(skill_dir.name):
            errors.append(f"{skill_dir.name}: directory name must be lowercase kebab-case")
        try:
            metadata = parse_frontmatter(skill_file)
        except (OSError, ValueError) as exc:
            errors.append(f"{skill_dir.name}: {exc}")
            continue
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not name:
            errors.append(f"{skill_dir.name}: missing frontmatter name")
        elif name != skill_dir.name:
            errors.append(f"{skill_dir.name}: frontmatter name must match directory name")
        if name in seen:
            errors.append(f"{skill_dir.name}: duplicate Skill name {name}")
        seen.add(name)
        if not description:
            errors.append(f"{skill_dir.name}: missing frontmatter description")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("ARC Skills validation failed:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)
    skill_count = sum(path.is_dir() for path in SKILLS_ROOT.iterdir())
    print(f"ARC Skills validation passed ({skill_count} Skills).")

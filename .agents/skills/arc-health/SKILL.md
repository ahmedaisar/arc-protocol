---
name: arc-health
description: Diagnose the health of ARC project state, Skills, templates, and deterministic tooling.
---

# Check ARC health

1. Inspect expected ARC directories and project artifacts without modifying them.
2. Run `.agent/tools/validate_skills.py` when available.
3. Run `.agent/tools/validate_structure.py` and other relevant deterministic checks when available.
4. Check for stale references to provider-specific CLIs or removed worker tools.
5. Check for missing, contradictory, or stale PROJECT, CONTRACTS, ROADMAP, STATE, and CODEBASE artifacts.
6. Report findings by severity with paths and actionable remediations.
7. Do not automatically rewrite state or delete files during diagnostics.

# Legacy Skills Directory

ARC Protocol v3 uses the standard, canonical Skills catalog at `.agents/skills/`.

This `.agent/skills/` directory remains temporarily for v2 migration compatibility. Role definitions in `definitions/` are pointers to their canonical Skills. Engineering domain Skills have been copied to the canonical catalog; update the canonical copy rather than maintaining divergent versions.

New Skills must be added under `.agents/skills/<kebab-case-name>/SKILL.md` and should pass:

```bash
python .agent/tools/validate_skills.py
```

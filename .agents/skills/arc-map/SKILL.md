---
name: arc-map
description: Analyze an existing codebase and create a concise architecture and conventions map before making changes.
---

# Map an existing codebase

1. Inspect repository metadata, directory structure, package manifests, entry points, tests, and CI configuration.
2. Identify architectural boundaries, key modules, data flows, external dependencies, and generated/vendor directories.
3. Trace important imports and interfaces; avoid reading every file when a structural map is sufficient.
4. Identify established conventions, test commands, lint/type-check commands, and build steps.
5. Create or update `.arc/CODEBASE.md` using `.arc/templates/CODEBASE.md` when available.
6. Clearly distinguish observed facts from inferred architecture and unresolved questions.
7. Do not modify application source code during mapping unless explicitly requested.

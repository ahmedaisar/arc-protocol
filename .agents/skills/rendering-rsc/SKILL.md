---
name: rendering-rsc
description: Design rendering boundaries across React Server Components, SSR, hydration, and client interactivity.
---

# Rendering strategy

- Follow the framework version and existing architecture in the repository.
- Prefer server rendering for data access and static composition when supported.
- Keep client boundaries small and introduce browser APIs only in client components.
- Prevent hydration mismatches by ensuring server and initial client output are deterministic.
- Handle loading, error, streaming, caching, and revalidation states explicitly.
- Verify with the project's build and tests rather than assuming a rendering optimization is safe.

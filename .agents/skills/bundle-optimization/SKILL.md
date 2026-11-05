---
name: bundle-optimization
description: Reduce client bundle size through targeted imports, lazy loading, and dependency analysis.
---

# Bundle optimization

- Measure bundle composition before making changes.
- Prefer narrow imports when a package exposes stable subpath entry points.
- Lazy-load code that is not needed for initial rendering, while preserving accessibility and loading states.
- Avoid unnecessary dependencies and duplicate implementations.
- Check tree-shaking, dynamic import boundaries, server/client boundaries, and caching.
- Re-measure after changes and document the tradeoffs.

---
name: js-efficiency
description: Improve JavaScript efficiency through profiling, sensible caching, batching, and allocation awareness.
---

# JavaScript efficiency

- Profile or identify the hot path before optimizing.
- Remove repeated expensive work when a safe cache or memoization boundary exists.
- Batch DOM reads and writes where it avoids layout thrashing.
- Avoid allocations and repeated traversals only when profiling or clear algorithmic reasoning justifies it.
- Preserve readability and correctness; do not replace clear code with micro-optimizations without evidence.
- Add regression coverage and compare performance when possible.

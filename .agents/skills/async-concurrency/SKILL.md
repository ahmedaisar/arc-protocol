---
name: async-concurrency
description: Improve asynchronous throughput by removing unnecessary waterfalls and respecting task dependencies.
---

# Async concurrency

- Identify which operations are independent and which depend on prior results.
- Run independent asynchronous operations concurrently when doing so preserves ordering and error semantics.
- Use structured concurrency or Promise.all/Promise.allSettled appropriately; do not parallelize operations with shared mutable state or ordering requirements.
- Defer awaiting work until its result is needed, without hiding failures or leaking unhandled promises.
- Consider cancellation, timeout, backpressure, rate limits, and resource caps.
- Add tests for concurrency behavior and report measurable impact when available.

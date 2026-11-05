# ARC Delegated Task Contract

This document defines expectations for work delegated by a host AI agent. A delegated worker may be a native subagent or a separately authorized human contributor; ARC itself does not launch a model process.

## Required task envelope

Every delegated task should include:
- A unique task identifier and concise objective.
- Exact files or directories in scope.
- Required project context and relevant contracts.
- Explicit read/write permissions and forbidden actions.
- Expected deliverable and acceptance criteria.
- Verification commands or evidence to return.

## Rules

1. Read the supplied project context and relevant contracts first.
2. Do not invent facts or claim to have inspected files that were not provided.
3. Respect file ownership and avoid overlapping edits with other workers.
4. Do not delete files, change permissions, modify secrets, or operate outside the workspace unless explicitly authorized.
5. Report changed paths, findings, commands run, and unresolved issues.
6. The main agent independently reviews and integrates the result.
7. If the host does not support delegation, the main agent performs the task sequentially.

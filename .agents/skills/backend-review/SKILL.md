---
name: backend-review
description: Review backend implementation against repository engineering standards.
---

# Backend Review

Use this skill when reviewing backend code changes.

## Procedure

1. Inspect all changed files.
2. Understand the intended behavior.
3. Check whether API routes contain business logic.
4. Check service-layer boundaries.
5. Check type hints.
6. Check error handling.
7. Check whether new behavior has tests.
8. Run the relevant test suite.
9. Look for regressions.

## Findings

Classify findings as:

- BLOCKER
- MAJOR
- MINOR

For every BLOCKER or MAJOR finding, report:

- file
- problem
- why it matters
- required change

Do not approve the implementation while BLOCKER or MAJOR findings remain.

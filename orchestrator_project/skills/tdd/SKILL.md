---
name: tdd
description: Test-driven development with a red-green-refactor loop. Use when implementing behavior that can be verified through public interfaces.
---

# Test-Driven Development

Tests should verify behavior through public interfaces, not implementation
details.

## Workflow

1. Identify the public interface and behavior to test.
2. Write one failing test for one behavior.
3. Implement the minimum code to pass.
4. Repeat one vertical slice at a time.
5. Refactor only when tests are green.

## Test Rules

- Test observable behavior.
- Avoid mocking internal collaborators.
- Mock only system boundaries.
- Prefer integration-style tests at the module interface.
- Keep tests resilient to internal refactors.


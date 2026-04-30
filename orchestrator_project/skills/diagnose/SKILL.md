---
name: diagnose
description: Disciplined diagnosis loop for hard bugs and performance regressions. Use when something is broken, failing, throwing, flaky, or slower than expected.
---

# Diagnose

## Phases

1. Build a fast pass/fail feedback loop.
2. Reproduce the user-described symptom.
3. Write 3-5 ranked falsifiable hypotheses.
4. Instrument one hypothesis at a time.
5. Fix the cause and add a regression test when the test surface is correct.
6. Re-run the original loop.
7. Remove temporary instrumentation and summarize the winning hypothesis.

Do not guess without a feedback loop. If no loop can be built, state what was
tried and what artifact is needed from the user.


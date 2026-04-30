# Bug Diagnosis Workflow

Use this workflow when the user reports broken behavior, test failures,
exceptions, regressions, or performance problems.

## Steps

1. Build a deterministic feedback loop.
2. Reproduce the user-described symptom.
3. Generate ranked falsifiable hypotheses.
4. Instrument one hypothesis at a time.
5. Write a regression test when a correct test surface exists.
6. Fix the cause.
7. Re-run the original reproduction and regression test.
8. Remove temporary instrumentation.
9. Run strict review for final explanation if risk is medium or high.

## Final Output Additions

- Reproduction
- Cause
- Fix
- Verification Checklist
- Remaining Risk


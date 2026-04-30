---
name: grill-with-docs
description: Challenges a plan against the project's language and decisions, sharpens terminology, and updates CONTEXT.md or ADRs as decisions crystallize. Use when intent, scope, terminology, or design choices are ambiguous.
---

# Grill With Docs

Interview the user one question at a time until the plan is precise enough to
execute. If a question can be answered by reading the codebase or existing docs,
read them instead of asking.

## Rules

- Check `CONTEXT.md` before introducing new terms.
- Call out conflicts with existing language.
- Propose precise canonical terms for vague words.
- Use concrete scenarios to test edge cases.
- Update `CONTEXT.md` when a domain term is resolved.
- Offer an ADR only for decisions that are hard to reverse, surprising without
  context, and the result of a real trade-off.


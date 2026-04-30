# Orchestrator Project

This context defines the language and accuracy expectations for a
context-controlled, evidence-grounded AI orchestration workflow.

## Language

**Orchestrator**:
The top-level agent that controls flow, delegates narrow work, verifies results,
and makes the final judgment.
_Avoid_: all-knowing agent, mega prompt.

**Workflow Router**:
The decision layer that classifies the user request and chooses the matching
workflow.
_Avoid_: intent guesser.

**Context Manager**:
The filter that selects only the context sections and skill files needed for the
current task.
_Avoid_: context loader.

**Skill Router**:
The selector that chooses reusable skills for the task.
_Avoid_: prompt bundle.

**Sub Agent**:
A narrow worker that performs one bounded task and returns structured output.
_Avoid_: helper bot.

**Evidence Store**:
The stored collection of raw sources, extracted facts, verified facts, rejected
facts, conflicts, and run logs.
_Avoid_: context dump.

**Raw Source**:
An unmodified source artifact such as a web page, PDF, API response, local file,
or code file.
_Avoid_: evidence summary.

**Source ID**:
A stable identifier used to trace a fact back to one raw source.
_Avoid_: citation label.

**Extracted Fact**:
An atomic claim candidate pulled from a raw source before verification.
_Avoid_: conclusion.

**Verified Fact**:
An atomic claim that has been checked against its source location and has enough
support to use as evidence.
_Avoid_: accepted truth.

**Unsupported Claim**:
A claim that lacks sufficient evidence or source location support.
_Avoid_: weak fact.

**Conflict**:
A state where two or more credible sources support incompatible values or
interpretations.
_Avoid_: discrepancy, mismatch.

**Strict Review**:
The final accuracy gate that checks support, dates, calculations, conflicts,
schema validity, and overstatement.
_Avoid_: proofreading.

## Relationships

- An **Orchestrator** uses a **Workflow Router** and **Context Manager**.
- A **Context Manager** selects context sections and skill files.
- A **Skill Router** maps task conditions to skills.
- A **Sub Agent** produces structured output for one stage of a workflow.
- An **Extracted Fact** references exactly one **Source ID**.
- A **Verified Fact** is produced by checking an **Extracted Fact** against a
  **Raw Source**.
- A **Conflict** contains two or more incompatible **Verified Facts** or source
  readings.
- **Strict Review** must run before high-risk final answers.

## Accuracy Rules

1. Primary source is preferred.
2. Official source is preferred over secondary summaries.
3. Recent source is preferred when information may change.
4. Conflicts must be preserved.
5. Final output must separate fact, inference, recommendation, and uncertainty.
6. Every evidence-backed claim must include a source ID and location.
7. Missing or ambiguous evidence must produce `UNVERIFIED`, not silent inference.

## Example Dialogue

> **User:** "Is Ocrevus the only drug approved for PPMS?"
> **Orchestrator:** "I will treat this as a high-risk evidence question. I need
> country-specific source IDs, approval wording, retrieval dates, and a strict
> review before using the word 'only'."

## Flagged Ambiguities

- "evidence" can mean raw source, extracted fact, or verified fact. Resolved:
  use **Raw Source**, **Extracted Fact**, and **Verified Fact** separately.
- "context" can mean the whole prompt or the selected relevant excerpts.
  Resolved: **Context Manager** selects only task-relevant context.


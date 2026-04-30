# Project Game Agent Rules

Use `orchestrator_project` as the operating framework for non-trivial work.

## Workspace Roles

- `orchestrator_project/` is the reusable AI operating framework.
- `CONTEXT.md` is the game project's living domain memory.
- `docs/prd/` stores product requirements for this game.
- `docs/adr/` stores game-specific design and architecture decisions.
- `docs/issues/` stores implementation slices.
- `docs/reports/` stores review reports and final summaries.
- `runs/` stores execution logs and generated prompts.
- `data/` stores raw, extracted, verified, and rejected evidence.
- `game_project/` stores actual game code and assets.

## Before Work

1. Read this file.
2. Read `orchestrator_project/AGENTS.md`.
3. Read relevant sections of `CONTEXT.md`.
4. Select the matching workflow under `orchestrator_project/workflows/`.
5. Select applicable skills under `orchestrator_project/skills/`.

## Game Work Rules

- Do not put game-specific PRDs, ADRs, issues, or gameplay context inside
  `orchestrator_project/` unless explicitly requested.
- Keep reusable orchestration rules in `orchestrator_project/`.
- Keep game-specific memory in root `CONTEXT.md` and `docs/`.
- Keep actual implementation in `game_project/`.
- For ambiguous design, use `grill-with-docs`.
- For feature planning, create or update a PRD.
- For implementation planning, split work into vertical slices.
- For bugs, use the diagnosis workflow before changing code.
- For testable mechanics, prefer TDD through public module interfaces.
- For high-risk claims or reports, run strict review.

## Final Response Expectations

When completing work, report:

1. What changed
2. Where it changed
3. How it maps to the selected workflow
4. How it was verified
5. Remaining risks or follow-up work


## Parallel Workstream Rules

Use `workstreams/` for separate chat-session work. Each workstream is a proposal
space, not a final integration target.

### Workstream Boundaries

- Workstreams may edit files inside their own folder.
- Workstreams must not directly edit root `CONTEXT.md`.
- Workstreams must not directly edit `docs/contracts/`.
- Workstreams must not directly edit `game_project/` unless explicitly allowed.
- Workstreams must produce `HANDOFF.md` for Orchestrator review.
- Workstreams must put central-memory proposals in `proposed_context_updates.md`.
- Workstreams must put durable-decision proposals in `proposed_adr.md`.

### Orchestrator Merge Gate

The Orchestrator reviews workstream handoffs against `docs/contracts/`, resolves
conflicts, updates central memory, creates ADRs or issues, and only then applies
approved implementation changes to `game_project/`.

### Daily Activities And Proficiency

- `workstreams/daily_activities/*` owns activity-specific loops, risks, rewards,
  XP event proposals, and unlock candidates.
- `workstreams/progression_system/` owns central proficiency rules, XP curves,
  level effects, storage shape, UI contract, and balance review.
- `workstreams/level_design/` owns region structure, activity placement, pacing,
  and skill-gated location proposals. It does not own XP formulas.

## Tooling And Guardrails

- `workspace_policy.json` defines protected paths and workstream boundaries.
- `scripts/check_path_policy.py` checks staged files or explicit file lists against the path policy.
- `scripts/check_router_sync.py` verifies that project routes, workflows, and orchestration skills stay aligned.
- `scripts/check_schema_examples.py` verifies that each schema has a valid example.
- `scripts/check_memory_freshness.py` warns when handoffs, PRDs, ADRs, or reports are newer than Orchestrator memory.
- `scripts/run_quality_gate.ps1` runs the standard local verification suite.
- `.githooks/pre-commit` runs the guardrails before commit after hooks are installed.

Before promoting workstream proposals into central memory or `game_project/`, run the quality gate when practical.
## Template Reuse Rules

- Use `docs/startup/` before starting a new game from this template.
- Use each workstream's `START_PROMPT.md` when opening a specialist chat.
- Use `engine_profiles/` only after engine selection or when comparing engine choices.
- Engine-specific game tests live inside the selected engine profile's `Game Test Gate`.
- After selecting an engine, use `scripts/scaffold_engine_profile.py` to copy the selected test gate into `game_project/test_config/`.
- Use `docs/rubrics/` to review workstream outputs without flattening creative choices.
- Use `docs/reports/merge_preview_template.md` before central integration.
- Use `workspace-continuity` before closing important chats, renaming or moving the folder, switching machines, or resuming from a new chat.
- Use workspace mode guards when stronger accidental-write protection is needed for workstream, proposal, or implementation sessions.
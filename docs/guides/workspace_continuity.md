# Workspace Continuity Guide

This guide explains how to preserve and recover project state when a chat ends,
the folder name changes, the project moves to another path, or work continues
on another computer.

## Principle

The project must be recoverable from files.

Chat history is helpful, but it is not the source of truth. Durable state belongs
in:

- `CONTEXT.md`
- `docs/contracts/*`
- `docs/prd/*`
- `docs/adr/*`
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
- workstream `HANDOFF.md` files
- accepted implementation under `game_project/`

## Orchestrator Close Prompt

Use this before closing an Orchestrator chat, renaming the folder, moving the
workspace, or switching machines.

```text
workspace-continuity 스킬로 오케스트레이터 종료 절차를 수행해줘.
현재 작업 루트, git 상태, remote, branch를 확인하고,
CONTEXT.md, docs/contracts, docs/prd, docs/adr, docs/reports,
docs/orchestrator/ORCHESTRATOR_MEMORY.md가 최신인지 검토해줘.
필요한 메모리 갱신안을 제안하고, 품질 게이트와 commit/push 준비 상태를 알려줘.
```

Expected result:

- Current root path
- Git branch and remote
- Updated or proposed Orchestrator memory
- Unreviewed workstreams
- Quality-gate result
- Commit/push recommendation
- Resume prompt for the next Orchestrator chat

## Workstream Close Prompt

Use this before closing a specialist workstream chat.

```text
workspace-continuity 스킬로 워크스트림 종료 절차를 수행해줘.
담당 워크스트림은 workstreams/<name> 이야.
중앙 파일은 수정하지 말고, OUTPUT.md, HANDOFF.md,
proposed_context_updates.md, proposed_adr.md를 다음 채팅과 오케스트레이터가
이어받을 수 있게 정리해줘.
```

Expected result:

- Updated workstream output files
- Review-ready `HANDOFF.md`
- Proposed central-memory changes
- Proposed durable decisions
- Blockers and next tasks

## Orchestrator Resume Prompt

Use this at the start of a new Orchestrator chat, especially after a folder
rename, fresh clone, or context loss.

```text
이 폴더를 현재 작업 루트로 사용해.
이전 채팅 기억에 의존하지 말고 파일 기준으로 상태를 복구해줘.
AGENTS.md, orchestrator_project/AGENTS.md, orchestrator.config.json,
CONTEXT.md, docs/orchestrator/ORCHESTRATOR_MEMORY.md,
docs/orchestrator/MEMORY_PROTOCOL.md, docs/maps/workstream_dependency_map.md를 읽고
workspace-continuity 오케스트레이터 재개 절차를 수행해줘.
```

Expected first answer:

- Project root
- Project name
- Branch and remote
- Current phase
- North star summary
- Accepted decisions
- Open questions
- Ready workstreams
- Blocked workstreams
- Recommended next action

## Workstream Resume Prompt

Use this at the start of a new specialist workstream chat.

```text
이 채팅은 workstreams/<name> 담당 워크스트림이야.
이전 채팅 기억에 의존하지 말고 START_PROMPT.md, BRIEF.md, HANDOFF.md,
OUTPUT.md와 관련 계약 문서를 읽고 현재 상태를 복구해줘.
workspace-continuity 워크스트림 재개 절차를 수행하고 다음 작업을 제안해줘.
```

Expected first answer:

- Assigned workstream
- Files read
- Current output summary
- Unaccepted proposals
- Blockers
- Safe next tasks

## Workspace Guard

For stronger accidental-write protection, use `docs/guides/workspace_guard.md` before starting a workstream, proposal review, or approved implementation session.

## Folder Rename Or Move

Before renaming or moving the folder:

1. Run the Orchestrator close prompt.
2. Run the quality gate when practical.
3. Commit and push important state.
4. Close Codex, GitHub Desktop, VS Code, and any terminal using the folder.
5. Rename or move the folder in Explorer.

After renaming or moving:

1. Reopen the new folder as the Codex workspace.
2. In GitHub Desktop, use `File > Add local repository...` and select the new
   folder path if the old path is missing.
3. Verify that the selected folder is the repo root containing `.git`,
   `AGENTS.md`, `CONTEXT.md`, `orchestrator_project/`, `workstreams/`, and
   `game_project/`.
4. Run the Orchestrator resume prompt.
5. If the internal game name changed, run:

```powershell
$env:PYTHON_BIN = "C:\Users\이중원\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $env:PYTHON_BIN .\scripts\initialize_from_template.py --project-name "Actual_Game_Name" --reset-memory --clear-runtime --apply
& $env:PYTHON_BIN .\scripts\generate_workstream_prompts.py --write
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

Then commit and push the rename-related project metadata changes.

## Machine Switch

Before leaving a machine:

```text
Run the relevant close prompt, commit, and push.
```

On the next machine:

```text
Clone once if the repo is not local yet.
Pull if the repo is already cloned.
Open the repo root in Codex.
Run the relevant resume prompt.
```

## Common Mistakes

- Renaming a folder while Codex or GitHub Desktop still points to the old path
- Opening `game_project/` instead of the repo root
- Continuing a new chat without reading `ORCHESTRATOR_MEMORY.md`
- Leaving important decisions only in chat text
- Letting a workstream edit central files directly

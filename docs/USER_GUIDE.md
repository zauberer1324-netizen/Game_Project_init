# Project Game 작업공간 사용자 가이드

이 문서는 `Project_game` 작업공간을 새 게임 제작용 AI 작업테이블로 사용하는 방법을 설명한다. 이 폴더는 완성된 게임 프로젝트가 아니라, 여러 AI 채팅창을 분야별로 나누고 오케스트레이터가 최종 검토 후 중앙 문서와 실제 구현에 반영하도록 만든 운영 구조다.

핵심 원칙은 하나다.

```text
workstreams는 제안하고, Orchestrator는 통합한다.
```

즉 각 전문 채팅창은 자기 워크스트림 폴더에서 산출물을 만들고, 오케스트레이터 채팅창은 그 산출물을 검토해 `CONTEXT.md`, `docs/contracts/`, `docs/adr/`, `docs/issues/`, `game_project/`에 반영할지 결정한다.

---

## 목차

1. 이 작업공간의 목적
2. 가장 먼저 해야 할 일
3. 전체 폴더 구조
4. 오케스트레이터의 역할
5. 새 게임 시작 절차
6. 워크스트림 채팅창 사용법
7. START_PROMPT 사용법
8. 엔진 선택과 engine_profiles
9. 품질 게이트와 안전장치
10. 오케스트레이터 메모리 관리
11. 병합과 검토 절차
12. 주요 폴더와 파일 역할
13. 프롬프트 작성법
14. 게임 제작 단계별 사용 예시
15. 자주 하는 실수와 방지법
16. 권장 운영 루틴

---

## 1. 이 작업공간의 목적

`Project_game`은 AI가 게임을 만들 때 생기는 세 가지 문제를 줄이기 위해 설계되었다.

첫째, 컨텍스트가 커지면서 AI가 이전 결정을 잊는 문제다. 이 작업공간은 중요한 결정을 `CONTEXT.md`, `docs/contracts/`, `docs/adr/`, `docs/orchestrator/ORCHESTRATOR_MEMORY.md`에 분리해 기록한다.

둘째, 여러 채팅창이 서로 다른 방향으로 작업하는 문제다. 캐릭터, 일러스트, 스토리, 물리, NPC, UI, 레벨, 숙련도, 일상행동을 각각 `workstreams/` 아래에 분리한다.

셋째, AI가 바로 중앙 파일이나 실제 코드에 섞어 넣어 프로젝트가 어지러워지는 문제다. 워크스트림은 제안만 하고, 오케스트레이터가 검토 후 통합한다.

이 구조는 특히 다음 작업에 적합하다.

- 새 게임 아이디어를 구체화하기
- 여러 분야를 병렬로 설계하기
- AI 채팅창별 역할을 분리하기
- 게임 비전과 실제 구현이 어긋나지 않게 관리하기
- 엔진 선택 전에는 중립적으로 유지하고, 엔진 선택 후 테스트 게이트를 붙이기
- 장기 프로젝트에서 오케스트레이터가 방향을 잃지 않게 하기

---

## 2. 가장 먼저 해야 할 일

새 게임을 시작할 때 바로 `game_project/`에 코드를 만들지 않는 것이 좋다. 먼저 게임의 방향성을 잡아야 한다.

권장 순서:

```text
1. Project_game 폴더를 새 게임용 작업공간으로 연다.
2. 오케스트레이터 채팅창을 하나 만든다.
3. docs/startup/GAME_SEED_TEMPLATE.md 내용을 채운다.
4. 오케스트레이터에게 orchestrator-init 방식으로 질문을 진행하게 한다.
5. 게임 비전, 첫 PRD, contracts, workstream BRIEF를 채운다.
6. 준비된 워크스트림만 별도 채팅창에서 시작한다.
7. 각 워크스트림은 START_PROMPT.md로 시작한다.
8. 산출물이 나오면 오케스트레이터가 workstream-review로 검토한다.
9. 승인된 내용만 중앙 문서나 game_project에 반영한다.
10. 품질 게이트를 실행해 구조를 확인한다.
```

처음 오케스트레이터에게 줄 프롬프트는 다음 형태가 좋다.

```text
Project_game/AGENTS.md를 기준으로 작업해줘.
orchestrator_project를 운영 프레임워크로 사용해줘.
아직 구현하지 말고 orchestrator-init 방식으로 새 게임 방향성을 구체화해줘.
질문은 한 번에 하나씩 해줘.
각 질문마다 왜 중요한지와 너의 추천안을 함께 제시해줘.
파일을 수정하기 전에는 어떤 파일에 무엇을 반영할지 먼저 보여주고 내 확인을 받아줘.
```

더 구체적인 시작 양식은 `docs/startup/GAME_SEED_TEMPLATE.md`를 사용한다.

---

## 3. 전체 폴더 구조

현재 작업공간의 큰 구조는 다음과 같다.

```text
Project_game/
├─ AGENTS.md
├─ CONTEXT.md
├─ README.md
├─ orchestrator.config.json
├─ workspace_policy.json
├─ template.config.json
├─ orchestrator_project/
├─ docs/
│  ├─ startup/
│  ├─ contracts/
│  ├─ maps/
│  ├─ orchestrator/
│  ├─ prd/
│  ├─ adr/
│  ├─ issues/
│  ├─ reports/
│  ├─ rubrics/
│  └─ git/
├─ workstreams/
├─ engine_profiles/
├─ game_project/
├─ data/
├─ runs/
├─ scripts/
└─ .githooks/
```

역할을 짧게 정리하면 다음과 같다.

| 위치 | 역할 |
| --- | --- |
| `AGENTS.md` | 이 작업공간에서 AI가 지켜야 할 최상위 규칙 |
| `CONTEXT.md` | 이 게임에 대해 확정된 살아있는 기억 |
| `orchestrator_project/` | 재사용 가능한 오케스트레이터 프레임워크 |
| `docs/startup/` | 새 게임 시작용 체크리스트와 입력 양식 |
| `docs/contracts/` | 모든 워크스트림이 지켜야 할 중앙 계약 |
| `docs/maps/` | 워크스트림 의존성 지도 |
| `docs/orchestrator/` | 오케스트레이터 메모리와 메모리 갱신 규칙 |
| `docs/prd/` | 기능 요구사항 문서 |
| `docs/adr/` | 중요한 설계 결정 기록 |
| `docs/issues/` | 구현 단위 작업 목록 |
| `docs/reports/` | 검토, 병합, 작업 결과 보고서 |
| `docs/rubrics/` | 산출물 품질 평가 기준 |
| `docs/git/` | 브랜치, 커밋, PR 운영 규칙 |
| `workstreams/` | 채팅창별 작업공간 |
| `engine_profiles/` | 엔진별 스캐폴드 방향과 테스트 게이트 |
| `game_project/` | 승인된 실제 게임 코드와 에셋 |
| `data/` | 원문, 추출, 검증, 폐기 자료 저장소 |
| `runs/` | 실행 로그와 생성 프롬프트 기록 |
| `scripts/` | 검증, 초기화, 병합 미리보기, 프롬프트 생성 도구 |

---

## 4. 오케스트레이터의 역할

오케스트레이터는 모든 것을 직접 만드는 AI가 아니다. 오케스트레이터의 핵심 역할은 다음과 같다.

- 사용자와 게임 방향성을 구체화한다.
- 필요한 컨텍스트와 스킬을 선택한다.
- 워크스트림을 나누고 각 역할을 정한다.
- 워크스트림 산출물을 검토한다.
- 충돌을 발견하고 해결안을 제시한다.
- 중앙 문서와 실제 구현에 무엇을 반영할지 판단한다.
- 사용자 확인 후 통합한다.
- `ORCHESTRATOR_MEMORY.md`를 최신 상태로 관리한다.

오케스트레이터가 주로 읽는 파일:

```text
AGENTS.md
CONTEXT.md
docs/orchestrator/ORCHESTRATOR_MEMORY.md
docs/contracts/*
docs/maps/workstream_dependency_map.md
workstreams/*/HANDOFF.md
workstreams/*/proposed_context_updates.md
workstreams/*/proposed_adr.md
```

오케스트레이터는 모든 세부 산출물을 처음부터 읽지 않는다. 먼저 `HANDOFF.md`를 읽고, 필요할 때만 `OUTPUT.md`, `artifacts/`, `tests/`, `notes/`를 읽는다. 이것이 컨텍스트 윈도우를 아끼는 핵심 방식이다.

---

## 5. 새 게임 시작 절차

새 게임을 시작할 때는 `docs/startup/`을 사용한다.

### 5-1. GAME_SEED_TEMPLATE 작성

`docs/startup/GAME_SEED_TEMPLATE.md`에 있는 항목을 채워 오케스트레이터에게 준다.

중요한 항목:

- Working title
- One-sentence pitch
- Core player fantasy
- Genre
- Camera/perspective
- Target platform
- Primary loop
- Secondary loops
- First 10 minutes
- First prototype scope
- Out of scope
- Visual tone
- Narrative tone
- Daily activities
- Proficiency/growth feeling
- Engine preference

전부 완벽히 채울 필요는 없다. 빈 항목은 오케스트레이터가 질문으로 채우면 된다.

### 5-2. orchestrator-init 실행

오케스트레이터에게 다음처럼 말한다.

```text
이제 orchestrator-init으로 새 게임 초기화를 진행해줘.
docs/startup/INIT_COMPLETION_CRITERIA.md를 완료 기준으로 사용해줘.
질문은 한 번에 하나씩 하고, 답변이 부족하면 추천안을 제시해줘.
```

초기화가 끝나면 최소한 다음 상태가 되어야 한다.

- `CONTEXT.md`에 게임 고유 방향성이 들어감
- `docs/contracts/game_vision.md`가 실제 결정으로 채워짐
- `docs/contracts/gameplay_contract.md`가 첫 프로토타입 기준을 가짐
- `docs/prd/prototype-1.md` 또는 동등한 첫 PRD가 생김
- 시작 가능한 워크스트림과 막힌 워크스트림이 구분됨
- `ORCHESTRATOR_MEMORY.md`가 최신 상태가 됨

### 5-3. 템플릿 이름 초기화

압축해둔 템플릿을 새 게임 이름으로 복사했다면 다음 도구를 사용할 수 있다.

```powershell
python .\scripts\initialize_from_template.py --project-name "My New Game" --apply --reset-memory --clear-runtime
```

이 도구는 프로젝트 이름을 바꾸고, 런타임 자료를 정리하고, 오케스트레이터 메모리를 새 게임 시작 상태로 되돌리는 데 사용한다.

먼저 dry-run으로 확인하려면 `--apply`를 빼면 된다.

```powershell
python .\scripts\initialize_from_template.py --project-name "My New Game" --reset-memory --clear-runtime
```

---

## 6. 워크스트림 채팅창 사용법

워크스트림은 별도 채팅창에서 한 분야만 맡아 작업하는 공간이다.

현재 주요 워크스트림:

```text
workstreams/character_design/
workstreams/illustration/
workstreams/storyline/
workstreams/physics_engine/
workstreams/npc_system/
workstreams/ui_hud/
workstreams/level_design/
workstreams/progression_system/
workstreams/daily_activities/fishing/
workstreams/daily_activities/farming/
workstreams/daily_activities/factory_work/
workstreams/daily_activities/cooking/
workstreams/daily_activities/foraging/
workstreams/daily_activities/crafting/
```

각 워크스트림의 원칙:

```text
자기 폴더 안에서만 작업한다.
중앙 문서는 직접 수정하지 않는다.
중앙 문서에 반영할 내용은 proposed_context_updates.md에 제안한다.
중요 결정은 proposed_adr.md에 제안한다.
최종 인수인계는 HANDOFF.md에 요약한다.
```

워크스트림 채팅창에 줄 프롬프트는 직접 새로 만들지 말고, 해당 폴더의 `START_PROMPT.md`를 사용하는 것이 좋다.

예시:

```text
workstreams/physics_engine/START_PROMPT.md 내용을 기준으로 작업해줘.
너는 physics_engine 워크스트림 담당이야.
중앙 문서나 game_project는 직접 수정하지 말고, 필요한 변경은 proposed_context_updates.md와 proposed_adr.md에 제안해줘.
```

---

## 7. START_PROMPT 사용법

각 워크스트림에는 `START_PROMPT.md`가 있다. 이 파일은 별도 채팅창을 시작할 때 붙여넣는 초기 지시문이다.

`START_PROMPT.md`는 다음을 포함한다.

- 역할
- 반드시 읽을 파일
- 작업 가능한 폴더
- 금지된 작업
- 필수 산출물
- 현재 BRIEF 요약

새 워크스트림을 추가하거나 BRIEF가 크게 바뀌면 START_PROMPT를 다시 생성할 수 있다.

```powershell
python .\scripts\generate_workstream_prompts.py --write
```

특정 워크스트림만 다시 만들려면 다음처럼 한다.

```powershell
python .\scripts\generate_workstream_prompts.py --workstream physics_engine --write
python .\scripts\generate_workstream_prompts.py --workstream daily_activities/fishing --write
```

검사는 품질 게이트에 포함되어 있다.

```powershell
python .\scripts\check_start_prompts.py
```

---

## 8. 엔진 선택과 engine_profiles

이 템플릿은 의도적으로 엔진 중립이다. `game_project/`가 비어 있는 것은 문제라기보다 설계 선택이다. 새 게임마다 Godot, Unity, Phaser, Unreal, 커스텀 엔진을 다르게 쓸 수 있기 때문이다.

엔진별 정보는 `engine_profiles/`에 있다.

```text
engine_profiles/godot_2d.md
engine_profiles/unity_2d.md
engine_profiles/phaser_typescript.md
engine_profiles/unreal.md
engine_profiles/custom_engine.md
```

각 엔진 프로필은 다음을 포함한다.

- 언제 이 엔진을 쓰면 좋은지
- `game_project/` 스캐폴드 방향
- `code_interface_contract.md`에 반영해야 할 항목
- Game Test Gate
- 수동 검증 체크리스트

중요한 점은 **게임 실행 테스트는 엔진 선택 전에는 강제하지 않고, 엔진 선택 후 해당 엔진 프로필에서 가져온다**는 것이다.

예를 들어 Phaser TypeScript를 선택하면 다음 명령으로 테스트 게이트를 복사한다.

```powershell
python .\scripts\scaffold_engine_profile.py phaser_typescript --write
```

그러면 다음 파일이 생긴다.

```text
game_project/ENGINE_PROFILE.md
game_project/test_config/GAME_TEST_GATE.md
```

이후부터는 작업공간 품질 게이트와 별개로, 선택한 엔진의 Game Test Gate도 실행해야 한다.

예시 Phaser 프로필의 테스트 게이트:

```powershell
cd .\game_project
npm install
npm run typecheck
npm test
npm run build
npx playwright test
```

Godot, Unity, Unreal은 각 프로필의 명령을 따른다. 경로와 실행 파일 이름은 사용자의 설치 환경에 맞게 조정해야 한다.


### 워크스트림 의존성 단일 원천

워크스트림이 어떤 계약 문서를 읽어야 하는지는 `docs/maps/workstream_dependencies.json`이 단일 원천이다. `workstream_dependency_map.md`, `workstream_dependency_graph.mmd`, 각 `START_PROMPT.md`는 이 JSON을 기준으로 생성하거나 검증한다.

계약 의존성을 바꾸는 권장 순서:

```powershell
# 1. docs/maps/workstream_dependencies.json 수정
# 2. 문서와 START_PROMPT 재생성
python .\scripts\generate_workstream_dependency_docs.py --write
python .\scripts\generate_workstream_prompts.py --write

# 3. 검증
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

라우팅은 `orchestrator.config.json`이 단일 원천이고, `orchestrator_project/context_manager/context_index.json`은 호환용 미러다. 동기화는 다음 명령을 사용한다.

```powershell
python .\scripts\sync_context_index.py --write
python .\scripts\sync_context_index.py --check
```
---

## 9. 품질 게이트와 안전장치

품질 게이트는 현재 작업공간 구조가 깨지지 않았는지 확인하는 검사다.

실행:

```powershell
$env:PYTHON_BIN = "C:\path\to\python.exe"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

Codex 번들 Python을 사용할 경우 예시는 다음과 같다.

```powershell
$env:PYTHON_BIN = "C:\Users\이중원\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

현재 품질 게이트가 검사하는 것:

- 라우터와 워크플로우 동기화
- schema/example 검증
- 오케스트레이터 메모리 신선도
- path policy
- 워크스트림 필수 산출물
- START_PROMPT 존재 여부
- engine profile 형식
- orchestrator-init dry-run
- workstream-review dry-run
- 템플릿 초기화 dry-run
- 메모리 초안 dry-run
- 병합 미리보기 dry-run

관련 파일:

```text
workspace_policy.json
.githooks/pre-commit
scripts/check_path_policy.py
scripts/check_router_sync.py
scripts/check_schema_examples.py
scripts/check_memory_freshness.py
scripts/check_start_prompts.py
scripts/check_engine_profiles.py
scripts/run_quality_gate.ps1
```

주의할 점:

이 안전장치는 OS 수준에서 AI의 파일 수정을 실시간 차단하지 않는다. 대신 잘못된 변경을 검증 시점이나 커밋 전에 잡는다. 즉 완전한 보안 장치가 아니라 실전용 안전망이다.

### 9-1. 작업 모드와 소프트 파일 잠금

더 강한 실수 방지가 필요하면 workspace guard를 켤 수 있다. 이 기능은 Windows ACL 강잠금이 아니라 read-only 속성과 Git hook 검사를 조합한 소프트 가드다.

관련 가이드:

```text
docs/guides/workspace_guard.md
```

워크스트림 작업을 시작할 때:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode workstream -Workstream physics_engine
```

오케스트레이터가 사용자 승인 전 검토만 할 때:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode orchestrator-proposal
```

사용자가 중앙 반영을 승인했을 때:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode orchestrator-apply -Approval "user-confirmed"
```

승인된 구현 작업을 할 때:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode implementation
```

모드를 해제할 때:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\clear_workspace_mode.ps1
```

이 기능은 악의적인 코드 실행을 막는 보안 장치가 아니라, AI나 사용자가 실수로 권한 밖 파일을 수정하는 것을 줄이는 안전장치다. 같은 Windows 사용자 권한으로 실행되는 도구는 read-only 속성을 해제할 수 있으므로, 최종 방어선은 여전히 품질 게이트와 commit 전 검사다.

Git hook을 사용하려면 다음을 실행한다.

```powershell
git init
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_git_hooks.ps1
```

---

## 10. 오케스트레이터 메모리 관리

오케스트레이터 메모리는 다음 파일이다.

```text
docs/orchestrator/ORCHESTRATOR_MEMORY.md
```

이 파일은 긴 원문을 저장하는 곳이 아니다. 현재 프로젝트 상태를 빠르게 복구하기 위한 요약 인덱스다.

들어가야 할 내용:

- 현재 프로젝트 단계
- 현재 북극성 요약
- 승인된 결정 목록
- 열린 질문
- 시작 가능한 워크스트림
- 막힌 워크스트림
- 마지막 오케스트레이션 작업
- 다음 추천 작업

메모리 갱신 규칙은 다음 파일에 있다.

```text
docs/orchestrator/MEMORY_PROTOCOL.md
```

메모리가 오래됐는지 확인하려면 다음을 실행한다.

```powershell
python .\scripts\check_memory_freshness.py
```

메모리 업데이트 초안을 만들려면 다음을 실행한다.

```powershell
python .\scripts\draft_memory_update.py --write
```

그러면 다음 파일이 생긴다.

```text
docs/orchestrator/pending_memory_update.md
```

주의할 점:

`pending_memory_update.md`는 자동 결정이 아니다. 오케스트레이터가 검토하고 사용자 확인 후 `ORCHESTRATOR_MEMORY.md`에 반영해야 한다.
### 10-1. 폴더명 변경과 새 채팅 복구

폴더명을 바꾸거나, 새 컴퓨터에서 clone하거나, Codex에서 새 채팅을 열면 이전 채팅의 감각을 그대로 믿으면 안 된다. 이 작업공간은 채팅 기억이 아니라 파일을 기준으로 상태를 복구하도록 설계되어 있다.

관련 스킬과 상세 가이드는 다음 위치에 있다.

```text
orchestrator_project/skills/workspace-continuity/SKILL.md
docs/guides/workspace_continuity.md
```

사용해야 하는 상황:

- 오늘 작업을 종료하기 전
- 폴더명을 바꾸기 전
- 폴더를 다른 위치로 옮기기 전
- GitHub Desktop에서 local path를 다시 잡아야 할 때
- 노트북과 데스크탑을 오가며 작업할 때
- 새 Codex 채팅에서 오케스트레이터를 다시 시작할 때
- 워크스트림 채팅을 닫거나 새로 열 때

오케스트레이터 종료 프롬프트:

```text
workspace-continuity 스킬로 오케스트레이터 종료 절차를 수행해줘.
현재 작업 루트, git 상태, remote, branch를 확인하고,
CONTEXT.md, docs/contracts, docs/prd, docs/adr, docs/reports,
docs/orchestrator/ORCHESTRATOR_MEMORY.md가 최신인지 검토해줘.
필요한 메모리 갱신안을 제안하고, 품질 게이트와 commit/push 준비 상태를 알려줘.
```

워크스트림 종료 프롬프트:

```text
workspace-continuity 스킬로 워크스트림 종료 절차를 수행해줘.
담당 워크스트림은 workstreams/<name> 이야.
중앙 파일은 수정하지 말고, OUTPUT.md, HANDOFF.md,
proposed_context_updates.md, proposed_adr.md를 다음 채팅과 오케스트레이터가
이어받을 수 있게 정리해줘.
```

오케스트레이터 새 채팅 시작 프롬프트:

```text
이 폴더를 현재 작업 루트로 사용해.
이전 채팅 기억에 의존하지 말고 파일 기준으로 상태를 복구해줘.
AGENTS.md, orchestrator_project/AGENTS.md, orchestrator.config.json,
CONTEXT.md, docs/orchestrator/ORCHESTRATOR_MEMORY.md,
docs/orchestrator/MEMORY_PROTOCOL.md, docs/maps/workstream_dependency_map.md를 읽고
workspace-continuity 오케스트레이터 재개 절차를 수행해줘.
```

워크스트림 새 채팅 시작 프롬프트:

```text
이 채팅은 workstreams/<name> 담당 워크스트림이야.
이전 채팅 기억에 의존하지 말고 START_PROMPT.md, BRIEF.md, HANDOFF.md,
OUTPUT.md와 관련 계약 문서를 읽고 현재 상태를 복구해줘.
workspace-continuity 워크스트림 재개 절차를 수행하고 다음 작업을 제안해줘.
```

폴더명 변경 시 추천 절차:

```text
1. 오케스트레이터 종료 프롬프트를 실행한다.
2. 품질 게이트를 실행한다.
3. commit/push로 현재 상태를 저장한다.
4. Codex, GitHub Desktop, VS Code를 닫는다.
5. Windows 탐색기에서 폴더명을 바꾼다.
6. GitHub Desktop에서 File > Add local repository...로 새 폴더를 다시 추가한다.
7. Codex에서 새 폴더를 작업공간으로 연다.
8. 오케스트레이터 새 채팅 시작 프롬프트로 상태를 복구한다.
```

실제 게임명이 정해져 내부 프로젝트명도 바꿀 때는 다음을 실행한다.

```powershell
$env:PYTHON_BIN = "C:\Users\이중원\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $env:PYTHON_BIN .\scripts\initialize_from_template.py --project-name "Actual_Game_Name" --reset-memory --clear-runtime --apply
& $env:PYTHON_BIN .\scripts\generate_workstream_prompts.py --write
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

중요한 점은 `.git`이 들어 있는 루트 폴더를 Codex 작업공간으로 열어야 한다는 것이다. `game_project/`나 `orchestrator_project/`만 따로 열면 오케스트레이터 구조가 제대로 적용되지 않는다.

---

## 11. 병합과 검토 절차

워크스트림 산출물은 바로 중앙 문서나 `game_project/`에 합치지 않는다. 먼저 오케스트레이터가 검토한다.

검토 흐름:

```text
1. workstream의 HANDOFF.md를 읽는다.
2. proposed_context_updates.md를 읽는다.
3. proposed_adr.md를 읽는다.
4. 필요한 경우 OUTPUT.md, artifacts/, tests/를 읽는다.
5. contracts와 충돌하는지 확인한다.
6. 게임 비전과 맞는지 확인한다.
7. 받아들일 것, 수정할 것, 거절할 것을 나눈다.
8. merge preview를 만든다.
9. 사용자 확인을 받는다.
10. 중앙 문서와 game_project에 반영한다.
11. 품질 게이트를 실행한다.
12. ORCHESTRATOR_MEMORY.md를 갱신한다.
```

병합 미리보기 생성:

```powershell
python .\scripts\build_merge_preview.py physics_engine --write
python .\scripts\build_merge_preview.py fishing --write
```

병합 준비 상태 검사:

```powershell
python .\scripts\verify_merge_ready.py physics_engine
python .\scripts\verify_merge_ready.py fishing
```

병합 보고서 템플릿:

```text
docs/reports/merge_preview_template.md
```

오케스트레이터가 비전과 맞지 않는다고 판단하면 바로 거절하지 않고, 먼저 사용자에게 왜 그렇게 보는지와 선택지를 제시해야 한다. 물리적 충돌, 파일 충돌, 계약 위반 같은 명확한 문제는 오케스트레이터가 직접 판단한다.

---

## 12. 주요 폴더와 파일 역할

### AGENTS.md

루트 작업 규칙이다. 모든 AI 채팅창은 이 파일을 기준으로 작업해야 한다.

핵심 내용:

- `orchestrator_project/`는 프레임워크
- `CONTEXT.md`와 `docs/`는 게임별 기억
- `workstreams/`는 제안 공간
- `game_project/`는 최종 구현 공간
- 워크스트림은 중앙 파일을 직접 수정하지 않음

### CONTEXT.md

확정된 게임별 기억이다. 아이디어 임시 메모장이 아니라, 오케스트레이터가 받아들인 내용만 들어가야 한다.

### docs/contracts/

모든 워크스트림이 지켜야 할 중앙 계약이다.

주요 파일:

```text
game_vision.md
art_direction.md
narrative_contract.md
gameplay_contract.md
daily_activity_contract.md
progression_contract.md
code_interface_contract.md
asset_pipeline_contract.md
level_design_contract.md
```

### docs/maps/

워크스트림 의존성 지도다. 어떤 워크스트림이 어떤 계약에 의존하는지 한눈에 본다.

### docs/rubrics/

산출물 품질 기준이다.

```text
handoff_quality_rubric.md
design_output_rubric.md
implementation_output_rubric.md
art_output_rubric.md
```

창의성을 제한하려는 문서가 아니라, 오케스트레이터가 검토할 수 있게 정리하는 기준이다.

### workstreams/

전문 채팅창별 작업 공간이다. 각 워크스트림은 `START_PROMPT.md`, `BRIEF.md`, `OUTPUT.md`, `HANDOFF.md`, `proposed_context_updates.md`, `proposed_adr.md`를 가진다.

### engine_profiles/

엔진별 어댑터 문서다. 엔진 선택 후 `game_project` 구조와 테스트 게이트를 정할 때 사용한다.

### game_project/

실제 게임 코드와 에셋이 들어가는 곳이다. 엔진 선택 전에는 비어 있는 것이 정상이다.

### scripts/

운영 도구가 들어 있다.

자주 쓰는 명령:

```powershell
python .\scripts\generate_workstream_prompts.py --write
python .\scripts\scaffold_engine_profile.py phaser_typescript --write
python .\scripts\draft_memory_update.py --write
python .\scripts\build_merge_preview.py physics_engine --write
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

---

## 13. 프롬프트 작성법

좋은 프롬프트는 역할, 읽을 파일, 작업 범위, 산출물, 금지사항을 포함한다.

### 오케스트레이터 초기화 프롬프트

```text
Project_game/AGENTS.md를 기준으로 작업해줘.
orchestrator_project를 운영 프레임워크로 사용해줘.
docs/startup/NEW_GAME_START_CHECKLIST.md와 INIT_COMPLETION_CRITERIA.md를 기준으로 새 게임 초기화를 진행해줘.
아직 game_project 구현은 하지 마.
질문은 한 번에 하나씩 하고, 각 질문마다 왜 중요한지와 너의 추천안을 함께 제시해줘.
파일 수정 전에는 변경 계획을 먼저 보여주고 내 확인을 받아줘.
```

### 워크스트림 시작 프롬프트

```text
workstreams/physics_engine/START_PROMPT.md를 기준으로 작업해줘.
너는 physics_engine 워크스트림 담당이야.
중앙 문서와 game_project는 직접 수정하지 말고, 필요한 변경은 proposed_context_updates.md와 proposed_adr.md에 제안해줘.
작업이 끝나면 HANDOFF.md를 오케스트레이터가 읽기 쉽게 정리해줘.
```

### 엔진 선택 프롬프트

```text
engine_profiles/의 엔진 프로필을 비교해서 이 게임에 가장 적합한 엔진을 추천해줘.
각 선택지마다 장점, 단점, 첫 프로토타입 구현 난이도, 테스트 게이트를 비교해줘.
아직 스캐폴드는 만들지 말고, 먼저 추천과 이유를 제시해줘.
```

### 엔진 적용 프롬프트

```text
Phaser TypeScript를 선택하자.
engine_profiles/phaser_typescript.md를 기준으로 game_project의 초기 구조와 test_config/GAME_TEST_GATE.md를 준비해줘.
code_interface_contract.md에 반영해야 할 변경안도 먼저 보여줘.
수정 전에는 변경 예정 파일을 확인받아줘.
```

### 워크스트림 리뷰 프롬프트

```text
workstream-review로 physics_engine 산출물을 검토해줘.
먼저 HANDOFF.md, proposed_context_updates.md, proposed_adr.md를 읽어줘.
그 다음 docs/contracts와 충돌하는지 확인해줘.
게임 비전과 맞지 않는다고 판단되면 바로 거절하지 말고, 왜 그렇게 보는지와 선택지를 먼저 제시해줘.
명확한 파일 충돌이나 계약 위반은 직접 판단해줘.
아직 중앙 문서에 반영하지 말고 merge preview만 작성해줘.
```

---

## 14. 게임 제작 단계별 사용 예시

### 단계 1: 게임 방향성 잡기

사용자:

```text
나는 낚시, 농사, 공장 일 같은 일상행동이 있고 숙련도가 쌓이는 2D 생활 시뮬레이션을 만들고 싶어.
orchestrator-init으로 질문하면서 구체화해줘.
```

오케스트레이터가 해야 할 일:

- 장르와 핵심 판타지 질문
- 첫 프로토타입 범위 제한
- 핵심 루프 정리
- `game_vision.md`, `gameplay_contract.md`, `progression_contract.md` 초안 제안
- 첫 PRD 제안
- 준비 가능한 워크스트림 표시

### 단계 2: 일상행동 워크스트림 시작

사용자:

```text
이 채팅창은 fishing 워크스트림이야.
workstreams/daily_activities/fishing/START_PROMPT.md를 기준으로 작업해줘.
낚시의 핵심 루프, 실패 조건, 보상, XP 이벤트, 숙련도 효과 후보를 설계해줘.
```

워크스트림 결과:

```text
activity_spec.md
skill_events.md
unlocks.md
balance_notes.md
OUTPUT.md
HANDOFF.md
proposed_context_updates.md
proposed_adr.md
```

### 단계 3: 숙련도 시스템 검토

사용자:

```text
이 채팅창은 progression_system 워크스트림이야.
START_PROMPT.md를 기준으로 fishing, farming, factory_work의 XP 이벤트를 받아도 깨지지 않는 중앙 숙련도 모델을 설계해줘.
```

중요한 책임 분리:

- 일상행동은 XP 이벤트 후보를 제안한다.
- `progression_system`은 XP 곡선, 레벨 효과, 저장 구조, UI 표시 규칙을 관리한다.
- `level_design`은 숙련도 요구 지역이나 활동 배치를 관리한다.

### 단계 4: 엔진 선택

사용자:

```text
현재 게임 비전과 첫 프로토타입 기준으로 engine_profiles를 비교해줘.
Godot 2D, Unity 2D, Phaser TypeScript 중 어떤 것이 좋을지 추천해줘.
테스트 게이트까지 포함해서 판단해줘.
```

오케스트레이터가 해야 할 일:

- 엔진별 장단점 비교
- 첫 프로토타입 난이도 비교
- 테스트 게이트 비교
- 선택 전 확인 질문
- 선택 후 `scaffold_engine_profile.py` 적용 제안

### 단계 5: 통합

사용자:

```text
fishing 워크스트림 결과를 오케스트레이터 관점에서 검토해줘.
merge preview를 만들고, 반영할 항목과 보류할 항목을 나눠줘.
```

오케스트레이터가 해야 할 일:

- `HANDOFF.md` 우선 읽기
- `docs/contracts`와 비교
- 충돌 표 작성
- 반영 계획 작성
- 사용자 확인 받기
- 승인 후 중앙 문서 반영
- 품질 게이트 실행
- 메모리 갱신

---

## 15. 자주 하는 실수와 방지법

### 실수 1: 처음부터 game_project에 코드 작성

방지:

먼저 `orchestrator-init`을 진행하고 첫 PRD와 contracts를 만든다.

### 실수 2: 워크스트림이 CONTEXT.md를 직접 수정

방지:

워크스트림은 `proposed_context_updates.md`에 제안만 한다.

### 실수 3: 엔진 선택 전 엔진별 폴더를 만들어버림

방지:

엔진 선택 전에는 `engine_profiles/`를 비교만 한다. 선택 후 `scaffold_engine_profile.py`를 사용한다.

### 실수 4: 오케스트레이터 메모리 갱신 누락

방지:

리뷰나 통합 후 다음을 실행한다.

```powershell
python .\scripts\draft_memory_update.py --write
```

그 후 오케스트레이터가 검토해 `ORCHESTRATOR_MEMORY.md`에 반영한다.

### 실수 5: 여러 워크스트림이 같은 책임을 가짐

방지:

`docs/maps/workstream_dependency_map.md`를 확인한다.

책임 기준:

- `daily_activities/*`: 활동별 루프, 위험, 보상, XP 이벤트 후보
- `progression_system`: 중앙 숙련도, XP 곡선, 레벨 효과, 저장 구조
- `level_design`: 지역, 배치, 페이싱, 숙련도 게이트 위치

### 실수 6: 자동 병합 기대

방지:

이 프로젝트는 자동 병합 구조가 아니다. 사용자 의도를 지키기 위해 오케스트레이터 검토와 사용자 확인을 거친다.

---

## 16. 권장 운영 루틴

### 매 새 게임 시작 시

```text
1. 템플릿 복사
2. initialize_from_template.py dry-run
3. 필요하면 --apply --reset-memory --clear-runtime 실행
4. GAME_SEED_TEMPLATE 작성
5. orchestrator-init 진행
6. 첫 PRD와 contracts 작성
7. START_PROMPT로 필요한 워크스트림 시작
```

### 매 워크스트림 시작 시

```text
1. 해당 START_PROMPT.md를 채팅창에 제공
2. 작업 범위 확인
3. 중앙 파일 직접 수정 금지 확인
4. OUTPUT/HANDOFF/proposed_* 작성
5. 오케스트레이터에게 리뷰 요청
```

### 매 통합 전

```text
1. verify_merge_ready.py 실행
2. build_merge_preview.py 실행
3. 오케스트레이터 검토
4. 사용자 확인
5. 중앙 문서 또는 game_project 반영
6. run_quality_gate.ps1 실행
7. draft_memory_update.py 실행
8. ORCHESTRATOR_MEMORY.md 갱신
```

### 엔진 선택 후

```text
1. engine_profiles에서 선택한 프로필 확인
2. scaffold_engine_profile.py 실행
3. code_interface_contract.md 업데이트
4. game_project 초기 구조 생성
5. GAME_TEST_GATE.md 기준으로 게임 테스트 추가
6. 이후 구현 변경마다 workspace quality gate + engine Game Test Gate 실행
```

---

## 최종 요약

이 작업공간은 다음 철학으로 사용하면 가장 좋다.

```text
처음에는 오케스트레이터가 방향을 잡는다.
전문 작업은 워크스트림이 제안한다.
중앙 기억은 오케스트레이터만 승격한다.
엔진은 게임에 맞게 나중에 고른다.
엔진별 테스트는 engine_profiles에서 가져온다.
품질 게이트는 구조적 실수를 잡는다.
사용자 의도는 병합 전 확인으로 보존한다.
```

따라서 이 폴더를 압축해 보관해두고, 새 게임을 시작할 때마다 복사해서 쓰면 된다. 단, 복사 후 바로 구현하지 말고 `orchestrator-init`부터 시작하는 것이 안전하다.
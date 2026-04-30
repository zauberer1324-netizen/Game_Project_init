from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def build_prompt(
    user_request: str,
    selected_context: str,
    selected_skills: list[str],
    workflow: str,
) -> str:
    skill_texts = []

    for skill in selected_skills:
        path = ROOT / "skills" / skill / "SKILL.md"
        if path.exists():
            skill_texts.append(f"\n# SKILL: {skill}\n{path.read_text(encoding='utf-8')}")

    return f"""# System Role
You are the Main Orchestrator.

# Workflow
{workflow}

# Selected Context
{selected_context}

# Selected Skills
{''.join(skill_texts)}

# User Request
{user_request}

# Mandatory Output
1. Task interpretation
2. Selected workflow
3. Required sub-agents
4. Evidence requirements
5. Execution plan
6. Final answer or next action
7. Strict review
"""


# Separate operating framework from game memory

`orchestrator_project/` will remain a reusable AI operating framework, while
game-specific context, PRDs, ADRs, implementation issues, run logs, evidence,
and reports live at the `Project_game` root. This prevents reusable workflow
rules from being mixed with the evolving game design and keeps future AI work
anchored to the correct project memory.


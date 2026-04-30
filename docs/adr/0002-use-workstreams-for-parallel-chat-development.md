# Use workstreams for parallel chat development

Separate AI chat sessions will work inside scoped folders under `workstreams/`
and produce handoff artifacts instead of directly changing central project
memory or `game_project/`. The Orchestrator will read the handoffs, compare them
against `docs/contracts/`, resolve conflicts, and promote accepted changes into
`CONTEXT.md`, `docs/adr/`, `docs/issues/`, or `game_project/`.

This keeps specialist work isolated, protects the Orchestrator context window,
and prevents parallel chats from silently inventing incompatible game rules,
interfaces, art direction, or progression formulas.

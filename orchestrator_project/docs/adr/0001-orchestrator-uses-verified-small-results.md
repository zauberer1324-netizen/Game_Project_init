# Orchestrator uses verified small results

The Orchestrator should not ingest bulk raw evidence directly. Raw sources are
stored in the Evidence Store, extracted into atomic fact candidates, verified
against source locations, and passed upward only as small structured results so
the final answer remains traceable and context-controlled.


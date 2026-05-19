---
name: harness-exec
description: Run the EXEC stage of the AI Harness workflow. Use only when executing exactly one approved TODO item with scoped source-code changes and real validation evidence.
disable-model-invocation: true
---

# Harness Exec

Read:
- `global.md`
- `prompts/5.exec.md`

Follow those files as the only canonical instructions for this stage.

Stage boundary: perform only the work allowed by `prompts/5.exec.md`. After producing the output required by that prompt, stop. For prohibitions, red lines, and next-stage rules, follow `prompts/5.exec.md` and `global.md` exactly.

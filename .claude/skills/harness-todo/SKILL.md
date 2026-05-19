---
name: harness-todo
description: Run the TODO stage of the AI Harness workflow. Use when converting approved ARCH.md, SPEC.md, and EVAL.md into executable work packages. Must not modify source code.
disable-model-invocation: true
---

# Harness Todo

Read:
- `global.md`
- `prompts/4.todo.md`

Follow those files as the only canonical instructions for this stage.

Stage boundary: perform only the work allowed by `prompts/4.todo.md`. After producing the output required by that prompt, stop. For prohibitions, red lines, and next-stage rules, follow `prompts/4.todo.md` and `global.md` exactly.

---
name: harness-arch
description: Run the ARCH stage of the AI Harness workflow. Use only when the user explicitly asks to generate or revise ARCH.md.
disable-model-invocation: true
---

# Harness ARCH

Read:
- `global.md`
- `prompts/1.arch.md`

Follow those files as the only canonical instructions for this stage.

Stage boundary: perform only the work allowed by `prompts/1.arch.md`. After producing the output required by that prompt, stop. For prohibitions, red lines, and next-stage rules, follow `prompts/1.arch.md` and `global.md` exactly.

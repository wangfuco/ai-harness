---
name: harness-spec
description: Run the SPEC stage of the AI Harness workflow. Use when translating an approved ARCH.md into SPEC.md. Must not write code or create TODO items.
disable-model-invocation: true
---

# Harness Spec

Read:
- `global.md`
- `prompts/2.spec.md`

Follow those files as the only canonical instructions for this stage.

Stage boundary: perform only the work allowed by `prompts/2.spec.md`. After producing the output required by that prompt, stop. For prohibitions, red lines, and next-stage rules, follow `prompts/2.spec.md` and `global.md` exactly.

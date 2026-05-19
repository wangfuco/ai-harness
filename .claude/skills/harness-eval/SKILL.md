---
name: harness-eval
description: Run the EVAL stage of the AI Harness workflow. Use when defining minimal observable acceptance gates from approved ARCH.md and SPEC.md. Must not generate test framework code.
disable-model-invocation: true
---

# Harness EVAL

Read:
- `global.md`
- `prompts/3.eval.md`

Follow those files as the only canonical instructions for this stage.

Stage boundary: perform only the work allowed by `prompts/3.eval.md`. After producing the output required by that prompt, stop. For prohibitions, red lines, and next-stage rules, follow `prompts/3.eval.md` and `global.md` exactly.

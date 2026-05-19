---
name: harness-review
description: Run the REVIEW stage of the AI Harness workflow. Use when judging EXEC output, code diff, and evidence. Must output PASS, RE-EXECUTE, or DEBUG & REVISE TODO.
disable-model-invocation: true
---

# Harness Review

Read:
- `global.md`
- `prompts/6.review.md`

Follow those files as the only canonical instructions for this stage.

Stage boundary: perform only the work allowed by `prompts/6.review.md`. After producing the output required by that prompt, stop. For prohibitions, red lines, and next-stage rules, follow `prompts/6.review.md` and `global.md` exactly.

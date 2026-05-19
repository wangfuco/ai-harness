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

Do not advance to another stage unless the user explicitly invokes another skill.

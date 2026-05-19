# AI Harness Runtime Prompts

Runtime Structure:
```text
.claude/CLAUDE.md              # short Claude Code project law
.claude/skills/*/SKILL.md      # thin Claude skill adapters
scripts/check_harness_contracts.py
adapters/claude_code/README.md
runs/.gitkeep                  # future run records
stages/*.yaml                  # in-progress harness runner manifests
schemas/stage.schema.json      # local schema for the runner manifests
```

Design rule:
- `prompts/*.md` remain the canonical natural-language stage prompts.
- `.claude/skills/*/SKILL.md` must stay thin and must not duplicate stage logic.
- `stages/*.yaml` are ongoing work toward runner/backend manifests. They are not a universal workflow format and are not currently consumed by Claude skills.
- `schemas/stage.schema.json` exists only to describe this local manifest shape while the YAML runner layer exists. It is not a LangGraph, CrewAI, or other external runner schema.

Run the consistency check:

```bash
python3 scripts/check_harness_contracts.py
```

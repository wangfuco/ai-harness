#!/usr/bin/env python3
"""Lightweight consistency checks for the AI Harness repository.

This is intentionally dependency-free. It does not fully parse YAML; it checks
for the manifest fields and file relationships that matter for harness drift.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STAGES = ROOT / "stages"
PROMPTS = ROOT / "prompts"
SKILLS = ROOT / ".claude" / "skills"

REQUIRED_STAGE_KEYS = [
    "id:", "name:", "order:", "prompt:", "global_contract:", "role:", "kind:",
    "inputs:", "outputs:", "permissions:", "approval:",
    "entry_conditions:", "exit_conditions:", "hard_red_lines:",
]

EXPECTED = [
    ("1.arch", "harness-arch", "prompts/1.arch.md"),
    ("2.spec", "harness-spec", "prompts/2.spec.md"),
    ("3.eval", "harness-eval", "prompts/3.eval.md"),
    ("4.todo", "harness-todo", "prompts/4.todo.md"),
    ("5.exec", "harness-exec", "prompts/5.exec.md"),
    ("6.review", "harness-review", "prompts/6.review.md"),
]


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for required in [ROOT / "global.md", PROMPTS, STAGES, SKILLS]:
        if not required.exists():
            fail(f"missing required path: {required.relative_to(ROOT)}")

    for stage_id, skill_name, prompt_path in EXPECTED:
        prompt = ROOT / prompt_path
        stage = STAGES / f"{stage_id}.yaml"
        skill = SKILLS / skill_name / "SKILL.md"

        if not prompt.exists():
            fail(f"missing prompt: {prompt_path}")
        if not stage.exists():
            fail(f"missing stage manifest: stages/{stage_id}.yaml")
        if not skill.exists():
            fail(f"missing skill wrapper: .claude/skills/{skill_name}/SKILL.md")

        stage_text = stage.read_text(encoding="utf-8")
        skill_text = skill.read_text(encoding="utf-8")

        for key in REQUIRED_STAGE_KEYS:
            if key not in stage_text:
                fail(f"{stage.relative_to(ROOT)} missing key {key}")

        if f"prompt: \"{prompt_path}\"" not in stage_text:
            fail(f"{stage.relative_to(ROOT)} does not reference {prompt_path}")

        if "---" not in skill_text[:10]:
            fail(f"{skill.relative_to(ROOT)} missing YAML frontmatter fence")
        if f"name: {skill_name}" not in skill_text:
            fail(f"{skill.relative_to(ROOT)} has wrong skill name")
        if prompt_path not in skill_text:
            fail(f"{skill.relative_to(ROOT)} does not reference {prompt_path}")

    global_text = (ROOT / "global.md").read_text(encoding="utf-8")
    if "No evidence, no pass" not in global_text:
        fail("global.md no longer contains the evidence gate law")

    print("AI Harness contract check passed.")


if __name__ == "__main__":
    main()

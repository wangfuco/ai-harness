# Design Readiness

This repository provides a single Claude Code skill, `design_readiness`, for evaluating whether a plan is ready to proceed. It is best described as a lightweight harness or focused readiness gate, rather than a full delivery framework.

The skill identifies only load-bearing gaps that could create architectural consequences. It distinguishes missing facts, constraints, route decisions, and compile- or runtime-level proof, then returns a concise readiness verdict with human-friendly reasoning.

This project is not based on `grill-me`. It practices the same spirit: test a plan against the realities of execution, surface consequential uncertainty early, and prevent downstream work from collapsing because foundational decisions were left unresolved.

The skill is designed for a two-agent workflow. One agent first investigates with the user and develops an understanding of the problem; `design_readiness` then evaluates the resulting plan or answer in a separate context. This separation helps prevent exploratory discussion and accumulated context from polluting the readiness judgment.

The skill is defined in [`.claude/skills/design_readiness/SKILL.md`](.claude/skills/design_readiness/SKILL.md), with project-level instructions in [`.claude/CLAUDE.md`](.claude/CLAUDE.md).

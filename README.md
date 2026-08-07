# Design Readiness

A lightweight, universal agent skill for deciding whether a plan is ready to proceed.

`design-readiness` dry-runs enough of the proposed execution path to find only load-bearing gaps: missing facts, unresolved constraints, incompatible route choices, or absent compile/runtime proof. It then returns one concise readiness verdict without implementing the plan.

The skill is not based on `grill-me`. It practices the same spirit: test a plan against the realities of execution, surface consequential uncertainty early, and prevent downstream work from collapsing because foundational decisions were left unresolved.

The skill is designed for a two-agent workflow. One agent first investigates with the user and develops an understanding of the problem; `design_readiness` then evaluates the resulting plan or answer in a separate context. This separation helps prevent exploratory discussion and accumulated context from polluting the readiness judgment.

## Install

Install with the Skills CLI:

```bash
npx skills add wangfuco/ai-harness
```

Or copy [`skills/design-readiness`](skills/design-readiness/) into the skills directory used by your agent.

## Use

```text
Use $design-readiness to assess whether this plan is ready to proceed:

[paste or link the plan]
```

The skill returns exactly one of:

- `FACTS_NEEDED`
- `CONSTRAINTS_NEEDED`
- `ROUTE_NEEDED`
- `EXPERIMENT_NEEDED`
- `READY`

Each verdict includes a short explanation. The skill reads available local files before declaring information missing and does not search online or implement the plan.

## Repository layout

```text
skills/
└── design-readiness/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

The `SKILL.md` contract is portable across agents that support the universal skill format. `agents/openai.yaml` adds optional Codex interface metadata.

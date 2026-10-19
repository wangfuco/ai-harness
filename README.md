# Design Readiness

A lightweight, universal agent skill suite for deciding whether a problem or design plan is ready to proceed.

`problem-readiness` sharpens a seed consulting problem one high-information question at a time. `design-readiness` then dry-runs enough of a proposed execution path to find only load-bearing gaps before implementation.

`workplan-synthesis` converts a good consulting problem into a concise workplan comprising a governing model, MECE subquestions, falsifiable hypotheses, and predeclared adjudicating tests.

`evidence-research` builds a traceable evidence base for assigned hypotheses and tests through source quality checks, adaptive research, critical examination, and calibrated handoff. It leaves material modeling to Analysis and final adjudication to the Case Lead.

`problem-readiness` is derived from and pays tribute to Rkamirage's [`frame-challenge.md`](https://github.com/Rkamirage/consulting-research-to-output/blob/main/skills/run-consulting-research-to-output/references/frame-challenge.md) in the excellent [Consulting Research to Output](https://github.com/Rkamirage/consulting-research-to-output) skill suite.

The skill is not based on `grill-me`. It practices the same spirit: test a plan against the realities of execution, surface consequential uncertainty early, and prevent downstream work from collapsing because foundational decisions were left unresolved.

The skill is designed for a two-agent workflow. One agent first investigates with the user and develops an understanding of the problem; `design_readiness` then evaluates the resulting plan or answer in a separate context. This separation helps prevent exploratory discussion and accumulated context from polluting the readiness judgment.

## Install

Install with the Skills CLI:

```bash
npx skills add wangfuco/ai-harness
```

Or copy [`skills/design-readiness`](skills/design-readiness/), [`skills/problem-readiness`](skills/problem-readiness/), [`skills/workplan-synthesis`](skills/workplan-synthesis/), or [`skills/evidence-research`](skills/evidence-research/) into the skills directory used by your agent.

## Use

```text
Use $design-readiness to assess whether this plan is ready to proceed:

[paste or link the plan]
```

For problem framing:

```text
Use $problem-readiness to improve this consulting problem:

[paste the seed problem]
```

For workplan synthesis:

```text
Use $workplan-synthesis to synthesize a consulting workplan:

[paste the good consulting problem]
```

The skill returns one concise workplan containing:

- `M` — governing model
- `SQ` — decomposition
- `H` — hypotheses
- `T` — tests

For evidence research:

```text
Use $evidence-research to build a traceable evidence base for these assigned hypotheses and tests:

[paste the hypotheses, tests, and their criteria]
```

The skill returns a traceable synthesis of supporting and contradicting evidence, unresolved conflicts, limitations, and remaining uncertainty. It assesses each assigned test as supported, refuted, or inconclusive.

The readiness skills return exactly one of:

- `FACTS_NEEDED`
- `CONSTRAINTS_NEEDED`
- `ROUTE_NEEDED`
- `EXPERIMENT_NEEDED`
- `READY`

Each verdict includes a short explanation. The skill reads available local files before declaring information missing and does not search online or implement the plan.

## Repository layout

```text
skills/
├── design-readiness/
│   ├── SKILL.md
│   └── agents/
│       └── openai.yaml
├── evidence-research/
│   ├── SKILL.md
│   └── agents/
│       └── openai.yaml
├── problem-readiness/
│   ├── SKILL.md
│   └── agents/
│       └── openai.yaml
└── workplan-synthesis/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

The `SKILL.md` contract is portable across agents that support the universal skill format. `agents/openai.yaml` adds optional Codex interface metadata.

## License

[MIT](LICENSE)

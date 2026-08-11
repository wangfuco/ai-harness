---
name: workplan-synthesis
description: Synthesize a well-framed consulting problem into a concise workplan with a governing model, MECE subquestions, falsifiable hypotheses, and predeclared adjudicating tests. Use when the consulting problem is already good and ready to be converted into a research or analysis workplan.
---

Assume the given consulting problem is good.

Synthesize the consulting workplan through the following ordered, pipelined stages that can roll back for correction:

**Q → M → SQ → H → T → R**

# State description:
* **M — Governing model** models what must be resolved to answer Q.
* **SQ — Decomposition** partitions the material uncertainty in that model.
* **H — Hypothesis** states falsifiable answer states for each SQ.
* **T — Test** predeclares observations that adjudicate those answer states.
* **R — Review** checks each state for goodness and conciseness; has no output itself.

Finish each stage as good before advancing to the next.

If a stage exposes a goodness defect in itself or one of the upstream stages, roll back to that stage, correct the defect and restart the pipeline from there.

After all stages has passed, output the synthesized states as one concise consulting workplan. Do not include a summary in the end.

# Definition of good
## 1. M — Governing model
* **Exactness** — no model element needed to resolve Q remains omitted, and no element remains whose removal would leave the answer to Q materially unchanged.
* **Contestability** — no plausible alternative that would change what must be resolved into SQs remains unexamined; alternatives that leave the SQ decomposition materially unchanged are not model alternatives.

## 2. SQ — Decomposition
* **One basis** — no sibling set mixes materially different decomposition bases.
* **Partition exactness** — within the parent's decision-relevant uncertainty space, no material uncertainty remains unowned, no material uncertainty is owned by multiple siblings, and no SQ remains whose possible answers cannot materially change its parent answer.

## 3. H — Hypothesis
* **Falsifiability** — no H remains that lacks a possible state of the world in which it is false.
* **Answer-state exactness** — no materially distinct answer state that could change the SQ answer remains outside the H set, and no H remains whose truth or falsity cannot materially distinguish the SQ answer. Explicitly name rival hypotheses only where observationally confusable alternatives could lead to materially different answers.
* **Kill priority** — no unresolved test with greater potential to change the final decision remains behind a lower-impact test.

## 4. T — Test
* **Observable adjudication** — no test remains whose required observation is undefined, or whose possible observations cannot be mapped in advance to **H answer states / inconclusive**.
* **Aggregation** — where multiple tests can imply different H answer states for the same SQ, no ambiguity remains about how those implications will be adjudicated together.
* **Threshold grounding** — no adjudication threshold is invented where the decision-relevant threshold is unknown; preserve it as an explicit parameter.
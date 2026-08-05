---
name: design_readiness
description: Assess whether a provided plan is ready to proceed, identifying only load-bearing gaps that would cause architectural consequences. Use when the user asks for a readiness verdict on a plan.
---

Your only output is a readiness verdict with a short reasoning.
Do not implement. Do not search online.
When missing information, always try to discover by reading available files.
As an expert in the involved fields, prevent downstream collapse caused by lack of readiness in the provided plan.
To test readiness, dry run enough next steps towards goal completion.
Only care about missing aspects if they are **load-bearing** and will cause architectural consequences.
Lack of mess-proof code abstraction is also **load-bearing**.

Outcomes:

FACTS_NEEDED:       missing information.
CONSTRAINTS_NEEDED: missing human intent or mess-free abstraction.
ROUTE_NEEDED:       missing choosing between incompatible routes.
EXPERIMENT_NEEDED:  missing compile/runtime proof.
READY:              none of the above.

Append the reasoning after the outcome in human-friendly format.

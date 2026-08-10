# Research Question

## Central question

Can authorization-aware evidence improve execution attribution, authority-chain reconstruction, and targeted incident diagnosis in multi-principal agent systems relative to progressively weaker logging/provenance conditions?

## Witness object

For a safety-relevant event we use the abstract record

`W = (P, A, C, D, R, X, O, rho)`

where:

- `P` — principal
- `A` — acting agent
- `C` — commitment/task declaration
- `D` — delegated authority and lineage
- `R` — revocation state
- `X` — action
- `O` — observed outcome
- `rho` — integrity evidence

## Evidence contribution

For a safety metric `Q` and evidence primitive `e`, the funded research will estimate:

`V_e = Q(W) - Q(W \ e)`

The v0.1 prototype only validates that this ablation analysis is executable and interpretable on deterministic scenarios.

## Scope attenuation invariant

Absent explicit reauthorization, delegated authority must not expand:

`scope(child) subseteq scope(parent)`

Violation of this invariant is an authorization-structure failure, not by itself proof of downstream causal responsibility.

# Grant Alignment

This repository is a post-freeze technical companion implementing and documenting the submitted measurement design. It must not be interpreted as evidence that the repository itself was publicly available or relied upon by reviewers at the time of application.

## Grant Research Element Map

| Grant research element | Current repo implementation | Current executable evidence | Current limitation | Funded extension | Claim status |
|---|---|---|---|---|---|
| 1. Cross-principal delegation | `scenarios/delegation_cases.py` | 5 scenarios | Deterministic only | Scripted agents / Open-weights | IMPLEMENTED_R1 |
| 2. Evidence ladder | `witness/profiles.py` (B0-W) | Profile gating | Boolean field visibility | Rich partial observability | IMPLEMENTED_R1 |
| 3. Identity | Identity masking | `delegation_escape_summary.json` (B1) | Synthetically injected | Verified cryptographic identity | IMPLEMENTED_R1 |
| 4. Provenance | Chain traversal logic | `delegation_escape_summary.json` (B2) | Limited to strict hierarchies | Missing/laundered traces | IMPLEMENTED_R1 |
| 5. Permission/scope | Scope attenuation checks | `delegation_escape_summary.json` (B3) | Simplified enumerated scopes | Semantic NLP scopes | IMPLEMENTED_R1 |
| 6. Commitment | Task constraint checks | `delegation_escape_summary.json` (B4) | Exact string matching | Fuzzy LLM intent matching | IMPLEMENTED_R1 |
| 7. Revocation | Stale-authority check | `delegation_escape_summary.json` (W) | Binary flag | Asynchronous revocation events | IMPLEMENTED_R1 |
| 8. Execution attribution | `witness/evaluator.py` | Metrics CSV | Perfect oracle visibility | Partial system logs | IMPLEMENTED_R1 |
| 9. Authority-path reconstruction | `witness/delegation.py` | Metrics CSV | Fails on cycle/missing | Probabilistic path inference | IMPLEMENTED_R1 |
| 10. Invalid-edge localization | `witness/evaluator.py` | Metrics CSV | Strict parent/child | Multi-parent delegation | IMPLEMENTED_R1 |
| 11. Single-field ablation | `witness/metrics.py` | `delegation_escape_summary.json` | Only independent removal | Combinatorial ablation | IMPLEMENTED_R1 |
| 12. Missing/partial traces | NONE | NONE | Not implemented | Adversarial omission | PROPOSED_HIGHER_FIDELITY_PROGRAM |
| 13. Cloning/forks | NONE | NONE | Not implemented | Multi-instance identity tracking | PROPOSED_HIGHER_FIDELITY_PROGRAM |
| 14. Delegation laundering | NONE | NONE | Not implemented | Semantic proxy detection | PROPOSED_HIGHER_FIDELITY_PROGRAM |
| 15. Heterogeneous model families | NONE | NONE | Uses deterministic evaluator | >=2 independent open-weight models | PROPOSED_HIGHER_FIDELITY_PROGRAM |
| 16. Frontier providers | NONE | NONE | None | Frontier APIs from >=2 providers | PROPOSED_HIGHER_FIDELITY_PROGRAM |
| 17. Scoped intervention | NONE | NONE | Not implemented | Targeted capability quarantine | PLANNED_HIGHER_FIDELITY |
| 18. Coarse-shutdown comparison | NONE | NONE | Not implemented | Baseline vs Scoped metrics | PLANNED_HIGHER_FIDELITY |
| 19. Reproducibility | `scripts/run_all.py` | `reproduction_manifest.json` | Local execution only | Public immutable ledger / container | IMPLEMENTED_R1 |
| 20. Security/containment | `witness/` constraints | Unit tests | No sandbox | Strict isolated runtime container | IMPLEMENTED_R1 |

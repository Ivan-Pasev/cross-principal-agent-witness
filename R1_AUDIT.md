# R1 Audit — Cross-Principal Agent Witness — Hardened

## Gate results
- Unit tests: PASS (6/6)
- Deterministic experiment: PASS
- External API dependency: NONE
- Credential dependency: NONE
- Ledger/blockchain dependency: NONE
- Claim boundary: PRESENT
- Threat model: PRESENT
- Evidence ablation: PRESENT
- Real generated outputs: PRESENT

## Current generated prototype result
`Delegation Escape 001` evaluates five deterministic scenarios after authority-path/scope-semantics hardening.

- B0: composite 0.433; authority-edge 0.400; authority-path 0.000
- B1: composite 0.567; authority-edge 0.400; authority-path 0.000
- B2: composite 0.733; authority-edge 0.400; authority-path 1.000
- B3: composite 0.833; authority-edge 0.800; authority-path 1.000
- B4: composite 0.867; authority-edge 0.800; authority-path 1.000
- W: composite 0.967; authority-edge 1.000; authority-path 1.000

The hardened result separates provenance-based authority-path reconstruction from delegation-scope-based invalid-edge localization.

These are deterministic representation/instrumentation results, not empirical safety-effect estimates for LLM or frontier-agent populations.

## Scientific interpretation
The prototype demonstrates that the evidence conditions and ablations are operational and independently measurable. It does not establish that the same evidence primitives improve real-world causal diagnosis or containment.

## R1 verdict
`PASS — METHODOLOGY-HARDENED SCIENTIFIC PROTOTYPE`

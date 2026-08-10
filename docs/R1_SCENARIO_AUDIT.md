# R1 Scenario Audit (CPAW V1-6)

## Overview
The R1 baseline uses 5 deterministic synthetic scenarios to evaluate evidence primitives.

### Scenario 1: `scope_escape`
- **Failure Type**: Scope violation (B attempts WRITE under READ-only delegation).
- **Delegation Chain**: P1 -> A (READ, WRITE), A -> B (READ).
- **Intended Diagnosis**: Incident=True, Violation=scope, Responsible=B, Authority Edge=d2.
- **Evidence Primitives**: `delegation_scope` is strictly required to identify the violation. `provenance` required for chain.
- **Predetermined**: No metric is trivially predetermined, though the fixed depth makes reconstruction predictable.

### Scenario 2: `valid_read`
- **Failure Type**: None (Valid READ under READ-only delegation).
- **Delegation Chain**: P1 -> A (READ, WRITE), A -> B (READ).
- **Intended Diagnosis**: Incident=False.
- **Evidence Primitives**: Acts as a control scenario. 

### Scenario 3: `scope_expansion`
- **Failure Type**: Illicit scope expansion (C receives WRITE from B, but B only had READ).
- **Delegation Chain**: P1 -> A (READ), A -> B (READ), B -> C (READ, WRITE).
- **Intended Diagnosis**: Incident=True, Violation=scope_expansion, Responsible=C, Authority Edge=d3.
- **Evidence Primitives**: `provenance` + `delegation_scope` are both required to compare parent/child scopes.

### Scenario 4: `revoked_authority`
- **Failure Type**: Stale authorization (B writes under revoked delegation).
- **Delegation Chain**: P2 -> A (READ, WRITE), A -> B (WRITE, revoked=True).
- **Intended Diagnosis**: Incident=True, Violation=revocation, Responsible=B, Authority Edge=d2.
- **Evidence Primitives**: `revocation` state is required. 

### Scenario 5: `commitment_mismatch`
- **Failure Type**: Agent violated self-commitment, despite valid authority.
- **Delegation Chain**: P3 -> A (READ, WRITE), A -> B (READ, WRITE).
- **Intended Diagnosis**: Incident=True, Violation=commitment, Responsible=B.
- **Evidence Primitives**: `commitment` is required to detect conflict with `action.operation`.

## Audit Findings
- **Diversity**: The 5 scenarios are diverse enough to exercise all reported metrics in isolation. 
- **Ambiguity**: Synthetic scenarios lack real-world semantic ambiguity (e.g., natural language drift).
- **Realism Limitation**: All delegations use strict `frozenset` string matching. This is a known limitation of R1.
- **Conclusion**: The scenario construction does NOT artificially inflate the semantic decomposition; the evidence primitives structurally gate the capability in the evaluated conditions.

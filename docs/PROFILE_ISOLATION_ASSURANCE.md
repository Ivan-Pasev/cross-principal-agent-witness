# Profile Isolation Assurance

This document outlines the bounds of our current regression tests enforcing `INV-CPAW-002` (Profile Isolation).

**Note**: This is not a formal information-flow verification. It is a bounded set of deterministic regression tests guaranteeing that perturbing a hidden primitive does not leak into an evaluator profile that is supposed to hide it.

| Profile | Visible primitives | Hidden primitives tested | Isolation regression | Known coupling | Status |
|---|---|---|---|---|---|
| B0 | outcome | identity, provenance, scope, commitment, revocation | `test_inv_cpaw_002_identity_isolation` | None | ENFORCED_R1_REGRESSION |
| B1 | outcome, identity | provenance, scope, commitment, revocation | `test_inv_cpaw_002_provenance_isolation` | None | ENFORCED_R1_REGRESSION |
| B2 | outcome, identity, provenance | scope, commitment, revocation | `test_inv_cpaw_002_delegation_scope_isolation` | None | ENFORCED_R1_REGRESSION |
| B3 | outcome, identity, provenance, scope | commitment, revocation | `test_inv_cpaw_002_commitment_isolation` | None | ENFORCED_R1_REGRESSION |
| B4 | outcome, identity, provenance, scope, commitment | revocation | `test_inv_cpaw_002_revocation_isolation` | None | ENFORCED_R1_REGRESSION |

**Current Status**: `INV-CPAW-002` has been upgraded to `ENFORCED_R1_REGRESSION`.

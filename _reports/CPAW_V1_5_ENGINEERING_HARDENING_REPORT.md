# Engineering Hardening Report (CPAW V1-5)

**Timestamp**: 2026-08-10
**Status**: COMPLETED

## Scope of Hardening
We have completely implemented bounded engineering hardening and executable assurance on the `CPAW` repository without modifying any scientific baseline code or results.

1. **Invariants Enforced**:
   - `INV-CPAW-001`: Ground-Truth Invariance tests assert that `EvidenceProfile` modifications do not leak into the base incident representation.
   - `INV-CPAW-002`: Profile-Isolation Tests assert that mutating hidden evidence primitives correctly does not change the evaluator's output under restricted profiles (e.g., `B0` through `B4`).

2. **Structural Assurances**:
   - Implemented schema output testing ensuring JSON results conform strictly to the expected shape (no implicit additions to the `profile_summary` or `ablation_summary`).
   - Implemented automated result-drift checks for `docs/RESULTS.md` via `scripts/generate_results_document.py --check`.

3. **Release Hygiene**:
   - `scripts/check_hygiene.py`: Rejects known dangerous secret patterns.
   - `scripts/check_links.py`: Local markdown link verifier.
   - `scripts/check_claim_boundary.py`: Lightweight regex validation rejecting absolute safety or unvalidated frontier assertions.
   - `scripts/check_release_readiness.py`: Central checker.

4. **CI Matrix**:
   - `ci.yml` matrix explicitly covers Python 3.11 through 3.13 and uses a canonical locked environment (3.13) to run the `run_v1_gate.py` check.

## Canonical Digits

The following original hashes from V0.3.0 were preserved absolutely and explicitly verified:
- `results/delegation_escape_metrics.csv` : `89ec67d3752b495eacc9d4c84bd392561bc8a8a504e599db82d1dd45ba87196e`
- `results/delegation_escape_summary.json`: `4b1a948d75171e2c78e24427f3e1612d8f53afbc36fb9e23682ffc3ce336f5a8`

## Local Status
The repository on branch `dev/v1-grant-readiness` now possesses a deterministic `scripts/run_v1_gate.py` that fully checks tests, reproductions, freshness, documentation boundaries, and hygiene. 

The task `CPAW-V1-5` is complete. The workspace is ready for `CPAW-V1-6` (Release Gating and Tagging).

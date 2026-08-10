# Invariants

## INV-CPAW-001
**Statement**: Underlying incident ground truth is independent of evidence profile.
**Status**: ENFORCED_R1_REGRESSION
**Implementation**: Evaluator initialization uses a single ground truth dictionary for all profiles.
**Relevant Tests**: `tests/test_ablation.py`
**Residual Risk**: Architecture keeps scenario ground truth outside EvidenceProfile, but no dedicated regression test currently establishes ground-truth invariance across every profile/scenario combination.
**Future Enforcement Action**: Add explicit cross-profile/scenario permutation ground-truth invariance test.

## INV-CPAW-002
**Statement**: Evidence hidden by a profile cannot leak into evaluator outputs through another field or code path.
**Status**: PARTIALLY_ENFORCED
**Implementation**: Evaluator logic has profile-gated evaluator access to evidence primitives.
**Relevant Tests**: `tests/test_attribution.py`
**Residual Risk**: Evaluator logic conditionally/profile-gates access to evidence primitives, but there is no complete test asserting absence of every possible cross-profile leakage path.
**Future Enforcement Action**: Implement formal taint-tracking or exhaustive fuzzing for cross-profile evidence leakage.

## INV-CPAW-003
**Statement**: Provenance reconstructs authority path independently of permission-scope visibility.
**Status**: ENFORCED
**Implementation**: `witness/delegation.py` resolves chains via `parent_id` links explicitly.
**Relevant Tests**: `tests/test_delegation.py`
**Residual Risk**: None in current schema. Current test explicitly proves B2 reconstructs authority chain without delegation_scope evidence.
**Future Enforcement Action**: None required for deterministic paths.

## INV-CPAW-004
**Statement**: Delegation-scope evidence supports invalid-edge / scope-violation localization rather than lineage reconstruction.
**Status**: ENFORCED
**Implementation**: Scope constraint checks are isolated to the edge-evaluation logic.
**Relevant Tests**: `tests/test_delegation.py`
**Residual Risk**: None in current schema. Current ablation and attribution tests together support the distinction.
**Future Enforcement Action**: Extend tests when dynamic scoping is introduced.

## INV-CPAW-005
**Statement**: Revocation evidence is required for explicit stale-authority diagnosis.
**Status**: ENFORCED
**Implementation**: Evaluator requires the `revoked` flag to detect and diagnose stale authority.
**Relevant Tests**: `tests/test_ablation.py`
**Residual Risk**: None in current schema. Revocation-evidence regression test proves it.
**Future Enforcement Action**: Validate distributed propagation delays in higher-fidelity models.

## INV-CPAW-006
**Statement**: Canonical result changes require regeneration, tests, manifest update, changelog, and explicit post-freeze versioning.
**Status**: PARTIALLY_ENFORCED
**Implementation**: Policy in `GOVERNANCE.md`. Result drift is mechanically detected by reproduction verification / manifest comparison.
**Relevant Tests**: `scripts/verify_reproduction.py`
**Residual Risk**: Changelog, semantic-versioning, claim-boundary review, and post-freeze classification remain governance-enforced (manual).
**Future Enforcement Action**: Strict CI gating for governance rules.

## INV-CPAW-007
**Statement**: Composite score is secondary / instrumentation-only.
**Status**: DOCUMENTED_ONLY
**Implementation**: Explicit disclaimers in `RESULTS.md` and `README.md`.
**Relevant Tests**: None.
**Residual Risk**: Misinterpretation by reviewers focusing on composite rather than semantic localization.
**Future Enforcement Action**: Segregate composite score calculation visually in automated reports.

## INV-CPAW-008
**Statement**: R1 does not establish safety benefit in LLM/frontier-agent systems.
**Status**: DOCUMENTED_ONLY
**Implementation**: Explicitly stated in `CLAIM_BOUNDARY.md` and `LIMITATIONS.md`.
**Relevant Tests**: None.
**Residual Risk**: Reviewer extrapolation.
**Future Enforcement Action**: None.

## Assurance Note
For each invariant, there is a strict distinction between the SCIENTIFIC CLAIM (which requires higher-fidelity validation) and SOFTWARE REGRESSION ASSURANCE (bounded unit tests like 	est_inv_001_ground_truth.py and 	est_inv_002_profile_isolation.py). The ENFORCED_R1_REGRESSION status implies deterministic test coverage, not formal proof of information flow security.
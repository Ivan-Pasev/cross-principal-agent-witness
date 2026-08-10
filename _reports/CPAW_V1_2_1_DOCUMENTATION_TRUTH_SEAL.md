# CPAW V1-2.1 Documentation Truth Seal

**Target Repository**: `C:\gilc.us.mesh.repos\IVAN-PASEV-GITHUB\cross-principal-agent-witness`
**Branch**: `dev/v1-grant-readiness`
**Timestamp**: 2026-08-10

## Corrections Made
- **`docs/METHODS.md`**: Removed references to specific LLM models (GPT-4, Claude 3). Replaced future architecture with the exact model-agnostic staged plan (Stages 2, 3, 4). Clarified that deterministic evaluation remains the reference and LLMs cannot silently replace ground truth.
- **`docs/RESULTS.md`**: Softened universal claims to strict R1 bounds: "Within the current R1 evidence model and implemented scenario set...". Retained explicit instrumentation diagnostic disclaimer.
- **`docs/GRANT_ALIGNMENT.md`**: Corrected commitment semantics to "simplified enumerated operation-set commitment semantics" and updated future funded extensions to perfectly map to the frozen proposal's terminology (e.g., "Candidate future mechanism" for unauthorized extensions).
- **`docs/REVIEWER_GUIDE.md`**: Replaced "strictly masks evidence" with "profile-gates evaluator access to evidence primitives according to EvidenceProfile."
- **`docs/LIMITATIONS.md`**: Appended the three mandatory constraints covering profile gating, test exhaustiveness, and chain reconstruction semantics.
- **`docs/INVARIANTS.md`**: Re-audited and corrected statuses to accurately reflect current regression testing.

## Final Invariant Matrix
- **INV-CPAW-001**: PARTIALLY_ENFORCED
- **INV-CPAW-002**: PARTIALLY_ENFORCED
- **INV-CPAW-003**: ENFORCED
- **INV-CPAW-004**: ENFORCED
- **INV-CPAW-005**: ENFORCED
- **INV-CPAW-006**: PARTIALLY_ENFORCED
- **INV-CPAW-007**: DOCUMENTED_ONLY
- **INV-CPAW-008**: DOCUMENTED_ONLY

## Tracked / Untracked Inventory
**TRACKED_MODIFIED**:
- `README.md`

**UNTRACKED_NEW**:
- `AUTHORS.md`
- `GOVERNANCE.md`
- `_reports/CPAW_V1_2_DOCUMENTATION_BUILD_REPORT.md`
- `docs/GRANT_ALIGNMENT.md`
- `docs/INDEX.md`
- `docs/INVARIANTS.md`
- `docs/LIMITATIONS.md`
- `docs/METHODS.md`
- `docs/RELEASE_CHECKLIST.md`
- `docs/RESULTS.md`
- `docs/REVIEWER_GUIDE.md`
- `docs/SECURITY_AND_CONTAINMENT.md`

## Verification & Integrity
- **Tests**: 6 passed in 0.10s (100% Pass)
- **Reproduction**: ALL_GATES_PASS
- **Canonical Digest Comparison**:
  - `delegation_escape_metrics.csv`: `89ec67d3752b495eacc9d4c84bd392561bc8a8a504e599db82d1dd45ba87196e` (MATCH)
  - `delegation_escape_summary.json`: `4b1a948d75171e2c78e24427f3e1612d8f53afbc36fb9e23682ffc3ce336f5a8` (MATCH)

## Terminology Scan
- A recursive regex scan was performed across all `*.md` files for forbidden phrases.
- **Result**: 0 violations found in active documentation. (1 match found in `CPAW_V1_2_DOCUMENTATION_BUILD_REPORT.md`, which is `VALID_CONTEXT` as it was listing the scan criteria).

## Remaining ENFORCEMENT_GAP Items
- **INV-CPAW-001**: Needs explicit cross-profile/scenario permutation ground-truth invariance test.
- **INV-CPAW-002**: Needs formal taint-tracking or exhaustive fuzzing for cross-profile evidence leakage.
- **INV-CPAW-006**: Needs strict CI gating for governance rules.
- **INV-CPAW-007**: Needs to segregate composite score calculation visually in automated reports.
- **INV-CPAW-008**: None (inherently documented limit).

## Readiness
**READY_FOR_CPAW_V1_3**: Yes. The repository documentation now strictly reflects the verified codebase reality without unsupported ambition.

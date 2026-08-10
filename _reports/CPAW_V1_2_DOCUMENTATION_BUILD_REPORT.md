# CPAW V1-2 Professional Documentation Build Report

**Target Repository**: `C:\gilc.us.mesh.repos\IVAN-PASEV-GITHUB\cross-principal-agent-witness`
**Branch**: `dev/v1-grant-readiness`
**Timestamp**: 2026-08-10

## File Operations
- **Files Created**:
  - `AUTHORS.md`
  - `GOVERNANCE.md`
  - `docs/RESULTS.md`
  - `docs/INVARIANTS.md`
  - `docs/METHODS.md`
  - `docs/LIMITATIONS.md`
  - `docs/SECURITY_AND_CONTAINMENT.md`
  - `docs/REVIEWER_GUIDE.md`
  - `docs/GRANT_ALIGNMENT.md`
  - `docs/INDEX.md`
  - `docs/RELEASE_CHECKLIST.md`
- **Files Modified**:
  - `README.md`
- **Files Deliberately Left Unchanged**:
  - `CLAIM_BOUNDARY.md`, `CITATION.cff`, `CHANGELOG.md`, `docs/ARCHITECTURE.md`, `docs/EXPERIMENT_PROTOCOL.md`, `docs/REPRODUCIBILITY.md`, `docs/ROADMAP.md`, `docs/RELEASE_POLICY.md`, `SECURITY.md`, `CONTRIBUTING.md`
  - `docs/WHITEPAPER.md` (Deferred to CPAW-V1-3)
  - All scientific source, tests, canonical schemas, and result files.

## Evidence & Provenance
- **Machine-Readable Evidence Used**: `results/delegation_escape_summary.json`
- **Result-Table Provenance**: Table data in `docs/RESULTS.md` was procedurally generated and structurally extracted from `profile_summary` and `ablation_summary` inside the canonical JSON. The specific metrics requested (Authority Edge Loc = 0.4 for B2, etc.) were independently cross-checked and found to perfectly match the JSON output.

## Invariant Enforcement Matrix
- **INV-CPAW-001**: ENFORCED
- **INV-CPAW-002**: ENFORCED
- **INV-CPAW-003**: ENFORCED
- **INV-CPAW-004**: ENFORCED
- **INV-CPAW-005**: ENFORCED
- **INV-CPAW-006**: DOCUMENTED_ONLY
- **INV-CPAW-007**: DOCUMENTED_ONLY
- **INV-CPAW-008**: DOCUMENTED_ONLY

**ENFORCEMENT_GAP List**:
- `INV-CPAW-006`, `007`, `008` currently lack algorithmic testing enforcement, relying on administrative policy in `GOVERNANCE.md` and manual assertions.

## Document Scan Results
- **Unsupported/Stale Claims Removed**: `README.md` was rewritten to remove marketing tone, and strictly enforce the `PIPELINE_VALIDATED / SCIENTIFIC_HYPOTHESIS: NOT_ESTABLISHED` boundary without using any forbidden terminology.
- **Unsupported-Phrase Scan**: 0 matches found for ("proven safe", "validated on frontier agents", "production-ready", "universal solution", "public repository at submission", "peer-reviewed prototype").
- **Broken-Link Scan**: All internal documentation pointers in `README.md` and `docs/INDEX.md` resolve to physical files generated in this build phase.

## Verification & Build Integrity
- **Tests**: 6 passed in 0.12s (100% Pass)
- **Reproduction**: ALL_GATES_PASS
- **Baseline vs Post-Build Digests**:
  - `delegation_escape_metrics.csv`: `89ec67d3752b495eacc9d4c84bd392561bc8a8a504e599db82d1dd45ba87196e` (MATCH)
  - `delegation_escape_summary.json`: `4b1a948d75171e2c78e24427f3e1612d8f53afbc36fb9e23682ffc3ce336f5a8` (MATCH)

## Git Workspace Status
**`git diff --stat`**:
```text
 README.md | 85 +++++++++++++++++++--------------------------------------------
 1 file changed, 25 insertions(+), 60 deletions(-)
```
**Current Working-Tree Status**:
Branch `dev/v1-grant-readiness`. Modifications and new files exist locally. Workspace is strictly uncommitted in accordance with the `DO NOT COMMIT` constraint.
`v0.3.0` tag remains perfectly locked to the unchanged baseline. No remote has been configured.

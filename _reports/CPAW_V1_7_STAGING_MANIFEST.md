# CPAW-V1-7 Staging Manifest

## STAGED FILES

### RELEASE_METADATA
- `pyproject.toml`
- `CITATION.cff`
- `CHANGELOG.md`
- `README.md`

### GOVERNANCE
- `AUTHORS.md`
- `GOVERNANCE.md`

### SCIENTIFIC_DOCUMENTATION
- `docs/CLAIM_EVIDENCE_MATRIX.md`
- `docs/CLAIM_EVIDENCE_MATRIX_V1_REVIEW.md`
- `docs/GRANT_ALIGNMENT.md`
- `docs/GRANT_REVIEW_PACKET.md`
- `docs/INDEX.md`
- `docs/LIMITATIONS.md`
- `docs/METHODS.md`
- `docs/NOTATION.md`
- `docs/REFERENCES_VERIFIED.md`
- `docs/RELEASE_CHECKLIST.md`
- `docs/REPOSITORY_STATUS.md`
- `docs/RESULTS.md`
- `docs/REVIEWER_GUIDE.md`
- `docs/SECURITY_AND_CONTAINMENT.md`
- `docs/WHITEPAPER.md`

### ENGINEERING_ASSURANCE
- `docs/INVARIANTS.md`
- `docs/PROFILE_ISOLATION_ASSURANCE.md`
- `docs/REPRODUCIBILITY.md`
- `scripts/check_claim_boundary.py`
- `scripts/check_hygiene.py`
- `scripts/check_links.py`
- `scripts/check_release_readiness.py`
- `scripts/generate_release_report.py`
- `scripts/generate_results_document.py`
- `scripts/run_v1_gate.py`

### TEST
- `tests/test_inv_001_ground_truth.py`
- `tests/test_inv_002_profile_isolation.py`
- `tests/test_schema_contracts.py`

### CI
- `.github/workflows/ci.yml`

### AUDIT_REPORT
- `_reports/CPAW_V1_2_DOCUMENTATION_BUILD_REPORT.md`
- `_reports/CPAW_V1_4_SIMULATED_REVIEW.md`
- `_reports/CPAW_V1_6_HOSTILE_REVIEW_REPORT.md`
- `_reports/CPAW_V1_6_1_FINAL_CLAIM_BOUNDARY_SEAL.md`
- `_reports/CPAW_V1_RELEASE_CONTENT_INVENTORY.md`
- `_reports/CPAW_V1_7_STAGING_MANIFEST.md`
- `docs/METRIC_AUDIT.md`
- `docs/R1_SCENARIO_AUDIT.md`

## EXCLUDED FILES
- `scripts/expand_packet.py` (DEVELOPMENT_ONLY / One-off build script)
- `_reports/LOCAL_RELEASE_READINESS.md` (GENERATED_DYNAMIC_REPORT)

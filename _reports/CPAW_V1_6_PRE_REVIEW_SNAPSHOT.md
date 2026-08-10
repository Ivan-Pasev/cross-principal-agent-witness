# CPAW-V1-6 PRE-REVIEW SNAPSHOT

**Timestamp**: 2026-08-10
**Python Version**: 3.13

## Current Test State
- **Test Count**: 14 tests
- **Tests**:
  - `tests/test_attribution.py` (assumed 6 original)
  - `tests/test_ablation.py` (assumed 1 original)
  - `tests/test_inv_001_ground_truth.py` (1 test)
  - `tests/test_inv_002_profile_isolation.py` (5 tests)
  - `tests/test_schema_contracts.py` (1 test)
- **Canonical Digests**:
  - `results/delegation_escape_metrics.csv` : `89ec67d3752b495eacc9d4c84bd392561bc8a8a504e599db82d1dd45ba87196e`
  - `results/delegation_escape_summary.json`: `4b1a948d75171e2c78e24427f3e1612d8f53afbc36fb9e23682ffc3ce336f5a8`

## Git State
- **Branch**: `dev/v1-grant-readiness`
- **Dirty State**: Modified `README.md`, `.github/workflows/ci.yml`, `docs/REPRODUCIBILITY.md`
- **Untracked**: Numerous `docs/`, `scripts/`, `tests/` and `_reports/` files from V1-2 through V1-5.

## V1 Gate Output
```
--- Running Tests ---
[OK] Tests
--- Running Canonical Reproduction Verification ---
[OK] Canonical Reproduction Verification
--- Running Result Document Freshness ---
[OK] Result Document Freshness
--- Running Claim Scan ---
[OK] Claim Scan
--- Running Markdown Link Check ---
[OK] Markdown Link Check
--- Running Bounded Hygiene Check ---
[OK] Bounded Hygiene Check
--- Running Release Report Generation ---
[OK] Release Report Generation

=== V1 GATE PASSED ===
```

## Release Readiness Report
The `LOCAL_RELEASE_READINESS.md` report exists and confirms all checks PASSED.

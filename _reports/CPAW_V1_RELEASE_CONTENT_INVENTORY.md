# CPAW V1 Release Content Inventory

## RELEASE_REQUIRED
The following files are required for the V1 release and grant submission alignment:
- `docs/WHITEPAPER.md`: The core scientific and methodological documentation.
- `docs/GRANT_REVIEW_PACKET.md`: Alignment surface for grant reviewers.
- `docs/RESULTS.md`: The generated, human-readable rendering of the exact JSON results.
- `docs/METHODS.md`, `docs/ARCHITECTURE.md`, `docs/LIMITATIONS.md`: Scientific integrity documentation.
- `docs/INVARIANTS.md`, `docs/PROFILE_ISOLATION_ASSURANCE.md`: Engineering bounds of the deterministic evaluator.
- `docs/REFERENCES_VERIFIED.md`: Bibliographic support.
- `scripts/check_claim_boundary.py`, `scripts/check_links.py`, `scripts/check_hygiene.py`, `scripts/check_release_readiness.py`, `scripts/run_v1_gate.py`: Automation ensuring the V1 gate never drifts.
- `tests/test_inv_001_ground_truth.py`, `tests/test_inv_002_profile_isolation.py`, `tests/test_schema_contracts.py`: Regression safety testing.

## DEVELOPMENT_ONLY / TEMPORARY (SHOULD_NOT_BE_PUBLISHED)
The following files were created during the V1 preparation as scratch/hostile testing frameworks and must NOT be committed to the V1 tag:
- `scratch_hostile_attacks.py`: The automated vulnerability injector used during CPAW-V1-6.
- `task.md`, `walkthrough.md`, `implementation_plan.md`: LLM workflow orchestration files (these belong to Antigravity context, not Git tracking).

## REPORTS (SHOULD_BE_PUBLISHED)
The following internal workflow reports belong in the repository history for transparency, demonstrating the rigorous, bounded methodology applied to prepare the repository for grant review:
- `_reports/CPAW_V1_2_DOCUMENTATION_BUILD_REPORT.md`
- `_reports/CPAW_V1_2_1_DOCUMENTATION_TRUTH_SEAL.md`
- `_reports/CPAW_V1_3_WHITEPAPER_BUILD_REPORT.md`
- `_reports/CPAW_V1_4_REVIEWER_GRANT_CONTRACT_REPORT.md`
- `_reports/CPAW_V1_5_ENGINEERING_HARDENING_REPORT.md`
- `_reports/LOCAL_RELEASE_READINESS.md`
- `_reports/CPAW_V1_6_PRE_REVIEW_SNAPSHOT.md`
- `_reports/CPAW_V1_6_HOSTILE_REVIEW_REPORT.md`

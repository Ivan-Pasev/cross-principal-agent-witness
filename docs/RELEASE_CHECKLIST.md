# Release Checklist

Prior to tagging any new version, the following must be verified:
- [ ] Canonical tests pass (`python -m pytest -q`)
- [ ] Reproduction verifies cleanly (`python scripts/run_all.py`)
- [ ] Canonical CSV/JSON digests updated if scientific methodology changed
- [ ] CHANGELOG.md updated
- [ ] CLAIM_BOUNDARY.md accurately reflects new capability
- [ ] No credential or secret leakage
- [ ] Invariants remain ENFORCED

## Automated Release Gate
Prior to release, run python scripts/run_v1_gate.py to generate _reports/LOCAL_RELEASE_READINESS.md and verify all structural output contracts, link integrities, claim boundaries, and hygiene scanners.
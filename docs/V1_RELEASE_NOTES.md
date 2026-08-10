# Cross-Principal Agent Witness v1.0.0 — Release Notes

A reproducible research artifact for measuring how identity, provenance, delegated scope, commitment, and revocation evidence affect diagnosis in deterministic cross-principal delegation scenarios.

## Status & Scientific Boundaries

**Scientific Status:** `PIPELINE_VALIDATED` / `SCIENTIFIC_HYPOTHESIS_NOT_ESTABLISHED`

- **No Canonical R1 Scientific Result Changed:** No underlying experimental code, data files, or metrics were modified for this v1.0.0 release.
- **Artifact-Maturity Milestone:** v1.0.0 denotes public repository maturity, reviewer documentation clarity, and automated CI assurance. It does **NOT** establish real-world multi-agent safety efficacy.

## Canonical Result Digests

- `results/delegation_escape_metrics.csv`: `89ec67d3752b495eacc9d4c84bd392561bc8a8a504e599db82d1dd45ba87196e`
- `results/delegation_escape_summary.json`: `4b1a948d75171e2c78e24427f3e1612d8f53afbc36fb9e23682ffc3ce336f5a8`

## Verification Instructions

```bash
python -m pytest -q
python scripts/verify_reproduction.py
python scripts/run_all.py
python scripts/run_v1_gate.py
```

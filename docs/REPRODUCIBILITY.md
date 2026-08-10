# Reproducibility contract

1. Install dependencies.
2. Run `python -m pytest -q`.
3. Run `python -m experiments.delegation_escape`.
4. Compare generated CSV/JSON outputs with committed evidence.
5. Record semantic or metric changes in `CHANGELOG.md`.
6. Never update historical claims without regenerating their evidence files.

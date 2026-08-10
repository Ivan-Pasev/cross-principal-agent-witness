# Cross-Principal Agent Witness

Research prototype for measuring the safety value of delegation, authorization, provenance, commitment, revocation, and outcome evidence in cross-principal AI-agent networks.

## Status

`v0.3.0 POST-FREEZE REPOSITORY-HARDENED RESEARCH PROTOTYPE`

Companion to the frozen Schmidt Sciences 2026 proposal:

**Measuring the Safety Value of Delegation and Action Provenance in Cross-Principal AI Agent Networks**

The submission is frozen separately. Repository evolution does not retroactively modify that record.

## Research question

When AI agents act for different principals and delegate authority through multi-agent chains, which evidence primitives materially improve execution attribution, authority-path reconstruction, invalid-delegation-edge localization, causal diagnosis, and targeted containment?

## Evidence ladder

- `B0` — ordinary events / outcome
- `B1` — + authenticated identity
- `B2` — + provenance
- `B3` — + delegated authority / permission scope
- `B4` — + commitment / task constraint
- `W` — + revocation and full witness evidence

## Hardened semantic separation

- provenance → authority-path reconstruction
- delegation scope → invalid-edge / scope-violation localization
- commitment evidence → declared-task mismatch
- revocation evidence → stale-authority detection

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m experiments.delegation_escape
```

Expected current verification:

```text
6 passed
STATUS: PIPELINE_VALIDATED
SCIENTIFIC_HYPOTHESIS: NOT_ESTABLISHED
```

## Claim boundary

The prototype demonstrates that the evidence conditions, evaluator paths, and ablations are operational. It does **not** establish real-world safety benefit in frontier-agent systems.

## Structure

```text
experiments/   deterministic experiment entry points
scenarios/     cross-principal failure scenarios
witness/       evidence records, evaluator, delegation logic
tests/         semantic and leakage-regression tests
results/       generated CSV / JSON evidence
docs/          reproducibility and frozen-submission linkage
```

## Licensing

No open-source license is granted yet. All rights are reserved pending an explicit licensing decision.

## Repository quality gates

```bash
python scripts/run_all.py
```

This runs the unit-test suite and then regenerates the canonical deterministic outputs and checks them against normalized cross-platform digests in `results/reproduction_manifest.json`.

See `docs/ARCHITECTURE.md`, `docs/RELEASE_POLICY.md`, and `docs/PUBLICATION_CHECKLIST.md`.

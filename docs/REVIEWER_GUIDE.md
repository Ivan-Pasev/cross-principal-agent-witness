# Skeptical Reviewer Guide

This guide provides a hostile-review path to evaluate the claims, limitations, and methodological boundaries of the CPAW R1 instrument.

## 1. What this repository claims
- The ability to deterministically separate authority-path reconstruction (provenance) from invalid-edge localization (permission scope) using the R1 evidence ladder.
- The same underlying incident is evaluated across six evidence conditions (B0-W) and ablation profiles.
- Machine-readable, strictly reproducible execution outputs.

## 2. What it explicitly does not claim
- **No LLM or Frontier-Agent Validation**: R1 uses deterministic evaluators, not LLMs. It does not establish real-world safety for LLM-driven agents.
- **Not a Production Security Protocol**: This is a measurement instrument, not an authorization protocol or formally verified information-flow security system.
- **Not Exhaustively Enforced**: Some invariants (e.g., cross-profile leakage) are `PARTIALLY_ENFORCED` due to missing formal fuzzing.
- **No External Validity**: Five hand-designed synthetic scenarios do not guarantee external generalization.

## 3. Fast reproduction
To verify the canonical results locally, run the following exact commands:
```bash
python -m pytest -q
python scripts/verify_reproduction.py
python scripts/run_all.py
```

## 4. Canonical evidence to inspect
The entire scientific claim boundary rests on these three files:
- `results/delegation_escape_metrics.csv`
- `results/delegation_escape_summary.json`
- `results/reproduction_manifest.json`

## 5. Five questions a skeptical reviewer should ask
1. **Are different evidence profiles evaluating the same incident?** Yes, the `EvidenceProfile` gates visibility over a fixed scenario instance, though formal leakage fuzzing is incomplete (`INV-CPAW-001`).
2. **Can hidden evidence leak into weaker conditions?** The codebase relies on Python conditional logic. It is not formally verified against covert channels (`INV-CPAW-002`).
3. **Is provenance actually distinct from permission scope?** Yes. In R1, `B2` yields 1.0 for path reconstruction but only 0.4 for edge localization, whereas `B3` improves edge localization to 0.8.
4. **Is the composite score being used to inflate scientific claims?** No. It is strictly explicitly documented as a secondary instrumentation diagnostic, not a primary endpoint.
5. **Does R1 justify any statement about frontier agents?** No. R1 tests deterministic scenarios. Frontier safety is a future funded hypothesis.

## 6. Known weaknesses
Please see [LIMITATIONS.md](LIMITATIONS.md) for a comprehensive list of known weaknesses and missing evidence.

## 7. What the funded work would test next
The R1 baseline serves as the foundation for the upcoming grant milestones. Please see [GRANT_ALIGNMENT.md](GRANT_ALIGNMENT.md) and [ROADMAP.md](ROADMAP.md) for the progression to open-weight models, frontier APIs, and adversarial stress.

## 8. Whitepaper
The detailed theoretical model, methodology, and measurement outcomes are synthesized in [WHITEPAPER.md](WHITEPAPER.md).

# Architecture

## Core objects

`Delegation` → `Action` → `Scenario` → `EvidenceProfile` → `Evaluation`

The evaluator is deterministic. Evidence profiles control visibility; they do not mutate the underlying incident.

## Semantic modules

- `witness/models.py` — immutable research records.
- `witness/delegation.py` — delegation traversal, scope attenuation, authority-path reconstruction.
- `witness/evaluator.py` — evidence-conditioned deterministic evaluator.
- `witness/metrics.py` — metric decomposition and aggregate instrumentation diagnostics.
- `witness/profiles.py` — B0/B1/B2/B3/B4/W evidence conditions.
- `scenarios/` — ground-truth incidents, independent of evidence condition.
- `experiments/` — reproducible experiment orchestration.
- `results/` — canonical machine-readable evidence.

## Invariant

Evidence visibility must never leak hidden ground truth into weaker conditions.

# Metric Audit (CPAW V1-6)

## Metric Implementation Review
The metrics calculated in `experiments/delegation_escape.py` evaluate the distance between the evaluator's output and the scenario ground truth.

### Primary Metrics
1. **`incident_accuracy`**: 
   - *Target*: Exact match of `incident` boolean.
   - *Denominator*: 5 (total scenarios).
   - *Vulnerability*: Trivial `False` or `True` guessing would yield a base rate, but the scenarios are balanced (4 True, 1 False).
2. **`execution_attribution`**:
   - *Target*: Match of `responsible_agent` when incident is True.
   - *Vulnerability*: Requires `identity` primitive.
3. **`authority_edge_localization`**:
   - *Target*: Exact match of `authority_edge`.
   - *Vulnerability*: Cannot be guessed randomly. Highly dependent on `delegation_scope`.
4. **`principal_chain_reconstruction`**:
   - *Target*: Exact match of tuple `principal_chain`.
   - *Vulnerability*: Strict exact match. Dependent strictly on `provenance`.
5. **`commitment_localization`** / **`revocation_localization`**:
   - *Target*: Exact match of violation type.
   - *Vulnerability*: Gated directly by `commitment` and `revocation` visibility.

### Composite Score
- *Formula*: Average of the primary metrics.
- *Status*: Secondary diagnostic.
- *Vulnerability*: The composite score effectively blends orthogonal capabilities (e.g., provenance and revocation). It has no primary scientific meaning because an incident response requires *all* relevant data, not a partial average.
- **Assurance**: `generate_results_document.py` correctly relegates it to a "Secondary Instrumentation" section.

## Conclusion
The metric labels accurately match the semantics. The composite score is not treated as a primary scientific endpoint. No `RELEASE_BLOCKER_SCIENTIFIC` defects found in metric calculation.

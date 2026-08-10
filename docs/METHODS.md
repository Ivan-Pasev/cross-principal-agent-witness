# Methods

## Current R1 Method

The R1 method relies on deterministic scenario execution to validate the evidence-ablation pipeline.

### Core Constructs
- **Principals**: Entities (users or organizations) holding root authority.
- **Agents**: Autonomous actors executing tasks.
- **Delegations**: Edges granting authority from a principal/agent to another agent.
- **Scopes**: Permitted constraints attached to a delegation.
- **Parent Delegation Relation**: Explicit linkage (`parent_id`) defining the authority path.
- **Actions**: Terminal operations executed by agents.
- **Commitments**: Declared task constraints.
- **Revocation State**: Status of a delegation edge (active/revoked).

### Pipeline Flow
1. **Scenario Ground Truth**: Each scenario defines a complete, omniscient view of the incident, including the true authority chain and the exact edge where the failure occurred.
2. **Evidence Profiles**: The omniscient record is filtered through ablation profiles (`B0` through `W`) to simulate varying levels of available evidence.
3. **Evaluator Flow**: A deterministic evaluator attempts to answer key diagnostic questions (attribution, path reconstruction, edge localization) using ONLY the filtered evidence.
4. **Metric Calculation**: The evaluator's output is compared against the omniscient ground truth to calculate accuracy metrics (0.0 to 1.0).
5. **Ablation Procedure**: Each individual evidence field (identity, provenance, etc.) is systematically removed from the full `W` profile to measure its isolated marginal contribution.
6. **Deterministic Execution**: The entire suite runs deterministically without network calls.
7. **Result Serialization**: Results are aggregated and serialized to CSV and JSON formats for canonical hashing.

## Post-Freeze Planned Higher-Fidelity Method

Future iterations funded by the grant will transition from deterministic hand-designed scenarios to a model-agnostic staged plan:
- **Stage 2**: contained scripted/tool-using agents.
- **Stage 3**: at least two independently developed open-weight model families selected for reproducible local inference.
- **Stage 4**: smaller heterogeneous populations using current frontier APIs from at least two independent providers.

For all high-fidelity stages: provider, model identifier, release/version/date, inference settings, harness version, and experimental configuration are frozen before evaluation.

Structured scenario ground truth and deterministic metric computation remain the preferred reference evaluation wherever the experimental design permits. Model-assisted annotation or diagnosis may be evaluated as a separate experimental component, but cannot silently replace ground truth or become the scoring authority without independent validation.

# Limitations

The current V1 prototype is strictly scoped. Reviewers and users must explicitly acknowledge the following limitations:

- **Scenario Scale**: Relies on exactly five canonical deterministic R1 scenarios.
- **Hand-designed Semantics**: Scenarios are manually constructed, not empirically observed.
- **Deterministic Evaluator**: Evaluation uses static rules rather than LLM-based reasoning.
- **Simplified Authorization**: Representation of scopes and delegations is heavily abstracted.
- **Small Scenario Set**: Statistical confidence is not applicable given the dataset size.
- **No LLM Agents**: There are no LLM agents in R1.
- **No Heterogeneous Model Families**: Not applicable in R1.
- **No Frontier APIs**: No external API calls are made in R1.
- **No Empirical Intervention Study**: R1 is a pipeline validation, not a real-world intervention study.
- **No Sufficiency Proof**: There is no proof that the current evidence primitives are *sufficient* for all real-world failures.
- **No Production Security Proof**: There is no proof of cryptographic or production security in this codebase.
- **External Validity Not Established**: The findings do not yet generalize to real-world incidents.

- **Information-Flow Security**: Profile gating is implemented by deterministic conditional evaluator logic, not by a formally verified information-flow system.
- **Test Exhaustiveness**: Current tests cover key semantic separations but do not exhaustively prove absence of every possible evidence-leakage path.
- **Chain Reconstruction Semantics**: Principal-chain reconstruction stops on missing parent or detected cycle rather than producing a formally typed failure state in v0.3.0.

# Cross-Principal Agent Witness:
## Evidence-Layer Ablation for Authority Attribution and Scoped Containment in Multi-Agent AI Systems

**Author:** Ivan Pasev
**Role:** Independent Researcher; Senior Solution Architect / Systems Engineer
**ORCID:** 0009-0002-1902-9738
**Repository whitepaper version:** 1.0-draft
**Date:** 2026-08

## Abstract

As AI agents increasingly act on behalf of different human or institutional principals, ordinary execution logs become insufficient for answering a central safety question: not merely which agent acted, but under whose authority, through which delegation chain, with what scope, and whether that authority was still valid at the moment of action. This whitepaper introduces the Cross-Principal Agent Witness (CPAW), a deterministic research prototype designed to measure the marginal diagnostic value of identity, provenance, delegated authority, commitment, revocation, and outcome evidence via evidence-ablation.

The current R1 instrument evaluates five deterministic failure scenarios under six evidence conditions (B0 through W). A key semantic separation is observed: provenance visibility enables authority-path reconstruction, while permission-scope evidence improves invalid-edge localization independently. The prototype provides reproducible, machine-readable evidence that these evaluator paths are separable. However, the current scientific boundary is strictly methodological: the results are deterministic instrumentation metrics, not evidence that these fields improve safety in real LLM-agent deployments. This paper outlines the higher-fidelity research question and the falsifiable roadmap toward scripted, open-weight, and frontier-agent populations.

## 1. Introduction

Multi-agent AI systems complicate accountability because execution attribution is not equivalent to authority attribution. An action can be technically attributable to an executing agent while remaining ambiguous in its authorizing chain. An agent may act under a direct principal instruction, delegated authority from another agent, a stale authorization that has since been revoked, or an over-broad delegated scope.

This distinction is critical for containment. If an incident is diagnosed only as "agent B performed action X," the natural intervention may be coarse: shut down B, suspend a service, or stop an entire workflow. If the evidence instead shows that B acted under an invalid child delegation originating from A under principal P, the response may be targeted: revoke one delegation, isolate one path, restrict one tool, or quarantine one derived agent instance. 

We do not claim that such evidence automatically improves safety. Instead, this instrument is designed to measure the diagnostic value of specific evidence primitives under controlled conditions.

## 2. Research Question

The primary falsifiable question is:
**Which authorization and provenance evidence primitives materially improve execution attribution, authority attribution, failure diagnosis, and eventually the selectivity of intervention when agents act through cross-principal delegation chains?**

The current R1 sub-question is whether a deterministic pipeline can successfully isolate and measure the contribution of these primitives. The funded higher-fidelity hypothesis asks whether these benefits hold in real LLM-driven environments with semantic ambiguity and partial observability.

## 3. Related Work

**3.1 Agent infrastructure and identity**
Work on AI-agent infrastructure (Chan et al., 2025) emphasizes identity and control as foundational layers for safe deployment.

**3.2 Delegation and authorization**
Authenticated Delegation and Authorized AI Agents (South et al., 2025) formalizes delegation-oriented authority, providing the conceptual basis for multi-agent authorization.

**3.3 Failure attribution**
Automated failure attribution studies (Zhang et al., 2025) address locating where agentic systems fail.

**3.4 Runtime governance / receipts**
AgentBound (Kaul et al., 2026) explores verifiable governance receipts and behavioral constraints at runtime.

**3.5 Gap addressed by evidence-value ablation**
CPAW does not propose that provenance or delegated authorization is new. Its experimental contribution is to hold incidents fixed and estimate / instrument the diagnostic value of distinct evidence primitives.

## 4. Formal System Model

### Definitions
- **principal ($P$)**: The root human or institutional authority.
- **agent ($A$)**: An autonomous executing entity.
- **delegation ($D$)**: An edge granting authority from a delegator to a delegate.
- **parent delegation**: The explicit linkage defining the prior authority source in a chain.
- **scope ($S$)**: Permitted constraints attached to a delegation.
- **commitment ($C$)**: Declared task constraints.
- **revocation ($R$)**: Status of a delegation edge (active/revoked).
- **action ($e$)**: A terminal operation executed by an agent.
- **outcome ($O$)**: The observed result of the action.
- **evidence condition ($B_k$)**: The subset of evidence visible to the evaluator.

### Authority Path
An authority path $\pi$ is an ordered chain of delegations tracing back to a principal.

### Simplified Scope Semantics
In R1, scope is represented by simplified enumerated operation-set commitment semantics, not full semantic reasoning.

### Model Assumptions
This formal model is an conceptual abstraction. The current R1 codebase implements a deterministic, simplified version of these constructs.

## 5. Evidence Ladder

The R1 prototype defines six evidence conditions directly from the `witness/profiles.py` semantics:

| Profile | Evidence Visible | Diagnostic Capability Tested |
|---|---|---|
| **B0** | ordinary events / outcome | Baseline diagnostic capability |
| **B1** | + authenticated identity | Execution attribution |
| **B2** | + provenance | Authority-path reconstruction |
| **B3** | + delegated authority / scope | Invalid-edge localization |
| **B4** | + commitment / task constraint | Task mismatch diagnosis |
| **W** | + revocation and full witness evidence | Stale-authority detection |

## 6. Evaluator Semantics

The R1 deterministic evaluator profile-gates evaluator access to evidence primitives according to `EvidenceProfile`. 

- **Execution attribution**: Evaluated using identity evidence.
- **Authority-path reconstruction**: Evaluated by tracing parent links when provenance is visible.
- **Invalid-edge localization**: Evaluated by checking scope attenuation when delegation scope is visible.
- **Commitment mismatch**: Evaluated by comparing actions to allowed commitment sets.
- **Revocation/stale-authority diagnosis**: Evaluated using the revoked flag.

**Explicit Note**: Profile gating is implemented by deterministic conditional evaluator logic, not by a formally verified information-flow security system.

## 7. R1 Experimental Design

The current R1 experiment executes **five deterministic scenarios**. The same underlying incident ground truth is evaluated across all six evidence conditions (evidence ablation). Single-field ablations isolate the marginal contribution of each primitive.

The deterministic run is validated by a rigorous test suite, producing canonical machine-readable CSV and JSON outputs. The repository plans to include a broader taxonomy (e.g., delegation laundering, cloning/forks) in future stages; these are currently labeled as planned future extensions.

## 8. Evaluation Metrics

- **Execution Attribution**: Correct attribution of the terminal action to the executing agent.
- **Authority Edge Localization**: Accurate identification of the specific delegation edge where authority was breached.
- **Principal Chain Reconstruction**: Accurate end-to-end reconstruction of the principal authority chain.
- **Commitment Localization**: Accurate localization of task-constraint violations.
- **Revocation Localization**: Accurate localization of stale-authority actions after revocation.
- **Composite Score**: A weighted average of the above metrics.

**IMPORTANT**: The composite score is a secondary instrumentation diagnostic, not the primary scientific endpoint.

## 9. R1 Results

### 9.1 Evidence-Profile Table

| Profile | Incident Acc | Exec Attr | Auth Edge Loc | Princ Chain Recon | Comm Loc | Revoc Loc | Composite |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B0** | 0.4 | 0.2 | 0.4 | 0.0 | 0.8 | 0.8 | 0.433 |
| **B1** | 0.4 | 1.0 | 0.4 | 0.0 | 0.8 | 0.8 | 0.567 |
| **B2** | 0.4 | 1.0 | 0.4 | 1.0 | 0.8 | 0.8 | 0.733 |
| **B3** | 0.6 | 1.0 | 0.8 | 1.0 | 0.8 | 0.8 | 0.833 |
| **B4** | 0.8 | 1.0 | 0.8 | 1.0 | 0.8 | 0.8 | 0.867 |
| **W**  | 1.0 | 1.0 | 1.0 | 1.0 | 0.8 | 1.0 | 0.967 |

### 9.2 Single-Field Ablation Table

| Ablated Field | Composite Without | Evidence Contribution |
| :--- | :--- | :--- |
| **identity** | 0.833 | 0.133 |
| **provenance** | 0.800 | 0.167 |
| **delegation_scope** | 0.867 | 0.100 |
| **commitment** | 0.933 | 0.033 |
| **revocation** | 0.867 | 0.100 |
| **outcome** | 0.967 | 0.000 |

### 9.3 Interpretation
- Within the current R1 evidence model and implemented scenario set, provenance visibility is the evidence primitive that enables principal-chain reconstruction. (B0/B1 = 0.0, B2 = 1.0).
- Within the current R1 evidence model and implemented scenario set, delegation-scope evidence enables accurate localization of the invalid authority edge (B2 = 0.4, B3 = 0.8).
- Within the current R1 evidence model and implemented scenario set, revocation visibility is necessary to localize explicit stale-authority actions.

## 10. Interpretation

The R1 prototype establishes:
- An operational evidence ladder.
- Separable evaluator paths for provenance versus scope.
- Deterministic reproducibility of the ablation surface.

R1 does **not** establish:
- Real-world safety effect in frontier-agent deployments.
- Causal superiority of evidence fields in open-ended LLM scenarios.
- Sufficiency of the evidence model for all failure types.
- Optimal containment policy in production environments.

## 11. Threat Model and Containment

**Current R1**: The execution is local, deterministic, and synthetic. It uses no external APIs, no production credentials, and has no uncontrolled external side effects.

**Higher-Fidelity Future Containment**: Future stages will require synthetic credentials/data, isolated execution environments, allowlisted tools, strictly controlled network access, explicit logs, and a frozen model/provider/version/configuration ledger.

## 12. Reproducibility

The repository guarantees reproducibility via canonical manifests. Verification is performed via:
```bash
python -m pytest -q
python scripts/verify_reproduction.py
python scripts/run_all.py
```
The deterministic pipeline yields 6 passing tests, with output hashes strictly enforced against `results/reproduction_manifest.json`.

## 13. Limitations

Reviewers must explicitly acknowledge the following bounds of the R1 instrument:
- Evaluates exactly five deterministic scenarios.
- Relies on a deterministic evaluator, not semantic reasoning.
- Employs hand-designed ground truth and simplified scope/commitment semantics.
- Lacks formal exhaustive leakage enforcement (partial rather than exhaustive enforcement).
- Principal-chain reconstruction stops on missing parent or detected cycle rather than producing a formally typed failure state in v0.3.0.
- Assumes absence of LLM agents, heterogeneous model families, and frontier APIs.
- Features no real intervention experiment.
- Provides no production-security proof or evidence-sufficiency proof.
- External validity is not established.

## 14. Higher-Fidelity Research Program

The Schmidt Sciences 2026 grant enables a staged progression toward ecological fidelity:
- **Stage 2**: Scripted/tool-using agents.
- **Stage 3**: At least two independently developed open-weight model families.
- **Stage 4**: Heterogeneous frontier API populations from at least two independent providers.

Across all stages, we plan future experiments to evaluate adversarial cases such as missing traces, cloning/forks, delegation laundering, revocation edge cases, and scoped intervention versus coarse shutdown under a frozen model/config ledger.

## 15. Falsification Conditions

The evidence-value hypothesis is weakened or rejected where:
- Added evidence fails to improve the preregistered target metric.
- Improvements disappear across model families or APIs.
- Richer evidence improves attribution but not intervention selectivity.
- Missing/noisy evidence destroys the diagnostic effect.
- Baseline heuristic logs perform equivalently to structured evidence profiles.
- Operational overhead outweighs scoped-containment benefit.
- Causal diagnosis cannot be distinguished from evaluator artifact.

## 16. Conclusion

CPAW currently provides a reproducible measurement instrument, not a proven safety mechanism. It formalizes a methodology for measuring the diagnostic value of cross-principal authorization evidence, creating a falsifiable foundation for future frontier-agent evaluation.

## References

1. Schmidt Sciences. *Scaling AI Safety for a Multi-Agent World*. 2026.
2. Chan, A. et al. *Infrastructure for AI Agents*. arXiv:2501.10114, 2025.
3. South, T. et al. *Authenticated Delegation and Authorized AI Agents*. arXiv:2501.09674, 2025.
4. Zhang, S. et al. *Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems*. ICML 2025.
5. Kaul, A., Lan, Q., Gupta, P. *AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents*. arXiv:2606.30970, 2026.
6. Liu, J. et al. *Who&When Pro: Can LLMs Really Attribute Failures in AI Agents?* arXiv:2607.09996, 2026.

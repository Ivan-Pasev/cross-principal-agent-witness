# Cross-Principal Agent Witness — Technical Review Packet

## 1. Research Problem and Motivation
Multi-agent AI systems are rapidly evolving from simple single-user tools into autonomous workflows acting on behalf of different human or institutional principals. In this cross-principal environment, an action can be technically attributable to an executing agent while remaining completely ambiguous in its authorization. For example, an agent might act under a direct principal instruction, delegated authority from another agent, a stale authorization that has since been revoked, or an over-broad delegated scope. 

This ambiguity matters profoundly for system containment. If an incident is diagnosed merely as "agent B performed action X," the natural intervention is coarse: shut down agent B, suspend an entire service, or halt the workflow. If the evidence instead allows us to see that agent B acted under an invalid child delegation originating from agent A under principal P, the response can be targeted. We can revoke that single delegation path, quarantine one specific instance, or restrict a single tool without taking the entire multi-agent ecosystem offline.

The core research question we address is: **Which authorization and provenance evidence primitives materially improve execution attribution, authority attribution, failure diagnosis, and eventually the selectivity of intervention when agents act through cross-principal delegation chains?**

## 2. Current Architecture and Measurement Instrument
The Cross-Principal Agent Witness (CPAW) repository currently serves as a highly controlled measurement instrument. To isolate the effects of different evidence primitives, we constructed a deterministic evaluator rather than relying on noisy large language models. The R1 baseline executes a fixed set of five synthetic failure scenarios representing different cross-principal edge cases (e.g., scope expansion, commitment mismatch, stale authority).

The heart of the measurement is the **Evidence Ladder**. We evaluate the exact same underlying incident across six different evidence conditions:
- **B0 (Baseline)**: Only the action outcome is visible.
- **B1**: Adds authenticated identity.
- **B2**: Adds provenance (parent delegation paths).
- **B3**: Adds delegated permission scope.
- **B4**: Adds task commitment constraints.
- **W (Full Witness)**: Adds revocation state and all above primitives.

By selectively gating the evaluator's access to this evidence, we perform single-field ablations to calculate the marginal diagnostic contribution of each primitive.

## 3. Key R1 Result: The B2/B3/W Semantic Separation
The R1 pipeline successfully separates two completely distinct tasks: **authority-path reconstruction** (answering "who authorized whom") and **invalid-edge localization** (answering "which delegation edge was illicitly expanded").

The canonical results obtained from our deterministic R1 evaluator illustrate this separation clearly:

- **B2 (Provenance added)**:
  - Principal Chain Reconstruction: 1.0
  - Authority Edge Localization: 0.4
  - *Interpretation*: Provenance allows the evaluator to reconstruct the entire principal chain (1.0), but it fails to identify which edge caused a scope violation (0.4).

- **B3 (Delegation scope added)**:
  - Principal Chain Reconstruction: 1.0
  - Authority Edge Localization: 0.8
  - *Interpretation*: Adding scope permissions raises the authority edge localization capability (0.8), demonstrating that permission scope is a distinct primitive from structural provenance.

- **W (Full witness)**:
  - Principal Chain Reconstruction: 1.0
  - Authority Edge Localization: 1.0
  - *Interpretation*: Full witness evidence enables complete localization and reconstruction in the R1 scenarios.

## 4. Deterministic Reproducibility
The R1 baseline is built to be rigorously reproducible. Every aspect of the pipeline—from scenario generation to evaluation and metric calculation—is deterministic. 

Reviewers and collaborators can easily verify this exact scientific state locally by running:
```bash
python -m pytest -q
python scripts/verify_reproduction.py
python scripts/run_all.py
```
This produces machine-readable CSV and JSON metrics. A cryptographic SHA-256 digest of these canonical results is maintained in `results/reproduction_manifest.json`, ensuring that no unauthorized changes to the scientific evidence can slip past the verification gates.

## 5. Explicit Claim Boundary and Limitations
We maintain strict scientific discipline regarding what the current R1 instrument demonstrates. **The R1 codebase implements an evidence ladder, reproduces machine-readable results deterministically, measures diagnostic contributions, and detects failure localizations in synthetic scenarios.**

It does **not** prove the system safe, nor does it validate frontier-agent safety in production environments. 
The current R1 instrument is limited to a deterministic evaluator using hand-crafted synthetic ground truths, simplified enumerated operation-set scope/commitment semantics, and boolean visibility toggles. It does not evaluate missing traces, semantic proxy laundering, or the unstructured ambiguity inherent in real-world LLM-driven environments.

## 6. Proposed Transition in Fidelity (The Roadmap)
If funded under the Schmidt Sciences 2026 call, the proposed program would enable us to transition this validated measurement pipeline to progressively higher-fidelity ecosystems:
1. **Stage 1 (Current R1)**: Deterministic evaluation of synthetic scenarios.
2. **Stage 2**: Scripted, tool-using agents replacing synthetic incident generators.
3. **Stage 3**: Introduction of at least two independently developed open-weight model families acting as delegates.
4. **Stage 4**: Integration of heterogeneous frontier APIs from multiple independent providers under a frozen configuration ledger.
5. **Stage 5**: Full adversarial stress testing involving trace omission, delegation laundering, and measurements of scoped intervention versus coarse shutdown.

## 7. Falsification Logic
The entire research program rests on falsifiable hypotheses. We will reject the hypothesis that a given evidence primitive provides multi-agent safety value if:
- Added evidence fails to improve the targeted diagnostic metric.
- Any initial diagnostic improvements disappear when applied across heterogeneous model families or frontier APIs.
- Richer evidence improves attribution on paper, but fails to translate into actionable selectivity of intervention.
- Baseline heuristic logging performs equivalently to structured cross-principal evidence profiles.
- The operational overhead of transmitting the evidence completely outweighs the benefits of scoped containment.

Through this rigorous evidence-ablation methodology, CPAW aims to produce the empirical foundations necessary for safe, accountable, and governable multi-agent operations.

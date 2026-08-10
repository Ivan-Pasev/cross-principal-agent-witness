# Simulated Review (CPAW V1-4)

## PERSONA A: Multi-agent safety researcher
- **Strongest aspect**: The ablation of evidence fields explicitly isolates provenance from permission scope.
- **Biggest concern**: The deterministic evaluator assumes perfect semantic visibility, which LLMs do not have.
- **Misleading wording**: None detected. R1 boundaries are explicitly marked.
- **Missing evidence**: Performance with open-weights and real LLM function-calling traces.
- **Likely reviewer question**: Will this scale to heterogeneous models without structural collapse?
- **Current docs answer it**: Yes, explicitly marked as a Stage 3/4 hypothesis in `GRANT_ALIGNMENT.md` and `WHITEPAPER.md`.
- **Release-blocking issue**: NO

## PERSONA B: Systems/security engineer
- **Strongest aspect**: Total local reproducibility and canonical result digests.
- **Biggest concern**: No formal verification of information leakage across profiles (conditional logic vs structural typing).
- **Misleading wording**: None. Profile gating is correctly labeled as logic rather than information-flow security.
- **Missing evidence**: Fuzzing for cross-profile leakage.
- **Likely reviewer question**: Can evidence fields be spoofed by a delegated agent?
- **Current docs answer it**: Yes, `SECURITY_AND_CONTAINMENT.md` and `LIMITATIONS.md` cover the synthetic cryptographic assumption.
- **Release-blocking issue**: NO

## PERSONA C: Grant reviewer with 10 minutes
- **Strongest aspect**: The `GRANT_REVIEW_PACKET.md` immediately surfaces the key R1 metric separation and future hypotheses.
- **Biggest concern**: Wondering if this repo was submitted as a public URL during the grant cycle.
- **Misleading wording**: None. `REPOSITORY_STATUS.md` and `GRANT_ALIGNMENT.md` explicitly state it is a post-freeze companion and was NOT public at submission.
- **Missing evidence**: N/A for R1 scope.
- **Likely reviewer question**: Is this production ready?
- **Current docs answer it**: Yes, it explicitly states it is a measurement instrument, not a safety mechanism.
- **Release-blocking issue**: NO

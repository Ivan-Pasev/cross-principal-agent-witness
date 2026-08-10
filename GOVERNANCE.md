# Governance

This repository adheres to the following governance model to maintain the integrity of the scientific claims and baseline validation.

## Invariant
`SUBMISSION_FREEZE_v14 != LIVING_REPOSITORY`

Repository evolution must never retroactively modify or obscure the frozen submission record. 

## Scientific Claim Review
Any modification to the fundamental scientific claims, boundaries, or limitations requires explicit review by the Scientific Lead (Ivan Pasev).

## Canonical R1 Result Changes
Changes that alter the canonical R1 results require:
- methodological explanation
- regenerated evidence
- tests
- reproduction manifest
- changelog
- claim-boundary review
- explicit new version

## Post-Freeze Scientific Deltas
Any new scientific experiments, features, or capability expansions that are not part of the `v0.3.0` baseline must be clearly segregated and marked as post-freeze scientific deltas.

## Documentation-Only Changes
Documentation, grammar, and formatting corrections that do not alter the methodology, results, or claims can be merged continuously without a version bump.

## Experiment Versioning & Release Approval
All releases (including release candidates like `v1.0.0-rc.1`) must pass the complete set of automated gates and canonical reproduction tests. Final release approval is retained by the Scientific Lead.

## Collaborator Contributions
Contributors must adhere to the claim boundaries and cannot upgrade the maturity claims of the repository (e.g., claiming real-world LLM safety) without explicit validation and lead approval.

## Security-Sensitive Changes
Modifications to `SECURITY.md`, `THREAT_MODEL.md`, or the execution containment envelope require rigorous hostile review.

## License Changes
No open-source license is granted yet. License changes require explicit authorization from the repository owner.

## Remote/Publication Approval
Pushing to a public remote repository or publishing the repository state requires a final local v1 release seal and explicit operator approval.

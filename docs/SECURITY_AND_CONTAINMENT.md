# Security and Containment

## Current R1

The current prototype operates entirely locally and poses no external risks:
- local deterministic execution;
- no production credentials;
- no private keys;
- no external API requirement;
- no ledger/blockchain requirement;
- no uncontrolled network side effects;
- synthetic research scenarios.

## Future Higher-Fidelity Requirements

When transitioning to the planned post-freeze LLM agent implementation, the following containment policies will be strictly enforced:
- synthetic credentials and data;
- isolated workspace;
- allowlisted tools;
- controlled network access;
- explicit event logging;
- model/provider/version freeze;
- no uncontrolled external actions.

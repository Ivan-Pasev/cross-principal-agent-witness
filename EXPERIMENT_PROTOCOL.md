# Experiment Protocol — Delegation Escape 001

## Objective

Validate the experimental pipeline used to compare evidence conditions and evidence ablations in deterministic multi-principal authorization scenarios.

## Evidence conditions

| Condition | Identity | Provenance | Delegation scope | Commitment | Revocation | Observed result |
|---|---:|---:|---:|---:|---:|---:|
| B0 | No | No | No | No | No | Yes |
| B1 | Yes | No | No | No | No | Yes |
| B2 | Yes | Yes | No | No | No | Yes |
| B3 | Yes | Yes | Yes | No | No | Yes |
| B4 | Yes | Yes | Yes | Yes | No | Yes |
| W | Yes | Yes | Yes | Yes | Yes | Yes |

## Deterministic scenarios

1. delegated scope escape;
2. valid delegated action;
3. delegation laundering / scope expansion;
4. action under revoked delegation;
5. commitment/action mismatch.

## Prototype metrics

- incident classification accuracy;
- execution attribution accuracy;
- authority-edge localization accuracy;
- principal-chain reconstruction accuracy;
- commitment-violation localization accuracy;
- revocation-violation localization accuracy;
- a simple composite instrumentation score (prototype diagnostic only).

These metrics validate instrumentation only. Frontier-agent safety effects require the funded experiments.

## Reproducibility

The experiment is deterministic and has no external API, cloud, model, ledger, or credential dependency.

**Note:** v0.1 treats the observed action result as available to all logging conditions. Cryptographic binding of action-to-outcome correspondence is part of the funded stress-test programme, not a claimed result of this deterministic prototype.

## Grant-facing analysis

The funded study does not use the prototype composite as the primary scientific endpoint. It reports metric-specific paired changes under single-field ablation (for example, authority-edge localization with versus without delegation-scope evidence), together with uncertainty.

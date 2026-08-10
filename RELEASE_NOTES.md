# v0.1.0-rfp — Research Prototype Candidate

Frozen for grant-feasibility evidence.

Includes:

- typed delegation/action/scenario objects;
- scope-attenuation invariant;
- five deterministic failure/authorization scenarios;
- six evidence conditions B0–B4/W;
- full-witness evidence ablation;
- unit tests;
- machine-readable CSV/JSON results;
- explicit claim boundary and threat model.

No frontier-model experiments are claimed in this release.


# Methodological Hardening R2

Provenance now reconstructs the full authority path independently of permission-scope evidence; delegation-scope evidence remains responsible for invalid-edge localization.

Verification: **6 passed**.

This change was made before submission freeze because it reduces the chance that the prototype overstates evidence quality. All generated CSV/JSON outputs in this capsule were regenerated after the change.

from __future__ import annotations

from dataclasses import asdict
from typing import Iterable

from .models import Evaluation, Scenario


def score(scenario: Scenario, evaluation: Evaluation) -> dict[str, float]:
    incident_ok = float(evaluation.incident_detected == scenario.expected_incident)

    if scenario.expected_responsible_agent is None:
        exec_ok = float(evaluation.responsible_agent is None or not scenario.expected_incident)
    else:
        exec_ok = float(evaluation.responsible_agent == scenario.expected_responsible_agent)

    if scenario.expected_authority_edge is None:
        edge_ok = float(evaluation.authority_edge is None)
    else:
        edge_ok = float(evaluation.authority_edge == scenario.expected_authority_edge)

    principal_ok = float(evaluation.principal_chain == scenario.expected_principal_chain)

    expected_commitment = scenario.expected_violation_type == "commitment"
    commitment_ok = float(evaluation.commitment_violation == expected_commitment)

    expected_revocation = scenario.expected_violation_type == "revocation"
    revocation_ok = float(evaluation.revocation_violation == expected_revocation)

    composite = (incident_ok + exec_ok + edge_ok + principal_ok + commitment_ok + revocation_ok) / 6.0
    return {
        "incident_accuracy": incident_ok,
        "execution_attribution": exec_ok,
        "authority_edge_localization": edge_ok,
        "principal_chain_reconstruction": principal_ok,
        "commitment_localization": commitment_ok,
        "revocation_localization": revocation_ok,
        "composite": composite,
    }


def aggregate(rows: Iterable[dict[str, float]]) -> dict[str, float]:
    rows = list(rows)
    keys = rows[0].keys()
    return {k: sum(r[k] for r in rows) / len(rows) for k in keys}

from __future__ import annotations

from .delegation import find_delegation_for_agent, find_scope_expansion, principal_chain
from .models import EvidenceProfile, Evaluation, Scenario


def evaluate(scenario: Scenario, profile: EvidenceProfile) -> Evaluation:
    leaf = find_delegation_for_agent(scenario.delegations, scenario.action.agent)

    responsible_agent = scenario.action.agent if profile.identity else None
    authority_edge = None
    principal_path: tuple[str, ...] = ()
    commitment_violation = False
    revocation_violation = False
    incident = False

    # Ordinary event records can expose an externally observable failure/result,
    # but cannot infer hidden authorization or commitment violations.
    if profile.outcome:
        incident = scenario.observable_failure

    # Provenance can reconstruct the authority path without revealing permission scope.
    if profile.provenance and leaf is not None:
        principal_path = principal_chain(scenario.delegations, leaf)

    if profile.delegation_scope and leaf is not None:
        scope_expansion = find_scope_expansion(scenario.delegations)
        action_out_of_scope = scenario.action.operation not in leaf.scope
        if scope_expansion:
            authority_edge = scope_expansion
            incident = True
        elif action_out_of_scope:
            authority_edge = leaf.delegation_id
            incident = True

    if profile.commitment and scenario.commitment is not None:
        commitment_violation = scenario.action.operation not in scenario.commitment_allows
        incident = incident or commitment_violation

    if profile.revocation and leaf is not None:
        revocation_violation = leaf.revoked
        if revocation_violation:
            authority_edge = leaf.delegation_id
            incident = True

    return Evaluation(
        incident_detected=incident,
        responsible_agent=responsible_agent,
        authority_edge=authority_edge,
        principal_chain=principal_path,
        commitment_violation=commitment_violation,
        revocation_violation=revocation_violation,
    )

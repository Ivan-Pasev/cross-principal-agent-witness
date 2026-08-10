from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Optional, Tuple


@dataclass(frozen=True)
class Delegation:
    delegation_id: str
    principal: str
    delegator: str
    delegate: str
    scope: FrozenSet[str]
    parent_id: Optional[str] = None
    revoked: bool = False


@dataclass(frozen=True)
class Action:
    agent: str
    operation: str
    resource: str


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    description: str
    delegations: Tuple[Delegation, ...]
    action: Action
    commitment: Optional[str]
    commitment_allows: FrozenSet[str]
    observable_failure: bool
    expected_incident: bool
    expected_violation_type: Optional[str]
    expected_responsible_agent: Optional[str]
    expected_authority_edge: Optional[str]
    expected_principal_chain: Tuple[str, ...]


@dataclass(frozen=True)
class EvidenceProfile:
    name: str
    identity: bool
    provenance: bool
    delegation_scope: bool
    commitment: bool
    revocation: bool
    outcome: bool


@dataclass(frozen=True)
class Evaluation:
    incident_detected: bool
    responsible_agent: Optional[str]
    authority_edge: Optional[str]
    principal_chain: Tuple[str, ...]
    commitment_violation: bool
    revocation_violation: bool

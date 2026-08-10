from .models import EvidenceProfile


PROFILES = {
    "B0": EvidenceProfile("B0", identity=False, provenance=False, delegation_scope=False, commitment=False, revocation=False, outcome=True),
    "B1": EvidenceProfile("B1", identity=True, provenance=False, delegation_scope=False, commitment=False, revocation=False, outcome=True),
    "B2": EvidenceProfile("B2", identity=True, provenance=True, delegation_scope=False, commitment=False, revocation=False, outcome=True),
    "B3": EvidenceProfile("B3", identity=True, provenance=True, delegation_scope=True, commitment=False, revocation=False, outcome=True),
    "B4": EvidenceProfile("B4", identity=True, provenance=True, delegation_scope=True, commitment=True, revocation=False, outcome=True),
    "W": EvidenceProfile("W", identity=True, provenance=True, delegation_scope=True, commitment=True, revocation=True, outcome=True),
}


def ablate(profile: EvidenceProfile, primitive: str) -> EvidenceProfile:
    fields = {
        "identity": profile.identity,
        "provenance": profile.provenance,
        "delegation_scope": profile.delegation_scope,
        "commitment": profile.commitment,
        "revocation": profile.revocation,
        "outcome": profile.outcome,
    }
    if primitive not in fields:
        raise KeyError(primitive)
    fields[primitive] = False
    return EvidenceProfile(name=f"{profile.name}-minus-{primitive}", **fields)

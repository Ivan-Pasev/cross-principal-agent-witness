from scenarios import build_scenarios
from witness.evaluator import evaluate
from witness.profiles import PROFILES


def test_full_witness_localizes_scope_escape():
    scenario = next(s for s in build_scenarios() if s.scenario_id == "scope_escape")
    ev = evaluate(scenario, PROFILES["W"])
    assert ev.incident_detected
    assert ev.responsible_agent == "B"
    assert ev.authority_edge == "d2"
    assert ev.principal_chain == ("P1", "A", "B")


def test_revocation_requires_revocation_evidence_for_specific_localization():
    scenario = next(s for s in build_scenarios() if s.scenario_id == "revoked_authority")
    b4 = evaluate(scenario, PROFILES["B4"])
    w = evaluate(scenario, PROFILES["W"])
    assert not b4.revocation_violation
    assert w.revocation_violation
    assert w.authority_edge == "d2"


def test_provenance_reconstructs_authority_chain_without_scope_evidence():
    scenario = next(s for s in build_scenarios() if s.scenario_id == "scope_escape")
    ev = evaluate(scenario, PROFILES["B2"])
    assert ev.principal_chain == ("P1", "A", "B")
    assert ev.authority_edge is None

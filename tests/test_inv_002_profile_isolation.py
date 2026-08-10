import dataclasses
from scenarios.delegation_cases import build_scenarios
from witness.evaluator import evaluate
from witness.profiles import PROFILES

def test_inv_cpaw_002_identity_isolation():
    """Identity is hidden in B0. Perturbing agent identity should not affect B0 output."""
    scenarios = build_scenarios()
    profile = PROFILES["B0"]
    for scenario in scenarios:
        baseline_result = evaluate(scenario, profile)
        
        # Perturb hidden primitive: identity
        perturbed_action = dataclasses.replace(scenario.action, agent="FAKE_AGENT")
        perturbed_scenario = dataclasses.replace(scenario, action=perturbed_action)
        
        perturbed_result = evaluate(perturbed_scenario, profile)
        assert baseline_result == perturbed_result

def test_inv_cpaw_002_provenance_isolation():
    """Provenance is hidden in B0, B1. Perturbing parent_id should not affect B1 output."""
    scenarios = build_scenarios()
    profile = PROFILES["B1"]
    for scenario in scenarios:
        baseline_result = evaluate(scenario, profile)
        
        # Perturb hidden primitive: provenance
        new_delegations = tuple(dataclasses.replace(d, parent_id="FAKE_PARENT") for d in scenario.delegations)
        perturbed_scenario = dataclasses.replace(scenario, delegations=new_delegations)
        
        perturbed_result = evaluate(perturbed_scenario, profile)
        assert baseline_result == perturbed_result

def test_inv_cpaw_002_delegation_scope_isolation():
    """Delegation scope is hidden in B0, B1, B2. Perturbing scope should not affect B2 output."""
    scenarios = build_scenarios()
    profile = PROFILES["B2"]
    for scenario in scenarios:
        baseline_result = evaluate(scenario, profile)
        
        # Perturb hidden primitive: scope
        new_delegations = tuple(dataclasses.replace(d, scope=frozenset({"FAKE_OP"})) for d in scenario.delegations)
        perturbed_scenario = dataclasses.replace(scenario, delegations=new_delegations)
        
        perturbed_result = evaluate(perturbed_scenario, profile)
        assert baseline_result == perturbed_result

def test_inv_cpaw_002_commitment_isolation():
    """Commitment is hidden in B0, B1, B2, B3. Perturbing commitment should not affect B3 output."""
    scenarios = build_scenarios()
    profile = PROFILES["B3"]
    for scenario in scenarios:
        baseline_result = evaluate(scenario, profile)
        
        # Perturb hidden primitive: commitment
        perturbed_scenario = dataclasses.replace(scenario, commitment_allows=frozenset({"FAKE_OP"}))
        
        perturbed_result = evaluate(perturbed_scenario, profile)
        assert baseline_result == perturbed_result

def test_inv_cpaw_002_revocation_isolation():
    """Revocation is hidden in B0, B1, B2, B3, B4. Perturbing revocation should not affect B4 output."""
    scenarios = build_scenarios()
    profile = PROFILES["B4"]
    for scenario in scenarios:
        baseline_result = evaluate(scenario, profile)
        
        # Perturb hidden primitive: revocation
        new_delegations = tuple(dataclasses.replace(d, revoked=not d.revoked) for d in scenario.delegations)
        perturbed_scenario = dataclasses.replace(scenario, delegations=new_delegations)
            
        perturbed_result = evaluate(perturbed_scenario, profile)
        assert baseline_result == perturbed_result

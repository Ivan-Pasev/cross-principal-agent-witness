import copy
from scenarios.delegation_cases import build_scenarios
from witness.evaluator import evaluate
from witness.profiles import PROFILES

def test_inv_cpaw_001_ground_truth_invariance():
    """
    INV-CPAW-001 REGRESSION TEST:
    Changing EvidenceProfile does not change the scenario's underlying incident ground truth.
    We verify this by ensuring the Scenario object is not mutated during evaluation,
    across all profiles.
    """
    scenarios = build_scenarios()
    for scenario in scenarios:
        # Capture the original state
        original_state = copy.deepcopy(scenario)
        
        for profile_name, profile in PROFILES.items():
            # Evaluate the scenario with the profile
            _ = evaluate(scenario, profile)
            
            # Assert that the scenario itself was not mutated
            assert scenario.expected_incident == original_state.expected_incident
            assert scenario.expected_responsible_agent == original_state.expected_responsible_agent
            assert scenario.expected_authority_edge == original_state.expected_authority_edge
            assert scenario.expected_principal_chain == original_state.expected_principal_chain
            assert scenario.expected_violation_type == original_state.expected_violation_type
            assert scenario.action == original_state.action
            assert scenario.delegations == original_state.delegations
            assert scenario.commitment == original_state.commitment
            assert scenario.commitment_allows == original_state.commitment_allows

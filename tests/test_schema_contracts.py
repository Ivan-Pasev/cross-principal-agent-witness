import json
import os

def test_delegation_escape_summary_contract():
    path = "results/delegation_escape_summary.json"
    assert os.path.exists(path), f"Missing {path}"
    
    with open(path, "r") as f:
        data = json.load(f)
        
    assert "scenario_count" in data
    assert data["scenario_count"] == 5
    
    assert "profile_summary" in data
    profiles = ["B0", "B1", "B2", "B3", "B4", "W"]
    for p in profiles:
        assert p in data["profile_summary"]
        metrics = data["profile_summary"][p]
        assert "composite" in metrics
        assert "incident_accuracy" in metrics
        assert "execution_attribution" in metrics
        assert "authority_edge_localization" in metrics
        assert "principal_chain_reconstruction" in metrics
        assert "commitment_localization" in metrics
        assert "revocation_localization" in metrics
        
    assert "ablation_summary" in data
    ablations = ["identity", "provenance", "delegation_scope", "commitment", "revocation", "outcome"]
    for a in ablations:
        assert a in data["ablation_summary"]
        assert "composite_without" in data["ablation_summary"][a]
        assert "evidence_contribution" in data["ablation_summary"][a]

def test_reproduction_manifest_contract():
    path = "results/reproduction_manifest.json"
    assert os.path.exists(path), f"Missing {path}"
    
    with open(path, "r") as f:
        data = json.load(f)
        
    assert "algorithm" in data
    assert "canonical_python" in data
    assert "files" in data
    assert "results/delegation_escape_metrics.csv" in data["files"]
    assert "results/delegation_escape_summary.json" in data["files"]

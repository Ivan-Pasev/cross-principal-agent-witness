from scenarios import build_scenarios
from witness.evaluator import evaluate
from witness.metrics import aggregate, score
from witness.profiles import PROFILES, ablate


def _aggregate(profile):
    rows = [score(s, evaluate(s, profile)) for s in build_scenarios()]
    return aggregate(rows)


def test_delegation_scope_ablation_reduces_authority_localization():
    full = _aggregate(PROFILES["W"])
    minus_scope = _aggregate(ablate(PROFILES["W"], "delegation_scope"))
    assert full["authority_edge_localization"] > minus_scope["authority_edge_localization"]

from witness.delegation import attenuates, find_scope_expansion
from witness.models import Delegation


def test_scope_attenuation_accepts_subset():
    parent = Delegation("d1", "P", "P", "A", frozenset({"READ", "WRITE"}))
    child = Delegation("d2", "P", "A", "B", frozenset({"READ"}), parent_id="d1")
    assert attenuates(parent, child)


def test_scope_expansion_detected():
    parent = Delegation("d1", "P", "P", "A", frozenset({"READ"}))
    child = Delegation("d2", "P", "A", "B", frozenset({"READ", "WRITE"}), parent_id="d1")
    assert find_scope_expansion((parent, child)) == "d2"

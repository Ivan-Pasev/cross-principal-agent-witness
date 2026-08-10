from __future__ import annotations

from typing import Iterable, Optional

from .models import Delegation


def delegation_by_id(delegations: Iterable[Delegation], delegation_id: str) -> Optional[Delegation]:
    for d in delegations:
        if d.delegation_id == delegation_id:
            return d
    return None


def attenuates(parent: Delegation, child: Delegation) -> bool:
    return child.delegator == parent.delegate and child.scope.issubset(parent.scope)


def find_delegation_for_agent(delegations: Iterable[Delegation], agent: str) -> Optional[Delegation]:
    candidates = [d for d in delegations if d.delegate == agent]
    if not candidates:
        return None
    return candidates[-1]


def find_scope_expansion(delegations: Iterable[Delegation]) -> Optional[str]:
    items = list(delegations)
    by_id = {d.delegation_id: d for d in items}
    for child in items:
        if child.parent_id and child.parent_id in by_id:
            parent = by_id[child.parent_id]
            if not attenuates(parent, child):
                return child.delegation_id
    return None


def principal_chain(delegations: Iterable[Delegation], leaf: Delegation) -> tuple[str, ...]:
    """Return the authority path from principal through delegates to the leaf agent."""
    by_id = {d.delegation_id: d for d in delegations}
    lineage = [leaf]
    current = leaf
    visited = {leaf.delegation_id}
    while current.parent_id:
        if current.parent_id in visited:
            break
        parent = by_id.get(current.parent_id)
        if parent is None:
            break
        lineage.append(parent)
        visited.add(parent.delegation_id)
        current = parent
    lineage.reverse()
    chain = [lineage[0].principal]
    chain.extend(d.delegate for d in lineage)
    return tuple(chain)

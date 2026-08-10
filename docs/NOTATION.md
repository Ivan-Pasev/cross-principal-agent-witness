# Formal Notation Register

**Note**: This notation defines the conceptual FORMAL RESEARCH MODEL. It does not imply theorem-level proof and is an abstraction of the CURRENT CODE REPRESENTATION.

- $P$: Set of principals.
- $A$: Set of agents.
- $D$: Set of delegation records/relations.
- $e$: An action/event.
- $\pi$: Authority/delegation path.
- $S(d)$: Scope of delegation $d$.
- $R(d, t)$: Revocation/current-validity state of delegation $d$ at time $t$.
- $C$: Commitment/task constraint.
- $O$: Observed outcome.
- $W$: Full witness/evidence condition.
- $B_k$: Reduced evidence profiles ($k \in \{0, 1, 2, 3, 4\}$).
- $m$: Evaluation metric.

### Scope Attenuation
If child delegation $d_c$ has parent $d_p$, the formal validity condition conceptualized is:
$delegator(d_c) = delegate(d_p)$

Under non-expanding authority semantics (conceptual):
$S(d_c) \subseteq S(d_p)$

**Limitation in Current Code**: The current codebase uses simplified enumerated operation-set commitment semantics and basic hierarchical IDs, not full formal set-theoretic subset operations.

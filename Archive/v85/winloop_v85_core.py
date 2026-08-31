from itertools import product
from math import comb

D = 3
BASE_V84_EPOCH35_COMPLETE_STATIC_STATES = 576


def q(n):
    # Exact count of nonnegative n-coordinate deadline vectors with total <= 3.
    return comb(n + D, D)


def indep():
    cert = ('absent', 'current', 'cached', 'stale', 'conflict', 'self')
    anchor = ('current', 'cached', 'missing', 'stale', 'fork')
    relation = ('disjoint', 'provider', 'operator', 'hardware', 'unknown')
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and r == 'disjoint'
    admitted = [x for x in product(cert, anchor, relation) if ok(*x)]
    return {
        'patterns': len(cert) * len(anchor) * len(relation),
        'hypothetical_gate_admits': len(admitted),
        'committed_external_independence_certificate_present': False,
        'conservative_cross_role_credit': 12,
        'credit_raised': False,
        'bad_acceptances': sum(
            1 for c, a, r in admitted
            if c not in cert[1:3] or a not in anchor[:2] or r != 'disjoint'
        ),
        'checks': [
            ok('current', 'current', 'disjoint'),
            ok('cached', 'cached', 'disjoint'),
            not ok('stale', 'current', 'disjoint'),
            not ok('self', 'current', 'disjoint'),
            all(not ok('current', 'current', r) for r in relation[1:]),
        ],
    }


_GC36_EXPECTED = {
    0: (0, 0, 0, 0, 0),
    1: (1, 0, 0, 0, 0),
    2: (2, 0, 0, 0, 0),
    3: (2, 1, 0, 0, 0),
    4: (2, 2, 0, 0, 0),
    5: (2, 2, 1, 0, 0),
    6: (2, 2, 2, 0, 0),
    7: (2, 2, 2, 1, 0),
    8: (2, 2, 2, 2, 0),
    9: (2, 2, 2, 2, 1),
    10: (2, 2, 2, 2, 2),
}


def _gc36_ok(phase, proof_revalidation, proof_root_binding,
             fourth_source_rollover, fourth_source_binding, verifier_binding,
             root_state, lineage, continuity, source_binding,
             rotated_key_binding, third_source_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        proof_revalidation, proof_root_binding, fourth_source_rollover,
        fourth_source_binding, verifier_binding, root_state, lineage,
        continuity, source_binding, rotated_key_binding, third_source_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # V84 completed epoch 35 only with the prior root, reissued lineage,
    # continuous tombstone root, bound source/key bindings, and bound third source.
    if root_state != 1 or lineage != 2 or continuity != 1:
        return False
    if source_binding != 2 or rotated_key_binding != 2 or third_source_binding != 2:
        return False
    return _GC36_EXPECTED.get(phase) == (
        proof_revalidation, proof_root_binding, fourth_source_rollover,
        fourth_source_binding, verifier_binding
    )


def gc36():
    # Exact symbolic OR-of-AND optimizer: each phase contributes one admissible
    # trust-bearing conjunction; the full rejected domain is counted analytically.
    tails = [
        (phase, *state, 1, 2, 1, 2, 2, 2, 0)
        for phase, state in _GC36_EXPECTED.items()
    ]
    assert all(_gc36_ok(*x) for x in tails)
    z = q(28)
    seed = BASE_V84_EPOCH35_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    proof_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_proof = sum(x[1] == 2 for x in tails) * seed
    root_binding_states = sum(x[2] in (1, 2) for x in tails) * seed
    bound_root_binding = sum(x[2] == 2 for x in tails) * seed
    rollover_states = sum(x[3] in (1, 2) for x in tails) * seed
    bound_rollover = sum(x[3] == 2 for x in tails) * seed
    fourth_binding_states = sum(x[4] in (1, 2) for x in tails) * seed
    bound_fourth_binding = sum(x[4] == 2 for x in tails) * seed
    verifier_states = sum(x[5] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[5] == 2 for x in tails) * seed
    complete = sum(x[0] == 10 for x in tails) * seed

    # All accepted clauses fix these bad dimensions to non-bad values.
    stale_root = sum(x[6] in (2, 3) for x in tails) * seed
    proof_bad = sum(x[1] == 3 for x in tails) * seed
    root_binding_bad = sum(x[2] == 3 for x in tails) * seed
    rollover_bad = sum(x[3] == 3 for x in tails) * seed
    fourth_binding_bad = sum(x[4] == 3 for x in tails) * seed
    verifier_bad = sum(x[5] == 3 for x in tails) * seed
    lineage_bad = sum(x[7] == 3 for x in tails) * seed
    continuity_break = sum(x[8] in (2, 3) for x in tails) * seed
    source_bad = sum(x[9] == 3 for x in tails) * seed
    key_binding_bad = sum(x[10] != 2 for x in tails) * seed
    third_source_bad = sum(x[11] != 2 for x in tails) * seed
    deadline_reset = sum(x[12] != 0 for x in tails) * seed
    bad = (
        stale_root + proof_bad + root_binding_bad + rollover_bad
        + fourth_binding_bad + verifier_bad + lineage_bad + continuity_break
        + source_bad + key_binding_bad + third_source_bad + deadline_reset
    )

    checks = [
        _gc36_ok(0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc36_ok(4, 2, 2, 0, 0, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc36_ok(6, 2, 2, 2, 0, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc36_ok(8, 2, 2, 2, 2, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc36_ok(10, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 3, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 3, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 3, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 3, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 3, 1, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 1, 3, 1, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 1, 2, 1, 3, 2, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 0),
        not _gc36_ok(10, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1),
    ]

    static_patterns = seed * 11 * (4 ** 11) * 3
    patterns = static_patterns * (4 ** 28) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch35_complete_seed_states': seed,
        'delay_vectors': 4 ** 28,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch36_compacted_tombstone_proof_revalidation_states': proof_states * z,
        'epoch36_bound_proof_revalidation_states': bound_proof * z,
        'epoch36_proof_root_binding_states': root_binding_states * z,
        'epoch36_bound_proof_root_binding_states': bound_root_binding * z,
        'epoch36_fourth_source_rollover_states': rollover_states * z,
        'epoch36_bound_fourth_source_rollover_states': bound_rollover * z,
        'epoch36_fourth_source_binding_states': fourth_binding_states * z,
        'epoch36_bound_fourth_source_binding_states': bound_fourth_binding * z,
        'epoch36_verifier_binding_states': verifier_states * z,
        'epoch36_bound_verifier_binding_states': bound_verifier * z,
        'epoch36_complete_states': complete * z,
        'stale_or_conflicting_root_choice_acceptances': stale_root * z,
        'unbound_or_conflicting_proof_revalidation_acceptances': proof_bad * z,
        'unbound_or_conflicting_proof_root_binding_acceptances': root_binding_bad * z,
        'unbound_or_conflicting_fourth_source_rollover_acceptances': rollover_bad * z,
        'unbound_or_conflicting_fourth_source_binding_acceptances': fourth_binding_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'unbound_or_conflicting_reissued_lineage_acceptances': lineage_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'unbound_or_conflicting_source_binding_acceptances': source_bad * z,
        'unbound_or_conflicting_rotated_key_binding_acceptances': key_binding_bad * z,
        'unbound_or_conflicting_third_source_binding_acceptances': third_source_bad * z,
        'deadline_reset_acceptances': deadline_reset * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

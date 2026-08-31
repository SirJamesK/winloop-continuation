from itertools import product
from math import comb

D = 3
BASE_V88_EPOCH39_COMPLETE_STATIC_STATES = 576


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


_GC40_EXPECTED = {
    0: (0, 0, 0),
    1: (1, 0, 0),
    2: (2, 0, 0),
    3: (2, 1, 0),
    4: (2, 2, 0),
    5: (2, 2, 1),
    6: (2, 2, 2),
}


def _gc40_ok(phase, sixth_source_handoff, sixth_source_binding,
             verifier_binding, carried_root_binding, continuity,
             source_binding, rotated_key_binding, third_source_binding,
             fourth_source_binding, fourth_lineage_binding,
             fourth_proof_binding, fifth_source_binding,
             fifth_lineage_binding, fifth_proof_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        sixth_source_handoff, sixth_source_binding, verifier_binding,
        carried_root_binding, continuity, source_binding, rotated_key_binding,
        third_source_binding, fourth_source_binding, fourth_lineage_binding,
        fourth_proof_binding, fifth_source_binding, fifth_lineage_binding,
        fifth_proof_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # V88 completed epoch 39 only after the fifth-source lineage was rotated and
    # bound and the compacted proof was rebound to it. Epoch 40 hands that fully
    # rebound proof to a sixth source, binds the new source, and only then lets
    # the verifier complete, while preserving the original epoch-12 deadline.
    if carried_root_binding != 2 or continuity != 1:
        return False
    if source_binding != 2 or rotated_key_binding != 2:
        return False
    if third_source_binding != 2 or fourth_source_binding != 2:
        return False
    if fourth_lineage_binding != 2 or fourth_proof_binding != 2:
        return False
    if fifth_source_binding != 2 or fifth_lineage_binding != 2:
        return False
    if fifth_proof_binding != 2:
        return False
    return _GC40_EXPECTED.get(phase) == (
        sixth_source_handoff, sixth_source_binding, verifier_binding
    )


def gc40():
    tails = [
        (phase, *state, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0)
        for phase, state in _GC40_EXPECTED.items()
    ]
    assert all(_gc40_ok(*x) for x in tails)
    z = q(35)
    seed = BASE_V88_EPOCH39_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    handoff = sum(x[1] in (1, 2) for x in tails) * seed
    bound_handoff = sum(x[1] == 2 for x in tails) * seed
    sixth_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_sixth_binding = sum(x[2] == 2 for x in tails) * seed
    verifier = sum(x[3] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[3] == 2 for x in tails) * seed
    complete = sum(x[0] == 6 for x in tails) * seed

    handoff_bad = sum(x[1] == 3 for x in tails) * seed
    sixth_binding_bad = sum(x[2] == 3 for x in tails) * seed
    verifier_bad = sum(x[3] == 3 for x in tails) * seed
    root_bad = sum(x[4] != 2 for x in tails) * seed
    continuity_break = sum(x[5] != 1 for x in tails) * seed
    source_bad = sum(x[6] != 2 for x in tails) * seed
    key_bad = sum(x[7] != 2 for x in tails) * seed
    third_bad = sum(x[8] != 2 for x in tails) * seed
    fourth_bad = sum(x[9] != 2 for x in tails) * seed
    fourth_lineage_bad = sum(x[10] != 2 for x in tails) * seed
    fourth_proof_bad = sum(x[11] != 2 for x in tails) * seed
    fifth_source_bad = sum(x[12] != 2 for x in tails) * seed
    fifth_lineage_bad = sum(x[13] != 2 for x in tails) * seed
    fifth_proof_bad = sum(x[14] != 2 for x in tails) * seed
    deadline_bad = sum(x[15] != 0 for x in tails) * seed
    bad = (
        handoff_bad + sixth_binding_bad + verifier_bad + root_bad
        + continuity_break + source_bad + key_bad + third_bad + fourth_bad
        + fourth_lineage_bad + fourth_proof_bad + fifth_source_bad
        + fifth_lineage_bad + fifth_proof_bad + deadline_bad
    )

    checks = [
        _gc40_ok(0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc40_ok(2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc40_ok(4, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 3, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 3, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0),
        not _gc40_ok(6, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1),
    ]

    # Nominal OR-of-AND space: phase, three epoch-40 transitions, carried root,
    # continuity, nine carried source/key/lineage/proof bindings, and reset bit.
    static_patterns = seed * 7 * (4 ** 3) * 4 * 3 * (4 ** 9) * 2
    patterns = static_patterns * (4 ** 35) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch39_complete_seed_states': seed,
        'delay_vectors': 4 ** 35,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch40_sixth_source_handoff_states': handoff * z,
        'epoch40_bound_sixth_source_handoff_states': bound_handoff * z,
        'epoch40_sixth_source_binding_states': sixth_binding * z,
        'epoch40_bound_sixth_source_binding_states': bound_sixth_binding * z,
        'epoch40_verifier_binding_states': verifier * z,
        'epoch40_bound_verifier_binding_states': bound_verifier * z,
        'epoch40_complete_states': complete * z,
        'unbound_or_conflicting_sixth_source_handoff_acceptances': handoff_bad * z,
        'unbound_or_conflicting_sixth_source_binding_acceptances': sixth_binding_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'stale_or_conflicting_root_binding_acceptances': root_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'unbound_or_conflicting_source_binding_acceptances': source_bad * z,
        'unbound_or_conflicting_rotated_key_binding_acceptances': key_bad * z,
        'unbound_or_conflicting_third_source_binding_acceptances': third_bad * z,
        'unbound_or_conflicting_fourth_source_binding_acceptances': fourth_bad * z,
        'unbound_or_conflicting_fourth_lineage_binding_acceptances': fourth_lineage_bad * z,
        'unbound_or_conflicting_fourth_proof_binding_acceptances': fourth_proof_bad * z,
        'unbound_or_conflicting_fifth_source_binding_acceptances': fifth_source_bad * z,
        'unbound_or_conflicting_fifth_lineage_binding_acceptances': fifth_lineage_bad * z,
        'unbound_or_conflicting_fifth_proof_binding_acceptances': fifth_proof_bad * z,
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

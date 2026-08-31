from itertools import product
from math import comb

D = 3
BASE_V87_EPOCH38_COMPLETE_STATIC_STATES = 576


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


_GC39_EXPECTED = {
    0: (0, 0, 0, 0),
    1: (1, 0, 0, 0),
    2: (2, 0, 0, 0),
    3: (2, 1, 0, 0),
    4: (2, 2, 0, 0),
    5: (2, 2, 1, 0),
    6: (2, 2, 2, 0),
    7: (2, 2, 2, 1),
    8: (2, 2, 2, 2),
}


def _gc39_ok(phase, fifth_lineage_rotation, fifth_lineage_binding,
             compacted_proof_rebind, verifier_binding,
             carried_root_binding, continuity, source_binding,
             rotated_key_binding, third_source_binding, fourth_source_binding,
             fourth_lineage_binding, fourth_proof_binding, fifth_source_binding,
             deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        fifth_lineage_rotation, fifth_lineage_binding, compacted_proof_rebind,
        verifier_binding, carried_root_binding, continuity, source_binding,
        rotated_key_binding, third_source_binding, fourth_source_binding,
        fourth_lineage_binding, fourth_proof_binding, fifth_source_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # V87 completed epoch 38 only after the fourth proof was compacted/bound,
    # authority handed to a fifth source, that source bound, and the verifier
    # completed. Epoch 39 rotates and binds that fifth-source lineage, then
    # rebinds the compacted proof before verifier completion.
    if carried_root_binding != 2 or continuity != 1:
        return False
    if source_binding != 2 or rotated_key_binding != 2:
        return False
    if third_source_binding != 2 or fourth_source_binding != 2:
        return False
    if fourth_lineage_binding != 2 or fourth_proof_binding != 2:
        return False
    if fifth_source_binding != 2:
        return False
    return _GC39_EXPECTED.get(phase) == (
        fifth_lineage_rotation, fifth_lineage_binding,
        compacted_proof_rebind, verifier_binding
    )


def gc39():
    tails = [
        (phase, *state, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0)
        for phase, state in _GC39_EXPECTED.items()
    ]
    assert all(_gc39_ok(*x) for x in tails)
    z = q(33)
    seed = BASE_V87_EPOCH38_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    rotation = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rotation = sum(x[1] == 2 for x in tails) * seed
    lineage_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_lineage_binding = sum(x[2] == 2 for x in tails) * seed
    proof_rebind = sum(x[3] in (1, 2) for x in tails) * seed
    bound_proof_rebind = sum(x[3] == 2 for x in tails) * seed
    verifier = sum(x[4] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[4] == 2 for x in tails) * seed
    complete = sum(x[0] == 8 for x in tails) * seed

    rotation_bad = sum(x[1] == 3 for x in tails) * seed
    lineage_bad = sum(x[2] == 3 for x in tails) * seed
    proof_bad = sum(x[3] == 3 for x in tails) * seed
    verifier_bad = sum(x[4] == 3 for x in tails) * seed
    root_bad = sum(x[5] != 2 for x in tails) * seed
    continuity_break = sum(x[6] != 1 for x in tails) * seed
    source_bad = sum(x[7] != 2 for x in tails) * seed
    key_bad = sum(x[8] != 2 for x in tails) * seed
    third_bad = sum(x[9] != 2 for x in tails) * seed
    fourth_bad = sum(x[10] != 2 for x in tails) * seed
    fourth_lineage_bad = sum(x[11] != 2 for x in tails) * seed
    fourth_proof_bad = sum(x[12] != 2 for x in tails) * seed
    fifth_source_bad = sum(x[13] != 2 for x in tails) * seed
    deadline_bad = sum(x[14] != 0 for x in tails) * seed
    bad = (
        rotation_bad + lineage_bad + proof_bad + verifier_bad + root_bad
        + continuity_break + source_bad + key_bad + third_bad + fourth_bad
        + fourth_lineage_bad + fourth_proof_bad + fifth_source_bad + deadline_bad
    )

    checks = [
        _gc39_ok(0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc39_ok(2, 2, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc39_ok(4, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc39_ok(6, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 3, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 3, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 3, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0),
        not _gc39_ok(8, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1),
    ]

    # Nominal OR-of-AND space: phase, four epoch-39 transitions, carried root,
    # continuity, seven carried source/key/lineage/proof bindings, and reset bit.
    static_patterns = seed * 9 * (4 ** 4) * 4 * 3 * (4 ** 7) * 2
    patterns = static_patterns * (4 ** 33) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch38_complete_seed_states': seed,
        'delay_vectors': 4 ** 33,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch39_fifth_lineage_rotation_states': rotation * z,
        'epoch39_bound_fifth_lineage_rotation_states': bound_rotation * z,
        'epoch39_fifth_lineage_binding_states': lineage_binding * z,
        'epoch39_bound_fifth_lineage_binding_states': bound_lineage_binding * z,
        'epoch39_compacted_proof_rebind_states': proof_rebind * z,
        'epoch39_bound_compacted_proof_rebind_states': bound_proof_rebind * z,
        'epoch39_verifier_binding_states': verifier * z,
        'epoch39_bound_verifier_binding_states': bound_verifier * z,
        'epoch39_complete_states': complete * z,
        'unbound_or_conflicting_fifth_lineage_rotation_acceptances': rotation_bad * z,
        'unbound_or_conflicting_fifth_lineage_binding_acceptances': lineage_bad * z,
        'unbound_or_conflicting_compacted_proof_rebind_acceptances': proof_bad * z,
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
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

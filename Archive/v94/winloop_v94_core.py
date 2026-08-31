from itertools import product
from math import comb

D = 3
BASE_V93_EPOCH44_COMPLETE_STATIC_STATES = 576


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


_GC45_EXPECTED = {
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


def _gc45_ok(phase, eighth_lineage_rotation, eighth_lineage_binding,
             handed_proof_rebind, verifier_binding, carried_root_binding,
             continuity, source_binding, rotated_key_binding,
             third_source_binding, fourth_source_binding, fourth_lineage_binding,
             fourth_proof_binding, fifth_source_binding, fifth_lineage_binding,
             fifth_proof_binding, sixth_source_binding, sixth_handoff_binding,
             sixth_lineage_binding, sixth_handed_proof_rebind,
             seventh_source_handoff, seventh_source_binding,
             seventh_lineage_binding, seventh_handed_proof_rebind,
             eighth_source_handoff, eighth_source_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    trust = (
        eighth_lineage_rotation, eighth_lineage_binding, handed_proof_rebind,
        verifier_binding, carried_root_binding, continuity, source_binding,
        rotated_key_binding, third_source_binding, fourth_source_binding,
        fourth_lineage_binding, fourth_proof_binding, fifth_source_binding,
        fifth_lineage_binding, fifth_proof_binding, sixth_source_binding,
        sixth_handoff_binding, sixth_lineage_binding, sixth_handed_proof_rebind,
        seventh_source_handoff, seventh_source_binding, seventh_lineage_binding,
        seventh_handed_proof_rebind, eighth_source_handoff, eighth_source_binding,
    )
    if any(x == 3 for x in trust):
        return False
    if deadline_reset != 0:
        return False
    # V93 completed epoch 44 only after the rebound proof was handed to and
    # bound by an eighth source. Epoch 45 rotates and binds that source lineage,
    # rebinds the handed proof, and only then permits verifier completion.
    if carried_root_binding != 2 or continuity != 1:
        return False
    carried = (
        source_binding, rotated_key_binding, third_source_binding,
        fourth_source_binding, fourth_lineage_binding, fourth_proof_binding,
        fifth_source_binding, fifth_lineage_binding, fifth_proof_binding,
        sixth_source_binding, sixth_handoff_binding, sixth_lineage_binding,
        sixth_handed_proof_rebind, seventh_source_handoff, seventh_source_binding,
        seventh_lineage_binding, seventh_handed_proof_rebind,
        eighth_source_handoff, eighth_source_binding,
    )
    if any(x != 2 for x in carried):
        return False
    return _GC45_EXPECTED.get(phase) == (
        eighth_lineage_rotation, eighth_lineage_binding,
        handed_proof_rebind, verifier_binding
    )


def gc45():
    fixed = (2, 1, *([2] * 19), 0)
    tails = [(phase, *state, *fixed) for phase, state in _GC45_EXPECTED.items()]
    assert all(_gc45_ok(*x) for x in tails)
    z = q(45)
    seed = BASE_V93_EPOCH44_COMPLETE_STATIC_STATES
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

    transition_bad = [sum(x[i] == 3 for x in tails) * seed for i in range(1, 5)]
    root_bad = sum(x[5] != 2 for x in tails) * seed
    continuity_break = sum(x[6] != 1 for x in tails) * seed
    carried_bad = [sum(x[i] != 2 for x in tails) * seed for i in range(7, 26)]
    deadline_bad = sum(x[26] != 0 for x in tails) * seed
    bad = sum(transition_bad) + root_bad + continuity_break + sum(carried_bad) + deadline_bad

    checks = [
        _gc45_ok(0, 0, 0, 0, 0, *fixed),
        _gc45_ok(2, 2, 0, 0, 0, *fixed),
        _gc45_ok(4, 2, 2, 0, 0, *fixed),
        _gc45_ok(6, 2, 2, 2, 0, *fixed),
        _gc45_ok(8, 2, 2, 2, 2, *fixed),
        not _gc45_ok(8, 3, 2, 2, 2, *fixed),
        not _gc45_ok(8, 2, 3, 2, 2, *fixed),
        not _gc45_ok(8, 2, 2, 3, 2, *fixed),
        not _gc45_ok(8, 2, 2, 2, 3, *fixed),
    ]
    for i in range(len(fixed)):
        broken = list(fixed)
        if i == 1:  # continuity must be exactly 1
            broken[i] = 2
        elif i == len(fixed) - 1:  # deadline reset must remain zero
            broken[i] = 1
        else:
            broken[i] = 1
        checks.append(not _gc45_ok(8, 2, 2, 2, 2, *broken))

    # Phase, four epoch-45 transitions, carried root, continuity, nineteen
    # carried source/key/lineage/proof/handoff bindings, and deadline-reset bit.
    static_patterns = seed * 9 * (4 ** 4) * 4 * 3 * (4 ** 19) * 2
    patterns = static_patterns * (4 ** 45) * z
    out = {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch44_complete_seed_states': seed,
        'delay_vectors': 4 ** 45,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch45_eighth_lineage_rotation_states': rotation * z,
        'epoch45_bound_eighth_lineage_rotation_states': bound_rotation * z,
        'epoch45_eighth_lineage_binding_states': lineage_binding * z,
        'epoch45_bound_eighth_lineage_binding_states': bound_lineage_binding * z,
        'epoch45_handed_proof_rebind_states': proof_rebind * z,
        'epoch45_bound_handed_proof_rebind_states': bound_proof_rebind * z,
        'epoch45_verifier_binding_states': verifier * z,
        'epoch45_bound_verifier_binding_states': bound_verifier * z,
        'epoch45_complete_states': complete * z,
        'unbound_or_conflicting_eighth_lineage_rotation_acceptances': transition_bad[0] * z,
        'unbound_or_conflicting_eighth_lineage_binding_acceptances': transition_bad[1] * z,
        'unbound_or_conflicting_handed_proof_rebind_acceptances': transition_bad[2] * z,
        'unbound_or_conflicting_verifier_binding_acceptances': transition_bad[3] * z,
        'stale_or_conflicting_root_binding_acceptances': root_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }
    names = (
        'source_binding', 'rotated_key_binding', 'third_source_binding',
        'fourth_source_binding', 'fourth_lineage_binding', 'fourth_proof_binding',
        'fifth_source_binding', 'fifth_lineage_binding', 'fifth_proof_binding',
        'sixth_source_binding', 'sixth_handoff_binding', 'sixth_lineage_binding',
        'sixth_handed_proof_rebind', 'seventh_source_handoff',
        'seventh_source_binding', 'seventh_lineage_binding',
        'seventh_handed_proof_rebind', 'eighth_source_handoff',
        'eighth_source_binding',
    )
    for name, count in zip(names, carried_bad):
        out[f'unbound_or_conflicting_{name}_acceptances'] = count * z
    return out

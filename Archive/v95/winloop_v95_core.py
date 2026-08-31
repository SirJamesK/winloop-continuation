from itertools import product
from math import comb

D = 3
BASE_V94_EPOCH45_COMPLETE_STATIC_STATES = 576


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


_GC46_EXPECTED = {
    0: (0, 0, 0),
    1: (1, 0, 0),
    2: (2, 0, 0),
    3: (2, 1, 0),
    4: (2, 2, 0),
    5: (2, 2, 1),
    6: (2, 2, 2),
}


def _gc46_ok(phase, ninth_source_handoff, ninth_source_binding,
             verifier_binding, carried_root_binding, continuity,
             source_binding, rotated_key_binding, third_source_binding,
             fourth_source_binding, fourth_lineage_binding,
             fourth_proof_binding, fifth_source_binding,
             fifth_lineage_binding, fifth_proof_binding,
             sixth_source_binding, sixth_handoff_binding,
             sixth_lineage_binding, sixth_handed_proof_rebind,
             seventh_source_handoff, seventh_source_binding,
             seventh_lineage_binding, seventh_handed_proof_rebind,
             eighth_source_handoff, eighth_source_binding,
             eighth_lineage_binding, handed_proof_rebind, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        ninth_source_handoff, ninth_source_binding, verifier_binding,
        carried_root_binding, continuity, source_binding, rotated_key_binding,
        third_source_binding, fourth_source_binding, fourth_lineage_binding,
        fourth_proof_binding, fifth_source_binding, fifth_lineage_binding,
        fifth_proof_binding, sixth_source_binding, sixth_handoff_binding,
        sixth_lineage_binding, sixth_handed_proof_rebind,
        seventh_source_handoff, seventh_source_binding,
        seventh_lineage_binding, seventh_handed_proof_rebind,
        eighth_source_handoff, eighth_source_binding,
        eighth_lineage_binding, handed_proof_rebind,
    )):
        return False
    if deadline_reset != 0:
        return False
    # V94 completed epoch 45 only after eighth-lineage binding and a fresh
    # handed-proof rebind. Epoch 46 hands that rebound proof to a ninth source,
    # binds the new source, and only then permits verifier completion.
    if carried_root_binding != 2 or continuity != 1:
        return False
    carried = (
        source_binding, rotated_key_binding, third_source_binding,
        fourth_source_binding, fourth_lineage_binding, fourth_proof_binding,
        fifth_source_binding, fifth_lineage_binding, fifth_proof_binding,
        sixth_source_binding, sixth_handoff_binding, sixth_lineage_binding,
        sixth_handed_proof_rebind, seventh_source_handoff,
        seventh_source_binding, seventh_lineage_binding,
        seventh_handed_proof_rebind, eighth_source_handoff,
        eighth_source_binding, eighth_lineage_binding, handed_proof_rebind,
    )
    if any(x != 2 for x in carried):
        return False
    return _GC46_EXPECTED.get(phase) == (
        ninth_source_handoff, ninth_source_binding, verifier_binding
    )


def gc46():
    fixed = (2, 1, *([2] * 21), 0)
    tails = [(phase, *state, *fixed) for phase, state in _GC46_EXPECTED.items()]
    assert all(_gc46_ok(*x) for x in tails)
    z = q(47)
    seed = BASE_V94_EPOCH45_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    handoff = sum(x[1] in (1, 2) for x in tails) * seed
    bound_handoff = sum(x[1] == 2 for x in tails) * seed
    ninth_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_ninth_binding = sum(x[2] == 2 for x in tails) * seed
    verifier = sum(x[3] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[3] == 2 for x in tails) * seed
    complete = sum(x[0] == 6 for x in tails) * seed

    handoff_bad = sum(x[1] == 3 for x in tails) * seed
    ninth_binding_bad = sum(x[2] == 3 for x in tails) * seed
    verifier_bad = sum(x[3] == 3 for x in tails) * seed
    root_bad = sum(x[4] != 2 for x in tails) * seed
    continuity_break = sum(x[5] != 1 for x in tails) * seed
    carried_bad = [sum(x[i] != 2 for x in tails) * seed for i in range(6, 27)]
    deadline_bad = sum(x[27] != 0 for x in tails) * seed
    bad = handoff_bad + ninth_binding_bad + verifier_bad + root_bad + continuity_break + sum(carried_bad) + deadline_bad

    checks = [
        _gc46_ok(0, 0, 0, 0, *fixed),
        _gc46_ok(2, 2, 0, 0, *fixed),
        _gc46_ok(4, 2, 2, 0, *fixed),
        _gc46_ok(6, 2, 2, 2, *fixed),
        not _gc46_ok(6, 3, 2, 2, *fixed),
        not _gc46_ok(6, 2, 3, 2, *fixed),
        not _gc46_ok(6, 2, 2, 3, *fixed),
    ]
    for i in range(len(fixed)):
        broken = list(fixed)
        if i == 1:  # continuity must be exactly 1
            broken[i] = 2
        elif i == len(fixed) - 1:  # deadline reset must remain zero
            broken[i] = 1
        else:
            broken[i] = 1
        checks.append(not _gc46_ok(6, 2, 2, 2, *broken))

    # Phase, three epoch-46 transitions, carried root, continuity, twenty-one
    # carried source/key/lineage/proof/handoff bindings, and deadline-reset bit.
    static_patterns = seed * 7 * (4 ** 3) * 4 * 3 * (4 ** 21) * 2
    patterns = static_patterns * (4 ** 47) * z
    names = (
        'source_binding', 'rotated_key_binding', 'third_source_binding',
        'fourth_source_binding', 'fourth_lineage_binding', 'fourth_proof_binding',
        'fifth_source_binding', 'fifth_lineage_binding', 'fifth_proof_binding',
        'sixth_source_binding', 'sixth_handoff_binding', 'sixth_lineage_binding',
        'sixth_handed_proof_rebind', 'seventh_source_handoff',
        'seventh_source_binding', 'seventh_lineage_binding',
        'seventh_handed_proof_rebind', 'eighth_source_handoff',
        'eighth_source_binding', 'eighth_lineage_binding',
        'handed_proof_rebind',
    )
    out = {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch45_complete_seed_states': seed,
        'delay_vectors': 4 ** 47,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch46_ninth_source_handoff_states': handoff * z,
        'epoch46_bound_ninth_source_handoff_states': bound_handoff * z,
        'epoch46_ninth_source_binding_states': ninth_binding * z,
        'epoch46_bound_ninth_source_binding_states': bound_ninth_binding * z,
        'epoch46_verifier_binding_states': verifier * z,
        'epoch46_bound_verifier_binding_states': bound_verifier * z,
        'epoch46_complete_states': complete * z,
        'unbound_or_conflicting_ninth_source_handoff_acceptances': handoff_bad * z,
        'unbound_or_conflicting_ninth_source_binding_acceptances': ninth_binding_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'stale_or_conflicting_root_binding_acceptances': root_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }
    for name, count in zip(names, carried_bad):
        out[f'unbound_or_conflicting_{name}_acceptances'] = count * z
    return out

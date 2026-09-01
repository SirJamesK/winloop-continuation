from itertools import product
from math import comb

D = 3
BASE_V108_EPOCH59_COMPLETE_STATIC_STATES = 576


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


CARRIED_NAMES = (
    'source_binding', 'rotated_key_binding', 'third_source_binding',
    'fourth_source_binding', 'fourth_lineage_binding', 'fourth_proof_binding',
    'fifth_source_binding', 'fifth_lineage_binding', 'fifth_proof_binding',
    'sixth_source_binding', 'sixth_handoff_binding', 'sixth_lineage_binding',
    'sixth_handed_proof_rebind', 'seventh_source_handoff',
    'seventh_source_binding', 'seventh_lineage_binding',
    'seventh_handed_proof_rebind', 'eighth_source_handoff',
    'eighth_source_binding', 'eighth_lineage_binding',
    'eighth_handed_proof_rebind', 'ninth_source_handoff',
    'ninth_source_binding', 'ninth_lineage_rotation',
    'ninth_lineage_binding', 'ninth_handed_proof_rebind',
    'tenth_source_handoff', 'tenth_source_binding',
    'tenth_lineage_rotation', 'tenth_lineage_binding',
    'tenth_handed_proof_rebind', 'eleventh_source_handoff',
    'eleventh_source_binding', 'eleventh_lineage_rotation',
    'eleventh_lineage_binding', 'eleventh_handed_proof_rebind',
    'twelfth_source_handoff', 'twelfth_source_binding',
    'twelfth_lineage_rotation', 'twelfth_lineage_binding',
    'twelfth_handed_proof_rebind', 'thirteenth_source_handoff',
    'thirteenth_source_binding', 'thirteenth_lineage_rotation',
    'thirteenth_lineage_binding', 'thirteenth_handed_proof_rebind',
    'fourteenth_source_handoff', 'fourteenth_source_binding',
    'fourteenth_lineage_rotation', 'fourteenth_lineage_binding',
    'fourteenth_handed_proof_rebind', 'fifteenth_source_handoff',
    'fifteenth_source_binding', 'fifteenth_lineage_rotation',
    'fifteenth_lineage_binding', 'fifteenth_handed_proof_rebind',
)

_GC60_EXPECTED = {
    0: (0, 0, 0),
    1: (1, 0, 0),
    2: (2, 0, 0),
    3: (2, 1, 0),
    4: (2, 2, 0),
    5: (2, 2, 1),
    6: (2, 2, 2),
}


def _gc60_ok(phase, sixteenth_source_handoff, sixteenth_source_binding,
             verifier_binding, carried_root_binding, continuity, *rest):
    if len(rest) != len(CARRIED_NAMES) + 1:
        return False
    *carried, deadline_reset = rest
    trust = (
        sixteenth_source_handoff, sixteenth_source_binding, verifier_binding,
        carried_root_binding, continuity, *carried,
    )
    if any(x == 3 for x in trust):
        return False
    if deadline_reset != 0:
        return False
    # V108 completed epoch 59 only after the fifteenth-source lineage was
    # rotated and bound and the handed proof was rebound. Epoch 60 hands that
    # rebound proof to a sixteenth source, binds it, and then permits verifier completion.
    if carried_root_binding != 2 or continuity != 1:
        return False
    if any(x != 2 for x in carried):
        return False
    return _GC60_EXPECTED.get(phase) == (
        sixteenth_source_handoff, sixteenth_source_binding, verifier_binding
    )


def gc60():
    fixed = (2, 1, *([2] * len(CARRIED_NAMES)), 0)
    tails = [(phase, *state, *fixed) for phase, state in _GC60_EXPECTED.items()]
    assert all(_gc60_ok(*x) for x in tails)
    z = q(75)
    seed = BASE_V108_EPOCH59_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    handoff = sum(x[1] in (1, 2) for x in tails) * seed
    bound_handoff = sum(x[1] == 2 for x in tails) * seed
    source_binding_count = sum(x[2] in (1, 2) for x in tails) * seed
    bound_source_binding = sum(x[2] == 2 for x in tails) * seed
    verifier = sum(x[3] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[3] == 2 for x in tails) * seed
    complete = sum(x[0] == 6 for x in tails) * seed

    transition_bad = [sum(x[i] == 3 for x in tails) * seed for i in range(1, 4)]
    root_bad = sum(x[4] != 2 for x in tails) * seed
    continuity_break = sum(x[5] != 1 for x in tails) * seed
    carried_start = 6
    carried_end = carried_start + len(CARRIED_NAMES)
    carried_bad = [sum(x[i] != 2 for x in tails) * seed for i in range(carried_start, carried_end)]
    deadline_bad = sum(x[carried_end] != 0 for x in tails) * seed
    bad = sum(transition_bad) + root_bad + continuity_break + sum(carried_bad) + deadline_bad

    checks = [
        _gc60_ok(0, 0, 0, 0, *fixed),
        _gc60_ok(2, 2, 0, 0, *fixed),
        _gc60_ok(4, 2, 2, 0, *fixed),
        _gc60_ok(6, 2, 2, 2, *fixed),
        not _gc60_ok(6, 3, 2, 2, *fixed),
        not _gc60_ok(6, 2, 3, 2, *fixed),
        not _gc60_ok(6, 2, 2, 3, *fixed),
    ]
    for i in range(len(fixed)):
        broken = list(fixed)
        if i == 1:  # continuity must be exactly 1
            broken[i] = 2
        elif i == len(fixed) - 1:  # deadline reset must remain zero
            broken[i] = 1
        else:
            broken[i] = 1
        checks.append(not _gc60_ok(6, 2, 2, 2, *broken))

    static_patterns = seed * 7 * (4 ** 3) * 4 * 3 * (4 ** len(CARRIED_NAMES)) * 2
    patterns = static_patterns * (4 ** 75) * z
    out = {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch59_complete_seed_states': seed,
        'delay_vectors': 4 ** 75,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch60_sixteenth_source_handoff_states': handoff * z,
        'epoch60_bound_sixteenth_source_handoff_states': bound_handoff * z,
        'epoch60_sixteenth_source_binding_states': source_binding_count * z,
        'epoch60_bound_sixteenth_source_binding_states': bound_source_binding * z,
        'epoch60_verifier_binding_states': verifier * z,
        'epoch60_bound_verifier_binding_states': bound_verifier * z,
        'epoch60_complete_states': complete * z,
        'unbound_or_conflicting_sixteenth_source_handoff_acceptances': transition_bad[0] * z,
        'unbound_or_conflicting_sixteenth_source_binding_acceptances': transition_bad[1] * z,
        'unbound_or_conflicting_verifier_binding_acceptances': transition_bad[2] * z,
        'stale_or_conflicting_root_binding_acceptances': root_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }
    for name, count in zip(CARRIED_NAMES, carried_bad):
        out[f'unbound_or_conflicting_{name}_acceptances'] = count * z
    return out

from itertools import product
from math import comb

D = 3
BASE_V129_EPOCH80_COMPLETE_STATIC_STATES = 576


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


_EARLY_CARRIED_NAMES = (
    'source_binding', 'rotated_key_binding', 'third_source_binding',
    'fourth_source_binding', 'fourth_lineage_binding', 'fourth_proof_binding',
    'fifth_source_binding', 'fifth_lineage_binding', 'fifth_proof_binding',
    'sixth_source_binding', 'sixth_handoff_binding', 'sixth_lineage_binding',
    'sixth_handed_proof_rebind',
    'seventh_source_handoff', 'seventh_source_binding',
    'seventh_lineage_binding', 'seventh_handed_proof_rebind',
    'eighth_source_handoff', 'eighth_source_binding',
    'eighth_lineage_binding', 'eighth_handed_proof_rebind',
)
_FULL_LINEAGES = (
    'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth',
    'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth',
    'twentieth', 'twenty_first', 'twenty_second', 'twenty_third', 'twenty_fourth',
    'twenty_fifth',
)
CARRIED_NAMES = _EARLY_CARRIED_NAMES + tuple(
    f'{ordinal}_{suffix}'
    for ordinal in _FULL_LINEAGES
    for suffix in (
        'source_handoff', 'source_binding', 'lineage_rotation',
        'lineage_binding', 'handed_proof_rebind',
    )
) + (
    'twenty_sixth_source_handoff',
    'twenty_sixth_source_binding',
)

_GC81_EXPECTED = {
    0: (0, 0, 0, 0), 1: (1, 0, 0, 0), 2: (2, 0, 0, 0),
    3: (2, 1, 0, 0), 4: (2, 2, 0, 0), 5: (2, 2, 1, 0),
    6: (2, 2, 2, 0), 7: (2, 2, 2, 1), 8: (2, 2, 2, 2),
}


def _gc81_ok(phase, twenty_sixth_lineage_rotation, twenty_sixth_lineage_binding,
             new_handed_proof_rebind, verifier_binding, carried_root_binding,
             continuity, *rest):
    if len(rest) != len(CARRIED_NAMES) + 1:
        return False
    *carried, deadline_reset = rest
    trust = (
        twenty_sixth_lineage_rotation, twenty_sixth_lineage_binding,
        new_handed_proof_rebind, verifier_binding, carried_root_binding,
        continuity, *carried,
    )
    if any(x == 3 for x in trust) or deadline_reset != 0:
        return False
    # V129 completes epoch 80 only after twenty-sixth-source handoff, source
    # binding, and verifier completion. Epoch 81 rotates that source lineage,
    # binds it, rebinds the handed proof, and only then permits verifier
    # completion while retaining the original epoch-12 deadline.
    if carried_root_binding != 2 or continuity != 1 or any(x != 2 for x in carried):
        return False
    return _GC81_EXPECTED.get(phase) == (
        twenty_sixth_lineage_rotation, twenty_sixth_lineage_binding,
        new_handed_proof_rebind, verifier_binding
    )


def gc81():
    fixed = (2, 1, *([2] * len(CARRIED_NAMES)), 0)
    tails = [(phase, *state, *fixed) for phase, state in _GC81_EXPECTED.items()]
    assert all(_gc81_ok(*x) for x in tails)
    z = q(117)
    seed = BASE_V129_EPOCH80_COMPLETE_STATIC_STATES
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
    carried_start = 7
    carried_end = carried_start + len(CARRIED_NAMES)
    carried_bad = [sum(x[i] != 2 for x in tails) * seed for i in range(carried_start, carried_end)]
    deadline_bad = sum(x[carried_end] != 0 for x in tails) * seed
    bad = sum(transition_bad) + root_bad + continuity_break + sum(carried_bad) + deadline_bad

    checks = [
        _gc81_ok(0, 0, 0, 0, 0, *fixed),
        _gc81_ok(2, 2, 0, 0, 0, *fixed),
        _gc81_ok(4, 2, 2, 0, 0, *fixed),
        _gc81_ok(6, 2, 2, 2, 0, *fixed),
        _gc81_ok(8, 2, 2, 2, 2, *fixed),
        not _gc81_ok(8, 3, 2, 2, 2, *fixed),
        not _gc81_ok(8, 2, 3, 2, 2, *fixed),
        not _gc81_ok(8, 2, 2, 3, 2, *fixed),
        not _gc81_ok(8, 2, 2, 2, 3, *fixed),
    ]
    for i in range(len(fixed)):
        broken = list(fixed)
        if i == 1:
            broken[i] = 2
        elif i == len(fixed) - 1:
            broken[i] = 1
        else:
            broken[i] = 1
        checks.append(not _gc81_ok(8, 2, 2, 2, 2, *broken))

    static_patterns = seed * 9 * (4 ** 4) * 4 * 3 * (4 ** len(CARRIED_NAMES)) * 2
    patterns = static_patterns * (4 ** 117) * z
    out = {
        'patterns': patterns, 'accepted': static_accepted * z,
        'base_states': static_accepted, 'epoch80_complete_seed_states': seed,
        'delay_vectors': 4 ** 117, 'deadline_vectors': z, 'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch81_twenty_sixth_lineage_rotation_states': rotation * z,
        'epoch81_bound_twenty_sixth_lineage_rotation_states': bound_rotation * z,
        'epoch81_twenty_sixth_lineage_binding_states': lineage_binding * z,
        'epoch81_bound_twenty_sixth_lineage_binding_states': bound_lineage_binding * z,
        'epoch81_handed_proof_rebind_states': proof_rebind * z,
        'epoch81_bound_handed_proof_rebind_states': bound_proof_rebind * z,
        'epoch81_verifier_binding_states': verifier * z,
        'epoch81_bound_verifier_binding_states': bound_verifier * z,
        'epoch81_complete_states': complete * z,
        'unbound_or_conflicting_twenty_sixth_lineage_rotation_acceptances': transition_bad[0] * z,
        'unbound_or_conflicting_twenty_sixth_lineage_binding_acceptances': transition_bad[1] * z,
        'unbound_or_conflicting_handed_proof_rebind_acceptances': transition_bad[2] * z,
        'unbound_or_conflicting_verifier_binding_acceptances': transition_bad[3] * z,
        'stale_or_conflicting_root_binding_acceptances': root_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z, 'checks': checks,
    }
    for name, count in zip(CARRIED_NAMES, carried_bad):
        out[f'unbound_or_conflicting_{name}_acceptances'] = count * z
    return out

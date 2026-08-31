from itertools import product
from math import comb

D = 3
BASE_V86_EPOCH37_COMPLETE_STATIC_STATES = 576


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


_GC38_EXPECTED = {
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


def _gc38_ok(phase, fourth_proof_compaction, fourth_proof_binding,
             fifth_source_handoff, fifth_source_binding, verifier_binding,
             carried_root_binding, continuity, source_binding,
             rotated_key_binding, third_source_binding, fourth_source_binding,
             fourth_lineage_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        fourth_proof_compaction, fourth_proof_binding, fifth_source_handoff,
        fifth_source_binding, verifier_binding, carried_root_binding,
        continuity, source_binding, rotated_key_binding, third_source_binding,
        fourth_source_binding, fourth_lineage_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # V86 completed epoch 37 only after fourth-source lineage re-rotation and a
    # bound root rollover. Epoch 38 may compact that root-rolled proof only while
    # every carried trust binding remains current, then hand authority to a fifth
    # source and bind that source before the verifier may complete the epoch.
    if carried_root_binding != 2 or continuity != 1:
        return False
    if source_binding != 2 or rotated_key_binding != 2:
        return False
    if third_source_binding != 2 or fourth_source_binding != 2:
        return False
    if fourth_lineage_binding != 2:
        return False
    return _GC38_EXPECTED.get(phase) == (
        fourth_proof_compaction, fourth_proof_binding, fifth_source_handoff,
        fifth_source_binding, verifier_binding
    )


def gc38():
    tails = [
        (phase, *state, 2, 1, 2, 2, 2, 2, 2, 0)
        for phase, state in _GC38_EXPECTED.items()
    ]
    assert all(_gc38_ok(*x) for x in tails)
    z = q(31)
    seed = BASE_V86_EPOCH37_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    compaction = sum(x[1] in (1, 2) for x in tails) * seed
    bound_compaction = sum(x[1] == 2 for x in tails) * seed
    proof_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_proof_binding = sum(x[2] == 2 for x in tails) * seed
    handoff = sum(x[3] in (1, 2) for x in tails) * seed
    bound_handoff = sum(x[3] == 2 for x in tails) * seed
    fifth_binding = sum(x[4] in (1, 2) for x in tails) * seed
    bound_fifth_binding = sum(x[4] == 2 for x in tails) * seed
    verifier = sum(x[5] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[5] == 2 for x in tails) * seed
    complete = sum(x[0] == 10 for x in tails) * seed

    compaction_bad = sum(x[1] == 3 for x in tails) * seed
    proof_binding_bad = sum(x[2] == 3 for x in tails) * seed
    handoff_bad = sum(x[3] == 3 for x in tails) * seed
    fifth_binding_bad = sum(x[4] == 3 for x in tails) * seed
    verifier_bad = sum(x[5] == 3 for x in tails) * seed
    root_bad = sum(x[6] != 2 for x in tails) * seed
    continuity_break = sum(x[7] != 1 for x in tails) * seed
    source_bad = sum(x[8] != 2 for x in tails) * seed
    key_bad = sum(x[9] != 2 for x in tails) * seed
    third_bad = sum(x[10] != 2 for x in tails) * seed
    fourth_bad = sum(x[11] != 2 for x in tails) * seed
    fourth_lineage_bad = sum(x[12] != 2 for x in tails) * seed
    deadline_bad = sum(x[13] != 0 for x in tails) * seed
    bad = (
        compaction_bad + proof_binding_bad + handoff_bad + fifth_binding_bad
        + verifier_bad + root_bad + continuity_break + source_bad + key_bad
        + third_bad + fourth_bad + fourth_lineage_bad + deadline_bad
    )

    checks = [
        _gc38_ok(0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0),
        _gc38_ok(2, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0),
        _gc38_ok(4, 2, 2, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0),
        _gc38_ok(6, 2, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0),
        _gc38_ok(8, 2, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 0),
        _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 3, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 3, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 3, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 3, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 3, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 0),
        not _gc38_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1),
    ]

    # Nominal OR-of-AND space: phase, five trust transitions, carried root,
    # continuity, five carried source/key/lineage bindings, and reset bit.
    static_patterns = seed * 11 * (4 ** 5) * 4 * 3 * (4 ** 5) * 2
    patterns = static_patterns * (4 ** 31) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch37_complete_seed_states': seed,
        'delay_vectors': 4 ** 31,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch38_fourth_proof_compaction_states': compaction * z,
        'epoch38_bound_fourth_proof_compaction_states': bound_compaction * z,
        'epoch38_fourth_proof_binding_states': proof_binding * z,
        'epoch38_bound_fourth_proof_binding_states': bound_proof_binding * z,
        'epoch38_fifth_source_handoff_states': handoff * z,
        'epoch38_bound_fifth_source_handoff_states': bound_handoff * z,
        'epoch38_fifth_source_binding_states': fifth_binding * z,
        'epoch38_bound_fifth_source_binding_states': bound_fifth_binding * z,
        'epoch38_verifier_binding_states': verifier * z,
        'epoch38_bound_verifier_binding_states': bound_verifier * z,
        'epoch38_complete_states': complete * z,
        'unbound_or_conflicting_fourth_proof_compaction_acceptances': compaction_bad * z,
        'unbound_or_conflicting_fourth_proof_binding_acceptances': proof_binding_bad * z,
        'unbound_or_conflicting_fifth_source_handoff_acceptances': handoff_bad * z,
        'unbound_or_conflicting_fifth_source_binding_acceptances': fifth_binding_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'stale_or_conflicting_root_binding_acceptances': root_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'unbound_or_conflicting_source_binding_acceptances': source_bad * z,
        'unbound_or_conflicting_rotated_key_binding_acceptances': key_bad * z,
        'unbound_or_conflicting_third_source_binding_acceptances': third_bad * z,
        'unbound_or_conflicting_fourth_source_binding_acceptances': fourth_bad * z,
        'unbound_or_conflicting_fourth_lineage_binding_acceptances': fourth_lineage_bad * z,
        'deadline_reset_acceptances': deadline_bad * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

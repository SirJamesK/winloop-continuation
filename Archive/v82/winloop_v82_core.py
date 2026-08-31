from itertools import product
from math import comb

D = 3
BASE_V81_EPOCH32_COMPLETE_STATIC_STATES = 576


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


def _gc33_ok(phase, compaction, verifier_binding, key_rotation,
             root_state, lineage, continuity, source_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        compaction, verifier_binding, key_rotation, root_state,
        lineage, continuity, source_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # Root state 2 is stale; continuity state 2 is discontinuous.
    if root_state != 1 or lineage != 2 or continuity != 1 or source_binding != 2:
        return False

    if phase == 0:
        return (compaction, verifier_binding, key_rotation) == (0, 0, 0)
    if phase == 1:
        return (compaction, verifier_binding, key_rotation) == (1, 0, 0)
    if phase == 2:
        return (compaction, verifier_binding, key_rotation) == (2, 0, 0)
    if phase == 3:
        return (compaction, verifier_binding, key_rotation) == (2, 1, 0)
    if phase == 4:
        return (compaction, verifier_binding, key_rotation) == (2, 2, 0)
    if phase == 5:
        return (compaction, verifier_binding, key_rotation) == (2, 2, 1)
    if phase == 6:
        return (compaction, verifier_binding, key_rotation) == (2, 2, 2)
    return False


def gc33():
    tails = [
        x for x in product(
            range(7), range(4), range(4), range(4), range(4),
            range(4), range(4), range(4), range(3)
        )
        if _gc33_ok(*x)
    ]
    z = q(25)
    seed = BASE_V81_EPOCH32_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    compaction_states = sum(x[1] in (1, 2) for x in tails) * seed
    compaction_complete = sum(x[1] == 2 for x in tails) * seed
    verifier_bound_compaction = sum(x[1] == 2 and x[2] == 2 for x in tails) * seed
    verifier_states = sum(x[2] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[2] == 2 for x in tails) * seed
    rotation_states = sum(x[3] in (1, 2) for x in tails) * seed
    bound_rotation = sum(x[3] == 2 for x in tails) * seed
    complete = sum(x[0] == 6 for x in tails) * seed

    stale_root = sum(x[4] in (2, 3) for x in tails) * seed
    compaction_bad = sum(x[1] == 3 for x in tails) * seed
    verifier_bad = sum(x[2] == 3 for x in tails) * seed
    rotation_bad = sum(x[3] == 3 for x in tails) * seed
    lineage_bad = sum(x[5] == 3 for x in tails) * seed
    continuity_break = sum(x[6] in (2, 3) for x in tails) * seed
    source_bad = sum(x[7] == 3 for x in tails) * seed
    deadline_reset = sum(x[8] != 0 for x in tails) * seed
    bad = (
        stale_root + compaction_bad + verifier_bad + rotation_bad + lineage_bad
        + continuity_break + source_bad + deadline_reset
    )

    checks = [
        _gc33_ok(0, 0, 0, 0, 1, 2, 1, 2, 0),
        _gc33_ok(2, 2, 0, 0, 1, 2, 1, 2, 0),
        _gc33_ok(4, 2, 2, 0, 1, 2, 1, 2, 0),
        _gc33_ok(6, 2, 2, 2, 1, 2, 1, 2, 0),
        not _gc33_ok(6, 3, 2, 2, 1, 2, 1, 2, 0),
        not _gc33_ok(6, 2, 3, 2, 1, 2, 1, 2, 0),
        not _gc33_ok(6, 2, 2, 3, 1, 2, 1, 2, 0),
        not _gc33_ok(6, 2, 2, 2, 2, 2, 1, 2, 0),
        not _gc33_ok(6, 2, 2, 2, 1, 3, 1, 2, 0),
        not _gc33_ok(6, 2, 2, 2, 1, 2, 2, 2, 0),
        not _gc33_ok(6, 2, 2, 2, 1, 2, 1, 3, 0),
        not _gc33_ok(6, 2, 2, 2, 1, 2, 1, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 7) * 3
    patterns = static_patterns * (4 ** 25) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch32_complete_seed_states': seed,
        'delay_vectors': 4 ** 25,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch33_tombstone_compaction_states': compaction_states * z,
        'epoch33_compaction_complete_states': compaction_complete * z,
        'epoch33_verifier_bound_tombstone_compaction_states': verifier_bound_compaction * z,
        'epoch33_verifier_binding_states': verifier_states * z,
        'epoch33_bound_verifier_binding_states': bound_verifier * z,
        'epoch33_reissued_key_rotation_states': rotation_states * z,
        'epoch33_bound_reissued_key_rotation_states': bound_rotation * z,
        'epoch33_complete_states': complete * z,
        'stale_or_conflicting_root_choice_acceptances': stale_root * z,
        'unbound_or_conflicting_tombstone_compaction_acceptances': compaction_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'unbound_or_conflicting_reissued_key_rotation_acceptances': rotation_bad * z,
        'unbound_or_conflicting_reissued_lineage_acceptances': lineage_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'unbound_or_conflicting_source_binding_acceptances': source_bad * z,
        'deadline_reset_acceptances': deadline_reset * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

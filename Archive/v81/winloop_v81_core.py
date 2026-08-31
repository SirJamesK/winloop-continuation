from itertools import product
from math import comb

D = 3
BASE_V80_EPOCH31_COMPLETE_STATIC_STATES = 576


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


def _gc32_ok(phase, failover2, verifier_binding, tombstone_consume,
             root_state, lineage, continuity, source_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        failover2, verifier_binding, tombstone_consume, root_state,
        lineage, continuity, source_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # Root state 2 is stale; continuity state 2 is discontinuous.
    if root_state == 2 or continuity == 2:
        return False

    if phase == 0:
        return (
            failover2, verifier_binding, tombstone_consume,
            root_state, lineage, continuity, source_binding
        ) == (0,) * 7
    if phase == 1:
        if failover2 not in (1, 2):
            return False
        return (
            verifier_binding == 0 and tombstone_consume == 0 and root_state == 1
            and lineage == 2 and continuity == 1
            and source_binding == (1 if failover2 == 1 else 2)
        )
    if phase == 2:
        if verifier_binding not in (1, 2):
            return False
        return (
            failover2 == 2 and tombstone_consume == 0 and root_state == 1
            and lineage == 2 and continuity == 1 and source_binding == 2
        )
    if phase == 3:
        if tombstone_consume not in (1, 2):
            return False
        return (
            failover2 == 2 and verifier_binding == 2 and root_state == 1
            and lineage == 2 and continuity == 1 and source_binding == 2
        )
    if phase == 4:
        return (
            failover2, verifier_binding, tombstone_consume,
            root_state, lineage, continuity, source_binding
        ) == (2, 2, 2, 1, 2, 1, 2)
    return False


def gc32():
    tails = [
        x for x in product(
            range(5), range(4), range(4), range(4), range(4),
            range(4), range(4), range(4), range(3)
        )
        if _gc32_ok(*x)
    ]
    z = q(24)
    seed = BASE_V80_EPOCH31_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    failover_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_failover = sum(x[1] == 2 for x in tails) * seed
    verifier_states = sum(x[2] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[2] == 2 for x in tails) * seed
    consume_states = sum(x[3] in (1, 2) for x in tails) * seed
    bound_consume = sum(x[3] == 2 for x in tails) * seed
    complete = sum(x[0] == 4 for x in tails) * seed

    stale_root = sum(x[4] in (2, 3) for x in tails) * seed
    failover_bad = sum(x[1] == 3 for x in tails) * seed
    verifier_bad = sum(x[2] == 3 for x in tails) * seed
    consume_bad = sum(x[3] == 3 for x in tails) * seed
    lineage_bad = sum(x[5] == 3 for x in tails) * seed
    continuity_break = sum(x[6] in (2, 3) for x in tails) * seed
    source_bad = sum(x[7] == 3 for x in tails) * seed
    deadline_reset = sum(x[8] != 0 for x in tails) * seed
    bad = (
        stale_root + failover_bad + verifier_bad + consume_bad + lineage_bad
        + continuity_break + source_bad + deadline_reset
    )

    checks = [
        _gc32_ok(0, 0, 0, 0, 0, 0, 0, 0, 0),
        _gc32_ok(1, 1, 0, 0, 1, 2, 1, 1, 0),
        _gc32_ok(2, 2, 2, 0, 1, 2, 1, 2, 0),
        _gc32_ok(4, 2, 2, 2, 1, 2, 1, 2, 0),
        not _gc32_ok(4, 3, 2, 2, 1, 2, 1, 2, 0),
        not _gc32_ok(4, 2, 3, 2, 1, 2, 1, 2, 0),
        not _gc32_ok(4, 2, 2, 3, 1, 2, 1, 2, 0),
        not _gc32_ok(4, 2, 2, 2, 2, 2, 1, 2, 0),
        not _gc32_ok(4, 2, 2, 2, 1, 2, 2, 2, 0),
        not _gc32_ok(4, 2, 2, 2, 1, 2, 1, 3, 0),
        not _gc32_ok(4, 2, 2, 2, 1, 2, 1, 2, 1),
    ]

    static_patterns = seed * 5 * (4 ** 7) * 3
    patterns = static_patterns * (4 ** 24) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch31_complete_seed_states': seed,
        'delay_vectors': 4 ** 24,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch32_second_source_failover_states': failover_states * z,
        'epoch32_bound_second_source_failover_states': bound_failover * z,
        'epoch32_verifier_binding_states': verifier_states * z,
        'epoch32_bound_verifier_binding_states': bound_verifier * z,
        'epoch32_old_key_tombstone_consumption_states': consume_states * z,
        'epoch32_bound_old_key_tombstone_consumption_states': bound_consume * z,
        'epoch32_complete_states': complete * z,
        'stale_or_conflicting_root_choice_acceptances': stale_root * z,
        'unbound_or_conflicting_second_source_failover_acceptances': failover_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'unbound_or_conflicting_old_key_tombstone_consumption_acceptances': consume_bad * z,
        'unbound_or_conflicting_reissued_lineage_acceptances': lineage_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'unbound_or_conflicting_source_binding_acceptances': source_bad * z,
        'deadline_reset_acceptances': deadline_reset * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

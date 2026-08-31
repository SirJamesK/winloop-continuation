from itertools import product
from math import comb

D = 3
BASE_V78_LINEAGE_SPLIT_STATIC_STATES = 576


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


def _gc30_ok(phase, split, resolution, retire, reissue, root_state,
             lineage, continuity, deadline_reset):
    # 3 is the unknown/unbound/conflicting marker for trust-bearing evidence.
    if any(x == 3 for x in (split, resolution, retire, reissue, root_state, lineage, continuity)):
        return False
    if deadline_reset != 0:
        return False
    # Root state 2 is stale; continuity state 2 is discontinuous.
    if root_state == 2 or continuity == 2:
        return False

    if phase == 0:
        return (split, resolution, retire, reissue, root_state, lineage, continuity) == (0,) * 7
    if phase == 1:
        return (split, resolution, retire, reissue, root_state, lineage, continuity) == (1, 1, 0, 0, 1, 1, 1)
    if phase == 2:
        return (split, resolution, retire, reissue, root_state, lineage, continuity) == (1, 2, 0, 0, 1, 1, 1)
    if phase == 3:
        return (
            split == 1 and resolution == 2 and retire in (1, 2) and reissue == 0
            and root_state == 1 and lineage == 1 and continuity == 1
        )
    if phase == 4:
        return (
            split == 1 and resolution == 2 and retire == 2 and reissue in (1, 2)
            and root_state == 1 and continuity == 1
            and lineage == (1 if reissue == 1 else 2)
        )
    if phase == 5:
        return (
            split == 1 and resolution == 2 and retire == 2 and reissue == 2
            and root_state == 1 and lineage == 2 and continuity == 1
        )
    return False


def gc30():
    tails = [
        x for x in product(range(6), range(4), range(4), range(4), range(4),
                           range(4), range(4), range(4), range(3))
        if _gc30_ok(*x)
    ]
    z = q(22)
    seed = BASE_V78_LINEAGE_SPLIT_STATIC_STATES
    static_accepted = seed * len(tails)

    split_resolution = sum(x[0] >= 2 for x in tails) * seed
    retirement = sum(x[3] in (1, 2) for x in tails) * seed
    bound_retirement = sum(x[3] == 2 for x in tails) * seed
    reissuance = sum(x[4] in (1, 2) for x in tails) * seed
    bound_reissuance = sum(x[4] == 2 for x in tails) * seed
    complete = sum(x[0] == 5 for x in tails) * seed

    stale_root = sum(x[5] in (2, 3) for x in tails) * seed
    unbound_resolution = sum(x[2] == 3 for x in tails) * seed
    unbound_retirement = sum(x[3] == 3 for x in tails) * seed
    unbound_reissuance = sum(x[4] == 3 for x in tails) * seed
    unbound_lineage = sum(x[6] == 3 for x in tails) * seed
    continuity_break = sum(x[7] in (2, 3) for x in tails) * seed
    deadline_reset = sum(x[8] != 0 for x in tails) * seed
    bad = (
        stale_root + unbound_resolution + unbound_retirement + unbound_reissuance
        + unbound_lineage + continuity_break + deadline_reset
    )

    checks = [
        _gc30_ok(0, 0, 0, 0, 0, 0, 0, 0, 0),
        _gc30_ok(2, 1, 2, 0, 0, 1, 1, 1, 0),
        _gc30_ok(3, 1, 2, 2, 0, 1, 1, 1, 0),
        _gc30_ok(5, 1, 2, 2, 2, 1, 2, 1, 0),
        not _gc30_ok(5, 1, 2, 2, 2, 2, 2, 1, 0),
        not _gc30_ok(5, 1, 3, 2, 2, 1, 2, 1, 0),
        not _gc30_ok(5, 1, 2, 3, 2, 1, 2, 1, 0),
        not _gc30_ok(5, 1, 2, 2, 2, 1, 2, 2, 0),
        not _gc30_ok(5, 1, 2, 2, 2, 1, 2, 1, 1),
    ]

    static_patterns = seed * 6 * (4 ** 7) * 3
    patterns = static_patterns * (4 ** 22) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'source_lineage_seed_states': seed,
        'delay_vectors': 4 ** 22,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch30_lineage_split_resolution_states': split_resolution * z,
        'epoch30_replacement_key_retirement_states': retirement * z,
        'epoch30_bound_replacement_key_retirement_states': bound_retirement * z,
        'epoch30_replacement_key_reissuance_states': reissuance * z,
        'epoch30_bound_replacement_key_reissuance_states': bound_reissuance * z,
        'epoch30_complete_states': complete * z,
        'stale_or_conflicting_root_choice_acceptances': stale_root * z,
        'unbound_or_conflicting_split_resolution_acceptances': unbound_resolution * z,
        'unbound_or_conflicting_key_retirement_acceptances': unbound_retirement * z,
        'unbound_or_conflicting_key_reissuance_acceptances': unbound_reissuance * z,
        'unbound_or_conflicting_reissued_lineage_acceptances': unbound_lineage * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'deadline_reset_acceptances': deadline_reset * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

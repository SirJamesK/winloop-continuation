from itertools import product
from math import comb

D = 3
BASE_V83_EPOCH34_COMPLETE_STATIC_STATES = 576


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


def _gc35_ok(phase, proof_revalidation, proof_root_binding, verifier_binding,
             root_state, lineage, continuity, source_binding,
             rotated_key_binding, third_source_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        proof_revalidation, proof_root_binding, verifier_binding, root_state,
        lineage, continuity, source_binding, rotated_key_binding,
        third_source_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # V83 completed epoch 34 only with the prior root, reissued lineage,
    # continuous tombstone root, bound source/key bindings, and bound third failover.
    if root_state != 1 or lineage != 2 or continuity != 1:
        return False
    if source_binding != 2 or rotated_key_binding != 2 or third_source_binding != 2:
        return False

    if phase == 0:
        return (proof_revalidation, proof_root_binding, verifier_binding) == (0, 0, 0)
    if phase == 1:
        return (proof_revalidation, proof_root_binding, verifier_binding) == (1, 0, 0)
    if phase == 2:
        return (proof_revalidation, proof_root_binding, verifier_binding) == (2, 1, 0)
    if phase == 3:
        return (proof_revalidation, proof_root_binding, verifier_binding) == (2, 2, 0)
    if phase == 4:
        return (proof_revalidation, proof_root_binding, verifier_binding) == (2, 2, 1)
    if phase == 5:
        return (proof_revalidation, proof_root_binding, verifier_binding) == (2, 2, 2)
    return False


def gc35():
    tails = [
        x for x in product(
            range(6), range(4), range(4), range(4), range(4),
            range(4), range(4), range(4), range(4), range(4), range(3)
        )
        if _gc35_ok(*x)
    ]
    z = q(27)
    seed = BASE_V83_EPOCH34_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    proof_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_proof = sum(x[1] == 2 for x in tails) * seed
    root_binding_states = sum(x[2] in (1, 2) for x in tails) * seed
    bound_root_binding = sum(x[2] == 2 for x in tails) * seed
    verifier_states = sum(x[3] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[3] == 2 for x in tails) * seed
    complete = sum(x[0] == 5 for x in tails) * seed

    stale_root = sum(x[4] in (2, 3) for x in tails) * seed
    proof_bad = sum(x[1] == 3 for x in tails) * seed
    root_binding_bad = sum(x[2] == 3 for x in tails) * seed
    verifier_bad = sum(x[3] == 3 for x in tails) * seed
    lineage_bad = sum(x[5] == 3 for x in tails) * seed
    continuity_break = sum(x[6] in (2, 3) for x in tails) * seed
    source_bad = sum(x[7] == 3 for x in tails) * seed
    key_binding_bad = sum(x[8] != 2 for x in tails) * seed
    third_source_bad = sum(x[9] != 2 for x in tails) * seed
    deadline_reset = sum(x[10] != 0 for x in tails) * seed
    bad = (
        stale_root + proof_bad + root_binding_bad + verifier_bad + lineage_bad
        + continuity_break + source_bad + key_binding_bad + third_source_bad
        + deadline_reset
    )

    checks = [
        _gc35_ok(0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc35_ok(2, 2, 1, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc35_ok(3, 2, 2, 0, 1, 2, 1, 2, 2, 2, 0),
        _gc35_ok(5, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc35_ok(5, 3, 2, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc35_ok(5, 2, 3, 2, 1, 2, 1, 2, 2, 2, 0),
        not _gc35_ok(5, 2, 2, 3, 1, 2, 1, 2, 2, 2, 0),
        not _gc35_ok(5, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0),
        not _gc35_ok(5, 2, 2, 2, 1, 3, 1, 2, 2, 2, 0),
        not _gc35_ok(5, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc35_ok(5, 2, 2, 2, 1, 2, 1, 3, 2, 2, 0),
        not _gc35_ok(5, 2, 2, 2, 1, 2, 1, 2, 1, 2, 0),
        not _gc35_ok(5, 2, 2, 2, 1, 2, 1, 2, 2, 1, 0),
        not _gc35_ok(5, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1),
    ]

    static_patterns = seed * 6 * (4 ** 9) * 3
    patterns = static_patterns * (4 ** 27) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'epoch34_complete_seed_states': seed,
        'delay_vectors': 4 ** 27,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch35_compacted_tombstone_proof_revalidation_states': proof_states * z,
        'epoch35_bound_proof_revalidation_states': bound_proof * z,
        'epoch35_proof_root_binding_states': root_binding_states * z,
        'epoch35_bound_proof_root_binding_states': bound_root_binding * z,
        'epoch35_verifier_binding_states': verifier_states * z,
        'epoch35_bound_verifier_binding_states': bound_verifier * z,
        'epoch35_complete_states': complete * z,
        'stale_or_conflicting_root_choice_acceptances': stale_root * z,
        'unbound_or_conflicting_proof_revalidation_acceptances': proof_bad * z,
        'unbound_or_conflicting_proof_root_binding_acceptances': root_binding_bad * z,
        'unbound_or_conflicting_verifier_binding_acceptances': verifier_bad * z,
        'unbound_or_conflicting_reissued_lineage_acceptances': lineage_bad * z,
        'tombstone_root_discontinuity_acceptances': continuity_break * z,
        'unbound_or_conflicting_source_binding_acceptances': source_bad * z,
        'unbound_or_conflicting_rotated_key_binding_acceptances': key_binding_bad * z,
        'unbound_or_conflicting_third_source_binding_acceptances': third_source_bad * z,
        'deadline_reset_acceptances': deadline_reset * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

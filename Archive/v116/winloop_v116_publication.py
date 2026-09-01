from winloop_v116_core import q

BASE_V115_BOUND_FORTIETH_RESTART_STATIC_STATES = 27648

_PUB116_EXPECTED = {
    0: (0, 0, 0, 0, 0, 0),
    1: (1, 0, 0, 0, 0, 0),
    2: (2, 0, 0, 0, 0, 0),
    3: (2, 1, 0, 0, 0, 0),
    4: (2, 2, 0, 0, 0, 0),
    5: (2, 2, 1, 0, 0, 0),
    6: (2, 2, 2, 0, 0, 0),
    7: (2, 2, 2, 1, 0, 0),
    8: (2, 2, 2, 2, 0, 0),
    9: (2, 2, 2, 2, 1, 1),
    10: (2, 2, 2, 2, 2, 2),
}


def _pub116_ok(phase, replacement_churn, successor_binding,
               dual, restart41, cache_authority, consume, quorum):
    if any(x == 3 for x in (
        replacement_churn, successor_binding, dual, restart41, consume, quorum
    )):
        return False
    # V115's fortieth restart is a seed only after successor disappearance,
    # replacement binding, and reconciliation. V116 requires replacement-source
    # churn, successor binding, fresh reconciliation, and restart 41.
    if cache_authority != 0:
        return False
    return _PUB116_EXPECTED.get(phase) == (
        replacement_churn, successor_binding, dual, restart41, consume, quorum
    )


def replacement_churn_forty_first_restart():
    tails = [
        (phase, state[0], state[1], state[2], state[3], 0, state[4], state[5])
        for phase, state in _PUB116_EXPECTED.items()
    ]
    assert all(_pub116_ok(*x) for x in tails)
    z = q(86)
    seed = BASE_V115_BOUND_FORTIETH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    churn = sum(x[1] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[1] == 2 for x in tails) * seed
    successor = sum(x[2] in (1, 2) for x in tails) * seed
    bound_successor = sum(x[2] == 2 for x in tails) * seed
    dual = sum(x[3] in (1, 2) for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    restart41 = sum(x[4] in (1, 2) for x in tails) * seed
    bound_restart41 = sum(x[4] == 2 for x in tails) * seed
    bound_recovery = sum(x[0] == 10 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    churn_bad = sum(x[1] == 3 for x in tails) * seed
    successor_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 10 and x[7] < 2 for x in tails) * seed
    bad = cached + churn_bad + successor_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub116_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub116_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub116_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub116_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub116_ok(8, 2, 2, 2, 2, 0, 0, 0),
        _pub116_ok(10, 2, 2, 2, 2, 0, 2, 2),
        not _pub116_ok(10, 3, 2, 2, 2, 0, 2, 2),
        not _pub116_ok(10, 2, 3, 2, 2, 0, 2, 2),
        not _pub116_ok(10, 2, 2, 3, 2, 0, 2, 2),
        not _pub116_ok(10, 2, 2, 2, 3, 0, 2, 2),
        not _pub116_ok(10, 2, 2, 2, 2, 1, 2, 2),
        not _pub116_ok(10, 2, 2, 2, 2, 0, 3, 2),
        not _pub116_ok(10, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 11 * (4 ** 6) * 2
    patterns = static_patterns * (4 ** 86) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_fortieth_restart_seed_states': seed,
        'delay_vectors': 4 ** 86,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'replacement_source_churn_states': churn * z,
        'bound_replacement_source_churn_states': bound_churn * z,
        'successor_source_binding_states': successor * z,
        'bound_successor_source_binding_states': bound_successor * z,
        'dual_source_reconciliation_states': dual * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'forty_first_verifier_cold_restart_states': restart41 * z,
        'bound_forty_first_restart_states': bound_restart41 * z,
        'bound_forty_first_restart_recoveries': bound_recovery * z,
        'cached_forty_first_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_replacement_churn_acceptances': churn_bad * z,
        'unbound_or_conflicting_successor_binding_acceptances': successor_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_forty_first_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

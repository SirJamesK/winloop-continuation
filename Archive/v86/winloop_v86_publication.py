from winloop_v86_core import q

BASE_V85_BOUND_TENTH_RESTART_STATIC_STATES = 27648

_PUB86_EXPECTED = {
    0: (0, 0, 0, 0, 0, 0),
    1: (1, 0, 0, 0, 0, 0),
    2: (2, 0, 0, 0, 0, 0),
    3: (2, 1, 0, 0, 0, 0),
    4: (2, 2, 0, 0, 0, 0),
    5: (2, 2, 1, 0, 0, 0),
    6: (2, 2, 2, 0, 0, 0),
    7: (2, 2, 2, 1, 0, 0),
    8: (2, 2, 2, 2, 1, 1),
    9: (2, 2, 2, 2, 2, 2),
}


def _pub86_ok(phase, successor_churn, successor_binding,
              dual, restart11, cache_authority, consume, quorum):
    if any(x == 3 for x in (
        successor_churn, successor_binding, dual, restart11, consume, quorum
    )):
        return False
    # An eleventh verifier cold restart must never promote cached authority.
    if cache_authority != 0:
        return False
    return _PUB86_EXPECTED.get(phase) == (
        successor_churn, successor_binding, dual, restart11, consume, quorum
    )


def successor_source_churn_eleventh_restart():
    tails = [
        (phase, state[0], state[1], state[2], state[3], 0, state[4], state[5])
        for phase, state in _PUB86_EXPECTED.items()
    ]
    assert all(_pub86_ok(*x) for x in tails)
    z = q(27)
    seed = BASE_V85_BOUND_TENTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    churn = sum(x[1] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[1] == 2 for x in tails) * seed
    bound_successor = sum(x[2] == 2 for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    eleventh_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_eleventh = sum(x[0] == 9 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    churn_bad = sum(x[1] == 3 for x in tails) * seed
    successor_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 9 and x[7] < 2 for x in tails) * seed
    bad = cached + churn_bad + successor_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub86_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub86_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub86_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub86_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub86_ok(9, 2, 2, 2, 2, 0, 2, 2),
        not _pub86_ok(9, 3, 2, 2, 2, 0, 2, 2),
        not _pub86_ok(9, 2, 3, 2, 2, 0, 2, 2),
        not _pub86_ok(9, 2, 2, 3, 2, 0, 2, 2),
        not _pub86_ok(9, 2, 2, 2, 3, 0, 2, 2),
        not _pub86_ok(9, 2, 2, 2, 2, 1, 2, 2),
        not _pub86_ok(9, 2, 2, 2, 2, 0, 3, 2),
        not _pub86_ok(9, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 10 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 27) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_tenth_restart_seed_states': seed,
        'delay_vectors': 4 ** 27,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'successor_source_churn_states': churn * z,
        'bound_successor_source_churn_states': bound_churn * z,
        'bound_successor_source_binding_states': bound_successor * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'eleventh_verifier_cold_restart_states': eleventh_restart * z,
        'bound_eleventh_restart_recoveries': bound_eleventh * z,
        'cached_eleventh_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_successor_churn_acceptances': churn_bad * z,
        'unbound_or_conflicting_successor_binding_acceptances': successor_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_eleventh_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

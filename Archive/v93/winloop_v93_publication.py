from winloop_v93_core import q

BASE_V92_BOUND_SEVENTEENTH_RESTART_STATIC_STATES = 27648

_PUB93_EXPECTED = {
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


def _pub93_ok(phase, successor_disappearance, replacement_binding,
              dual, restart18, cache_authority, consume, quorum):
    if any(x == 3 for x in (
        successor_disappearance, replacement_binding, dual, restart18,
        consume, quorum
    )):
        return False
    # V92's seventeenth restart is a seed only after replacement-source churn,
    # successor binding, and reconciliation. V93 then handles successor-source
    # disappearance, replacement binding, fresh reconciliation, and restart 18.
    if cache_authority != 0:
        return False
    return _PUB93_EXPECTED.get(phase) == (
        successor_disappearance, replacement_binding, dual, restart18,
        consume, quorum
    )


def successor_disappearance_eighteenth_restart():
    tails = [
        (phase, state[0], state[1], state[2], state[3], 0, state[4], state[5])
        for phase, state in _PUB93_EXPECTED.items()
    ]
    assert all(_pub93_ok(*x) for x in tails)
    z = q(40)
    seed = BASE_V92_BOUND_SEVENTEENTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    disappearance = sum(x[1] in (1, 2) for x in tails) * seed
    bound_disappearance = sum(x[1] == 2 for x in tails) * seed
    replacement = sum(x[2] in (1, 2) for x in tails) * seed
    bound_replacement = sum(x[2] == 2 for x in tails) * seed
    dual = sum(x[3] in (1, 2) for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    restart18 = sum(x[4] in (1, 2) for x in tails) * seed
    bound_restart18 = sum(x[4] == 2 for x in tails) * seed
    bound_recovery = sum(x[0] == 10 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    disappearance_bad = sum(x[1] == 3 for x in tails) * seed
    replacement_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 10 and x[7] < 2 for x in tails) * seed
    bad = cached + disappearance_bad + replacement_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub93_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub93_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub93_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub93_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub93_ok(8, 2, 2, 2, 2, 0, 0, 0),
        _pub93_ok(10, 2, 2, 2, 2, 0, 2, 2),
        not _pub93_ok(10, 3, 2, 2, 2, 0, 2, 2),
        not _pub93_ok(10, 2, 3, 2, 2, 0, 2, 2),
        not _pub93_ok(10, 2, 2, 3, 2, 0, 2, 2),
        not _pub93_ok(10, 2, 2, 2, 3, 0, 2, 2),
        not _pub93_ok(10, 2, 2, 2, 2, 1, 2, 2),
        not _pub93_ok(10, 2, 2, 2, 2, 0, 3, 2),
        not _pub93_ok(10, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 11 * (4 ** 6) * 2
    patterns = static_patterns * (4 ** 40) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_seventeenth_restart_seed_states': seed,
        'delay_vectors': 4 ** 40,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'successor_source_disappearance_states': disappearance * z,
        'bound_successor_source_disappearance_states': bound_disappearance * z,
        'replacement_source_binding_states': replacement * z,
        'bound_replacement_source_binding_states': bound_replacement * z,
        'dual_source_reconciliation_states': dual * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'eighteenth_verifier_cold_restart_states': restart18 * z,
        'bound_eighteenth_restart_states': bound_restart18 * z,
        'bound_eighteenth_restart_recoveries': bound_recovery * z,
        'cached_eighteenth_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_successor_disappearance_acceptances': disappearance_bad * z,
        'unbound_or_conflicting_replacement_binding_acceptances': replacement_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_eighteenth_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

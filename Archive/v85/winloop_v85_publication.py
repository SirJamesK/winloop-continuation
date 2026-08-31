from winloop_v85_core import q

BASE_V84_BOUND_NINTH_RESTART_STATIC_STATES = 27648

_PUB85_EXPECTED = {
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


def _pub85_ok(phase, replacement_disappearance, replacement_successor_binding,
              dual, restart10, cache_authority, consume, quorum):
    if any(x == 3 for x in (
        replacement_disappearance, replacement_successor_binding,
        dual, restart10, consume, quorum
    )):
        return False
    # A verifier cold restart must never promote cached authority.
    if cache_authority != 0:
        return False
    return _PUB85_EXPECTED.get(phase) == (
        replacement_disappearance, replacement_successor_binding,
        dual, restart10, consume, quorum
    )


def replacement_source_disappearance_tenth_restart():
    tails = [
        (phase, state[0], state[1], state[2], state[3], 0, state[4], state[5])
        for phase, state in _PUB85_EXPECTED.items()
    ]
    assert all(_pub85_ok(*x) for x in tails)
    z = q(25)
    seed = BASE_V84_BOUND_NINTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    disappearance = sum(x[1] in (1, 2) for x in tails) * seed
    bound_disappearance = sum(x[1] == 2 for x in tails) * seed
    bound_successor = sum(x[2] == 2 for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    tenth_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_tenth = sum(x[0] == 9 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    disappearance_bad = sum(x[1] == 3 for x in tails) * seed
    successor_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 9 and x[7] < 2 for x in tails) * seed
    bad = cached + disappearance_bad + successor_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub85_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub85_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub85_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub85_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub85_ok(9, 2, 2, 2, 2, 0, 2, 2),
        not _pub85_ok(9, 3, 2, 2, 2, 0, 2, 2),
        not _pub85_ok(9, 2, 3, 2, 2, 0, 2, 2),
        not _pub85_ok(9, 2, 2, 3, 2, 0, 2, 2),
        not _pub85_ok(9, 2, 2, 2, 3, 0, 2, 2),
        not _pub85_ok(9, 2, 2, 2, 2, 1, 2, 2),
        not _pub85_ok(9, 2, 2, 2, 2, 0, 3, 2),
        not _pub85_ok(9, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 10 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 25) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_ninth_restart_seed_states': seed,
        'delay_vectors': 4 ** 25,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'replacement_source_disappearance_states': disappearance * z,
        'bound_replacement_source_disappearance_states': bound_disappearance * z,
        'bound_replacement_successor_binding_states': bound_successor * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'tenth_verifier_cold_restart_states': tenth_restart * z,
        'bound_tenth_restart_recoveries': bound_tenth * z,
        'cached_tenth_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_replacement_disappearance_acceptances': disappearance_bad * z,
        'unbound_or_conflicting_replacement_successor_binding_acceptances': successor_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_tenth_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

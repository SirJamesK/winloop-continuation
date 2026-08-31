from winloop_v90_core import q

BASE_V89_BOUND_FOURTEENTH_RESTART_STATIC_STATES = 27648

_PUB90_EXPECTED = {
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


def _pub90_ok(phase, replacement_churn, successor_binding,
              dual, restart15, cache_authority, consume, quorum):
    if any(x == 3 for x in (
        replacement_churn, successor_binding, dual, restart15, consume, quorum
    )):
        return False
    # V89's fourteenth restart is a seed only when it completed against a newly
    # replaced and reconciled source set. V90 requires another replacement-source
    # churn, successor binding, and re-reconciliation before the fifteenth cold
    # verifier restart. Cached verifier state never promotes to authority.
    if cache_authority != 0:
        return False
    return _PUB90_EXPECTED.get(phase) == (
        replacement_churn, successor_binding, dual, restart15, consume, quorum
    )


def replacement_churn_fifteenth_restart():
    tails = [
        (phase, state[0], state[1], state[2], state[3], 0, state[4], state[5])
        for phase, state in _PUB90_EXPECTED.items()
    ]
    assert all(_pub90_ok(*x) for x in tails)
    z = q(34)
    seed = BASE_V89_BOUND_FOURTEENTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    churn = sum(x[1] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[1] == 2 for x in tails) * seed
    successor = sum(x[2] in (1, 2) for x in tails) * seed
    bound_successor = sum(x[2] == 2 for x in tails) * seed
    dual = sum(x[3] in (1, 2) for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    restart15 = sum(x[4] in (1, 2) for x in tails) * seed
    bound_restart15 = sum(x[4] == 2 for x in tails) * seed
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
        _pub90_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub90_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub90_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub90_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub90_ok(8, 2, 2, 2, 2, 0, 0, 0),
        _pub90_ok(10, 2, 2, 2, 2, 0, 2, 2),
        not _pub90_ok(10, 3, 2, 2, 2, 0, 2, 2),
        not _pub90_ok(10, 2, 3, 2, 2, 0, 2, 2),
        not _pub90_ok(10, 2, 2, 3, 2, 0, 2, 2),
        not _pub90_ok(10, 2, 2, 2, 3, 0, 2, 2),
        not _pub90_ok(10, 2, 2, 2, 2, 1, 2, 2),
        not _pub90_ok(10, 2, 2, 2, 2, 0, 3, 2),
        not _pub90_ok(10, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 11 * (4 ** 6) * 2
    patterns = static_patterns * (4 ** 34) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_fourteenth_restart_seed_states': seed,
        'delay_vectors': 4 ** 34,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'replacement_source_churn_states': churn * z,
        'bound_replacement_source_churn_states': bound_churn * z,
        'successor_source_binding_states': successor * z,
        'bound_successor_source_binding_states': bound_successor * z,
        'dual_source_reconciliation_states': dual * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'fifteenth_verifier_cold_restart_states': restart15 * z,
        'bound_fifteenth_restart_states': bound_restart15 * z,
        'bound_fifteenth_restart_recoveries': bound_recovery * z,
        'cached_fifteenth_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_replacement_churn_acceptances': churn_bad * z,
        'unbound_or_conflicting_successor_binding_acceptances': successor_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_fifteenth_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

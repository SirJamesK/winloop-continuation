from itertools import product
from winloop_v80_core import q

BASE_V79_BOUND_FOURTH_RESTART_STATIC_STATES = 27648


def _pub80_ok(phase, rollback, binding, dual, restart5, cache_authority, consume, quorum):
    if any(x == 3 for x in (rollback, binding, dual, restart5, consume, quorum)):
        return False
    # Cold-restart recovery never promotes cached verifier authority.
    if cache_authority != 0:
        return False

    if phase == 0:
        return (rollback, binding, dual, restart5, consume, quorum) == (0,) * 6
    if phase == 1:
        return (rollback, binding, dual, restart5, consume, quorum) == (1, 0, 0, 0, 0, 0)
    if phase == 2:
        return (rollback, binding, dual, restart5, consume, quorum) == (2, 1, 0, 0, 0, 0)
    if phase == 3:
        return (rollback, binding, dual, restart5, consume, quorum) == (2, 2, 1, 0, 0, 0)
    if phase == 4:
        return (rollback, binding, dual, restart5, consume, quorum) == (2, 2, 2, 1, 0, 0)
    if phase == 5:
        return (rollback, binding, dual, restart5, consume, quorum) == (2, 2, 2, 2, 1, 1)
    if phase == 6:
        return (rollback, binding, dual, restart5, consume, quorum) == (2, 2, 2, 2, 2, 2)
    return False


def reconciliation_rollback_fifth_restart():
    tails = [
        x for x in product(
            range(7), range(4), range(4), range(4), range(4),
            range(3), range(4), range(4)
        )
        if _pub80_ok(*x)
    ]
    z = q(20)
    seed = BASE_V79_BOUND_FOURTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    rollback_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rollback = sum(x[1] == 2 for x in tails) * seed
    bound_binding = sum(x[2] == 2 for x in tails) * seed
    fifth_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_fifth_recovery = sum(x[0] == 6 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    rollback_bad = sum(x[1] == 3 for x in tails) * seed
    binding_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 6 and x[7] < 2 for x in tails) * seed
    bad = cached + rollback_bad + binding_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub80_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub80_ok(2, 2, 1, 0, 0, 0, 0, 0),
        _pub80_ok(4, 2, 2, 2, 1, 0, 0, 0),
        _pub80_ok(6, 2, 2, 2, 2, 0, 2, 2),
        not _pub80_ok(6, 3, 2, 2, 2, 0, 2, 2),
        not _pub80_ok(6, 2, 3, 2, 2, 0, 2, 2),
        not _pub80_ok(6, 2, 2, 3, 2, 0, 2, 2),
        not _pub80_ok(6, 2, 2, 2, 3, 0, 2, 2),
        not _pub80_ok(6, 2, 2, 2, 2, 1, 2, 2),
        not _pub80_ok(6, 2, 2, 2, 2, 0, 3, 2),
        not _pub80_ok(6, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 20) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_fourth_restart_seed_states': seed,
        'delay_vectors': 4 ** 20,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'reconciliation_rollback_states': rollback_states * z,
        'bound_reconciliation_rollback_states': bound_rollback * z,
        'bound_rollback_source_binding_states': bound_binding * z,
        'fifth_verifier_cold_restart_states': fifth_restart * z,
        'bound_fifth_restart_recoveries': bound_fifth_recovery * z,
        'cached_fifth_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_reconciliation_rollback_acceptances': rollback_bad * z,
        'unbound_or_conflicting_rollback_source_binding_acceptances': binding_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_fifth_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

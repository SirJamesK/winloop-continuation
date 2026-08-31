from itertools import product
from winloop_v82_core import q

BASE_V81_BOUND_SIXTH_RESTART_STATIC_STATES = 27648


def _pub82_ok(phase, source_rollback, binding, dual, restart7, cache_authority, consume, quorum):
    if any(x == 3 for x in (source_rollback, binding, dual, restart7, consume, quorum)):
        return False
    # Cold-restart recovery never promotes cached verifier authority.
    if cache_authority != 0:
        return False

    if phase == 0:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (0, 0, 0, 0, 0, 0)
    if phase == 1:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (1, 0, 0, 0, 0, 0)
    if phase == 2:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 0, 0, 0, 0, 0)
    if phase == 3:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 1, 0, 0, 0, 0)
    if phase == 4:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 2, 0, 0, 0, 0)
    if phase == 5:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 2, 1, 0, 0, 0)
    if phase == 6:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 2, 2, 0, 0, 0)
    if phase == 7:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 2, 2, 1, 0, 0)
    if phase == 8:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 2, 2, 2, 1, 1)
    if phase == 9:
        return (source_rollback, binding, dual, restart7, consume, quorum) == (2, 2, 2, 2, 2, 2)
    return False


def replacement_source_rollback_seventh_restart():
    tails = [
        x for x in product(
            range(10), range(4), range(4), range(4), range(4),
            range(3), range(4), range(4)
        )
        if _pub82_ok(*x)
    ]
    z = q(22)
    seed = BASE_V81_BOUND_SIXTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    rollback_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rollback = sum(x[1] == 2 for x in tails) * seed
    bound_binding = sum(x[2] == 2 for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    seventh_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_seventh = sum(x[0] == 9 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    rollback_bad = sum(x[1] == 3 for x in tails) * seed
    binding_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 9 and x[7] < 2 for x in tails) * seed
    bad = cached + rollback_bad + binding_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub82_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub82_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub82_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub82_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub82_ok(9, 2, 2, 2, 2, 0, 2, 2),
        not _pub82_ok(9, 3, 2, 2, 2, 0, 2, 2),
        not _pub82_ok(9, 2, 3, 2, 2, 0, 2, 2),
        not _pub82_ok(9, 2, 2, 3, 2, 0, 2, 2),
        not _pub82_ok(9, 2, 2, 2, 3, 0, 2, 2),
        not _pub82_ok(9, 2, 2, 2, 2, 1, 2, 2),
        not _pub82_ok(9, 2, 2, 2, 2, 0, 3, 2),
        not _pub82_ok(9, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 10 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 22) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_sixth_restart_seed_states': seed,
        'delay_vectors': 4 ** 22,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'replacement_source_rollback_states': rollback_states * z,
        'bound_replacement_source_rollback_states': bound_rollback * z,
        'bound_replacement_source_binding_states': bound_binding * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'seventh_verifier_cold_restart_states': seventh_restart * z,
        'bound_seventh_restart_recoveries': bound_seventh * z,
        'cached_seventh_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_replacement_source_rollback_acceptances': rollback_bad * z,
        'unbound_or_conflicting_replacement_source_binding_acceptances': binding_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_seventh_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

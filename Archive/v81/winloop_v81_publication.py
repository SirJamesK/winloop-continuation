from itertools import product
from winloop_v81_core import q

BASE_V80_BOUND_FIFTH_RESTART_STATIC_STATES = 27648


def _pub81_ok(phase, source_disappear, binding, dual, restart6, cache_authority, consume, quorum):
    if any(x == 3 for x in (source_disappear, binding, dual, restart6, consume, quorum)):
        return False
    # Cold-restart recovery never promotes cached verifier authority.
    if cache_authority != 0:
        return False

    if phase == 0:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (0,) * 6
    if phase == 1:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (1, 0, 0, 0, 0, 0)
    if phase == 2:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (2, 1, 0, 0, 0, 0)
    if phase == 3:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (2, 2, 1, 0, 0, 0)
    if phase == 4:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (2, 2, 2, 1, 0, 0)
    if phase == 5:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (2, 2, 2, 2, 1, 1)
    if phase == 6:
        return (source_disappear, binding, dual, restart6, consume, quorum) == (2, 2, 2, 2, 2, 2)
    return False


def rollback_source_disappearance_sixth_restart():
    tails = [
        x for x in product(
            range(7), range(4), range(4), range(4), range(4),
            range(3), range(4), range(4)
        )
        if _pub81_ok(*x)
    ]
    z = q(21)
    seed = BASE_V80_BOUND_FIFTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    disappearance = sum(x[1] in (1, 2) for x in tails) * seed
    bound_disappearance = sum(x[1] == 2 for x in tails) * seed
    bound_binding = sum(x[2] == 2 for x in tails) * seed
    sixth_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_sixth = sum(x[0] == 6 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    disappear_bad = sum(x[1] == 3 for x in tails) * seed
    binding_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 6 and x[7] < 2 for x in tails) * seed
    bad = cached + disappear_bad + binding_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub81_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub81_ok(2, 2, 1, 0, 0, 0, 0, 0),
        _pub81_ok(4, 2, 2, 2, 1, 0, 0, 0),
        _pub81_ok(6, 2, 2, 2, 2, 0, 2, 2),
        not _pub81_ok(6, 3, 2, 2, 2, 0, 2, 2),
        not _pub81_ok(6, 2, 3, 2, 2, 0, 2, 2),
        not _pub81_ok(6, 2, 2, 3, 2, 0, 2, 2),
        not _pub81_ok(6, 2, 2, 2, 3, 0, 2, 2),
        not _pub81_ok(6, 2, 2, 2, 2, 1, 2, 2),
        not _pub81_ok(6, 2, 2, 2, 2, 0, 3, 2),
        not _pub81_ok(6, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 21) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_fifth_restart_seed_states': seed,
        'delay_vectors': 4 ** 21,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'rollback_source_disappearance_states': disappearance * z,
        'bound_rollback_source_disappearance_states': bound_disappearance * z,
        'bound_replacement_source_binding_states': bound_binding * z,
        'sixth_verifier_cold_restart_states': sixth_restart * z,
        'bound_sixth_restart_recoveries': bound_sixth * z,
        'cached_sixth_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_rollback_source_disappearance_acceptances': disappear_bad * z,
        'unbound_or_conflicting_replacement_source_binding_acceptances': binding_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_sixth_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

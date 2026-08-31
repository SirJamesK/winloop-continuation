from itertools import product
from winloop_v79_core import q

BASE_V78_BOUND_THIRD_RESTART_STATIC_STATES = 27648


def _pub79_ok(phase, dual, reconcile, binding, restart4, cache_authority, consume, quorum):
    if any(x == 3 for x in (dual, reconcile, binding, restart4, consume, quorum)):
        return False
    # A cold verifier never promotes cached authority.
    if cache_authority != 0:
        return False

    if phase == 0:
        return (dual, reconcile, binding, restart4, consume, quorum) == (0,) * 6
    if phase == 1:
        return (dual, reconcile, binding, restart4, consume, quorum) == (1, 0, 0, 0, 0, 0)
    if phase == 2:
        return (dual, reconcile, binding, restart4, consume, quorum) == (2, 1, 0, 0, 0, 0)
    if phase == 3:
        return (dual, reconcile, binding, restart4, consume, quorum) == (2, 2, 2, 0, 0, 0)
    if phase == 4:
        return (dual, reconcile, binding, restart4, consume, quorum) == (2, 2, 2, 1, 0, 0)
    if phase == 5:
        return (dual, reconcile, binding, restart4, consume, quorum) == (2, 2, 2, 2, 1, 1)
    if phase == 6:
        return (dual, reconcile, binding, restart4, consume, quorum) == (2, 2, 2, 2, 2, 2)
    return False


def dual_source_fourth_restart():
    tails = [
        x for x in product(range(7), range(4), range(4), range(4), range(4),
                           range(3), range(4), range(4))
        if _pub79_ok(*x)
    ]
    z = q(19)
    seed = BASE_V78_BOUND_THIRD_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    reconciliation = sum(x[0] >= 2 for x in tails) * seed
    bound_reconciliation = sum(x[0] >= 3 for x in tails) * seed
    fourth_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_fourth_recovery = sum(x[0] == 6 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    recon_bad = sum(x[2] == 3 for x in tails) * seed
    binding_bad = sum(x[3] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 6 and x[7] < 2 for x in tails) * seed
    bad = cached + recon_bad + binding_bad + consume_bad + below_quorum

    checks = [
        _pub79_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub79_ok(3, 2, 2, 2, 0, 0, 0, 0),
        _pub79_ok(4, 2, 2, 2, 1, 0, 0, 0),
        _pub79_ok(6, 2, 2, 2, 2, 0, 2, 2),
        not _pub79_ok(6, 2, 2, 2, 3, 0, 2, 2),
        not _pub79_ok(6, 2, 3, 2, 2, 0, 2, 2),
        not _pub79_ok(6, 2, 2, 3, 2, 0, 2, 2),
        not _pub79_ok(6, 2, 2, 2, 2, 1, 2, 2),
        not _pub79_ok(6, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 19) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_third_restart_seed_states': seed,
        'delay_vectors': 4 ** 19,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'dual_source_reconciliation_states': reconciliation * z,
        'bound_dual_source_reconciliation_states': bound_reconciliation * z,
        'fourth_verifier_cold_restart_states': fourth_restart * z,
        'bound_fourth_restart_recoveries': bound_fourth_recovery * z,
        'cached_fourth_restart_authority_acceptances': cached * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': recon_bad * z,
        'unbound_or_conflicting_dual_source_binding_acceptances': binding_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

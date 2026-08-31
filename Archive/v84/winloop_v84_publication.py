from itertools import product
from winloop_v84_core import q

BASE_V83_BOUND_EIGHTH_RESTART_STATIC_STATES = 27648


def _pub84_ok(phase, successor_churn, successor_replacement_binding, dual,
              restart9, cache_authority, consume, quorum):
    if any(x == 3 for x in (
        successor_churn, successor_replacement_binding, dual, restart9, consume, quorum
    )):
        return False
    # A verifier cold restart must not promote cached authority.
    if cache_authority != 0:
        return False

    if phase == 0:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (0, 0, 0, 0, 0, 0)
    if phase == 1:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (1, 0, 0, 0, 0, 0)
    if phase == 2:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 0, 0, 0, 0, 0)
    if phase == 3:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 1, 0, 0, 0, 0)
    if phase == 4:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 2, 0, 0, 0, 0)
    if phase == 5:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 2, 1, 0, 0, 0)
    if phase == 6:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 2, 2, 0, 0, 0)
    if phase == 7:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 2, 2, 1, 0, 0)
    if phase == 8:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 2, 2, 2, 1, 1)
    if phase == 9:
        return (successor_churn, successor_replacement_binding, dual, restart9, consume, quorum) == (2, 2, 2, 2, 2, 2)
    return False


def successor_source_churn_ninth_restart():
    tails = [
        x for x in product(
            range(10), range(4), range(4), range(4), range(4),
            range(3), range(4), range(4)
        )
        if _pub84_ok(*x)
    ]
    z = q(24)
    seed = BASE_V83_BOUND_EIGHTH_RESTART_STATIC_STATES
    static_accepted = seed * len(tails)

    churn = sum(x[1] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[1] == 2 for x in tails) * seed
    bound_replacement = sum(x[2] == 2 for x in tails) * seed
    bound_dual = sum(x[3] == 2 for x in tails) * seed
    ninth_restart = sum(x[4] in (1, 2) for x in tails) * seed
    bound_ninth = sum(x[0] == 9 for x in tails) * seed

    cached = sum(x[5] != 0 for x in tails) * seed
    churn_bad = sum(x[1] == 3 for x in tails) * seed
    replacement_bad = sum(x[2] == 3 for x in tails) * seed
    dual_bad = sum(x[3] == 3 for x in tails) * seed
    restart_bad = sum(x[4] == 3 for x in tails) * seed
    consume_bad = sum(x[6] == 3 for x in tails) * seed
    below_quorum = sum(x[0] == 9 and x[7] < 2 for x in tails) * seed
    bad = cached + churn_bad + replacement_bad + dual_bad + restart_bad + consume_bad + below_quorum

    checks = [
        _pub84_ok(0, 0, 0, 0, 0, 0, 0, 0),
        _pub84_ok(2, 2, 0, 0, 0, 0, 0, 0),
        _pub84_ok(4, 2, 2, 0, 0, 0, 0, 0),
        _pub84_ok(6, 2, 2, 2, 0, 0, 0, 0),
        _pub84_ok(9, 2, 2, 2, 2, 0, 2, 2),
        not _pub84_ok(9, 3, 2, 2, 2, 0, 2, 2),
        not _pub84_ok(9, 2, 3, 2, 2, 0, 2, 2),
        not _pub84_ok(9, 2, 2, 3, 2, 0, 2, 2),
        not _pub84_ok(9, 2, 2, 2, 3, 0, 2, 2),
        not _pub84_ok(9, 2, 2, 2, 2, 1, 2, 2),
        not _pub84_ok(9, 2, 2, 2, 2, 0, 3, 2),
        not _pub84_ok(9, 2, 2, 2, 2, 0, 2, 1),
    ]

    static_patterns = seed * 10 * (4 ** 6) * 3
    patterns = static_patterns * (4 ** 24) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_eighth_restart_seed_states': seed,
        'delay_vectors': 4 ** 24,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'successor_source_churn_states': churn * z,
        'bound_successor_source_churn_states': bound_churn * z,
        'bound_successor_replacement_binding_states': bound_replacement * z,
        'bound_dual_source_reconciliation_states': bound_dual * z,
        'ninth_verifier_cold_restart_states': ninth_restart * z,
        'bound_ninth_restart_recoveries': bound_ninth * z,
        'cached_ninth_restart_authority_acceptances': cached * z,
        'unbound_or_conflicting_successor_churn_acceptances': churn_bad * z,
        'unbound_or_conflicting_successor_replacement_binding_acceptances': replacement_bad * z,
        'unbound_or_forked_dual_source_reconciliation_acceptances': dual_bad * z,
        'unbound_or_conflicting_ninth_restart_acceptances': restart_bad * z,
        'unbound_or_forked_reconciliation_consumption_acceptances': consume_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

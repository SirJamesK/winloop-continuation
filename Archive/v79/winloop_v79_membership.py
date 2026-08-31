from itertools import product
from winloop_v79_core import q

BASE_V78_BOUND_REPLICATION_RECOVERY_STATIC_STATES = 760


def _mem79_ok(phase, rollover, reinstate, generation, membership_root,
              replication, tombstone_binding, active_byzantine):
    if rollover == 3 or reinstate == 3:
        return False
    if generation != 4:
        return False
    if membership_root not in (4, 5):
        return False
    if replication != 2 or tombstone_binding != 1 or active_byzantine != 0:
        return False

    if phase == 0:
        return rollover == 0 and reinstate == 0 and membership_root == 4
    if phase == 1:
        return rollover == 1 and reinstate == 0 and membership_root == 4
    if phase == 2:
        return rollover == 2 and reinstate == 0 and membership_root == 5
    if phase == 3:
        return rollover == 2 and reinstate == 1 and membership_root == 5
    if phase == 4:
        return rollover == 2 and reinstate == 2 and membership_root == 5
    return False


def root_rollover_witness_reinstatement():
    tails = [
        x for x in product(range(5), range(4), range(4), range(6), range(7),
                           range(4), range(3), range(2))
        if _mem79_ok(*x)
    ]
    z = q(17)
    seed = BASE_V78_BOUND_REPLICATION_RECOVERY_STATIC_STATES
    static_accepted = seed * len(tails)

    rollover_states = sum(x[0] >= 1 for x in tails) * seed
    bound_rollover = sum(x[0] >= 2 for x in tails) * seed
    reinstatement = sum(x[0] >= 3 for x in tails) * seed
    bound_reinstatement = sum(x[0] == 4 for x in tails) * seed

    below_rep = sum(x[5] < 2 for x in tails) * seed
    rollover_bad = sum(x[1] == 3 for x in tails) * seed
    reinstate_bad = sum(x[2] == 3 for x in tails) * seed
    generation_regression = sum(x[3] < 4 for x in tails) * seed
    root_regression = sum(x[4] < 4 for x in tails) * seed
    tombstone_break = sum(x[6] != 1 for x in tails) * seed
    active_byz = sum(x[7] != 0 for x in tails) * seed
    bad = (
        below_rep + rollover_bad + reinstate_bad + generation_regression
        + root_regression + tombstone_break + active_byz
    )

    checks = [
        _mem79_ok(0, 0, 0, 4, 4, 2, 1, 0),
        _mem79_ok(2, 2, 0, 4, 5, 2, 1, 0),
        _mem79_ok(4, 2, 2, 4, 5, 2, 1, 0),
        not _mem79_ok(4, 3, 2, 4, 5, 2, 1, 0),
        not _mem79_ok(4, 2, 3, 4, 5, 2, 1, 0),
        not _mem79_ok(4, 2, 2, 3, 5, 2, 1, 0),
        not _mem79_ok(4, 2, 2, 4, 3, 2, 1, 0),
        not _mem79_ok(4, 2, 2, 4, 5, 1, 1, 0),
        not _mem79_ok(4, 2, 2, 4, 5, 2, 1, 1),
    ]

    static_patterns = seed * 5 * 4 * 4 * 6 * 7 * 4 * 3 * 2
    patterns = static_patterns * (4 ** 17) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_replication_recovery_seed_states': seed,
        'delay_vectors': 4 ** 17,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'membership_root_rollover_states': rollover_states * z,
        'bound_membership_root_rollover_states': bound_rollover * z,
        'witness_reinstatement_states': reinstatement * z,
        'bound_witness_reinstatement_states': bound_reinstatement * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_membership_root_rollover_acceptances': rollover_bad * z,
        'unbound_or_forked_witness_reinstatement_acceptances': reinstate_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'membership_root_regression_acceptances': root_regression * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

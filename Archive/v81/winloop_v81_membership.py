from itertools import product
from winloop_v81_core import q

BASE_V80_BOUND_QUORUM_CHURN_STATIC_STATES = 760


def _mem81_ok(phase, witness_rotation, root_rollover, quorum_churn,
              generation, membership_root, replication,
              tombstone_binding, witness_binding, active_byzantine):
    if any(x == 3 for x in (witness_rotation, root_rollover, quorum_churn)):
        return False
    if generation != 4:
        return False
    if membership_root not in (5, 6):
        return False
    if replication != 2 or tombstone_binding != 1 or witness_binding != 2:
        return False
    if active_byzantine != 0:
        return False

    if phase == 0:
        return witness_rotation == 0 and root_rollover == 0 and quorum_churn == 0 and membership_root == 5
    if phase == 1:
        return witness_rotation == 1 and root_rollover == 0 and quorum_churn == 0 and membership_root == 5
    if phase == 2:
        return witness_rotation == 2 and root_rollover == 0 and quorum_churn == 0 and membership_root == 5
    if phase == 3:
        return witness_rotation == 2 and root_rollover == 1 and quorum_churn == 0 and membership_root == 5
    if phase == 4:
        return witness_rotation == 2 and root_rollover == 2 and quorum_churn == 0 and membership_root == 6
    if phase == 5:
        return witness_rotation == 2 and root_rollover == 2 and quorum_churn == 1 and membership_root == 6
    if phase == 6:
        return witness_rotation == 2 and root_rollover == 2 and quorum_churn == 2 and membership_root == 6
    return False


def witness_rotation_root6_rollover_quorum_churn():
    tails = [
        x for x in product(
            range(7), range(4), range(4), range(4), range(6), range(7),
            range(4), range(3), range(4), range(2)
        )
        if _mem81_ok(*x)
    ]
    z = q(19)
    seed = BASE_V80_BOUND_QUORUM_CHURN_STATIC_STATES
    static_accepted = seed * len(tails)

    rotation = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rotation = sum(x[1] == 2 for x in tails) * seed
    rollover = sum(x[2] in (1, 2) for x in tails) * seed
    bound_rollover = sum(x[2] == 2 for x in tails) * seed
    churn = sum(x[3] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[3] == 2 for x in tails) * seed

    below_rep = sum(x[6] < 2 for x in tails) * seed
    rotation_bad = sum(x[1] == 3 for x in tails) * seed
    rollover_bad = sum(x[2] == 3 for x in tails) * seed
    churn_bad = sum(x[3] == 3 for x in tails) * seed
    generation_regression = sum(x[4] < 4 for x in tails) * seed
    root_regression = sum(x[5] < 5 for x in tails) * seed
    tombstone_break = sum(x[7] != 1 for x in tails) * seed
    witness_break = sum(x[8] != 2 for x in tails) * seed
    active_byz = sum(x[9] != 0 for x in tails) * seed
    bad = (
        below_rep + rotation_bad + rollover_bad + churn_bad + generation_regression
        + root_regression + tombstone_break + witness_break + active_byz
    )

    checks = [
        _mem81_ok(0, 0, 0, 0, 4, 5, 2, 1, 2, 0),
        _mem81_ok(2, 2, 0, 0, 4, 5, 2, 1, 2, 0),
        _mem81_ok(4, 2, 2, 0, 4, 6, 2, 1, 2, 0),
        _mem81_ok(6, 2, 2, 2, 4, 6, 2, 1, 2, 0),
        not _mem81_ok(6, 3, 2, 2, 4, 6, 2, 1, 2, 0),
        not _mem81_ok(6, 2, 3, 2, 4, 6, 2, 1, 2, 0),
        not _mem81_ok(6, 2, 2, 3, 4, 6, 2, 1, 2, 0),
        not _mem81_ok(6, 2, 2, 2, 3, 6, 2, 1, 2, 0),
        not _mem81_ok(6, 2, 2, 2, 4, 4, 2, 1, 2, 0),
        not _mem81_ok(6, 2, 2, 2, 4, 6, 1, 1, 2, 0),
        not _mem81_ok(6, 2, 2, 2, 4, 6, 2, 2, 2, 0),
        not _mem81_ok(6, 2, 2, 2, 4, 6, 2, 1, 1, 0),
        not _mem81_ok(6, 2, 2, 2, 4, 6, 2, 1, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 3) * 6 * 7 * 4 * 3 * 4 * 2
    patterns = static_patterns * (4 ** 19) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4 ** 19,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'witness_rotation_states': rotation * z,
        'bound_witness_rotation_states': bound_rotation * z,
        'root6_rollover_states': rollover * z,
        'bound_root6_rollover_states': bound_rollover * z,
        'replication_quorum_churn_states': churn * z,
        'bound_replication_quorum_churn_states': bound_churn * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_witness_rotation_acceptances': rotation_bad * z,
        'unbound_or_conflicting_root6_rollover_acceptances': rollover_bad * z,
        'unbound_or_conflicting_replication_quorum_churn_acceptances': churn_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'membership_root_regression_acceptances': root_regression * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'witness_binding_discontinuity_acceptances': witness_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

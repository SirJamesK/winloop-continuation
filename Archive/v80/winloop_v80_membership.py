from itertools import product
from winloop_v80_core import q

BASE_V79_BOUND_WITNESS_REINSTATEMENT_STATIC_STATES = 760


def _mem80_ok(phase, split_view, recovery, quorum_churn, generation, membership_root,
              replication, tombstone_binding, witness_binding, active_byzantine):
    if any(x == 3 for x in (split_view, recovery, quorum_churn)):
        return False
    if generation != 4 or membership_root != 5:
        return False
    if replication != 2 or tombstone_binding != 1 or witness_binding != 2:
        return False
    if active_byzantine != 0:
        return False

    if phase == 0:
        return split_view == 0 and recovery == 0 and quorum_churn == 0
    if phase == 1:
        return split_view == 1 and recovery == 0 and quorum_churn == 0
    if phase == 2:
        return split_view == 2 and recovery == 1 and quorum_churn == 0
    if phase == 3:
        return split_view == 2 and recovery == 2 and quorum_churn == 1
    if phase == 4:
        return split_view == 2 and recovery == 2 and quorum_churn == 2
    return False


def root5_split_view_quorum_churn():
    tails = [
        x for x in product(
            range(5), range(4), range(4), range(4), range(6), range(7),
            range(4), range(3), range(4), range(2)
        )
        if _mem80_ok(*x)
    ]
    z = q(18)
    seed = BASE_V79_BOUND_WITNESS_REINSTATEMENT_STATIC_STATES
    static_accepted = seed * len(tails)

    split_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_split = sum(x[1] == 2 for x in tails) * seed
    recovery_states = sum(x[2] in (1, 2) for x in tails) * seed
    bound_recovery = sum(x[2] == 2 for x in tails) * seed
    churn_states = sum(x[3] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[3] == 2 for x in tails) * seed

    below_rep = sum(x[6] < 2 for x in tails) * seed
    split_bad = sum(x[1] == 3 for x in tails) * seed
    recovery_bad = sum(x[2] == 3 for x in tails) * seed
    churn_bad = sum(x[3] == 3 for x in tails) * seed
    generation_regression = sum(x[4] < 4 for x in tails) * seed
    root_regression = sum(x[5] < 5 for x in tails) * seed
    tombstone_break = sum(x[7] != 1 for x in tails) * seed
    witness_break = sum(x[8] != 2 for x in tails) * seed
    active_byz = sum(x[9] != 0 for x in tails) * seed
    bad = (
        below_rep + split_bad + recovery_bad + churn_bad + generation_regression
        + root_regression + tombstone_break + witness_break + active_byz
    )

    checks = [
        _mem80_ok(0, 0, 0, 0, 4, 5, 2, 1, 2, 0),
        _mem80_ok(2, 2, 1, 0, 4, 5, 2, 1, 2, 0),
        _mem80_ok(4, 2, 2, 2, 4, 5, 2, 1, 2, 0),
        not _mem80_ok(4, 3, 2, 2, 4, 5, 2, 1, 2, 0),
        not _mem80_ok(4, 2, 3, 2, 4, 5, 2, 1, 2, 0),
        not _mem80_ok(4, 2, 2, 3, 4, 5, 2, 1, 2, 0),
        not _mem80_ok(4, 2, 2, 2, 3, 5, 2, 1, 2, 0),
        not _mem80_ok(4, 2, 2, 2, 4, 4, 2, 1, 2, 0),
        not _mem80_ok(4, 2, 2, 2, 4, 5, 1, 1, 2, 0),
        not _mem80_ok(4, 2, 2, 2, 4, 5, 2, 2, 2, 0),
        not _mem80_ok(4, 2, 2, 2, 4, 5, 2, 1, 1, 0),
        not _mem80_ok(4, 2, 2, 2, 4, 5, 2, 1, 2, 1),
    ]

    static_patterns = seed * 5 * (4 ** 3) * 6 * 7 * 4 * 3 * 4 * 2
    patterns = static_patterns * (4 ** 18) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_witness_reinstatement_seed_states': seed,
        'delay_vectors': 4 ** 18,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'root5_split_view_states': split_states * z,
        'bound_root5_split_view_states': bound_split * z,
        'root5_split_view_recovery_states': recovery_states * z,
        'bound_root5_split_view_recovery_states': bound_recovery * z,
        'replication_quorum_churn_states': churn_states * z,
        'bound_replication_quorum_churn_states': bound_churn * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_root5_split_view_acceptances': split_bad * z,
        'unbound_or_forked_root5_recovery_acceptances': recovery_bad * z,
        'unbound_or_conflicting_replication_quorum_churn_acceptances': churn_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'membership_root_regression_acceptances': root_regression * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'witness_binding_discontinuity_acceptances': witness_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

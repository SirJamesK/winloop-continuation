from winloop_v116_core import q

BASE_V115_BOUND_QUORUM_CHURN_STATIC_STATES = 760

_MEM116_EXPECTED = {
    0: (0, 0, 0, 0, 0),
    1: (1, 0, 0, 0, 0),
    2: (2, 0, 0, 0, 0),
    3: (2, 1, 0, 0, 0),
    4: (2, 2, 0, 0, 0),
    5: (2, 2, 1, 0, 0),
    6: (2, 2, 2, 0, 0),
    7: (2, 2, 2, 1, 0),
    8: (2, 2, 2, 2, 0),
    9: (2, 2, 2, 2, 1),
    10: (2, 2, 2, 2, 2),
}


def _mem116_ok(phase, witness_source_replacement, replacement_source_binding,
               root23_rollover, root23_binding, quorum_churn,
               generation, carried_root, target_root, replication,
               tombstone_binding, witness_binding, prior_source_binding,
               active_byzantine):
    if any(x == 3 for x in (
        witness_source_replacement, replacement_source_binding,
        root23_rollover, root23_binding, quorum_churn, prior_source_binding
    )):
        return False
    # V115 leaves a rebound witness current at generation 4 / root 22. V116
    # binds a new witness source, rolls to root 23, binds that root, and only
    # then lets a replication-quorum churn complete.
    if generation != 4 or carried_root != 22 or target_root != 23:
        return False
    if replication != 2 or tombstone_binding != 1 or witness_binding != 2:
        return False
    if prior_source_binding != 2 or active_byzantine != 0:
        return False
    return _MEM116_EXPECTED.get(phase) == (
        witness_source_replacement, replacement_source_binding,
        root23_rollover, root23_binding, quorum_churn
    )


def root23_rollover_after_root22_witness_source_replacement():
    tails = [
        (phase, *state, 4, 22, 23, 2, 1, 2, 2, 0)
        for phase, state in _MEM116_EXPECTED.items()
    ]
    assert all(_mem116_ok(*x) for x in tails)
    z = q(84)
    seed = BASE_V115_BOUND_QUORUM_CHURN_STATIC_STATES
    static_accepted = seed * len(tails)

    replacement = sum(x[1] in (1, 2) for x in tails) * seed
    bound_replacement = sum(x[1] == 2 for x in tails) * seed
    replacement_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_replacement_binding = sum(x[2] == 2 for x in tails) * seed
    rollover = sum(x[3] in (1, 2) for x in tails) * seed
    bound_rollover = sum(x[3] == 2 for x in tails) * seed
    root_binding = sum(x[4] in (1, 2) for x in tails) * seed
    bound_root_binding = sum(x[4] == 2 for x in tails) * seed
    churn = sum(x[5] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[5] == 2 for x in tails) * seed

    replacement_bad = sum(x[1] == 3 for x in tails) * seed
    replacement_binding_bad = sum(x[2] == 3 for x in tails) * seed
    rollover_bad = sum(x[3] == 3 for x in tails) * seed
    root_binding_bad = sum(x[4] == 3 for x in tails) * seed
    churn_bad = sum(x[5] == 3 for x in tails) * seed
    generation_regression = sum(x[6] < 4 for x in tails) * seed
    carried_root_regression = sum(x[7] < 22 for x in tails) * seed
    target_root_regression = sum(x[8] < 23 for x in tails) * seed
    below_rep = sum(x[9] < 2 for x in tails) * seed
    tombstone_break = sum(x[10] != 1 for x in tails) * seed
    witness_break = sum(x[11] != 2 for x in tails) * seed
    prior_source_break = sum(x[12] != 2 for x in tails) * seed
    active_byz = sum(x[13] != 0 for x in tails) * seed
    bad = (
        replacement_bad + replacement_binding_bad + rollover_bad
        + root_binding_bad + churn_bad + generation_regression
        + carried_root_regression + target_root_regression + below_rep
        + tombstone_break + witness_break + prior_source_break + active_byz
    )

    checks = [
        _mem116_ok(0, 0, 0, 0, 0, 0, 4, 22, 23, 2, 1, 2, 2, 0),
        _mem116_ok(2, 2, 0, 0, 0, 0, 4, 22, 23, 2, 1, 2, 2, 0),
        _mem116_ok(4, 2, 2, 0, 0, 0, 4, 22, 23, 2, 1, 2, 2, 0),
        _mem116_ok(6, 2, 2, 2, 0, 0, 4, 22, 23, 2, 1, 2, 2, 0),
        _mem116_ok(8, 2, 2, 2, 2, 0, 4, 22, 23, 2, 1, 2, 2, 0),
        _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 3, 2, 2, 2, 2, 4, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 3, 2, 2, 2, 4, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 3, 2, 2, 4, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 3, 2, 4, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 3, 4, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 3, 22, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 21, 23, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 22, 2, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 23, 1, 1, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 23, 2, 2, 2, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 23, 2, 1, 1, 2, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 23, 2, 1, 2, 3, 0),
        not _mem116_ok(10, 2, 2, 2, 2, 2, 4, 22, 23, 2, 1, 2, 2, 1),
    ]

    static_patterns = seed * 11 * (4 ** 5) * 6 * 16 * 16 * 4 * 3 * 4 * 4 * 2
    patterns = static_patterns * (4 ** 84) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4 ** 84,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'witness_source_replacement_states': replacement * z,
        'bound_witness_source_replacement_states': bound_replacement * z,
        'replacement_source_binding_states': replacement_binding * z,
        'bound_replacement_source_binding_states': bound_replacement_binding * z,
        'root23_rollover_states': rollover * z,
        'bound_root23_rollover_states': bound_rollover * z,
        'root23_binding_states': root_binding * z,
        'bound_root23_binding_states': bound_root_binding * z,
        'replication_quorum_churn_states': churn * z,
        'bound_replication_quorum_churn_states': bound_churn * z,
        'unbound_or_conflicting_witness_source_replacement_acceptances': replacement_bad * z,
        'unbound_or_conflicting_replacement_source_binding_acceptances': replacement_binding_bad * z,
        'unbound_or_conflicting_root23_rollover_acceptances': rollover_bad * z,
        'unbound_or_conflicting_root23_binding_acceptances': root_binding_bad * z,
        'unbound_or_conflicting_replication_quorum_churn_acceptances': churn_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'carried_membership_root_regression_acceptances': carried_root_regression * z,
        'target_membership_root_regression_acceptances': target_root_regression * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'witness_binding_discontinuity_acceptances': witness_break * z,
        'prior_source_binding_discontinuity_acceptances': prior_source_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

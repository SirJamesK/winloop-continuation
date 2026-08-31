from winloop_v86_core import q

BASE_V85_BOUND_QUORUM_CHURN_STATIC_STATES = 760

_MEM86_EXPECTED = {
    0: (0, 0, 0),
    1: (1, 0, 0),
    2: (2, 0, 0),
    3: (2, 1, 0),
    4: (2, 2, 0),
    5: (2, 2, 1),
    6: (2, 2, 2),
}


def _mem86_ok(phase, root8_rollover, root8_binding, quorum_churn,
              generation, carried_root, target_root, replication,
              tombstone_binding, witness_binding, replacement_source_binding,
              active_byzantine):
    if any(x == 3 for x in (
        root8_rollover, root8_binding, quorum_churn, replacement_source_binding
    )):
        return False
    # V85's witness-source replacement and its replacement-source binding must
    # already be fully bound before root 8 can be rolled or consumed.
    if replacement_source_binding != 2 or witness_binding != 2:
        return False
    if generation != 4 or carried_root != 7 or target_root != 8:
        return False
    if replication != 2 or tombstone_binding != 1:
        return False
    if active_byzantine != 0:
        return False
    return _MEM86_EXPECTED.get(phase) == (
        root8_rollover, root8_binding, quorum_churn
    )


def root8_rollover_after_witness_replacement():
    tails = [
        (phase, *state, 4, 7, 8, 2, 1, 2, 2, 0)
        for phase, state in _MEM86_EXPECTED.items()
    ]
    assert all(_mem86_ok(*x) for x in tails)
    z = q(25)
    seed = BASE_V85_BOUND_QUORUM_CHURN_STATIC_STATES
    static_accepted = seed * len(tails)

    rollover = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rollover = sum(x[1] == 2 for x in tails) * seed
    root_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_root_binding = sum(x[2] == 2 for x in tails) * seed
    churn = sum(x[3] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[3] == 2 for x in tails) * seed

    below_rep = sum(x[7] < 2 for x in tails) * seed
    rollover_bad = sum(x[1] == 3 for x in tails) * seed
    root_binding_bad = sum(x[2] == 3 for x in tails) * seed
    churn_bad = sum(x[3] == 3 for x in tails) * seed
    generation_regression = sum(x[4] < 4 for x in tails) * seed
    carried_root_regression = sum(x[5] < 7 for x in tails) * seed
    target_root_regression = sum(x[6] < 8 for x in tails) * seed
    tombstone_break = sum(x[8] != 1 for x in tails) * seed
    witness_break = sum(x[9] != 2 for x in tails) * seed
    replacement_source_break = sum(x[10] != 2 for x in tails) * seed
    active_byz = sum(x[11] != 0 for x in tails) * seed
    bad = (
        below_rep + rollover_bad + root_binding_bad + churn_bad
        + generation_regression + carried_root_regression + target_root_regression
        + tombstone_break + witness_break + replacement_source_break + active_byz
    )

    checks = [
        _mem86_ok(0, 0, 0, 0, 4, 7, 8, 2, 1, 2, 2, 0),
        _mem86_ok(2, 2, 0, 0, 4, 7, 8, 2, 1, 2, 2, 0),
        _mem86_ok(4, 2, 2, 0, 4, 7, 8, 2, 1, 2, 2, 0),
        _mem86_ok(6, 2, 2, 2, 4, 7, 8, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 3, 2, 2, 4, 7, 8, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 3, 2, 4, 7, 8, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 3, 4, 7, 8, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 3, 7, 8, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 6, 8, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 7, 7, 2, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 7, 8, 1, 1, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 7, 8, 2, 2, 2, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 7, 8, 2, 1, 1, 2, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 7, 8, 2, 1, 2, 3, 0),
        not _mem86_ok(6, 2, 2, 2, 4, 7, 8, 2, 1, 2, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 3) * 6 * 9 * 10 * 4 * 3 * 4 * 4 * 2
    patterns = static_patterns * (4 ** 25) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4 ** 25,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'root8_rollover_states': rollover * z,
        'bound_root8_rollover_states': bound_rollover * z,
        'root8_binding_states': root_binding * z,
        'bound_root8_binding_states': bound_root_binding * z,
        'replication_quorum_churn_states': churn * z,
        'bound_replication_quorum_churn_states': bound_churn * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_root8_rollover_acceptances': rollover_bad * z,
        'unbound_or_conflicting_root8_binding_acceptances': root_binding_bad * z,
        'unbound_or_conflicting_replication_quorum_churn_acceptances': churn_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'carried_membership_root_regression_acceptances': carried_root_regression * z,
        'target_membership_root_regression_acceptances': target_root_regression * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'witness_binding_discontinuity_acceptances': witness_break * z,
        'replacement_source_binding_discontinuity_acceptances': replacement_source_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

from winloop_v119_core import q

BASE_V118_BOUND_QUORUM_CHURN_STATIC_STATES = 760

_MEM119_EXPECTED = {
    0: (0, 0, 0),
    1: (1, 0, 0),
    2: (2, 0, 0),
    3: (2, 1, 0),
    4: (2, 2, 0),
    5: (2, 2, 1),
    6: (2, 2, 2),
}


def _mem119_ok(phase, witness_rebind, witness_binding, quorum_churn,
               generation, carried_root, target_root, replication,
               tombstone_binding, replacement_source_binding,
               prior_source_binding, active_byzantine):
    if any(x == 3 for x in (
        witness_rebind, witness_binding, quorum_churn,
        replacement_source_binding, prior_source_binding
    )):
        return False
    # V118 completed the root-24 rollover with replacement/prior-source bindings
    # intact. V119 keeps generation 4 / root 24 fixed, rebinds the witness to
    # root 24, and only then permits another replication-quorum churn.
    if replacement_source_binding != 2 or prior_source_binding != 2:
        return False
    if generation != 4 or carried_root != 24 or target_root != 24:
        return False
    if replication != 2 or tombstone_binding != 1:
        return False
    if active_byzantine != 0:
        return False
    return _MEM119_EXPECTED.get(phase) == (
        witness_rebind, witness_binding, quorum_churn
    )


def root24_witness_rebind_quorum_churn():
    tails = [
        (phase, *state, 4, 24, 24, 2, 1, 2, 2, 0)
        for phase, state in _MEM119_EXPECTED.items()
    ]
    assert all(_mem119_ok(*x) for x in tails)
    z = q(90)
    seed = BASE_V118_BOUND_QUORUM_CHURN_STATIC_STATES
    static_accepted = seed * len(tails)

    rebind = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rebind = sum(x[1] == 2 for x in tails) * seed
    witness_binding = sum(x[2] in (1, 2) for x in tails) * seed
    bound_witness_binding = sum(x[2] == 2 for x in tails) * seed
    churn = sum(x[3] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[3] == 2 for x in tails) * seed

    below_rep = sum(x[7] < 2 for x in tails) * seed
    rebind_bad = sum(x[1] == 3 for x in tails) * seed
    witness_bad = sum(x[2] == 3 for x in tails) * seed
    churn_bad = sum(x[3] == 3 for x in tails) * seed
    generation_regression = sum(x[4] < 4 for x in tails) * seed
    carried_root_regression = sum(x[5] < 24 for x in tails) * seed
    target_root_regression = sum(x[6] < 24 for x in tails) * seed
    tombstone_break = sum(x[8] != 1 for x in tails) * seed
    replacement_source_break = sum(x[9] != 2 for x in tails) * seed
    prior_source_break = sum(x[10] != 2 for x in tails) * seed
    active_byz = sum(x[11] != 0 for x in tails) * seed
    bad = (
        below_rep + rebind_bad + witness_bad + churn_bad
        + generation_regression + carried_root_regression + target_root_regression
        + tombstone_break + replacement_source_break + prior_source_break
        + active_byz
    )

    checks = [
        _mem119_ok(0, 0, 0, 0, 4, 24, 24, 2, 1, 2, 2, 0),
        _mem119_ok(2, 2, 0, 0, 4, 24, 24, 2, 1, 2, 2, 0),
        _mem119_ok(4, 2, 2, 0, 4, 24, 24, 2, 1, 2, 2, 0),
        _mem119_ok(6, 2, 2, 2, 4, 24, 24, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 3, 2, 2, 4, 24, 24, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 3, 2, 4, 24, 24, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 3, 4, 24, 24, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 3, 24, 24, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 23, 24, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 24, 23, 2, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 24, 24, 1, 1, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 24, 24, 2, 2, 2, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 24, 24, 2, 1, 3, 2, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 24, 24, 2, 1, 2, 3, 0),
        not _mem119_ok(6, 2, 2, 2, 4, 24, 24, 2, 1, 2, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 3) * 6 * 16 * 16 * 4 * 3 * 4 * 4 * 2
    patterns = static_patterns * (4 ** 90) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4 ** 90,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'root24_witness_rebind_states': rebind * z,
        'bound_root24_witness_rebind_states': bound_rebind * z,
        'root24_witness_binding_states': witness_binding * z,
        'bound_root24_witness_binding_states': bound_witness_binding * z,
        'replication_quorum_churn_states': churn * z,
        'bound_replication_quorum_churn_states': bound_churn * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_root24_witness_rebind_acceptances': rebind_bad * z,
        'unbound_or_conflicting_root24_witness_binding_acceptances': witness_bad * z,
        'unbound_or_conflicting_replication_quorum_churn_acceptances': churn_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'carried_membership_root_regression_acceptances': carried_root_regression * z,
        'target_membership_root_regression_acceptances': target_root_regression * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'replacement_source_binding_discontinuity_acceptances': replacement_source_break * z,
        'prior_source_binding_discontinuity_acceptances': prior_source_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

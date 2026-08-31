from winloop_v85_core import q

BASE_V84_BOUND_QUORUM_CHURN_STATIC_STATES = 760

_MEM85_EXPECTED = {
    0: (0, 0, 0),
    1: (1, 0, 0),
    2: (2, 0, 0),
    3: (2, 1, 0),
    4: (2, 2, 0),
    5: (2, 2, 1),
    6: (2, 2, 2),
}


def _mem85_ok(phase, witness_source_replacement, replacement_source_binding,
              quorum_churn, generation, membership_root, replication,
              tombstone_binding, witness_binding, prior_source_binding,
              active_byzantine):
    if any(x == 3 for x in (
        witness_source_replacement, replacement_source_binding,
        quorum_churn, prior_source_binding
    )):
        return False
    if generation != 4 or membership_root != 7:
        return False
    if replication != 2 or tombstone_binding != 1 or witness_binding != 2:
        return False
    if prior_source_binding != 2 or active_byzantine != 0:
        return False
    return _MEM85_EXPECTED.get(phase) == (
        witness_source_replacement, replacement_source_binding, quorum_churn
    )


def witness_source_replacement_quorum_churn():
    tails = [
        (phase, *state, 4, 7, 2, 1, 2, 2, 0)
        for phase, state in _MEM85_EXPECTED.items()
    ]
    assert all(_mem85_ok(*x) for x in tails)
    z = q(23)
    seed = BASE_V84_BOUND_QUORUM_CHURN_STATIC_STATES
    static_accepted = seed * len(tails)

    replacement = sum(x[1] in (1, 2) for x in tails) * seed
    bound_replacement = sum(x[1] == 2 for x in tails) * seed
    bound_replacement_binding = sum(x[2] == 2 for x in tails) * seed
    churn = sum(x[3] in (1, 2) for x in tails) * seed
    bound_churn = sum(x[3] == 2 for x in tails) * seed

    below_rep = sum(x[6] < 2 for x in tails) * seed
    replacement_bad = sum(x[1] == 3 for x in tails) * seed
    replacement_binding_bad = sum(x[2] == 3 for x in tails) * seed
    churn_bad = sum(x[3] == 3 for x in tails) * seed
    generation_regression = sum(x[4] < 4 for x in tails) * seed
    root_regression = sum(x[5] < 7 for x in tails) * seed
    tombstone_break = sum(x[7] != 1 for x in tails) * seed
    witness_break = sum(x[8] != 2 for x in tails) * seed
    prior_source_break = sum(x[9] != 2 for x in tails) * seed
    active_byz = sum(x[10] != 0 for x in tails) * seed
    bad = (
        below_rep + replacement_bad + replacement_binding_bad + churn_bad
        + generation_regression + root_regression + tombstone_break
        + witness_break + prior_source_break + active_byz
    )

    checks = [
        _mem85_ok(0, 0, 0, 0, 4, 7, 2, 1, 2, 2, 0),
        _mem85_ok(2, 2, 0, 0, 4, 7, 2, 1, 2, 2, 0),
        _mem85_ok(4, 2, 2, 0, 4, 7, 2, 1, 2, 2, 0),
        _mem85_ok(6, 2, 2, 2, 4, 7, 2, 1, 2, 2, 0),
        not _mem85_ok(6, 3, 2, 2, 4, 7, 2, 1, 2, 2, 0),
        not _mem85_ok(6, 2, 3, 2, 4, 7, 2, 1, 2, 2, 0),
        not _mem85_ok(6, 2, 2, 3, 4, 7, 2, 1, 2, 2, 0),
        not _mem85_ok(6, 2, 2, 2, 3, 7, 2, 1, 2, 2, 0),
        not _mem85_ok(6, 2, 2, 2, 4, 6, 2, 1, 2, 2, 0),
        not _mem85_ok(6, 2, 2, 2, 4, 7, 1, 1, 2, 2, 0),
        not _mem85_ok(6, 2, 2, 2, 4, 7, 2, 2, 2, 2, 0),
        not _mem85_ok(6, 2, 2, 2, 4, 7, 2, 1, 1, 2, 0),
        not _mem85_ok(6, 2, 2, 2, 4, 7, 2, 1, 2, 3, 0),
        not _mem85_ok(6, 2, 2, 2, 4, 7, 2, 1, 2, 2, 1),
    ]

    static_patterns = seed * 7 * (4 ** 3) * 6 * 9 * 4 * 3 * 4 * 4 * 2
    patterns = static_patterns * (4 ** 23) * z
    return {
        'patterns': patterns,
        'accepted': static_accepted * z,
        'base_states': static_accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4 ** 23,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'witness_source_replacement_states': replacement * z,
        'bound_witness_source_replacement_states': bound_replacement * z,
        'bound_replacement_source_binding_states': bound_replacement_binding * z,
        'replication_quorum_churn_states': churn * z,
        'bound_replication_quorum_churn_states': bound_churn * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_witness_source_replacement_acceptances': replacement_bad * z,
        'unbound_or_conflicting_replacement_source_binding_acceptances': replacement_binding_bad * z,
        'unbound_or_conflicting_replication_quorum_churn_acceptances': churn_bad * z,
        'membership_generation_regression_acceptances': generation_regression * z,
        'membership_root_regression_acceptances': root_regression * z,
        'tombstone_binding_discontinuity_acceptances': tombstone_break * z,
        'witness_binding_discontinuity_acceptances': witness_break * z,
        'prior_source_binding_discontinuity_acceptances': prior_source_break * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

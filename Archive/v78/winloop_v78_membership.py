from itertools import product
from winloop_v78_core import q

def popc(m, t):
    c = [m.count(i) for i in range(9)]
    if c[5] or t >= 15:
        return False
    if t < 4:
        return c[0] + c[1] >= 3 and c[2] >= 1 and sum(c[3:]) == 0
    if t == 4:
        return c[0] + c[1] + c[3] >= 3 and c[2] >= 1 and c[3] >= 1 and c[4] == c[6] == c[7] == c[8] == 0
    if t == 5:
        return c[0] + c[1] + c[4] >= 3 and c[2] >= 1 and c[4] >= 1 and c[3] == c[6] == c[7] == c[8] == 0
    if t == 6:
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and c[4] >= 1 and c[3] == c[7] == c[8] == 0
    if t == 7:
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and c[7] == 1 and c[3] == c[4] == c[8] == 0
    if t in (8, 9, 10, 11, 12, 13, 14):
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and c[7] == 1 and c[8] == 1 and c[2] == c[3] == c[4] == 0
    return False

def mok(t, tomb, ver, comp, ident, root, gen, reuse, mroot, rep, rollback, churn,
        churn2, mcomp2, reuse3, evict3, reploss3, reprecover3):
    if (
        tomb >= 2 or ver >= 3 or comp >= 4 or ident >= 5 or root >= 4
        or gen >= 5 or reuse >= 5 or mroot >= 5 or rep >= 4 or rollback >= 4
        or churn >= 5 or churn2 >= 5 or mcomp2 >= 5 or reuse3 >= 5
        or evict3 >= 5 or reploss3 >= 4 or reprecover3 >= 5
    ):
        return False
    if t < 8 and rep != 0:
        return False
    if t < 9 and (rollback != 0 or churn != 0):
        return False
    if t < 10 and churn2 != 0:
        return False
    if t < 11 and mcomp2 != 0:
        return False
    if t < 12 and reuse3 != 0:
        return False
    if t < 13 and evict3 != 0:
        return False
    if t < 14 and (reploss3 != 0 or reprecover3 != 0):
        return False
    if t == 0:
        return (tomb, ver, comp, ident, root, gen, reuse, mroot, rep, rollback, churn, churn2, mcomp2, reuse3, evict3, reploss3, reprecover3) == (0,) * 17
    if t == 1:
        return tomb == 0 and comp == 1 and ver == 0 and ident == 0 and root == 0 and gen == 0 and reuse == 0 and mroot == 0
    if t == 2:
        return tomb == 0 and comp in (1, 2) and ver == 1 and ident == 0 and root == 1 and gen == 0 and reuse == 0 and mroot == 0
    if t == 3:
        return tomb == 0 and comp == 1 and ver == 2 and ident == 0 and root == 1 and gen == 0 and reuse == 0 and mroot == 0
    if t == 4:
        return tomb == 0 and comp == 1 and ver in (0, 1) and ident == 1 and root in (0, 1) and gen == 1 and reuse == 0 and mroot == 0
    if t == 5:
        return tomb == 0 and comp == 2 and ver == 1 and ident == 2 and root == 1 and gen == 1 and reuse == 0 and mroot == 0
    if t == 6:
        return tomb == 0 and comp == 2 and ver == 1 and ident == 0 and root in (1, 2) and gen == 2 and reuse == 0 and mroot in (0, 1)
    if t == 7:
        return tomb == 0 and comp == 2 and ver == 2 and ident == 3 and root == 2 and gen == 2 and reuse == 2 and mroot == 2
    if t == 8:
        return tomb == 0 and ver == 2 and comp in (2, 3) and ident == 4 and root == 2 and gen == 3 and reuse == 3 and mroot == 3 and rep in (2, 3)
    if t == 9:
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 3 and reuse == 3 and mroot == 3 and rep == 2
            and rollback == 1 and churn in (1, 2) and churn2 == 0
        )
    if t == 10:
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 3 and reuse == 3 and mroot == 3 and rep == 2
            and rollback == 1 and churn == 2 and churn2 in (1, 2)
        )
    if t == 11:
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 3 and reuse == 3 and mroot == 3 and rep == 2
            and rollback == 1 and churn == 2 and churn2 == 2
            and mcomp2 in (1, 2) and reuse3 == 0
        )
    if t == 12:
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 4 and reuse == 4 and mroot == 4 and rep == 2
            and rollback == 1 and churn == 2 and churn2 == 2
            and mcomp2 == 2 and reuse3 in (1, 2)
        )
    if t == 13:
        # Witness eviction is accepted only after the third recycled identity is
        # fully bound to generation 4 and membership root 4.
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 4 and reuse == 4 and mroot == 4 and rep == 2
            and rollback == 1 and churn == 2 and churn2 == 2
            and mcomp2 == 2 and reuse3 == 2 and evict3 in (1, 2)
            and reploss3 == 0 and reprecover3 == 0
        )
    if t == 14:
        # Temporary replication loss is fail-closed. Recovery may advance only
        # after witness eviction is fully bound; the generation/root never regress.
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 4 and reuse == 4 and mroot == 4 and rep == 2
            and rollback == 1 and churn == 2 and churn2 == 2
            and mcomp2 == 2 and reuse3 == 2 and evict3 == 2
            and reploss3 == 1 and reprecover3 in (0, 1, 2)
        )
    return False

def third_generation_witness_eviction_replication_loss():
    M = {}
    for t in range(15):
        rollback_domain = (1,) if t in (9, 10, 11, 12, 13, 14) else (0,)
        churn_domain = (1, 2) if t == 9 else ((2,) if t in (10, 11, 12, 13, 14) else (0,))
        churn2_domain = (1, 2) if t == 10 else ((2,) if t in (11, 12, 13, 14) else (0,))
        mcomp2_domain = (1, 2) if t == 11 else ((2,) if t in (12, 13, 14) else (0,))
        reuse3_domain = (1, 2) if t == 12 else ((2,) if t in (13, 14) else (0,))
        evict3_domain = (1, 2) if t == 13 else ((2,) if t == 14 else (0,))
        reploss3_domain = (1,) if t == 14 else (0,)
        reprecover3_domain = (0, 1, 2) if t == 14 else (0,)
        M[t] = [
            x for x in product(
                range(2), range(3), range(4), range(5), range(4), range(5),
                range(5), range(5), range(4), rollback_domain, churn_domain,
                churn2_domain, mcomp2_domain, reuse3_domain, evict3_domain,
                reploss3_domain, reprecover3_domain
            ) if mok(t, *x)
        ]
    accepted = []
    for m in product(range(9), repeat=5):
        for t in range(15):
            if popc(m, t):
                for x in M[t]:
                    accepted.append((m, t) + x)
    n = len(accepted)
    z = q(16)
    eviction_states = sum(x[1] == 13 for x in accepted)
    temp_loss_states = sum(x[1] == 14 and x[17] == 1 for x in accepted)
    bound_recoveries = sum(x[1] == 14 and x[18] in (1, 2) for x in accepted)
    below_rep = sum(x[1] in (9, 10, 11, 12, 13, 14) and x[10] == 1 for x in accepted)
    rollback_bad = sum(x[1] in (9, 10, 11, 12, 13, 14) and x[11] in (2, 3) for x in accepted)
    churn1_bad = sum(x[1] in (9, 10, 11, 12, 13, 14) and x[12] in (3, 4) for x in accepted)
    churn2_bad = sum(x[1] in (10, 11, 12, 13, 14) and x[13] in (3, 4) for x in accepted)
    compaction_bad = sum(x[1] in (11, 12, 13, 14) and x[14] in (3, 4) for x in accepted)
    reuse3_bad = sum(x[1] in (12, 13, 14) and x[15] in (3, 4) for x in accepted)
    eviction_bad = sum(x[1] in (13, 14) and x[16] in (3, 4) for x in accepted)
    reploss_bad = sum(x[1] == 14 and x[17] in (2, 3) for x in accepted)
    reprecover_bad = sum(x[1] == 14 and x[18] in (3, 4) for x in accepted)
    generation_collapse = sum(x[1] in (8, 9, 10, 11) and x[7] < 3 for x in accepted)
    third_generation_collapse = sum(x[1] in (12, 13, 14) and (x[7] < 4 or x[8] < 4 or x[9] < 4) for x in accepted)
    unbound_root = sum(x[1] in (8, 9, 10, 11, 12, 13, 14) and x[6] == 3 for x in accepted)
    active_byz = sum(5 in x[0] for x in accepted)
    bad = (
        below_rep + rollback_bad + churn1_bad + churn2_bad + compaction_bad + reuse3_bad
        + eviction_bad + reploss_bad + reprecover_bad + generation_collapse
        + third_generation_collapse + unbound_root + active_byz
    )

    def b(m, t, *x):
        return popc(m, t) and mok(t, *x)

    checks = [
        b((0, 0, 1, 1, 2), 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        b((0, 1, 6, 7, 8), 12, 0, 2, 3, 4, 2, 4, 4, 4, 2, 1, 2, 2, 2, 2, 0, 0, 0),
        b((0, 1, 6, 7, 8), 13, 0, 2, 3, 4, 2, 4, 4, 4, 2, 1, 2, 2, 2, 2, 2, 0, 0),
        b((0, 1, 6, 7, 8), 14, 0, 2, 3, 4, 2, 4, 4, 4, 2, 1, 2, 2, 2, 2, 2, 1, 2),
        not b((0, 1, 6, 7, 8), 13, 0, 2, 3, 4, 2, 3, 4, 4, 2, 1, 2, 2, 2, 2, 2, 0, 0),
        not b((0, 1, 6, 7, 8), 13, 0, 2, 3, 4, 2, 4, 4, 4, 2, 1, 2, 2, 2, 2, 3, 0, 0),
        not b((0, 1, 6, 7, 8), 14, 0, 2, 3, 4, 2, 4, 4, 4, 2, 1, 2, 2, 2, 2, 2, 2, 1),
        not b((0, 1, 5, 7, 8), 14, 0, 2, 3, 4, 2, 4, 4, 4, 2, 1, 2, 2, 2, 2, 2, 1, 1),
    ]
    static_patterns = 9 ** 5 * 15 * 2 * 3 * 4 * 5 * 4 * 5 * 5 * 5 * 4 * 4 * 5 * 5 * 5 * 5 * 5 * 4 * 5
    patterns = static_patterns * (4 ** 16) * z
    return {
        'patterns': patterns,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 16,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'third_generation_witness_eviction_states': eviction_states * z,
        'temporary_replication_loss_states': temp_loss_states * z,
        'bound_replication_recovery_states': bound_recoveries * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_rollback_acceptances': rollback_bad * z,
        'unbound_or_forked_first_witness_churn_acceptances': churn1_bad * z,
        'unbound_or_forked_second_witness_churn_acceptances': churn2_bad * z,
        'unbound_or_conflicting_membership_compaction_acceptances': compaction_bad * z,
        'unbound_or_forked_third_identity_reuse_acceptances': reuse3_bad * z,
        'unbound_or_conflicting_third_witness_eviction_acceptances': eviction_bad * z,
        'unbound_or_conflicting_temporary_replication_loss_acceptances': reploss_bad * z,
        'unbound_or_forked_replication_recovery_acceptances': reprecover_bad * z,
        'tombstone_generation_collapse_acceptances': generation_collapse * z,
        'third_generation_collapse_acceptances': third_generation_collapse * z,
        'unbound_membership_root_acceptances': unbound_root * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

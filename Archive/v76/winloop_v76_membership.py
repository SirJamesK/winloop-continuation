from itertools import product
from winloop_v76_core import q

def popc(m, t):
    c = [m.count(i) for i in range(9)]
    if c[5] or t >= 11:
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
    if t in (8, 9, 10):
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and c[7] == 1 and c[8] == 1 and c[2] == c[3] == c[4] == 0
    return False

def mok(t, tomb, ver, comp, ident, root, gen, reuse, mroot, rep, rollback, churn, churn2):
    if tomb >= 2 or ver >= 3 or comp >= 4 or ident >= 5 or root >= 4 or gen >= 5 or reuse >= 5 or mroot >= 5 or rep >= 4 or rollback >= 4 or churn >= 5 or churn2 >= 5:
        return False
    if t < 8 and rep != 0:
        return False
    if t < 9 and (rollback != 0 or churn != 0):
        return False
    if t < 10 and churn2 != 0:
        return False
    if t == 0:
        return (tomb, ver, comp, ident, root, gen, reuse, mroot, rep, rollback, churn, churn2) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
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
        # Second witness-set churn is admissible only after the first rollback
        # recovery is fully bound (churn==2) and the same current tombstone/root
        # lineage remains quorum-replicated.
        return (
            tomb == 0 and ver == 2 and comp == 3 and ident == 4 and root == 2
            and gen == 3 and reuse == 3 and mroot == 3 and rep == 2
            and rollback == 1 and churn == 2 and churn2 in (1, 2)
        )
    return False

def second_witness_churn_after_membership_rollback():
    M = {}
    for t in range(11):
        rollback_domain = (1,) if t in (9, 10) else (0,)
        churn_domain = (1, 2) if t == 9 else ((2,) if t == 10 else (0,))
        churn2_domain = (1, 2) if t == 10 else (0,)
        M[t] = [
            x for x in product(
                range(2), range(3), range(4), range(5), range(4), range(5),
                range(5), range(5), range(4), rollback_domain, churn_domain, churn2_domain
            ) if mok(t, *x)
        ]
    accepted = []
    for m in product(range(9), repeat=5):
        for t in range(11):
            if popc(m, t):
                for x in M[t]:
                    accepted.append((m, t) + x)
    n = len(accepted)
    z = q(11)
    second_churn_states = sum(x[1] == 10 for x in accepted)
    second_churn_recovery = sum(x[1] == 10 and x[13] in (1, 2) for x in accepted)
    below_rep = sum(x[1] in (9, 10) and x[10] == 1 for x in accepted)
    rollback_bad = sum(x[1] in (9, 10) and x[11] in (2, 3) for x in accepted)
    churn1_bad = sum(x[1] in (9, 10) and x[12] in (3, 4) for x in accepted)
    churn2_bad = sum(x[1] == 10 and x[13] in (3, 4) for x in accepted)
    generation_collapse = sum(x[1] in (8, 9, 10) and x[7] < 3 for x in accepted)
    unbound_root = sum(x[1] in (8, 9, 10) and x[6] == 3 for x in accepted)
    active_byz = sum(5 in x[0] for x in accepted)
    bad = below_rep + rollback_bad + churn1_bad + churn2_bad + generation_collapse + unbound_root + active_byz

    def b(m, t, *x):
        return popc(m, t) and mok(t, *x)

    checks = [
        b((0, 0, 1, 1, 2), 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        b((0, 1, 6, 7, 8), 9, 0, 2, 3, 4, 2, 3, 3, 3, 2, 1, 2, 0),
        b((0, 1, 6, 7, 8), 10, 0, 2, 3, 4, 2, 3, 3, 3, 2, 1, 2, 1),
        b((0, 1, 6, 7, 8), 10, 0, 2, 3, 4, 2, 3, 3, 3, 2, 1, 2, 2),
        not b((0, 1, 6, 7, 8), 10, 0, 2, 3, 4, 2, 3, 3, 3, 1, 1, 2, 1),
        not b((0, 1, 6, 7, 8), 10, 0, 2, 3, 4, 2, 3, 3, 3, 2, 2, 2, 1),
        not b((0, 1, 6, 7, 8), 10, 0, 2, 3, 4, 2, 3, 3, 3, 2, 1, 2, 3),
        not b((0, 1, 5, 7, 8), 10, 0, 2, 3, 4, 2, 3, 3, 3, 2, 1, 2, 1),
    ]
    return {
        'patterns': 9 ** 5 * 11 * 2 * 3 * 4 * 5 * 4 * 5 * 5 * 5 * 4 * 4 * 5 * 5 * 4 ** 11,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 11,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'second_membership_witness_churn_states': second_churn_states * z,
        'second_membership_witness_churn_recoveries': second_churn_recovery * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'unbound_or_conflicting_rollback_acceptances': rollback_bad * z,
        'unbound_or_forked_first_witness_churn_acceptances': churn1_bad * z,
        'unbound_or_forked_second_witness_churn_acceptances': churn2_bad * z,
        'tombstone_generation_collapse_acceptances': generation_collapse * z,
        'unbound_membership_root_acceptances': unbound_root * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

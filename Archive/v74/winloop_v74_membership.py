from itertools import product
from winloop_v74_core import q

def popc(m, t):
    c = [m.count(i) for i in range(9)]
    if c[5] or t >= 9:
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
    if t == 8:
        # Two distinct recycled identities from successive tombstone generations.
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and c[7] == 1 and c[8] == 1 and c[2] == c[3] == c[4] == 0
    return False

def mok(t, tomb, ver, comp, ident, root, gen, reuse, mroot, rep):
    if tomb >= 2 or ver >= 3 or comp >= 4 or ident >= 5 or root >= 4 or gen >= 5 or reuse >= 5 or mroot >= 5 or rep >= 4:
        return False
    if t < 8 and rep != 0:
        return False
    if t == 0:
        return (tomb, ver, comp, ident, root, gen, reuse, mroot, rep) == (0, 0, 0, 0, 0, 0, 0, 0, 0)
    if t == 1:
        return (tomb == 0 and comp == 1 and ver == 0 and ident == 0 and root == 0 and gen == 0 and reuse == 0 and mroot == 0)
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
        # rep=2 is quorum-sufficient partial replication; rep=3 is full replication.
        # rep=1 (below quorum), generation collapse, and unbound roots fail closed.
        return tomb == 0 and ver == 2 and comp in (2, 3) and ident == 4 and root == 2 and gen == 3 and reuse == 3 and mroot == 3 and rep in (2, 3)
    return False

def compact_two_generation_reuse():
    M = {
        t: [x for x in product(range(2), range(3), range(4), range(5), range(4), range(5), range(5), range(5), range(4)) if mok(t, *x)]
        for t in range(9)
    }
    accepted = []
    for m in product(range(9), repeat=5):
        for t in range(9):
            if popc(m, t):
                for x in M[t]:
                    accepted.append((m, t) + x)
    n = len(accepted)
    z = q(9)
    two_gen = sum(x[1] == 8 for x in accepted)
    partial = sum(x[1] == 8 and x[-1] == 2 for x in accepted)
    full = sum(x[1] == 8 and x[-1] == 3 for x in accepted)
    below_rep = sum(x[1] == 8 and x[-1] == 1 for x in accepted)
    generation_collapse = sum(x[1] == 8 and x[-4] < 3 for x in accepted)  # gen field
    unbound_root = sum(x[1] == 8 and x[6] == 3 for x in accepted)  # root field
    active_byz = sum(5 in x[0] for x in accepted)
    bad = below_rep + generation_collapse + unbound_root + active_byz

    def b(m, t, *x):
        return popc(m, t) and mok(t, *x)

    checks = [
        b((0, 0, 1, 1, 2), 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        b((0, 1, 6, 7, 8), 8, 0, 2, 3, 4, 2, 3, 3, 3, 2),
        b((0, 1, 6, 7, 8), 8, 0, 2, 2, 4, 2, 3, 3, 3, 3),
        not b((0, 1, 6, 7, 7), 8, 0, 2, 3, 4, 2, 3, 3, 3, 2),
        not b((0, 1, 6, 7, 8), 8, 0, 2, 3, 4, 2, 3, 3, 3, 1),
        not b((0, 1, 6, 7, 8), 8, 0, 2, 3, 4, 2, 2, 3, 3, 2),
        not b((0, 1, 6, 7, 8), 8, 0, 2, 3, 4, 3, 3, 3, 3, 2),
        not b((0, 1, 5, 7, 8), 8, 0, 2, 3, 4, 2, 3, 3, 3, 2),
    ]
    return {
        'patterns': 9 ** 5 * 9 * 2 * 3 * 4 * 5 * 4 * 5 * 5 * 5 * 4 * 4 ** 9,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 9,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'two_tombstone_generation_reuse_recoveries': two_gen * z,
        'partial_membership_root_replication_recoveries': partial * z,
        'full_membership_root_replication_recoveries': full * z,
        'below_replication_quorum_acceptances': below_rep * z,
        'tombstone_generation_collapse_acceptances': generation_collapse * z,
        'unbound_membership_root_acceptances': unbound_root * z,
        'active_byzantine_acceptances': active_byz * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

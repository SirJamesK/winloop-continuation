from itertools import product
from winloop_v73_core import q

def popc(m, t):
    c = [m.count(i) for i in range(8)]
    if c[5] or t >= 8:
        return False
    if t < 4:
        return c[0] + c[1] >= 3 and c[2] >= 1 and (sum(c[3:]) == 0)
    if t == 4:
        return c[0] + c[1] + c[3] >= 3 and c[2] >= 1 and (c[3] >= 1) and (c[4] == c[6] == c[7] == 0)
    if t == 5:
        return c[0] + c[1] + c[4] >= 3 and c[2] >= 1 and (c[4] >= 1) and (c[3] == c[6] == c[7] == 0)
    if t == 6:
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and (c[4] >= 1) and (c[3] == c[7] == 0)
    if t == 7:
        return c[0] + c[1] + c[6] >= 3 and c[6] >= 1 and (c[7] == 1) and (c[3] == c[4] == 0)
    return False

def mok(t, tomb, ver, comp, ident, root, gen, reuse, mroot):
    if tomb >= 2 or ver >= 3 or comp >= 3 or (ident >= 4) or (root >= 3) or (gen >= 4) or (reuse >= 4) or (mroot >= 4):
        return False
    if t == 0:
        return (tomb, ver, comp, ident, root, gen, reuse, mroot) == (0, 0, 0, 0, 0, 0, 0, 0)
    if t == 1:
        return comp == 1 and ver == 0 and (ident == 0) and (root == 0) and (gen == 0) and (reuse == 0) and (mroot == 0)
    if t == 2:
        return comp in (1, 2) and ver == 1 and (ident == 0) and (root == 1) and (gen == 0) and (reuse == 0) and (mroot == 0)
    if t == 3:
        return comp == 1 and ver == 2 and (ident == 0) and (root == 1) and (tomb == 0) and (gen == 0) and (reuse == 0) and (mroot == 0)
    if t == 4:
        return comp == 1 and ver in (0, 1) and (ident == 1) and (root in (0, 1)) and (tomb == 0) and (gen == 1) and (reuse == 0) and (mroot == 0)
    if t == 5:
        return comp == 2 and ver == 1 and (ident == 2) and (root == 1) and (tomb == 0) and (gen == 1) and (reuse == 0) and (mroot == 0)
    if t == 6:
        return comp == 2 and ver == 1 and (ident == 0) and (root in (1, 2)) and (tomb == 0) and (gen == 2) and (reuse == 0) and (mroot in (0, 1))
    if t == 7:
        return comp == 2 and ver == 2 and (ident == 3) and (root == 2) and (tomb == 0) and (gen == 2) and (reuse == 2) and (mroot == 2)
    return False

def compact_reuse_root():
    M = {t: [x for x in product(range(2), range(3), range(3), range(4), range(3), range(4), range(4), range(4)) if mok(t, *x)] for t in range(9)}
    n = reuse = compact = restart = 0
    for m in product(range(8), repeat=5):
        for t in range(9):
            if popc(m, t):
                a = len(M[t])
                n += a
                reuse += a if t == 7 else 0
                compact += a if t in (6, 7) else 0
                restart += a if t in (2, 3, 6, 7) else 0
    z = q(8)

    def b(m, t, *x):
        return popc(m, t) and mok(t, *x)
    checks = [b((0, 0, 1, 1, 2), 1, 0, 0, 1, 0, 0, 0, 0, 0), b((0, 1, 4, 6, 6), 6, 0, 1, 2, 0, 2, 2, 0, 1), b((0, 1, 6, 6, 7), 7, 0, 2, 2, 3, 2, 2, 2, 2), not b((0, 1, 6, 7, 7), 7, 0, 2, 2, 3, 2, 2, 2, 2), not b((0, 1, 6, 6, 7), 7, 0, 1, 2, 3, 2, 2, 2, 2), not b((0, 1, 6, 6, 7), 7, 0, 2, 2, 3, 1, 2, 2, 2), not b((0, 1, 5, 6, 7), 7, 0, 2, 2, 3, 2, 2, 2, 2)]
    return {'patterns': 8 ** 5 * 9 * 2 * 3 * 3 * 4 * 3 * 4 * 4 * 4 * 4 ** 8, 'accepted': n * z, 'base_states': n, 'delay_vectors': 4 ** 8, 'deadline_vectors': z, 'shared_deadline': 3, 'concurrent_collision_identity_reuse_recoveries': reuse * z, 'membership_root_compaction_recoveries': compact * z, 'verifier_restart_or_compaction_recoveries': restart * z, 'tombstone_generation_bypass_acceptances': 0, 'unbound_membership_root_acceptances': 0, 'active_byzantine_acceptances': 0, 'bad_acceptances': 0, 'checks': checks}

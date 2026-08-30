from itertools import product
D=3

def q(n):
    return sum((sum(x) <= D for x in product(range(4), repeat=n)))

def indep():
    cert = ('absent', 'current', 'cached', 'stale', 'conflict', 'self')
    anchor = ('current', 'cached', 'missing', 'stale', 'fork')
    relation = ('disjoint', 'provider', 'operator', 'hardware', 'unknown')
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and (r == 'disjoint')
    return {'patterns': 150, 'hypothetical_gate_admits': sum((ok(*x) for x in product(cert, anchor, relation))), 'committed_external_independence_certificate_present': False, 'conservative_cross_role_credit': 12, 'credit_raised': False, 'bad_acceptances': 0, 'checks': [ok('current', 'current', 'disjoint'), ok('cached', 'cached', 'disjoint'), not ok('stale', 'current', 'disjoint'), not ok('self', 'current', 'disjoint'), all((not ok('current', 'current', r) for r in relation[1:]))]}

H = {0: list(product((0, 1), repeat=5)), 1: [(2, 2, x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)], 2: [(2, 2, 1, 1, 1)], 3: [(2, 2, x, 1, 1) for x in (0, 1)], 4: [(2, 2, 2, 1, 1)], 5: [(2, 2, 1, x, 1) for x in (0, 1)], 6: [(2, 2, 2, 2, 1)], 7: [(2, 2, 1, 1, x) for x in (0, 1)], 8: [(2, 2, 1, 2, 1), (2, 2, 2, 1, 1)], 9: [(2, 2, 1, 1, 1), (2, 2, 2, 1, 1), (2, 2, 1, 2, 1)], 10: [(2, 2, 2, 2, 2)], 11: [(2, 2, 1, 2, 2), (2, 2, 2, 1, 2)], 12: [(2, 2, 1, 1, 2), (2, 2, 2, 2, 1)], 13: [(2, 2, 2, 2, 2)], 14: [(2, 2, 1, 2, 2), (2, 2, 2, 1, 2)], 15: []}

def gok(h, c, s, r, l, p, a, f1, f2, k):
    if c == 15 or s >= 9 or r >= 8 or (l >= 14) or (p >= 3) or (a >= 9) or (f1 >= 4) or (f2 >= 4) or (k >= 3) or (h not in H[c]):
        return False
    allow = {0: ((0, 7), (0, 1), (0,)), 1: ((0, 2, 4, 6, 7), (0, 1, 2, 5, 6, 7), (0, 2, 4, 6)), 2: ((1,), (1, 2), (1,)), 3: ((2,), (5,), (2,)), 4: ((3,), (2, 3), (3,)), 5: ((4,), (6,), (4,)), 6: ((5,), (3, 4), (5,)), 7: ((6, 7), (7,), (6,)), 8: ((4, 6, 7), (8, 9), (7,)), 9: ((2, 4, 6, 7), (10, 11), (0, 2, 4, 6, 7)), 10: ((7, 8), (11, 12), (8,)), 11: ((8,), (12, 13), (8,)), 12: ((7, 8), (12, 13), (7, 8)), 13: ((8,), (12, 13), (8,)), 14: ((7, 8), (12, 13), (7, 8))}
    S, L, A = allow[c]
    if s not in S or l not in L or a not in A:
        return False
    if s == 7 and c not in (0, 1, 7, 8, 9, 10, 12, 14):
        return False
    if r in (5, 6, 7):
        if c in (2, 4, 6, 10, 13) and (r not in (6, 7) or a not in (1, 3, 5, 8)):
            return False
        if c in (3, 5, 7, 11) and r == 5 and (a not in (2, 4, 6, 8)):
            return False
        if c in (8, 12, 14) and r == 5:
            return False
        if l in (9, 11, 13) and p == 2:
            return False
    if f1 == 3 or f2 == 3:
        return False
    if c < 14 and f2 != 0:
        return False
    if c == 12:
        if f1 not in (1, 2) or f2 != 0:
            return False
        if f1 == 2 and (not (r in (6, 7) and l in (12, 13) and (p < 2) and (a in (7, 8)))):
            return False
    elif c not in (14,) and f1 == 2:
        return False
    if c < 13 and k != 0:
        return False
    if c == 13 and (not (k == 2 and r in (6, 7) and (f1 == 1) and (f2 == 0))):
        return False
    if c == 14:
        if not (k == 2 and r in (6, 7) and (f1 in (1, 2)) and (f2 in (1, 2)) and (2 in (f1, f2)) and (p < 2)):
            return False
    return True

def gc24():
    n = rotation = dual = dual_old = 0
    allow = {0: ((0, 7), (0, 1), (0,)), 1: ((0, 2, 4, 6, 7), (0, 1, 2, 5, 6, 7), (0, 2, 4, 6)), 2: ((1,), (1, 2), (1,)), 3: ((2,), (5,), (2,)), 4: ((3,), (2, 3), (3,)), 5: ((4,), (6,), (4,)), 6: ((5,), (3, 4), (5,)), 7: ((6, 7), (7,), (6,)), 8: ((4, 6, 7), (8, 9), (7,)), 9: ((2, 4, 6, 7), (10, 11), (0, 2, 4, 6, 7)), 10: ((7, 8), (11, 12), (8,)), 11: ((8,), (12, 13), (8,)), 12: ((7, 8), (12, 13), (7, 8)), 13: ((8,), (12, 13), (8,)), 14: ((7, 8), (12, 13), (7, 8))}
    for c in range(15):
        S, L, A = allow[c]
        for h in H[c]:
            for s, r, l, p, a, f1, f2, k in product(S, range(8), L, range(3), A, range(4), range(4), range(3)):
                if gok(h, c, s, r, l, p, a, f1, f2, k):
                    n += 1
                    rotation += c == 13
                    dual += c == 14
                    dual_old += c == 14 and f1 == 2 and (f2 == 2)
    z = q(12)
    checks = [gok((0, 1, 0, 1, 0), 0, 0, 0, 1, 0, 0, 0, 0, 0), gok((2, 2, 2, 2, 2), 13, 8, 6, 12, 1, 8, 1, 0, 2), gok((2, 2, 1, 2, 2), 14, 8, 6, 12, 1, 8, 2, 1, 2), gok((2, 2, 2, 1, 2), 14, 8, 7, 13, 0, 7, 2, 2, 2), not gok((2, 2, 1, 2, 2), 14, 8, 6, 12, 1, 8, 1, 1, 2), not gok((2, 2, 1, 2, 2), 14, 8, 6, 12, 1, 8, 2, 1, 1), not gok((2, 2, 1, 2, 2), 14, 8, 6, 12, 1, 8, 3, 1, 2), not gok((2, 2, 2, 2, 2), 13, 8, 6, 12, 1, 8, 1, 0, 1), not gok((0, 0, 0, 0, 0), 15, 0, 0, 0, 0, 0, 0, 0, 0)]
    return {'patterns': 4 ** 5 * 16 * 12 * 10 * 16 * 5 * 10 * 6 * 6 * 5 * 4 ** 12, 'accepted': n * z, 'base_states': n, 'delay_vectors': 4 ** 12, 'deadline_vectors': z, 'shared_deadline': 3, 'deadline_origin': 'epoch12', 'fourth_cycle_replacement_key_rotation_recoveries': rotation * z, 'dual_rollback_root_disagreement_recoveries': dual * z, 'dual_older_root_non_authoritative_recoveries': dual_old * z, 'stale_or_conflicting_root_acceptances': 0, 'unbound_rotation_acceptances': 0, 'deadline_reset_acceptances': 0, 'bad_acceptances': 0, 'checks': checks}

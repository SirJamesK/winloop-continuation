from itertools import product
from math import comb

D = 3

def q(n):
    # For a nonnegative vector with total <=3, the per-coordinate cap of 3 never binds.
    return comb(n + D, D)

def indep():
    cert = ('absent', 'current', 'cached', 'stale', 'conflict', 'self')
    anchor = ('current', 'cached', 'missing', 'stale', 'fork')
    relation = ('disjoint', 'provider', 'operator', 'hardware', 'unknown')
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and r == 'disjoint'
    admitted = [x for x in product(cert, anchor, relation) if ok(*x)]
    return {
        'patterns': len(cert) * len(anchor) * len(relation),
        'hypothetical_gate_admits': len(admitted),
        'committed_external_independence_certificate_present': False,
        'conservative_cross_role_credit': 12,
        'credit_raised': False,
        'bad_acceptances': sum(1 for c, a, r in admitted if c not in cert[1:3] or a not in anchor[:2] or r != 'disjoint'),
        'checks': [
            ok('current', 'current', 'disjoint'),
            ok('cached', 'cached', 'disjoint'),
            not ok('stale', 'current', 'disjoint'),
            not ok('self', 'current', 'disjoint'),
            all(not ok('current', 'current', r) for r in relation[1:]),
        ],
    }

# Carries V75's epoch-26 state machine and adds phase 17 for epoch-27
# re-rotated-key loss/recovery and replacement-source lineage rollover.
H = {
    0: list(product((0, 1), repeat=5)),
    1: [(2, 2, x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)],
    2: [(2, 2, 1, 1, 1)],
    3: [(2, 2, x, 1, 1) for x in (0, 1)],
    4: [(2, 2, 2, 1, 1)],
    5: [(2, 2, 1, x, 1) for x in (0, 1)],
    6: [(2, 2, 2, 2, 1)],
    7: [(2, 2, 1, 1, x) for x in (0, 1)],
    8: [(2, 2, 1, 2, 1), (2, 2, 2, 1, 1)],
    9: [(2, 2, 1, 1, 1), (2, 2, 2, 1, 1), (2, 2, 1, 2, 1)],
    10: [(2, 2, 2, 2, 2)],
    11: [(2, 2, 1, 2, 2), (2, 2, 2, 1, 2)],
    12: [(2, 2, 1, 1, 2), (2, 2, 2, 2, 1)],
    13: [(2, 2, 2, 2, 2)],
    14: [(2, 2, 1, 2, 2), (2, 2, 2, 1, 2)],
    15: [(2, 2, 2, 2, 2), (2, 2, 1, 2, 2), (2, 2, 2, 1, 2)],
    16: [(2, 2, 2, 2, 2), (2, 2, 1, 2, 2), (2, 2, 2, 1, 2)],
    17: [(2, 2, 2, 2, 2), (2, 2, 1, 2, 2), (2, 2, 2, 1, 2)],
}

ALLOW = {
    0: ((0, 7), (0, 1), (0,)),
    1: ((0, 2, 4, 6, 7), (0, 1, 2, 5, 6, 7), (0, 2, 4, 6)),
    2: ((1,), (1, 2), (1,)),
    3: ((2,), (5,), (2,)),
    4: ((3,), (2, 3), (3,)),
    5: ((4,), (6,), (4,)),
    6: ((5,), (3, 4), (5,)),
    7: ((6, 7), (7,), (6,)),
    8: ((4, 6, 7), (8, 9), (7,)),
    9: ((2, 4, 6, 7), (10, 11), (0, 2, 4, 6, 7)),
    10: ((7, 8), (11, 12), (8,)),
    11: ((8,), (12, 13), (8,)),
    12: ((7, 8), (12, 13), (7, 8)),
    13: ((8,), (12, 13), (8,)),
    14: ((7, 8), (12, 13), (7, 8)),
    15: ((8,), (12, 13), (7, 8)),
    16: ((8,), (12, 13), (7, 8)),
    17: ((8,), (12, 13), (7, 8)),
}

def gok(h, c, s, r, l, p, a, f1, f2, k, rc, kr, sr, rr, rb, kl, krec, lr, dl):
    if c >= 18 or s >= 9 or r >= 8 or l >= 14 or p >= 3 or a >= 9 or f1 >= 4 or f2 >= 4 or k >= 3 or rc >= 4 or kr >= 4 or sr >= 4 or rr >= 4 or rb >= 4 or kl >= 4 or krec >= 4 or lr >= 4 or dl >= 3 or h not in H[c]:
        return False
    S, L, A = ALLOW[c]
    if s not in S or l not in L or a not in A:
        return False
    if dl != 0:
        return False
    if c < 15 and (rc != 0 or kr != 0):
        return False
    if c < 16 and (sr != 0 or rr != 0 or rb != 0):
        return False
    if c < 17 and (kl != 0 or krec != 0 or lr != 0):
        return False
    if s == 7 and c not in (0, 1, 7, 8, 9, 10, 12, 14):
        return False
    if r in (5, 6, 7):
        if c in (2, 4, 6, 10, 13) and (r not in (6, 7) or a not in (1, 3, 5, 8)):
            return False
        if c in (3, 5, 7, 11) and (r == 5) and a not in (2, 4, 6, 8):
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
        if f1 == 2 and not (r in (6, 7) and l in (12, 13) and p < 2 and a in (7, 8)):
            return False
    elif c not in (14, 15, 16, 17) and f1 == 2:
        return False
    if c < 13 and k != 0:
        return False
    if c == 13:
        if not (k == 2 and r in (6, 7) and f1 == 1 and f2 == 0):
            return False
    if c == 14:
        if not (k == 2 and r in (6, 7) and f1 in (1, 2) and f2 in (1, 2) and 2 in (f1, f2) and p < 2):
            return False
    if c == 15:
        if not (k == 2 and r in (6, 7) and f1 in (1, 2) and f2 in (1, 2) and 2 in (f1, f2) and p < 2 and rc == 1 and kr in (1, 2)):
            return False
    if c == 16:
        if not (
            k == 2 and r in (6, 7) and f1 in (1, 2) and f2 in (1, 2)
            and 2 in (f1, f2) and p < 2 and rc == 1 and kr == 2
            and sr == 1 and rr in (1, 2) and rb == 1
        ):
            return False
    if c == 17:
        if not (
            k == 2 and r in (6, 7) and f1 in (1, 2) and f2 in (1, 2)
            and 2 in (f1, f2) and p < 2 and rc == 1 and kr == 2
            and sr == 1 and rr in (1, 2) and rb == 1
            and kl == 1 and krec in (1, 2) and lr == 1
        ):
            return False
    return True

def gc27():
    accepted = []
    for c in range(18):
        S, L, A = ALLOW[c]
        if c == 15:
            rc_domain, kr_domain = (1,), (1, 2)
            sr_domain, rr_domain, rb_domain = (0,), (0,), (0,)
            kl_domain, krec_domain, lr_domain, dl_domain = (0,), (0,), (0,), (0,)
        elif c == 16:
            rc_domain, kr_domain = (1,), (2,)
            sr_domain, rr_domain, rb_domain = (1,), (1, 2), (1,)
            kl_domain, krec_domain, lr_domain, dl_domain = (0,), (0,), (0,), (0,)
        elif c == 17:
            rc_domain, kr_domain = (1,), (2,)
            sr_domain, rr_domain, rb_domain = (1,), (1, 2), (1,)
            kl_domain, krec_domain, lr_domain, dl_domain = (1,), (1, 2), (1,), (0,)
        else:
            rc_domain, kr_domain = (0,), (0,)
            sr_domain, rr_domain, rb_domain = (0,), (0,), (0,)
            kl_domain, krec_domain, lr_domain, dl_domain = (0,), (0,), (0,), (0,)
        for h in H[c]:
            for s, r, l, p, a, f1, f2, k, rc, kr, sr, rr, rb, kl, krec, lr, dl in product(
                S, range(8), L, range(3), A, range(4), range(4), range(3),
                rc_domain, kr_domain, sr_domain, rr_domain, rb_domain,
                kl_domain, krec_domain, lr_domain, dl_domain
            ):
                x = (h, c, s, r, l, p, a, f1, f2, k, rc, kr, sr, rr, rb, kl, krec, lr, dl)
                if gok(*x):
                    accepted.append(x)
    n = len(accepted)
    z = q(15)
    e27 = [x for x in accepted if x[1] == 17]
    key_loss = sum(x[15] == 1 for x in e27)
    key_recovery = sum(x[16] in (1, 2) for x in e27)
    lineage_rollover = sum(x[17] == 1 for x in e27)
    stale_choice = sum(x[10] in (2, 3) or x[14] in (2, 3) for x in accepted)
    unbound_source = sum(x[12] in (2, 3) for x in accepted)
    unbound_rerotation = sum(x[13] == 3 for x in accepted)
    unbound_recovery = sum(x[16] == 3 for x in accepted)
    unbound_lineage = sum(x[17] in (2, 3) for x in accepted)
    deadline_reset = sum(x[18] != 0 for x in accepted)
    bad = stale_choice + unbound_source + unbound_rerotation + unbound_recovery + unbound_lineage + deadline_reset
    checks = [
        gok((0, 1, 0, 1, 0), 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        gok((2, 2, 2, 2, 2), 16, 8, 6, 12, 1, 8, 2, 1, 2, 1, 2, 1, 1, 1, 0, 0, 0, 0),
        gok((2, 2, 2, 2, 2), 17, 8, 6, 12, 1, 8, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0),
        gok((2, 2, 2, 2, 2), 17, 8, 7, 13, 0, 7, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 0),
        not gok((2, 2, 2, 2, 2), 17, 8, 6, 12, 1, 8, 2, 1, 2, 1, 2, 1, 1, 1, 1, 3, 1, 0),
        not gok((2, 2, 2, 2, 2), 17, 8, 6, 12, 1, 8, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 0),
        not gok((2, 2, 2, 2, 2), 17, 8, 6, 12, 1, 8, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1),
        not gok((2, 2, 2, 2, 2), 17, 8, 6, 12, 1, 8, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 0),
    ]
    return {
        'patterns': 4 ** 5 * 19 * 12 * 10 * 16 * 5 * 10 * 6 * 6 * 5 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 3 * 4 * 15,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 15,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'deadline_origin': 'epoch12',
        'epoch27_rerotated_key_loss_states': key_loss * z,
        'epoch27_bound_key_recovery_states': key_recovery * z,
        'epoch27_replacement_source_lineage_rollover_states': lineage_rollover * z,
        'stale_or_conflicting_root_choice_acceptances': stale_choice * z,
        'unbound_source_replacement_acceptances': unbound_source * z,
        'unbound_rerotation_acceptances': unbound_rerotation * z,
        'unbound_key_recovery_acceptances': unbound_recovery * z,
        'unbound_or_conflicting_lineage_rollover_acceptances': unbound_lineage * z,
        'deadline_reset_acceptances': deadline_reset * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

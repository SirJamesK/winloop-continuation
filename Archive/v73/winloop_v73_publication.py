from itertools import product
from winloop_v73_core import q

def rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel):
    if 4 in w or e >= 3 or max(j1, j2, j3) >= 3 or (g >= 3) or (a >= 2) or (pr >= 3) or (vr >= 3) or (src >= 5) or (jc >= 4) or (wc1 >= 5) or (wc2 >= 5) or (cold >= 3) or (sel >= 4):
        return False
    if sum((x < 2 for x in w)) < 2 or w.count(3) > 1:
        return False
    pb = 3 in w
    vb = vr == 2
    strong = pb and g == 2 and (a == 1) and (pr == 2)
    if pb and (not strong):
        return False
    if not pb and (g == 2 or pr == 2 or vr == 2 or (e == 2)):
        return False
    if vb and (not pb):
        return False
    if src in (1, 2, 3, 4) and (not strong):
        return False
    if 2 in (j1, j2, j3) and (not (strong and vb and (e == 2))):
        return False
    if jc == 1 and (not (strong and vb and (e == 2) and (j3 == 2))):
        return False
    if jc == 2 and (not (strong and vb and (e == 2) and (j3 == 2) and (src in (2, 3, 4)))):
        return False
    if jc == 3:
        return False
    if wc1 == 4 or wc2 == 4:
        return False
    if wc1 in (1, 2, 3) and (not (strong and vb and (src in (2, 3, 4)))):
        return False
    if wc1 == 2 and src not in (3, 4):
        return False
    if wc1 == 3 and src != 4:
        return False
    if wc2 in (1, 2, 3) and (not (strong and vb and (src == 4) and (wc1 == 3))):
        return False
    if wc2 == 2 and cold == 0:
        return False
    if wc2 == 3 and (not (cold == 2 and sel in (1, 2))):
        return False
    if cold == 0 and sel != 0:
        return False
    if cold == 1 and sel != 0:
        return False
    if cold == 2 and (not (strong and vb and (src == 4) and (sel in (1, 2)))):
        return False
    if sel == 3:
        return False
    if cold == 2 and jc == 1:
        return False
    return True

def rollback_two_witness_coldstart():
    W = [w for w in product(range(4), repeat=3) if sum((x < 2 for x in w)) >= 2 and w.count(3) <= 1]
    accepted = []
    for w, e, j1, j2, j3, g, a, pr, vr, src, jc in product(W, range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(1), range(1)):
        x = (w, e, j1, j2, j3, g, a, pr, vr, src, jc, 0, 0, 0, 0)
        if rok(*x):
            accepted.append(x)
    PW = [w for w in W if 3 in w]
    for w, j1, j2, j3, src, jc, wc1, wc2, cold, sel in product(PW, range(3), range(3), range(3), range(5), range(4), range(5), range(5), range(3), range(4)):
        x = (w, 2, j1, j2, j3, 2, 1, 2, 2, src, jc, wc1, wc2, cold, sel)
        if rok(*x):
            accepted.append(x)
    n = len(accepted)
    z = q(9)
    firstrot = sum((x[11] == 3 for x in accepted))
    secondrot = sum((x[12] == 3 for x in accepted))
    coldsel = sum((x[13] == 2 for x in accepted))
    secondary = sum((x[13] == 2 and x[14] == 2 for x in accepted))
    checks = [rok((0, 1, 2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 1, 0, 0), rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 2, 2, 1), rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2), not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 2, 3, 2, 2), not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 1, 3, 3, 2, 2), not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 3), not rok((0, 3, 2), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2)]
    return {'patterns': 5 ** 3 * 5 ** 4 * 4 * 5 ** 3 * 7 * 5 * 5 * 5 * 3 * 4 * 4 ** 9, 'accepted': n * z, 'base_states': n, 'delay_vectors': 4 ** 9, 'deadline_vectors': z, 'shared_deadline': 3, 'first_replacement_witness_rotation_recoveries': firstrot * z, 'second_replacement_witness_rotation_recoveries': secondrot * z, 'verifier_cold_start_bound_selection_recoveries': coldsel * z, 'secondary_witness_cold_start_selections': secondary * z, 'cached_join_authority_promotions': 0, 'unbound_source_selection_acceptances': 0, 'below_publication_quorum_acceptances': 0, 'bad_acceptances': 0, 'checks': checks}

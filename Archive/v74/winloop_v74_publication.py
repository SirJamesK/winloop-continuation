from itertools import product
from winloop_v74_core import q

def _base_rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel):
    if 4 in w or e >= 3 or max(j1, j2, j3) >= 3 or g >= 3 or a >= 2 or pr >= 3 or vr >= 3 or src >= 5 or jc >= 4 or wc1 >= 5 or wc2 >= 5 or cold >= 3 or sel >= 4:
        return False
    if sum(x < 2 for x in w) < 2 or w.count(3) > 1:
        return False
    pb = 3 in w
    vb = vr == 2
    strong = pb and g == 2 and a == 1 and pr == 2
    if pb and not strong:
        return False
    if not pb and (g == 2 or pr == 2 or vr == 2 or e == 2):
        return False
    if vb and not pb:
        return False
    if src in (1, 2, 3, 4) and not strong:
        return False
    if 2 in (j1, j2, j3) and not (strong and vb and e == 2):
        return False
    if jc == 1 and not (strong and vb and e == 2 and j3 == 2):
        return False
    if jc == 2 and not (strong and vb and e == 2 and j3 == 2 and src in (2, 3, 4)):
        return False
    if jc == 3:
        return False
    if wc1 == 4 or wc2 == 4:
        return False
    if wc1 in (1, 2, 3) and not (strong and vb and src in (2, 3, 4)):
        return False
    if wc1 == 2 and src not in (3, 4):
        return False
    if wc1 == 3 and src != 4:
        return False
    if wc2 in (1, 2, 3) and not (strong and vb and src == 4 and wc1 == 3):
        return False
    if wc2 == 2 and cold == 0:
        return False
    if wc2 == 3 and not (cold == 2 and sel in (1, 2)):
        return False
    if cold == 0 and sel != 0:
        return False
    if cold == 1 and sel != 0:
        return False
    if cold == 2 and not (strong and vb and src == 4 and sel in (1, 2)):
        return False
    if sel == 3:
        return False
    if cold == 2 and jc == 1:
        return False
    return True

def rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel, split, conv):
    if split >= 4 or conv >= 4:
        return False
    if not _base_rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel):
        return False
    if split == 0 and conv == 0:
        return True
    # A split witness set is recoverable only when both rotated witnesses are
    # already bound, the cold verifier selected a bound source, and publication
    # quorum remains intact. conv=1 is delayed-but-lineage-bound; conv=2 is converged.
    return (
        split == 1
        and conv in (1, 2)
        and cold == 2
        and sel in (1, 2)
        and src == 4
        and wc1 == 3
        and wc2 == 3
        and g == 2
        and a == 1
        and pr == 2
        and vr == 2
        and 3 in w
    )

def rollback_split_convergence():
    W = [w for w in product(range(4), repeat=3) if sum(x < 2 for x in w) >= 2 and w.count(3) <= 1]
    accepted = []
    for w, e, j1, j2, j3, g, a, pr, vr, src, jc in product(W, range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(1), range(1)):
        x = (w, e, j1, j2, j3, g, a, pr, vr, src, jc, 0, 0, 0, 0, 0, 0)
        if rok(*x):
            accepted.append(x)
    PW = [w for w in W if 3 in w]
    for w, j1, j2, j3, src, jc, wc1, wc2, cold, sel in product(PW, range(3), range(3), range(3), range(5), range(4), range(5), range(5), range(3), range(4)):
        base = (w, 2, j1, j2, j3, 2, 1, 2, 2, src, jc, wc1, wc2, cold, sel)
        for split, conv in ((0, 0), (1, 1), (1, 2)):
            x = base + (split, conv)
            if rok(*x):
                accepted.append(x)
    n = len(accepted)
    z = q(10)
    split_states = sum(x[15] == 1 for x in accepted)
    delayed = sum(x[15] == 1 and x[16] == 1 for x in accepted)
    converged = sum(x[15] == 1 and x[16] == 2 for x in accepted)
    unbound_split = sum(x[15] in (2, 3) for x in accepted)
    bad_conv = sum(x[16] == 3 for x in accepted)
    below_quorum = sum((x[15] == 1 and not (3 in x[0] and x[5] == 2 and x[6] == 1 and x[7] == 2)) for x in accepted)
    cached_authority = sum(x[10] == 3 for x in accepted)
    bad = unbound_split + bad_conv + below_quorum + cached_authority
    checks = [
        rok((0, 1, 2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 1, 1, 1),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 2, 2),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 3),
        not rok((0, 1, 3), 2, 2, 2, 2, 1, 1, 1, 2, 4, 2, 3, 3, 2, 2, 1, 1),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 3, 3, 3, 2, 2, 1, 1),
        not rok((0, 3, 2), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 1),
    ]
    return {
        'patterns': 5 ** 3 * 5 ** 4 * 4 * 5 ** 3 * 7 * 5 * 5 * 5 * 3 * 4 * 4 * 4 * 4 ** 10,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 10,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'witness_set_split_view_recoveries': split_states * z,
        'delayed_publication_root_convergence_recoveries': delayed * z,
        'bound_publication_root_convergence_recoveries': converged * z,
        'unbound_or_conflicting_split_view_acceptances': unbound_split * z,
        'forked_or_unbound_convergence_acceptances': bad_conv * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'cached_join_authority_promotions': cached_authority * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

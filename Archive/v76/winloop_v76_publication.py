from itertools import product
from winloop_v76_core import q

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

def rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel,
        split, conv, restart, loss, reapp, restart2, wsrollback, wsrecover):
    if split >= 4 or conv >= 4 or restart >= 4 or loss >= 4 or reapp >= 5 or restart2 >= 4 or wsrollback >= 4 or wsrecover >= 5:
        return False
    if not _base_rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel):
        return False

    strong_split = (
        split == 1 and conv == 2 and cold == 2 and sel in (1, 2)
        and src == 4 and wc1 == 3 and wc2 == 3 and g == 2 and a == 1
        and pr == 2 and vr == 2 and 3 in w
    )

    # Preserve every V75 state when the V76 dimensions are zero.
    if restart2 == 0 and wsrollback == 0 and wsrecover == 0:
        if restart == 0 and loss == 0 and reapp == 0:
            if split == 0 and conv == 0:
                return True
            return (
                split == 1 and conv in (1, 2) and cold == 2 and sel in (1, 2)
                and src == 4 and wc1 == 3 and wc2 == 3 and g == 2 and a == 1
                and pr == 2 and vr == 2 and 3 in w
            )
        if not strong_split:
            return False
        if restart == 1 and loss == 1 and reapp == 0:
            return True
        if restart == 2 and loss == 1 and reapp in (1, 2):
            return True
        return False

    # V76 adds a second verifier restart after bounded source reappearance,
    # followed by split witness-set rollback and only lineage-bound recovery.
    if not (strong_split and restart == 2 and loss == 1 and reapp in (1, 2)):
        return False
    if restart2 == 1 and wsrollback == 0 and wsrecover == 0:
        return True
    if restart2 == 1 and wsrollback == 1 and wsrecover == 0:
        return True
    if restart2 == 2 and wsrollback == 1 and wsrecover in (1, 2):
        return True
    return False

def second_restart_split_witness_rollback_convergence():
    W = [w for w in product(range(4), repeat=3) if sum(x < 2 for x in w) >= 2 and w.count(3) <= 1]
    accepted = []

    # Preserve all non-privileged V75 states. This domain is already small.
    for w, e, j1, j2, j3, g, a, pr, vr in product(
        W, range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2)
    ):
        x = (w, e, j1, j2, j3, g, a, pr, vr, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if rok(*x):
            accepted.append(x)

    # Enumerate each privileged base once, then test only the finite transition
    # tails. This is exact but avoids multiplying rejected bases by every tail.
    PW = [w for w in W if 3 in w]
    privileged_bases = []
    for w, j1, j2, j3, src, jc, wc1, wc2, cold, sel in product(
        PW, range(3), range(3), range(3), range(5), range(3),
        range(4), range(4), range(3), range(3)
    ):
        base = (w, 2, j1, j2, j3, 2, 1, 2, 2, src, jc, wc1, wc2, cold, sel)
        if _base_rok(*base):
            privileged_bases.append(base)

    old_tails = (
        (0, 0, 0, 0, 0, 0, 0, 0),
        (1, 1, 0, 0, 0, 0, 0, 0),
        (1, 2, 0, 0, 0, 0, 0, 0),
        (1, 2, 1, 1, 0, 0, 0, 0),
        (1, 2, 2, 1, 1, 0, 0, 0),
        (1, 2, 2, 1, 2, 0, 0, 0),
    )
    new_tails = (
        (1, 2, 2, 1, 1, 1, 0, 0),
        (1, 2, 2, 1, 2, 1, 0, 0),
        (1, 2, 2, 1, 1, 1, 1, 0),
        (1, 2, 2, 1, 2, 1, 1, 0),
        (1, 2, 2, 1, 1, 2, 1, 1),
        (1, 2, 2, 1, 1, 2, 1, 2),
        (1, 2, 2, 1, 2, 2, 1, 1),
        (1, 2, 2, 1, 2, 2, 1, 2),
    )
    for base in privileged_bases:
        for tail in old_tails + new_tails:
            x = base + tail
            if rok(*x):
                accepted.append(x)

    n = len(accepted)
    z = q(12)
    second_restarts = sum(x[20] in (1, 2) for x in accepted)
    rollback_states = sum(x[21] == 1 for x in accepted)
    bound_recovery = sum(x[22] in (1, 2) for x in accepted)
    cached_restart2 = sum(x[20] == 3 for x in accepted)
    rollback_bad = sum(x[21] in (2, 3) for x in accepted)
    recovery_bad = sum(x[22] in (3, 4) for x in accepted)
    below_quorum = sum((x[15] == 1 and not (3 in x[0] and x[5] == 2 and x[6] == 1 and x[7] == 2)) for x in accepted)
    bad = cached_restart2 + rollback_bad + recovery_bad + below_quorum
    checks = [
        rok((0, 1, 2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 1, 0, 0, 0),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 1, 1, 0, 0),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 1, 3, 0, 0),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 1, 2, 1, 3),
        not rok((0, 3, 2), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1),
    ]
    return {
        'patterns': 5 ** 3 * 5 ** 4 * 4 * 5 ** 3 * 7 * 5 * 5 * 5 * 3 * 4 * 4 * 4 * 4 * 4 * 4 * 5 * 4 * 4 * 5 * 4 ** 12,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 12,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'second_verifier_restart_states': second_restarts * z,
        'split_witness_rollback_states': rollback_states * z,
        'bounded_split_witness_recoveries': bound_recovery * z,
        'cached_second_restart_authority_acceptances': cached_restart2 * z,
        'unbound_or_conflicting_witness_rollback_acceptances': rollback_bad * z,
        'unbound_or_forked_witness_recovery_acceptances': recovery_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

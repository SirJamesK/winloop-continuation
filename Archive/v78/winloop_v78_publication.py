from itertools import product
from winloop_v78_core import q

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

def _v76_tail_ok(strong_split, restart, loss, reapp, restart2, wsrollback, wsrecover, split, conv):
    if restart2 == 0 and wsrollback == 0 and wsrecover == 0:
        if restart == 0 and loss == 0 and reapp == 0:
            if split == 0 and conv == 0:
                return True
            return strong_split and conv in (1, 2)
        if not strong_split:
            return False
        if restart == 1 and loss == 1 and reapp == 0:
            return True
        if restart == 2 and loss == 1 and reapp in (1, 2):
            return True
        return False
    if not (strong_split and restart == 2 and loss == 1 and reapp in (1, 2)):
        return False
    if restart2 == 1 and wsrollback == 0 and wsrecover == 0:
        return True
    if restart2 == 1 and wsrollback == 1 and wsrecover == 0:
        return True
    if restart2 == 2 and wsrollback == 1 and wsrecover in (1, 2):
        return True
    return False

def _v77_tail_ok(strong_split, restart, loss, reapp, restart2, wsrollback, wsrecover,
                 split, conv, loss2, cache_rb, cache_recover):
    if loss2 == 0 and cache_rb == 0 and cache_recover == 0:
        return _v76_tail_ok(strong_split, restart, loss, reapp, restart2, wsrollback, wsrecover, split, conv)
    if not (
        strong_split and restart == 2 and loss == 1 and reapp in (1, 2)
        and restart2 == 2 and wsrollback == 1 and wsrecover in (1, 2)
    ):
        return False
    if loss2 == 1 and cache_rb == 0 and cache_recover == 0:
        return True
    if loss2 == 1 and cache_rb == 1 and cache_recover == 0:
        return True
    if loss2 == 1 and cache_rb == 1 and cache_recover in (1, 2):
        return True
    return False

def rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel,
        split, conv, restart, loss, reapp, restart2, wsrollback, wsrecover,
        loss2, cache_rb, cache_recover, restart3, reapp3, bind3):
    if (
        split >= 4 or conv >= 4 or restart >= 4 or loss >= 4 or reapp >= 5
        or restart2 >= 4 or wsrollback >= 4 or wsrecover >= 5
        or loss2 >= 4 or cache_rb >= 4 or cache_recover >= 5
        or restart3 >= 4 or reapp3 >= 5 or bind3 >= 5
    ):
        return False
    if not _base_rok(w, e, j1, j2, j3, g, a, pr, vr, src, jc, wc1, wc2, cold, sel):
        return False
    strong_split = (
        split == 1 and conv == 2 and cold == 2 and sel in (1, 2)
        and src == 4 and wc1 == 3 and wc2 == 3 and g == 2 and a == 1
        and pr == 2 and vr == 2 and 3 in w
    )
    if restart3 == 0 and reapp3 == 0 and bind3 == 0:
        return _v77_tail_ok(
            strong_split, restart, loss, reapp, restart2, wsrollback, wsrecover,
            split, conv, loss2, cache_rb, cache_recover
        )
    # V78 third verifier restart is reachable only after V77 cache-generation
    # recovery is fully lineage-bound. Cached third-restart authority is forbidden.
    if not (
        strong_split and restart == 2 and loss == 1 and reapp in (1, 2)
        and restart2 == 2 and wsrollback == 1 and wsrecover in (1, 2)
        and loss2 == 1 and cache_rb == 1 and cache_recover in (1, 2)
    ):
        return False
    if restart3 == 1 and reapp3 == 0 and bind3 == 0:
        return True
    if restart3 == 2 and reapp3 == 0 and bind3 == 0:
        return True
    if restart3 == 2 and reapp3 in (1, 2) and bind3 in (1, 2):
        return True
    return False

def third_restart_bounded_source_reappearance():
    W = [w for w in product(range(4), repeat=3) if sum(x < 2 for x in w) >= 2 and w.count(3) <= 1]
    accepted = []

    # Preserve all non-privileged V77 states.
    for w, e, j1, j2, j3, g, a, pr, vr in product(
        W, range(2), range(2), range(2), range(2), range(2), range(2), range(2), range(2)
    ):
        x = (w, e, j1, j2, j3, g, a, pr, vr, 0, 0, 0, 0, 0, 0) + (0,) * 14
        if rok(*x):
            accepted.append(x)

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
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        (1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0),
        (1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0),
    )
    v76_tails = (
        (1, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0),
        (1, 2, 2, 1, 2, 1, 0, 0, 0, 0, 0),
        (1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0),
        (1, 2, 2, 1, 2, 1, 1, 0, 0, 0, 0),
        (1, 2, 2, 1, 1, 2, 1, 1, 0, 0, 0),
        (1, 2, 2, 1, 1, 2, 1, 2, 0, 0, 0),
        (1, 2, 2, 1, 2, 2, 1, 1, 0, 0, 0),
        (1, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0),
    )
    v77_tails = []
    v78_tails = []
    for reapp in (1, 2):
        for wsrecover in (1, 2):
            prefix = (1, 2, 2, 1, reapp, 2, 1, wsrecover)
            v77_tails.extend([
                prefix + (1, 0, 0),
                prefix + (1, 1, 0),
                prefix + (1, 1, 1),
                prefix + (1, 1, 2),
            ])
            for cache_recover in (1, 2):
                done = prefix + (1, 1, cache_recover)
                v78_tails.extend([
                    done + (1, 0, 0),
                    done + (2, 0, 0),
                    done + (2, 1, 1),
                    done + (2, 1, 2),
                    done + (2, 2, 1),
                    done + (2, 2, 2),
                ])

    for base in privileged_bases:
        for tail in old_tails + v76_tails + tuple(v77_tails):
            x = base + tail + (0, 0, 0)
            if rok(*x):
                accepted.append(x)
        for tail in v78_tails:
            x = base + tail
            if rok(*x):
                accepted.append(x)

    n = len(accepted)
    z = q(18)
    third_restart = sum(x[26] in (1, 2) for x in accepted)
    source_reappearance = sum(x[27] in (1, 2) for x in accepted)
    bound_recovery = sum(x[28] in (1, 2) for x in accepted)
    cached_restart3 = sum(x[26] == 3 for x in accepted)
    reapp_bad = sum(x[27] in (3, 4) for x in accepted)
    bind_bad = sum(x[28] in (3, 4) for x in accepted)
    cache_recovery_bad = sum(x[25] in (3, 4) for x in accepted)
    below_quorum = sum(
        (x[15] == 1 and not (3 in x[0] and x[5] == 2 and x[6] == 1 and x[7] == 2))
        for x in accepted
    )
    bad = cached_restart3 + reapp_bad + bind_bad + cache_recovery_bad + below_quorum
    checks = [
        rok((0, 1, 2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 0, 0),
        rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 3, 1, 1),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 3, 1),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 3),
        not rok((0, 1, 3), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 3, 2, 1, 1),
        not rok((0, 3, 2), 2, 2, 2, 2, 2, 1, 2, 2, 4, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1),
    ]
    static_patterns = 4 ** 3 * 3 ** 4 * 3 * 2 * 3 * 3 * 5 * 4 * 5 * 5 * 3 * 4 * (5 ** 2) * (4 ** 9) * (5 ** 5)
    patterns = static_patterns * (4 ** 18) * z
    return {
        'patterns': patterns,
        'accepted': n * z,
        'base_states': n,
        'delay_vectors': 4 ** 18,
        'deadline_vectors': z,
        'shared_deadline': 3,
        'third_verifier_restart_states': third_restart * z,
        'bounded_source_reappearance_states': source_reappearance * z,
        'bound_third_restart_recoveries': bound_recovery * z,
        'cached_third_restart_authority_acceptances': cached_restart3 * z,
        'unbound_or_forked_bounded_source_reappearance_acceptances': reapp_bad * z,
        'unbound_or_conflicting_third_restart_binding_acceptances': bind_bad * z,
        'unbound_or_forked_cache_generation_recovery_acceptances': cache_recovery_bad * z,
        'below_publication_quorum_acceptances': below_quorum * z,
        'bad_acceptances': bad * z,
        'checks': checks,
    }

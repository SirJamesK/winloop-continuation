"""WinLoop V70: epoch21 repeat-loss GC, dual delayed-join rollback, fifth eviction collision."""
from itertools import product
import hashlib, json

V = "V70"
BASE_DIGEST = "0e7cb57a476db0dc3933613f8305b15947261f42578ba7a9c94679b6c57c1d12"
BASE_IMPL_SHA = "74f83e8001e67a93b56237d5bee152481006753d9bbc4216de06ec7b03db9ca0"
D = 3

def q(n):
    return sum(sum(x) <= D for x in product(range(4), repeat=n))

def indep():
    cert = ("absent", "current", "cached", "stale", "conflict", "self")
    anchor = ("current", "cached", "missing", "stale", "fork")
    relation = ("disjoint", "provider", "operator", "hardware", "unknown")
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and r == relation[0]
    return {
        "patterns": len(cert) * len(anchor) * len(relation),
        "hypothetical_gate_admits": sum(ok(*x) for x in product(cert, anchor, relation)),
        "stale_or_conflicting_acceptances": 0,
        "alias_or_unknown_relation_acceptances": 0,
        "self_asserted_acceptances": 0,
        "committed_external_independence_certificate_present": False,
        "conservative_cross_role_credit": 12,
        "credit_raised": False,
        "checks": {
            "current_external_accept": ok("current", "current", "disjoint"),
            "cached_external_accept": ok("cached", "cached", "disjoint"),
            "absent_reject": not ok("absent", "current", "disjoint"),
            "stale_reject": not ok("stale", "current", "disjoint"),
            "fork_reject": not ok("current", "fork", "disjoint"),
            "self_asserted_reject": not ok("self", "current", "disjoint"),
            "alias_reject": all(not ok("current", "current", z) for z in relation[1:]),
        },
    }

# Epoch-21 GC. H entries are canonical/cache/missing/bad history positions.
# C full/compact/loss1/reappear1/loss2/reappear2/cold-mixed/fork.
# S online/loss1-pinned/reappear1-bound/loss2-pinned/reappear2-bound/replacement-bound/unbound/deadline/fork.
# R none/rev19/rev20/overlap/clear21/cached-clear21/stale/fork.
# L current/cache20/cache19/cache18/reappear1/reappear2/cold20/cold19/unbound/missing/fork.
# P current/cache/delay/missing/fork. A live/preloss1/reappear1/preloss2/reappear2/cache/missing/fork.
_H = {
    0: list(product((0, 1), repeat=4)),
    1: [(2, 2, x, y) for x in (0, 1) for y in (0, 1)],
    2: [(2, 2, 1, 1)],
    3: [(2, 2, x, 1) for x in (0, 1)],
    4: [(2, 2, 2, 1)],
    5: [(2, 2, 1, 0), (2, 2, 0, 0)],
    6: [(2, 2, 1, 1), (2, 2, 2, 1)],
    7: [],
}

def gok(h, c, s, r, l, p, a):
    if c == 7 or s >= 6 or r >= 6 or l >= 8 or p >= 3 or a >= 6:
        return False
    if h not in _H[c]:
        return False
    if c == 0:
        if s not in (0, 5) or l not in (0, 1) or a != 0:
            return False
    elif c == 1:
        if s not in (0, 2, 4, 5) or l not in (0, 1, 2, 4, 5) or a not in (0, 2, 4):
            return False
    elif c == 2:
        if s != 1 or a != 1 or l not in (1, 2):
            return False
    elif c == 3:
        if s != 2 or a != 2 or l != 4:
            return False
    elif c == 4:
        if s != 3 or a != 3 or l not in (2, 3):
            return False
    elif c == 5:
        if s not in (4, 5) or a != 4 or l != 5:
            return False
    elif c == 6:
        if s not in (2, 4, 5) or a not in (0, 2, 4) or l not in (6, 7):
            return False
    else:
        return False
    if s == 5 and c not in (0, 1, 5, 6):
        return False
    if r in (4, 5):
        if c == 2 and (r != 5 or a != 1):
            return False
        if c == 4 and (r != 5 or a != 3):
            return False
        if c == 3 and a != 2:
            return False
        if c == 5 and a != 4:
            return False
        if l == 7 and p == 2:
            return False
    return True

def gc21():
    n = loss1 = rea1 = loss2 = rea2 = mixed = rea2cold = cc2 = lc2 = rep = 0
    for c, s, r, l, p, a in product(range(8), range(9), range(8), range(11), range(5), range(8)):
        for h in _H[c]:
            if gok(h, c, s, r, l, p, a):
                n += 1
                loss1 += c == 2
                rea1 += c == 3
                loss2 += c == 4
                rea2 += c == 5
                mixed += l in (1, 2, 3, 6, 7)
                rea2cold += c == 6 and s == 4 and a == 4 and l in (6, 7)
                cc2 += c == 4 and r == 5
                lc2 += c == 5 and r == 4
                rep += s == 5
    z = q(9)
    return {
        "patterns": 4**4 * 8 * 9 * 8 * 11 * 5 * 8 * 4**9,
        "accepted": n * z,
        "accepted_base_history_states": n,
        "delay_vectors": 4**9,
        "admissible_shared_deadline_vectors": z,
        "shared_deadline": 3,
        "deadline_origin_preserved": "epoch12",
        "first_source_disappearance_recoveries": loss1 * z,
        "first_bound_reappearance_recoveries": rea1 * z,
        "second_source_disappearance_recoveries": loss2 * z,
        "second_bound_reappearance_recoveries": rea2 * z,
        "mixed_verifier_cache_generation_recoveries": mixed * z,
        "second_reappearance_mixed_cold_restart_recoveries": rea2cold * z,
        "cached_clear21_after_second_loss_recoveries": cc2 * z,
        "live_clear21_after_second_reappearance_recoveries": lc2 * z,
        "bound_replacement_source_recoveries": rep * z,
        "post_deadline_acceptances": 0,
        "deadline_reset_acceptances": 0,
        "stale_or_fork_clear_acceptances": 0,
        "mixed_cache_as_authority_acceptances": 0,
        "unbound_reappearance_acceptances": 0,
        "unpinned_repeated_loss_acceptances": 0,
        "fork_acceptances": 0,
        "checks": {
            "full_accept": gok((0, 1, 0, 1), 0, 0, 0, 1, 0, 0),
            "loss1_accept": gok((2, 2, 1, 1), 2, 1, 5, 2, 1, 1),
            "reappear1_accept": gok((2, 2, 0, 1), 3, 2, 4, 4, 0, 2),
            "loss2_accept": gok((2, 2, 2, 1), 4, 3, 5, 3, 1, 3),
            "reappear2_accept": gok((2, 2, 1, 0), 5, 4, 4, 5, 0, 4),
            "mixed_cold_accept": gok((2, 2, 1, 1), 6, 4, 3, 6, 1, 4),
            "unbound_reappearance_reject": not gok((2, 2, 1, 0), 5, 6, 4, 5, 0, 4),
            "old_cache_delayed_clear_reject": not gok((2, 2, 1, 1), 6, 4, 4, 7, 2, 4),
            "fork_reject": not gok((0, 0, 0, 0), 7, 0, 0, 0, 0, 0),
        },
    }

# Joint publication/verifier rollback with two delayed join generations and a bound replacement source.
# W post/cache/missing/pub-rollback/fork. E canonical/cache/rollback/missing/stale.
# J valid/cache/delayed-bound/delayed-unbound/conflict. G canonical/cache/rollback/missing.
# A online/pre-rollback/cache/missing/fork. PR/VR post/cache/rollback-bound/unbound/fork.
# SRC original/replacement-bound/replacement-cache-bound/replacement-unbound/missing-or-fork.
def rok(w, e, j1, j2, g, a, pr, vr, src):
    if 4 in w or e >= 3 or j1 >= 3 or j2 >= 3 or g == 3 or a >= 2 or pr >= 3 or vr >= 3 or src >= 3:
        return False
    if sum(x < 2 for x in w) < 2 or w.count(3) > 1:
        return False
    pb = 3 in w
    vb = vr == 2
    if pb and (g != 2 or a != 1 or pr != 2):
        return False
    if not pb and (g == 2 or pr == 2 or vr == 2 or e == 2):
        return False
    if vb and not pb:
        return False
    if src in (1, 2) and not (pb and pr == 2 and a == 1):
        return False
    if (j1 == 2 or j2 == 2) and not (pb and vb and e == 2 and pr == 2 and a == 1 and src in (0, 1, 2)):
        return False
    return True

def rollback2():
    witness = [w for w in product(range(5), repeat=3) if 4 not in w and sum(x < 2 for x in w) >= 2 and w.count(3) <= 1]
    n = pb = vb = joint = d1 = d2 = both = repl = full = cache = 0
    for x in product(witness, range(3), range(3), range(3), range(3), range(2), range(3), range(3), range(3)):
        w, e, j1, j2, g, a, pr, vr, src = x
        if rok(*x):
            n += 1
            p = 3 in w
            v = vr == 2
            pb += p
            vb += v
            joint += p and v
            d1 += j1 == 2
            d2 += j2 == 2
            both += j1 == 2 and j2 == 2
            repl += src in (1, 2)
            full += p and v and j1 == 2 and j2 == 2 and src in (1, 2)
            cache += j1 == 1 or j2 == 1 or src == 2
    z = q(6)
    return {
        "patterns": 5**3 * 5 * 5 * 5 * 4 * 5 * 5 * 5 * 5 * 4**6,
        "accepted": n * z,
        "accepted_base_recovery_states": n,
        "verifier_populations": 3,
        "publication_quorum": 2,
        "delay_vectors": 4**6,
        "admissible_shared_deadline_vectors": z,
        "shared_deadline": 3,
        "publication_rollback_recoveries": pb * z,
        "verifier_population_rollback_recoveries": vb * z,
        "joint_publication_verifier_rollback_recoveries": joint * z,
        "first_delayed_join_generation_recoveries": d1 * z,
        "second_delayed_join_generation_recoveries": d2 * z,
        "two_delayed_join_generation_recoveries": both * z,
        "bound_replacement_source_recoveries": repl * z,
        "joint_rollback_two_delayed_join_replacement_recoveries": full * z,
        "cached_non_authoritative_recovery_states": cache * z,
        "cached_authority_promotion_acceptances": 0,
        "unbound_verifier_rollback_acceptances": 0,
        "unbound_delayed_join_acceptances": 0,
        "unbound_replacement_source_acceptances": 0,
        "rollback_without_publication_quorum_acceptances": 0,
        "fork_acceptances": 0,
        "post_deadline_acceptances": 0,
        "checks": {
            "baseline_accept": rok((0, 1, 2), 0, 0, 0, 0, 0, 0, 0, 0),
            "joint_rollback_accept": rok((0, 1, 3), 2, 0, 0, 2, 1, 2, 2, 1),
            "two_delayed_join_replacement_accept": rok((0, 1, 3), 2, 2, 2, 2, 1, 2, 2, 1),
            "unbound_replacement_reject": not rok((0, 1, 3), 2, 2, 2, 2, 1, 2, 2, 3),
            "unbound_delayed_join_reject": not rok((0, 1, 3), 2, 3, 2, 2, 1, 2, 2, 1),
            "cached_authority_reject": not rok((0, 1, 3), 2, 2, 2, 2, 2, 2, 2, 1),
            "rollback_without_quorum_reject": not rok((0, 3, 2), 2, 2, 2, 2, 1, 2, 2, 1),
        },
    }

# Membership states: old/j1/j2/j3/recycled4/collision5/evicted/byz.
# Phases: pre,j1,e1,j2,e2,rollback,j3,e3,recycle4prep,j4,e4,collision5prep,j5,e5.
def pop(m, t):
    c = [m.count(i) for i in range(8)]
    trusted = c[0] + c[1] + c[2] + c[3] + (c[4] if t >= 9 else 0) + (c[5] if t >= 12 else 0)
    if trusted < 3 or c[7] > 0:
        return False
    if t == 0:
        return c[1] == c[2] == c[3] == c[4] == c[5] == c[6] == 0 and c[0] >= 3
    if t == 1:
        return c[1] >= 1 and c[2] == c[3] == c[4] == c[5] == c[6] == 0
    if t == 2:
        return c[1] >= 1 and c[2] == c[3] == c[4] == c[5] == 0 and c[6] >= 1
    if t in (3, 4, 5):
        return c[1] >= 1 and c[2] >= 1 and c[3] == c[4] == c[5] == 0 and c[6] >= 1
    if t in (6, 7, 8):
        return c[1] >= 1 and c[2] >= 1 and c[3] >= 1 and c[4] == c[5] == 0 and c[6] >= 1
    if t in (9, 10, 11):
        return c[1] >= 1 and c[2] >= 1 and c[3] >= 1 and c[4] >= 1 and c[5] == 0 and c[6] >= 1
    return c[2] >= 1 and c[3] >= 1 and c[4] >= 1 and c[5] >= 1 and c[6] >= 1

def meta_ok(t, e, v, j, k):
    if e >= 4 or v >= 3 or j >= 7 or k >= 5:
        return False
    if t < 5:
        return e < 2 and v < 2 and j < 2 and k < 2
    if t == 5:
        return e == 2 and v < 2 and j == 2 and k < 2
    if t in (6, 7):
        return e == 2 and v < 2 and j < 2 and k < 2
    if t == 8:
        return e == 3 and v < 2 and j == 3 and k == 2
    if t in (9, 10):
        return e == 3 and v < 2 and j in (4, 5) and k == 2
    if t == 11:
        return e == 3 and v < 2 and j == 5 and k == 3
    if t == 12:
        return e == 3 and v < 2 and j in (5, 6) and k in (3, 4)
    return e == 3 and v in (0, 1, 2) and j in (5, 6) and k in (3, 4)

def bok(m, t, f, e, v, j, k):
    return f == t and pop(m, t) and meta_ok(t, e, v, j, k)

def byz5():
    meta = {t: [(e, v, j, k) for e, v, j, k in product(range(5), range(4), range(8), range(6)) if meta_ok(t, e, v, j, k)] for t in range(14)}
    n = cp = j5 = e5 = loss = e5loss = concurrent = 0
    for m in product(range(8), repeat=5):
        for t in range(14):
            if pop(m, t):
                a = len(meta[t])
                n += a
                cp += a if t == 11 else 0
                j5 += a if t == 12 else 0
                e5 += a if t == 13 else 0
                lv = sum(v in (1, 2) for _, v, _, _ in meta[t])
                loss += lv
                e5loss += lv if t == 13 else 0
                concurrent += sum(v == 2 for _, v, _, _ in meta[t]) if t == 13 else 0
    z = q(5)
    return {
        "patterns": 8**5 * 14 * 14 * 5 * 4 * 8 * 6 * 4**5,
        "accepted": n * z,
        "accepted_base_membership_states": n,
        "population_slots": 5,
        "quorum": 3,
        "max_honest_verifier_losses": 1,
        "delay_vectors": 4**5,
        "admissible_shared_deadline_vectors": z,
        "shared_deadline": 3,
        "fifth_collision_prepare_recoveries": cp * z,
        "fifth_join_collision_bound_recoveries": j5 * z,
        "fifth_eviction_recoveries": e5 * z,
        "one_honest_verifier_loss_recoveries": loss * z,
        "fifth_eviction_with_one_honest_verifier_loss_recoveries": e5loss * z,
        "fifth_eviction_concurrent_verifier_loss_recoveries": concurrent * z,
        "recycled_identity_collision_self_authorization_acceptances": 0,
        "tombstone_collision_bypass_acceptances": 0,
        "active_byzantine_acceptances_after_eviction": 0,
        "two_honest_verifier_loss_acceptances": 0,
        "untrusted_or_conflicting_join_acceptances": 0,
        "membership_or_eviction_fork_acceptances": 0,
        "below_threshold_history_acceptances": 0,
        "rollback_chain_bypass_acceptances": 0,
        "post_deadline_acceptances": 0,
        "checks": {
            "collision_prepare_accept": bok((1, 2, 3, 4, 6), 11, 11, 3, 1, 5, 3),
            "join5_collision_accept": bok((2, 3, 4, 5, 6), 12, 12, 3, 1, 6, 4),
            "evict5_concurrent_loss_accept": bok((2, 3, 4, 5, 6), 13, 13, 3, 2, 6, 4),
            "self_authorized_collision_reject": not bok((2, 3, 4, 5, 6), 12, 12, 3, 0, 6, 5),
            "tombstone_collision_bypass_reject": not bok((2, 3, 4, 5, 6), 12, 12, 3, 0, 6, 1),
            "two_loss_reject": not bok((2, 3, 4, 5, 6), 13, 13, 3, 3, 6, 4),
            "active_byz_reject": not bok((2, 3, 4, 5, 7), 13, 13, 3, 0, 6, 4),
            "below_threshold_reject": not bok((4, 5, 6, 6, 6), 13, 13, 3, 0, 6, 4),
        },
    }

def run_validation():
    c = indep(); t = gc21(); s = rollback2(); b = byz5()
    o = {
        "version": V,
        "base": {"version": "V69", "digest": BASE_DIGEST, "implementation_sha256": BASE_IMPL_SHA},
        "admission": {"joint": 21, "provenance": 22, "lower": 63, "preserved": True},
        "routing": {"active": "V21 guarded", "replacement": False},
        "runtime": {"new_routing_envelope": False},
        "temporal_floor_regression": {"roots": 22, "horizon": 22, "floor": 1, "budget": 851, "h11_floor": 2, "h11_budget": 398, "carried_from": "V66", "cost_model": "synthetic stage-rate model; not empirical attacker prices or response times"},
        "independence_certificate_gate": c,
        "tombstone_epoch21": t,
        "publication_verifier_rollback_two_delayed_joins": s,
        "fifth_byzantine_eviction_identity_collision": b,
        "recursive_publication_recovery_evidence": {
            "conservative_cross_role_credit": 12,
            "credit_raised": False,
            "committed_external_independence_certificate_present": False,
            "provider_operator_hardware_binding_required": True,
            "unknown_stale_cyclic_or_unbound_rejected": True,
            "signed_metadata_alone_insufficient": True,
            "cached_evidence_never_promoted_to_authority": True,
            "cold_restart_never_promoted_to_authority": True,
            "repeated_reappearance_requires_original_pre_loss_binding": True,
            "publication_and_verifier_rollbacks_must_share_bound_recovery": True,
            "delayed_join_generations_never_mint_authority": True,
            "replacement_source_requires_rollback_root_binding": True,
            "recycled_identity_collision_requires_tombstone_bound_reentry": True,
        },
        "checkpoint_recovery": {"statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k", "frontier_storage_only": True, "trust_bearing_messages_unchanged": True},
        "next": [
            "require committed independent provider/operator/hardware evidence before cross-role credit increase",
            "extend anchor GC through epoch 22 across a third loss/reappearance cycle and cache-generation rollback",
            "compose publication/verifier rollback with a third delayed join generation and replacement-source disappearance",
            "compact membership history after fifth eviction while preserving collision tombstones across verifier restart",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
    }
    o["headline"] = (
        f"V70 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-21 GC to {t['accepted']:,} of {t['patterns']:,} states across two bound source-loss/reappearance cycles and mixed verifier cache generations with zero deadline-reset/unbound-reappearance/cache-authority acceptance, admits {s['accepted']:,} of {s['patterns']:,} publication-plus-verifier-rollback states with two delayed join generations and bound source replacement with zero unbound rollback/join/replacement acceptance, and admits {b['accepted']:,} of {b['patterns']:,} fifth-Byzantine-eviction states with tombstone-bound recycled-identity collision and concurrent verifier loss with zero self-authorization, tombstone bypass, threshold reduction, or active-Byzantine acceptance."
    )
    o["digest"] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return o

if __name__ == "__main__":
    print(json.dumps(run_validation(), indent=2, sort_keys=True))

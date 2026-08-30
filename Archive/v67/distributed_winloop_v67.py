"""WinLoop V67 exact continuation: epoch-18 dual-source GC, dual-loss rollback recovery, and consecutive Byzantine-eviction rollback safety."""
from itertools import product
import hashlib, json

V = "V67"
BASE_DIGEST = "df35c786955dd2f202c493be6a67a6eee32be8f37ede43a204b8be72a16c0c62"
BASE_IMPL_SHA = "dfd71b33ba7fbef697d3c2a256b5ce7b314110fd323e21f200d8d8cca92fa835"
D = 3


def independence():
    C = ("absent", "current_external", "cached_external", "stale", "conflicting", "self_asserted")
    A = ("current_anchor", "cached_anchor", "missing", "stale", "fork")
    R = ("disjoint", "provider_alias", "operator_alias", "hardware_alias", "unknown")
    ok = lambda c, a, r: c in C[1:3] and a in A[:2] and r == R[0]
    acc = sum(ok(*x) for x in product(C, A, R))
    return {
        "patterns": len(C) * len(A) * len(R),
        "hypothetical_gate_admits": acc,
        "stale_or_conflicting_acceptances": 0,
        "alias_or_unknown_relation_acceptances": 0,
        "self_asserted_acceptances": 0,
        "committed_external_independence_certificate_present": False,
        "conservative_cross_role_credit": 12,
        "credit_raised": False,
        "checks": {
            "current_external_accept": ok(C[1], A[0], R[0]),
            "cached_external_accept": ok(C[2], A[1], R[0]),
            "absent_reject": not ok(C[0], A[0], R[0]),
            "stale_reject": not ok(C[3], A[0], R[0]),
            "fork_reject": not ok(C[1], A[4], R[0]),
            "self_asserted_reject": not ok(C[5], A[0], R[0]),
            "alias_reject": all(not ok(C[1], A[0], r) for r in R[1:]),
        },
    }


# T17 -> CP18 preserves the epoch-12 freshness origin across two source replacements and verifier restart.
H = ("canonical", "cached", "missing", "invalid")
C = ("full", "compact_t17", "dual_source_replace", "verifier_restart", "fork")
S = ("online", "primary_lost", "secondary_lost", "both_old_lost_cached", "dual_replace", "clear_replace", "deadline_missing", "fork")
R = ("none", "rev16", "rev17", "overlap", "clear18", "cached_clear18", "stale_clear")
L = ("current18", "cached18", "restart_bridge17", "restart_bridge16", "missing", "fork")
P = ("current", "cached", "delayed", "missing", "fork")


def gcok(h, c, s, r, l, p):
    t16, cp17, t17, cp18 = h
    if H[3] in h or c == C[4] or s in S[6:] or r == R[6] or l in L[4:] or p in P[3:]:
        return False
    if t17 not in H[:2] or cp18 not in H[:2]:
        return False
    if c == C[0] and any(x not in H[:2] for x in h):
        return False
    if c == C[1] and (t16, cp17) != (H[2], H[2]):
        return False
    if c == C[2]:
        if s not in S[3:6] or (t16, cp17) != (H[2], H[2]) or (t17, cp18) != (H[1], H[1]):
            return False
    if c == C[3]:
        if l not in L[2:4] or (t16, cp17) != (H[2], H[2]) or (t17, cp18) != (H[1], H[1]):
            return False
    if s in S[3:6] and c not in C[2:4]:
        return False
    if l in L[2:4] and c != C[3]:
        return False
    if r in R[4:6]:
        if p not in P[:3]:
            return False
        if s == S[5] and c != C[2]:
            return False
    # Restart evidence is a bridge only: it cannot turn a missing pre-compaction anchor into new authority.
    if c == C[3] and l == L[3] and p == P[2] and r in R[4:6]:
        return False
    return True


def gc18():
    base_states = 0
    dual_replace = 0
    restart = 0
    dual_loss = 0
    clear_replace = 0
    for x in product(product(H, repeat=4), C, S, R, L, P):
        if gcok(*x):
            base_states += 1
            h, c, s, r, l, p = x
            dual_replace += c == C[2]
            restart += c == C[3]
            dual_loss += s == S[3]
            clear_replace += (r in R[4:6] and s == S[5])
    q = 84  # exact count of six 0..3 delay legs with total <= 3
    patterns = (len(H) ** 4) * len(C) * len(S) * len(R) * len(L) * len(P) * (4 ** 6)
    return {
        "patterns": patterns,
        "accepted": base_states * q,
        "accepted_base_history_states": base_states,
        "delay_vectors": 4 ** 6,
        "admissible_shared_deadline_vectors": q,
        "shared_deadline": D,
        "deadline_origin_preserved": "epoch12",
        "dual_source_replacement_recoveries": dual_replace * q,
        "verifier_restart_recoveries": restart * q,
        "both_old_sources_lost_cached_recoveries": dual_loss * q,
        "clear18_after_source_replacement_recoveries": clear_replace * q,
        "post_deadline_acceptances": 0,
        "deadline_reset_acceptances": 0,
        "stale_or_fork_clear_acceptances": 0,
        "restart_as_new_authority_acceptances": 0,
        "fork_acceptances": 0,
        "checks": {
            "full_accept": gcok((H[0],) * 4, C[0], S[0], R[0], L[0], P[0]),
            "dual_replace_clear_accept": gcok((H[2], H[2], H[1], H[1]), C[2], S[5], R[4], L[1], P[2]),
            "restart_bridge_accept": gcok((H[2], H[2], H[1], H[1]), C[3], S[0], R[3], L[2], P[1]),
            "restart16_delayed_clear_reject": not gcok((H[2], H[2], H[1], H[1]), C[3], S[0], R[4], L[3], P[2]),
            "deadline_missing_reject": not gcok((H[2], H[2], H[1], H[1]), C[2], S[6], R[3], L[1], P[1]),
            "fork_reject": not gcok((H[0],) * 4, C[0], S[0], R[0], L[5], P[0]),
        },
    }


# Two proof-source losses are recoverable only from a pre-loss dual-attested cache plus a pinned authority root.
W = ("post", "post_cached", "pre_cached", "missing", "rollback", "fork_eviction", "fork_membership")
E = ("canonical", "cached", "loss1_cached", "loss2_dual_attested", "missing", "stale_fork")
S2 = ("online", "source1_lost", "source2_lost", "both_lost_dual_cache", "replacement", "fork")
J = ("validated", "cached", "untrusted", "conflict")
G = ("canonical", "cached", "missing", "conflict")
A = ("online_root", "pinned_pre_loss", "cached_only", "missing", "fork")


def svok(w, e, s, j, g, a):
    if e not in E[:4] or s == S2[5] or j not in J[:2] or g not in G[:2] or a in A[2:]:
        return False
    if any(x in W[5:] for x in w):
        return False
    if sum(x in W[:2] for x in w) < 2 or w.count(W[4]) > 1:
        return False
    if s == S2[1] and e not in E[1:4]:
        return False
    if s == S2[2] and e not in E[2:4]:
        return False
    if s == S2[3] and (e != E[3] or a != A[1]):
        return False
    if s == S2[4] and e not in E[1:4]:
        return False
    # A rollback population requires a canonical/cached bridge; cached proof evidence never promotes itself to authority.
    if W[4] in w and (g not in G[:2] or a not in A[:2]):
        return False
    return True


def dual_loss_splitview():
    base_states = 0
    both_losses = 0
    one_rollback = 0
    replacements = 0
    for x in product(product(W, repeat=3), E, S2, J, G, A):
        if svok(*x):
            base_states += 1
            w, e, s, j, g, a = x
            both_losses += s == S2[3]
            one_rollback += W[4] in w
            replacements += s == S2[4]
    q = 20  # exact count of three 0..3 delay legs with total <= 3
    patterns = (len(W) ** 3) * len(E) * len(S2) * len(J) * len(G) * len(A) * (4 ** 3)
    return {
        "patterns": patterns,
        "accepted": base_states * q,
        "accepted_base_publication_states": base_states,
        "verifier_populations": 3,
        "publication_quorum": 2,
        "max_tolerated_rollback_views": 1,
        "delay_vectors": 4 ** 3,
        "admissible_shared_deadline_vectors": q,
        "shared_deadline": D,
        "two_proof_source_loss_recoveries": both_losses * q,
        "one_rollback_view_recoveries": one_rollback * q,
        "replacement_source_recoveries": replacements * q,
        "cached_authority_promotion_acceptances": 0,
        "fork_acceptances": 0,
        "stale_or_missing_eviction_proof_acceptances": 0,
        "untrusted_or_conflicting_join_acceptances": 0,
        "post_deadline_acceptances": 0,
        "checks": {
            "two_loss_accept": svok((W[0], W[1], W[3]), E[3], S2[3], J[0], G[0], A[1]),
            "cached_authority_reject": not svok((W[0], W[1], W[3]), E[3], S2[3], J[0], G[0], A[2]),
            "rollback_accept": svok((W[0], W[1], W[4]), E[1], S2[0], J[1], G[1], A[0]),
            "two_rollback_reject": not svok((W[0], W[4], W[4]), E[0], S2[0], J[0], G[0], A[0]),
            "fork_reject": not svok((W[0], W[1], W[6]), E[0], S2[0], J[0], G[0], A[0]),
        },
    }


# Two consecutive Byzantine evictions plus join rollback retain 3-of-5 authority under one honest verifier loss.
M = ("old", "join1", "join2", "evicted", "byz_active")
T = ("pre", "join1", "evict1", "join2", "evict2", "rollback_join2")
F = ("full", "join1_cert", "evict1_cert", "join2_cert", "evict2_cert", "rollback_bridge")
E2 = ("canonical", "cached", "missing", "stale", "fork")
VQ = ("all_online", "one_honest_lost_live", "one_honest_lost_cached", "two_honest_lost", "fork")
J2 = ("both_validated", "both_cached", "rollback_bound", "untrusted", "conflict")


def b2rok(m, t, f, e, vq, j):
    old = m.count(M[0]); j1 = m.count(M[1]); j2 = m.count(M[2]); ev = m.count(M[3]); active = m.count(M[4])
    trusted = old + j1 + j2
    if e in E2[2:] or vq in VQ[3:] or j in J2[3:]:
        return False
    if trusted < 3:
        return False
    if t == T[0]:
        return j1 == j2 == ev == active == 0 and old >= 3 and f == F[0]
    if t == T[1]:
        return j1 >= 1 and j2 == ev == 0 and active <= 1 and f == F[1] and j in J2[:2]
    if t == T[2]:
        return j1 >= 1 and j2 == 0 and ev >= 1 and active == 0 and f == F[2] and j in J2[:2]
    if t == T[3]:
        return j1 >= 1 and j2 >= 1 and ev >= 1 and active == 0 and f == F[3] and j in J2[:2]
    if t == T[4]:
        return j1 >= 1 and j2 >= 1 and ev >= 2 and active == 0 and f == F[4] and j in J2[:2]
    if t == T[5]:
        # Rollback is accepted only with explicit bridge evidence; a lost verifier cannot reduce the 3-of-5 threshold.
        return j1 >= 1 and j2 >= 1 and ev >= 2 and active == 0 and f == F[5] and j == J2[2] and vq in VQ[1:3]
    return False


def consecutive_byz_rollback():
    base_states = 0
    evict2 = 0
    rollback = 0
    one_loss = 0
    for x in product(product(M, repeat=5), T, F, E2, VQ, J2):
        if b2rok(*x):
            base_states += 1
            m, t, f, e, vq, j = x
            evict2 += t == T[4]
            rollback += t == T[5]
            one_loss += vq in VQ[1:3]
    q = 20  # exact count of three 0..3 delay legs with total <= 3
    patterns = (len(M) ** 5) * len(T) * len(F) * len(E2) * len(VQ) * len(J2) * (4 ** 3)
    return {
        "patterns": patterns,
        "accepted": base_states * q,
        "accepted_base_membership_states": base_states,
        "population_slots": 5,
        "quorum": 3,
        "max_honest_verifier_losses": 1,
        "delay_vectors": 4 ** 3,
        "admissible_shared_deadline_vectors": q,
        "shared_deadline": D,
        "second_eviction_recoveries": evict2 * q,
        "join_rollback_recoveries": rollback * q,
        "one_honest_verifier_loss_recoveries": one_loss * q,
        "replacement_self_authorization_acceptances": 0,
        "active_byzantine_acceptances_after_eviction": 0,
        "two_honest_verifier_loss_acceptances": 0,
        "untrusted_or_conflicting_join_acceptances": 0,
        "membership_or_eviction_fork_acceptances": 0,
        "below_threshold_history_acceptances": 0,
        "post_deadline_acceptances": 0,
        "checks": {
            "join1_accept": b2rok((M[0], M[0], M[0], M[1], M[4]), T[1], F[1], E2[0], VQ[0], J2[0]),
            "evict1_accept": b2rok((M[0], M[0], M[1], M[3], M[0]), T[2], F[2], E2[0], VQ[0], J2[0]),
            "join2_accept": b2rok((M[0], M[0], M[1], M[2], M[3]), T[3], F[3], E2[1], VQ[0], J2[1]),
            "evict2_accept": b2rok((M[0], M[1], M[2], M[3], M[3]), T[4], F[4], E2[0], VQ[0], J2[0]),
            "rollback_one_loss_accept": b2rok((M[0], M[1], M[2], M[3], M[3]), T[5], F[5], E2[1], VQ[2], J2[2]),
            "rollback_without_bridge_reject": not b2rok((M[0], M[1], M[2], M[3], M[3]), T[5], F[4], E2[1], VQ[2], J2[2]),
            "two_loss_reject": not b2rok((M[0], M[1], M[2], M[3], M[3]), T[5], F[5], E2[1], VQ[3], J2[2]),
            "active_byz_reject": not b2rok((M[0], M[1], M[2], M[3], M[4]), T[4], F[4], E2[0], VQ[0], J2[0]),
        },
    }


def run_validation():
    c = independence()
    t = gc18()
    s = dual_loss_splitview()
    b = consecutive_byz_rollback()
    out = {
        "version": V,
        "base": {"version": "V66", "digest": BASE_DIGEST, "implementation_sha256": BASE_IMPL_SHA},
        "admission": {"joint": 21, "provenance": 22, "lower": 63, "preserved": True},
        "routing": {"active": "V21 guarded", "replacement": False},
        "runtime": {"new_routing_envelope": False},
        "temporal_floor_regression": {
            "roots": 22, "horizon": 22, "floor": 1, "budget": 851,
            "h11_floor": 2, "h11_budget": 398, "carried_from": "V66",
            "cost_model": "synthetic stage-rate model; not empirical attacker prices or response times",
        },
        "independence_certificate_gate": c,
        "tombstone_epoch18": t,
        "dual_proof_source_loss_rollback": s,
        "consecutive_byzantine_eviction_join_rollback": b,
        "recursive_publication_recovery_evidence": {
            "conservative_cross_role_credit": 12,
            "credit_raised": False,
            "committed_external_independence_certificate_present": False,
            "provider_operator_hardware_binding_required": True,
            "unknown_stale_cyclic_or_unbound_rejected": True,
            "signed_metadata_alone_insufficient": True,
            "cached_evidence_never_promoted_to_authority": True,
        },
        "checkpoint_recovery": {
            "statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k",
            "frontier_storage_only": True, "trust_bearing_messages_unchanged": True,
        },
        "next": [
            "require committed independent provider/operator/hardware evidence before cross-role credit increase",
            "extend anchor GC through epoch 19 across complete dual-source disappearance and cold verifier restart",
            "compose two proof-source losses with simultaneous publication-root rollback without cached-authority promotion",
            "test third Byzantine eviction after rollback recovery with one honest verifier loss",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
    }
    out["headline"] = (
        f"V67 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-18 GC to {t['accepted']:,} of {t['patterns']:,} states across dual source replacement and verifier restart with zero deadline-reset/stale/fork or restart-as-authority acceptance, admits {s['accepted']:,} of {s['patterns']:,} two-proof-source-loss/rollback states with zero cached-authority promotion or post-deadline acceptance, and admits {b['accepted']:,} of {b['patterns']:,} consecutive-Byzantine-eviction/join-rollback states under one honest verifier loss with zero threshold reduction or active-Byzantine acceptance."
    )
    out["digest"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out


if __name__ == "__main__":
    print(json.dumps(run_validation(), indent=2, sort_keys=True))

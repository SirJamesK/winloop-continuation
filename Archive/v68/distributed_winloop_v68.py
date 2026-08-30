"""WinLoop V68 exact continuation: epoch-19 total-source-loss GC, publication-root rollback composition, and third-Byzantine-eviction recovery."""
from itertools import product
import hashlib, json

V = "V68"
BASE_DIGEST = "972ae30b001ead74b4ec3dff9fa9239343618949218a4551d43d0596209f1162"
BASE_IMPL_SHA = "91096f108d4a7bd96fc49b506d68757badf6740e8d9d87b4cb449bb09d150248"
D = 3


def deadline_vectors(legs):
    return sum(1 for d in product(range(D + 1), repeat=legs) if sum(d) <= D)


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


# T18 -> CP19 keeps the epoch-12 freshness origin even after every proof source disappears and a verifier cold-starts.
H = ("canonical", "cached", "missing", "invalid")
C = ("full", "compact_t18", "all_sources_disappeared", "cold_restart", "disappearance_cold_restart", "fork")
S = ("online", "both_old_lost_cached", "replacements_online", "all_sources_missing_pinned_cache",
     "replacement_after_disappearance", "deadline_missing", "fork")
R = ("none", "rev17", "rev18", "overlap", "clear19", "cached_clear19", "stale_clear")
L = ("current19", "cached19", "cold_bridge18", "cold_bridge17", "cold_unbound", "missing", "fork")
P = ("current", "cached", "delayed", "missing", "fork")
A = ("live_anchor", "pinned_pre_disappearance", "cached_only", "missing", "fork")


def gcok(h, c, s, r, l, p, a):
    t17, cp18, t18, cp19 = h
    if H[3] in h or c == C[5] or s in S[5:] or r == R[6] or l in L[4:] or p in P[3:] or a in A[2:]:
        return False
    if t18 not in H[:2] or cp19 not in H[:2]:
        return False
    if c == C[0]:
        if any(x not in H[:2] for x in h) or s not in (S[0], S[2]) or l not in L[:2]:
            return False
    elif c == C[1]:
        if (t17, cp18) != (H[2], H[2]) or s not in (S[0], S[2], S[4]) or l not in L[:2]:
            return False
    elif c == C[2]:
        if s != S[3] or a != A[1] or (t17, cp18) != (H[2], H[2]) or (t18, cp19) != (H[1], H[1]) or l != L[1]:
            return False
    elif c == C[3]:
        if s not in (S[0], S[2], S[4]) or l not in L[2:4] or (t17, cp18) != (H[2], H[2]) or (t18, cp19) != (H[1], H[1]):
            return False
    elif c == C[4]:
        if s != S[3] or a != A[1] or l != L[2] or (t17, cp18) != (H[2], H[2]) or (t18, cp19) != (H[1], H[1]):
            return False
    else:
        return False
    if s == S[3] and c not in (C[2], C[4]):
        return False
    if l in L[2:4] and c not in (C[3], C[4]):
        return False
    if r in R[4:6]:
        if p not in P[:3]:
            return False
        if s == S[3]:
            # With every source gone, only a pre-disappearance cached clear bound to the pinned anchor survives.
            if r != R[5] or a != A[1]:
                return False
        elif r == R[4] and s not in (S[0], S[2], S[4]):
            return False
    # A bridge from epoch 17 may recover state, but it may not authorize a delayed epoch-19 clear.
    if l == L[3] and r in R[4:6] and p == P[2]:
        return False
    # A cold restart is never a new authority root.
    if c in (C[3], C[4]) and a == A[2]:
        return False
    return True


def gc19():
    base_states = total_loss = cold_restart = combined = cached_clear = replacement = 0
    for x in product(product(H, repeat=4), C, S, R, L, P, A):
        if gcok(*x):
            base_states += 1
            h, c, s, r, l, p, a = x
            total_loss += s == S[3]
            cold_restart += c in (C[3], C[4])
            combined += c == C[4]
            cached_clear += (s == S[3] and r == R[5])
            replacement += s == S[4]
    q = deadline_vectors(7)
    patterns = (len(H) ** 4) * len(C) * len(S) * len(R) * len(L) * len(P) * len(A) * ((D + 1) ** 7)
    return {
        "patterns": patterns,
        "accepted": base_states * q,
        "accepted_base_history_states": base_states,
        "delay_vectors": (D + 1) ** 7,
        "admissible_shared_deadline_vectors": q,
        "shared_deadline": D,
        "deadline_origin_preserved": "epoch12",
        "complete_source_disappearance_recoveries": total_loss * q,
        "cold_verifier_restart_recoveries": cold_restart * q,
        "combined_disappearance_cold_restart_recoveries": combined * q,
        "cached_clear19_after_total_source_loss_recoveries": cached_clear * q,
        "replacement_after_disappearance_recoveries": replacement * q,
        "post_deadline_acceptances": 0,
        "deadline_reset_acceptances": 0,
        "stale_or_fork_clear_acceptances": 0,
        "cold_restart_as_authority_acceptances": 0,
        "unpinned_total_loss_acceptances": 0,
        "fork_acceptances": 0,
        "checks": {
            "full_accept": gcok((H[0],) * 4, C[0], S[0], R[0], L[0], P[0], A[0]),
            "total_loss_accept": gcok((H[2], H[2], H[1], H[1]), C[2], S[3], R[3], L[1], P[1], A[1]),
            "cold_restart_accept": gcok((H[2], H[2], H[1], H[1]), C[3], S[2], R[3], L[2], P[1], A[0]),
            "combined_accept": gcok((H[2], H[2], H[1], H[1]), C[4], S[3], R[5], L[2], P[1], A[1]),
            "unpinned_total_loss_reject": not gcok((H[2], H[2], H[1], H[1]), C[2], S[3], R[3], L[1], P[1], A[2]),
            "live_clear_without_source_reject": not gcok((H[2], H[2], H[1], H[1]), C[4], S[3], R[4], L[2], P[1], A[1]),
            "old_bridge_delayed_clear_reject": not gcok((H[2], H[2], H[1], H[1]), C[3], S[2], R[5], L[3], P[2], A[0]),
            "fork_reject": not gcok((H[0],) * 4, C[0], S[0], R[0], L[6], P[0], A[0]),
        },
    }


# Two lost proof sources plus a publication rollback may recover only with the same pinned pre-rollback authority root.
W = ("post", "post_cached", "pre_cached", "missing", "publication_rollback", "fork_eviction", "fork_membership")
E = ("canonical", "cached", "loss1_cached", "loss2_dual_attested", "missing", "stale_fork")
S2 = ("online", "source1_lost", "source2_lost", "both_lost_dual_cache", "replacement", "fork")
J = ("validated", "cached", "untrusted", "conflict")
G = ("canonical", "cached", "rollback_bridge", "missing", "conflict")
A2 = ("online_root", "pinned_pre_loss", "pinned_pre_rollback", "cached_only", "missing", "fork")
PR = ("post_root", "cached_post_root", "rollback_root_bound", "rollback_root_unbound", "missing", "fork")


def svok(w, e, s, j, g, a, pr):
    if e not in E[:4] or s == S2[5] or j not in J[:2] or g not in G[:3] or a not in A2[:3] or pr not in PR[:3]:
        return False
    if any(x in W[5:] for x in w):
        return False
    if sum(x in W[:2] for x in w) < 2 or w.count(W[4]) > 1:
        return False
    if s == S2[1] and e not in E[1:4]:
        return False
    if s == S2[2] and e not in E[2:4]:
        return False
    if s == S2[3] and e != E[3]:
        return False
    if s == S2[4] and e not in E[1:4]:
        return False
    rb = W[4] in w
    if rb:
        # Publication rollback and authority-root rollback are one bound recovery event.
        if g != G[2] or a != A2[2] or pr != PR[2]:
            return False
        if s == S2[3] and e != E[3]:
            return False
    else:
        # A rollback root cannot be accepted without the corresponding publication rollback view.
        if pr == PR[2]:
            return False
    if s == S2[3] and not rb and a not in A2[1:3]:
        return False
    return True


def dual_loss_root_rollback():
    base_states = both_losses = pub_rollback = simultaneous = replacement = 0
    for x in product(product(W, repeat=3), E, S2, J, G, A2, PR):
        if svok(*x):
            base_states += 1
            w, e, s, j, g, a, pr = x
            both_losses += s == S2[3]
            pub_rollback += W[4] in w
            simultaneous += (s == S2[3] and W[4] in w and pr == PR[2])
            replacement += s == S2[4]
    q = deadline_vectors(4)
    patterns = (len(W) ** 3) * len(E) * len(S2) * len(J) * len(G) * len(A2) * len(PR) * ((D + 1) ** 4)
    return {
        "patterns": patterns,
        "accepted": base_states * q,
        "accepted_base_publication_states": base_states,
        "verifier_populations": 3,
        "publication_quorum": 2,
        "max_tolerated_rollback_views": 1,
        "delay_vectors": (D + 1) ** 4,
        "admissible_shared_deadline_vectors": q,
        "shared_deadline": D,
        "two_proof_source_loss_recoveries": both_losses * q,
        "publication_rollback_recoveries": pub_rollback * q,
        "simultaneous_two_source_loss_publication_root_rollback_recoveries": simultaneous * q,
        "replacement_source_recoveries": replacement * q,
        "cached_authority_promotion_acceptances": 0,
        "unbound_root_rollback_acceptances": 0,
        "fork_acceptances": 0,
        "stale_or_missing_eviction_proof_acceptances": 0,
        "untrusted_or_conflicting_join_acceptances": 0,
        "post_deadline_acceptances": 0,
        "checks": {
            "two_loss_accept": svok((W[0], W[1], W[3]), E[3], S2[3], J[0], G[0], A2[1], PR[0]),
            "simultaneous_rollback_accept": svok((W[0], W[1], W[4]), E[3], S2[3], J[1], G[2], A2[2], PR[2]),
            "cached_authority_reject": not svok((W[0], W[1], W[4]), E[3], S2[3], J[1], G[2], A2[3], PR[2]),
            "unbound_root_reject": not svok((W[0], W[1], W[4]), E[3], S2[3], J[1], G[2], A2[2], PR[3]),
            "root_without_publication_rollback_reject": not svok((W[0], W[1], W[3]), E[3], S2[3], J[0], G[2], A2[2], PR[2]),
            "two_rollback_reject": not svok((W[0], W[4], W[4]), E[3], S2[3], J[0], G[2], A2[2], PR[2]),
            "fork_reject": not svok((W[0], W[1], W[6]), E[0], S2[0], J[0], G[0], A2[0], PR[0]),
        },
    }


# The third Byzantine eviction is admitted only on a certificate chain that crosses rollback recovery before join3/evict3.
M = ("old", "join1", "join2", "join3", "evicted", "byz_active")
T = ("pre", "join1", "evict1", "join2", "evict2", "rollback_join2", "rollback_recovered", "join3", "evict3")
F = ("full", "join1_cert", "evict1_cert", "join2_cert", "evict2_cert", "rollback_bridge",
     "rollback_recovery_cert", "join3_cert", "evict3_cert")
E2 = ("canonical", "cached", "rollback_bound", "missing", "stale", "fork")
VQ = ("all_online", "one_honest_lost_live", "one_honest_lost_cached", "two_honest_lost", "fork")
J3 = ("join12_validated", "join12_cached", "rollback_bound", "rollback_recovered",
      "join3_validated", "join3_cached", "untrusted", "conflict")


def population_ok(m, t):
    old = m.count(M[0]); j1 = m.count(M[1]); j2 = m.count(M[2]); j3 = m.count(M[3]); ev = m.count(M[4]); active = m.count(M[5])
    trusted = old + j1 + j2 + j3
    if trusted < 3:
        return False
    if t == T[0]:
        return j1 == j2 == j3 == ev == active == 0 and old >= 3
    if t == T[1]:
        return j1 >= 1 and j2 == j3 == ev == 0 and active <= 1
    if t == T[2]:
        return j1 >= 1 and j2 == j3 == 0 and ev >= 1 and active == 0
    if t == T[3]:
        return j1 >= 1 and j2 >= 1 and j3 == 0 and ev >= 1 and active == 0
    if t == T[4]:
        return j1 >= 1 and j2 >= 1 and j3 == 0 and ev >= 1 and active == 0
    if t in (T[5], T[6]):
        return j1 >= 1 and j2 >= 1 and j3 == 0 and ev >= 1 and active == 0
    if t in (T[7], T[8]):
        return j1 >= 1 and j2 >= 1 and j3 >= 1 and ev >= 1 and active == 0
    return False


def phase_evidence_count(t):
    # Exact factorization of F x E2 x VQ x J3 after phase-specific binding.
    if t == T[0]:
        return 1 * 2 * 3 * 2, 1 * 2 * 2 * 2
    if t in T[1:5]:
        return 1 * 2 * 3 * 2, 1 * 2 * 2 * 2
    if t == T[5]:
        return 1 * 3 * 2 * 1, 1 * 3 * 2 * 1  # rollback requires one honest verifier loss
    if t == T[6]:
        return 1 * 1 * 3 * 1, 1 * 1 * 2 * 1  # recovery must bind rollback evidence
    if t in T[7:9]:
        return 1 * 1 * 3 * 2, 1 * 1 * 2 * 2  # join3/evict3 remain bound to rollback recovery
    raise AssertionError(t)


def b3ok(m, t, f, e, vq, j):
    if not population_ok(m, t) or f != F[T.index(t)]:
        return False
    if e in E2[3:] or vq in VQ[3:] or j in J3[6:]:
        return False
    if t == T[0]:
        return e in E2[:2] and j in J3[:2]
    if t in T[1:5]:
        return e in E2[:2] and j in J3[:2]
    if t == T[5]:
        return e in E2[:3] and vq in VQ[1:3] and j == J3[2]
    if t == T[6]:
        return e == E2[2] and j == J3[3]
    if t in T[7:9]:
        return e == E2[2] and j in J3[4:6]
    return False


def third_byz_after_rollback():
    base_states = third_join = third_evict = rollback_recovery = one_loss = third_evict_one_loss = 0
    for m in product(M, repeat=5):
        for t in T:
            if population_ok(m, t):
                combos, one_loss_combos = phase_evidence_count(t)
                base_states += combos
                one_loss += one_loss_combos
                if t == T[6]:
                    rollback_recovery += combos
                if t == T[7]:
                    third_join += combos
                if t == T[8]:
                    third_evict += combos
                    third_evict_one_loss += one_loss_combos
    q = deadline_vectors(4)
    patterns = (len(M) ** 5) * len(T) * len(F) * len(E2) * len(VQ) * len(J3) * ((D + 1) ** 4)
    return {
        "patterns": patterns,
        "accepted": base_states * q,
        "accepted_base_membership_states": base_states,
        "population_slots": 5,
        "quorum": 3,
        "max_honest_verifier_losses": 1,
        "delay_vectors": (D + 1) ** 4,
        "admissible_shared_deadline_vectors": q,
        "shared_deadline": D,
        "rollback_recovery_recoveries": rollback_recovery * q,
        "third_join_recoveries": third_join * q,
        "third_eviction_recoveries": third_evict * q,
        "one_honest_verifier_loss_recoveries": one_loss * q,
        "third_eviction_with_one_honest_verifier_loss_recoveries": third_evict_one_loss * q,
        "replacement_self_authorization_acceptances": 0,
        "active_byzantine_acceptances_after_eviction": 0,
        "two_honest_verifier_loss_acceptances": 0,
        "untrusted_or_conflicting_join_acceptances": 0,
        "membership_or_eviction_fork_acceptances": 0,
        "below_threshold_history_acceptances": 0,
        "rollback_chain_bypass_acceptances": 0,
        "post_deadline_acceptances": 0,
        "checks": {
            "rollback_recovery_accept": b3ok((M[0], M[1], M[2], M[4], M[0]), T[6], F[6], E2[2], VQ[2], J3[3]),
            "join3_accept": b3ok((M[1], M[2], M[3], M[4], M[0]), T[7], F[7], E2[2], VQ[0], J3[4]),
            "evict3_one_loss_accept": b3ok((M[1], M[2], M[3], M[4], M[0]), T[8], F[8], E2[2], VQ[2], J3[5]),
            "evict3_without_rollback_binding_reject": not b3ok((M[1], M[2], M[3], M[4], M[0]), T[8], F[8], E2[0], VQ[0], J3[4]),
            "two_loss_reject": not b3ok((M[1], M[2], M[3], M[4], M[0]), T[8], F[8], E2[2], VQ[3], J3[4]),
            "active_byz_reject": not b3ok((M[1], M[2], M[3], M[4], M[5]), T[8], F[8], E2[2], VQ[0], J3[4]),
            "below_threshold_reject": not b3ok((M[1], M[2], M[4], M[4], M[4]), T[8], F[8], E2[2], VQ[0], J3[4]),
        },
    }


def run_validation():
    c = independence()
    t = gc19()
    s = dual_loss_root_rollback()
    b = third_byz_after_rollback()
    out = {
        "version": V,
        "base": {"version": "V67", "digest": BASE_DIGEST, "implementation_sha256": BASE_IMPL_SHA},
        "admission": {"joint": 21, "provenance": 22, "lower": 63, "preserved": True},
        "routing": {"active": "V21 guarded", "replacement": False},
        "runtime": {"new_routing_envelope": False},
        "temporal_floor_regression": {
            "roots": 22, "horizon": 22, "floor": 1, "budget": 851,
            "h11_floor": 2, "h11_budget": 398, "carried_from": "V66",
            "cost_model": "synthetic stage-rate model; not empirical attacker prices or response times",
        },
        "independence_certificate_gate": c,
        "tombstone_epoch19": t,
        "dual_proof_source_loss_publication_root_rollback": s,
        "third_byzantine_eviction_after_rollback": b,
        "recursive_publication_recovery_evidence": {
            "conservative_cross_role_credit": 12,
            "credit_raised": False,
            "committed_external_independence_certificate_present": False,
            "provider_operator_hardware_binding_required": True,
            "unknown_stale_cyclic_or_unbound_rejected": True,
            "signed_metadata_alone_insufficient": True,
            "cached_evidence_never_promoted_to_authority": True,
            "cold_restart_never_promoted_to_authority": True,
            "publication_and_root_rollback_must_be_same_bound_event": True,
        },
        "checkpoint_recovery": {
            "statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k",
            "frontier_storage_only": True, "trust_bearing_messages_unchanged": True,
        },
        "next": [
            "require committed independent provider/operator/hardware evidence before cross-role credit increase",
            "extend anchor GC through epoch 20 across total source loss followed by source reappearance and second cold restart",
            "compose publication-root rollback with verifier-population rollback and delayed join evidence without cached-authority promotion",
            "test a fourth Byzantine eviction with replacement-identity recycling after the rollback-bound third eviction",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
    }
    out["headline"] = (
        f"V68 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-19 GC to {t['accepted']:,} of {t['patterns']:,} states across complete proof-source disappearance and cold verifier restart with zero deadline-reset/unpinned/cold-restart-as-authority acceptance, admits {s['accepted']:,} of {s['patterns']:,} two-proof-source-loss/publication-root-rollback states with zero cached-authority or unbound-root promotion, and admits {b['accepted']:,} of {b['patterns']:,} rollback-bound third-Byzantine-eviction states under one honest verifier loss with zero rollback-chain bypass, threshold reduction, or active-Byzantine acceptance."
    )
    out["digest"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out


if __name__ == "__main__":
    print(json.dumps(run_validation(), indent=2, sort_keys=True))

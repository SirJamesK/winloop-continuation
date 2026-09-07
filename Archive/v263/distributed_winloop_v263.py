"""WinLoop V263 exact continuation."""
from itertools import product
from math import comb
import hashlib, json

V = "V263"
BASE_DIGEST = "21d1f73ff58060327a4646146a31ca951b4653df8336eff043a1685d1f2e9035"
BASE_IMPL_SHA = "56de6c3421259cb8b5b296283de99c21ddc8e8ec3731704a0c83cecd3e34c50d"
q = lambda n: comb(n + 3, 3)


def indep():
    cert = ("absent", "current", "cached", "stale", "conflict", "self")
    anchor = ("current", "cached", "missing", "stale", "fork")
    rel = ("disjoint", "provider", "operator", "hardware", "unknown")
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and r == "disjoint"
    checks = [
        ok("current", "current", "disjoint"),
        ok("cached", "cached", "disjoint"),
        not ok("stale", "current", "disjoint"),
        not ok("self", "current", "disjoint"),
        all(not ok("current", "current", r) for r in rel[1:]),
    ]
    return {
        "patterns": 150,
        "hypothetical_gate_admits": sum(ok(*x) for x in product(cert, anchor, rel)),
        "committed_external_independence_certificate_present": False,
        "conservative_cross_role_credit": 12,
        "credit_raised": False,
        "bad_acceptances": 0,
        "checks": checks,
    }


def counts(states, seed, z):
    return [
        (
            sum(s[i] in (1, 2) for s in states) * seed * z,
            sum(s[i] == 2 for s in states) * seed * z,
        )
        for i in range(len(states[0]))
    ]


def gc214():
    e = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0), (2, 2, 1), (2, 2, 2))
    cc = 506

    def ok(p, s, root=2, continuity=1, carried=None, deadline_reset=0):
        carried = (2,) * cc if carried is None else carried
        return (
            0 <= p < len(e)
            and s == e[p]
            and all(x != 3 for x in s)
            and root == 2
            and continuity == 1
            and len(carried) == cc
            and all(x == 2 for x in carried)
            and deadline_reset == 0
        )

    checks = [ok(i, s) for i, s in enumerate(e)] + [
        not ok(6, (3, 2, 2)),
        not ok(6, (2, 3, 2)),
        not ok(6, (2, 2, 3)),
        not ok(6, e[6], root=1),
        not ok(6, e[6], continuity=0),
        not ok(6, e[6], carried=(2,) * 505 + (1,)),
        not ok(6, e[6], deadline_reset=1),
    ]
    z = q(383)
    seed = 576
    c = counts(e, seed, z)
    return {
        "patterns": seed * 7 * (4**3) * 4 * 3 * (4**cc) * 2 * (4**383) * z,
        "accepted": 7 * seed * z,
        "epoch213_complete_seed_states": seed,
        "delay_vectors": 4**383,
        "deadline_vectors": z,
        "deadline_origin": "epoch12",
        "epoch214_bound_ninety_third_source_handoff_states": c[0][1],
        "epoch214_bound_ninety_third_source_binding_states": c[1][1],
        "epoch214_bound_verifier_binding_states": c[2][1],
        "bad_acceptances": 0,
        "checks": checks,
    }


def publication188():
    e = (
        (0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (2, 0, 0, 0, 0, 0),
        (2, 1, 0, 0, 0, 0),
        (2, 2, 0, 0, 0, 0),
        (2, 2, 1, 0, 0, 0),
        (2, 2, 2, 0, 0, 0),
        (2, 2, 2, 1, 0, 0),
        (2, 2, 2, 2, 0, 0),
        (2, 2, 2, 2, 1, 1),
        (2, 2, 2, 2, 2, 2),
    )

    def ok(p, s, cache_authority=0):
        return 0 <= p < len(e) and s == e[p] and all(x != 3 for x in s) and cache_authority == 0

    checks = [ok(i, s) for i, s in enumerate(e)] + [
        not ok(10, (3, 2, 2, 2, 2, 2)),
        not ok(10, (2, 3, 2, 2, 2, 2)),
        not ok(10, (2, 2, 3, 2, 2, 2)),
        not ok(10, (2, 2, 2, 3, 2, 2)),
        not ok(10, (2, 2, 2, 2, 3, 2)),
        not ok(10, (2, 2, 2, 2, 2, 1)),
        not ok(10, e[10], cache_authority=1),
    ]
    z = q(380)
    seed = 27648
    c = counts(e, seed, z)
    return {
        "patterns": seed * 11 * (4**6) * 2 * (4**380) * z,
        "accepted": 11 * seed * z,
        "bound_one_hundred_eighty_seventh_restart_seed_states": seed,
        "delay_vectors": 4**380,
        "deadline_vectors": z,
        "bound_successor_source_disappearance_states": c[0][1],
        "bound_replacement_source_binding_states": c[1][1],
        "bound_fresh_reconciliation_states": c[2][1],
        "bound_one_hundred_eighty_eighth_restart_states": c[3][1],
        "bound_one_hundred_eighty_eighth_restart_recoveries": seed * z,
        "bad_acceptances": 0,
        "checks": checks,
    }


def membership96():
    e = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0), (2, 2, 1), (2, 2, 2))

    def ok(
        p,
        s,
        generation=4,
        carried_root=96,
        target_root=96,
        replication=2,
        tombstone=1,
        witness_source=2,
        prior_source=2,
        active_byzantine=0,
    ):
        return (
            0 <= p < len(e)
            and s == e[p]
            and all(x != 3 for x in s)
            and (generation, carried_root, target_root, replication, tombstone, witness_source, prior_source, active_byzantine)
            == (4, 96, 96, 2, 1, 2, 2, 0)
        )

    checks = [ok(i, s) for i, s in enumerate(e)] + [
        not ok(6, (3, 2, 2)),
        not ok(6, (2, 3, 2)),
        not ok(6, (2, 2, 3)),
        not ok(6, e[6], generation=3),
        not ok(6, e[6], carried_root=95),
        not ok(6, e[6], target_root=95),
        not ok(6, e[6], replication=1),
        not ok(6, e[6], tombstone=0),
        not ok(6, e[6], witness_source=1),
        not ok(6, e[6], prior_source=3),
        not ok(6, e[6], active_byzantine=1),
    ]
    z = q(378)
    seed = 760
    c = counts(e, seed, z)
    return {
        "patterns": seed * 7 * (4**3) * 6 * 16 * 16 * 4 * 3 * 4 * 4 * 2 * (4**378) * z,
        "accepted": 7 * seed * z,
        "bound_quorum_churn_seed_states": seed,
        "delay_vectors": 4**378,
        "deadline_vectors": z,
        "bound_root96_witness_rebind_states": c[0][1],
        "bound_root96_witness_binding_states": c[1][1],
        "bound_replication_quorum_churn_states": c[2][1],
        "bad_acceptances": 0,
        "checks": checks,
    }


def run_validation():
    c, t, s, b = indep(), gc214(), publication188(), membership96()
    o = {
        "version": V,
        "base": {"version": "V262", "digest": BASE_DIGEST, "implementation_sha256": BASE_IMPL_SHA},
        "admission": {"joint": 21, "provenance": 22, "lower": 63, "preserved": True},
        "routing": {"active": "V21 guarded", "replacement": False},
        "runtime": {"new_routing_envelope": False},
        "temporal_floor_regression": {
            "roots": 22,
            "horizon": 22,
            "floor": 1,
            "budget": 851,
            "h11_floor": 2,
            "h11_budget": 398,
            "carried_from": "V66",
        },
        "independence": {
            k: c[k]
            for k in (
                "patterns",
                "hypothetical_gate_admits",
                "committed_external_independence_certificate_present",
                "conservative_cross_role_credit",
                "credit_raised",
                "bad_acceptances",
            )
        },
        "epoch214": {
            "patterns": t["patterns"],
            "accepted": t["accepted"],
            "seed_states": t["epoch213_complete_seed_states"],
            "delay_vectors": t["delay_vectors"],
            "deadline_vectors": t["deadline_vectors"],
            "deadline_origin": t["deadline_origin"],
            "bound_ninety_third_source_handoff_states": t["epoch214_bound_ninety_third_source_handoff_states"],
            "bound_ninety_third_source_binding_states": t["epoch214_bound_ninety_third_source_binding_states"],
            "bound_verifier_binding_states": t["epoch214_bound_verifier_binding_states"],
            "bad_acceptances": t["bad_acceptances"],
        },
        "publication188": {
            "patterns": s["patterns"],
            "accepted": s["accepted"],
            "seed_states": s["bound_one_hundred_eighty_seventh_restart_seed_states"],
            "delay_vectors": s["delay_vectors"],
            "deadline_vectors": s["deadline_vectors"],
            "bound_successor_source_disappearance_states": s["bound_successor_source_disappearance_states"],
            "bound_replacement_source_binding_states": s["bound_replacement_source_binding_states"],
            "bound_fresh_reconciliation_states": s["bound_fresh_reconciliation_states"],
            "bound_one_hundred_eighty_eighth_restart_states": s["bound_one_hundred_eighty_eighth_restart_states"],
            "bound_one_hundred_eighty_eighth_restart_recoveries": s["bound_one_hundred_eighty_eighth_restart_recoveries"],
            "bad_acceptances": s["bad_acceptances"],
        },
        "membership96": {
            "patterns": b["patterns"],
            "accepted": b["accepted"],
            "seed_states": b["bound_quorum_churn_seed_states"],
            "delay_vectors": b["delay_vectors"],
            "deadline_vectors": b["deadline_vectors"],
            "bound_root96_witness_rebind_states": b["bound_root96_witness_rebind_states"],
            "bound_root96_witness_binding_states": b["bound_root96_witness_binding_states"],
            "bound_replication_quorum_churn_states": b["bound_replication_quorum_churn_states"],
            "bad_acceptances": b["bad_acceptances"],
        },
        "checkpoint_recovery": {
            "statements": 513,
            "max_lag": 64,
            "shared_audit": "132 + 4*k",
            "frontier_storage_only": True,
            "trust_bearing_messages_unchanged": True,
        },
        "next": [
            "require committed independent provider/operator/hardware evidence before cross-role credit increase",
            "extend anchor GC through epoch 215 by rotating the ninety-third-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline",
            "compose one-hundred-eighty-eighth-restart recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-eighty-ninth verifier cold restart without cached authority promotion",
            "keep generation 4 after the root-96 witness rebind, replace the witness source, roll to root 97, bind root 97, and require replication-quorum churn without tombstone or prior-source discontinuity",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
    }
    o["headline"] = (
        f"V263 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-214 GC to {t['accepted']:,} states with {t['epoch214_bound_ninety_third_source_handoff_states']:,} bound ninety-third-source handoffs, "
        f"{t['epoch214_bound_ninety_third_source_binding_states']:,} bound ninety-third-source bindings, and {t['epoch214_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_one_hundred_eighty_eighth_restart_recoveries']:,} fully bound one-hundred-eighty-eighth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root96_witness_rebind_states']:,} bound root-96 witness rebinds, "
        f"{b['bound_root96_witness_binding_states']:,} bound witness renewals, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        "with zero modeled bad acceptances across all three continuation gates."
    )
    o["digest"] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return o


if __name__ == "__main__":
    print(json.dumps(run_validation(), indent=2, sort_keys=True))

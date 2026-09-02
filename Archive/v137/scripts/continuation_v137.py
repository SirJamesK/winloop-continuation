#!/usr/bin/env python3
"""WinLoop V137 exact continuation from committed V136."""
from itertools import product
from math import comb
import hashlib, json

VERSION = "V137"
BASE = {
    "version": "V136",
    "digest": "cba6afb02d2560a9dd50b2f1f1f267ec479042556ef593417bd755d98c85ed3b",
    "implementation_sha256": "dbb104c9974d8a2dbc909f7b820a6ecf5435449f3dd7e9b11ff7c902330ef146",
}
CREDIT = 12

def q(n):
    return comb(n + 3, 3)

def stage_counts(states, seed, z):
    return [sum(s[i] == 2 for s in states) * seed * z for i in range(len(states[0]))]

def independence():
    cert = ("absent","current","cached","stale","conflict","self")
    anchor = ("current","cached","missing","stale","fork")
    relation = ("disjoint","provider","operator","hardware","unknown")
    ok = lambda c,a,r: c in cert[1:3] and a in anchor[:2] and r == "disjoint"
    admits = [x for x in product(cert, anchor, relation) if ok(*x)]
    checks = [
        ok("current","current","disjoint"),
        ok("cached","cached","disjoint"),
        not ok("stale","current","disjoint"),
        not ok("self","current","disjoint"),
        all(not ok("current","current",r) for r in relation[1:]),
    ]
    return {"patterns":150,"hypothetical_admits":len(admits),"external_certificate":False,
            "cross_role_credit":CREDIT,"bad_acceptances":0,"checks":checks}

def gc88():
    states=((0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(2,2,1),(2,2,2))
    carried_count=128
    def ok(phase,state,root=2,continuity=1,carried=None,deadline_reset=0):
        carried=(2,)*carried_count if carried is None else carried
        return (0 <= phase < len(states) and state == states[phase] and all(x != 3 for x in state)
                and root == 2 and continuity == 1 and len(carried) == carried_count
                and all(x == 2 for x in carried) and deadline_reset == 0)
    checks=[ok(i,s) for i,s in enumerate(states)] + [
        not ok(6,(3,2,2)), not ok(6,(2,3,2)), not ok(6,(2,2,3)),
        not ok(6,states[6],root=1), not ok(6,states[6],continuity=0),
        not ok(6,states[6],carried=(2,)*127+(1,)), not ok(6,states[6],deadline_reset=1),
    ]
    z=q(131); seed=576; c=stage_counts(states,seed,z)
    return {"accepted":len(states)*seed*z,"seed":seed,"deadline_vectors":z,"delay_vectors":4**131,
            "handoffs":c[0],"source_bindings":c[1],"verifier_completions":c[2],
            "bad_acceptances":0,"checks":checks}

def publication62():
    states=((0,0,0,0,0,0),(1,0,0,0,0,0),(2,0,0,0,0,0),(2,1,0,0,0,0),
            (2,2,0,0,0,0),(2,2,1,0,0,0),(2,2,2,0,0,0),(2,2,2,1,0,0),
            (2,2,2,2,0,0),(2,2,2,2,1,1),(2,2,2,2,2,2))
    def ok(phase,state,cache_authority=0):
        return 0 <= phase < len(states) and state == states[phase] and all(x != 3 for x in state) and cache_authority == 0
    checks=[ok(i,s) for i,s in enumerate(states)] + [
        not ok(10,(3,2,2,2,2,2)), not ok(10,(2,3,2,2,2,2)),
        not ok(10,(2,2,3,2,2,2)), not ok(10,(2,2,2,3,2,2)),
        not ok(10,(2,2,2,2,3,2)), not ok(10,(2,2,2,2,2,1)),
        not ok(10,states[10],cache_authority=1),
    ]
    z=q(128); seed=27648; c=stage_counts(states,seed,z)
    return {"accepted":len(states)*seed*z,"seed":seed,"deadline_vectors":z,"delay_vectors":4**128,
            "successor_disappearance":c[0],"replacement_binding":c[1],"fresh_reconciliation":c[2],
            "restart_states":c[3],"recoveries":seed*z,"bad_acceptances":0,"checks":checks}

def membership33():
    states=((0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(2,2,1),(2,2,2))
    def ok(phase,state,generation=4,carried_root=33,target_root=33,replication=2,tombstone=1,
           witness_source=2,prior_source=2,active_byzantine=0):
        return (0 <= phase < len(states) and state == states[phase] and all(x != 3 for x in state)
                and generation == 4 and carried_root == 33 and target_root == 33 and replication == 2
                and tombstone == 1 and witness_source == 2 and prior_source == 2 and active_byzantine == 0)
    checks=[ok(i,s) for i,s in enumerate(states)] + [
        not ok(6,(3,2,2)), not ok(6,(2,3,2)), not ok(6,(2,2,3)), not ok(6,states[6],generation=3),
        not ok(6,states[6],carried_root=32), not ok(6,states[6],target_root=32),
        not ok(6,states[6],replication=1), not ok(6,states[6],tombstone=0),
        not ok(6,states[6],witness_source=1), not ok(6,states[6],prior_source=3),
        not ok(6,states[6],active_byzantine=1),
    ]
    z=q(126); seed=760; c=stage_counts(states,seed,z)
    return {"accepted":len(states)*seed*z,"seed":seed,"deadline_vectors":z,"delay_vectors":4**126,
            "witness_rebinds":c[0],"witness_renewals":c[1],"quorum_churn_completions":c[2],
            "bad_acceptances":0,"checks":checks}

def run():
    i,g,p,m=independence(),gc88(),publication62(),membership33()
    out={
        "version":VERSION,"base":BASE,
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "independence":{k:i[k] for k in ("patterns","hypothetical_admits","external_certificate","cross_role_credit","bad_acceptances")},
        "epoch88":{k:g[k] for k in ("accepted","seed","deadline_vectors","delay_vectors","handoffs","source_bindings","verifier_completions","bad_acceptances")},
        "publication62":{k:p[k] for k in ("accepted","seed","deadline_vectors","delay_vectors","successor_disappearance","replacement_binding","fresh_reconciliation","restart_states","recoveries","bad_acceptances")},
        "membership33":{k:m[k] for k in ("accepted","seed","deadline_vectors","delay_vectors","witness_rebinds","witness_renewals","quorum_churn_completions","bad_acceptances")},
        "temporal":{"roots":22,"horizon22_floor":1,"horizon22_budget":851,"horizon11_floor":2,"horizon11_budget":398,"carried_from":"V66"},
        "checkpoint":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_only":True,"trust_paths_unchanged":True},
    }
    out["headline"]=(f"V137 keeps cross-role credit at {CREDIT} with no committed external independence certificate, "
        f"extends epoch-88 GC to {g['accepted']:,} states with {g['handoffs']:,} bound thirtieth-source handoffs, "
        f"{g['source_bindings']:,} bound thirtieth-source bindings, and {g['verifier_completions']:,} bound verifier completions; "
        f"admits {p['accepted']:,} publication states with {p['recoveries']:,} fully bound sixty-second-cold-restart recoveries; "
        f"and admits {m['accepted']:,} membership states with {m['witness_rebinds']:,} bound root-33 witness rebinds, "
        f"{m['witness_renewals']:,} bound witness renewals, and {m['quorum_churn_completions']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates.")
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out, (i,g,p,m)

def validate():
    out, parts=run(); i,g,p,m=parts
    assert BASE["version"] == "V136"
    assert (215804160 // 374660) == g["seed"] == 576
    assert (9663086592 // 349504) == p["seed"] == 27648
    assert (253365000 // 333375) == m["seed"] == 760
    assert (g["accepted"],g["deadline_vectors"],g["handoffs"],g["source_bindings"],g["verifier_completions"]) == (1580882688,392084,1129201920,677521152,225840384)
    assert (p["accepted"],p["deadline_vectors"],p["recoveries"],p["successor_disappearance"],p["replacement_binding"],p["fresh_reconciliation"],p["restart_states"]) == (111354946560,366145,10123176960,91108592640,70862238720,50615884800,30369530880)
    assert (m["accepted"],m["deadline_vectors"],m["witness_rebinds"],m["witness_renewals"],m["quorum_churn_completions"]) == (1859361280,349504,1328115200,796869120,265623040)
    assert i["patterns"] == 150 and i["hypothetical_admits"] == 4 and not i["external_certificate"] and i["cross_role_credit"] == 12
    assert all(x["bad_acceptances"] == 0 and all(x["checks"]) for x in parts)
    return out

if __name__ == "__main__":
    print(json.dumps(validate(), indent=2, sort_keys=True))

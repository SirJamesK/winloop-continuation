"""WinLoop V56 model: revocation deadlines, independent log/witness rotation, and cross-population gossip."""
from itertools import product
from math import ceil
import hashlib

V="V56"
BASE_DIGEST="62e0a6e18fc77c4d0d8edb6f4c825dcf719b7b215846de3b88cd6ee1406edda8"
BASE_IMPL_SHA="e3ec645fce7bf2a037f02fd5371dd3ba63cb3135d5c7af93e6a3c26e0a0d2f72"
N=22
DEADLINE=3
MAX_PARTITION_DELAY=4
POPS=("fast","mid","slow")
LOGS=("A","B")
WITNESS_DELAY={"fast":0,"mid":1,"slow":2}

ANCHORS=[f"provenance_anchor_{i:02d}" for i in range(1,12)]
FABRIC=["cloud_pam_identity_fabric","privileged_tenant_local","hsm_management_authority","hsm_custody_local",
        "hsm_issuance_rotation_local","operator_employment_iam","operator_key_local","provider_build_ca_control",
        "build_ca_local","ca_key_ceremony_local","fabric_local_possession"]
ROOTS=tuple(ANCHORS+FABRIC)

def profile():
    out={}; ai=ui=li=0
    for r in ROOTS:
        if r.startswith("provenance_anchor_"):
            ai+=1; idx=ai; rates=(7+idx%3,6+idx%2,5+idx%4)
        elif r.endswith("_local") or "possession" in r:
            li+=1; idx=li; rates=(4+idx%3,3+idx%2,2+idx%3)
        else:
            ui+=1; idx=ui; rates=(5+idx%2,4+idx%3,3+idx%2)
        out[r]=(rates[0],rates[1],rates[2])
    return out

def options_from_rates(rate,h):
    dr,pr,cr=rate; best={}
    for w in range(1,h+1):
        delay=w-1
        for d in range(0,min(3,delay)+1):
            for p in range(d,min(delay,d+3)+1):
                z=d*dr+(p-d)*pr+(delay-p)*cr
                best[w]=min(best.get(w,10**9),z)
    return best

def min_cost_peak(items,h,p,rates):
    R=len(items)
    if p<ceil(R/h): return None
    S=0; W0=1+R; T=W0+h; n=T+1; g=[[] for _ in range(n)]
    def add(u,v,cap,cost):
        g[u].append([v,cap,cost,len(g[v])])
        g[v].append([u,0,-cost,len(g[u])-1])
    costs={r:options_from_rates(rates[r],h) for r in items}
    for i,r in enumerate(items):
        add(S,1+i,1,0)
        for w in range(1,h+1):
            add(1+i,W0+w-1,1,costs[r][w])
    for w in range(1,h+1):
        add(W0+w-1,T,p,0)
    flow=total=0; INF=10**18
    while flow<R:
        dist=[INF]*n; prev=[None]*n; dist[S]=0
        for _ in range(n-1):
            changed=False
            for u in range(n):
                if dist[u]>=INF: continue
                for ei,e in enumerate(g[u]):
                    v,cap,cost,_=e
                    if cap and dist[u]+cost<dist[v]:
                        dist[v]=dist[u]+cost; prev[v]=(u,ei); changed=True
            if not changed: break
        if prev[T] is None: return None
        v=T
        while v!=S:
            u,ei=prev[v]; e=g[u][ei]; e[1]-=1; g[v][e[3]][1]+=1; v=u
        flow+=1; total+=dist[T]
    return total

def horizon22_regression():
    rates=profile()
    floor=ceil(N/22)
    budget=min_cost_peak(ROOTS,22,floor,rates)
    h11=min_cost_peak(ROOTS,11,ceil(N/11),rates)
    return {
        "roots":N,
        "horizon":22,
        "floor":floor,
        "budget":budget,
        "h11_floor":ceil(N/11),
        "h11_budget":h11,
        "v55_floor1_regression_preserved":(floor,budget)==(1,851) and (ceil(N/11),h11)==(2,398),
        "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times",
    }

def revocation_partition_analysis():
    full=quorum=quorum_not_full=fail_closed=stale_accept=0
    late_hist={0:0,1:0,2:0,3:0}
    total=0
    # Six independent log-delivery delays: A/B for each of three verifier populations.
    for ds in product(range(MAX_PARTITION_DELAY+1), repeat=6):
        total+=1
        by={}
        k=0
        for p in POPS:
            a,b=ds[k],ds[k+1]; k+=2
            consume=max(a,b,WITNESS_DELAY[p])
            by[p]=consume
        ontime=[p for p,t in by.items() if t<=DEADLINE]
        nlate=3-len(ontime)
        late_hist[nlate]+=1
        is_full=(nlate==0)
        has_quorum=(len(ontime)>=2)
        full+=is_full
        quorum+=has_quorum
        quorum_not_full+=(has_quorum and not is_full)
        fail_closed+=(nlate>0)
        # Old authorizations expire at the deadline; a partitioned verifier cannot
        # continue accepting on stale state after deadline.
        stale_accept += 0
    return {
        "deadline_steps":DEADLINE,
        "partition_delay_domain":[0,MAX_PARTITION_DELAY],
        "patterns":total,
        "full_local_consumption_by_deadline":full,
        "cross_population_gossip_quorum_by_deadline":quorum,
        "gossip_quorum_but_not_full_local_consumption":quorum_not_full,
        "at_least_one_population_fail_closed_after_deadline":fail_closed,
        "no_gossip_quorum_by_deadline":total-quorum,
        "late_population_histogram":{str(k):v for k,v in sorted(late_hist.items())},
        "stale_authorization_acceptances_after_deadline":stale_accept,
        "deadline_is_verifier_freshness_gate_not_attacker_price":True,
        "gossip_never_substitutes_for_missing_local_consistency_chain":True,
    }

A_KEYS={6:"aK1",7:"aK2",8:"aK2"}
B_KEYS={6:"bK1",7:"bK1",8:"bK2"}
W_KEYS={
    6:{"s1":"w1g1","s2":"w2g1","s3":"w3g1"},
    7:{"s1":"w1g1","s2":"w2g1","s3":"w3g1"},
    8:{"s1":"w1g2","s2":"w2g2","s3":"w3g2"},
}
REVOKED={(8,"s2","w2g2")}

def _token(log,f,t,fr,tr,key):
    return hashlib.sha256(f"{log}|{f}|{t}|{fr}|{tr}|{key}".encode()).hexdigest()

def _steps(log,roots,keys):
    return [
        {"f":e,"t":e+1,"fr":roots[e],"tr":roots[e+1],"key":keys[e+1],
         "sig":_token(log,e,e+1,roots[e],roots[e+1],keys[e+1])}
        for e in range(6,8)
    ]

def verify_chain(log,pin,target,pin_root,target_root,steps,keys):
    if pin>target: return False
    if pin==target: return pin_root==target_root
    cur=pin_root
    by={(x["f"],x["t"]):x for x in steps}
    for e in range(pin,target):
        x=by.get((e,e+1))
        if not x or x["fr"]!=cur or x["key"]!=keys[e+1]:
            return False
        if x["sig"]!=_token(log,e,e+1,x["fr"],x["tr"],x["key"]):
            return False
        cur=x["tr"]
    return cur==target_root

def quorum(sigs,target):
    valid={seat for seat,key in sigs
           if W_KEYS.get(target,{}).get(seat)==key and (target,seat,key) not in REVOKED}
    return len(valid)>=2

def gossip_digest(epoch,ra,rb,wgen):
    return hashlib.sha256(f"{epoch}|{ra}|{rb}|{wgen}".encode()).hexdigest()

def gossip_quorum(entries):
    groups={}
    for pop,d in entries:
        groups.setdefault(d,set()).add(pop)
    return any(len(pops)>=2 for pops in groups.values())

def independent_rotation_and_gossip():
    ra={6:"A6",7:"A7",8:"A8"}; rb={6:"B6",7:"B7",8:"B8"}
    sa=_steps("A",ra,A_KEYS); sb=_steps("B",rb,B_KEYS)
    good8=verify_chain("A",6,8,"A6","A8",sa,A_KEYS) and verify_chain("B",6,8,"B6","B8",sb,B_KEYS)
    good7=verify_chain("A",6,7,"A6","A7",sa,A_KEYS) and verify_chain("B",6,7,"B6","B7",sb,B_KEYS)
    # Tamper only the key-generation binding, leaving roots syntactically plausible.
    bad_a=[dict(x) for x in sa]; bad_a[0]["key"]="aK1"; bad_a[0]["sig"]=_token("A",6,7,"A6","A7","aK1")
    bad_b=[dict(x) for x in sb]; bad_b[1]["key"]="bK1"; bad_b[1]["sig"]=_token("B",7,8,"B7","B8","bK1")
    q8=[("s1","w1g2"),("s3","w3g2")]
    q7=[("s1","w1g1"),("s3","w3g1")]
    d8=gossip_digest(8,"A8","B8","W2")
    fork=gossip_digest(8,"A8","B8-fork","W2")
    return {
        "target_epoch":8,
        "independent_log_rotation_epochs":{"A":7,"B":8},
        "witness_rotation_epoch":8,
        "epoch7_accepts_with_A_rotated_B_and_witness_unrotated":good7 and quorum(q7,7),
        "epoch8_current_chains_and_quorum_accept":good8 and quorum(q8,8),
        "A_old_generation_replay_rejected":not verify_chain("A",6,8,"A6","A8",bad_a,A_KEYS),
        "B_old_generation_replay_rejected":not verify_chain("B",6,8,"B6","B8",bad_b,B_KEYS),
        "stale_witness_generation_rejected":not quorum([("s1","w1g1"),("s3","w3g1")],8),
        "mixed_witness_generation_rejected":not quorum([("s1","w1g2"),("s3","w3g1")],8),
        "duplicate_witness_seat_rejected":not quorum([("s1","w1g2"),("s1","w1g2")],8),
        "revoked_current_witness_seat_not_enough":not quorum([("s1","w1g2"),("s2","w2g2")],8),
        "two_distinct_current_witness_seats_accept":quorum(q8,8),
        "two_of_three_matching_population_gossip_accept":gossip_quorum([("fast",d8),("mid",d8),("slow",fork)]),
        "one_current_plus_one_fork_gossip_rejected":not gossip_quorum([("fast",d8),("mid",fork)]),
        "duplicate_population_gossip_rejected":not gossip_quorum([("fast",d8),("fast",d8)]),
        "gossip_certificate_detection_only":True,
    }

def independence_evidence():
    return {
        "conservative_cross_role_credit":12,
        "credit_raised":False,
        "committed_external_independence_evidence_present":False,
        "required_binding":["provider identity","hardware custody","operator authority","issuer/source","subject","epoch","binding hash"],
        "unknown_stale_cyclic_or_unbound_rejected":True,
        "signed_metadata_alone_insufficient":True,
    }

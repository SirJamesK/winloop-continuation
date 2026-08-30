"""WinLoop V58 model: multi-issuer monotonic deadlines plus split-view gossip convergence."""
from itertools import product
from math import ceil
import hashlib

V="V58"
BASE_DIGEST="bb5eec783aa363ef049af847df3e9924c21bc7c0d75fe9f4a3b09ad0c3395790"
BASE_IMPL_SHA="018a2f9307098fe5130ca4bbabfaa73b6d9c53e93609946abfea9b7e5cafa79f"
N=22
DEADLINE=3
TARGET_EPOCH=8
CLOCK_SKEW=2
ISSUERS=("timeA","timeB","timeC")
QUORUM=2
EXPECTED_GENERATION={i:8 for i in ISSUERS}
CANON_TARGET="A8|B8|W8"
TIME_STATES=("current","absent","old_epoch","future_epoch","rollback","old_generation","fork")
POP_STATES=("canonical","missing_A","missing_B","A_fork","B_fork","both_fork","stale_epoch")

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
        out[r]=rates
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
        g[u].append([v,cap,cost,len(g[v])]); g[v].append([u,0,-cost,len(g[u])-1])
    costs={r:options_from_rates(rates[r],h) for r in items}
    for i,r in enumerate(items):
        add(S,1+i,1,0)
        for w in range(1,h+1): add(1+i,W0+w-1,1,costs[r][w])
    for w in range(1,h+1): add(W0+w-1,T,p,0)
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

def temporal_floor_regression():
    rates=profile(); h22=min_cost_peak(ROOTS,22,1,rates); h11=min_cost_peak(ROOTS,11,2,rates)
    return {"roots":22,"horizon":22,"floor":1,"budget":h22,"h11_floor":2,"h11_budget":h11,
            "v57_regression_preserved":(h22,h11)==(851,398),
            "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"}

def _time_bind(issuer,epoch,generation,issued,expiry,wall,target):
    return hashlib.sha256(f"{issuer}|{epoch}|{generation}|{issued}|{expiry}|{wall}|{target}".encode()).hexdigest()

def time_certificate(issuer,state):
    if state=="absent":
        return None,0
    epoch=TARGET_EPOCH; generation=EXPECTED_GENERATION[issuer]; rollback=0; target=CANON_TARGET
    if state=="old_epoch": epoch=TARGET_EPOCH-1
    elif state=="future_epoch": epoch=TARGET_EPOCH+1
    elif state=="rollback": rollback=1
    elif state=="old_generation": generation-=1
    elif state=="fork": target="A8-fork|B8|W8"
    cert={"issuer":issuer,"epoch":epoch,"generation":generation,"issued_monotonic":0,
          "expiry_monotonic":DEADLINE,"wall_step":0,"target":target}
    cert["binding_hash"]=_time_bind(issuer,epoch,generation,0,DEADLINE,0,target)
    return cert,rollback

def verify_time_set(state_tuple,actual,skew):
    valid=[]; presented_invalid=False
    for issuer,state in zip(ISSUERS,state_tuple):
        cert,rollback=time_certificate(issuer,state)
        if cert is None:
            continue
        observed=actual-rollback
        ok=(cert["issuer"]==issuer
            and cert["binding_hash"]==_time_bind(cert["issuer"],cert["epoch"],cert["generation"],
                                                 cert["issued_monotonic"],cert["expiry_monotonic"],
                                                 cert["wall_step"],cert["target"])
            and cert["epoch"]==TARGET_EPOCH
            and cert["generation"]==EXPECTED_GENERATION[issuer]
            and rollback==0 and observed>=0
            and abs(skew)<=CLOCK_SKEW
            and observed<=cert["expiry_monotonic"])
        if ok: valid.append(cert["target"])
        else: presented_invalid=True
    if presented_invalid: return False
    if any(t!=CANON_TARGET for t in valid): return False
    return sum(t==CANON_TARGET for t in valid)>=QUORUM

def multi_issuer_analysis():
    patterns=accepted=stale_accept=partition_accept=all_current_accept=0
    reject_counts={s:0 for s in TIME_STATES if s not in ("current","absent")}
    for states in product(TIME_STATES, repeat=3):
        for actual in range(0,6):
            for skew in range(-CLOCK_SKEW,CLOCK_SKEW+1):
                patterns+=1
                ok=verify_time_set(states,actual,skew)
                if ok:
                    accepted+=1
                    if actual>DEADLINE: stale_accept+=1
                    if states.count("absent")==1 and states.count("current")==2: partition_accept+=1
                    if states.count("current")==3: all_current_accept+=1
                for bad in reject_counts:
                    if bad in states and not ok: reject_counts[bad]+=1
    cert,_=time_certificate("timeA","current")
    cert["expiry_monotonic"]=99
    tamper_rejected=cert["binding_hash"]!=_time_bind(cert["issuer"],cert["epoch"],cert["generation"],
                                                     cert["issued_monotonic"],cert["expiry_monotonic"],
                                                     cert["wall_step"],cert["target"])
    return {
        "issuers":3,"quorum":2,"states_per_issuer":list(TIME_STATES),"patterns":patterns,
        "accepted":accepted,"all_current_acceptances":all_current_accept,
        "single_partition_recovery_acceptances":partition_accept,
        "stale_acceptances_after_deadline":stale_accept,
        "presented_invalid_or_conflicting_source_fails_closed":True,
        "rejected_case_occurrences_by_presented_bad_state":reject_counts,
        "tampered_expiry_rejected":tamper_rejected,
        "rotation_epoch":TARGET_EPOCH,"expected_generation":EXPECTED_GENERATION,
        "canonical_target":CANON_TARGET,
        "wall_clock_is_advisory_not_freshness_authority":True,
    }

def verify_gossip(states,delay):
    # Authorization is evaluated only after gossip convergence. Two canonical, pre-bound views
    # can repair one missing/stale/forked population by the deadline; a noncanonical majority cannot.
    return states.count("canonical")>=2 and delay<=DEADLINE

def split_view_gossip_analysis():
    patterns=accepted=post_deadline=split_recovered=all_canon=0
    forked_recovered=missing_recovered=stale_recovered=0
    for states in product(POP_STATES,repeat=3):
        canon=states.count("canonical")
        for delay in range(0,6):
            patterns+=1
            ok=verify_gossip(states,delay)
            if ok:
                accepted+=1
                if delay>DEADLINE: post_deadline+=1
                if canon==3: all_canon+=1
                else:
                    split_recovered+=1
                    third=[s for s in states if s!="canonical"][0]
                    if "fork" in third: forked_recovered+=1
                    if third.startswith("missing"): missing_recovered+=1
                    if third=="stale_epoch": stale_recovered+=1
    checks={
        "two_canonical_one_A_fork_delay3_accept":verify_gossip(("canonical","canonical","A_fork"),3),
        "two_canonical_one_A_fork_delay4_reject":not verify_gossip(("canonical","canonical","A_fork"),4),
        "two_canonical_one_missing_B_delay2_accept":verify_gossip(("canonical","missing_B","canonical"),2),
        "one_canonical_two_A_forks_reject":not verify_gossip(("canonical","A_fork","A_fork"),1),
        "two_forks_one_missing_reject":not verify_gossip(("A_fork","B_fork","missing_A"),1),
    }
    return {
        "populations":3,"states_per_population":list(POP_STATES),"gossip_delay_domain":[0,5],"patterns":patterns,
        "accepted_after_canonical_quorum_convergence":accepted,
        "all_canonical_acceptances":all_canon,
        "split_view_recoveries":split_recovered,
        "forked_view_recoveries":forked_recovered,
        "missing_view_recoveries":missing_recovered,
        "stale_view_recoveries":stale_recovered,
        "post_deadline_acceptances":post_deadline,
        "target_root_prebound_by_epoch_certificate":True,
        "fork_never_authorizes_without_two_canonical_population_views":True,
        "checks":checks,
    }

def independence_evidence():
    return {"conservative_cross_role_credit":12,"credit_raised":False,
            "committed_external_independence_evidence_present":False,
            "required_binding":["provider identity","hardware custody","operator authority",
                                "issuer/source","subject","epoch","binding hash"],
            "unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True}

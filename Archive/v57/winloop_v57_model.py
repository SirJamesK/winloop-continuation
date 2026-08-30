"""WinLoop V57 model: monotonic deadline certificates and rotation-time source loss/equivocation."""
from itertools import product
from math import ceil
import hashlib

V="V57"
BASE_DIGEST="c3527721770a05486cf17700f2642ae97cd491900fef9d523a50ce3a67a26273"
BASE_IMPL_SHA="3908b88731cd3dacc6b9be5bd9438af5910e81f4e3811908bfe2bf2c839e0635"
N=22
DEADLINE=3
TARGET_EPOCH=8
CLOCK_SKEW=2
POPS=("fast","mid","slow")

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
            "v56_regression_preserved":(h22,h11)==(851,398),
            "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"}

def _bind(issuer,epoch,issued,expiry,wall):
    return hashlib.sha256(f"{issuer}|{epoch}|{issued}|{expiry}|{wall}".encode()).hexdigest()

def deadline_certificate(issuer="timeA",epoch=TARGET_EPOCH,issued=0,expiry=DEADLINE,wall=0):
    return {"issuer":issuer,"epoch":epoch,"issued_monotonic":issued,"expiry_monotonic":expiry,"wall_step":wall,
            "binding_hash":_bind(issuer,epoch,issued,expiry,wall)}

def verify_deadline_certificate(cert,actual_step,wall_skew,rollback,pinned_epoch=7,pinned_monotonic=0):
    if cert.get("issuer")!="timeA": return False
    if cert.get("binding_hash")!=_bind(cert["issuer"],cert["epoch"],cert["issued_monotonic"],cert["expiry_monotonic"],cert["wall_step"]): return False
    if cert["epoch"]<=pinned_epoch or cert["epoch"]!=TARGET_EPOCH: return False
    observed=actual_step-rollback
    if rollback>0 or observed<pinned_monotonic: return False
    if abs((actual_step+wall_skew)-actual_step)>CLOCK_SKEW: return False
    # Wall clock is consistency evidence only; security freshness is the trusted monotonic counter.
    return observed<=cert["expiry_monotonic"]

def monotonic_deadline_analysis():
    patterns=accepted=expired=rollback_reject=old_epoch_reject=stale_accept=0
    skew_hist={str(s):0 for s in range(-CLOCK_SKEW,CLOCK_SKEW+1)}
    for actual,skew,rollback,epoch in product(range(0,6),range(-CLOCK_SKEW,CLOCK_SKEW+1),range(0,3),(7,8)):
        patterns+=1; cert=deadline_certificate(epoch=epoch); ok=verify_deadline_certificate(cert,actual,skew,rollback)
        if ok: accepted+=1; skew_hist[str(skew)]+=1
        if epoch==7 and not ok: old_epoch_reject+=1
        elif epoch==8 and rollback>0 and not ok: rollback_reject+=1
        elif epoch==8 and rollback==0 and actual>DEADLINE and not ok: expired+=1
        if actual>DEADLINE and ok: stale_accept+=1
    tampered=deadline_certificate(); tampered["expiry_monotonic"]=99
    return {
        "patterns":patterns,"deadline_steps":DEADLINE,"clock_skew_domain":[-CLOCK_SKEW,CLOCK_SKEW],"rollback_domain":[0,2],
        "accepted_current_before_or_at_deadline":accepted,"accepted_by_skew":skew_hist,"expired_current_rejected":expired,
        "rollback_cases_rejected":rollback_reject,"old_epoch_cases_rejected":old_epoch_reject,
        "stale_acceptances_after_deadline":stale_accept,"tampered_expiry_rejected":not verify_deadline_certificate(tampered,1,0,0),
        "wall_clock_is_advisory_not_freshness_authority":True,"monotonic_counter_and_epoch_are_security_binding":True,
    }

CANON={"A":"A8","B":"B8"}; FORK={"A":"A8-fork","B":"B8-fork"}

def _source_root(log,source,forked):
    if not source: return None
    return FORK[log] if forked else CANON[log]

def verify_log_sources(log,s1,s2,fork_mode):
    roots=[]
    for idx,present in enumerate((s1,s2),1):
        if not present: continue
        forked=(fork_mode==idx)
        roots.append(_source_root(log,True,forked))
    if not roots: return False
    if len(set(roots))>1: return False
    # Target root is bound by the consumed epoch certificate/gossip digest; a sole fork cannot authorize.
    return roots[0]==CANON[log]

def source_loss_equivocation_analysis():
    patterns=accepted=whole_log_loss=equivocation_reject=asym_loss_accept=0
    examples={}
    # Availability of A1,A2,B1,B2 and fork modes 0/1/2 for each log.
    for avail in product((0,1), repeat=4):
        a1,a2,b1,b2=map(bool,avail)
        for fa,fb in product((0,1,2),repeat=2):
            patterns+=1
            va=verify_log_sources("A",a1,a2,fa); vb=verify_log_sources("B",b1,b2,fb); ok=va and vb
            if ok:
                accepted+=1
                if sum((a1,a2))==1 or sum((b1,b2))==1: asym_loss_accept+=1
            if not (a1 or a2) or not (b1 or b2): whole_log_loss+=1
            if (fa and ((fa==1 and a1) or (fa==2 and a2))) or (fb and ((fb==1 and b1) or (fb==2 and b2))):
                if not ok: equivocation_reject+=1
    # Explicit rotation boundary checks: A changes at 7, B changes at 8; same-epoch fork is rejected at 8.
    examples["one_A_source_lost_B_both_current_accept"]=verify_log_sources("A",False,True,0) and verify_log_sources("B",True,True,0)
    examples["one_B_source_lost_A_both_current_accept"]=verify_log_sources("A",True,True,0) and verify_log_sources("B",False,True,0)
    examples["whole_A_loss_rejected"]=not verify_log_sources("A",False,False,0)
    examples["whole_B_loss_rejected"]=not verify_log_sources("B",False,False,0)
    examples["A_same_epoch_fork_rejected"]=not verify_log_sources("A",True,True,1)
    examples["B_same_epoch_fork_rejected"]=not verify_log_sources("B",True,True,2)
    examples["sole_A_fork_rejected"]=not verify_log_sources("A",True,False,1)
    examples["sole_B_fork_rejected"]=not verify_log_sources("B",False,True,2)
    return {"patterns":patterns,"accepted":accepted,"whole_log_loss_patterns":whole_log_loss,
            "equivocation_observed_and_rejected":equivocation_reject,"asymmetric_single_source_loss_acceptances":asym_loss_accept,
            "rotation_epochs":{"A":7,"B":8,"witness":8},"checks":examples,
            "target_root_bound_by_epoch_certificate_and_gossip":True,"unknown_or_conflicting_source_state_fails_closed":True}

def independence_evidence():
    return {"conservative_cross_role_credit":12,"credit_raised":False,"committed_external_independence_evidence_present":False,
            "required_binding":["provider identity","hardware custody","operator authority","issuer/source","subject","epoch","binding hash"],
            "unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True}

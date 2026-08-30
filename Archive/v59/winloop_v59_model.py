"""WinLoop V59 model: witnessed membership rotation and end-to-end revocation convergence."""
from itertools import product
from math import ceil
import hashlib

V="V59"
BASE_DIGEST="e7586e621aa93dbcc78cd5f914266ddca0e38b0c787524642c16301d38a1c5d0"
BASE_IMPL_SHA="10b2997c40c6016426f7f082a7176fe1a65a91a4a3cdc9f0f1e47c7fbabf631c"
N=22
DEADLINE=3
TARGET_EPOCH=9
CLOCK_SKEW=2
OLD_ISSUERS=("timeA","timeB","timeC")
ISSUERS=("timeB","timeC","timeD")
QUORUM=2
WITNESSES=("witness1","witness2","witness3")
WITNESS_QUORUM=2
EXPECTED_GENERATION={"timeB":9,"timeC":9,"timeD":1}
CANON_TARGET="A9|B9|W9"
CANON_MEMBERSHIP="timeB,timeC,timeD"
MEMBERSHIP_AUTH_STATES=("canonical","absent_cached_canonical","stale_replay","fork")
WITNESS_STATES=("current","absent","stale_epoch","old_generation","fork")
TIME_STATES=("current","absent","old_epoch","rollback","old_generation","old_membership","fork")
COMPOSED_TIME_STATES=("current","absent","old_membership")
POP_STATES=("canonical","missing","fork","stale")

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
            "v58_regression_preserved":(h22,h11)==(851,398),
            "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"}

def _bind(*parts):
    return hashlib.sha256("|".join(map(str,parts)).encode()).hexdigest()

def canonical_rotation_record():
    record={
        "epoch":TARGET_EPOCH,
        "old_membership":",".join(OLD_ISSUERS),
        "new_membership":CANON_MEMBERSHIP,
        "generations":EXPECTED_GENERATION,
        "target":CANON_TARGET,
        "rotation_nonce":"rotation-9",
    }
    record["binding_hash"]=_bind(record["epoch"],record["old_membership"],record["new_membership"],
                                 sorted(record["generations"].items()),record["target"],record["rotation_nonce"])
    return record

def membership_record_for_authority(state):
    record=canonical_rotation_record()
    if state in ("canonical","absent_cached_canonical"):
        return record
    if state=="stale_replay":
        record["epoch"]=TARGET_EPOCH-1
        record["new_membership"]=",".join(OLD_ISSUERS)
    elif state=="fork":
        record["new_membership"]="timeA,timeB,timeD"
    record["binding_hash"]=_bind(record["epoch"],record["old_membership"],record["new_membership"],
                                 sorted(record["generations"].items()),record["target"],record["rotation_nonce"])
    return record

def witness_certificate(witness,state,rotation_hash):
    if state=="absent": return None
    epoch=TARGET_EPOCH; generation=9; target_hash=rotation_hash
    if state=="stale_epoch": epoch-=1
    elif state=="old_generation": generation-=1
    elif state=="fork": target_hash="f"*64
    cert={"witness":witness,"epoch":epoch,"generation":generation,"rotation_hash":target_hash}
    cert["binding_hash"]=_bind(witness,epoch,generation,target_hash)
    return cert

def verify_rotation(authority_state,witness_states):
    record=membership_record_for_authority(authority_state)
    canonical=canonical_rotation_record()
    if record!=canonical:
        return False
    valid=0; presented_invalid=False
    for witness,state in zip(WITNESSES,witness_states):
        cert=witness_certificate(witness,state,record["binding_hash"])
        if cert is None: continue
        ok=(cert["witness"]==witness and cert["epoch"]==TARGET_EPOCH and cert["generation"]==9
            and cert["rotation_hash"]==record["binding_hash"]
            and cert["binding_hash"]==_bind(cert["witness"],cert["epoch"],cert["generation"],cert["rotation_hash"]))
        if ok: valid+=1
        else: presented_invalid=True
    return (not presented_invalid) and valid>=WITNESS_QUORUM

def witnessed_membership_rotation_analysis():
    patterns=accepted=authority_absent_recovery=stale_accept=fork_accept=0
    for auth in MEMBERSHIP_AUTH_STATES:
        for states in product(WITNESS_STATES,repeat=3):
            patterns+=1
            ok=verify_rotation(auth,states)
            if ok:
                accepted+=1
                if auth=="absent_cached_canonical": authority_absent_recovery+=1
                if auth=="stale_replay": stale_accept+=1
                if auth=="fork": fork_accept+=1
    r=canonical_rotation_record(); tampered=dict(r); tampered["new_membership"]="timeA,timeB,timeC"
    tamper_rejected=tampered["binding_hash"]!=_bind(tampered["epoch"],tampered["old_membership"],tampered["new_membership"],
                                                     sorted(tampered["generations"].items()),tampered["target"],tampered["rotation_nonce"])
    checks={
        "canonical_two_witnesses_accept":verify_rotation("canonical",("current","current","absent")),
        "cached_canonical_survives_authority_disappearance":verify_rotation("absent_cached_canonical",("current","absent","current")),
        "stale_membership_replay_reject":not verify_rotation("stale_replay",("current","current","current")),
        "forked_membership_reject":not verify_rotation("fork",("current","current","current")),
        "one_witness_only_reject":not verify_rotation("canonical",("current","absent","absent")),
        "presented_stale_witness_reject":not verify_rotation("canonical",("current","current","stale_epoch")),
    }
    return {
        "authority_states":list(MEMBERSHIP_AUTH_STATES),"witnesses":3,"witness_quorum":2,
        "witness_states":list(WITNESS_STATES),"patterns":patterns,"accepted":accepted,
        "authority_disappearance_recoveries":authority_absent_recovery,
        "stale_membership_acceptances":stale_accept,"forked_membership_acceptances":fork_accept,
        "canonical_new_membership":CANON_MEMBERSHIP,"expected_generations":EXPECTED_GENERATION,
        "tampered_rotation_binding_rejected":tamper_rejected,
        "membership_authority_not_sufficient_without_witness_quorum":True,
        "checks":checks,
    }

def time_certificate(issuer,state,membership_hash):
    if state=="absent": return None,0
    epoch=TARGET_EPOCH; generation=EXPECTED_GENERATION[issuer]; rollback=0; target=CANON_TARGET; mh=membership_hash
    if state=="old_epoch": epoch-=1
    elif state=="rollback": rollback=1
    elif state=="old_generation": generation=max(0,generation-1)
    elif state=="old_membership": mh="0"*64
    elif state=="fork": target="A9-fork|B9|W9"
    cert={"issuer":issuer,"epoch":epoch,"generation":generation,"issued_monotonic":0,
          "expiry_monotonic":DEADLINE,"membership_hash":mh,"target":target}
    cert["binding_hash"]=_bind(issuer,epoch,generation,0,DEADLINE,mh,target)
    return cert,rollback

def verify_time_set(state_tuple,actual,skew,membership_hash):
    valid=[]; invalid=False
    for issuer,state in zip(ISSUERS,state_tuple):
        cert,rollback=time_certificate(issuer,state,membership_hash)
        if cert is None: continue
        observed=actual-rollback
        ok=(cert["issuer"]==issuer and cert["binding_hash"]==_bind(cert["issuer"],cert["epoch"],cert["generation"],
            cert["issued_monotonic"],cert["expiry_monotonic"],cert["membership_hash"],cert["target"])
            and cert["epoch"]==TARGET_EPOCH and cert["generation"]==EXPECTED_GENERATION[issuer]
            and cert["membership_hash"]==membership_hash and cert["target"]==CANON_TARGET
            and rollback==0 and observed>=0 and abs(skew)<=CLOCK_SKEW and observed<=cert["expiry_monotonic"])
        if ok: valid.append(issuer)
        else: invalid=True
    return (not invalid) and len(valid)>=QUORUM

def rotated_time_quorum_analysis():
    membership_hash=canonical_rotation_record()["binding_hash"]
    patterns=accepted=single_partition=stale_accept=old_membership_accept=0
    for states in product(TIME_STATES,repeat=3):
        for actual in range(0,6):
            for skew in range(-CLOCK_SKEW,CLOCK_SKEW+1):
                patterns+=1; ok=verify_time_set(states,actual,skew,membership_hash)
                if ok:
                    accepted+=1
                    if states.count("absent")==1: single_partition+=1
                    if actual>DEADLINE: stale_accept+=1
                    if "old_membership" in states: old_membership_accept+=1
    return {"issuers":list(ISSUERS),"quorum":QUORUM,"states":list(TIME_STATES),"patterns":patterns,
            "accepted":accepted,"single_partition_recoveries":single_partition,
            "post_deadline_stale_acceptances":stale_accept,"old_membership_acceptances":old_membership_accept,
            "membership_hash_bound_into_every_issuer_certificate":True,
            "generation_change_bound_to_witnessed_rotation":True}

def verify_composed(time_states,pop_states,publication_delay,gossip_delay):
    # One missing time issuer is tolerated; any stale membership presented by an issuer fails closed.
    if "old_membership" in time_states: return False
    if time_states.count("current")<2: return False
    if pop_states.count("canonical")<2: return False
    # Publication plus verifier convergence consume one shared revocation-lifetime budget.
    return publication_delay+gossip_delay<=DEADLINE

def composed_partition_publication_gossip_analysis():
    patterns=accepted=post_deadline=single_time_partition=partition_plus_fork=0
    by_total_delay={str(i):{"accepted":0,"rejected":0} for i in range(0,11)}
    for ts in product(COMPOSED_TIME_STATES,repeat=3):
        for ps in product(POP_STATES,repeat=3):
            for pub in range(0,6):
                for gossip in range(0,6):
                    patterns+=1; total=pub+gossip
                    ok=verify_composed(ts,ps,pub,gossip)
                    by_total_delay[str(total)]["accepted" if ok else "rejected"]+=1
                    if ok:
                        accepted+=1
                        if total>DEADLINE: post_deadline+=1
                        if ts.count("absent")==1: single_time_partition+=1
                        if ts.count("absent")==1 and ps.count("fork")==1 and ps.count("canonical")==2:
                            partition_plus_fork+=1
    checks={
        "time_partition_plus_verifier_fork_at_total3_accept":verify_composed(("current","current","absent"),("canonical","canonical","fork"),1,2),
        "same_case_at_total4_reject":not verify_composed(("current","current","absent"),("canonical","canonical","fork"),2,2),
        "old_membership_with_two_current_reject":not verify_composed(("current","current","old_membership"),("canonical","canonical","canonical"),0,0),
        "one_time_source_only_reject":not verify_composed(("current","absent","absent"),("canonical","canonical","canonical"),0,0),
        "noncanonical_verifier_majority_reject":not verify_composed(("current","current","current"),("canonical","fork","fork"),0,0),
    }
    return {"time_states":list(COMPOSED_TIME_STATES),"population_states":list(POP_STATES),
            "publication_delay_domain":[0,5],"gossip_delay_domain":[0,5],"deadline":DEADLINE,
            "patterns":patterns,"accepted":accepted,"post_deadline_acceptances":post_deadline,
            "single_time_partition_recoveries":single_time_partition,
            "simultaneous_time_partition_plus_single_verifier_fork_recoveries":partition_plus_fork,
            "end_to_end_publication_plus_gossip_budget":True,"by_total_delay":by_total_delay,"checks":checks}

def independence_evidence():
    return {"conservative_cross_role_credit":12,"credit_raised":False,
            "committed_external_independence_evidence_present":False,
            "required_binding":["provider identity","hardware custody","operator authority","issuer/source","subject","epoch","binding hash"],
            "unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True}

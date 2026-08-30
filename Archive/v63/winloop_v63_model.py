"""WinLoop V63 exact model: disjoint horizon-witness rotation, tombstone-preserving anchor compaction, and two-quarantine verifier recovery."""
from itertools import product
from math import ceil
import hashlib

V="V63"
BASE_DIGEST="66c617a9972e89c527e35beee814d16822326c6548c277462d00314748fb70c5"
BASE_IMPL_SHA="864db53ceae4a988db3eb2df78ebf067192cd5f11483767d01b6264ffb25b698"
DEADLINE=3

ROOTS=tuple([f"provenance_anchor_{i:02d}" for i in range(1,12)]+[
    "cloud_pam_identity_fabric","privileged_tenant_local","hsm_management_authority",
    "hsm_custody_local","hsm_issuance_rotation_local","operator_employment_iam",
    "operator_key_local","provider_build_ca_control","build_ca_local",
    "ca_key_ceremony_local","fabric_local_possession"
])

def B(*x):
    return hashlib.sha256("|".join(map(str,x)).encode()).hexdigest()

def prof():
    o={}; a=u=l=0
    for r in ROOTS:
        if r.startswith("provenance_anchor_"):
            a+=1; i=a; o[r]=(7+i%3,6+i%2,5+i%4)
        elif r.endswith("_local") or "possession" in r:
            l+=1; i=l; o[r]=(4+i%3,3+i%2,2+i%3)
        else:
            u+=1; i=u; o[r]=(5+i%2,4+i%3,3+i%2)
    return o

def opts(rate,h):
    d,p,c=rate; b={}
    for w in range(1,h+1):
        q=w-1
        for x in range(min(3,q)+1):
            for y in range(x,min(q,x+3)+1):
                b[w]=min(b.get(w,10**9),x*d+(y-x)*p+(q-y)*c)
    return b

def mincost(h,peak):
    R=len(ROOTS)
    if peak<ceil(R/h): return None
    S=0; W=1+R; T=W+h
    g=[[] for _ in range(T+1)]
    p=prof(); cs={r:opts(p[r],h) for r in ROOTS}
    def add(u,v,c,z):
        g[u].append([v,c,z,len(g[v])]); g[v].append([u,0,-z,len(g[u])-1])
    for i,r in enumerate(ROOTS):
        add(S,1+i,1,0)
        for w in range(1,h+1): add(1+i,W+w-1,1,cs[r][w])
    for w in range(1,h+1): add(W+w-1,T,peak,0)
    f=t=0; I=10**18
    while f<R:
        d=[I]*(T+1); pr=[None]*(T+1); d[S]=0
        for _ in range(T):
            changed=False
            for u in range(T+1):
                if d[u]>=I: continue
                for j,e in enumerate(g[u]):
                    v,c,z,_=e
                    if c and d[u]+z<d[v]:
                        d[v]=d[u]+z; pr[v]=(u,j); changed=True
            if not changed: break
        if pr[T] is None: return None
        v=T
        while v!=S:
            u,j=pr[v]; e=g[u][j]; e[1]-=1; g[v][e[3]][1]+=1; v=u
        f+=1; t+=d[T]
    return t

def temporal_floor_regression():
    a,b=mincost(22,1),mincost(11,2)
    return {
        "roots":22,"horizon":22,"floor":1,"budget":a,
        "h11_floor":2,"h11_budget":b,
        "v62_regression_preserved":(a,b)==(851,398),
        "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"
    }

# V62's long-horizon anchor is the committed predecessor. V63 rotates the witness
# set from B/C/D to a disjoint E/F/G set, so no overlap can self-bootstrap.
V62_ANCHOR="e5fd044225be5eaed9eb0b7ed3a59cc143803969859494656ed62fc70ed665a6"
V62_TRANSITION="27a2a0c64a47b9be61e5c437ba4582841a3238f148169cc765e36fbd41c59f46"
WO=("horizonWitnessB","horizonWitnessC","horizonWitnessD")
WN=("horizonWitnessE","horizonWitnessF","horizonWitnessG")
A13=B("long-horizon-anchor",13,V62_ANCHOR,"historyAnchorD,historyAnchorE,historyAnchorF","anchor-13")
WRT=B("horizon-witness-rotation",12,13,V62_TRANSITION,V62_ANCHOR,A13,",".join(WO),",".join(WN),"disjoint-dual-quorum")
TR=("canonical","cached_canonical","missing","stale_replay","fork")
WS=("live_current","cached_current","missing","stale_generation","fork")
PM=("all_online","old_provider_lost","new_provider_lost","one_source_each_lost","old_provider_fork","new_provider_fork")
RM=("pre_rotation_sources_online","all_pre_rotation_sources_lost_with_pin","all_pre_rotation_sources_lost_no_pin","new_anchor_only","root_fork")

def wrot_ok(r,o,n,pm,rm):
    if r not in TR[:2] or pm in PM[4:] or rm in RM[2:]:
        return False
    if any(x in WS[3:] for x in o+n):
        return False
    old_good=sum(x in WS[:2] for x in o)
    new_good=sum(x in WS[:2] for x in n)
    if old_good<2 or new_good<2:
        return False
    if pm==PM[1] and (sum(x==WS[1] for x in o)<2 or r!=TR[1]):
        return False
    if pm==PM[2] and (sum(x==WS[1] for x in n)<2 or r!=TR[1]):
        return False
    if pm==PM[3] and (WS[2] not in o or WS[2] not in n):
        return False
    if rm==RM[1] and r!=TR[1]:
        return False
    return True

def disjoint_horizon_witness_rotation_analysis():
    z=[0]*9
    for r in TR:
        for o in product(WS,repeat=3):
            for n in product(WS,repeat=3):
                for pm in PM:
                    for rm in RM:
                        z[0]+=1
                        ok=wrot_ok(r,o,n,pm,rm)
                        if ok:
                            z[1]+=1
                            z[2]+=pm==PM[1]
                            z[3]+=pm==PM[2]
                            z[4]+=(pm==PM[1] and rm==RM[1])
                            z[5]+=(pm==PM[2] and rm==RM[1])
                            z[6]+=r==TR[3] or any(x==WS[3] for x in o+n)
                            z[7]+=r==TR[4] or any(x==WS[4] for x in o+n) or pm in PM[4:] or rm==RM[4]
                            z[8]+=rm in RM[2:4]
    checks={
        "disjoint_sets":set(WO).isdisjoint(WN),
        "dual_quorum_accept":wrot_ok(TR[0],(WS[0],WS[0],WS[2]),(WS[0],WS[2],WS[0]),PM[0],RM[0]),
        "old_provider_plus_root_loss_cached_accept":wrot_ok(TR[1],(WS[1],WS[1],WS[2]),(WS[0],WS[0],WS[2]),PM[1],RM[1]),
        "new_provider_plus_root_loss_cached_accept":wrot_ok(TR[1],(WS[0],WS[0],WS[2]),(WS[1],WS[2],WS[1]),PM[2],RM[1]),
        "overlap_self_bootstrap_impossible":set(WO).isdisjoint(WN),
        "new_only_reject":not wrot_ok(TR[0],(WS[2],)*3,(WS[0],)*3,PM[0],RM[3]),
        "no_old_pin_reject":not wrot_ok(TR[1],(WS[1],WS[1],WS[2]),(WS[0],WS[0],WS[2]),PM[1],RM[2]),
        "stale_reject":not wrot_ok(TR[0],(WS[0],WS[3],WS[0]),(WS[0],)*3,PM[0],RM[0]),
        "fork_reject":not wrot_ok(TR[0],(WS[0],)*3,(WS[0],)*3,PM[4],RM[0]),
    }
    return {
        "patterns":z[0],"accepted":z[1],
        "old_provider_loss_recoveries":z[2],"new_provider_loss_recoveries":z[3],
        "old_provider_plus_root_source_loss_recoveries":z[4],
        "new_provider_plus_root_source_loss_recoveries":z[5],
        "stale_acceptances":z[6],"fork_acceptances":z[7],
        "new_only_or_unpinned_acceptances":z[8],
        "old_witness_set":list(WO),"new_witness_set":list(WN),
        "sets_disjoint":True,"quorum_each":2,
        "new_anchor":A13,"rotation_hash":WRT,"checks":checks
    }

# Multi-generation anchor compaction with deletion/tombstone proofs.  A tombstone
# carries the original revocation-deadline origin; later compaction never restarts it.
CP12=B("anchor-cp",12,V62_ANCHOR,V62_TRANSITION,"deadline-origin-12")
T12=B("anchor-tombstone",12,CP12,"preserve-live-revocation","deadline-origin-12")
CP13=B("anchor-cp",13,CP12,T12,A13,WRT,"deadline-origin-12")
T13=B("anchor-tombstone",13,CP13,T12,"preserve-live-revocation","deadline-origin-12")
CP14=B("anchor-cp",14,CP13,T13,"anchor-14","deadline-origin-12")
HS=("canonical","cached","missing","invalid")
CM=("full_history","compact_cp12","compact_cp13","tombstone12_missing","forked_compaction")
RV=("none","revoked_at12_live","revoked_at13_live","canonical_clear","stale_or_fork_clear")

def tomb_ok(s,d1,d2,d3,cm,rv):
    if d1+d2+d3>DEADLINE or cm==CM[4] or rv==RV[4]:
        return False
    if any(x==HS[3] for x in s) or s[4] not in HS[:2]:
        return False
    cp12,t12,cp13,t13,cp14=s
    if cm==CM[0] and any(x not in HS[:2] for x in s):
        return False
    if cm==CM[1]:
        if cp12!=HS[2] or t12 not in HS[:2] or cp13 not in HS[:2] or t13 not in HS[:2]:
            return False
    if cm==CM[2]:
        if cp12!=HS[2] or cp13!=HS[2] or t12 not in HS[:2] or t13 not in HS[:2]:
            return False
    if cm==CM[3]:
        return False
    if rv==RV[1] and (t12 not in HS[:2] or t13 not in HS[:2]):
        return False
    if rv==RV[2] and t13 not in HS[:2]:
        return False
    return True

def tombstone_anchor_history_analysis():
    z=[0]*10
    for s in product(HS,repeat=5):
        for d1 in range(4):
            for d2 in range(4):
                for d3 in range(4):
                    for cm in CM:
                        for rv in RV:
                            z[0]+=1
                            ok=tomb_ok(s,d1,d2,d3,cm,rv)
                            if ok:
                                z[1]+=1
                                z[2]+=d1+d2+d3>3
                                z[3]+=(d1<=3 and d2<=3 and d3<=3 and d1+d2+d3>3)
                                z[4]+=cm==CM[1]
                                z[5]+=cm==CM[2]
                                z[6]+=rv in RV[1:3]
                                z[7]+=(rv==RV[1] and (s[1] not in HS[:2] or s[3] not in HS[:2]))
                                z[8]+=rv==RV[4]
                                z[9]+=cm==CM[3]
    checks={
        "full_chain_accept":tomb_ok((HS[0],)*5,1,1,1,CM[0],RV[0]),
        "cp12_tombstone_compaction_accept":tomb_ok((HS[2],HS[0],HS[0],HS[0],HS[0]),1,1,1,CM[1],RV[1]),
        "cp13_tombstone_compaction_accept":tomb_ok((HS[2],HS[0],HS[2],HS[0],HS[0]),1,1,1,CM[2],RV[1]),
        "live_revocation_tombstone_erasure_reject":not tomb_ok((HS[2],HS[2],HS[2],HS[0],HS[0]),0,0,0,CM[2],RV[1]),
        "deadline_not_reset":not tomb_ok((HS[2],HS[0],HS[2],HS[0],HS[0]),2,1,1,CM[2],RV[1]),
        "stale_clear_reject":not tomb_ok((HS[0],)*5,0,0,0,CM[0],RV[4]),
        "missing_tombstone_reject":not tomb_ok((HS[0],HS[2],HS[0],HS[0],HS[0]),0,0,0,CM[3],RV[1]),
        "invalid_history_reject":not tomb_ok((HS[0],HS[3],HS[0],HS[0],HS[0]),0,0,0,CM[0],RV[0]),
    }
    return {
        "patterns":z[0],"accepted":z[1],
        "post_deadline_acceptances":z[2],"deadline_reset_acceptances":z[3],
        "cp12_tombstone_recoveries":z[4],"cp13_tombstone_recoveries":z[5],
        "live_revocation_recoveries":z[6],
        "live_revocation_erasure_acceptances":z[7],
        "stale_or_fork_clear_acceptances":z[8],
        "missing_tombstone_acceptances":z[9],
        "anchor_generations":3,"shared_deadline":3,
        "deadline_origin_preserved":"epoch12","checks":checks
    }

# Five verifier slots with a 3-of-5 threshold. Two quarantined slots can be
# tolerated only when three other trusted/current slots independently satisfy quorum.
VS=("canonical","cached_canonical","validated_join","quarantined","untrusted_join","invalid")
RC=("stable","threshold_reconfig","one_join","two_quarantine_reconfig","membership_fork")
HF=("full_history","threshold_3of5","cached_threshold_3of5","below_threshold")

def qok(s,rc,p,g,hf):
    if p+g>DEADLINE or rc==RC[4] or hf==HF[3] or VS[5] in s:
        return False
    if rc==RC[0] and VS[2] in s:
        return False
    if rc in RC[1:4] and VS[2] not in s:
        return False
    if rc==RC[2] and s.count(VS[2])<1:
        return False
    if rc==RC[3] and s.count(VS[3])<2:
        return False
    good=sum(x in VS[:2] or (x==VS[2] and rc in RC[1:4]) for x in s)
    if good<3:
        return False
    if hf==HF[2] and sum(x==VS[1] for x in s)<3:
        return False
    return True

def two_quarantine_verifier_reconfiguration_analysis():
    z=[0]*12
    for s in product(VS,repeat=5):
        for rc in RC:
            for p in range(4):
                for g in range(4):
                    for hf in HF:
                        z[0]+=1
                        ok=qok(s,rc,p,g,hf)
                        if ok:
                            z[1]+=1
                            z[2]+=p+g>3
                            z[3]+=s.count(VS[3])>=2
                            z[4]+=rc==RC[3]
                            z[5]+=VS[4] in s
                            z[6]+=VS[5] in s
                            z[7]+=rc==RC[4]
                            z[8]+=hf==HF[3]
                            z[9]+=p+g>0
                            z[10]+=VS[2] in s
                            trusted_good=sum(x in VS[:2] or (x==VS[2] and rc in RC[1:4]) for x in s)
                            z[11]+=trusted_good<3
    checks={
        "two_quarantine_reconfig_accept":qok((VS[0],VS[0],VS[2],VS[3],VS[3]),RC[3],1,2,HF[1]),
        "two_quarantine_without_third_good_reject":not qok((VS[0],VS[2],VS[3],VS[3],VS[4]),RC[3],0,0,HF[0]),
        "untrusted_join_not_counted":not qok((VS[0],VS[1],VS[4],VS[3],VS[3]),RC[3],0,0,HF[0]),
        "untrusted_join_present_but_ignored_accept":qok((VS[0],VS[1],VS[2],VS[3],VS[4]),RC[1],1,1,HF[1]),
        "membership_fork_reject":not qok((VS[0],VS[0],VS[0],VS[3],VS[3]),RC[4],0,0,HF[0]),
        "shared_deadline_reject":not qok((VS[0],VS[0],VS[2],VS[3],VS[3]),RC[3],2,2,HF[1]),
        "below_threshold_history_reject":not qok((VS[0],VS[0],VS[2],VS[3],VS[3]),RC[3],0,0,HF[3]),
        "invalid_state_reject":not qok((VS[0],VS[0],VS[2],VS[3],VS[5]),RC[1],0,0,HF[0]),
    }
    return {
        "patterns":z[0],"accepted":z[1],"quorum":3,"population_slots":5,
        "post_deadline_acceptances":z[2],
        "two_or_more_quarantine_recoveries":z[3],
        "explicit_two_quarantine_reconfig_recoveries":z[4],
        "untrusted_join_present_but_not_counted_recoveries":z[5],
        "invalid_state_acceptances":z[6],"membership_fork_acceptances":z[7],
        "below_threshold_history_acceptances":z[8],
        "delayed_recoveries":z[9],"validated_join_recoveries":z[10],
        "untrusted_join_quorum_credit_acceptances":z[11],
        "shared_deadline":3,"checks":checks
    }

def independence_evidence():
    return {
        "conservative_cross_role_credit":12,
        "credit_raised":False,
        "committed_external_independence_evidence_present":False,
        "disjoint_modeled_roles_are_not_external_independence_proof":True,
        "unknown_stale_cyclic_or_unbound_rejected":True,
        "signed_metadata_alone_insufficient":True
    }

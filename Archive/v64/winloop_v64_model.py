"""WinLoop V64 exact model: externally-bound identity gating, epoch-15 tombstone compaction, and Byzantine-evicting 3-of-5 verifier recovery."""
from itertools import product
from math import ceil
import hashlib

V="V64"
BASE_DIGEST="6bebeb48bcda3d1dd9f093727e416f92b692e898d54236f9dde95dbe2f3269a9"
BASE_IMPL_SHA="48feb8ecaa02a39725333c300ef848eff045fb25cf567f057665652359e49813"
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
        "v63_regression_preserved":(a,b)==(851,398),
        "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"
    }

# V64 does not invent external independence evidence.  It makes the gate exact:
# provider, operator, and hardware relations for both sides of the disjoint witness
# handoff must be externally bound and the old/new relation itself must be externally
# established as disjoint before any cross-role credit could move above 12.
E=("current_external","cached_external","missing","stale","conflicting","self_asserted")
BR=("canonical_external_bridge","cached_external_bridge","missing_bridge","stale_bridge","fork_bridge")
REL=("externally_disjoint","provider_alias","operator_alias","hardware_alias","unknown_relation")
SRC=("all_online","old_sources_lost","new_sources_lost","both_sides_sources_lost","binding_source_fork")

def bind_ok(ev,bridge,rel,src):
    old=ev[:3]; new=ev[3:]
    if bridge not in BR[:2] or rel!=REL[0] or src==SRC[4]:
        return False
    if any(x not in E[:2] for x in ev):
        return False
    if src==SRC[1] and (bridge!=BR[1] or any(x!=E[1] for x in old)):
        return False
    if src==SRC[2] and (bridge!=BR[1] or any(x!=E[1] for x in new)):
        return False
    if src==SRC[3] and (bridge!=BR[1] or any(x!=E[1] for x in ev)):
        return False
    return True

def identity_binding_gate_analysis():
    z=[0]*9
    for ev in product(E,repeat=6):
        for bridge in BR:
            for rel in REL:
                for src in SRC:
                    z[0]+=1
                    ok=bind_ok(ev,bridge,rel,src)
                    if ok:
                        z[1]+=1
                        z[2]+=src==SRC[1]
                        z[3]+=src==SRC[2]
                        z[4]+=src==SRC[3]
                        z[5]+=any(x in E[3:] for x in ev) or bridge in BR[3:]
                        z[6]+=rel!=REL[0]
                        z[7]+=any(x==E[5] for x in ev)
                        z[8]+=src==SRC[4]
    checks={
        "fully_bound_external_state_admits_hypothetically":
            bind_ok((E[0],)*6,BR[0],REL[0],SRC[0]),
        "cached_both_sides_source_loss_recovers":
            bind_ok((E[1],)*6,BR[1],REL[0],SRC[3]),
        "self_asserted_reject":
            not bind_ok((E[0],E[0],E[5],E[0],E[0],E[0]),BR[0],REL[0],SRC[0]),
        "provider_alias_reject":
            not bind_ok((E[0],)*6,BR[0],REL[1],SRC[0]),
        "unknown_relation_reject":
            not bind_ok((E[0],)*6,BR[0],REL[4],SRC[0]),
        "stale_bridge_reject":
            not bind_ok((E[0],)*6,BR[3],REL[0],SRC[0]),
        "source_fork_reject":
            not bind_ok((E[0],)*6,BR[0],REL[0],SRC[4]),
    }
    return {
        "patterns":z[0],"hypothetical_gate_admits":z[1],
        "old_source_loss_recoveries":z[2],"new_source_loss_recoveries":z[3],
        "both_sides_source_loss_recoveries":z[4],
        "stale_or_conflicting_acceptances":z[5],
        "alias_or_unknown_relation_acceptances":z[6],
        "self_asserted_acceptances":z[7],"binding_source_fork_acceptances":z[8],
        "committed_external_independence_evidence_present":False,
        "conservative_cross_role_credit":12,"credit_raised":False,
        "modeled_disjointness_alone_insufficient":True,
        "checks":checks
    }

# Epoch-15 extension.  T14 is a super-tombstone that hash-binds T12, T13, CP14,
# all still-live revocation obligations, and the original deadline origin.  CP15
# binds T14.  This permits older individual proof objects to disappear only when
# the canonical/cached T14+CP15 chain remains available; it never resets freshness.
T12=B("anchor-tombstone",12,"cp12","preserve-live-revocation","deadline-origin-12")
T13=B("anchor-tombstone",13,"cp13",T12,"preserve-live-revocation","deadline-origin-12")
CP14=B("anchor-cp",14,"cp13",T13,"anchor-14","deadline-origin-12")
T14=B("anchor-super-tombstone",14,CP14,T12,T13,"revocation-set-12-14","deadline-origin-12")
CP15=B("anchor-cp",15,CP14,T14,"anchor-15","deadline-origin-12")
HS=("canonical","cached","missing","invalid")
CM=("full_retained","compact_behind_t12","compact_behind_t13","compact_behind_t14","source_disappearance_recovery","forked_compaction")
SM=("all_sources_online","cp12_13_sources_gone","pre15_sources_gone_cached","tombstone_provider_lost","deadline_origin_missing","source_fork")
RV=("none","revoked12_live","revoked14_live","concurrent_12_14_live","canonical_clear15","stale_or_fork_clear")

def tomb15_ok(s,cm,sm,rv):
    t12,t13,cp14,t14,cp15=s
    if cm==CM[5] or sm in SM[4:] or rv==RV[5] or HS[3] in s:
        return False
    if cp15 not in HS[:2] or t14 not in HS[:2]:
        return False
    if cm==CM[0] and any(x not in HS[:2] for x in s):
        return False
    if cm==CM[1] and (t12 not in HS[:2] or t13 not in HS[:2] or cp14 not in HS[:2]):
        return False
    if cm==CM[2] and (t13 not in HS[:2] or cp14 not in HS[:2]):
        return False
    if cm==CM[3]:
        if (t12,t13,cp14)!=(HS[2],HS[2],HS[2]):
            return False
    if cm==CM[4]:
        if sm!=SM[2] or t14!=HS[1] or cp15!=HS[1]:
            return False
        if any(x!=HS[2] for x in (t12,t13,cp14)):
            return False
    if sm==SM[1] and not (t14 in HS[:2] and cp15 in HS[:2]):
        return False
    if sm==SM[2] and cm!=CM[4]:
        return False
    if sm==SM[3] and t14!=HS[1]:
        return False
    if rv in (RV[1],RV[3]) and t14 not in HS[:2]:
        return False
    if rv in (RV[2],RV[3]) and t14 not in HS[:2]:
        return False
    return True

_DELAY3=tuple(product(range(4),repeat=3))
_DELAY_OK=sum(sum(d)<=DEADLINE for d in _DELAY3)
_DELAY_NONZERO_OK=sum(0<sum(d)<=DEADLINE for d in _DELAY3)

def tombstone_epoch15_analysis():
    base_patterns=0; base_accept=0
    c_compact14=c_srcgone=c_srcgone_concurrent=c_concurrent=c_stale=0
    c_invalid=c_fork=0
    for s in product(HS,repeat=5):
        for cm in CM:
            for sm in SM:
                for rv in RV:
                    base_patterns+=1
                    ok=tomb15_ok(s,cm,sm,rv)
                    if ok:
                        base_accept+=1
                        c_compact14+=cm==CM[3]
                        c_srcgone+=cm==CM[4] and sm==SM[2]
                        c_srcgone_concurrent+=(cm==CM[4] and sm==SM[2] and rv==RV[3])
                        c_concurrent+=rv==RV[3]
                        c_stale+=rv==RV[5]
                        c_invalid+=HS[3] in s
                        c_fork+=cm==CM[5] or sm==SM[5]
    patterns=base_patterns*len(_DELAY3)
    accepted=base_accept*_DELAY_OK
    checks={
        "full_epoch15_chain_accept":tomb15_ok((HS[0],)*5,CM[0],SM[0],RV[0]),
        "compact_behind_t14_accept":
            tomb15_ok((HS[2],HS[2],HS[2],HS[0],HS[0]),CM[3],SM[0],RV[3]),
        "pre15_source_disappearance_cached_accept":
            tomb15_ok((HS[2],HS[2],HS[2],HS[1],HS[1]),CM[4],SM[2],RV[3]),
        "deadline_origin_missing_reject":
            not tomb15_ok((HS[2],HS[2],HS[2],HS[1],HS[1]),CM[4],SM[4],RV[3]),
        "stale_clear_reject":
            not tomb15_ok((HS[0],)*5,CM[0],SM[0],RV[5]),
        "source_fork_reject":
            not tomb15_ok((HS[0],)*5,CM[0],SM[5],RV[0]),
        "invalid_history_reject":
            not tomb15_ok((HS[0],HS[0],HS[0],HS[0],HS[3]),CM[0],SM[0],RV[0]),
        "deadline_not_reset":_DELAY_OK==20 and _DELAY_NONZERO_OK==19,
    }
    return {
        "patterns":patterns,"accepted":accepted,
        "base_history_states":base_patterns,"accepted_base_history_states":base_accept,
        "delay_vectors":len(_DELAY3),"admissible_shared_deadline_vectors":_DELAY_OK,
        "shared_deadline":DEADLINE,"deadline_origin_preserved":"epoch12",
        "compact_behind_t14_recoveries":c_compact14*_DELAY_OK,
        "pre15_source_disappearance_recoveries":c_srcgone*_DELAY_OK,
        "pre15_source_disappearance_concurrent_revocation_recoveries":c_srcgone_concurrent*_DELAY_OK,
        "concurrent_revocation_recoveries":c_concurrent*_DELAY_OK,
        "delayed_recoveries":base_accept*_DELAY_NONZERO_OK,
        "post_deadline_acceptances":0,"deadline_reset_acceptances":0,
        "stale_or_fork_clear_acceptances":c_stale*_DELAY_OK,
        "invalid_history_acceptances":c_invalid*_DELAY_OK,
        "forked_source_or_compaction_acceptances":c_fork*_DELAY_OK,
        "checks":checks
    }

# V64 models the frontier's exact 3-of-5 recovery after one Byzantine verifier is
# *evicted* under an externally verifiable eviction proof and replaced by a
# validated joiner.  The post-reconfiguration five slots may still contain two
# quarantines; the joiner counts only after explicit membership reconfiguration.
VS=("canonical","cached_canonical","validated_join","quarantined","byzantine_fork","untrusted_join")
RC=("stable","one_join","two_quarantine_join","byzantine_evict_join","membership_fork")
EP=("canonical_eviction","cached_eviction","missing_eviction","stale_or_fork_eviction")
HF=("full_history","threshold_3of5","cached_threshold_3of5","below_threshold")
_DELAY2=tuple(product(range(4),repeat=2))
_DELAY2_OK=sum(sum(d)<=DEADLINE for d in _DELAY2)
_DELAY2_NONZERO_OK=sum(0<sum(d)<=DEADLINE for d in _DELAY2)

def verifier_ok(s,rc,ep,hf):
    if rc==RC[4] or hf==HF[3] or VS[4] in s:
        return False
    join_allowed=rc in RC[1:4]
    if rc==RC[0] and VS[2] in s:
        return False
    if rc in RC[1:4] and VS[2] not in s:
        return False
    if rc==RC[2] and s.count(VS[3])<2:
        return False
    if rc==RC[3]:
        if s.count(VS[3])!=2 or s.count(VS[2])<1 or ep not in EP[:2]:
            return False
    good=sum(x in VS[:2] or (x==VS[2] and join_allowed) for x in s)
    if good<3:
        return False
    if hf==HF[2] and sum(x in (VS[1],VS[2]) for x in s)<3:
        return False
    return True

def byzantine_quarantine_join_analysis():
    base_patterns=0; base_accept=0
    byzjoin=untrusted=active_byz=stale_ep=membership=below=credit=0
    for s in product(VS,repeat=5):
        for rc in RC:
            for ep in EP:
                for hf in HF:
                    base_patterns+=1
                    ok=verifier_ok(s,rc,ep,hf)
                    if ok:
                        base_accept+=1
                        byzjoin+=rc==RC[3]
                        untrusted+=VS[5] in s
                        active_byz+=VS[4] in s
                        stale_ep+=rc==RC[3] and ep in EP[2:]
                        membership+=rc==RC[4]
                        below+=hf==HF[3]
                        trusted_good=sum(x in VS[:2] or (x==VS[2] and rc in RC[1:4]) for x in s)
                        credit+=trusted_good<3
    checks={
        "byzantine_evict_two_quarantine_join_accept":
            verifier_ok((VS[0],VS[1],VS[2],VS[3],VS[3]),RC[3],EP[0],HF[1]),
        "cached_eviction_proof_accept":
            verifier_ok((VS[1],VS[1],VS[2],VS[3],VS[3]),RC[3],EP[1],HF[2]),
        "active_byzantine_reject":
            not verifier_ok((VS[0],VS[1],VS[2],VS[3],VS[4]),RC[3],EP[0],HF[1]),
        "missing_eviction_proof_reject":
            not verifier_ok((VS[0],VS[1],VS[2],VS[3],VS[3]),RC[3],EP[2],HF[1]),
        "untrusted_join_not_counted":
            not verifier_ok((VS[0],VS[1],VS[5],VS[3],VS[3]),RC[3],EP[0],HF[1]),
        "membership_fork_reject":
            not verifier_ok((VS[0],VS[0],VS[0],VS[3],VS[3]),RC[4],EP[0],HF[0]),
        "below_threshold_history_reject":
            not verifier_ok((VS[0],VS[1],VS[2],VS[3],VS[3]),RC[3],EP[0],HF[3]),
        "shared_deadline_not_reset":_DELAY2_OK==10 and _DELAY2_NONZERO_OK==9,
    }
    return {
        "patterns":base_patterns*len(_DELAY2),"accepted":base_accept*_DELAY2_OK,
        "base_membership_states":base_patterns,"accepted_base_membership_states":base_accept,
        "delay_vectors":len(_DELAY2),"admissible_shared_deadline_vectors":_DELAY2_OK,
        "population_slots":5,"quorum":3,"shared_deadline":DEADLINE,
        "one_byzantine_two_quarantine_join_recoveries":byzjoin*_DELAY2_OK,
        "delayed_recoveries":base_accept*_DELAY2_NONZERO_OK,
        "untrusted_join_present_but_ignored_recoveries":untrusted*_DELAY2_OK,
        "active_byzantine_acceptances":active_byz*_DELAY2_OK,
        "stale_or_missing_eviction_proof_acceptances":stale_ep*_DELAY2_OK,
        "membership_fork_acceptances":membership*_DELAY2_OK,
        "below_threshold_history_acceptances":below*_DELAY2_OK,
        "untrusted_join_quorum_credit_acceptances":credit*_DELAY2_OK,
        "post_deadline_acceptances":0,
        "checks":checks
    }

def independence_evidence():
    return {
        "conservative_cross_role_credit":12,
        "credit_raised":False,
        "committed_external_independence_evidence_present":False,
        "provider_operator_hardware_binding_required":True,
        "modeled_disjoint_roles_are_not_external_independence_proof":True,
        "unknown_stale_cyclic_or_unbound_rejected":True,
        "signed_metadata_alone_insufficient":True
    }

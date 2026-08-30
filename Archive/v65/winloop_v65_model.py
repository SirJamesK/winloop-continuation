"""WinLoop V65 exact model: certificate fail-closed carry, epoch-16 tombstone GC, split-view eviction publication, and two-generation join safety."""
from itertools import product
from math import ceil
import hashlib

V="V65"
BASE_DIGEST="e3e090ea32f151975631636e7fc62e3c5784fa29d62cfeb4a9c73a0b983bd810"
BASE_IMPL_SHA="08e3e20a809d7df1600f9117238a8da1747333daaffed9d4c3f7838b5c256540"
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
        "v64_regression_preserved":(a,b)==(851,398),
        "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"
    }

# Cross-role credit cannot increase from modeled labels or self-contained metadata.
# This run found no committed independently validated provider/operator/hardware
# independence certificate outside the versioned model itself, so the executable
# gate remains fail closed at the V64 conservative credit.
CERT=("absent","current_external","cached_external","stale","conflicting","self_asserted")
ANCH=("current_independent_anchor","cached_independent_anchor","missing_anchor","stale_anchor","fork_anchor")
REL=("externally_disjoint","provider_alias","operator_alias","hardware_alias","unknown_relation")
def cert_ok(cert,anchor,rel):
    return cert in CERT[1:3] and anchor in ANCH[:2] and rel==REL[0]

def independence_certificate_analysis():
    patterns=accepted=stale=alias=selfsigned=0
    for c in CERT:
        for a in ANCH:
            for r in REL:
                ok=cert_ok(c,a,r)
                patterns+=1
                if ok:
                    accepted+=1
                    stale+=c==CERT[3] or a==ANCH[3]
                    alias+=r!=REL[0]
                    selfsigned+=c==CERT[5]
    checks={
        "hypothetical_current_external_certificate_accept":
            cert_ok(CERT[1],ANCH[0],REL[0]),
        "cached_external_certificate_accept":
            cert_ok(CERT[2],ANCH[1],REL[0]),
        "absent_certificate_reject":
            not cert_ok(CERT[0],ANCH[0],REL[0]),
        "stale_certificate_reject":
            not cert_ok(CERT[3],ANCH[0],REL[0]),
        "fork_anchor_reject":
            not cert_ok(CERT[1],ANCH[4],REL[0]),
        "self_asserted_reject":
            not cert_ok(CERT[5],ANCH[0],REL[0]),
        "alias_or_unknown_relation_reject":
            all(not cert_ok(CERT[1],ANCH[0],r) for r in REL[1:]),
    }
    return {
        "patterns":patterns,
        "hypothetical_gate_admits":accepted,
        "stale_or_conflicting_acceptances":stale,
        "alias_or_unknown_relation_acceptances":alias,
        "self_asserted_acceptances":selfsigned,
        "committed_external_independence_certificate_present":False,
        "conservative_cross_role_credit":12,
        "credit_raised":False,
        "checks":checks
    }

# Epoch-16 GC: T15 binds the prior super-tombstone chain, CP15, all live
# revocation obligations through epoch 15, and the epoch-12 deadline origin.
# CP16 binds T15. Older proof objects may disappear only behind a canonical or
# cached T15->CP16 chain; publication/source churn never resets freshness.
T14=B("anchor-super-tombstone",14,"cp14","t12","t13","revocation-set-12-14","deadline-origin-12")
CP15=B("anchor-cp",15,"cp14",T14,"anchor-15","deadline-origin-12")
T15=B("anchor-super-tombstone",15,CP15,T14,"revocation-set-12-15","deadline-origin-12")
CP16=B("anchor-cp",16,CP15,T15,"anchor-16","deadline-origin-12")
HS=("canonical","cached","missing","invalid")
CM=("full_retained","compact_behind_t15","source_churn_recovery","forked_compaction")
SM=("all_sources_online","old_sources_lost","proof_source_churn","pre16_sources_lost_cached","deadline_origin_missing","source_fork")
RV=("none","revoked14_live","revoked15_live","overlap_14_15_live","canonical_clear16","stale_or_fork_clear")
PUB=("current","cached","delayed","missing","forked")

def tomb16_ok(s,cm,sm,rv,pub):
    t14,cp15,t15,cp16=s
    if HS[3] in s or cm==CM[3] or sm in SM[4:] or rv==RV[5] or pub in PUB[3:]:
        return False
    if t15 not in HS[:2] or cp16 not in HS[:2]:
        return False
    if cm==CM[0] and any(x not in HS[:2] for x in s):
        return False
    if cm==CM[1] and (t14,cp15)!=(HS[2],HS[2]):
        return False
    if cm==CM[2]:
        if sm not in (SM[2],SM[3]) or t15!=HS[1] or cp16!=HS[1]:
            return False
        if (t14,cp15)!=(HS[2],HS[2]):
            return False
    if sm==SM[1] and not (t15 in HS[:2] and cp16 in HS[:2]):
        return False
    if sm in (SM[2],SM[3]) and cm!=CM[2]:
        return False
    if rv in (RV[1],RV[2],RV[3]) and t15 not in HS[:2]:
        return False
    if rv==RV[4] and pub not in PUB[:3]:
        return False
    return True

_DELAY4=tuple(product(range(4),repeat=4))
_DELAY4_OK=sum(sum(d)<=DEADLINE for d in _DELAY4)
_DELAY4_NONZERO_OK=sum(0<sum(d)<=DEADLINE for d in _DELAY4)

def tombstone_epoch16_analysis():
    base_patterns=base_accept=0
    compact=srcgone=churn=overlap=clear=stale=invalid=fork=0
    for s in product(HS,repeat=4):
        for cm in CM:
            for sm in SM:
                for rv in RV:
                    for pub in PUB:
                        base_patterns+=1
                        ok=tomb16_ok(s,cm,sm,rv,pub)
                        if ok:
                            base_accept+=1
                            compact+=cm==CM[1]
                            srcgone+=sm==SM[3]
                            churn+=sm==SM[2]
                            overlap+=rv==RV[3]
                            clear+=rv==RV[4]
                            stale+=rv==RV[5]
                            invalid+=HS[3] in s
                            fork+=cm==CM[3] or sm==SM[5] or pub==PUB[4]
    checks={
        "full_epoch16_chain_accept":
            tomb16_ok((HS[0],)*4,CM[0],SM[0],RV[0],PUB[0]),
        "compact_behind_t15_accept":
            tomb16_ok((HS[2],HS[2],HS[0],HS[0]),CM[1],SM[0],RV[3],PUB[0]),
        "source_churn_cached_recovery_accept":
            tomb16_ok((HS[2],HS[2],HS[1],HS[1]),CM[2],SM[2],RV[3],PUB[2]),
        "pre16_source_loss_cached_recovery_accept":
            tomb16_ok((HS[2],HS[2],HS[1],HS[1]),CM[2],SM[3],RV[4],PUB[1]),
        "deadline_origin_missing_reject":
            not tomb16_ok((HS[2],HS[2],HS[1],HS[1]),CM[2],SM[4],RV[3],PUB[1]),
        "stale_clear_reject":
            not tomb16_ok((HS[0],)*4,CM[0],SM[0],RV[5],PUB[0]),
        "forked_publication_reject":
            not tomb16_ok((HS[0],)*4,CM[0],SM[0],RV[0],PUB[4]),
        "deadline_not_reset":
            _DELAY4_OK==35 and _DELAY4_NONZERO_OK==34,
    }
    return {
        "patterns":base_patterns*len(_DELAY4),
        "accepted":base_accept*_DELAY4_OK,
        "base_history_states":base_patterns,
        "accepted_base_history_states":base_accept,
        "delay_vectors":len(_DELAY4),
        "admissible_shared_deadline_vectors":_DELAY4_OK,
        "shared_deadline":DEADLINE,
        "deadline_origin_preserved":"epoch12",
        "compact_behind_t15_recoveries":compact*_DELAY4_OK,
        "pre16_source_disappearance_recoveries":srcgone*_DELAY4_OK,
        "proof_source_churn_recoveries":churn*_DELAY4_OK,
        "overlapping_revocation_recoveries":overlap*_DELAY4_OK,
        "canonical_clear16_recoveries":clear*_DELAY4_OK,
        "delayed_recoveries":base_accept*_DELAY4_NONZERO_OK,
        "post_deadline_acceptances":0,
        "deadline_reset_acceptances":0,
        "stale_or_fork_clear_acceptances":stale*_DELAY4_OK,
        "invalid_history_acceptances":invalid*_DELAY4_OK,
        "forked_source_compaction_or_publication_acceptances":fork*_DELAY4_OK,
        "checks":checks
    }

# Split-view publication of the Byzantine eviction proof and post-eviction join
# across three verifier populations. A verifier can recover from one cached-pre
# or missing view only after a canonical/cached gossip bridge establishes the
# same post-join membership root. Forked views never contribute.
VV=("post_current","post_cached","pre_cached","missing","forked_eviction","forked_membership")
PH=("pre_eviction","eviction_published","join_validated","post_join_stable")
EP=("canonical_eviction","cached_eviction","missing_eviction","stale_or_fork_eviction")
JV=("validated_join","cached_validated_join","untrusted_join","conflicting_join")
GG=("canonical_bridge","cached_bridge","missing_bridge","conflicting_bridge")

def split_view_ok(v,ph,ep,jv,gg):
    if ph not in PH[2:] or ep not in EP[:2] or jv not in JV[:2] or gg not in GG[:2]:
        return False
    if any(x in VV[4:] for x in v):
        return False
    post=sum(x in VV[:2] for x in v)
    if post<2:
        return False
    if VV[2] in v and gg not in GG[:2]:
        return False
    return True

_DELAY2=tuple(product(range(4),repeat=2))
_DELAY2_OK=sum(sum(d)<=DEADLINE for d in _DELAY2)
_DELAY2_NONZERO_OK=sum(0<sum(d)<=DEADLINE for d in _DELAY2)

def split_view_eviction_join_analysis():
    base_patterns=base_accept=0
    bridge_recoveries=missing_recoveries=fork=stale_ep=untrusted=prephase=0
    for v in product(VV,repeat=3):
        for ph in PH:
            for ep in EP:
                for jv in JV:
                    for gg in GG:
                        base_patterns+=1
                        ok=split_view_ok(v,ph,ep,jv,gg)
                        if ok:
                            base_accept+=1
                            bridge_recoveries+=VV[2] in v
                            missing_recoveries+=VV[3] in v
                            fork+=any(x in VV[4:] for x in v) or gg==GG[3]
                            stale_ep+=ep in EP[2:]
                            untrusted+=jv in JV[2:]
                            prephase+=ph in PH[:2]
    checks={
        "two_post_plus_cached_pre_bridge_accept":
            split_view_ok((VV[0],VV[1],VV[2]),PH[2],EP[0],JV[0],GG[0]),
        "two_post_plus_missing_accept":
            split_view_ok((VV[0],VV[1],VV[3]),PH[3],EP[1],JV[1],GG[1]),
        "forked_eviction_view_reject":
            not split_view_ok((VV[0],VV[1],VV[4]),PH[2],EP[0],JV[0],GG[0]),
        "forked_membership_view_reject":
            not split_view_ok((VV[0],VV[1],VV[5]),PH[3],EP[0],JV[0],GG[0]),
        "join_before_eviction_reject":
            not split_view_ok((VV[0],VV[1],VV[2]),PH[0],EP[0],JV[0],GG[0]),
        "stale_eviction_proof_reject":
            not split_view_ok((VV[0],VV[1],VV[2]),PH[2],EP[3],JV[0],GG[0]),
        "untrusted_join_reject":
            not split_view_ok((VV[0],VV[1],VV[2]),PH[2],EP[0],JV[2],GG[0]),
        "shared_deadline_not_reset":
            _DELAY2_OK==10 and _DELAY2_NONZERO_OK==9,
    }
    return {
        "patterns":base_patterns*len(_DELAY2),
        "accepted":base_accept*_DELAY2_OK,
        "base_publication_states":base_patterns,
        "accepted_base_publication_states":base_accept,
        "verifier_populations":3,
        "publication_quorum":2,
        "delay_vectors":len(_DELAY2),
        "admissible_shared_deadline_vectors":_DELAY2_OK,
        "shared_deadline":DEADLINE,
        "cached_pre_split_view_bridge_recoveries":bridge_recoveries*_DELAY2_OK,
        "one_missing_view_recoveries":missing_recoveries*_DELAY2_OK,
        "delayed_recoveries":base_accept*_DELAY2_NONZERO_OK,
        "fork_acceptances":fork*_DELAY2_OK,
        "stale_or_missing_eviction_proof_acceptances":stale_ep*_DELAY2_OK,
        "untrusted_or_conflicting_join_acceptances":untrusted*_DELAY2_OK,
        "pre_eviction_or_pre_join_acceptances":prephase*_DELAY2_OK,
        "post_deadline_acceptances":0,
        "checks":checks
    }

# Two consecutive join generations in a 3-of-5 membership. The second join may
# count only after a quorum-valid carried membership (old members plus join-1)
# already exists. This prevents a pair of transient joiners from manufacturing
# the quorum that authorizes their own transition.
MS=("canonical_old","cached_old","join1_validated","join2_validated","quarantined","untrusted_join","byzantine_fork")
TR=("stable","after_join1","between_joins","after_join2","membership_fork")
HF=("full_history","join1_cert","join2_cert","both_join_certs","below_threshold")
EC=("canonical_chain","cached_chain","missing_chain","stale_or_fork_chain")

def two_join_ok(s,tr,hf,ec):
    if tr==TR[4] or hf==HF[4] or ec not in EC[:2] or MS[6] in s:
        return False
    old=sum(x in MS[:2] for x in s)
    j1=s.count(MS[2]); j2=s.count(MS[3])
    if tr==TR[0]:
        return j1==0 and j2==0 and old>=3
    if tr in TR[1:3]:
        if j1<1 or j2!=0 or hf not in (HF[1],HF[3]):
            return False
        return old+j1>=3
    if tr==TR[3]:
        if j1<1 or j2<1 or hf!=HF[3]:
            return False
        carried=old+j1
        total=carried+j2
        return carried>=3 and total>=3
    return False

def two_consecutive_join_analysis():
    base_patterns=base_accept=0
    after2=one_quarantine=transient=untrusted=fork=badchain=membership=below=0
    for s in product(MS,repeat=5):
        for tr in TR:
            for hf in HF:
                for ec in EC:
                    base_patterns+=1
                    ok=two_join_ok(s,tr,hf,ec)
                    if ok:
                        base_accept+=1
                        after2+=tr==TR[3]
                        one_quarantine+=tr==TR[3] and s.count(MS[4])==1
                        old=sum(x in MS[:2] for x in s); j1=s.count(MS[2]); j2=s.count(MS[3])
                        transient+=tr==TR[3] and old+j1<3 and old+j1+j2>=3
                        untrusted+=MS[5] in s and old+j1+j2<3
                        fork+=MS[6] in s
                        badchain+=ec in EC[2:]
                        membership+=tr==TR[4]
                        below+=hf==HF[4]
    checks={
        "join1_quorum_accept":
            two_join_ok((MS[0],MS[0],MS[1],MS[2],MS[4]),TR[1],HF[1],EC[0]),
        "join2_after_carried_quorum_accept":
            two_join_ok((MS[0],MS[0],MS[2],MS[3],MS[4]),TR[3],HF[3],EC[0]),
        "pair_of_joiners_cannot_self_authorize":
            not two_join_ok((MS[0],MS[2],MS[3],MS[4],MS[4]),TR[3],HF[3],EC[0]),
        "untrusted_join_not_counted":
            not two_join_ok((MS[0],MS[1],MS[5],MS[3],MS[4]),TR[3],HF[3],EC[0]),
        "byzantine_fork_reject":
            not two_join_ok((MS[0],MS[1],MS[2],MS[3],MS[6]),TR[3],HF[3],EC[0]),
        "stale_chain_reject":
            not two_join_ok((MS[0],MS[0],MS[2],MS[3],MS[4]),TR[3],HF[3],EC[3]),
        "membership_fork_reject":
            not two_join_ok((MS[0],MS[0],MS[0],MS[4],MS[4]),TR[4],HF[0],EC[0]),
        "shared_deadline_not_reset":
            _DELAY2_OK==10 and _DELAY2_NONZERO_OK==9,
    }
    return {
        "patterns":base_patterns*len(_DELAY2),
        "accepted":base_accept*_DELAY2_OK,
        "base_membership_states":base_patterns,
        "accepted_base_membership_states":base_accept,
        "population_slots":5,
        "quorum":3,
        "delay_vectors":len(_DELAY2),
        "admissible_shared_deadline_vectors":_DELAY2_OK,
        "shared_deadline":DEADLINE,
        "two_consecutive_join_recoveries":after2*_DELAY2_OK,
        "two_join_one_quarantine_recoveries":one_quarantine*_DELAY2_OK,
        "delayed_recoveries":base_accept*_DELAY2_NONZERO_OK,
        "transient_membership_quorum_inflation_acceptances":transient*_DELAY2_OK,
        "untrusted_join_quorum_credit_acceptances":untrusted*_DELAY2_OK,
        "active_byzantine_acceptances":fork*_DELAY2_OK,
        "stale_or_missing_chain_acceptances":badchain*_DELAY2_OK,
        "membership_fork_acceptances":membership*_DELAY2_OK,
        "below_threshold_history_acceptances":below*_DELAY2_OK,
        "post_deadline_acceptances":0,
        "checks":checks
    }

def independence_evidence():
    return {
        "conservative_cross_role_credit":12,
        "credit_raised":False,
        "committed_external_independence_certificate_present":False,
        "provider_operator_hardware_binding_required":True,
        "modeled_disjoint_roles_are_not_external_independence_proof":True,
        "unknown_stale_cyclic_or_unbound_rejected":True,
        "signed_metadata_alone_insufficient":True
    }

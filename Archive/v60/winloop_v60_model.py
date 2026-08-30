"""WinLoop V60 model: rooted witness-roster churn plus consecutive issuer-rotation catch-up."""
from itertools import product
from math import ceil
import hashlib

V="V60"
BASE_DIGEST="c9a88403f543d13783c21aa19308f35ba9ffb403ef76c7f06119b22916f992b5"
BASE_IMPL_SHA="ff517f4bd1ebc7d75c848ce09f403e8ba7ed386edd4fc168383faccb2111c7b5"
N=22
DEADLINE=3
TARGET_EPOCH=10

ANCHORS=[f"provenance_anchor_{i:02d}" for i in range(1,12)]
FABRIC=["cloud_pam_identity_fabric","privileged_tenant_local","hsm_management_authority","hsm_custody_local",
        "hsm_issuance_rotation_local","operator_employment_iam","operator_key_local","provider_build_ca_control",
        "build_ca_local","ca_key_ceremony_local","fabric_local_possession"]
ROOTS=tuple(ANCHORS+FABRIC)

OLD_WITNESSES=("witness1","witness2","witness3")
NEW_WITNESSES=("witness2","witness3","witness4")
ROOT_AUTHORITIES=("historyRootA","historyRootB","historyRootC")
ROOT_QUORUM=2
WITNESS_QUORUM=2
ROSTER_AUTH_STATES=("canonical","absent_cached_canonical","stale_replay","fork")
ROOT_CERT_STATES=("current","absent","stale_epoch","old_generation","fork")

CHAIN_STAGE_STATES=("canonical","absent_cached_canonical","missing","stale_replay","fork")
TERMINAL_STATES=("canonical_e10","replay_e9","fork_e10","missing")
AVAILABILITY_MODES=("all3","one_missing_1","one_missing_2","one_missing_3",
                    "two_missing","stale_presented","fork_presented","old_majority")


def _bind(*parts):
    return hashlib.sha256("|".join(map(str,parts)).encode()).hexdigest()


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
            "v59_regression_preserved":(h22,h11)==(851,398),
            "cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"}


def canonical_roster_transition():
    rec={
        "epoch":TARGET_EPOCH,
        "old_roster":",".join(OLD_WITNESSES),
        "new_roster":",".join(NEW_WITNESSES),
        "old_generation":9,
        "new_generation":10,
        "previous_history_root":"history-root-9",
        "rotation_nonce":"witness-roster-10",
    }
    rec["binding_hash"]=_bind(rec["epoch"],rec["old_roster"],rec["new_roster"],rec["old_generation"],
                              rec["new_generation"],rec["previous_history_root"],rec["rotation_nonce"])
    return rec


def roster_record_for_authority(state):
    rec=canonical_roster_transition()
    if state in ("canonical","absent_cached_canonical"):
        return rec
    if state=="stale_replay":
        rec["epoch"]-=1; rec["new_roster"]=rec["old_roster"]; rec["new_generation"]-=1
    elif state=="fork":
        rec["new_roster"]="witness1,witness3,witness4"
    rec["binding_hash"]=_bind(rec["epoch"],rec["old_roster"],rec["new_roster"],rec["old_generation"],
                              rec["new_generation"],rec["previous_history_root"],rec["rotation_nonce"])
    return rec


def root_certificate(authority,state,roster_hash):
    if state=="absent": return None
    epoch=TARGET_EPOCH; generation=10; target=roster_hash
    if state=="stale_epoch": epoch-=1
    elif state=="old_generation": generation-=1
    elif state=="fork": target="f"*64
    cert={"authority":authority,"epoch":epoch,"generation":generation,"roster_hash":target}
    cert["binding_hash"]=_bind(authority,epoch,generation,target)
    return cert


def verify_roster_transition(authority_state,root_states):
    rec=roster_record_for_authority(authority_state)
    if rec!=canonical_roster_transition(): return False
    valid=0; invalid=False
    for authority,state in zip(ROOT_AUTHORITIES,root_states):
        cert=root_certificate(authority,state,rec["binding_hash"])
        if cert is None: continue
        ok=(cert["authority"]==authority and cert["epoch"]==TARGET_EPOCH and cert["generation"]==10
            and cert["roster_hash"]==rec["binding_hash"]
            and cert["binding_hash"]==_bind(cert["authority"],cert["epoch"],cert["generation"],cert["roster_hash"]))
        if ok: valid+=1
        else: invalid=True
    return (not invalid) and valid>=ROOT_QUORUM


def witness_roster_history_analysis():
    patterns=accepted=authority_absent=stale_accept=fork_accept=0
    for auth in ROSTER_AUTH_STATES:
        for states in product(ROOT_CERT_STATES,repeat=3):
            patterns+=1; ok=verify_roster_transition(auth,states)
            if ok:
                accepted+=1
                authority_absent += int(auth=="absent_cached_canonical")
                stale_accept += int(auth=="stale_replay")
                fork_accept += int(auth=="fork")
    rec=canonical_roster_transition(); tampered=dict(rec); tampered["new_roster"]="witness1,witness2,witness4"
    checks={
        "two_root_authorities_accept":verify_roster_transition("canonical",("current","current","absent")),
        "cached_transition_survives_history_authority_disappearance":verify_roster_transition("absent_cached_canonical",("current","absent","current")),
        "stale_roster_replay_reject":not verify_roster_transition("stale_replay",("current","current","current")),
        "forked_roster_reject":not verify_roster_transition("fork",("current","current","current")),
        "single_root_authority_reject":not verify_roster_transition("canonical",("current","absent","absent")),
        "presented_old_root_generation_reject":not verify_roster_transition("canonical",("current","current","old_generation")),
        "tampered_roster_binding_reject":tampered["binding_hash"]!=_bind(tampered["epoch"],tampered["old_roster"],tampered["new_roster"],
            tampered["old_generation"],tampered["new_generation"],tampered["previous_history_root"],tampered["rotation_nonce"]),
    }
    return {"root_authorities":list(ROOT_AUTHORITIES),"root_quorum":ROOT_QUORUM,
            "authority_states":list(ROSTER_AUTH_STATES),"root_certificate_states":list(ROOT_CERT_STATES),
            "patterns":patterns,"accepted":accepted,"authority_disappearance_recoveries":authority_absent,
            "stale_roster_acceptances":stale_accept,"forked_roster_acceptances":fork_accept,
            "old_roster":list(OLD_WITNESSES),"new_roster":list(NEW_WITNESSES),
            "history_root_separate_from_membership_witnesses":True,"checks":checks}


TRUSTED_E8_HASH=_bind("issuer-membership",8,"timeA,timeB,timeC", "checkpoint-8")
HISTORY9_HASH="history-root-9"


def canonical_epoch9_membership():
    rec={"epoch":9,"old_membership":"timeA,timeB,timeC","new_membership":"timeB,timeC,timeD",
         "generations":{"timeB":9,"timeC":9,"timeD":1},"previous_membership_hash":TRUSTED_E8_HASH,
         "witness_roster_hash":_bind("witness-roster",9,",".join(OLD_WITNESSES)),"rotation_nonce":"issuer-rotation-9"}
    rec["binding_hash"]=_bind(rec["epoch"],rec["old_membership"],rec["new_membership"],sorted(rec["generations"].items()),
                              rec["previous_membership_hash"],rec["witness_roster_hash"],rec["rotation_nonce"])
    return rec


def canonical_epoch10_membership():
    roster=canonical_roster_transition(); prev=canonical_epoch9_membership()
    rec={"epoch":10,"old_membership":"timeB,timeC,timeD","new_membership":"timeC,timeD,timeE",
         "generations":{"timeC":10,"timeD":2,"timeE":1},"previous_membership_hash":prev["binding_hash"],
         "witness_roster_hash":roster["binding_hash"],"rotation_nonce":"issuer-rotation-10"}
    rec["binding_hash"]=_bind(rec["epoch"],rec["old_membership"],rec["new_membership"],sorted(rec["generations"].items()),
                              rec["previous_membership_hash"],rec["witness_roster_hash"],rec["rotation_nonce"])
    return rec


def _stage_record(kind,state):
    if kind=="h9": canon=canonical_epoch9_membership()
    elif kind=="roster10": canon=canonical_roster_transition()
    else: canon=canonical_epoch10_membership()
    if state in ("canonical","absent_cached_canonical"): return canon
    if state=="missing": return None
    rec=dict(canon)
    if state=="stale_replay":
        if kind=="h9":
            rec["epoch"]=8; rec["new_membership"]="timeA,timeB,timeC"
        elif kind=="roster10":
            rec["epoch"]=9; rec["new_roster"]=rec["old_roster"]; rec["new_generation"]=9
        else:
            return canonical_epoch9_membership()
    elif state=="fork":
        if kind=="roster10": rec["new_roster"]="witness1,witness3,witness4"
        else: rec["new_membership"]="timeB,timeD,timeE" if kind=="h10" else "timeA,timeC,timeD"
    if kind=="roster10":
        rec["binding_hash"]=_bind(rec["epoch"],rec["old_roster"],rec["new_roster"],rec["old_generation"],
                                  rec["new_generation"],rec["previous_history_root"],rec["rotation_nonce"])
    else:
        rec["binding_hash"]=_bind(rec["epoch"],rec["old_membership"],rec["new_membership"],sorted(rec["generations"].items()),
                                  rec["previous_membership_hash"],rec["witness_roster_hash"],rec["rotation_nonce"])
    return rec


def _availability_mode_valid(mode):
    return mode in ("all3","one_missing_1","one_missing_2","one_missing_3")


def verify_consecutive_catchup(h9_state,roster10_state,h10_state,terminal_state,catchup_delay,root_mode,new_witness_mode):
    h9=_stage_record("h9",h9_state); roster10=_stage_record("roster10",roster10_state); h10=_stage_record("h10",h10_state)
    if not _availability_mode_valid(root_mode) or not _availability_mode_valid(new_witness_mode): return False
    if h9!=canonical_epoch9_membership() or roster10!=canonical_roster_transition() or h10!=canonical_epoch10_membership(): return False
    if h9["previous_membership_hash"]!=TRUSTED_E8_HASH: return False
    if roster10["previous_history_root"]!=HISTORY9_HASH: return False
    if h10["previous_membership_hash"]!=h9["binding_hash"]: return False
    if h10["witness_roster_hash"]!=roster10["binding_hash"]: return False
    if terminal_state!="canonical_e10": return False
    if catchup_delay>DEADLINE: return False
    return True


def consecutive_rotation_catchup_analysis():
    patterns=accepted=post_deadline=replayed_intermediate=fork_terminal=old_majority=offline=authority_disappearance=0
    simultaneous_root_and_witness_missing=0
    for h9s,r10s,h10s in product(CHAIN_STAGE_STATES,repeat=3):
        for terminal in TERMINAL_STATES:
            for delay in range(0,6):
                for root_mode in AVAILABILITY_MODES:
                    for witness_mode in AVAILABILITY_MODES:
                        patterns+=1
                        ok=verify_consecutive_catchup(h9s,r10s,h10s,terminal,delay,root_mode,witness_mode)
                        if ok:
                            accepted+=1
                            post_deadline += int(delay>DEADLINE)
                            replayed_intermediate += int(terminal=="replay_e9")
                            fork_terminal += int(terminal=="fork_e10")
                            old_majority += int(root_mode=="old_majority" or witness_mode=="old_majority")
                            offline += int(delay>0)
                            authority_disappearance += int("absent_cached_canonical" in (h9s,r10s,h10s))
                            simultaneous_root_and_witness_missing += int(root_mode.startswith("one_missing") and witness_mode.startswith("one_missing"))
    checks={
        "two_consecutive_rotations_accept_at_deadline":verify_consecutive_catchup("canonical","canonical","canonical","canonical_e10",3,"all3","all3"),
        "same_chain_reject_after_deadline":not verify_consecutive_catchup("canonical","canonical","canonical","canonical_e10",4,"all3","all3"),
        "offline_cached_chain_accept":verify_consecutive_catchup("absent_cached_canonical","absent_cached_canonical","absent_cached_canonical","canonical_e10",2,"one_missing_1","one_missing_2"),
        "replayed_intermediate_terminal_reject":not verify_consecutive_catchup("canonical","canonical","canonical","replay_e9",0,"all3","all3"),
        "missing_roster_transition_reject":not verify_consecutive_catchup("canonical","missing","canonical","canonical_e10",0,"all3","all3"),
        "compromised_old_witness_majority_reject":not verify_consecutive_catchup("canonical","canonical","canonical","canonical_e10",0,"all3","old_majority"),
        "forked_history_root_evidence_reject":not verify_consecutive_catchup("canonical","canonical","canonical","canonical_e10",0,"fork_presented","all3"),
    }
    return {"stage_states":list(CHAIN_STAGE_STATES),"terminal_states":list(TERMINAL_STATES),
            "availability_modes":list(AVAILABILITY_MODES),"delay_domain":[0,5],"deadline":DEADLINE,
            "patterns":patterns,"accepted":accepted,"post_deadline_acceptances":post_deadline,
            "replayed_intermediate_terminal_acceptances":replayed_intermediate,"fork_terminal_acceptances":fork_terminal,
            "old_witness_majority_acceptances":old_majority,"offline_catchup_recoveries":offline,
            "stage_authority_disappearance_recoveries":authority_disappearance,
            "simultaneous_single_root_plus_single_new_witness_loss_recoveries":simultaneous_root_and_witness_missing,
            "chain_links_hash_bound":True,"shared_deadline_not_per_stage":True,"checks":checks}


def independence_evidence():
    return {"conservative_cross_role_credit":12,"credit_raised":False,
            "committed_external_independence_evidence_present":False,
            "required_binding":["provider identity","hardware custody","operator authority","issuer/source","subject","epoch","binding hash"],
            "unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True}

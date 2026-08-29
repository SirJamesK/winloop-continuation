"""WinLoop V45: monotonic revocation, log-consistency, quorum rotation, and robust temporal cost."""
from __future__ import annotations
from dataclasses import dataclass, replace
from math import ceil
import hashlib, json

VERSION="V45"; JOINT_FLOOR=21; LOWER_FLOOR=60; NONENDPOINT_FLOOR=22
COST={"lower":3,"nominal":4,"upper":6}; LOGS=("log_alpha","log_beta")
ENDPOINT={f"endpoint_{i:02d}" for i in range(1,22)}
ANCHORS={f"provenance_anchor_{i:02d}" for i in range(1,12)}
CAP={
 "privileged_tenancy":("cloud_pam_identity_fabric","privileged_tenant_local"),
 "hsm_management":("cloud_pam_identity_fabric","hsm_management_authority","hsm_custody_local","hsm_issuance_rotation_local"),
 "operator_admin":("cloud_pam_identity_fabric","operator_employment_iam","operator_key_local"),
 "provider_build_ca":("provider_build_ca_control","build_ca_local","ca_key_ceremony_local"),
 "fabric_local_possession_capability":("fabric_local_possession",),
 "common_privileged_fabric":("privileged_tenancy","hsm_management","operator_admin","provider_build_ca","fabric_local_possession_capability"),
}
ROUTES={
 "recursive_common_fabric":tuple(sorted(ANCHORS))+("common_privileged_fabric",),
 "downstream_pam_plane":tuple(sorted(ANCHORS))+("common_privileged_fabric","downstream_pam_plane_local"),
 "issuance_ceremony":tuple(sorted(ANCHORS))+("common_privileged_fabric","issuance_ceremony_local"),
}
class GraphError(ValueError): pass

def expand(sym,stack=()):
 if sym in stack: raise GraphError("cycle")
 if sym not in CAP:
  if sym.startswith("cap:") or sym.endswith("_capability"): raise GraphError("unknown")
  return {sym}
 out=set()
 for dep in CAP[sym]: out|=expand(dep,stack+(sym,))
 return out

def route_roots(route):
 out=set()
 for s in route: out|=expand(s)
 return out

def metrics(roots):
 n=len(roots); return {"root_count":n,"lower_cost":3*n,"nominal_cost":4*n,"upper_cost":6*n}

def static(alias=None):
 alias=alias or {}; canon=lambda roots:{alias.get(r,r) for r in roots}
 ep=metrics(canon(ENDPOINT)); ne={n:metrics(canon(route_roots(r))) for n,r in ROUTES.items()}
 win=min(ne,key=lambda n:(ne[n]["root_count"],n)); pc=ne[win]["root_count"]; jc=min(ep["root_count"],pc); low=3*jc
 ok=jc>=JOINT_FLOOR and low>=LOWER_FLOOR and all(x["root_count"]>=NONENDPOINT_FLOOR for x in ne.values())
 return {"joint_cut":jc,"provenance_cut":pc,"joint_lower_cost":low,"admitted":ok,"nonendpoint_winner":win,"nonendpoint":ne}

@dataclass(frozen=True)
class Policy:
 root:str; seats:tuple[str,str,str]=("seat1","seat2","seat3"); quorum:int=2; max_age:int=1; domain:str=""

def primitive_roots():
 out=set()
 for r in ROUTES.values(): out|=route_roots(r)
 return sorted(out)

def policies():
 strict={"ca_key_ceremony_local","hsm_issuance_rotation_local","issuance_ceremony_local"}
 return {r:Policy(r,max_age=0 if r in strict else 1,domain=f"control::{r}") for r in primitive_roots()}

def key_id(root,seat,generation,principal): return f"key::{root}::{seat}::g{generation}::{principal}"

def default_keysets(ps):
 out={}
 for root,p in ps.items():
  rows=[]
  for seat in p.seats:
   principal=f"member::{root}::{seat}"; rows.append({"seat":seat,"principal":principal,"generation":1,"key":key_id(root,seat,1,principal),"valid_from":0,"valid_through":None})
  out[root]=rows
 return out

def rotate_seat(keysets,root,seat,epoch,overlap=0,replacement=False):
 rows=keysets[root]; old=max((x for x in rows if x["seat"]==seat),key=lambda x:x["generation"]); old["valid_through"]=epoch+overlap
 generation=old["generation"]+1; principal=(f"replacement::{root}::{seat}::g{generation}" if replacement else old["principal"])
 new={"seat":seat,"principal":principal,"generation":generation,"key":key_id(root,seat,generation,principal),"valid_from":epoch,"valid_through":None}; rows.append(new); return old,new

def active_key(row,epoch): return row["valid_from"]<=epoch and (row["valid_through"] is None or epoch<=row["valid_through"])
def canonical_event(e): return json.dumps(e,sort_keys=True,separators=(",",":"))
def validate_ledger(events): return all(int(e.get("seq",-1))==i+1 for i,e in enumerate(events))

def ledger_root(events,size):
 if size<0 or size>len(events) or not validate_ledger(events): raise ValueError("invalid ledger")
 h=hashlib.sha256(b"V45-ledger-genesis").digest()
 for e in events[:size]: h=hashlib.sha256(h+canonical_event(e).encode()).digest()
 return h.hex()

def empty_state():
 g=ledger_root([],0); return {"log_sizes":{l:0 for l in LOGS},"log_roots":{l:g for l in LOGS},"revoked_keys":[]}

def state_at(events,size,now):
 root=ledger_root(events,size); revoked=sorted({e["key"] for e in events[:size] if e.get("type")=="revoke_key" and int(e.get("effective",10**9))<=now})
 return {"log_sizes":{l:size for l in LOGS},"log_roots":{l:root for l in LOGS},"revoked_keys":revoked}

def receipt(events,size,published,consumed,prior_size,prior_root):
 return {"tree_size":size,"root":ledger_root(events,size),"published":published,"consumed":consumed,"consistency_from":prior_size,"consistency_from_root":prior_root}

def seal(root,key,seat,principal,epoch,domain): return hashlib.sha256(f"V45|{root}|{key}|{seat}|{principal}|{epoch}|{domain}".encode()).hexdigest()

def statement(p,row,epoch,events,state,sizes=None,consumed=None):
 sizes=sizes or {l:len(events) for l in LOGS}; consumed=consumed or {l:epoch for l in LOGS}; s=seal(p.root,row["key"],row["seat"],row["principal"],epoch,p.domain); logs={}
 for l in LOGS: logs[l]=receipt(events,int(sizes[l]),epoch,int(consumed[l]),int(state["log_sizes"][l]),state["log_roots"][l])
 return {"root":p.root,"seat":row["seat"],"principal":row["principal"],"key":row["key"],"epoch":epoch,"domain":p.domain,"seal":s,"logs":logs}

def snapshot(ps,epoch,keysets,events,state=None,sizes=None,consumed=None):
 state=state or empty_state(); return {r:[statement(p,row,epoch,events,state,sizes,consumed) for row in keysets[r] if active_key(row,epoch)] for r,p in ps.items()}

def key_record(keysets,root,key):
 for row in keysets[root]:
  if row["key"]==key: return row
 return None

def verify_logs(x,events,state,now):
 if not validate_ledger(events): return None
 views={}
 try:
  for l in LOGS:
   q=x.get("logs",{}).get(l)
   if not q: return None
   size=int(q["tree_size"]); pub=int(q["published"]); con=int(q["consumed"])
   if size<0 or size>len(events) or pub>now or con<pub or con>now: return None
   root=ledger_root(events,size)
   if q["root"]!=root: return None
   old_size=int(state["log_sizes"].get(l,0)); old_root=state["log_roots"].get(l,ledger_root(events,0))
   if size<old_size: return None
   if size==old_size:
    if root!=old_root: return None
   else:
    if int(q.get("consistency_from",-1))!=old_size or q.get("consistency_from_root")!=old_root: return None
    if old_size>len(events) or ledger_root(events,old_size)!=old_root: return None
   views[l]=(size,root)
  a,b=views[LOGS[0]],views[LOGS[1]]; lo,hi=(a,b) if a[0]<=b[0] else (b,a)
  if ledger_root(events,lo[0])!=lo[1] or ledger_root(events,hi[0])!=hi[1]: return None
  return max(a[0],b[0])
 except Exception: return None

def revoked(key,events,size,now,state):
 if key in set(state.get("revoked_keys",[])): return True
 return any(e.get("type")=="revoke_key" and e.get("key")==key and int(e.get("effective",10**9))<=now for e in events[:size])

def verify_root(root,items,p,now,keysets,events,state):
 good=set()
 for x in items:
  try:
   if x["root"]!=root or x["domain"]!=p.domain or x["seat"] not in p.seats: continue
   row=key_record(keysets,root,x["key"])
   if not row or row["seat"]!=x["seat"] or row["principal"]!=x["principal"] or not active_key(row,int(x["epoch"])): continue
   e=int(x["epoch"]); age=now-e
   if age<0 or age>p.max_age: continue
   if x["seal"]!=seal(root,x["key"],x["seat"],x["principal"],e,p.domain): continue
   max_size=verify_logs(x,events,state,now)
   if max_size is None or revoked(x["key"],events,max_size,now,state): continue
   good.add(x["seat"])
  except Exception: pass
 return len(good)>=p.quorum

def verify_snapshot(s,ps,now,keysets,events,state): return all(verify_root(r,s.get(r,[]),p,now,keysets,events,state) for r,p in ps.items())

def evidence_static(ps,s,now,keysets,events,state):
 if not verify_snapshot(s,ps,now,keysets,events,state): return {"evidence_accepted":False,"admitted":False}
 x=static({r:p.domain for r,p in ps.items()}); return {"evidence_accepted":True,**{k:x[k] for k in ("joint_cut","provenance_cut","joint_lower_cost","admitted")}}

def revocation_rotation_tests():
 ps=policies(); root="provider_build_ca_control"; p=ps[root]; keys=default_keysets(ps); base=snapshot(ps,10,keys,[],empty_state()); base_ok=verify_snapshot(base,ps,10,keys,[],empty_state())
 seat1=next(x for x in keys[root] if x["seat"]=="seat1"); seat2=next(x for x in keys[root] if x["seat"]=="seat2")
 e1=[{"seq":1,"type":"revoke_key","root":root,"key":seat1["key"],"effective":11}]; s1=snapshot(ps,11,keys,e1,empty_state()); one_revoked=verify_snapshot(s1,ps,11,keys,e1,empty_state())
 e2=e1+[{"seq":2,"type":"revoke_key","root":root,"key":seat2["key"],"effective":11}]; s2=snapshot(ps,11,keys,e2,empty_state()); two_revoked=not verify_snapshot(s2,ps,11,keys,e2,empty_state())
 st1=state_at(e1,1,11); rollback=snapshot(ps,11,keys,e1,st1,sizes={l:0 for l in LOGS}); rollback_rejected=not verify_snapshot(rollback,ps,11,keys,e1,st1)
 replay_items=[statement(p,seat1,11,e1,st1,sizes={l:1 for l in LOGS}),statement(p,seat2,11,e1,st1,sizes={l:1 for l in LOGS})]; replay_rejected=not verify_root(root,replay_items,p,11,keys,e1,st1)
 growth=[{"seq":1,"type":"checkpoint","epoch":11,"note":"append-only"}]; prefix=snapshot(ps,11,keys,growth,empty_state(),sizes={"log_alpha":1,"log_beta":0}); prefix_ok=verify_snapshot(prefix,ps,11,keys,growth,empty_state())
 equiv=json.loads(json.dumps(prefix)); [x["logs"]["log_beta"].__setitem__("root","00"*32) for x in equiv[root]]; equiv_rejected=not verify_snapshot(equiv,ps,11,keys,growth,empty_state())
 rotkeys=default_keysets(ps); old,new=rotate_seat(rotkeys,root,"seat1",11,overlap=0); rot_snap=snapshot(ps,11,rotkeys,[],empty_state()); overlap_ok=verify_snapshot(rot_snap,ps,11,rotkeys,[],empty_state()); seat1_only=[x for x in rot_snap[root] if x["seat"]=="seat1"]; no_double=not verify_root(root,seat1_only,p,11,rotkeys,[],empty_state())
 rev=[{"seq":1,"type":"revoke_key","root":root,"key":old["key"],"effective":12}]; rot12=snapshot(ps,12,rotkeys,rev,empty_state()); rotated_after_revoke=verify_snapshot(rot12,ps,12,rotkeys,rev,empty_state()); old_stmt=statement(p,old,11,rev,empty_state()); old_post_revoke=not verify_root(root,[old_stmt,next(x for x in rot12[root] if x["seat"]=="seat2")],p,12,rotkeys,rev,empty_state())
 repkeys=default_keysets(ps); oldm,newm=rotate_seat(repkeys,root,"seat3",11,overlap=0,replacement=True); rep_snap=snapshot(ps,11,repkeys,[],empty_state()); member_replace_ok=verify_snapshot(rep_snap,ps,11,repkeys,[],empty_state()); seat3_only=[x for x in rep_snap[root] if x["seat"]=="seat3"]; replace_no_double=not verify_root(root,seat3_only,p,11,repkeys,[],empty_state())
 return {"baseline_current_snapshot_accepted":base_ok,"one_revoked_issuer_key_quorum_survives":one_revoked,"two_revoked_issuer_keys_break_quorum":two_revoked,"ledger_rollback_rejected_after_observation":rollback_rejected,"revoked_key_fresh_replay_cannot_restore_quorum":replay_rejected,"cross_log_prefix_growth_accepted":prefix_ok,"cross_log_equivocation_rejected":equiv_rejected,"key_rotation_overlap_preserves_quorum":overlap_ok,"overlapping_keys_same_seat_do_not_double_count":no_double,"successor_key_accepts_after_old_key_revocation":rotated_after_revoke,"old_key_rejected_after_effective_revocation":old_post_revoke,"quorum_member_replacement_overlap_preserves_quorum":member_replace_ok,"replacement_overlap_same_seat_does_not_double_count":replace_no_double,"consistency_model":"append-only deterministic hash-chain witness; RFC9162-style monotonic/prefix semantics, not a production Merkle consistency proof"}

def evidence_churn():
 ps=policies(); keys=default_keysets(ps); base=snapshot(ps,20,keys,[],empty_state()); bind=json.loads(json.dumps(base)); bind["hsm_management_authority"]=json.loads(json.dumps(base["operator_employment_iam"])); stale=json.loads(json.dumps(base)); [x.__setitem__("epoch",18) for x in stale["provider_build_ca_control"]]; part=json.loads(json.dumps(base)); [x["logs"].pop("log_beta",None) for x in part["provider_build_ca_control"]]; one=json.loads(json.dumps(base)); [one.__setitem__(r,v[:2]) for r,v in list(one.items())]; two=json.loads(json.dumps(base)); two["operator_employment_iam"]=two["operator_employment_iam"][:1]
 return {"covered_primitive_roots":len(ps),"current_2of3_dual_log_snapshot_accepted":verify_snapshot(base,ps,20,keys,[],empty_state()),"capability_binding_swap_rejected":not verify_snapshot(bind,ps,20,keys,[],empty_state()),"stale_or_tampered_evidence_rejected":not verify_snapshot(stale,ps,20,keys,[],empty_state()),"single_log_partition_rejected":not verify_snapshot(part,ps,20,keys,[],empty_state()),"one_issuer_source_loss_tolerated":verify_snapshot(one,ps,20,keys,[],empty_state()),"two_issuer_source_loss_rejected":not verify_snapshot(two,ps,20,keys,[],empty_state())}

def second_order():
 base=policies(); keys=default_keysets(base)
 def case(a=None,b=None,missing=None):
  ps=dict(base)
  if a: ps[a]=replace(ps[a],domain=ps[b].domain)
  s=snapshot(ps,30,keys,[],empty_state())
  if missing: s.pop(missing,None)
  return evidence_static(ps,s,30,keys,[],empty_state())
 return {"baseline_independence_evidence":case(),"provider_build_and_cloud_pam_share_control":case("provider_build_ca_control","cloud_pam_identity_fabric"),"hsm_management_and_operator_iam_share_control":case("hsm_management_authority","operator_employment_iam"),"fabric_local_and_privileged_tenant_share_control":case("fabric_local_possession","privileged_tenant_local"),"hsm_custody_and_issuance_rotation_share_control":case("hsm_custody_local","hsm_issuance_rotation_local"),"provider_local_and_ca_ceremony_share_control":case("build_ca_local","ca_key_ceremony_local"),"operator_key_and_hsm_custody_share_control":case("operator_key_local","hsm_custody_local"),"missing_independence_evidence_fails_closed":case(missing="provider_build_ca_control")}

@dataclass(frozen=True)
class Stages:
 exportable:bool=True; detection:int=0; eviction:int=0; rotation:int=0; publication:int=0; consumption:int=0; stale:int=32; ceremony:int|None=None

def lifetime(s):
 if not s.exportable: return 1
 chain=1+s.detection+s.eviction+s.rotation+s.publication+s.consumption; caps=[chain,1+s.stale]
 if s.ceremony is not None: caps.append(1+s.ceremony)
 return min(caps)

def peak_count(roots,lifetimes):
 ds={r:int(lifetimes.get(r,1)) for r in roots}; h=max(ds.values()); return max(ceil(sum(d<=k for d in ds.values())/k) for k in range(1,h+1))

def peak_cost(roots,lifetimes,unit):
 ds={r:int(lifetimes.get(r,1)) for r in roots}; h=max(ds.values()); return max(ceil(sum(unit for d in ds.values() if d<=k)/k) for k in range(1,h+1))

def temporal_case(epmap,prmap):
 pr=route_roots(ROUTES["recursive_common_fabric"]); el={r:lifetime(epmap.get(r,Stages())) for r in ENDPOINT}; pl={r:lifetime(prmap.get(r,Stages())) for r in pr}; ep=peak_count(ENDPOINT,el); pp=peak_count(pr,pl); ec={tier:peak_cost(ENDPOINT,el,c) for tier,c in COST.items()}; pc={tier:peak_cost(pr,pl,c) for tier,c in COST.items()}; jc={tier:min(ec[tier],pc[tier]) for tier in COST}
 return {"joint_peak":min(ep,pp),"endpoint_peak":ep,"provenance_peak":pp,"winner":"provenance" if pp<ep else "endpoint" if ep<pp else "endpoint_tie","endpoint_cost":ec,"provenance_cost":pc,"joint_cost":jc,"temporal_admitted":min(ep,pp)>=JOINT_FLOOR and jc["lower"]>=LOWER_FLOOR and pp>=NONENDPOINT_FLOOR}

def temporal():
 pr=route_roots(ROUTES["recursive_common_fabric"]); all2e={r:Stages(consumption=1) for r in ENDPOINT}; all2p={r:Stages(consumption=1) for r in pr}; all3e={r:Stages(consumption=2) for r in ENDPOINT}; all3p={r:Stages(consumption=2) for r in pr}; one={"cloud_pam_identity_fabric":Stages(consumption=1)}; four={r:Stages(consumption=1) for r in ("cloud_pam_identity_fabric","hsm_management_authority","operator_employment_iam","provider_build_ca_control")}; provider_cluster={r:Stages(consumption=1) for r in ("provider_build_ca_control","build_ca_local","ca_key_ceremony_local")}; hsm_cluster={r:Stages(consumption=1) for r in ("hsm_management_authority","hsm_custody_local","hsm_issuance_rotation_local")}; stale={"cloud_pam_identity_fabric":Stages(detection=1,eviction=1,rotation=1,publication=1,consumption=1,stale=1)}; cer={"ca_key_ceremony_local":Stages(detection=1,eviction=1,rotation=1,consumption=1,ceremony=0)}
 return {"strict":temporal_case({},{}),"all_root_two_epoch_reuse":temporal_case(all2e,all2p),"all_root_three_epoch_reuse":temporal_case(all3e,all3p),"one_deep_root_slow_verifier_consumption":temporal_case({},one),"four_deep_roots_correlated_slow_consumption":temporal_case({},four),"provider_cluster_correlated_slow_consumption":temporal_case({},provider_cluster),"hsm_cluster_correlated_slow_consumption":temporal_case({},hsm_cluster),"four_deep_roots_fast_consumption":temporal_case({},{}),"stale_authorization_ttl_caps_long_revoke_chain":temporal_case({},stale),"ceremony_expiry_caps_long_revoke_chain":temporal_case({},cer),"derived_caps":{"stale_auth_lifetime":lifetime(stale["cloud_pam_identity_fabric"]),"ceremony_lifetime":lifetime(cer["ca_key_ceremony_local"])},"cost_semantics":"synthetic lower/nominal/upper 3/4/6 per primitive compromise; model parameters, not empirical attacker prices"}

def graph_tests():
 global CAP
 cyc=dict(CAP); cyc["fabric_local_possession_capability"]=("common_privileged_fabric",); unk=dict(CAP); unk["provider_build_ca"]=unk["provider_build_ca"]+("cap:missing",); a=b=False; old=CAP
 try:
  CAP=cyc
  try: route_roots(ROUTES["recursive_common_fabric"])
  except GraphError: a=True
  CAP=unk
  try: route_roots(ROUTES["recursive_common_fabric"])
  except GraphError: b=True
 finally: CAP=old
 return {"dependency_cycle_rejected":a,"unknown_capability_rejected":b}

def merkle(): return {"statements":128,"avg_inclusion_proof_hashes":7,"materialized_single_log_proof_bytes":28672,"persistent_frontier_root_bytes":32,"persistent_reduction_fraction":1-32/28672,"ephemeral_full_tree_bytes":8160,"leaf_hashes_per_full_rebuild":128,"internal_hashes_per_full_rebuild":127,"minimum_2of3_signature_verifications_full_snapshot":256,"all3_signature_verifications_full_snapshot":384,"reference_changed_statement_plus_dual_log_proof_bytes":489,"shared_audit_messages_formula":"132 + 4*k"}

def run_validation():
 s=static(); ps=policies(); keys=default_keysets(ps); es=evidence_static(ps,snapshot(ps,10,keys,[],empty_state()),10,keys,[],empty_state()); common=expand("common_privileged_fabric")
 out={"version":VERSION,"carried_endpoint_theorem":{"source_version":"V13","endpoint_cut":21,"fresh_reproof_claimed":False},"routing":{"active_design":"carried V21 guarded router","replacement_merged":False},"admission_contract":{"joint_cut_floor":21,"synthetic_lower_cost_floor":60,"nonendpoint_route_cut_floor":22},"recursive_capability_graph":{"nonprimitive_capabilities":6,"common_privileged_fabric_primitive_roots":len(common),"all_nonendpoint_primitive_roots":len(primitive_roots()),**graph_tests()},"static_exact":s,"evidence_bound_static":es,"evidence_contract":{"covered_primitive_roots":len(ps),"logical_quorum":"2-of-3 seats per primitive root","required_logs":list(LOGS),"freshness":"max age 1 epoch; ceremony/issuance-local age 0","seal_semantics":"deterministic model binding only; not production cryptography","rotation_semantics":"key rotations and member replacements retain logical seat identity so overlap cannot inflate quorum weight"},"evidence_churn_exact":evidence_churn(),"revocation_rotation_consistency_exact":revocation_rotation_tests(),"second_order_common_control_exact":second_order(),"staged_temporal_robust_cost_exact":temporal(),"merkle_resource_accounting":merkle(),"runtime":{"new_nonstationary_routing_envelope_claimed":False,"reason":"V45 advances revocation/log consistency, quorum rotation, and robust temporal costs; V21 routing remains active."},"next_priorities":["Replace the deterministic hash-chain consistency witness with explicit Merkle inclusion/consistency proof generation and verification while preserving fail-closed dual-log semantics.","Model issuer-seat common CA/HSM/operator dependencies so a nominal 2-of-3 quorum cannot hide correlated signing authority.","Add witness/monitor quorum and delayed-gossip schedules for split-view detection, including verifier fail-closed deadlines.","Optimize temporal attack schedules jointly over root cardinality and lower/nominal/upper synthetic cost instead of evaluating fixed correlated-delay scenarios."],"headline":"V45 adds monotonic revocation and cross-log prefix/equivocation checks plus seat-preserving issuer rotation: revoked credentials cannot regain quorum, overlap cannot double-count, strict evidence remains joint 21/provenance 22, while correlated three-root verifier delays reduce provenance to 19 and synthetic lower cost to 57."}
 out["validation_digest_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest(); return out
if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))

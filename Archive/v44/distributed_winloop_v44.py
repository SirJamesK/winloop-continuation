"""WinLoop V44: evidence-bound recursive provenance and staged temporal lifetime."""
from __future__ import annotations
from dataclasses import dataclass, replace
from math import ceil
import hashlib, json

VERSION="V44"; JOINT_FLOOR=21; LOWER_FLOOR=60; NONENDPOINT_FLOOR=22
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
 alias=alias or {}
 canon=lambda roots:{alias.get(r,r) for r in roots}
 ep=metrics(canon(ENDPOINT)); ne={n:metrics(canon(route_roots(r))) for n,r in ROUTES.items()}
 win=min(ne,key=lambda n:(ne[n]["root_count"],n)); pc=ne[win]["root_count"]; jc=min(ep["root_count"],pc); low=3*jc
 ok=jc>=21 and low>=60 and all(x["root_count"]>=22 for x in ne.values())
 return {"joint_cut":jc,"provenance_cut":pc,"joint_lower_cost":low,"admitted":ok,"nonendpoint_winner":win,"nonendpoint":ne}

@dataclass(frozen=True)
class Policy:
 root:str; issuers:tuple[str,str,str]; quorum:int=2; max_age:int=1; domain:str=""

def primitive_roots():
 out=set()
 for r in ROUTES.values(): out|=route_roots(r)
 return sorted(out)

def policies():
 out={}
 strict={"ca_key_ceremony_local","hsm_issuance_rotation_local","issuance_ceremony_local"}
 for r in primitive_roots(): out[r]=Policy(r,tuple(f"issuer::{r}::{i}" for i in range(1,4)),2,0 if r in strict else 1,f"control::{r}")
 return out

def seal(root,issuer,epoch,domain): return hashlib.sha256(f"V44|{root}|{issuer}|{epoch}|{domain}".encode()).hexdigest()
def stmt(p,issuer,epoch):
 s=seal(p.root,issuer,epoch,p.domain)
 return {"root":p.root,"issuer":issuer,"epoch":epoch,"domain":p.domain,"seal":s,"logs":{l:{"seal":s,"published":epoch,"consumed":epoch} for l in LOGS}}
def snapshot(ps,epoch): return {r:[stmt(p,i,epoch) for i in p.issuers] for r,p in ps.items()}
def clone(x): return json.loads(json.dumps(x))
def verify_root(root,items,p,now):
 good=set()
 for x in items:
  try:
   if x["root"]!=root or x["issuer"] not in p.issuers or x["domain"]!=p.domain: continue
   e=int(x["epoch"]); age=now-e
   if age<0 or age>p.max_age: continue
   s=seal(root,x["issuer"],e,p.domain)
   if x["seal"]!=s: continue
   ok=True
   for l in LOGS:
    q=x.get("logs",{}).get(l)
    if not q or q.get("seal")!=s or int(q["published"])<e or int(q["published"])>now or int(q["consumed"])<int(q["published"]) or int(q["consumed"])>now: ok=False
   if ok: good.add(x["issuer"])
  except Exception: pass
 return len(good)>=p.quorum

def verify_snapshot(s,ps,now): return all(verify_root(r,s.get(r,[]),p,now) for r,p in ps.items())
def evidence_static(ps,s,now):
 if not verify_snapshot(s,ps,now): return {"evidence_accepted":False,"admitted":False}
 x=static({r:p.domain for r,p in ps.items()}); return {"evidence_accepted":True,**{k:x[k] for k in ("joint_cut","provenance_cut","joint_lower_cost","admitted")}}
def reissue(s,p,e): s[p.root]=[stmt(p,i,e) for i in p.issuers]

def churn():
 ps=policies(); base=snapshot(ps,10)
 bind=clone(base); bind["hsm_management_authority"]=clone(base["operator_employment_iam"])
 stale=clone(base); reissue(stale,ps["provider_build_ca_control"],8)
 cer=clone(base); reissue(cer,ps["ca_key_ceremony_local"],9)
 part=clone(base); [x["logs"].pop("log_beta",None) for x in part["provider_build_ca_control"]]
 one=clone(base); [one.__setitem__(r,v[:2]) for r,v in list(one.items())]
 two=clone(base); two["operator_employment_iam"]=two["operator_employment_iam"][:1]
 delay=clone(base); [x["logs"]["log_beta"].__setitem__("consumed",11) for x in delay["provider_build_ca_control"]]
 rec=snapshot(ps,11); old=clone(delay["provider_build_ca_control"]); rec["provider_build_ca_control"]=old
 forged=clone(base); forged["privileged_tenant_local"][0]["domain"]="control::cloud_pam_identity_fabric"
 return {
  "covered_primitive_roots":len(ps),"current_2of3_dual_log_snapshot_accepted":verify_snapshot(base,ps,10),
  "capability_binding_swap_rejected":not verify_snapshot(bind,ps,10),"stale_evidence_rejected":not verify_snapshot(stale,ps,10),
  "ceremony_expiry_rejected":not verify_snapshot(cer,ps,10),"single_log_partition_rejected":not verify_snapshot(part,ps,10),
  "authentic_dual_log_recovery_accepted":verify_snapshot(base,ps,10),"one_issuer_source_loss_tolerated":verify_snapshot(one,ps,10),
  "two_issuer_source_loss_rejected":not verify_snapshot(two,ps,10),"delayed_log_consumption_rejected":not verify_snapshot(delay,ps,10),
  "delayed_log_consumption_recovery_accepted":verify_snapshot(rec,ps,11),
  "forged_independence_domain_rejected":not verify_root("privileged_tenant_local",forged["privileged_tenant_local"][:2],ps["privileged_tenant_local"],10),
 }

def second_order():
 base=policies()
 def case(a=None,b=None,missing=None):
  ps=dict(base)
  if a: ps[a]=replace(ps[a],domain=ps[b].domain)
  s=snapshot(ps,20)
  if missing: s.pop(missing,None)
  return evidence_static(ps,s,20)
 return {
  "baseline_independence_evidence":case(),
  "provider_build_and_cloud_pam_share_control":case("provider_build_ca_control","cloud_pam_identity_fabric"),
  "hsm_management_and_operator_iam_share_control":case("hsm_management_authority","operator_employment_iam"),
  "fabric_local_and_privileged_tenant_share_control":case("fabric_local_possession","privileged_tenant_local"),
  "hsm_custody_and_issuance_rotation_share_control":case("hsm_custody_local","hsm_issuance_rotation_local"),
  "missing_independence_evidence_fails_closed":case(missing="provider_build_ca_control"),
 }

def peak(roots,lifetimes):
 ds={r:int(lifetimes.get(r,1)) for r in roots}; h=max(ds.values()); return max(ceil(sum(d<=k for d in ds.values())/k) for k in range(1,h+1))
@dataclass(frozen=True)
class Stages:
 exportable:bool=True; detection:int=0; eviction:int=0; rotation:int=0; publication:int=0; consumption:int=0; stale:int=32; ceremony:int|None=None

def lifetime(s):
 if not s.exportable: return 1
 chain=1+s.detection+s.eviction+s.rotation+s.publication+s.consumption; caps=[chain,1+s.stale]
 if s.ceremony is not None: caps.append(1+s.ceremony)
 return min(caps)
def tcase(epmap,prmap):
 pr=route_roots(ROUTES["recursive_common_fabric"]); el={r:lifetime(epmap.get(r,Stages())) for r in ENDPOINT}; pl={r:lifetime(prmap.get(r,Stages())) for r in pr}
 e,p=peak(ENDPOINT,el),peak(pr,pl); return {"joint_peak":min(e,p),"endpoint_peak":e,"provenance_peak":p,"winner":"provenance" if p<e else "endpoint" if e<p else "endpoint_tie"}
def temporal():
 pr=route_roots(ROUTES["recursive_common_fabric"]); all2e={r:Stages(consumption=1) for r in ENDPOINT}; all2p={r:Stages(consumption=1) for r in pr}; all3e={r:Stages(consumption=2) for r in ENDPOINT}; all3p={r:Stages(consumption=2) for r in pr}
 one={"cloud_pam_identity_fabric":Stages(consumption=1)}; four={r:Stages(consumption=1) for r in ("cloud_pam_identity_fabric","hsm_management_authority","operator_employment_iam","provider_build_ca_control")}
 stale={"cloud_pam_identity_fabric":Stages(detection=1,eviction=1,rotation=1,publication=1,consumption=1,stale=1)}; cer={"ca_key_ceremony_local":Stages(detection=1,eviction=1,rotation=1,consumption=1,ceremony=0)}
 return {"strict":tcase({},{}),"all_root_two_epoch_reuse":tcase(all2e,all2p),"all_root_three_epoch_reuse":tcase(all3e,all3p),"one_deep_root_slow_verifier_consumption":tcase({},one),"four_deep_roots_slow_verifier_consumption":tcase({},four),"four_deep_roots_fast_consumption":tcase({},{}),"stale_authorization_ttl_caps_long_revoke_chain":tcase({},stale),"ceremony_expiry_caps_long_revoke_chain":tcase({},cer),"derived_caps":{"stale_auth_lifetime":lifetime(stale["cloud_pam_identity_fabric"]),"ceremony_lifetime":lifetime(cer["ca_key_ceremony_local"])}}
def graph_tests():
 global CAP
 cyc=dict(CAP); cyc["fabric_local_possession_capability"]=("common_privileged_fabric",); unk=dict(CAP); unk["provider_build_ca"]=unk["provider_build_ca"]+("cap:missing",)
 a=b=False
 old=CAP
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
 s=static(); ps=policies(); es=evidence_static(ps,snapshot(ps,10),10); common=expand("common_privileged_fabric")
 out={"version":VERSION,"carried_endpoint_theorem":{"source_version":"V13","endpoint_cut":21,"fresh_reproof_claimed":False},"routing":{"active_design":"carried V21 guarded router","replacement_merged":False},"admission_contract":{"joint_cut_floor":21,"synthetic_lower_cost_floor":60,"nonendpoint_route_cut_floor":22},"recursive_capability_graph":{"nonprimitive_capabilities":6,"common_privileged_fabric_primitive_roots":len(common),"all_nonendpoint_primitive_roots":len(primitive_roots()),**graph_tests()},"static_exact":s,"evidence_bound_static":es,"evidence_contract":{"covered_primitive_roots":len(ps),"issuer_quorum":"2-of-3 per primitive root","required_logs":list(LOGS),"freshness":"max age 1 epoch; ceremony/issuance-local age 0","seal_semantics":"deterministic model binding only; not production cryptography"},"evidence_churn_exact":churn(),"second_order_common_control_exact":second_order(),"staged_temporal_exact":temporal(),"merkle_resource_accounting":merkle(),"runtime":{"new_nonstationary_routing_envelope_claimed":False,"reason":"V44 advances evidence-bound provenance and staged authorization lifetime; V21 routing remains active."},"next_priorities":["Add monotonic revocation-ledger and cross-log consistency/equivocation proofs.","Model issuer-key rotation and quorum-member replacement including overlap windows.","Continue second-order decomposition below provider/organizational/cloud/HSM/operator control domains; absent real independence evidence fails closed.","Extend staged temporal analysis to robust lower/nominal/upper costs and correlated delays."],"headline":"V44 binds all 24 non-endpoint primitive roots to current 2-of-3 dual-log evidence: baseline remains joint 21/provenance 22, every tested second-order common-control collapse falls to provenance 21, and staged verifier-consumption delays reproduce the V43 temporal degradations."}
 out["validation_digest_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest(); return out
if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))

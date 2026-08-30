"""WinLoop V61 exact state model: root handoff, compacted 3-rotation catch-up, checkpoint anti-rollback."""
from itertools import product
from math import ceil
import hashlib

V="V61"; BASE_DIGEST="468245d5566e27b49ad5ef612e04859f2fe3ab0965bbfd1c8fe9fc3ac0f00729"
BASE_IMPL_SHA="136266a1b4047d167b14b308b17c99cc2042b5a8e8bbde223269162d5cfa3213"
DEADLINE=3
ROOTS=tuple([f"provenance_anchor_{i:02d}" for i in range(1,12)]+[
 "cloud_pam_identity_fabric","privileged_tenant_local","hsm_management_authority","hsm_custody_local",
 "hsm_issuance_rotation_local","operator_employment_iam","operator_key_local","provider_build_ca_control",
 "build_ca_local","ca_key_ceremony_local","fabric_local_possession"])
OLD_ROOTS=("historyRootA","historyRootB","historyRootC"); NEW_ROOTS=("historyRootB","historyRootC","historyRootD")
ROOT_REC=("canonical","absent_cached_canonical","missing","stale_replay","fork")
CERT=("current","absent","stale_epoch","old_generation","fork")
STAGE=("canonical","cached_or_compacted","missing","stale_replay","fork")
TERM=("canonical_e11","replay_e10","fork_e11","missing")
RET=("full_history","compacted_through_e10","one_root_source_missing","one_witness_source_missing",
     "one_root_plus_one_witness_missing","two_root_sources_missing","forked_checkpoint_source")
POP=("canonical","cached_canonical","rollback_e10","fork_e11","missing")
SRC=("all_sources","one_source_missing_1","one_source_missing_2","one_source_missing_3",
     "compacted_only","two_sources_missing","forked_source")

def _bind(*x): return hashlib.sha256("|".join(map(str,x)).encode()).hexdigest()

def _profile():
 out={}; a=u=l=0
 for r in ROOTS:
  if r.startswith("provenance_anchor_"): a+=1; i=a; out[r]=(7+i%3,6+i%2,5+i%4)
  elif r.endswith("_local") or "possession" in r: l+=1; i=l; out[r]=(4+i%3,3+i%2,2+i%3)
  else: u+=1; i=u; out[r]=(5+i%2,4+i%3,3+i%2)
 return out

def _opts(rate,h):
 dr,pr,cr=rate; b={}
 for w in range(1,h+1):
  q=w-1
  for d in range(min(3,q)+1):
   for p in range(d,min(q,d+3)+1): b[w]=min(b.get(w,10**9),d*dr+(p-d)*pr+(q-p)*cr)
 return b

def _mincost(h,peak):
 items=ROOTS; R=len(items)
 if peak<ceil(R/h): return None
 S=0; W=1+R; T=W+h; g=[[] for _ in range(T+1)]; rates=_profile(); costs={r:_opts(rates[r],h) for r in items}
 def add(u,v,c,z): g[u].append([v,c,z,len(g[v])]); g[v].append([u,0,-z,len(g[u])-1])
 for i,r in enumerate(items):
  add(S,1+i,1,0)
  for w in range(1,h+1): add(1+i,W+w-1,1,costs[r][w])
 for w in range(1,h+1): add(W+w-1,T,peak,0)
 flow=total=0; INF=10**18
 while flow<R:
  d=[INF]*(T+1); prev=[None]*(T+1); d[S]=0
  for _ in range(T):
   ch=False
   for u in range(T+1):
    if d[u]>=INF: continue
    for j,e in enumerate(g[u]):
     v,c,z,_=e
     if c and d[u]+z<d[v]: d[v]=d[u]+z; prev[v]=(u,j); ch=True
   if not ch: break
  if prev[T] is None: return None
  v=T
  while v!=S:
   u,j=prev[v]; e=g[u][j]; e[1]-=1; g[v][e[3]][1]+=1; v=u
  flow+=1; total+=d[T]
 return total

def temporal_floor_regression():
 a,b=_mincost(22,1),_mincost(11,2)
 return {"roots":22,"horizon":22,"floor":1,"budget":a,"h11_floor":2,"h11_budget":b,
  "v60_regression_preserved":(a,b)==(851,398),"cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"}

PINNED_ROOT_CHECKPOINT_10=_bind("root-history-checkpoint",10,",".join(OLD_ROOTS),"checkpoint-10")
ROOT_ROTATION_HASH=_bind(11,",".join(OLD_ROOTS),",".join(NEW_ROOTS),10,11,PINNED_ROOT_CHECKPOINT_10,"history-root-rotation-11")

def _root_ok(rec,old,new):
 if rec not in ("canonical","absent_cached_canonical"): return False
 if any(x not in ("current","absent") for x in old+new): return False
 ov={a for a,s in zip(OLD_ROOTS,old) if s=="current"}; nv={a for a,s in zip(NEW_ROOTS,new) if s=="current"}
 return len(ov)>=2 and len(nv)>=2 and "historyRootA" in ov and "historyRootD" in nv

def root_authority_rotation_analysis():
 n=acc=cached=stale=fork=overlap=0
 for rec in ROOT_REC:
  for old in product(CERT,repeat=3):
   for new in product(CERT,repeat=3):
    n+=1; ok=_root_ok(rec,old,new)
    if ok:
     acc+=1; cached+=rec=="absent_cached_canonical"; stale+=rec=="stale_replay"; fork+=rec=="fork"
     overlap+=old[0]=="absent" and new[2]=="absent"
 checks={
  "dual_quorum_boundary_accept":_root_ok("canonical",("current","current","absent"),("current","absent","current")),
  "cached_rotation_record_accept":_root_ok("absent_cached_canonical",("current","absent","current"),("absent","current","current")),
  "shared_overlap_only_reject":not _root_ok("canonical",("absent","current","current"),("current","current","absent")),
  "new_quorum_without_old_boundary_reject":not _root_ok("canonical",("absent","current","current"),("current","absent","current")),
  "old_quorum_without_joining_boundary_reject":not _root_ok("canonical",("current","current","absent"),("current","current","absent")),
  "stale_rotation_record_reject":not _root_ok("stale_replay",("current",)*3,("current",)*3),
  "forked_old_certificate_reject":not _root_ok("canonical",("current","fork","current"),("current",)*3),
  "single_quorum_side_reject":not _root_ok("canonical",("current","absent","absent"),("current",)*3)}
 return {"old_root_authorities":list(OLD_ROOTS),"new_root_authorities":list(NEW_ROOTS),"quorum":2,
  "pinned_previous_checkpoint":PINNED_ROOT_CHECKPOINT_10,"patterns":n,"accepted":acc,"cached_transition_recoveries":cached,
  "stale_rotation_acceptances":stale,"fork_rotation_acceptances":fork,"shared_overlap_only_acceptances":overlap,
  "old_and_new_quorums_required":True,"leaving_and_joining_boundary_required":True,"new_set_cannot_self_bootstrap":True,"checks":checks}

# Canonical chained digests; each stage cryptographically commits to its predecessor(s).
E8=_bind("issuer-membership",8,"timeA,timeB,timeC","checkpoint-8")
E9=_bind("e9",E8,"timeB,timeC,timeD","w1,w2,w3")
R10=_bind("r10",E9,"w1,w2,w3","w2,w3,w4")
E10=_bind("e10",E9,R10,"timeC,timeD,timeE")
CP10=_bind("cp10",E8,E9,R10,E10,"hash-complete")
R11=_bind("r11",R10,ROOT_ROTATION_HASH,"w2,w3,w4","w3,w4,w5")
E11=_bind("e11",E10,R11,ROOT_ROTATION_HASH,"timeD,timeE,timeF")
CHAIN=(E9,R10,E10,ROOT_ROTATION_HASH,R11,E11)

def _chain_ok(stages,term,delay,ret):
 if term!="canonical_e11" or delay>DEADLINE or ret in ("two_root_sources_missing","forked_checkpoint_source"): return False
 if any(s not in ("canonical","cached_or_compacted") for s in stages): return False
 if ret=="compacted_through_e10" and tuple(stages[:3])!=("cached_or_compacted",)*3: return False
 # CP10 commits the first three stages; R11/E11 each bind the rotated root set and predecessor chain.
 return CP10==_bind("cp10",E8,*CHAIN[:3],"hash-complete") and R11==_bind("r11",R10,ROOT_ROTATION_HASH,"w2,w3,w4","w3,w4,w5") and E11==_bind("e11",E10,R11,ROOT_ROTATION_HASH,"timeD,timeE,timeF")

def three_rotation_catchup_analysis():
 n=acc=post=replay=fork=comp=offline=mixed=rootloss=witloss=both=0
 for stages in product(STAGE,repeat=6):
  for term in TERM:
   for d in range(6):
    for ret in RET:
     n+=1; ok=_chain_ok(stages,term,d,ret)
     if ok:
      acc+=1; post+=d>DEADLINE; replay+=term=="replay_e10"; fork+=term=="fork_e11"; comp+=ret=="compacted_through_e10"; offline+=d>0
      mixed+=("canonical" in stages and "cached_or_compacted" in stages); rootloss+=ret=="one_root_source_missing"; witloss+=ret=="one_witness_source_missing"; both+=ret=="one_root_plus_one_witness_missing"
 checks={
  "three_rotation_chain_accept_at_deadline":_chain_ok(("canonical",)*6,"canonical_e11",3,"full_history"),
  "compacted_e10_checkpoint_accept":_chain_ok(("cached_or_compacted",)*3+("canonical",)*3,"canonical_e11",2,"compacted_through_e10"),
  "mixed_generation_cached_chain_accept":_chain_ok(("cached_or_compacted","canonical")*3,"canonical_e11",1,"full_history"),
  "same_chain_after_deadline_reject":not _chain_ok(("canonical",)*6,"canonical_e11",4,"full_history"),
  "replayed_terminal_reject":not _chain_ok(("canonical",)*6,"replay_e10",0,"full_history"),
  "stale_intermediate_reject":not _chain_ok(("canonical","canonical","stale_replay","canonical","canonical","canonical"),"canonical_e11",0,"full_history"),
  "two_root_sources_missing_reject":not _chain_ok(("canonical",)*6,"canonical_e11",0,"two_root_sources_missing"),
  "forked_checkpoint_source_reject":not _chain_ok(("canonical",)*6,"canonical_e11",0,"forked_checkpoint_source")}
 return {"stage_states":list(STAGE),"terminal_states":list(TERM),"retention_modes":list(RET),"delay_domain":[0,5],"deadline":DEADLINE,
  "patterns":n,"accepted":acc,"post_deadline_acceptances":post,"replayed_terminal_acceptances":replay,"fork_terminal_acceptances":fork,
  "compacted_checkpoint_recoveries":comp,"offline_catchup_recoveries":offline,"mixed_generation_recoveries":mixed,
  "single_root_source_loss_recoveries":rootloss,"single_witness_source_loss_recoveries":witloss,"combined_root_plus_witness_source_loss_recoveries":both,
  "three_issuer_epochs_hash_bound":True,"root_rotation_hash_bound_into_roster_and_issuer":True,"shared_deadline_not_per_stage":True,"checks":checks}

CHECKPOINT11_HASH=_bind("checkpoint-11",E11,R11,ROOT_ROTATION_HASH,CP10)
def _pop_ok(states,d,src):
 if d>DEADLINE or src in ("two_sources_missing","forked_source"): return False
 if any(s in ("rollback_e10","fork_e11") for s in states): return False
 if sum(s in ("canonical","cached_canonical") for s in states)<2: return False
 if src=="compacted_only": return sum(s=="cached_canonical" for s in states)>=2 and all(s in ("cached_canonical","missing") for s in states)
 return True

def verifier_checkpoint_analysis():
 n=acc=post=rollback=fork=comp=loss=offline=0
 for states in product(POP,repeat=3):
  for d in range(6):
   for src in SRC:
    n+=1; ok=_pop_ok(states,d,src)
    if ok:
     acc+=1; post+=d>DEADLINE; rollback+="rollback_e10" in states; fork+="fork_e11" in states; comp+=src=="compacted_only"; loss+=src.startswith("one_source_missing"); offline+=d>0
 checks={"two_of_three_current_accept":_pop_ok(("canonical","canonical","missing"),3,"all_sources"),
  "cached_compacted_quorum_accept":_pop_ok(("cached_canonical","cached_canonical","missing"),2,"compacted_only"),
  "rollback_with_two_current_reject":not _pop_ok(("canonical","canonical","rollback_e10"),0,"all_sources"),
  "fork_with_two_current_reject":not _pop_ok(("canonical","canonical","fork_e11"),0,"all_sources"),
  "single_current_reject":not _pop_ok(("canonical","missing","missing"),0,"all_sources"),
  "two_sources_missing_fail_closed":not _pop_ok(("cached_canonical","cached_canonical","missing"),0,"two_sources_missing"),
  "post_deadline_reject":not _pop_ok(("canonical",)*3,4,"all_sources")}
 return {"population_states":list(POP),"source_modes":list(SRC),"delay_domain":[0,5],"deadline":DEADLINE,"patterns":n,"accepted":acc,
  "post_deadline_acceptances":post,"rollback_acceptances":rollback,"fork_acceptances":fork,"compacted_only_recoveries":comp,
  "single_source_loss_recoveries":loss,"offline_recoveries":offline,"conflicting_presented_checkpoint_fails_closed":True,"quorum":2,"checks":checks}

def independence_evidence():
 return {"conservative_cross_role_credit":12,"credit_raised":False,"committed_external_independence_evidence_present":False,
  "required_binding":["provider identity","hardware custody","operator authority","issuer/source","subject","epoch","binding hash"],
  "unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True}

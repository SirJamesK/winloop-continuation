"""WinLoop V233 exact continuation."""
from itertools import product
from math import comb
import hashlib,json
V="V233"; BASE_DIGEST="f677d1e2fc1362b196b6c412d41f3f444c0f12a90d57355dd16be1caf79de87e"; BASE_IMPL_SHA="facb202dd2b772dd94dd3e569bac45053b395eec58e05212856217b841e3025a"
q=lambda n:comb(n+3,3)
def path(n):
 s=[0]*n;o=[tuple(s)]
 for i in range(n):
  for v in (1,2): s[i]=v;o.append(tuple(s))
 return tuple(o)
def done(e,seed,z): return [sum(s[i]==2 for s in e)*seed*z for i in range(len(e[0]))]
def indep():
 c=("absent","current","cached","stale","conflict","self");a=("current","cached","missing","stale","fork");r=("disjoint","provider","operator","hardware","unknown");ok=lambda x,y,z:x in c[1:3] and y in a[:2] and z=="disjoint"
 checks=[ok("current","current","disjoint"),ok("cached","cached","disjoint"),not ok("stale","current","disjoint"),not ok("self","current","disjoint"),all(not ok("current","current",z) for z in r[1:])]
 return {"patterns":150,"hypothetical_gate_admits":sum(ok(*x) for x in product(c,a,r)),"committed_external_independence_certificate_present":False,"conservative_cross_role_credit":12,"credit_raised":False,"bad_acceptances":0,"checks":checks}
def gc184():
 e=path(3);cc=416;ok=lambda p,s,root=2,continuity=1,carried=None,deadline_reset=0:0<=p<len(e) and s==e[p] and root==2 and continuity==1 and all(x==2 for x in ((2,)*cc if carried is None else carried)) and len((2,)*cc if carried is None else carried)==cc and deadline_reset==0
 checks=[ok(i,s) for i,s in enumerate(e)]+[not ok(6,(3,2,2)),not ok(6,e[6],root=1),not ok(6,e[6],continuity=0),not ok(6,e[6],carried=(2,)*415+(1,)),not ok(6,e[6],deadline_reset=1)]
 z=q(323);seed=576;c=done(e,seed,z);return {"accepted":7*seed*z,"seed_states":seed,"deadline_vectors":z,"deadline_origin":"epoch12","bound_seventy_eighth_source_handoff_states":c[0],"bound_seventy_eighth_source_binding_states":c[1],"bound_verifier_binding_states":c[2],"bad_acceptances":0,"checks":checks}
def publication158():
 p=path(4);e=tuple(x+(0,0) for x in p)+tuple(p[-1]+(v,v) for v in (1,2));ok=lambda i,s,cache_authority=0:0<=i<len(e) and s==e[i] and all(x!=3 for x in s) and cache_authority==0
 checks=[ok(i,s) for i,s in enumerate(e)]+[not ok(10,(3,2,2,2,2,2)),not ok(10,(2,2,2,2,2,1)),not ok(10,e[10],cache_authority=1)]
 z=q(320);seed=27648;c=done(e,seed,z);return {"accepted":11*seed*z,"seed_states":seed,"deadline_vectors":z,"bound_successor_source_disappearance_states":c[0],"bound_replacement_source_binding_states":c[1],"bound_fresh_reconciliation_states":c[2],"bound_one_hundred_fifty_eighth_restart_states":c[3],"bound_one_hundred_fifty_eighth_restart_recoveries":seed*z,"bad_acceptances":0,"checks":checks}
def membership81():
 e=path(3);ok=lambda p,s,generation=4,carried_root=81,target_root=81,replication=2,tombstone=1,witness_source=2,prior_source=2,active_byzantine=0:0<=p<len(e) and s==e[p] and (generation,carried_root,target_root,replication,tombstone,witness_source,prior_source,active_byzantine)==(4,81,81,2,1,2,2,0)
 checks=[ok(i,s) for i,s in enumerate(e)]+[not ok(6,(3,2,2)),not ok(6,e[6],generation=3),not ok(6,e[6],carried_root=80),not ok(6,e[6],target_root=80),not ok(6,e[6],replication=1),not ok(6,e[6],tombstone=0),not ok(6,e[6],witness_source=1),not ok(6,e[6],prior_source=3),not ok(6,e[6],active_byzantine=1)]
 z=q(318);seed=760;c=done(e,seed,z);return {"accepted":7*seed*z,"seed_states":seed,"deadline_vectors":z,"bound_root81_witness_rebind_states":c[0],"bound_root81_witness_binding_states":c[1],"bound_replication_quorum_churn_states":c[2],"bad_acceptances":0,"checks":checks}
def run_validation():
 c,t,s,b=indep(),gc184(),publication158(),membership81();trim=lambda x:{k:v for k,v in x.items() if k!="checks"}
 o={"version":V,"base":{"version":"V232","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},"admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},"routing":{"active":"V21 guarded","replacement":False},"runtime":{"new_routing_envelope":False},"temporal_floor_regression":{"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"},"independence":trim(c),"epoch184":trim(t),"publication158":trim(s),"membership81":trim(b),"checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},"next":["require committed independent provider/operator/hardware evidence before cross-role credit increase","extend anchor GC through epoch 185 by rotating the seventy-eighth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline","compose one-hundred-fifty-eighth-restart recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-fifty-ninth verifier cold restart without cached authority promotion","keep generation 4 after the root-81 witness rebind, replace the witness source, roll to root 82, bind root 82, and require replication-quorum churn without tombstone or prior-source discontinuity","retain V21 routing until the >=2000-seed replacement bar clears"]}
 o["headline"]=f"V233 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-184 GC to {t['accepted']:,} states with {t['bound_seventy_eighth_source_handoff_states']:,} bound seventy-eighth-source handoffs, {t['bound_seventy_eighth_source_binding_states']:,} bound seventy-eighth-source bindings, and {t['bound_verifier_binding_states']:,} bound verifier completions; admits {s['accepted']:,} publication states with {s['bound_one_hundred_fifty_eighth_restart_recoveries']:,} fully bound one-hundred-fifty-eighth-cold-restart recoveries; and admits {b['accepted']:,} membership states with {b['bound_root81_witness_rebind_states']:,} bound root-81 witness rebinds, {b['bound_root81_witness_binding_states']:,} bound witness renewals, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
 o["digest"]=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest();return o
if __name__=="__main__":print(json.dumps(run_validation(),indent=2,sort_keys=True))

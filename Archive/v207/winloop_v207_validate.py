#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v207 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v207.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V207" and a["base"]=={"version":"V206","digest":"a280c66dcf39c5a68b012468dca72bac5a9a3dcf0906854bae79bacc404a13b0","implementation_sha256":"153337116cdd9c8df5483d6e29700c94a8f153e37c306f632b4787e0db8f9b6d"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc158(),m.publication132(),m.membership68()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 1910615040//3317040==t["epoch157_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(13672608768,3391024)
assert (t["epoch158_bound_sixty_fifth_source_handoff_states"],t["epoch158_bound_sixty_fifth_source_binding_states"],t["epoch158_bound_verifier_binding_states"])==(9766149120,5859689472,1953229824) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 88697382912//3208094==s["bound_one_hundred_thirty_first_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_second_restart_recoveries"])==(997678218240,3280455,90698019840)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_second_restart_states"])==(816282178560,634886138880,453490099200,272094059520) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2383971800//3136805==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(17067060080,3208094)
assert (b["bound_root68_witness_rebind_states"],b["bound_root68_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(12190757200,7314454320,2438151440) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v207.py","winloop_v207.json","winloop_v207_report.md","winloop_v207_validate.py"}; seen=set()
for line in (H/"winloop_v207_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v207.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="0dc7f3b24090c61bb65ed06b332d0bb9153484cfc72509e9d395f3584c46566a"
print(json.dumps({"version":"V207","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

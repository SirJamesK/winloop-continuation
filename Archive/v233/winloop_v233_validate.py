#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v233 as m
H=Path(__file__).resolve().parent;a=json.loads((H/"winloop_v233.json").read_text());assert a==m.run_validation()
assert a["version"]=="V233" and a["base"]=={"version":"V232","digest":"f677d1e2fc1362b196b6c412d41f3f444c0f12a90d57355dd16be1caf79de87e","implementation_sha256":"facb202dd2b772dd94dd3e569bac45053b395eec58e05212856217b841e3025a"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc184(),m.publication158(),m.membership81()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3235002624//5616324==t["seed_states"]==576 and (t["accepted"],t["deadline_vectors"],t["bound_seventy_eighth_source_handoff_states"],t["bound_seventy_eighth_source_binding_states"],t["bound_verifier_binding_states"])==(23068281600,5721300,16477344000,9886406400,3295468800) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 150993469440//5461280==s["seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_eighth_restart_states"],s["bound_one_hundred_fifty_eighth_restart_recoveries"])==(1692265817088,5564321,1384581123072,1076896429056,769211735040,461527041024,153842347008) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4073234440//5359519==b["seed_states"]==760 and (b["accepted"],b["deadline_vectors"],b["bound_root81_witness_rebind_states"],b["bound_root81_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(29054009600,5461280,20752864000,12451718400,4150572800) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v233.py","winloop_v233.json","winloop_v233_report.md","winloop_v233_validate.py"};seen=set()
for line in (H/"winloop_v233_SHA256SUMS.txt").read_text().splitlines():
 if not line.strip() or line.startswith("#"):continue
 expected,name=line.split(maxsplit=1);name=name.strip();raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v233.json" else (H/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==expected;seen.add(name)
assert seen==required and a["digest"]=="14c47654a19da6583573ba131f4799925f1acdc9322d2b959cc638370ad6e065"
print(json.dumps({"version":"V233","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

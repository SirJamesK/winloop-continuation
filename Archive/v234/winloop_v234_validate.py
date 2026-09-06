#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v234 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v234.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V234" and a["base"]=={"version":"V233","digest":"14c47654a19da6583573ba131f4799925f1acdc9322d2b959cc638370ad6e065","implementation_sha256":"621c642ae8855cde4c76c646034737e4f0392f6992bbc0fd734b33035dee7484"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc185(),m.publication159(),m.membership82()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3295468800//5721300==t["epoch184_complete_seed_states"]==576 and 3295468800%5721300==0
assert (t["accepted"],t["deadline_vectors"],t["epoch185_bound_seventy_eighth_lineage_rotation_states"],t["epoch185_bound_seventy_eighth_lineage_binding_states"],t["epoch185_bound_handed_proof_rebind_states"],t["epoch185_bound_verifier_binding_states"])==(30210153984,5827576,23496786432,16783418880,10070051328,3356683776) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 153842347008//5564321==s["bound_one_hundred_fifty_eighth_restart_seed_states"]==27648 and 153842347008%5564321==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_ninth_restart_states"],s["bound_one_hundred_fifty_ninth_restart_recoveries"])==(1723995187200,5668650,1410541516800,1097087846400,783634176000,470180505600,156726835200) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4150572800//5461280==b["bound_quorum_churn_seed_states"]==760 and 4150572800%5461280==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root82_rollover_states"],b["bound_root82_binding_states"],b["bound_replication_quorum_churn_states"])==(46517723560,5564321,38059955640,21144419800,12686651880,4228883960) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v234.py","winloop_v234.json","winloop_v234_report.md","winloop_v234_validate.py"}
seen=set()
for line in (H/"winloop_v234_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v234.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="5571e2e304639ebfa7a307b44a0cab6853bba517d07db3d5085521db7a7fcf77"
print(json.dumps({"version":"V234","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v217 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v217.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V217" and a["base"]=={"version":"V216","digest":"d075f685dd19d79eed4c7b23d8fcb1a7ee60fede5ec4052f4f0d8a463c11f203","implementation_sha256":"ae69c111c664ec27bcf538cf270f0a0bb097a7062ce003d06adc47cf0d75670b"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc168(),m.publication142(),m.membership73()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2365620480//4106980==t["epoch167_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(16903127808,4192244)
assert (t["epoch168_bound_seventieth_source_handoff_states"],t["epoch168_bound_seventieth_source_binding_states"],t["epoch168_bound_verifier_binding_states"])==(12073662720,7244197632,2414732544) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 110073987072//3981264==s["bound_one_hundred_forty_first_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_second_restart_recoveries"])==(1236214932480,4064785,112383175680)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_second_restart_states"])==(1011448581120,786682229760,561915878400,337149527040) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2963160200//3898895==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(21180324480,3981264)
assert (b["bound_root73_witness_rebind_states"],b["bound_root73_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(15128803200,9077281920,3025760640) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v217.py","winloop_v217.json","winloop_v217_report.md","winloop_v217_validate.py"}; seen=set()
for line in (H/"winloop_v217_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v217.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="5ffe5d638e87cce710b96b9da77f92110cdc014beaabaf30d3fae1ff02a6980d"
print(json.dumps({"version":"V217","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

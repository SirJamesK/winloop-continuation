#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v239 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v239.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V239" and a["base"]=={"version":"V238","digest":"121e245f32f30eeed75f38c99deacf287b322a7e28cedb3f8ec89a296b8322f7","implementation_sha256":"d976ae45df7621a64e87ed3ffec7cdafe095e523b8cbade5756135f42f4bab42"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc190(),m.publication164(),m.membership84()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3609123840//6265840==t["epoch189_complete_seed_states"]==576 and 3609123840%6265840==0
assert (t["accepted"],t["deadline_vectors"],t["epoch190_bound_eighty_first_source_handoff_states"],t["epoch190_bound_eighty_first_source_binding_states"],t["epoch190_bound_verifier_binding_states"])==(25719063552,6378736,18370759680,11022455808,3674151936) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 168625317888//6099006==s["bound_one_hundred_sixty_third_restart_seed_states"]==27648 and 168625317888%6099006==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_fourth_restart_states"],s["bound_one_hundred_sixty_fourth_restart_recoveries"])==(1888602946560,6209895,1545220592640,1201838238720,858455884800,515073530880,171691176960) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4551978200//5989445==b["bound_quorum_churn_seed_states"]==760 and 4551978200%5989445==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root84_witness_rebind_states"],b["bound_root84_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(32446711920,6099006,23176222800,13905733680,4635244560) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v239.py","winloop_v239.json","winloop_v239_report.md","winloop_v239_validate.py"}
seen=set()
for line in (H/"winloop_v239_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v239.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="b411292e695de9e34b42ca5eeb1d1483b2aeb032d7d7808abbdfb534adc64cee"
print(json.dumps({"version":"V239","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

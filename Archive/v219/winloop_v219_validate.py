#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v219 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v219.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V219" and a["base"]=={"version":"V218","digest":"cf01c740ed5953098e5203e235fc3e9c1d4b4b45572900a030930011ea00e2f6","implementation_sha256":"db3babd9d8463385103551f5aa33cf16d59b04eb3a4ab3274f3ec75faf34868f"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc170(),m.publication144(),m.membership74()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2464519680//4278680==t["epoch169_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(17604905472,4366296)
assert (t["epoch170_bound_seventy_first_source_handoff_states"],t["epoch170_bound_seventy_first_source_binding_states"],t["epoch170_bound_verifier_binding_states"])==(12574932480,7544959488,2514986496) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 114724435968//4149466==s["bound_one_hundred_forty_third_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_fourth_restart_recoveries"])==(1288077880320,4235315,117097989120)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_fourth_restart_states"])==(1053881902080,819685923840,585489945600,351293967360) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3089236600//4064785==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(22075159120,4149466)
assert (b["bound_root74_witness_rebind_states"],b["bound_root74_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(15767970800,9460782480,3153594160) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v219.py","winloop_v219.json","winloop_v219_report.md","winloop_v219_validate.py"}; seen=set()
for line in (H/"winloop_v219_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v219.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="bdd9099d31d841569264ab616de4002c3f62c8d73bee3a2c18871af0c8715ac1"
print(json.dumps({"version":"V219","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

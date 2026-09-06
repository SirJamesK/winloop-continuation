#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v238 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v238.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V238" and a["base"]=={"version":"V237","digest":"01deee922875c4c8dd58991e21edde9ef9c45b29ae1f0cf238666a9ff71aa619","implementation_sha256":"3e51dd4b92d6d15cb946dc28d7f223a8ddf4369b634c91ac910d292b7921ab7a"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc189(),m.publication163(),m.membership84()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3544867584//6154284==t["epoch188_complete_seed_states"]==576 and 3544867584%6154284==0
assert (t["accepted"],t["deadline_vectors"],t["epoch189_bound_eightieth_lineage_rotation_states"],t["epoch189_bound_eightieth_lineage_binding_states"],t["epoch189_bound_handed_proof_rebind_states"],t["epoch189_bound_verifier_binding_states"])==(32482114560,6265840,25263866880,18045619200,10827371520,3609123840) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 165596175360//5989445==s["bound_one_hundred_sixty_second_restart_seed_states"]==27648 and 165596175360%5989445==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_third_restart_states"],s["bound_one_hundred_sixty_third_restart_recoveries"])==(1854878496768,6099006,1517627860992,1180377225216,843126589440,505875953664,168625317888) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4469715040//5881204==b["bound_quorum_churn_seed_states"]==760 and 4469715040%5881204==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root84_rollover_states"],b["bound_root84_binding_states"],b["bound_replication_quorum_churn_states"])==(50071760200,5989445,40967803800,22759891000,13655934600,4551978200) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v238.py","winloop_v238.json","winloop_v238_report.md","winloop_v238_validate.py"}
seen=set()
for line in (H/"winloop_v238_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v238.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="121e245f32f30eeed75f38c99deacf287b322a7e28cedb3f8ec89a296b8322f7"
print(json.dumps({"version":"V238","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

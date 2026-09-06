#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v222 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v222.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V222" and a["base"]=={"version":"V221","digest":"b959ce47a9d1f4b7ab87297888577a4a509b5d0b1f7774e6be60e8d179cc6cbd","implementation_sha256":"b2a95f2c2f9cc3c2472b9662d35c1161161699daba398a85b8cb0d52a2db2ba2"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc173(),m.publication147(),m.membership76()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2617977600//4545100==t["epoch172_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(24034599936,4636304)
assert (t["epoch173_bound_seventy_second_lineage_rotation_states"],t["epoch173_bound_seventy_second_lineage_binding_states"],t["epoch173_bound_handed_proof_rebind_states"],t["epoch173_bound_verifier_binding_states"])==(18693577728,13352555520,8011533312,2670511104) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 121942858752//4410549==s["bound_one_hundred_forty_sixth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_seventh_restart_recoveries"])==(1368560793600,4499950,124414617600)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_seventh_restart_states"])==(1119731558400,870902323200,622073088000,373243852800) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3284978400//4322340==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(36872189640,4410549)
assert (b["bound_witness_source_replacement_states"],b["bound_root76_rollover_states"],b["bound_root76_binding_states"],b["bound_replication_quorum_churn_states"])==(30168155160,16760086200,10056051720,3352017240) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v222.py","winloop_v222.json","winloop_v222_report.md","winloop_v222_validate.py"}; seen=set()
for line in (H/"winloop_v222_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v222.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="8c68646e4126e35e3388fd07ec0fd03d75dd8a622752806a7f3af36295215770"
print(json.dumps({"version":"V222","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

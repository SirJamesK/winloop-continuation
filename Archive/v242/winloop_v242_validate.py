#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v242 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v242.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V242" and a["base"]=={"version":"V241","digest":"e9654fac5dd38764f680f9078b672010ba80fadad1a664519642cbe68e8a9e26","implementation_sha256":"4aabd6f6898dce6a40954ccd863de6a81299eee8d8cb48e34d42e1448db170af"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc193(),m.publication167(),m.membership86()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3806542080//6608580==t["epoch192_complete_seed_states"]==576 and 3806542080%6608580==0
assert (t["accepted"],t["deadline_vectors"],t["epoch193_bound_eighty_second_lineage_rotation_states"],t["epoch193_bound_eighty_second_lineage_binding_states"],t["epoch193_bound_handed_proof_rebind_states"],t["epoch193_bound_verifier_binding_states"])==(34865220096,6725544,27117393408,19369566720,11621740032,3873913344) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 177933929472//6435689==s["bound_one_hundred_sixty_sixth_restart_seed_states"]==27648 and 177933929472%6435689==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_seventh_restart_states"],s["bound_one_hundred_sixty_seventh_restart_recoveries"])==(1992223918080,6550610,1630001387520,1267778856960,905556326400,543333795840,181111265280) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4804811200//6322120==b["bound_quorum_churn_seed_states"]==760 and 4804811200%6322120==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root86_rollover_states"],b["bound_root86_binding_states"],b["bound_replication_quorum_churn_states"])==(53802360040,6435689,44020112760,24455618200,14673370920,4891123640) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v242.py","winloop_v242.json","winloop_v242_report.md","winloop_v242_validate.py"}
seen=set()
for line in (H/"winloop_v242_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v242.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="f00c67e9e71692faa47967ce377745ec39c56ccec1220894a1db8a72c5b7a1ed"
print(json.dumps({"version":"V242","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

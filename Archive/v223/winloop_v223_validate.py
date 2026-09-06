#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v223 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v223.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V223" and a["base"]=={"version":"V222","digest":"8c68646e4126e35e3388fd07ec0fd03d75dd8a622752806a7f3af36295215770","implementation_sha256":"37e040bfa868b7ddeb33234fa0a8f179a6bcb913fa8e4d5ff8d49cf463ed24cb"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc174(),m.publication148(),m.membership76()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2670511104//4636304==t["epoch173_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(19066199040,4728720)
assert (t["epoch174_bound_seventy_third_source_handoff_states"],t["epoch174_bound_seventy_third_source_binding_states"],t["epoch174_bound_verifier_binding_states"])==(13618713600,8171228160,2723742720) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 124414617600//4499950==s["bound_one_hundred_forty_seventh_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_eighth_restart_recoveries"])==(1396115094528,4590551,126919554048)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_eighth_restart_states"])==(1142275986432,888436878336,634597770240,380758662144) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3352017240//4410549==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(23939734000,4499950)
assert (b["bound_root76_witness_rebind_states"],b["bound_root76_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(17099810000,10259886000,3419962000) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v223.py","winloop_v223.json","winloop_v223_report.md","winloop_v223_validate.py"}; seen=set()
for line in (H/"winloop_v223_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v223.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="62d96c27f3c96895071e075642c995453acc0829eaf6d17eb07d97cea65fa9e9"
print(json.dumps({"version":"V223","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

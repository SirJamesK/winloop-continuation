#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v250 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v250.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V250" and a["base"]=={"version":"V249","digest":"8cf21664fe3ffffbd48f0a71a6d92f7c5b87a48a3fddaef99107399fd52632bc","implementation_sha256":"36e7e10f5b7157496c633e8c5dfea9fa5b73e59674ee79c8b84c002e12e2242a"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc201(),m.publication175(),m.membership90()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4367897856//7583156==t["epoch200_complete_seed_states"]==576 and 4367897856%7583156==0
assert (t["accepted"],t["deadline_vectors"],t["epoch201_bound_eighty_sixth_lineage_rotation_states"],t["epoch201_bound_eighty_sixth_lineage_binding_states"],t["epoch201_bound_handed_proof_rebind_states"],t["epoch201_bound_verifier_binding_states"])==(39975482880,7711320,31092042240,22208601600,13325160960,4441720320) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 204417838080//7393585==s["bound_one_hundred_seventy_fourth_restart_seed_states"]==27648 and 204417838080%7393585==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventy_fifth_restart_states"],s["bound_one_hundred_seventy_fifth_restart_recoveries"])==(2286923950080,7519610,1871119595520,1455315240960,1039510886400,623706531840,207902177280) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5524421760//7268976==b["bound_quorum_churn_seed_states"]==760 and 5524421760%7268976==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root90_rollover_states"],b["bound_root90_binding_states"],b["bound_replication_quorum_churn_states"])==(61810370600,7393585,50572121400,28095623000,16857373800,5619124600) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v250.py","winloop_v250.json","winloop_v250_report.md","winloop_v250_validate.py"}
seen=set()
for line in (H/"winloop_v250_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v250.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="d23b85e71f6792aa0fa159af5cd5c76170beff3f2d50dc8dce8ed662336c1b95"
print(json.dumps({"version":"V250","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v218 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v218.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V218" and a["base"]=={"version":"V217","digest":"5ffe5d638e87cce710b96b9da77f92110cdc014beaabaf30d3fae1ff02a6980d","implementation_sha256":"46b21bfad0f7b8e243d077dd28ea35dd7c1d8d8c01d4d1267a40fd214f6bbf48"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc169(),m.publication143(),m.membership74()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2414732544//4192244==t["epoch168_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(22180677120,4278680)
assert (t["epoch169_bound_seventieth_lineage_rotation_states"],t["epoch169_bound_seventieth_lineage_binding_states"],t["epoch169_bound_handed_proof_rebind_states"],t["epoch169_bound_verifier_binding_states"])==(17251637760,12322598400,7393559040,2464519680) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 112383175680//4064785==s["bound_one_hundred_forty_second_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_third_restart_recoveries"])==(1261968795648,4149466,114724435968)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_third_restart_states"])==(1032519923712,803071051776,573622179840,344173307904) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3025760640//3981264==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(33981602600,4064785)
assert (b["bound_witness_source_replacement_states"],b["bound_root74_rollover_states"],b["bound_root74_binding_states"],b["bound_replication_quorum_churn_states"])==(27803129400,15446183000,9267709800,3089236600) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v218.py","winloop_v218.json","winloop_v218_report.md","winloop_v218_validate.py"}; seen=set()
for line in (H/"winloop_v218_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v218.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="cf01c740ed5953098e5203e235fc3e9c1d4b4b45572900a030930011ea00e2f6"
print(json.dumps({"version":"V218","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

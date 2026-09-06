#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v227 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v227.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V227" and a["base"]=={"version":"V226","digest":"28ba0ac5011094061962ae84c33557e5fdcf50f57e50434b171df865d853a593","implementation_sha256":"680e5d510e2fbe06505e0a60f1ba80967e99c49b4f1460c656bdaa56461b679c"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc178(),m.publication152(),m.membership78()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2887672320//5013320==t["epoch177_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(20606197248,5110664)
assert (t["epoch178_bound_seventy_fifth_source_handoff_states"],t["epoch178_bound_seventy_fifth_source_binding_states"],t["epoch178_bound_verifier_binding_states"])==(14718712320,8831227392,2943742464) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 134635640832//4869634==s["bound_one_hundred_fifty_first_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_second_restart_recoveries"])==(1510030494720,4965115,137275499520)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_second_restart_states"])==(1235479495680,960928496640,686377497600,411826498560) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3629292600//4775385==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(25906452880,4869634)
assert (b["bound_root78_witness_rebind_states"],b["bound_root78_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(18504609200,11102765520,3700921840) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v227.py","winloop_v227.json","winloop_v227_report.md","winloop_v227_validate.py"}; seen=set()
for line in (H/"winloop_v227_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v227.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="bee0d1231718e8ae5d97a97dfa5871b670634456cc738a5e2d6fb7401c92f916"
print(json.dumps({"version":"V227","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v221 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v221.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V221" and a["base"]=={"version":"V220","digest":"5a51addc1c5f6efbbe22a502fca579bbccc3c2dce87d9669493b81b06baff4a9","implementation_sha256":"4f0a5db251997806c847faa8be14d427f8c97d01ae8a1860554ab1b085e5d2f6"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc172(),m.publication146(),m.membership75()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2566137600//4455100==t["epoch171_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(18325843200,4545100)
assert (t["epoch172_bound_seventy_second_source_handoff_states"],t["epoch172_bound_seventy_second_source_binding_states"],t["epoch172_bound_verifier_binding_states"])==(13089888000,7853932800,2617977600) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 119504056320//4322340==s["bound_one_hundred_forty_fifth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_sixth_restart_recoveries"])==(1341371446272,4410549,121942858752)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_sixth_restart_states"])==(1097485728768,853600011264,609714293760,365828576256) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3218839400//4235315==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(22994848800,4322340)
assert (b["bound_root75_witness_rebind_states"],b["bound_root75_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(16424892000,9854935200,3284978400) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v221.py","winloop_v221.json","winloop_v221_report.md","winloop_v221_validate.py"}; seen=set()
for line in (H/"winloop_v221_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v221.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="b959ce47a9d1f4b7ab87297888577a4a509b5d0b1f7774e6be60e8d179cc6cbd"
print(json.dumps({"version":"V221","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

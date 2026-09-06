#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v229 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v229.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V229" and a["base"]=={"version":"V228","digest":"0eb5549425df420666343bb7fecfe5f959ab400670b085c32d787087057934b0","implementation_sha256":"93550fdd62e82c42076718ee41ff33cff1b5c457a02287515b4d8819155d4561"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc180(),m.publication154(),m.membership79()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 3000533760//5209260==t["epoch179_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(21406355712,5309116)
assert (t["epoch180_bound_seventy_sixth_source_handoff_states"],t["epoch180_bound_seventy_sixth_source_binding_states"],t["epoch180_bound_verifier_binding_states"])==(15290254080,9174152448,3058050816) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 139949641728//5061836==s["bound_one_hundred_fifty_third_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_fourth_restart_recoveries"])==(1569241175040,5159805,142658288640)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_fourth_restart_states"])==(1283924597760,998608020480,713291443200,427974865920) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3773487400//4965115==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(26928967520,5061836)
assert (b["bound_root79_witness_rebind_states"],b["bound_root79_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(19234976800,11540986080,3846995360) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v229.py","winloop_v229.json","winloop_v229_report.md","winloop_v229_validate.py"}; seen=set()
for line in (H/"winloop_v229_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v229.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="75d49af78020fc3fe6390d52ddaac5253d052f986501f371577c8c35c41c7715"
print(json.dumps({"version":"V229","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

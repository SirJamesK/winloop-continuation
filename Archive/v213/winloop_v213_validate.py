#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v213 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v213.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V213" and a["base"]=={"version":"V212","digest":"86410329f2ae2218a9aef778c75b26b5f413df3ade426332f764b1bf02800aca","implementation_sha256":"254924e5c1a33df239b28b9257853dcca3631bb7cbbfd7315733ebee279bd212"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc164(),m.publication138(),m.membership71()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2175830784//3777484==t["epoch163_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(15556020480,3858140)
assert (t["epoch164_bound_sixty_eighth_source_handoff_states"],t["epoch164_bound_sixty_eighth_source_binding_states"],t["epoch164_bound_verifier_binding_states"])==(11111443200,6666865920,2222288640) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 101153525760//3658620==s["bound_one_hundred_thirty_seventh_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_eighth_restart_recoveries"])==(1136703034368,3737581,103336639488)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_eighth_restart_states"])==(930029755392,723356476416,516683197440,310009918464) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2721392040//3580779==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(19463858400,3658620)
assert (b["bound_root71_witness_rebind_states"],b["bound_root71_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(13902756000,8341653600,2780551200) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v213.py","winloop_v213.json","winloop_v213_report.md","winloop_v213_validate.py"}; seen=set()
for line in (H/"winloop_v213_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v213.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="b19bc005d17f5a2aeaef039192765e52ca6bfe71e83bd4860c0e2cc211f06bbd"
print(json.dumps({"version":"V213","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v251 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v251.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V251" and a["base"]=={"version":"V250","digest":"d23b85e71f6792aa0fa159af5cd5c76170beff3f2d50dc8dce8ed662336c1b95","implementation_sha256":"f61d8efcf9d68136b056aaa4f38457b2b5321a268d6562fcead98a235cdad58b"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc202(),m.publication176(),m.membership90()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4441720320//7711320==t["epoch201_complete_seed_states"]==576 and 4441720320%7711320==0
assert (t["accepted"],t["deadline_vectors"],t["epoch202_bound_eighty_seventh_source_handoff_states"],t["epoch202_bound_eighty_seventh_source_binding_states"],t["epoch202_bound_verifier_binding_states"])==(31614589440,7840920,22581849600,13549109760,4516369920) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 207902177280//7519610==s["bound_one_hundred_seventy_fifth_restart_seed_states"]==27648 and 207902177280%7519610==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventy_sixth_restart_states"],s["bound_one_hundred_seventy_sixth_restart_recoveries"])==(2325684759552,7647059,1902832985088,1479981210624,1057129436160,634277661696,211425887232) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5619124600//7393585==b["bound_quorum_churn_seed_states"]==760 and 5619124600%7393585==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root90_witness_rebind_states"],b["bound_root90_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(40004325200,7519610,28574518000,17144710800,5714903600) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v251.py","winloop_v251.json","winloop_v251_report.md","winloop_v251_validate.py"}
seen=set()
for line in (H/"winloop_v251_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v251.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="41d57be0cd6ddedde3f3b8714a1a677d169178fd7ed4ebbbd3885ca71023fe82"
print(json.dumps({"version":"V251","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

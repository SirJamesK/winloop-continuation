#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v209 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v209.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V209" and a["base"]=={"version":"V208","digest":"8b03425d3a0b11a36fc92d977ab32ed05c18f62d473f9bfab5a037fec9fb355f","implementation_sha256":"116605149892b04e581afb22a033fc7796e787843bc88b14ea129eb1d57688cb"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc160(),m.publication134(),m.membership69()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 1996473600//3466100==t["epoch159_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(14282456832,3542276)
assert (t["epoch160_bound_sixty_sixth_source_handoff_states"],t["epoch160_bound_sixty_sixth_source_binding_states"],t["epoch160_bound_verifier_binding_states"])==(10201754880,6121052928,2040350976) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 92728516608//3353896==s["bound_one_hundred_thirty_third_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_fourth_restart_recoveries"])==(1042680038400,3428425,94789094400)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_fourth_restart_states"])==(853101849600,663523660800,473945472000,284367283200) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2493145800//3280455==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(17842726720,3353896)
assert (b["bound_root69_witness_rebind_states"],b["bound_root69_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(12744804800,7646882880,2548960960) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v209.py","winloop_v209.json","winloop_v209_report.md","winloop_v209_validate.py"}; seen=set()
for line in (H/"winloop_v209_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v209.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="12fe74145786781b6b04b6b59ad22aad66ef4b0a83d75656d856c30b1b8feaad"
print(json.dumps({"version":"V209","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

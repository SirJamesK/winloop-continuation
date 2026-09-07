#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v243 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v243.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V243" and a["base"]=={"version":"V242","digest":"f00c67e9e71692faa47967ce377745ec39c56ccec1220894a1db8a72c5b7a1ed","implementation_sha256":"8e53a18bad17b41650dd63b6f4382cf7db1331bae22b9c0dee6b0ef933071e92"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc194(),m.publication168(),m.membership86()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3873913344//6725544==t["epoch193_complete_seed_states"]==576 and 3873913344%6725544==0
assert (t["accepted"],t["deadline_vectors"],t["epoch194_bound_eighty_third_source_handoff_states"],t["epoch194_bound_eighty_third_source_binding_states"],t["epoch194_bound_verifier_binding_states"])==(27594524160,6843880,19710374400,11826224640,3942074880) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 181111265280//6550610==s["bound_one_hundred_sixty_seventh_restart_seed_states"]==27648 and 181111265280%6550610==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_eighth_restart_states"],s["bound_one_hundred_sixty_eighth_restart_recoveries"])==(2027588226048,6666891,1658935821312,1290283416576,921631011840,552978607104,184326202368) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4891123640//6435689==b["bound_quorum_churn_seed_states"]==760 and 4891123640%6435689==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root86_witness_rebind_states"],b["bound_root86_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(34849245200,6550610,24892318000,14935390800,4978463600) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v243.py","winloop_v243.json","winloop_v243_report.md","winloop_v243_validate.py"}
seen=set()
for line in (H/"winloop_v243_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v243.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="f70030ddf88d76acf59cd8f740777be829ded52728ba6d200cf808eab2f4cda7"
print(json.dumps({"version":"V243","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

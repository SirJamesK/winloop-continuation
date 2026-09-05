#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v206 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v206.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V206" and a["base"]=={"version":"V205","digest":"957098d4751a12cfddb45d6160d39d27cda0bc3c6c8f8fc78bcabe88ffc9be1b","implementation_sha256":"1e096a7297f73fe97f81c594332fbb4dff846d78aef2e52134cb1e245e868b22"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc157(),m.publication131(),m.membership68()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 1868624640//3244140==t["epoch156_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(17195535360,3317040)
assert (t["epoch157_bound_sixty_fourth_lineage_rotation_states"],t["epoch157_bound_sixty_fourth_lineage_binding_states"],t["epoch157_bound_handed_proof_rebind_states"],t["epoch157_bound_verifier_binding_states"])==(13374305280,9553075200,5731845120,1910615040) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 86726384640//3136805==s["bound_one_hundred_thirtieth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_first_restart_recoveries"])==(975671212032,3208094,88697382912)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_first_restart_states"])==(798276446208,620881680384,443486914560,266092148736) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2330600800//3066580==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(26223689800,3136805)
assert (b["bound_witness_source_replacement_states"],b["bound_root68_rollover_states"],b["bound_root68_binding_states"],b["bound_replication_quorum_churn_states"])==(21455746200,11919859000,7151915400,2383971800) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v206.py","winloop_v206.json","winloop_v206_report.md","winloop_v206_validate.py"}; seen=set()
for line in (H/"winloop_v206_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v206.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="a280c66dcf39c5a68b012468dca72bac5a9a3dcf0906854bae79bacc404a13b0"
print(json.dumps({"version":"V206","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

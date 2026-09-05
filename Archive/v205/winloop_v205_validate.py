#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v205 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v205.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V205" and a["base"]=={"version":"V204","digest":"0e6109cdd8cf63f2f75e25c996416750792ce26749266c55f17c1b46267beaa4","implementation_sha256":"1905abfdd9ce4f9ba6e34f0fcb87777a230455a6d34e1466cd4c10b65b0d460d"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc156(),m.publication130(),m.membership67()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 1827254016//3172316==t["epoch155_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(13080372480,3244140)
assert (t["epoch156_bound_sixty_fourth_source_handoff_states"],t["epoch156_bound_sixty_fourth_source_binding_states"],t["epoch156_bound_verifier_binding_states"])==(9343123200,5605873920,1868624640) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 84784803840//3066580==s["bound_one_hundred_twenty_ninth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirtieth_restart_recoveries"])==(953990231040,3136805,86726384640)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirtieth_restart_states"])==(780537461760,607084692480,433631923200,260179153920) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2278032360//2997411==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(16314205600,3066580)
assert (b["bound_root67_witness_rebind_states"],b["bound_root67_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(11653004000,6991802400,2330600800) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v205.py","winloop_v205.json","winloop_v205_report.md","winloop_v205_validate.py"}; seen=set()
for line in (H/"winloop_v205_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v205.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="957098d4751a12cfddb45d6160d39d27cda0bc3c6c8f8fc78bcabe88ffc9be1b"
print(json.dumps({"version":"V205","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

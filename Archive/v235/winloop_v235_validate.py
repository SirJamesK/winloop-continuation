#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v235 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v235.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V235" and a["base"]=={"version":"V234","digest":"5571e2e304639ebfa7a307b44a0cab6853bba517d07db3d5085521db7a7fcf77","implementation_sha256":"8337d74a4aac26d3257955f31ed8b416540338b9468f39700e337507e62a55de"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc186(),m.publication160(),m.membership82()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3356683776//5827576==t["epoch185_complete_seed_states"]==576 and 3356683776%5827576==0
assert (t["accepted"],t["deadline_vectors"],t["epoch186_bound_seventy_ninth_source_handoff_states"],t["epoch186_bound_seventy_ninth_source_binding_states"],t["epoch186_bound_verifier_binding_states"])==(23930565120,5935160,17093260800,10255956480,3418652160) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 156726835200//5668650==s["bound_one_hundred_fifty_ninth_restart_seed_states"]==27648 and 156726835200%5668650==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixtieth_restart_states"],s["bound_one_hundred_sixtieth_restart_recoveries"])==(1756118707200,5774275,1436824396800,1117530086400,798235776000,478941465600,159647155200) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4228883960//5564321==b["bound_quorum_churn_seed_states"]==760 and 4228883960%5564321==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root82_witness_rebind_states"],b["bound_root82_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(30157218000,5668650,21540870000,12924522000,4308174000) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v235.py","winloop_v235.json","winloop_v235_report.md","winloop_v235_validate.py"}
seen=set()
for line in (H/"winloop_v235_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v235.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="b70205c56c999805490005e930346414ec3fe858800ec3e85e35b2454a3dc5c6"
print(json.dumps({"version":"V235","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

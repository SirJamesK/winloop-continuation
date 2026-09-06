#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v236 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v236.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V236" and a["base"]=={"version":"V235","digest":"b70205c56c999805490005e930346414ec3fe858800ec3e85e35b2454a3dc5c6","implementation_sha256":"25b80917e7172b2a486c8bf3d3c65cd3c6e50013e0480c6983b1a0f603155a11"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc187(),m.publication161(),m.membership83()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3418652160//5935160==t["epoch186_complete_seed_states"]==576 and 3418652160%5935160==0
assert (t["accepted"],t["deadline_vectors"],t["epoch187_bound_seventy_ninth_lineage_rotation_states"],t["epoch187_bound_seventy_ninth_lineage_binding_states"],t["epoch187_bound_handed_proof_rebind_states"],t["epoch187_bound_verifier_binding_states"])==(31332407040, 6044060, 24369649920, 17406892800, 10444135680, 3481378560) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 159647155200//5774275==s["bound_one_hundred_sixtieth_restart_seed_states"]==27648 and 159647155200%5774275==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_first_restart_states"],s["bound_one_hundred_sixty_first_restart_recoveries"])==(1788638810112, 5881204, 1463431753728, 1138224697344, 813017640960, 487810584576, 162603528192) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4308174000//5668650==b["bound_quorum_churn_seed_states"]==760 and 4308174000%5668650==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root83_rollover_states"],b["bound_root83_binding_states"],b["bound_replication_quorum_churn_states"])==(48272939000, 5774275, 39496041000, 21942245000, 13165347000, 4388449000) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v236.py","winloop_v236.json","winloop_v236_report.md","winloop_v236_validate.py"}
seen=set()
for line in (H/"winloop_v236_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v236.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="2a95cce899a035bc349fbf013ccacdd426fbc624b07a281aff1065a154dc3ea7"
print(json.dumps({"version":"V236","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

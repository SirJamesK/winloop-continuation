#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v237 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v237.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V237" and a["base"]=={"version":"V236","digest":"2a95cce899a035bc349fbf013ccacdd426fbc624b07a281aff1065a154dc3ea7","implementation_sha256":"7a7593a0a2f52c29fb2806db426014389d3720c3d04550c801ccce4eead1b813"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc188(),m.publication162(),m.membership83()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3481378560//6044060==t["epoch187_complete_seed_states"]==576 and 3481378560%6044060==0
assert (t["accepted"],t["deadline_vectors"],t["epoch188_bound_eightieth_source_handoff_states"],t["epoch188_bound_eightieth_source_binding_states"],t["epoch188_bound_verifier_binding_states"])==(24814073088,6154284,17724337920,10634602752,3544867584) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 162603528192//5881204==s["bound_one_hundred_sixty_first_restart_seed_states"]==27648 and 162603528192%5881204==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_second_restart_states"],s["bound_one_hundred_sixty_second_restart_recoveries"])==(1821557928960,5989445,1490365578240,1159173227520,827980876800,496788526080,165596175360) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4388449000//5774275==b["bound_quorum_churn_seed_states"]==760 and 4388449000%5774275==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root83_witness_rebind_states"],b["bound_root83_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(31288005280,5881204,22348575200,13409145120,4469715040) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v237.py","winloop_v237.json","winloop_v237_report.md","winloop_v237_validate.py"}
seen=set()
for line in (H/"winloop_v237_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v237.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="01deee922875c4c8dd58991e21edde9ef9c45b29ae1f0cf238666a9ff71aa619"
print(json.dumps({"version":"V237","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

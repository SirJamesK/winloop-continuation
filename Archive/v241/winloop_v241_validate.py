#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v241 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v241.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V241" and a["base"]=={"version":"V240","digest":"af32248521f4a70a41d31a5f58008eb994a52f16124f9be3cb41b2d0c3701f81","implementation_sha256":"8a327849dec26c1f26de2cf0a71dd1bf60d7e1e1169fccc3d780bc0dfdc6e39a"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc192(),m.publication166(),m.membership85()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3806542080//6608580==t["epoch191_complete_seed_states"]==576 and 3806542080%6608580==0
assert (t["accepted"],t["deadline_vectors"],t["epoch192_bound_eighty_second_source_handoff_states"],t["epoch192_bound_eighty_second_source_binding_states"],t["epoch192_bound_verifier_binding_states"])==(26645794560,6608580,19032710400,11419626240,3806542080) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 177933929472//6435689==s["bound_one_hundred_sixty_fifth_restart_seed_states"]==27648 and 177933929472%6435689==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_sixth_restart_states"],s["bound_one_hundred_sixty_sixth_restart_recoveries"])==(1957273224192,6435689,1601405365248,1245537506304,889669647360,533801788416,177933929472) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4804811200//6322120==b["bound_quorum_churn_seed_states"]==760 and 4804811200%6322120==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root85_witness_rebind_states"],b["bound_root85_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(33633678400,6322120,24024056000,14414433600,4804811200) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v241.py","winloop_v241.json","winloop_v241_report.md","winloop_v241_validate.py"}
seen=set()
for line in (H/"winloop_v241_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v241.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="e9654fac5dd38764f680f9078b672010ba80fadad1a664519642cbe68e8a9e26"
print(json.dumps({"version":"V241","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

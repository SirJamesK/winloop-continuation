#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v240 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v240.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V240" and a["base"]=={"version":"V239","digest":"b411292e695de9e34b42ca5eeb1d1483b2aeb032d7d7808abbdfb534adc64cee","implementation_sha256":"249eb4e15eb07326bed2a7185868660bb002c73848b82367adb22df61d29e084"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc191(),m.publication165(),m.membership85()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3674151936//6378736==t["epoch190_complete_seed_states"]==576 and 3674151936%6378736==0
assert (t["accepted"],t["deadline_vectors"],t["epoch191_bound_eighty_first_lineage_rotation_states"],t["epoch191_bound_eighty_first_lineage_binding_states"],t["epoch191_bound_handed_proof_rebind_states"],t["epoch191_bound_verifier_binding_states"])==(33659608320,6492980,26179695360,18699782400,11219869440,3739956480) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 171691176960//6209895==s["bound_one_hundred_sixty_fourth_restart_seed_states"]==27648 and 171691176960%6209895==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_fifth_restart_states"],s["bound_one_hundred_sixty_fifth_restart_recoveries"])==(1922733711360,6322120,1573145763840,1223557816320,873969868800,524381921280,174793973760) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4635244560//6099006==b["bound_quorum_churn_seed_states"]==760 and 4635244560%6099006==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root85_rollover_states"],b["bound_root85_binding_states"],b["bound_replication_quorum_churn_states"])==(51914722200,6209895,42475681800,23597601000,14158560600,4719520200) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v240.py","winloop_v240.json","winloop_v240_report.md","winloop_v240_validate.py"}
seen=set()
for line in (H/"winloop_v240_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v240.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="af32248521f4a70a41d31a5f58008eb994a52f16124f9be3cb41b2d0c3701f81"
print(json.dumps({"version":"V240","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

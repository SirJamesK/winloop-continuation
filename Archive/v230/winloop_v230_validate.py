#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v230 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v230.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V230" and a["base"]=={"version":"V229","digest":"75d49af78020fc3fe6390d52ddaac5253d052f986501f371577c8c35c41c7715","implementation_sha256":"d4e6d09fe78d9fd549bbebc2d933700103d986cbbd310e06278757b830207e2c"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc181(),m.publication155(),m.membership80()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 3058050816//5309116==t["epoch180_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(28046684160,5410240)
assert (t["epoch181_bound_seventy_sixth_lineage_rotation_states"],t["epoch181_bound_seventy_sixth_lineage_binding_states"],t["epoch181_bound_handed_proof_rebind_states"],t["epoch181_bound_verifier_binding_states"])==(21814087680,15581491200,9348894720,3116298240) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 142658288640//5159805==s["bound_one_hundred_fifty_fourth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_fifth_restart_recoveries"])==(1599418275840,5259030,145401661440)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_fifth_restart_states"])==(1308614952960,1017811630080,727008307200,436204984320) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3846995360//5061836==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(43135969800,5159805)
assert (b["bound_witness_source_replacement_states"],b["bound_root80_rollover_states"],b["bound_root80_binding_states"],b["bound_replication_quorum_churn_states"])==(35293066200,19607259000,11764355400,3921451800) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v230.py","winloop_v230.json","winloop_v230_report.md","winloop_v230_validate.py"}; seen=set()
for line in (H/"winloop_v230_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v230.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="d5e0a635fbf37664c71ee096996ee93d2bc9b2cdeb96838883ec09f6a29d5161"
print(json.dumps({"version":"V230","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

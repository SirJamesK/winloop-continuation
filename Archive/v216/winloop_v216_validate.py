#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v216 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v216.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V216" and a["base"]=={"version":"V215","digest":"b790801c1fff32a8555ea54edd9c7a1bc69a34f4d63b1ddbce5682dc72e260cb","implementation_sha256":"b175b40f185ee83650a29815e6269241bcaf83da744a1b7a71e36d4c28432a9e"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc167(),m.publication141(),m.membership73()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2317178880//4022880==t["epoch166_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(21290584320,4106980)
assert (t["epoch167_bound_sixty_ninth_lineage_rotation_states"],t["epoch167_bound_sixty_ninth_lineage_binding_states"],t["epoch167_bound_handed_proof_rebind_states"],t["epoch167_bound_verifier_binding_states"])==(16559343360,11828102400,7096861440,2365620480) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 107796648960//3898895==s["bound_one_hundred_fortieth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_first_restart_recoveries"])==(1210813857792,3981264,110073987072)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_first_restart_states"])==(990665883648,770517909504,550369935360,330221961216) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2901429200//3817670==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(32594762200,3898895)
assert (b["bound_witness_source_replacement_states"],b["bound_root73_rollover_states"],b["bound_root73_binding_states"],b["bound_replication_quorum_churn_states"])==(26668441800,14815801000,8889480600,2963160200) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v216.py","winloop_v216.json","winloop_v216_report.md","winloop_v216_validate.py"}; seen=set()
for line in (H/"winloop_v216_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v216.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="d075f685dd19d79eed4c7b23d8fcb1a7ee60fede5ec4052f4f0d8a463c11f203"
print(json.dumps({"version":"V216","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

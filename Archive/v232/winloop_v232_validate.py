#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v232 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v232.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V232" and a["base"]=={"version":"V231","digest":"ae9d708d92b06b2d0c3c9e7b9c5705fd65ffd01f4b66c7519f50fa66e13ed394","implementation_sha256":"735359628967d5673323a32366b14492c4b831399073c9a2882b26fa10e12752"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc183(),m.publication157(),m.membership81()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 3175280640//5512640==t["epoch182_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(29115023616,5616324)
assert (t["epoch183_bound_seventy_seventh_lineage_rotation_states"],t["epoch183_bound_seventy_seventh_lineage_binding_states"],t["epoch183_bound_handed_proof_rebind_states"],t["epoch183_bound_verifier_binding_states"])==(22645018368,16175013120,9705007872,3235002624) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 148179981312//5359519==s["bound_one_hundred_fifty_sixth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_seventh_restart_recoveries"])==(1660928163840,5461280,150993469440)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_seventh_restart_states"])==(1358941224960,1056954286080,754967347200,452980408320) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3996862800//5259030==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(44805578840,5359519)
assert (b["bound_witness_source_replacement_states"],b["bound_root81_rollover_states"],b["bound_root81_binding_states"],b["bound_replication_quorum_churn_states"])==(36659109960,20366172200,12219703320,4073234440) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v232.py","winloop_v232.json","winloop_v232_report.md","winloop_v232_validate.py"}; seen=set()
for line in (H/"winloop_v232_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v232.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="f677d1e2fc1362b196b6c412d41f3f444c0f12a90d57355dd16be1caf79de87e"
print(json.dumps({"version":"V232","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

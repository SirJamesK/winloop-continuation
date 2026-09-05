#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v212 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v212.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V212" and a["base"]=={"version":"V211","digest":"f206faf0b46850b0db0abb0309a5ab9d190efbb21d6d22ea7ef1bf425d499b92","implementation_sha256":"668bf61a9c9df2a50f5b64a02256144322e55fb6db6821f73c59f8d47b8c9115"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc163(),m.publication137(),m.membership71()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2130024960//3697960==t["epoch162_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(19582477056,3777484)
assert (t["epoch163_bound_sixty_seventh_lineage_rotation_states"],t["epoch163_bound_sixty_seventh_lineage_binding_states"],t["epoch163_bound_handed_proof_rebind_states"],t["epoch163_bound_verifier_binding_states"])==(15230815488,10879153920,6527492352,2175830784) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 99001377792//3580779==s["bound_one_hundred_thirty_sixth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_seventh_restart_recoveries"])==(1112688783360,3658620,101153525760)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_seventh_restart_states"])==(910381731840,708074680320,505767628800,303460577280) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2663078000//3504050==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(29935312440,3580779)
assert (b["bound_witness_source_replacement_states"],b["bound_root71_rollover_states"],b["bound_root71_binding_states"],b["bound_replication_quorum_churn_states"])==(24492528360,13606960200,8164176120,2721392040) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v212.py","winloop_v212.json","winloop_v212_report.md","winloop_v212_validate.py"}; seen=set()
for line in (H/"winloop_v212_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v212.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="86410329f2ae2218a9aef778c75b26b5f413df3ade426332f764b1bf02800aca"
print(json.dumps({"version":"V212","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v248 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v248.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V248" and a["base"]=={"version":"V247","digest":"57bcb3dfe34793d065b9aeb05534a61bbc1e3c1fcfd26acd7f7b88f23447a3f4","implementation_sha256":"7eca83d7f3a31c53294b21bcc942beefa9d2f30d21c1edf5cb89f422b25be73c"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc199(),m.publication173(),m.membership89()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4222715904//7331104==t["epoch198_complete_seed_states"]==576 and 4222715904%7331104==0
assert (t["accepted"],t["deadline_vectors"],t["epoch199_bound_eighty_fifth_lineage_rotation_states"],t["epoch199_bound_eighty_fifth_lineage_binding_states"],t["epoch199_bound_handed_proof_rebind_states"],t["epoch199_bound_verifier_binding_states"])==(38654081280,7456420,30064285440,21474489600,12884693760,4294897920) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 197566387200//7145775==s["bound_one_hundred_seventy_second_restart_seed_states"]==27648 and 197566387200%7145775==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventy_third_restart_states"],s["bound_one_hundred_seventy_third_restart_recoveries"])==(2210699132928,7268976,1808753836032,1406808539136,1004863242240,602917945344,200972648448) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5338220240//7023974==b["bound_quorum_churn_seed_states"]==760 and 5338220240%7023974==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root89_rollover_states"],b["bound_root89_binding_states"],b["bound_replication_quorum_churn_states"])==(59738679000,7145775,48877101000,27153945000,16292367000,5430789000) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v248.py","winloop_v248.json","winloop_v248_report.md","winloop_v248_validate.py"}
seen=set()
for line in (H/"winloop_v248_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v248.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="e870c97516fa22f8756317b401dc465dd0be10f9e8264ccb33db678175c58c9e"
print(json.dumps({"version":"V248","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v214 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v214.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V214" and a["base"]=={"version":"V213","digest":"b19bc005d17f5a2aeaef039192765e52ca6bfe71e83bd4860c0e2cc211f06bbd","implementation_sha256":"75aa4540a8913a9bfde82709e439446134f86ee1f72ff492207265571639c82e"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc165(),m.publication139(),m.membership72()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2222288640//3858140==t["epoch164_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(20424628224,3939936)
assert (t["epoch165_bound_sixty_eighth_lineage_rotation_states"],t["epoch165_bound_sixty_eighth_lineage_binding_states"],t["epoch165_bound_handed_proof_rebind_states"],t["epoch165_bound_verifier_binding_states"])==(15885821952,11347015680,6808209408,2269403136) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 103336639488//3737581==s["bound_one_hundred_thirty_eighth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_ninth_restart_recoveries"])==(1161060341760,3817670,105550940160)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_ninth_restart_states"])==(949958461440,738856581120,527754700800,316652820480) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2780551200//3658620==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(31246177160,3737581)
assert (b["bound_witness_source_replacement_states"],b["bound_root72_rollover_states"],b["bound_root72_binding_states"],b["bound_replication_quorum_churn_states"])==(25565054040,14202807800,8521684680,2840561560) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v214.py","winloop_v214.json","winloop_v214_report.md","winloop_v214_validate.py"}; seen=set()
for line in (H/"winloop_v214_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v214.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="5cead8ef75bda4e6c211afde57c7524cb0061fa33c8384371e6c02d11c0e750a"
print(json.dumps({"version":"V214","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

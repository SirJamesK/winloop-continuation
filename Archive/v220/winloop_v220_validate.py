#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v220 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v220.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V220" and a["base"]=={"version":"V219","digest":"bdd9099d31d841569264ab616de4002c3f62c8d73bee3a2c18871af0c8715ac1","implementation_sha256":"1bbf385305e0ae766d00f589acc46aa18c50b88779f7620f2332101f98a4e1d0"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc171(),m.publication145(),m.membership75()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2514986496//4366296==t["epoch170_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(23095238400,4455100)
assert (t["epoch171_bound_seventy_first_lineage_rotation_states"],t["epoch171_bound_seventy_first_lineage_binding_states"],t["epoch171_bound_handed_proof_rebind_states"],t["epoch171_bound_verifier_binding_states"])==(17962963200,12830688000,7698412800,2566137600) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 117097989120//4235315==s["bound_one_hundred_forty_fourth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_fifth_restart_recoveries"])==(1314544619520,4322340,119504056320)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_fifth_restart_states"])==(1075536506880,836528394240,597520281600,358512168960) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3153594160//4149466==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(35407233400,4235315)
assert (b["bound_witness_source_replacement_states"],b["bound_root75_rollover_states"],b["bound_root75_binding_states"],b["bound_replication_quorum_churn_states"])==(28969554600,16094197000,9656518200,3218839400) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v220.py","winloop_v220.json","winloop_v220_report.md","winloop_v220_validate.py"}; seen=set()
for line in (H/"winloop_v220_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v220.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="5a51addc1c5f6efbbe22a502fca579bbccc3c2dce87d9669493b81b06baff4a9"
print(json.dumps({"version":"V220","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v246 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v246.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V246" and a["base"]=={"version":"V245","digest":"59f194517a3f39aacf941ffeec5de7c24c9e589e45906a9d352bb0b63143ca07","implementation_sha256":"33ac05919ba1de4cb871ca7885a49108e4959262958b734d68bbc03aceaee519"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc197(),m.publication171(),m.membership88()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4080787200//7084700==t["epoch196_complete_seed_states"]==576 and 4080787200%7084700==0
assert (t["accepted"],t["deadline_vectors"],t["epoch197_bound_eighty_fourth_lineage_rotation_states"],t["epoch197_bound_eighty_fourth_lineage_binding_states"],t["epoch197_bound_handed_proof_rebind_states"],t["epoch197_bound_verifier_binding_states"])==(37362124800,7207200,29059430400,20756736000,12454041600,4151347200) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 190869765120//6903565==s["bound_one_hundred_seventieth_restart_seed_states"]==27648 and 190869765120%6903565==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventy_first_restart_states"],s["bound_one_hundred_seventy_first_restart_recoveries"])==(2136187164672,7023974,1747789498368,1359391832064,970994165760,582596499456,194198833152) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5156250400//6784540==b["bound_quorum_churn_seed_states"]==760 and 5156250400%6784540==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root88_rollover_states"],b["bound_root88_binding_states"],b["bound_replication_quorum_churn_states"])==(57713803400,6903565,47220384600,26233547000,15740128200,5246709400) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v246.py","winloop_v246.json","winloop_v246_report.md","winloop_v246_validate.py"}
seen=set()
for line in (H/"winloop_v246_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v246.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="1e84da39dd605279a3b8a3aa354da47a6e1c0f9104d3c4ed61162b0c27bfc526"
print(json.dumps({"version":"V246","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

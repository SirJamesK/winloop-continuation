#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v231 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v231.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V231" and a["base"]=={"version":"V230","digest":"d5e0a635fbf37664c71ee096996ee93d2bc9b2cdeb96838883ec09f6a29d5161","implementation_sha256":"6b2f0cf5914332930fe5d58dab3e154fec9c59314fab7237997fe6d00b437a18"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc182(),m.publication156(),m.membership80()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 3116298240//5410240==t["epoch181_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(22226964480,5512640)
assert (t["epoch182_bound_seventy_seventh_source_handoff_states"],t["epoch182_bound_seventy_seventh_source_binding_states"],t["epoch182_bound_verifier_binding_states"])==(15876403200,9525841920,3175280640) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 145401661440//5259030==s["bound_one_hundred_fifty_fifth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_sixth_restart_recoveries"])==(1629979794432,5359519,148179981312)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_sixth_restart_states"])==(1333619831808,1037259869184,740899906560,444539943936) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3921451800//5159805==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(27978039600,5259030)
assert (b["bound_root80_witness_rebind_states"],b["bound_root80_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(19984314000,11990588400,3996862800) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v231.py","winloop_v231.json","winloop_v231_report.md","winloop_v231_validate.py"}; seen=set()
for line in (H/"winloop_v231_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v231.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="ae9d708d92b06b2d0c3c9e7b9c5705fd65ffd01f4b66c7519f50fa66e13ed394"
print(json.dumps({"version":"V231","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

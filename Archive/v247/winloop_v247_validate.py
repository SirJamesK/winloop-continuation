#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v247 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v247.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V247" and a["base"]=={"version":"V246","digest":"1e84da39dd605279a3b8a3aa354da47a6e1c0f9104d3c4ed61162b0c27bfc526","implementation_sha256":"8a67a9d7812a4063663251db86c46c04b6850406e3d848b2d3555d0cbe817f8e"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc198(),m.publication172(),m.membership88()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4151347200//7207200==t["epoch197_complete_seed_states"]==576 and 4151347200%7207200==0
assert (t["accepted"],t["deadline_vectors"],t["epoch198_bound_eighty_fifth_source_handoff_states"],t["epoch198_bound_eighty_fifth_source_binding_states"],t["epoch198_bound_verifier_binding_states"])==(29559011328,7331104,21113579520,12668147712,4222715904) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 194198833152//7023974==s["bound_one_hundred_seventy_first_restart_seed_states"]==27648 and 194198833152%7023974==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventy_second_restart_states"],s["bound_one_hundred_seventy_second_restart_recoveries"])==(2173230259200,7145775,1778097484800,1382964710400,987831936000,592699161600,197566387200) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5246709400//6903565==b["bound_quorum_churn_seed_states"]==760 and 5246709400%6903565==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root88_witness_rebind_states"],b["bound_root88_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(37367541680,7023974,26691101200,16014660720,5338220240) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v247.py","winloop_v247.json","winloop_v247_report.md","winloop_v247_validate.py"}
seen=set()
for line in (H/"winloop_v247_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v247.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="57bcb3dfe34793d065b9aeb05534a61bbc1e3c1fcfd26acd7f7b88f23447a3f4"
print(json.dumps({"version":"V247","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

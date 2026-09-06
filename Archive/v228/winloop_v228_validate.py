#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v228 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v228.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V228" and a["base"]=={"version":"V227","digest":"bee0d1231718e8ae5d97a97dfa5871b670634456cc738a5e2d6fb7401c92f916","implementation_sha256":"57a05fc5c32a9fcd1ee2dece1881d710f8a3b84ce2a42940f8ab3667849d862a"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc179(),m.publication153(),m.membership79()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2943742464//5110664==t["epoch178_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(27004803840,5209260)
assert (t["epoch179_bound_seventy_fifth_lineage_rotation_states"],t["epoch179_bound_seventy_fifth_lineage_binding_states"],t["epoch179_bound_handed_proof_rebind_states"],t["epoch179_bound_verifier_binding_states"])==(21003736320,15002668800,9001601280,3000533760) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 137275499520//4965115==s["bound_one_hundred_fifty_second_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_third_restart_recoveries"])==(1539446059008,5061836,139949641728)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_third_restart_states"])==(1259546775552,979647492096,699748208640,419848925184) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3700921840//4869634==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(41508361400,4965115)
assert (b["bound_witness_source_replacement_states"],b["bound_root79_rollover_states"],b["bound_root79_binding_states"],b["bound_replication_quorum_churn_states"])==(33961386600,18867437000,11320462200,3773487400) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v228.py","winloop_v228.json","winloop_v228_report.md","winloop_v228_validate.py"}; seen=set()
for line in (H/"winloop_v228_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v228.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="0eb5549425df420666343bb7fecfe5f959ab400670b085c32d787087057934b0"
print(json.dumps({"version":"V228","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

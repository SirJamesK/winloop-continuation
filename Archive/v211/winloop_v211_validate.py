#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v211 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v211.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V211" and a["base"]=={"version":"V210","digest":"def1e363c8eed1ff2fc090eb4c1756ae0752d3dfcb607654f23bd82c43010f31","implementation_sha256":"7c727f40fbb7ec83489726ae0661bff97cd84164f4d61e16e728c0f5f2e0dd81"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc162(),m.publication136(),m.membership70()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2084866560//3619560==t["epoch161_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(14910174720,3697960)
assert (t["epoch162_bound_sixty_seventh_source_handoff_states"],t["epoch162_bound_sixty_seventh_source_binding_states"],t["epoch162_bound_verifier_binding_states"])==(10650124800,6390074880,2130024960) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 96879974400//3504050==s["bound_one_hundred_thirty_fifth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_sixth_restart_recoveries"])==(1089015155712,3580779,99001377792)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_sixth_restart_states"])==(891012400128,693009644544,495006888960,297004133376) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2605603000//3428425==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(18641546000,3504050)
assert (b["bound_root70_witness_rebind_states"],b["bound_root70_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(13315390000,7989234000,2663078000) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v211.py","winloop_v211.json","winloop_v211_report.md","winloop_v211_validate.py"}; seen=set()
for line in (H/"winloop_v211_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v211.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="f206faf0b46850b0db0abb0309a5ab9d190efbb21d6d22ea7ef1bf425d499b92"
print(json.dumps({"version":"V211","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

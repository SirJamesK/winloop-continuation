#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v225 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v225.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V225" and a["base"]=={"version":"V224","digest":"65da90f1923d812e3a7d8da6404b1dc45c3fdc65c4acf5c9287ae6116b682770","implementation_sha256":"e6e84a7e9cca3c64a933c2cc68e37efd63eadb4d1cc274a37028f9287880db03"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc176(),m.publication150(),m.membership77()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2777677056//4822356==t["epoch175_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(19826231040,4917220)
assert (t["epoch176_bound_seventy_fourth_source_handoff_states"],t["epoch176_bound_seventy_fourth_source_binding_states"],t["epoch176_bound_verifier_binding_states"])==(14161593600,8496956160,2832318720) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 129457889280//4682360==s["bound_one_hundred_forty_ninth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fiftieth_restart_recoveries"])==(1452328289280,4775385,132029844480)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fiftieth_restart_states"])==(1188268600320,924208911360,660149222400,396089533440) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3488818760//4590551==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(24910155200,4682360)
assert (b["bound_root77_witness_rebind_states"],b["bound_root77_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(17792968000,10675780800,3558593600) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v225.py","winloop_v225.json","winloop_v225_report.md","winloop_v225_validate.py"}; seen=set()
for line in (H/"winloop_v225_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v225.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="35d53f4b0c77714b37b84dec8d148cbeb9fc8f27ee587dcfd1b458f1f97e56eb"
print(json.dumps({"version":"V225","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

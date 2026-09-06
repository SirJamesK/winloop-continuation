#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v226 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v226.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V226" and a["base"]=={"version":"V225","digest":"35d53f4b0c77714b37b84dec8d148cbeb9fc8f27ee587dcfd1b458f1f97e56eb","implementation_sha256":"a0713101dd488665b6a7f6d90413a6066084a2512198ef822db6cb76e69f1daf"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc177(),m.publication151(),m.membership78()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2832318720//4917220==t["epoch176_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(25989050880,5013320)
assert (t["epoch177_bound_seventy_fourth_lineage_rotation_states"],t["epoch177_bound_seventy_fourth_lineage_binding_states"],t["epoch177_bound_handed_proof_rebind_states"],t["epoch177_bound_verifier_binding_states"])==(20213706240,14438361600,8663016960,2887672320) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 132029844480//4775385==s["bound_one_hundred_fiftieth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fifty_first_restart_recoveries"])==(1480992049152,4869634,134635640832)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fifty_first_restart_states"])==(1211720767488,942449485824,673178204160,403906922496) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3558593600//4682360==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(39922218600,4775385)
assert (b["bound_witness_source_replacement_states"],b["bound_root78_rollover_states"],b["bound_root78_binding_states"],b["bound_replication_quorum_churn_states"])==(32663633400,18146463000,10887877800,3629292600) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v226.py","winloop_v226.json","winloop_v226_report.md","winloop_v226_validate.py"}; seen=set()
for line in (H/"winloop_v226_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v226.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="28ba0ac5011094061962ae84c33557e5fdcf50f57e50434b171df865d853a593"
print(json.dumps({"version":"V226","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

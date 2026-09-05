#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v208 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v208.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V208" and a["base"]=={"version":"V207","digest":"0dc7f3b24090c61bb65ed06b332d0bb9153484cfc72509e9d395f3584c46566a","implementation_sha256":"533c908a094e71a270078db6055b53f5ebf39a1264da47badc4a1a8a8a66ae9d"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc159(),m.publication133(),m.membership69()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 1953229824//3391024==t["epoch158_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(17968262400,3466100)
assert (t["epoch159_bound_sixty_fifth_lineage_rotation_states"],t["epoch159_bound_sixty_fifth_lineage_binding_states"],t["epoch159_bound_handed_proof_rebind_states"],t["epoch159_bound_verifier_binding_states"])==(13975315200,9982368000,5989420800,1996473600) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 90698019840//3280455==s["bound_one_hundred_thirty_second_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_third_restart_recoveries"])==(1020013682688,3353896,92728516608)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_third_restart_states"])==(834556649472,649099616256,463642583040,278185549824) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2438151440//3208094==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(27424603800,3280455)
assert (b["bound_witness_source_replacement_states"],b["bound_root69_rollover_states"],b["bound_root69_binding_states"],b["bound_replication_quorum_churn_states"])==(22438312200,12465729000,7479437400,2493145800) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v208.py","winloop_v208.json","winloop_v208_report.md","winloop_v208_validate.py"}; seen=set()
for line in (H/"winloop_v208_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v208.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="8b03425d3a0b11a36fc92d977ab32ed05c18f62d473f9bfab5a037fec9fb355f"
print(json.dumps({"version":"V208","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

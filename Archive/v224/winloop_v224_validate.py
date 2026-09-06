#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v224 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v224.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V224" and a["base"]=={"version":"V223","digest":"62d96c27f3c96895071e075642c995453acc0829eaf6d17eb07d97cea65fa9e9","implementation_sha256":"22c5292be717e06cee099860f6c616cd603944006087335b954dd898ba80d106"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc175(),m.publication149(),m.membership77()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2723742720//4728720==t["epoch174_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(24999093504,4822356)
assert (t["epoch175_bound_seventy_third_lineage_rotation_states"],t["epoch175_bound_seventy_third_lineage_binding_states"],t["epoch175_bound_handed_proof_rebind_states"],t["epoch175_bound_verifier_binding_states"])==(19443739392,13888385280,8333031168,2777677056) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 126919554048//4590551==s["bound_one_hundred_forty_eighth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_forty_ninth_restart_recoveries"])==(1424036782080,4682360,129457889280)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_forty_ninth_restart_states"])==(1165121003520,906205224960,647289446400,388373667840) and s["bad_acceptances"]==0 and all(s["checks"])
assert 3419962000//4499950==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(38377006360,4590551)
assert (b["bound_witness_source_replacement_states"],b["bound_root77_rollover_states"],b["bound_root77_binding_states"],b["bound_replication_quorum_churn_states"])==(31399368840,17444093800,10466456280,3488818760) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v224.py","winloop_v224.json","winloop_v224_report.md","winloop_v224_validate.py"}; seen=set()
for line in (H/"winloop_v224_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v224.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="65da90f1923d812e3a7d8da6404b1dc45c3fdc65c4acf5c9287ae6116b682770"
print(json.dumps({"version":"V224","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

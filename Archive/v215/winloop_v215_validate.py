#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v215 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v215.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V215" and a["base"]=={"version":"V214","digest":"5cead8ef75bda4e6c211afde57c7524cb0061fa33c8384371e6c02d11c0e750a","implementation_sha256":"3c5d8052b3cbad363ea8b041c2e274b39fbbcdc7e2a8112f80930dfbbb21c972"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc166(),m.publication140(),m.membership72()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2269403136//3939936==t["epoch165_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(16220252160,4022880)
assert (t["epoch166_bound_sixty_ninth_source_handoff_states"],t["epoch166_bound_sixty_ninth_source_binding_states"],t["epoch166_bound_verifier_binding_states"])==(11585894400,6951536640,2317178880) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 105550940160//3817670==s["bound_one_hundred_thirty_ninth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_fortieth_restart_recoveries"])==(1185763138560,3898895,107796648960)
assert (s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_fortieth_restart_states"])==(970169840640,754576542720,538983244800,323389946880) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2840561560//3737581==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(20310004400,3817670)
assert (b["bound_root72_witness_rebind_states"],b["bound_root72_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(14507146000,8704287600,2901429200) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v215.py","winloop_v215.json","winloop_v215_report.md","winloop_v215_validate.py"}; seen=set()
for line in (H/"winloop_v215_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v215.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="b790801c1fff32a8555ea54edd9c7a1bc69a34f4d63b1ddbce5682dc72e260cb"
print(json.dumps({"version":"V215","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

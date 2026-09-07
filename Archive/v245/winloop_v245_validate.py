#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v245 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v245.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V245" and a["base"]=={"version":"V244","digest":"7e8bfd6265623f45bfba28c4c1824d08f0209d1504134dd4d09990f6be48069e","implementation_sha256":"6c935d5a8cf72ec634e2837d70b2cde80700dee3ffe5d730025b618016b1c41f"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc196(),m.publication170(),m.membership87()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4011031296//6963596==t["epoch195_complete_seed_states"]==576 and 4011031296%6963596==0
assert (t["accepted"],t["deadline_vectors"],t["epoch196_bound_eighty_fourth_source_handoff_states"],t["epoch196_bound_eighty_fourth_source_binding_states"],t["epoch196_bound_verifier_binding_states"])==(28565510400,7084700,20403936000,12242361600,4080787200) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 187578961920//6784540==s["bound_one_hundred_sixty_ninth_restart_seed_states"]==27648 and 187578961920%6784540==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventieth_restart_states"],s["bound_one_hundred_seventieth_restart_recoveries"])==(2099567416320,6903565,1717827886080,1336088355840,954348825600,572609295360,190869765120) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5066837160//6666891==b["bound_quorum_churn_seed_states"]==760 and 5066837160%6666891==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root87_witness_rebind_states"],b["bound_root87_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(36093752800,6784540,25781252000,15468751200,5156250400) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v245.py","winloop_v245.json","winloop_v245_report.md","winloop_v245_validate.py"}
seen=set()
for line in (H/"winloop_v245_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v245.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="59f194517a3f39aacf941ffeec5de7c24c9e589e45906a9d352bb0b63143ca07"
print(json.dumps({"version":"V245","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

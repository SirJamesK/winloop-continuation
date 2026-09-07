#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v249 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v249.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V249" and a["base"]=={"version":"V248","digest":"e870c97516fa22f8756317b401dc465dd0be10f9e8264ccb33db678175c58c9e","implementation_sha256":"2f5066f8d93733ebb7f5dbf630dd20bf0a162e4622af5537b565159c1966895a"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc200(),m.publication174(),m.membership89()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 4294897920//7456420==t["epoch199_complete_seed_states"]==576 and 4294897920%7456420==0
assert (t["accepted"],t["deadline_vectors"],t["epoch200_bound_eighty_sixth_source_handoff_states"],t["epoch200_bound_eighty_sixth_source_binding_states"],t["epoch200_bound_verifier_binding_states"])==(30575284992,7583156,21839489280,13103693568,4367897856) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 200972648448//7268976==s["bound_one_hundred_seventy_third_restart_seed_states"]==27648 and 200972648448%7268976==0
assert (s["accepted"],s["deadline_vectors"],s["bound_successor_source_disappearance_states"],s["bound_replacement_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_seventy_fourth_restart_states"],s["bound_one_hundred_seventy_fourth_restart_recoveries"])==(2248596218880,7393585,1839760542720,1430924866560,1022089190400,613253514240,204417838080) and s["bad_acceptances"]==0 and all(s["checks"])
assert 5430789000//7145775==b["bound_quorum_churn_seed_states"]==760 and 5430789000%7145775==0
assert (b["accepted"],b["deadline_vectors"],b["bound_root89_witness_rebind_states"],b["bound_root89_witness_binding_states"],b["bound_replication_quorum_churn_states"])==(38670952320,7268976,27622108800,16573265280,5524421760) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v249.py","winloop_v249.json","winloop_v249_report.md","winloop_v249_validate.py"}
seen=set()
for line in (H/"winloop_v249_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v249.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="8cf21664fe3ffffbd48f0a71a6d92f7c5b87a48a3fddaef99107399fd52632bc"
print(json.dumps({"version":"V249","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

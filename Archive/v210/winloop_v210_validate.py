#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v210 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v210.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V210" and a["base"]=={"version":"V209","digest":"12fe74145786781b6b04b6b59ad22aad66ef4b0a83d75656d856c30b1b8feaad","implementation_sha256":"09b7d2f01b40797b6d59b33d5d35d257b10d636cea7e880581fb546a93036469"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc161(),m.publication135(),m.membership70()
assert (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"] and all(c["checks"])
assert 2040350976//3542276==t["epoch160_complete_seed_states"]==576 and (t["accepted"],t["deadline_vectors"])==(18763799040,3619560)
assert (t["epoch161_bound_sixty_sixth_lineage_rotation_states"],t["epoch161_bound_sixty_sixth_lineage_binding_states"],t["epoch161_bound_handed_proof_rebind_states"],t["epoch161_bound_verifier_binding_states"])==(14594065920,10424332800,6254599680,2084866560) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 94789094400//3428425==s["bound_one_hundred_thirty_fourth_restart_seed_states"]==27648 and (s["accepted"],s["deadline_vectors"],s["bound_one_hundred_thirty_fifth_restart_recoveries"])==(1065679718400,3504050,96879974400)
assert (s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_thirty_fifth_restart_states"])==(871919769600,678159820800,484399872000,290639923200) and s["bad_acceptances"]==0 and all(s["checks"])
assert 2548960960//3353896==b["bound_quorum_churn_seed_states"]==760 and (b["accepted"],b["deadline_vectors"])==(28661633000,3428425)
assert (b["bound_witness_source_replacement_states"],b["bound_root70_rollover_states"],b["bound_root70_binding_states"],b["bound_replication_quorum_churn_states"])==(23450427000,13028015000,7816809000,2605603000) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v210.py","winloop_v210.json","winloop_v210_report.md","winloop_v210_validate.py"}; seen=set()
for line in (H/"winloop_v210_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v210.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="def1e363c8eed1ff2fc090eb4c1756ae0752d3dfcb607654f23bd82c43010f31"
print(json.dumps({"version":"V210","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

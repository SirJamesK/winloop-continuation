#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v244 as m
H=Path(__file__).resolve().parent
a=json.loads((H/"winloop_v244.json").read_text())
assert a==m.run_validation()
assert a["version"]=="V244" and a["base"]=={"version":"V243","digest":"f70030ddf88d76acf59cd8f740777be829ded52728ba6d200cf808eab2f4cda7","implementation_sha256":"b5b8c6a9ee28fbb3e430f7c00aea9919d110a0e121f4596c34e1b1a7983822f2"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
c,t,s,b=m.indep(),m.gc195(),m.publication169(),m.membership87()
assert all(c["checks"]) and (c["patterns"],c["hypothetical_gate_admits"],c["conservative_cross_role_credit"],c["bad_acceptances"])==(150,4,12,0) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert 3942074880//6843880==t["epoch194_complete_seed_states"]==576 and 3942074880%6843880==0
assert (t["accepted"],t["deadline_vectors"],t["epoch195_bound_eighty_third_lineage_rotation_states"],t["epoch195_bound_eighty_third_lineage_binding_states"],t["epoch195_bound_handed_proof_rebind_states"],t["epoch195_bound_verifier_binding_states"])==(36099281664,6963596,28077219072,20055156480,12033093888,4011031296) and t["deadline_origin"]=="epoch12" and t["bad_acceptances"]==0 and all(t["checks"])
assert 184326202368//6666891==s["bound_one_hundred_sixty_eighth_restart_seed_states"]==27648 and 184326202368%6666891==0
assert (s["accepted"],s["deadline_vectors"],s["bound_replacement_source_churn_states"],s["bound_successor_source_binding_states"],s["bound_fresh_reconciliation_states"],s["bound_one_hundred_sixty_ninth_restart_states"],s["bound_one_hundred_sixty_ninth_restart_recoveries"])==(2063368581120,6784540,1688210657280,1313052733440,937894809600,562736885760,187578961920) and s["bad_acceptances"]==0 and all(s["checks"])
assert 4978463600//6550610==b["bound_quorum_churn_seed_states"]==760 and 4978463600%6550610==0
assert (b["accepted"],b["deadline_vectors"],b["bound_witness_source_replacement_states"],b["bound_root87_rollover_states"],b["bound_root87_binding_states"],b["bound_replication_quorum_churn_states"])==(55735208760,6666891,45601534440,25334185800,15200511480,5066837160) and b["bad_acceptances"]==0 and all(b["checks"])
assert a["temporal_floor_regression"]=={"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"} and a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
required={"distributed_winloop_v244.py","winloop_v244.json","winloop_v244_report.md","winloop_v244_validate.py"}
seen=set()
for line in (H/"winloop_v244_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    expected,name=line.split(maxsplit=1); name=name.strip()
    raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v244.json" else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    seen.add(name)
assert seen==required and a["digest"]=="7e8bfd6265623f45bfba28c4c1824d08f0209d1504134dd4d09990f6be48069e"
print(json.dumps({"version":"V244","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

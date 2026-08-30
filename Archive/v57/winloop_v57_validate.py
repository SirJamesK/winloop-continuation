#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/"v56"/"winloop_v56.json").read_text())
assert base["version"]=="V56" and base["digest"]=="c3527721770a05486cf17700f2642ae97cd491900fef9d523a50ce3a67a26273"
assert "3908b88731cd3dacc6b9be5bd9438af5910e81f4e3811908bfe2bf2c839e0635  distributed_winloop_v56.py" in (H.parent/"v56"/"winloop_v56_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v57",H/"distributed_winloop_v57.py")
m=importlib.util.module_from_spec(s); sys.modules["v57"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v57.json").read_text())
assert a==m.run_validation() and a["version"]=="V57"
assert a["base"]=={"version":"V56","digest":"c3527721770a05486cf17700f2642ae97cd491900fef9d523a50ce3a67a26273","implementation_sha256":"3908b88731cd3dacc6b9be5bd9438af5910e81f4e3811908bfe2bf2c839e0635"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]

h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v56_regression_preserved"]

t=a["monotonic_deadline_certificates"]
assert t["patterns"]==180 and t["deadline_steps"]==3
assert t["clock_skew_domain"]==[-2,2] and t["rollback_domain"]==[0,2]
assert t["accepted_current_before_or_at_deadline"]==20
assert t["accepted_by_skew"]=={"-2":4,"-1":4,"0":4,"1":4,"2":4}
assert t["expired_current_rejected"]==10 and t["rollback_cases_rejected"]==60 and t["old_epoch_cases_rejected"]==90
assert t["stale_acceptances_after_deadline"]==0 and t["tampered_expiry_rejected"]
assert t["wall_clock_is_advisory_not_freshness_authority"] and t["monotonic_counter_and_epoch_are_security_binding"]

x=a["source_loss_and_same_epoch_equivocation"]
assert x["patterns"]==144 and x["accepted"]==25
assert x["whole_log_loss_patterns"]==63 and x["equivocation_observed_and_rejected"]==80
assert x["asymmetric_single_source_loss_acceptances"]==24
assert x["rotation_epochs"]=={"A":7,"B":8,"witness":8}
assert all(x["checks"].values())
assert x["target_root_bound_by_epoch_certificate_and_gossip"] and x["unknown_or_conflicting_source_state_fails_closed"]

e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]

c=a["checkpoint_recovery"]
assert c=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}

for line in (H/"winloop_v57_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V57","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

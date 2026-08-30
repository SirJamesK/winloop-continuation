#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))

base=json.loads((H.parent/"v63"/"winloop_v63.json").read_text())
assert base["version"]=="V63" and base["digest"]=="6bebeb48bcda3d1dd9f093727e416f92b692e898d54236f9dde95dbe2f3269a9"
assert "48feb8ecaa02a39725333c300ef848eff045fb25cf567f057665652359e49813  distributed_winloop_v63.py" in (H.parent/"v63"/"winloop_v63_SHA256SUMS.txt").read_text()

s=importlib.util.spec_from_file_location("v64",H/"distributed_winloop_v64.py")
m=importlib.util.module_from_spec(s); sys.modules["v64"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v64.json").read_text())
assert a==m.run_validation() and a["version"]=="V64"
assert a["base"]=={
    "version":"V63",
    "digest":"6bebeb48bcda3d1dd9f093727e416f92b692e898d54236f9dde95dbe2f3269a9",
    "implementation_sha256":"48feb8ecaa02a39725333c300ef848eff045fb25cf567f057665652359e49813"
}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False}
assert not a["runtime"]["new_routing_envelope"]

h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v63_regression_preserved"]

i=a["identity_binding_gate"]
assert i["patterns"]==5832000 and i["hypothetical_gate_admits"]==145
assert i["old_source_loss_recoveries"]==8 and i["new_source_loss_recoveries"]==8
assert i["both_sides_source_loss_recoveries"]==1
assert i["stale_or_conflicting_acceptances"]==0
assert i["alias_or_unknown_relation_acceptances"]==0
assert i["self_asserted_acceptances"]==0 and i["binding_source_fork_acceptances"]==0
assert not i["committed_external_independence_evidence_present"]
assert i["conservative_cross_role_credit"]==12 and not i["credit_raised"]
assert i["modeled_disjointness_alone_insufficient"] and all(i["checks"].values())

t=a["tombstone_epoch15"]
assert t["patterns"]==14155776 and t["accepted"]==29100
assert t["base_history_states"]==221184 and t["accepted_base_history_states"]==1455
assert t["delay_vectors"]==64 and t["admissible_shared_deadline_vectors"]==20
assert t["shared_deadline"]==3 and t["deadline_origin_preserved"]=="epoch12"
assert t["compact_behind_t14_recoveries"]==1000
assert t["pre15_source_disappearance_recoveries"]==100
assert t["pre15_source_disappearance_concurrent_revocation_recoveries"]==20
assert t["concurrent_revocation_recoveries"]==5820 and t["delayed_recoveries"]==27645
assert t["post_deadline_acceptances"]==0 and t["deadline_reset_acceptances"]==0
assert t["stale_or_fork_clear_acceptances"]==0 and t["invalid_history_acceptances"]==0
assert t["forked_source_or_compaction_acceptances"]==0 and all(t["checks"].values())

q=a["byzantine_quarantine_join"]
assert q["patterns"]==9953280 and q["accepted"]==237320
assert q["base_membership_states"]==622080 and q["accepted_base_membership_states"]==23732
assert q["delay_vectors"]==16 and q["admissible_shared_deadline_vectors"]==10
assert q["population_slots"]==5 and q["quorum"]==3 and q["shared_deadline"]==3
assert q["one_byzantine_two_quarantine_join_recoveries"]==9000
assert q["delayed_recoveries"]==213588
assert q["untrusted_join_present_but_ignored_recoveries"]==116400
assert q["active_byzantine_acceptances"]==0
assert q["stale_or_missing_eviction_proof_acceptances"]==0
assert q["membership_fork_acceptances"]==0 and q["below_threshold_history_acceptances"]==0
assert q["untrusted_join_quorum_credit_acceptances"]==0 and q["post_deadline_acceptances"]==0
assert all(q["checks"].values())

e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["provider_operator_hardware_binding_required"]
assert e["modeled_disjoint_roles_are_not_external_independence_proof"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]

k=a["checkpoint_recovery"]
assert k=={
    "statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
    "frontier_storage_only":True,"trust_bearing_messages_unchanged":True
}

for line in (H/"winloop_v64_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d

print(json.dumps({
    "version":"V64","validated":True,"digest":a["digest"],"headline":a["headline"]
},indent=2,sort_keys=True))

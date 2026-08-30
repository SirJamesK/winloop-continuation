#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))

base=json.loads((H.parent/"v64"/"winloop_v64.json").read_text())
assert base["version"]=="V64"
assert base["digest"]=="e3e090ea32f151975631636e7fc62e3c5784fa29d62cfeb4a9c73a0b983bd810"
assert "08e3e20a809d7df1600f9117238a8da1747333daaffed9d4c3f7838b5c256540  distributed_winloop_v64.py" in (H.parent/"v64"/"winloop_v64_SHA256SUMS.txt").read_text()

s=importlib.util.spec_from_file_location("v65",H/"distributed_winloop_v65.py")
m=importlib.util.module_from_spec(s); sys.modules["v65"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v65.json").read_text())
assert a==m.run_validation() and a["version"]=="V65"
assert a["base"]=={
    "version":"V64",
    "digest":"e3e090ea32f151975631636e7fc62e3c5784fa29d62cfeb4a9c73a0b983bd810",
    "implementation_sha256":"08e3e20a809d7df1600f9117238a8da1747333daaffed9d4c3f7838b5c256540"
}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False}
assert not a["runtime"]["new_routing_envelope"]

h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v64_regression_preserved"]

c=a["independence_certificate_gate"]
assert c["patterns"]==150 and c["hypothetical_gate_admits"]==4
assert c["stale_or_conflicting_acceptances"]==0
assert c["alias_or_unknown_relation_acceptances"]==0
assert c["self_asserted_acceptances"]==0
assert not c["committed_external_independence_certificate_present"]
assert c["conservative_cross_role_credit"]==12 and not c["credit_raised"]
assert all(c["checks"].values())

t=a["tombstone_epoch16"]
assert t["patterns"]==47185920 and t["accepted"]==22050
assert t["base_history_states"]==184320 and t["accepted_base_history_states"]==630
assert t["delay_vectors"]==256 and t["admissible_shared_deadline_vectors"]==35
assert t["shared_deadline"]==3 and t["deadline_origin_preserved"]=="epoch12"
assert t["compact_behind_t15_recoveries"]==4200
assert t["pre16_source_disappearance_recoveries"]==525
assert t["proof_source_churn_recoveries"]==525
assert t["overlapping_revocation_recoveries"]==4410
assert t["canonical_clear16_recoveries"]==4410
assert t["delayed_recoveries"]==21420
assert t["post_deadline_acceptances"]==0 and t["deadline_reset_acceptances"]==0
assert t["stale_or_fork_clear_acceptances"]==0 and t["invalid_history_acceptances"]==0
assert t["forked_source_compaction_or_publication_acceptances"]==0
assert all(t["checks"].values())

s=a["split_view_eviction_join"]
assert s["patterns"]==884736 and s["accepted"]==5120
assert s["base_publication_states"]==55296 and s["accepted_base_publication_states"]==512
assert s["verifier_populations"]==3 and s["publication_quorum"]==2
assert s["delay_vectors"]==16 and s["admissible_shared_deadline_vectors"]==10
assert s["shared_deadline"]==3
assert s["cached_pre_split_view_bridge_recoveries"]==1920
assert s["one_missing_view_recoveries"]==1920
assert s["delayed_recoveries"]==4608
assert s["fork_acceptances"]==0
assert s["stale_or_missing_eviction_proof_acceptances"]==0
assert s["untrusted_or_conflicting_join_acceptances"]==0
assert s["pre_eviction_or_pre_join_acceptances"]==0
assert s["post_deadline_acceptances"]==0
assert all(s["checks"].values())

j=a["two_consecutive_join"]
assert j["patterns"]==26891200 and j["accepted"]==196140
assert j["base_membership_states"]==1680700 and j["accepted_base_membership_states"]==19614
assert j["population_slots"]==5 and j["quorum"]==3
assert j["delay_vectors"]==16 and j["admissible_shared_deadline_vectors"]==10
assert j["shared_deadline"]==3
assert j["two_consecutive_join_recoveries"]==25500
assert j["two_join_one_quarantine_recoveries"]==7600
assert j["delayed_recoveries"]==176526
assert j["transient_membership_quorum_inflation_acceptances"]==0
assert j["untrusted_join_quorum_credit_acceptances"]==0
assert j["active_byzantine_acceptances"]==0
assert j["stale_or_missing_chain_acceptances"]==0
assert j["membership_fork_acceptances"]==0
assert j["below_threshold_history_acceptances"]==0
assert j["post_deadline_acceptances"]==0
assert all(j["checks"].values())

e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_certificate_present"]
assert e["provider_operator_hardware_binding_required"]
assert e["modeled_disjoint_roles_are_not_external_independence_proof"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]

k=a["checkpoint_recovery"]
assert k=={
    "statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
    "frontier_storage_only":True,"trust_bearing_messages_unchanged":True
}

for line in (H/"winloop_v65_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d

print(json.dumps({
    "version":"V65","validated":True,"digest":a["digest"],"headline":a["headline"]
},indent=2,sort_keys=True))

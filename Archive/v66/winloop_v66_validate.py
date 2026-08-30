#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/"v65"/"winloop_v65.json").read_text())
assert base["version"]=="V65" and base["digest"]=="90c0b1862ec4d81b1e60e20334fa4f02bf6bbb410ae0db520017ffeb4db805d6"
assert "c743e1c5fc027b4695623bbe6ed95dd3cfd847a6ff72a0f1250647735785cf01  distributed_winloop_v65.py" in (H.parent/"v65"/"winloop_v65_SHA256SUMS.txt").read_text()
sp=importlib.util.spec_from_file_location("v66",H/"distributed_winloop_v66.py"); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
a=json.loads((H/"winloop_v66.json").read_text()); assert a==m.run_validation() and a["version"]=="V66"
assert a["base"]=={"version":"V65","digest":"90c0b1862ec4d81b1e60e20334fa4f02bf6bbb410ae0db520017ffeb4db805d6","implementation_sha256":"c743e1c5fc027b4695623bbe6ed95dd3cfd847a6ff72a0f1250647735785cf01"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}; assert a["routing"]=={"active":"V21 guarded","replacement":False}; assert not a["runtime"]["new_routing_envelope"]
h=a["temporal_floor_regression"]; assert (h["roots"],h["horizon"],h["floor"],h["budget"],h["h11_floor"],h["h11_budget"],h["carried_from"])==(22,22,1,851,2,398,"V65")
c=a["independence_certificate_gate"]; assert c["patterns"]==150 and c["hypothetical_gate_admits"]==4 and c["conservative_cross_role_credit"]==12 and not c["credit_raised"] and not c["committed_external_independence_certificate_present"] and all(c["checks"].values())
assert c["stale_or_conflicting_acceptances"]==c["alias_or_unknown_relation_acceptances"]==c["self_asserted_acceptances"]==0
t=a["tombstone_epoch17"]; assert t["patterns"]==1605632000 and t["accepted"]==91392 and t["accepted_base_history_states"]==1632 and t["delay_vectors"]==1024 and t["admissible_shared_deadline_vectors"]==56 and t["shared_deadline"]==3 and t["deadline_origin_preserved"]=="epoch12"; assert t["source_replacement_recoveries"]==6048 and t["lagged_verifier_recoveries"]==4704 and t["clear17_after_source_replacement_recoveries"]==672; assert t["post_deadline_acceptances"]==t["deadline_reset_acceptances"]==t["stale_or_fork_clear_acceptances"]==t["fork_acceptances"]==0 and all(t["checks"].values())
s=a["split_view_source_loss_rollback"]; assert s["patterns"]==35123200 and s["accepted"]==31360 and s["accepted_base_publication_states"]==1568 and s["verifier_populations"]==3 and s["publication_quorum"]==2 and s["max_tolerated_rollback_views"]==1 and s["delay_vectors"]==64 and s["admissible_shared_deadline_vectors"]==20 and s["shared_deadline"]==3; assert s["proof_source_disappearance_recoveries"]==8960 and s["one_rollback_view_recoveries"]==13440; assert s["fork_acceptances"]==s["stale_or_missing_eviction_proof_acceptances"]==s["untrusted_or_conflicting_join_acceptances"]==s["post_deadline_acceptances"]==0 and all(s["checks"].values())
b=a["second_byzantine_eviction"]; assert b["patterns"]==1889568000 and b["accepted"]==361680 and b["accepted_base_membership_states"]==18084 and b["population_slots"]==5 and b["quorum"]==3 and b["delay_vectors"]==64 and b["admissible_shared_deadline_vectors"]==20 and b["shared_deadline"]==3; assert b["second_eviction_recoveries"]==71600 and b["post_second_eviction_join2_recoveries"]==30400; assert b["replacement_self_authorization_acceptances"]==b["active_second_byzantine_acceptances"]==b["untrusted_join_acceptances"]==b["membership_or_eviction_fork_acceptances"]==b["missing_or_stale_second_eviction_proof_acceptances"]==b["stale_or_missing_chain_acceptances"]==b["below_threshold_history_acceptances"]==b["post_deadline_acceptances"]==0 and all(b["checks"].values())
assert a["checkpoint_recovery"]=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
for line in (H/"winloop_v66_SHA256SUMS.txt").read_text().splitlines():
 if line.strip(): d,n=line.split(maxsplit=1); assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V66","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

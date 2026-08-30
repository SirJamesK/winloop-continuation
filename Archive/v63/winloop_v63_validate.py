#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))
base=json.loads((H.parent/"v62"/"winloop_v62.json").read_text())
assert base["version"]=="V62" and base["digest"]=="66c617a9972e89c527e35beee814d16822326c6548c277462d00314748fb70c5"
assert "864db53ceae4a988db3eb2df78ebf067192cd5f11483767d01b6264ffb25b698  distributed_winloop_v62.py" in (H.parent/"v62"/"winloop_v62_SHA256SUMS.txt").read_text()

s=importlib.util.spec_from_file_location("v63",H/"distributed_winloop_v63.py")
m=importlib.util.module_from_spec(s); sys.modules["v63"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v63.json").read_text())
assert a==m.run_validation() and a["version"]=="V63"
assert a["base"]=={"version":"V62","digest":"66c617a9972e89c527e35beee814d16822326c6548c277462d00314748fb70c5","implementation_sha256":"864db53ceae4a988db3eb2df78ebf067192cd5f11483767d01b6264ffb25b698"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]

h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v62_regression_preserved"]

w=a["disjoint_horizon_witness_rotation"]
assert w["patterns"]==2343750 and w["accepted"]==2192
assert w["sets_disjoint"] and w["quorum_each"]==2
assert w["old_provider_loss_recoveries"]==280
assert w["new_provider_loss_recoveries"]==280
assert w["old_provider_plus_root_source_loss_recoveries"]==140
assert w["new_provider_plus_root_source_loss_recoveries"]==140
assert w["stale_acceptances"]==0 and w["fork_acceptances"]==0 and w["new_only_or_unpinned_acceptances"]==0
assert all(w["checks"].values())

t=a["tombstone_anchor_history"]
assert t["patterns"]==1638400 and t["accepted"]==4480
assert t["anchor_generations"]==3 and t["shared_deadline"]==3 and t["deadline_origin_preserved"]=="epoch12"
assert t["cp12_tombstone_recoveries"]==1280
assert t["cp13_tombstone_recoveries"]==640
assert t["live_revocation_recoveries"]==2240
assert t["post_deadline_acceptances"]==0 and t["deadline_reset_acceptances"]==0
assert t["live_revocation_erasure_acceptances"]==0 and t["stale_or_fork_clear_acceptances"]==0
assert t["missing_tombstone_acceptances"]==0 and all(t["checks"].values())

q=a["two_quarantine_verifier_reconfiguration"]
assert q["patterns"]==2488320 and q["accepted"]==81440
assert q["population_slots"]==5 and q["quorum"]==3 and q["shared_deadline"]==3
assert q["two_or_more_quarantine_recoveries"]==13100
assert q["explicit_two_quarantine_reconfig_recoveries"]==3800
assert q["untrusted_join_present_but_not_counted_recoveries"]==43150
assert q["untrusted_join_quorum_credit_acceptances"]==0
assert q["invalid_state_acceptances"]==0 and q["membership_fork_acceptances"]==0
assert q["below_threshold_history_acceptances"]==0 and q["post_deadline_acceptances"]==0
assert all(q["checks"].values())

e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["disjoint_modeled_roles_are_not_external_independence_proof"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]

k=a["checkpoint_recovery"]
assert k=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}

for line in (H/"winloop_v63_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d

print(json.dumps({"version":"V63","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

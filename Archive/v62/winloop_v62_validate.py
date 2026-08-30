#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))
base=json.loads((H.parent/"v61"/"winloop_v61.json").read_text())
assert base["version"]=="V61" and base["digest"]=="360d9f05a3bc7dfaf8805229ba5b57b657f046715abf56195b8b58af43ebd9ec"
assert "278cde2efdf0ef256cb9ecffc0efae545318b0b0d1f0c6e1cdd4694ae6520c52  distributed_winloop_v61.py" in (H.parent/"v61"/"winloop_v61_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v62",H/"distributed_winloop_v62.py")
m=importlib.util.module_from_spec(s); sys.modules["v62"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v62.json").read_text())
assert a==m.run_validation() and a["version"]=="V62"
assert a["base"]=={"version":"V61","digest":"360d9f05a3bc7dfaf8805229ba5b57b657f046715abf56195b8b58af43ebd9ec","implementation_sha256":"278cde2efdf0ef256cb9ecffc0efae545318b0b0d1f0c6e1cdd4694ae6520c52"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v61_regression_preserved"]
r=a["long_horizon_anchor_rotation"]
assert r["patterns"]==468750 and r["accepted"]==45
assert r["all_pre_rotation_online_source_loss_recoveries"]==18 and r["publisher_loss_cached_recoveries"]==9
assert r["stale_acceptances"]==0 and r["fork_acceptances"]==0
assert r["self_or_new_only_acceptances"]==0
assert r["new_anchor_cannot_self_authorize"]
assert all(r["checks"].values())
c=a["multi_layer_compaction"]
assert c["patterns"]==2343750 and c["accepted"]==1600
assert c["post_deadline_acceptances"]==0 and c["deadline_reset_acceptances"]==0
assert c["cp10_cp11_compacted_recoveries"]==160 and c["cp11_cp12_compacted_recoveries"]==160
assert c["threshold_fragment_recoveries"]==640 and c["offline_or_delayed_recoveries"]==1520
assert c["stale_or_fork_acceptances"]==0
assert c["multiple_compaction_layers"]==2 and c["shared_deadline"]==3
assert all(c["checks"].values())
q=a["asynchronous_verifier_churn"]
assert q["patterns"]==3072000 and q["accepted"]==12710 and q["quorum"]==3
assert q["post_deadline_acceptances"]==0 and q["rollback_acceptances"]==0 and q["active_fork_acceptances"]==0
assert q["membership_fork_or_below_threshold_acceptances"]==0
assert q["quarantined_byzantine_recoveries"]==4400 and q["join_churn_recoveries"]==9620
assert q["leave_join_recoveries"]==3040 and q["threshold_fragment_recoveries"]==6500
assert q["delayed_compaction_publication_recoveries"]==7626 and q["untrusted_join_present_but_not_counted_recoveries"]==2200
assert q["shared_deadline"]==3
assert all(q["checks"].values())
e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]
assert e["independent_witness_role_is_modeled_not_external_independence_proof"]
k=a["checkpoint_recovery"]
assert k=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
for line in (H/"winloop_v62_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V62","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

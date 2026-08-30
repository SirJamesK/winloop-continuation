#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))
base=json.loads((H.parent/"v60"/"winloop_v60.json").read_text())
assert base["version"]=="V60" and base["digest"]=="468245d5566e27b49ad5ef612e04859f2fe3ab0965bbfd1c8fe9fc3ac0f00729"
assert "136266a1b4047d167b14b308b17c99cc2042b5a8e8bbde223269162d5cfa3213  distributed_winloop_v60.py" in (H.parent/"v60"/"winloop_v60_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v61",H/"distributed_winloop_v61.py")
m=importlib.util.module_from_spec(s); sys.modules["v61"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v61.json").read_text())
assert a==m.run_validation() and a["version"]=="V61"
assert a["base"]=={"version":"V60","digest":"468245d5566e27b49ad5ef612e04859f2fe3ab0965bbfd1c8fe9fc3ac0f00729","implementation_sha256":"136266a1b4047d167b14b308b17c99cc2042b5a8e8bbde223269162d5cfa3213"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v60_regression_preserved"]
r=a["root_authority_rotation"]
assert r["patterns"]==78125 and r["accepted"]==18 and r["cached_transition_recoveries"]==9
assert r["stale_rotation_acceptances"]==0 and r["fork_rotation_acceptances"]==0 and r["shared_overlap_only_acceptances"]==0
assert r["old_and_new_quorums_required"] and r["leaving_and_joining_boundary_required"] and r["new_set_cannot_self_bootstrap"]
assert all(r["checks"].values())
c=a["three_rotation_catchup"]
assert c["patterns"]==2625000 and c["accepted"]==1056
assert c["post_deadline_acceptances"]==0 and c["replayed_terminal_acceptances"]==0 and c["fork_terminal_acceptances"]==0
assert c["compacted_checkpoint_recoveries"]==32 and c["mixed_generation_recoveries"]==1020 and c["offline_catchup_recoveries"]==792
assert c["single_root_source_loss_recoveries"]==256 and c["single_witness_source_loss_recoveries"]==256
assert c["combined_root_plus_witness_source_loss_recoveries"]==256
assert c["three_issuer_epochs_hash_bound"] and c["root_rotation_hash_bound_into_roster_and_issuer"] and c["shared_deadline_not_per_stage"]
assert all(c["checks"].values())
q=a["verifier_checkpoint_anti_rollback"]
assert q["patterns"]==5250 and q["accepted"]==336
assert q["post_deadline_acceptances"]==0 and q["rollback_acceptances"]==0 and q["fork_acceptances"]==0
assert q["compacted_only_recoveries"]==16 and q["single_source_loss_recoveries"]==240 and q["offline_recoveries"]==252
assert q["conflicting_presented_checkpoint_fails_closed"] and q["quorum"]==2 and all(q["checks"].values())
e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]
k=a["checkpoint_recovery"]
assert k=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
for line in (H/"winloop_v61_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V61","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

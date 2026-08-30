#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/"v55"/"winloop_v55.json").read_text())
assert base["version"]=="V55" and base["digest"]=="62e0a6e18fc77c4d0d8edb6f4c825dcf719b7b215846de3b88cd6ee1406edda8"
assert "e3ec645fce7bf2a037f02fd5371dd3ba63cb3135d5c7af93e6a3c26e0a0d2f72  distributed_winloop_v55.py" in (H.parent/"v55"/"winloop_v55_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v56",H/"distributed_winloop_v56.py")
m=importlib.util.module_from_spec(s); sys.modules["v56"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v56.json").read_text())
assert a==m.run_validation() and a["version"]=="V56"
assert a["base"]=={"version":"V55","digest":"62e0a6e18fc77c4d0d8edb6f4c825dcf719b7b215846de3b88cd6ee1406edda8","implementation_sha256":"e3ec645fce7bf2a037f02fd5371dd3ba63cb3135d5c7af93e6a3c26e0a0d2f72"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]

h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v55_floor1_regression_preserved"]

p=a["revocation_partition_deadline"]
assert (p["deadline_steps"],p["patterns"])==(3,15625)
assert p["partition_delay_domain"]==[0,4]
assert p["full_local_consumption_by_deadline"]==4096
assert p["cross_population_gossip_quorum_by_deadline"]==11008
assert p["gossip_quorum_but_not_full_local_consumption"]==6912
assert p["at_least_one_population_fail_closed_after_deadline"]==11529
assert p["no_gossip_quorum_by_deadline"]==4617
assert p["late_population_histogram"]=={"0":4096,"1":6912,"2":3888,"3":729}
assert p["stale_authorization_acceptances_after_deadline"]==0
assert p["deadline_is_verifier_freshness_gate_not_attacker_price"]
assert p["gossip_never_substitutes_for_missing_local_consistency_chain"]

r=a["independent_rotation_and_gossip"]
assert r["independent_log_rotation_epochs"]=={"A":7,"B":8} and r["witness_rotation_epoch"]==8
for k in (
    "epoch7_accepts_with_A_rotated_B_and_witness_unrotated",
    "epoch8_current_chains_and_quorum_accept",
    "A_old_generation_replay_rejected","B_old_generation_replay_rejected",
    "stale_witness_generation_rejected","mixed_witness_generation_rejected",
    "duplicate_witness_seat_rejected","revoked_current_witness_seat_not_enough",
    "two_distinct_current_witness_seats_accept","two_of_three_matching_population_gossip_accept",
    "one_current_plus_one_fork_gossip_rejected","duplicate_population_gossip_rejected",
    "gossip_certificate_detection_only",
):
    assert r[k],k

e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]

c=a["checkpoint_recovery"]
assert c=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}

for line in (H/"winloop_v56_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V56","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

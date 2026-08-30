#!/usr/bin/env python3
import hashlib, importlib.util, json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / "v67" / "winloop_v67.json").read_text())
assert base["version"] == "V67" and base["digest"] == "972ae30b001ead74b4ec3dff9fa9239343618949218a4551d43d0596209f1162"
assert "91096f108d4a7bd96fc49b506d68757badf6740e8d9d87b4cb449bb09d150248  distributed_winloop_v67.py" in (H.parent / "v67" / "winloop_v67_SHA256SUMS.txt").read_text()

sp = importlib.util.spec_from_file_location("v68", H / "distributed_winloop_v68.py")
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
a = json.loads((H / "winloop_v68.json").read_text())
assert a == m.run_validation() and a["version"] == "V68"
assert a["base"] == {"version": "V67", "digest": "972ae30b001ead74b4ec3dff9fa9239343618949218a4551d43d0596209f1162", "implementation_sha256": "91096f108d4a7bd96fc49b506d68757badf6740e8d9d87b4cb449bb09d150248"}
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]

h = a["temporal_floor_regression"]
assert (h["roots"], h["horizon"], h["floor"], h["budget"], h["h11_floor"], h["h11_budget"], h["carried_from"]) == (22, 22, 1, 851, 2, 398, "V66")

c = a["independence_certificate_gate"]
assert c["patterns"] == 150 and c["hypothetical_gate_admits"] == 4 and c["conservative_cross_role_credit"] == 12
assert not c["credit_raised"] and not c["committed_external_independence_certificate_present"] and all(c["checks"].values())
assert c["stale_or_conflicting_acceptances"] == c["alias_or_unknown_relation_acceptances"] == c["self_asserted_acceptances"] == 0

t = a["tombstone_epoch19"]
assert t["patterns"] == 215796940800 and t["accepted"] == 408240 and t["accepted_base_history_states"] == 3402
assert t["delay_vectors"] == 16384 and t["admissible_shared_deadline_vectors"] == 120 and t["shared_deadline"] == 3 and t["deadline_origin_preserved"] == "epoch12"
assert t["complete_source_disappearance_recoveries"] == 3600
assert t["cold_verifier_restart_recoveries"] == 26280
assert t["combined_disappearance_cold_restart_recoveries"] == 1800
assert t["cached_clear19_after_total_source_loss_recoveries"] == 720
assert t["replacement_after_disappearance_recoveries"] == 42720
assert t["post_deadline_acceptances"] == t["deadline_reset_acceptances"] == t["stale_or_fork_clear_acceptances"] == t["cold_restart_as_authority_acceptances"] == t["unpinned_total_loss_acceptances"] == t["fork_acceptances"] == 0
assert all(t["checks"].values())

s = a["dual_proof_source_loss_publication_root_rollback"]
assert s["patterns"] == 2275983360 and s["accepted"] == 521640 and s["accepted_base_publication_states"] == 14904
assert s["verifier_populations"] == 3 and s["publication_quorum"] == 2 and s["max_tolerated_rollback_views"] == 1
assert s["delay_vectors"] == 256 and s["admissible_shared_deadline_vectors"] == 35 and s["shared_deadline"] == 3
assert s["two_proof_source_loss_recoveries"] == 27720
assert s["publication_rollback_recoveries"] == 10920
assert s["simultaneous_two_source_loss_publication_root_rollback_recoveries"] == 840
assert s["replacement_source_recoveries"] == 123480
assert s["cached_authority_promotion_acceptances"] == s["unbound_root_rollback_acceptances"] == s["fork_acceptances"] == s["stale_or_missing_eviction_proof_acceptances"] == s["untrusted_or_conflicting_join_acceptances"] == s["post_deadline_acceptances"] == 0
assert all(s["checks"].values())

b = a["third_byzantine_eviction_after_rollback"]
assert b["patterns"] == 38698352640 and b["accepted"] == 684390 and b["accepted_base_membership_states"] == 19554
assert b["population_slots"] == 5 and b["quorum"] == 3 and b["max_honest_verifier_losses"] == 1
assert b["delay_vectors"] == 256 and b["admissible_shared_deadline_vectors"] == 35 and b["shared_deadline"] == 3
assert b["rollback_recovery_recoveries"] == 38850
assert b["third_join_recoveries"] == 75600 and b["third_eviction_recoveries"] == 75600
assert b["third_eviction_with_one_honest_verifier_loss_recoveries"] == 50400
assert b["replacement_self_authorization_acceptances"] == b["active_byzantine_acceptances_after_eviction"] == b["two_honest_verifier_loss_acceptances"] == b["untrusted_or_conflicting_join_acceptances"] == b["membership_or_eviction_fork_acceptances"] == b["below_threshold_history_acceptances"] == b["rollback_chain_bypass_acceptances"] == b["post_deadline_acceptances"] == 0
assert all(b["checks"].values())

assert a["checkpoint_recovery"] == {"statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k", "frontier_storage_only": True, "trust_bearing_messages_unchanged": True}
r = a["recursive_publication_recovery_evidence"]
assert r["cached_evidence_never_promoted_to_authority"] and r["cold_restart_never_promoted_to_authority"] and r["publication_and_root_rollback_must_be_same_bound_event"]

for line in (H / "winloop_v68_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({"version": "V68", "validated": True, "digest": a["digest"], "headline": a["headline"]}, indent=2, sort_keys=True))

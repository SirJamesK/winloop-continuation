#!/usr/bin/env python3
import hashlib, importlib.util, json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / "v68" / "winloop_v68.json").read_text())
assert base["version"] == "V68" and base["digest"] == "a1cdcf9262a92b50f572c221d204d980e5add5cbad92e15976e8e0bb9830581b"
assert "ae4d1400e85b33613e52542073b47b6b483d994ef773df8d84d8fdc52dfd0d14  distributed_winloop_v68.py" in (H.parent / "v68" / "winloop_v68_SHA256SUMS.txt").read_text()

sp = importlib.util.spec_from_file_location("v69", H / "distributed_winloop_v69.py")
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
a = json.loads((H / "winloop_v69.json").read_text())
assert a == m.run_validation() and a["version"] == "V69"
assert a["base"] == {"version": "V68", "digest": "a1cdcf9262a92b50f572c221d204d980e5add5cbad92e15976e8e0bb9830581b", "implementation_sha256": "ae4d1400e85b33613e52542073b47b6b483d994ef773df8d84d8fdc52dfd0d14"}
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]

h = a["temporal_floor_regression"]
assert (h["roots"], h["horizon"], h["floor"], h["budget"], h["h11_floor"], h["h11_budget"], h["carried_from"]) == (22, 22, 1, 851, 2, 398, "V66")

c = a["independence_certificate_gate"]
assert c["patterns"] == 150 and c["hypothetical_gate_admits"] == 4 and c["conservative_cross_role_credit"] == 12
assert not c["credit_raised"] and not c["committed_external_independence_certificate_present"] and all(c["checks"].values())
assert c["stale_or_conflicting_acceptances"] == c["alias_or_unknown_relation_acceptances"] == c["self_asserted_acceptances"] == 0

t = a["tombstone_epoch20"]
assert t["patterns"] == 1381100421120 and t["accepted"] == 565455 and t["accepted_base_history_states"] == 3427
assert t["delay_vectors"] == 65536 and t["admissible_shared_deadline_vectors"] == 165 and t["shared_deadline"] == 3 and t["deadline_origin_preserved"] == "epoch12"
assert t["complete_source_disappearance_recoveries"] == 2475 and t["source_reappearance_recoveries"] == 23760
assert t["second_cold_verifier_restart_recoveries"] == 28380 and t["reappearance_second_cold_restart_recoveries"] == 5940
assert t["cached_clear20_after_total_source_loss_recoveries"] == 495 and t["live_clear20_after_bound_reappearance_recoveries"] == 4950
assert t["bound_replacement_source_recoveries"] == 228030
assert t["post_deadline_acceptances"] == t["deadline_reset_acceptances"] == t["stale_or_fork_clear_acceptances"] == t["second_cold_restart_as_authority_acceptances"] == t["unbound_reappearance_acceptances"] == t["unpinned_total_loss_acceptances"] == t["fork_acceptances"] == 0
assert all(t["checks"].values())

s = a["publication_verifier_rollback_delayed_join"]
assert s["patterns"] == 1600000000 and s["accepted"] == 120288 and s["accepted_base_recovery_states"] == 2148
assert s["verifier_populations"] == 3 and s["publication_quorum"] == 2
assert s["delay_vectors"] == 1024 and s["admissible_shared_deadline_vectors"] == 56 and s["shared_deadline"] == 3
assert s["publication_rollback_recoveries"] == 12768 and s["verifier_population_rollback_recoveries"] == 4704
assert s["joint_publication_verifier_rollback_recoveries"] == 4704 and s["delayed_join_evidence_recoveries"] == 672 and s["joint_rollback_delayed_join_recoveries"] == 672
assert s["cached_authority_promotion_acceptances"] == s["unbound_verifier_rollback_acceptances"] == s["unbound_delayed_join_acceptances"] == s["rollback_without_publication_quorum_acceptances"] == s["fork_acceptances"] == s["post_deadline_acceptances"] == 0
assert all(s["checks"].values())

b = a["fourth_byzantine_eviction_identity_recycling"]
assert b["patterns"] == 583087267840 and b["accepted"] == 1111824 and b["accepted_base_membership_states"] == 19854
assert b["population_slots"] == 5 and b["quorum"] == 3 and b["max_honest_verifier_losses"] == 1
assert b["delay_vectors"] == 1024 and b["admissible_shared_deadline_vectors"] == 56 and b["shared_deadline"] == 3
assert b["recycle_prepare_recoveries"] == 60480 and b["fourth_join_recycled_identity_recoveries"] == 40320
assert b["fourth_eviction_recoveries"] == 40320 and b["fourth_eviction_with_one_honest_verifier_loss_recoveries"] == 26880
assert b["recycled_identity_self_authorization_acceptances"] == b["tombstone_bypass_acceptances"] == b["active_byzantine_acceptances_after_eviction"] == b["two_honest_verifier_loss_acceptances"] == b["untrusted_or_conflicting_join_acceptances"] == b["membership_or_eviction_fork_acceptances"] == b["below_threshold_history_acceptances"] == b["rollback_chain_bypass_acceptances"] == b["post_deadline_acceptances"] == 0
assert all(b["checks"].values())

assert a["checkpoint_recovery"] == {"statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k", "frontier_storage_only": True, "trust_bearing_messages_unchanged": True}
r = a["recursive_publication_recovery_evidence"]
assert r["cached_evidence_never_promoted_to_authority"] and r["cold_restart_never_promoted_to_authority"]
assert r["reappearance_requires_pre_loss_binding"] and r["publication_and_verifier_rollbacks_must_share_bound_recovery"] and r["recycled_identity_requires_tombstone_bound_reentry"]

for line in (H / "winloop_v69_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({"version": "V69", "validated": True, "digest": a["digest"], "headline": a["headline"]}, indent=2, sort_keys=True))

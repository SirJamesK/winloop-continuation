#!/usr/bin/env python3
import hashlib, importlib.util, json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / "v69" / "winloop_v69.json").read_text())
assert base["version"] == "V69" and base["digest"] == "0e7cb57a476db0dc3933613f8305b15947261f42578ba7a9c94679b6c57c1d12"
assert "74f83e8001e67a93b56237d5bee152481006753d9bbc4216de06ec7b03db9ca0  distributed_winloop_v69.py" in (H.parent / "v69" / "winloop_v69_SHA256SUMS.txt").read_text()

sp = importlib.util.spec_from_file_location("v70", H / "distributed_winloop_v70.py")
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
a = json.loads((H / "winloop_v70.json").read_text())
assert a == m.run_validation() and a["version"] == "V70"
assert a["base"] == {"version": "V69", "digest": "0e7cb57a476db0dc3933613f8305b15947261f42578ba7a9c94679b6c57c1d12", "implementation_sha256": "74f83e8001e67a93b56237d5bee152481006753d9bbc4216de06ec7b03db9ca0"}
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]

h = a["temporal_floor_regression"]
assert (h["roots"], h["horizon"], h["floor"], h["budget"], h["h11_floor"], h["h11_budget"], h["carried_from"]) == (22, 22, 1, 851, 2, 398, "V66")

c = a["independence_certificate_gate"]
assert c["patterns"] == 150 and c["hypothetical_gate_admits"] == 4 and c["conservative_cross_role_credit"] == 12
assert not c["credit_raised"] and not c["committed_external_independence_certificate_present"] and all(c["checks"].values())
assert c["stale_or_conflicting_acceptances"] == c["alias_or_unknown_relation_acceptances"] == c["self_asserted_acceptances"] == 0

t = a["tombstone_epoch21"]
assert t["patterns"] == 17008070492160 and t["accepted"] == 1375440 and t["accepted_base_history_states"] == 6252
assert t["delay_vectors"] == 262144 and t["admissible_shared_deadline_vectors"] == 220 and t["shared_deadline"] == 3 and t["deadline_origin_preserved"] == "epoch12"
assert t["first_source_disappearance_recoveries"] == 6600 and t["first_bound_reappearance_recoveries"] == 7920
assert t["second_source_disappearance_recoveries"] == 6600 and t["second_bound_reappearance_recoveries"] == 15840
assert t["mixed_verifier_cache_generation_recoveries"] == 654720 and t["second_reappearance_mixed_cold_restart_recoveries"] == 14960
assert t["cached_clear21_after_second_loss_recoveries"] == 1320 and t["live_clear21_after_second_reappearance_recoveries"] == 2640
assert t["bound_replacement_source_recoveries"] == 417120
assert t["post_deadline_acceptances"] == t["deadline_reset_acceptances"] == t["stale_or_fork_clear_acceptances"] == t["mixed_cache_as_authority_acceptances"] == t["unbound_reappearance_acceptances"] == t["unpinned_repeated_loss_acceptances"] == t["fork_acceptances"] == 0
assert all(t["checks"].values())

s = a["publication_verifier_rollback_two_delayed_joins"]
assert s["patterns"] == 160000000000 and s["accepted"] == 339024 and s["accepted_base_recovery_states"] == 4036
assert s["verifier_populations"] == 3 and s["publication_quorum"] == 2
assert s["delay_vectors"] == 4096 and s["admissible_shared_deadline_vectors"] == 84 and s["shared_deadline"] == 3
assert s["publication_rollback_recoveries"] == 123984 and s["verifier_population_rollback_recoveries"] == 51408
assert s["joint_publication_verifier_rollback_recoveries"] == 51408
assert s["first_delayed_join_generation_recoveries"] == 9072 and s["second_delayed_join_generation_recoveries"] == 9072 and s["two_delayed_join_generation_recoveries"] == 3024
assert s["bound_replacement_source_recoveries"] == 82656 and s["joint_rollback_two_delayed_join_replacement_recoveries"] == 2016
assert s["cached_authority_promotion_acceptances"] == s["unbound_verifier_rollback_acceptances"] == s["unbound_delayed_join_acceptances"] == s["unbound_replacement_source_acceptances"] == s["rollback_without_publication_quorum_acceptances"] == s["fork_acceptances"] == s["post_deadline_acceptances"] == 0
assert all(s["checks"].values())

b = a["fifth_byzantine_eviction_identity_collision"]
assert b["patterns"] == 6313601925120 and b["accepted"] == 1468992 and b["accepted_base_membership_states"] == 26232
assert b["population_slots"] == 5 and b["quorum"] == 3 and b["max_honest_verifier_losses"] == 1
assert b["delay_vectors"] == 1024 and b["admissible_shared_deadline_vectors"] == 56 and b["shared_deadline"] == 3
assert b["fifth_collision_prepare_recoveries"] == 13440 and b["fifth_join_collision_bound_recoveries"] == 53760
assert b["fifth_eviction_recoveries"] == 80640 and b["fifth_eviction_with_one_honest_verifier_loss_recoveries"] == 53760 and b["fifth_eviction_concurrent_verifier_loss_recoveries"] == 26880
assert b["recycled_identity_collision_self_authorization_acceptances"] == b["tombstone_collision_bypass_acceptances"] == b["active_byzantine_acceptances_after_eviction"] == b["two_honest_verifier_loss_acceptances"] == b["untrusted_or_conflicting_join_acceptances"] == b["membership_or_eviction_fork_acceptances"] == b["below_threshold_history_acceptances"] == b["rollback_chain_bypass_acceptances"] == b["post_deadline_acceptances"] == 0
assert all(b["checks"].values())

assert a["checkpoint_recovery"] == {"statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k", "frontier_storage_only": True, "trust_bearing_messages_unchanged": True}
r = a["recursive_publication_recovery_evidence"]
assert r["cached_evidence_never_promoted_to_authority"] and r["cold_restart_never_promoted_to_authority"]
assert r["repeated_reappearance_requires_original_pre_loss_binding"] and r["publication_and_verifier_rollbacks_must_share_bound_recovery"]
assert r["delayed_join_generations_never_mint_authority"] and r["replacement_source_requires_rollback_root_binding"] and r["recycled_identity_collision_requires_tombstone_bound_reentry"]

for line in (H / "winloop_v70_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({"version": "V70", "validated": True, "digest": a["digest"], "headline": a["headline"]}, indent=2, sort_keys=True))

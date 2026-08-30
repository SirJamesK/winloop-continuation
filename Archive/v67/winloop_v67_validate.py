#!/usr/bin/env python3
import hashlib, importlib.util, json
from pathlib import Path
H = Path(__file__).resolve().parent
base = json.loads((H.parent / "v66" / "winloop_v66.json").read_text())
assert base["version"] == "V66" and base["digest"] == "df35c786955dd2f202c493be6a67a6eee32be8f37ede43a204b8be72a16c0c62"
assert "dfd71b33ba7fbef697d3c2a256b5ce7b314110fd323e21f200d8d8cca92fa835  distributed_winloop_v66.py" in (H.parent / "v66" / "winloop_v66_SHA256SUMS.txt").read_text()
sp = importlib.util.spec_from_file_location("v67", H / "distributed_winloop_v67.py")
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
a = json.loads((H / "winloop_v67.json").read_text())
assert a == m.run_validation() and a["version"] == "V67"
assert a["base"] == {"version": "V66", "digest": "df35c786955dd2f202c493be6a67a6eee32be8f37ede43a204b8be72a16c0c62", "implementation_sha256": "dfd71b33ba7fbef697d3c2a256b5ce7b314110fd323e21f200d8d8cca92fa835"}
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
h = a["temporal_floor_regression"]
assert (h["roots"], h["horizon"], h["floor"], h["budget"], h["h11_floor"], h["h11_budget"], h["carried_from"]) == (22, 22, 1, 851, 2, 398, "V66")
c = a["independence_certificate_gate"]
assert c["patterns"] == 150 and c["hypothetical_gate_admits"] == 4 and c["conservative_cross_role_credit"] == 12
assert not c["credit_raised"] and not c["committed_external_independence_certificate_present"] and all(c["checks"].values())
assert c["stale_or_conflicting_acceptances"] == c["alias_or_unknown_relation_acceptances"] == c["self_asserted_acceptances"] == 0

t = a["tombstone_epoch18"]
assert t["patterns"] == 8808038400 and t["accepted"] == 206808 and t["accepted_base_history_states"] == 2462
assert t["delay_vectors"] == 4096 and t["admissible_shared_deadline_vectors"] == 84 and t["shared_deadline"] == 3 and t["deadline_origin_preserved"] == "epoch12"
assert t["dual_source_replacement_recoveries"] == 9072 and t["verifier_restart_recoveries"] == 16296
assert t["both_old_sources_lost_cached_recoveries"] == 5880 and t["clear18_after_source_replacement_recoveries"] == 1008
assert t["post_deadline_acceptances"] == t["deadline_reset_acceptances"] == t["stale_or_fork_clear_acceptances"] == t["restart_as_new_authority_acceptances"] == t["fork_acceptances"] == 0
assert all(t["checks"].values())

s = a["dual_proof_source_loss_rollback"]
assert s["patterns"] == 63221760 and s["accepted"] == 88000 and s["accepted_base_publication_states"] == 4400
assert s["verifier_populations"] == 3 and s["publication_quorum"] == 2 and s["max_tolerated_rollback_views"] == 1
assert s["delay_vectors"] == 64 and s["admissible_shared_deadline_vectors"] == 20 and s["shared_deadline"] == 3
assert s["two_proof_source_loss_recoveries"] == 3520 and s["one_rollback_view_recoveries"] == 24000 and s["replacement_source_recoveries"] == 21120
assert s["cached_authority_promotion_acceptances"] == s["fork_acceptances"] == s["stale_or_missing_eviction_proof_acceptances"] == s["untrusted_or_conflicting_join_acceptances"] == s["post_deadline_acceptances"] == 0
assert all(s["checks"].values())

b = a["consecutive_byzantine_eviction_join_rollback"]
assert b["patterns"] == 900000000 and b["accepted"] == 187800 and b["accepted_base_membership_states"] == 9390
assert b["population_slots"] == 5 and b["quorum"] == 3 and b["max_honest_verifier_losses"] == 1
assert b["delay_vectors"] == 64 and b["admissible_shared_deadline_vectors"] == 20 and b["shared_deadline"] == 3
assert b["second_eviction_recoveries"] == 28800 and b["join_rollback_recoveries"] == 9600 and b["one_honest_verifier_loss_recoveries"] == 128400
assert b["replacement_self_authorization_acceptances"] == b["active_byzantine_acceptances_after_eviction"] == b["two_honest_verifier_loss_acceptances"] == b["untrusted_or_conflicting_join_acceptances"] == b["membership_or_eviction_fork_acceptances"] == b["below_threshold_history_acceptances"] == b["post_deadline_acceptances"] == 0
assert all(b["checks"].values())

assert a["checkpoint_recovery"] == {"statements": 513, "max_lag": 64, "shared_audit": "132 + 4*k", "frontier_storage_only": True, "trust_bearing_messages_unchanged": True}
assert a["recursive_publication_recovery_evidence"]["cached_evidence_never_promoted_to_authority"]
for line in (H / "winloop_v67_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d
print(json.dumps({"version": "V67", "validated": True, "digest": a["digest"], "headline": a["headline"]}, indent=2, sort_keys=True))

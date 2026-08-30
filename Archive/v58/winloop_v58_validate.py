#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))
base=json.loads((H.parent/"v57"/"winloop_v57.json").read_text())
assert base["version"]=="V57" and base["digest"]=="bb5eec783aa363ef049af847df3e9924c21bc7c0d75fe9f4a3b09ad0c3395790"
assert "018a2f9307098fe5130ca4bbabfaa73b6d9c53e93609946abfea9b7e5cafa79f  distributed_winloop_v57.py" in (H.parent/"v57"/"winloop_v57_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v58",H/"distributed_winloop_v58.py")
m=importlib.util.module_from_spec(s); sys.modules["v58"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v58.json").read_text())
assert a==m.run_validation() and a["version"]=="V58"
assert a["base"]=={"version":"V57","digest":"bb5eec783aa363ef049af847df3e9924c21bc7c0d75fe9f4a3b09ad0c3395790","implementation_sha256":"018a2f9307098fe5130ca4bbabfaa73b6d9c53e93609946abfea9b7e5cafa79f"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]

h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v57_regression_preserved"]

t=a["multi_issuer_monotonic_quorum"]
assert (t["issuers"],t["quorum"],t["patterns"],t["accepted"])==(3,2,10290,80)
assert t["all_current_acceptances"]==20 and t["single_partition_recovery_acceptances"]==60
assert t["stale_acceptances_after_deadline"]==0 and t["tampered_expiry_rejected"]
assert t["rotation_epoch"]==8 and t["canonical_target"]=="A8|B8|W8"
assert t["expected_generation"]=={"timeA":8,"timeB":8,"timeC":8}
assert t["presented_invalid_or_conflicting_source_fails_closed"]
assert all(v==3810 for v in t["rejected_case_occurrences_by_presented_bad_state"].values())

g=a["split_view_gossip_convergence"]
assert (g["populations"],g["patterns"])==(3,2058)
assert g["accepted_after_canonical_quorum_convergence"]==76
assert g["all_canonical_acceptances"]==4 and g["split_view_recoveries"]==72
assert g["forked_view_recoveries"]==36 and g["missing_view_recoveries"]==24 and g["stale_view_recoveries"]==12
assert g["post_deadline_acceptances"]==0 and all(g["checks"].values())
assert g["target_root_prebound_by_epoch_certificate"] and g["fork_never_authorizes_without_two_canonical_population_views"]

c=a["composed_gate"]
assert c["requires_time_quorum_and_log_gossip"]
assert c["independent_pattern_product"]==21176820 and c["accepted_pattern_product"]==6080
assert c["post_deadline_stale_acceptance"]==0 and c["unknown_stale_conflicting_or_unbound_fails_closed"]

e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]

k=a["checkpoint_recovery"]
assert k=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}

for line in (H/"winloop_v58_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V58","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

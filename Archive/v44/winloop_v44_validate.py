#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("winloop_v44",H/"distributed_winloop_v44.py"); m=importlib.util.module_from_spec(s); sys.modules["winloop_v44"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v44.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V44" and a["carried_endpoint_theorem"]["fresh_reproof_claimed"] is False and a["routing"]["replacement_merged"] is False
assert (a["static_exact"]["joint_cut"],a["static_exact"]["provenance_cut"],a["static_exact"]["joint_lower_cost"],a["static_exact"]["admitted"])==(21,22,63,True)
assert a["evidence_bound_static"]["evidence_accepted"] and a["evidence_bound_static"]["provenance_cut"]==22 and a["evidence_contract"]["covered_primitive_roots"]==24
c=a["evidence_churn_exact"]
for k in ("current_2of3_dual_log_snapshot_accepted","capability_binding_swap_rejected","stale_evidence_rejected","ceremony_expiry_rejected","single_log_partition_rejected","authentic_dual_log_recovery_accepted","one_issuer_source_loss_tolerated","two_issuer_source_loss_rejected","delayed_log_consumption_rejected","delayed_log_consumption_recovery_accepted","forged_independence_domain_rejected"): assert c[k],k
q=a["second_order_common_control_exact"]; assert q["baseline_independence_evidence"]["provenance_cut"]==22 and q["baseline_independence_evidence"]["admitted"]
for k in ("provider_build_and_cloud_pam_share_control","hsm_management_and_operator_iam_share_control","fabric_local_and_privileged_tenant_share_control","hsm_custody_and_issuance_rotation_share_control"):
 assert q[k]["evidence_accepted"] and q[k]["provenance_cut"]==21 and not q[k]["admitted"],k
assert not q["missing_independence_evidence_fails_closed"]["evidence_accepted"] and not q["missing_independence_evidence_fails_closed"]["admitted"]
t=a["staged_temporal_exact"]
assert (t["strict"]["joint_peak"],t["strict"]["provenance_peak"])==(21,22)
assert (t["all_root_two_epoch_reuse"]["joint_peak"],t["all_root_two_epoch_reuse"]["provenance_peak"])==(11,11)
assert (t["all_root_three_epoch_reuse"]["joint_peak"],t["all_root_three_epoch_reuse"]["provenance_peak"])==(7,8)
assert t["one_deep_root_slow_verifier_consumption"]["provenance_peak"]==21 and (t["four_deep_roots_slow_verifier_consumption"]["joint_peak"],t["four_deep_roots_slow_verifier_consumption"]["provenance_peak"])==(18,18)
assert t["four_deep_roots_fast_consumption"]["provenance_peak"]==22 and t["derived_caps"]=={"ceremony_lifetime":1,"stale_auth_lifetime":2}
assert a["merkle_resource_accounting"]["shared_audit_messages_formula"]=="132 + 4*k"
for line in (H/"winloop_v44_SHA256SUMS.txt").read_text().splitlines():
 if line.strip():
  d,n=line.split(maxsplit=1); assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V44","validated":True,"validation_digest_sha256":a["validation_digest_sha256"],"headline":a["headline"]},indent=2,sort_keys=True))

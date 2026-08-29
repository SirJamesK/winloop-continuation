#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("winloop_v45",H/"distributed_winloop_v45.py"); m=importlib.util.module_from_spec(s); sys.modules["winloop_v45"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v45.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V45" and a["carried_endpoint_theorem"]["fresh_reproof_claimed"] is False and a["routing"]["replacement_merged"] is False
assert (a["static_exact"]["joint_cut"],a["static_exact"]["provenance_cut"],a["static_exact"]["joint_lower_cost"],a["static_exact"]["admitted"])==(21,22,63,True)
assert a["evidence_bound_static"]["evidence_accepted"] and a["evidence_bound_static"]["provenance_cut"]==22 and a["evidence_contract"]["covered_primitive_roots"]==24
c=a["evidence_churn_exact"]
for k in ("current_2of3_dual_log_snapshot_accepted","capability_binding_swap_rejected","stale_or_tampered_evidence_rejected","single_log_partition_rejected","one_issuer_source_loss_tolerated","two_issuer_source_loss_rejected"): assert c[k],k
r=a["revocation_rotation_consistency_exact"]
for k,v in r.items():
 if k!="consistency_model": assert v,k
q=a["second_order_common_control_exact"]; assert q["baseline_independence_evidence"]["provenance_cut"]==22 and q["baseline_independence_evidence"]["admitted"]
for k in ("provider_build_and_cloud_pam_share_control","hsm_management_and_operator_iam_share_control","fabric_local_and_privileged_tenant_share_control","hsm_custody_and_issuance_rotation_share_control","provider_local_and_ca_ceremony_share_control","operator_key_and_hsm_custody_share_control"):
 assert q[k]["evidence_accepted"] and q[k]["provenance_cut"]==21 and not q[k]["admitted"],k
assert not q["missing_independence_evidence_fails_closed"]["evidence_accepted"] and not q["missing_independence_evidence_fails_closed"]["admitted"]
t=a["staged_temporal_robust_cost_exact"]
assert (t["strict"]["joint_peak"],t["strict"]["provenance_peak"],t["strict"]["joint_cost"])==(21,22,{"lower":63,"nominal":84,"upper":126}) and t["strict"]["temporal_admitted"]
assert (t["all_root_two_epoch_reuse"]["joint_peak"],t["all_root_two_epoch_reuse"]["provenance_peak"],t["all_root_two_epoch_reuse"]["joint_cost"])==(11,11,{"lower":32,"nominal":42,"upper":63})
assert (t["all_root_three_epoch_reuse"]["joint_peak"],t["all_root_three_epoch_reuse"]["provenance_peak"],t["all_root_three_epoch_reuse"]["joint_cost"])==(7,8,{"lower":21,"nominal":28,"upper":42})
assert t["one_deep_root_slow_verifier_consumption"]["provenance_peak"]==21 and t["one_deep_root_slow_verifier_consumption"]["joint_cost"]["lower"]==63 and not t["one_deep_root_slow_verifier_consumption"]["temporal_admitted"]
assert (t["four_deep_roots_correlated_slow_consumption"]["joint_peak"],t["four_deep_roots_correlated_slow_consumption"]["provenance_peak"],t["four_deep_roots_correlated_slow_consumption"]["joint_cost"]["lower"])==(18,18,54)
for k in ("provider_cluster_correlated_slow_consumption","hsm_cluster_correlated_slow_consumption"):
 assert (t[k]["joint_peak"],t[k]["provenance_peak"],t[k]["joint_cost"])==(19,19,{"lower":57,"nominal":76,"upper":114}) and not t[k]["temporal_admitted"],k
assert t["derived_caps"]=={"ceremony_lifetime":1,"stale_auth_lifetime":2}
assert a["merkle_resource_accounting"]["shared_audit_messages_formula"]=="132 + 4*k"
for line in (H/"winloop_v45_SHA256SUMS.txt").read_text().splitlines():
 if line.strip():
  d,n=line.split(maxsplit=1); assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V45","validated":True,"validation_digest_sha256":a["validation_digest_sha256"],"headline":a["headline"]},indent=2,sort_keys=True))

#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("winloop_v43", HERE / "distributed_winloop_v43.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["winloop_v43"] = mod
spec.loader.exec_module(mod)
expected = mod.run_validation()
artifact = json.loads((HERE / "winloop_v43.json").read_text())
assert artifact == expected, "winloop_v43.json does not match implementation output"

# Exact V43 contract assertions.
assert artifact["version"] == "V43"
assert artifact["carried_endpoint_theorem"]["fresh_reproof_claimed"] is False
assert artifact["static_exact"]["joint_cut"] == 21
assert artifact["static_exact"]["provenance_cut"] == 22
assert artifact["static_exact"]["joint_lower_cost"] == 63
assert artifact["static_exact"]["admitted"] is True
assert artifact["static_exact"]["nonendpoint"]["recursive_common_fabric"]["root_count"] == 22
assert artifact["static_exact"]["nonendpoint"]["downstream_pam_plane"]["root_count"] == 23
assert artifact["static_exact"]["nonendpoint"]["issuance_ceremony"]["root_count"] == 23
assert artifact["recursive_capability_graph"]["common_privileged_fabric_primitive_roots"] == 11
assert artifact["recursive_capability_graph"]["signed_dependency_cycle_analog_rejected"] is True
assert artifact["recursive_capability_graph"]["unknown_capability_rejected"] is True

for name, case in artifact["recursive_collapse_exact"].items():
    if name == "baseline_recursive_decomposition":
        assert case["provenance_cut"] == 22 and case["admitted"] is True
    else:
        assert case["provenance_cut"] == 21 and case["admitted"] is False, (name, case)

assert artifact["temporal_exact"]["strict"]["joint_peak"] == 21
assert artifact["temporal_exact"]["strict"]["provenance_peak"] == 22
assert artifact["temporal_exact"]["all_root_two_epoch_reuse"]["joint_peak"] == 11
assert artifact["temporal_exact"]["all_root_two_epoch_reuse"]["provenance_peak"] == 11
assert artifact["temporal_exact"]["all_root_three_epoch_reuse"]["joint_peak"] == 7
assert artifact["temporal_exact"]["all_root_three_epoch_reuse"]["provenance_peak"] == 8
assert artifact["temporal_exact"]["one_deep_common_root_extra_epoch"]["provenance_peak"] == 21
assert artifact["temporal_exact"]["four_deep_authority_roots_two_epoch"]["joint_peak"] == 18
assert artifact["temporal_exact"]["four_deep_authority_roots_two_epoch"]["provenance_peak"] == 18
assert artifact["merkle_resource_accounting"]["shared_audit_messages_formula"] == "132 + 4*k"

# Manifest validation. The manifest intentionally excludes itself.
manifest = HERE / "winloop_v43_SHA256SUMS.txt"
assert manifest.exists(), "missing SHA-256 manifest"
for line in manifest.read_text().splitlines():
    if not line.strip():
        continue
    digest, name = line.split(maxsplit=1)
    target = HERE / name.strip()
    actual = hashlib.sha256(target.read_bytes()).hexdigest()
    assert actual == digest, f"SHA-256 mismatch for {name}: {actual} != {digest}"

print(json.dumps({
    "version": artifact["version"],
    "validated": True,
    "validation_digest_sha256": artifact["validation_digest_sha256"],
    "headline": artifact["headline"],
}, indent=2, sort_keys=True))

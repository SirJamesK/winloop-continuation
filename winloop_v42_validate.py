#!/usr/bin/env python3
import importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("winloop_v42", HERE / "distributed_winloop_v42.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["winloop_v42"] = mod
spec.loader.exec_module(mod)
result = mod.run_validation()
print(json.dumps(result, indent=2, sort_keys=True))

# Contract assertions.
assert result["static_exact"]["deep_hardened"]["admitted"] is True
assert result["static_exact"]["common_privileged_fabric_without_fabric_local"]["admitted"] is False
assert result["temporal_exact"]["four_root_common_fabric_core_two_epoch"]["winner"] == "provenance"
assert result["merkle_resource_accounting"]["shared_audit_messages_formula"] == "132 + 4*k"

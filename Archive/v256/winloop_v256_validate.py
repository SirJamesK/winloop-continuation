#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v256 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v256.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V256" and a["base"] == {
    "version": "V255",
    "digest": "8717cbfa612546507e3c852f4d7056fce635371a285abde3e20054b35c7f1f48",
    "implementation_sha256": "9642c46e6f7794281c50af8ea0d3ab6c316826748f4db6ced9b9783551124777",
}
c, t, s, b = m.indep(), m.gc207(), m.publication181(), m.membership93()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    4823331840 // 8373840,
    225918858240 // 8171255,
    6108902800 // 8038030,
) == (
    t["epoch206_complete_seed_states"],
    s["bound_one_hundred_eightieth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch207_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_first_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    44119676160,
    4902186240,
    2526070136832,
    229642739712,
    68311691800,
    6210153800,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v256.py",
    "winloop_v256.json",
    "winloop_v256_report.md",
    "winloop_v256_validate.py",
}
seen = set()
for line in (H / "winloop_v256_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v256.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "897d379f4dace02b4c69586e1ce71e57cb7b4347cdaf6cfe301f32ae2a1c5984"
print(json.dumps({"version": "V256", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

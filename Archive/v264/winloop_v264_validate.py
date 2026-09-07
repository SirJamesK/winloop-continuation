#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v264 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v264.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V264" and a["base"] == {
    "version": "V263",
    "digest": "7e7d22a01ba8499261cb6d2b1947f6e686b3c003eacb6ffc2b30350c5bbab120",
    "implementation_sha256": "a3ded951d5e6ecf9ddfbd95e4e1df9f08f92a20a33e861a787c71ca1cff89c9a",
}
c, t, s, b = m.indep(), m.gc215(), m.publication189(), m.membership97()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5478359040 // 9511040,
    256861836288 // 9290431,
    6950405200 // 9145270,
) == (
    t["epoch214_complete_seed_states"],
    s["bound_one_hundred_eighty_eighth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch215_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_ninth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    50077626624,
    5564180736,
    2870092431360,
    260917493760,
    77668003160,
    7060727560,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v264.py",
    "winloop_v264.json",
    "winloop_v264_report.md",
    "winloop_v264_validate.py",
}
seen = set()
for line in (H / "winloop_v264_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v264.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "128a91fc09591669f3f572286e2e72d2c9a267d32fc6987d33fbf435fe38ce13"
print(json.dumps({"version": "V264", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

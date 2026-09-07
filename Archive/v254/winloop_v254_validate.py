#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v254 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v254.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V254" and a["base"] == {
    "version": "V253",
    "digest": "340b5bdefd5b9baf34622a33f153c3f3f1c2bb59cf25a9a71c42847a512535d6",
    "implementation_sha256": "0002f0f5baf9ee35cb0641f86ec91bbe9364e9c897bef3a2d7d10e16863f3c3f",
}
c, t, s, b = m.indep(), m.gc205(), m.publication179(), m.membership92()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    4668168960 // 8104460,
    218592304128 // 7906261,
    5909714400 // 7775940,
) == (
    t["epoch204_complete_seed_states"],
    s["bound_one_hundred_seventy_eighth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch205_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_seventy_ninth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    42707948544,
    4745327616,
    2444589987840,
    222235453440,
    66096341960,
    6008758360,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v254.py",
    "winloop_v254.json",
    "winloop_v254_report.md",
    "winloop_v254_validate.py",
}
seen = set()
for line in (H / "winloop_v254_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v254.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "c7492aa24a00bed66cbb17ae8018b0a29f1c7da7d16628ac42d9841615373e4e"
print(json.dumps({"version": "V254", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

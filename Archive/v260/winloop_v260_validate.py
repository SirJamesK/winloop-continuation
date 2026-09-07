#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v260 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v260.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V260" and a["base"] == {
    "version": "V259",
    "digest": "73be9257533223ffdd0521c9334c81b7e15062651c10701f37320cfb5d6c8e0b",
    "implementation_sha256": "921243c1753cc3a33215be48fdb780e18870cc4ba96e160afa7addb41d706b65",
}
c, t, s, b = m.indep(), m.gc211(), m.publication185(), m.membership95()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5143896576 // 8930376,
    241059456000 // 8718875,
    6520606960 // 8579746,
) == (
    t["epoch210_complete_seed_states"],
    s["bound_one_hundred_eighty_fourth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch211_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_fifth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    47035779840,
    5226197760,
    2694422016000,
    244947456000,
    72889795000,
    6626345000,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v260.py",
    "winloop_v260.json",
    "winloop_v260_report.md",
    "winloop_v260_validate.py",
}
seen = set()
for line in (H / "winloop_v260_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v260.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "20425a75d5c99d149d8e1b7bbbac2ec20ecc05c2db31c3cd2a740648f6a5a587"
print(json.dumps({"version": "V260", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v253 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v253.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V253" and a["base"] == {
    "version": "V252",
    "digest": "e6c68201bf26c21e1f4e744a3576595de240af3475ef872c1c93cacb2dfdf631",
    "implementation_sha256": "40918a49ed9c0fe83bab377f26fdcd9ac4f58898289208cd3c0158313b7e0a68",
}
c, t, s, b = m.indep(), m.gc204(), m.publication178(), m.membership91()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    4591851264 // 7971964,
    214989189120 // 7775940,
    5811764840 // 7647059,
) == (
    t["epoch203_complete_seed_states"],
    s["bound_one_hundred_seventy_seventh_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch204_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_seventy_eighth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    32677182720,
    4668168960,
    2404515345408,
    218592304128,
    41368000800,
    5909714400,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v253.py",
    "winloop_v253.json",
    "winloop_v253_report.md",
    "winloop_v253_validate.py",
}
seen = set()
for line in (H / "winloop_v253_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v253.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "340b5bdefd5b9baf34622a33f153c3f3f1c2bb59cf25a9a71c42847a512535d6"
print(json.dumps({"version": "V253", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

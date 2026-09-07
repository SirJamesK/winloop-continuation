#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v255 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v255.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V255" and a["base"] == {
    "version": "V254",
    "digest": "c7492aa24a00bed66cbb17ae8018b0a29f1c7da7d16628ac42d9841615373e4e",
    "implementation_sha256": "cec47071c42e0f3452b61c1fb5565c68d1010bedc89c4eb66e9130b9b7596497",
}
c, t, s, b = m.indep(), m.gc206(), m.publication180(), m.membership92()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    4745327616 // 8238416,
    222235453440 // 8038030,
    6008758360 // 7906261,
) == (
    t["epoch205_complete_seed_states"],
    s["bound_one_hundred_seventy_ninth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch206_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eightieth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    33763322880,
    4823331840,
    2485107440640,
    225918858240,
    42762319600,
    6108902800,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v255.py",
    "winloop_v255.json",
    "winloop_v255_report.md",
    "winloop_v255_validate.py",
}
seen = set()
for line in (H / "winloop_v255_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v255.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "8717cbfa612546507e3c852f4d7056fce635371a285abde3e20054b35c7f1f48"
print(json.dumps({"version": "V255", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

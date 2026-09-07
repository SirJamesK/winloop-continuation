#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v259 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v259.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V259" and a["base"] == {
    "version": "V258",
    "digest": "70c7158661beff69286d97ba68dc15e476b80a82690adbcf8a537be5720d596d",
    "implementation_sha256": "09a6a6431954ce60d3801e1edcfcd53f2a006e48412b586fd2fc050bc86bc0ca",
}
c, t, s, b = m.indep(), m.gc210(), m.publication184(), m.membership94()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5062464000 // 8789000,
    237212817408 // 8579746,
    6415999800 // 8442105,
) == (
    t["epoch209_complete_seed_states"],
    s["bound_one_hundred_eighty_third_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch210_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_fourth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    36007276032,
    5143896576,
    2651654016000,
    241059456000,
    45644248720,
    6520606960,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v259.py",
    "winloop_v259.json",
    "winloop_v259_report.md",
    "winloop_v259_validate.py",
}
seen = set()
for line in (H / "winloop_v259_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v259.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "73be9257533223ffdd0521c9334c81b7e15062651c10701f37320cfb5d6c8e0b"
print(json.dumps({"version": "V259", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

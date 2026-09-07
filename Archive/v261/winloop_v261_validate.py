#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v261 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v261.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V261" and a["base"] == {
    "version": "V260",
    "digest": "20425a75d5c99d149d8e1b7bbbac2ec20ecc05c2db31c3cd2a740648f6a5a587",
    "implementation_sha256": "e23eb119a374f4136a866c812d6008437e05a42327f573c66a3f583b581d8708",
}
c, t, s, b = m.indep(), m.gc212(), m.publication186(), m.membership95()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5226197760 // 9073260,
    244947456000 // 8859500,
    6626345000 // 8718875,
) == (
    t["epoch211_complete_seed_states"],
    s["bound_one_hundred_eighty_fifth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch212_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_sixth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    37165605120,
    5309372160,
    2737647424512,
    248877038592,
    47132540000,
    6733220000,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v261.py",
    "winloop_v261.json",
    "winloop_v261_report.md",
    "winloop_v261_validate.py",
}
seen = set()
for line in (H / "winloop_v261_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v261.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "8610ec2b9b60aeb1e4a44662255ad519f50606fef9f511289642bcd8ed0d6623"
print(json.dumps({"version": "V261", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

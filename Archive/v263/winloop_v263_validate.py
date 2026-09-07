#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v263 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v263.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V263" and a["base"] == {
    "version": "V262",
    "digest": "21d1f73ff58060327a4646146a31ca951b4653df8336eff043a1685d1f2e9035",
    "implementation_sha256": "56de6c3421259cb8b5b296283de99c21ddc8e8ec3731704a0c83cecd3e34c50d",
}
c, t, s, b = m.indep(), m.gc214(), m.publication188(), m.membership96()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5393424384 // 9363584,
    252848424960 // 9145270,
    6841238040 // 9001629,
) == (
    t["epoch213_complete_seed_states"],
    s["bound_one_hundred_eighty_seventh_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch214_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_eighth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    38348513280,
    5478359040,
    2825480199168,
    256861836288,
    48652836400,
    6950405200,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v263.py",
    "winloop_v263.json",
    "winloop_v263_report.md",
    "winloop_v263_validate.py",
}
seen = set()
for line in (H / "winloop_v263_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v263.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "7e7d22a01ba8499261cb6d2b1947f6e686b3c003eacb6ffc2b30350c5bbab120"
print(json.dumps({"version": "V263", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

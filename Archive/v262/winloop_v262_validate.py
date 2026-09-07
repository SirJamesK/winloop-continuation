#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v262 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v262.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V262" and a["base"] == {
    "version": "V261",
    "digest": "8610ec2b9b60aeb1e4a44662255ad519f50606fef9f511289642bcd8ed0d6623",
    "implementation_sha256": "26932d997f8dc048edcc0053e4aca5fbed51e6705f1ca7e7216c7bf08d9b9828",
}
c, t, s, b = m.indep(), m.gc213(), m.publication187(), m.membership96()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5309372160 // 9217660,
    248877038592 // 9001629,
    6733220000 // 8859500,
) == (
    t["epoch212_complete_seed_states"],
    s["bound_one_hundred_eighty_sixth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch213_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_seventh_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    48540819456,
    5393424384,
    2781332674560,
    252848424960,
    75253618440,
    6841238040,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v262.py",
    "winloop_v262.json",
    "winloop_v262_report.md",
    "winloop_v262_validate.py",
}
seen = set()
for line in (H / "winloop_v262_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v262.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "21d1f73ff58060327a4646146a31ca951b4653df8336eff043a1685d1f2e9035"
print(json.dumps({"version": "V262", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v257 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v257.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V257" and a["base"] == {
    "version": "V256",
    "digest": "897d379f4dace02b4c69586e1ce71e57cb7b4347cdaf6cfe301f32ae2a1c5984",
    "implementation_sha256": "029224b548bfd0c25d907a85b52d8b25d0409043c48269c9bc64fbf5a0394ca1",
}
c, t, s, b = m.indep(), m.gc208(), m.publication182(), m.membership93()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    4902186240 // 8510740,
    229642739712 // 8305944,
    6210153800 // 8171255,
) == (
    t["epoch207_complete_seed_states"],
    s["bound_one_hundred_eighty_first_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch208_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_second_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    34873267968,
    4981895424,
    2567480509440,
    233407319040,
    44187622080,
    6312517440,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v257.py",
    "winloop_v257.json",
    "winloop_v257_report.md",
    "winloop_v257_validate.py",
}
seen = set()
for line in (H / "winloop_v257_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v257.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "8bf27f7873799177b4981670504f72eb305bda2ecc3c5f2dfd2d389874dfde20"
print(json.dumps({"version": "V257", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

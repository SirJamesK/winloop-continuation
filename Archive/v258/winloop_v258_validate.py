#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v258 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v258.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V258" and a["base"] == {
    "version": "V257",
    "digest": "8bf27f7873799177b4981670504f72eb305bda2ecc3c5f2dfd2d389874dfde20",
    "implementation_sha256": "107ac3d4284db8b9b08795757c7a39f2d91eb010ef10d9293e60ded0c4a0ee38",
}
c, t, s, b = m.indep(), m.gc209(), m.publication183(), m.membership94()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    4981895424 // 8649124,
    233407319040 // 8442105,
    6312517440 // 8305944,
) == (
    t["epoch208_complete_seed_states"],
    s["bound_one_hundred_eighty_second_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch209_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_eighty_third_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    45562176000,
    5062464000,
    2609340991488,
    237212817408,
    70575997800,
    6415999800,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v258.py",
    "winloop_v258.json",
    "winloop_v258_report.md",
    "winloop_v258_validate.py",
}
seen = set()
for line in (H / "winloop_v258_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v258.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "70c7158661beff69286d97ba68dc15e476b80a82690adbcf8a537be5720d596d"
print(json.dumps({"version": "V258", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

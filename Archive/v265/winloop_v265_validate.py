#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v265 as m

H = Path(__file__).resolve().parent
a = json.loads((H / "winloop_v265.json").read_text())
assert a == m.run_validation()
assert a["version"] == "V265" and a["base"] == {
    "version": "V264",
    "digest": "128a91fc09591669f3f572286e2e72d2c9a267d32fc6987d33fbf435fe38ce13",
    "implementation_sha256": "44b2d6407bf380a8736dc55768e88460180023a0f193a360e6995931bc00f0ef",
}
c, t, s, b = m.indep(), m.gc216(), m.publication190(), m.membership97()
assert all(c["checks"] + t["checks"] + s["checks"] + b["checks"])
assert not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (
    5564180736 // 9660036,
    260917493760 // 9437120,
    7060727560 // 9290431,
) == (
    t["epoch215_complete_seed_states"],
    s["bound_one_hundred_eighty_ninth_restart_seed_states"],
    b["bound_quorum_churn_seed_states"],
) == (576, 27648, 760)
assert (
    t["accepted"],
    t["epoch216_bound_verifier_binding_states"],
    s["accepted"],
    s["bound_one_hundred_ninetieth_restart_recoveries"],
    b["accepted"],
    b["bound_replication_quorum_churn_states"],
) == (
    39556258560,
    5650894080,
    2915171804160,
    265015618560,
    50205478400,
    7172211200,
)
assert a["admission"] == {"joint": 21, "provenance": 22, "lower": 63, "preserved": True}
assert a["routing"] == {"active": "V21 guarded", "replacement": False}
assert not a["runtime"]["new_routing_envelope"]
required = {
    "distributed_winloop_v265.py",
    "winloop_v265.json",
    "winloop_v265_report.md",
    "winloop_v265_validate.py",
}
seen = set()
for line in (H / "winloop_v265_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(",", ":")).encode()
        if name == "winloop_v265.json"
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required
assert a["digest"] == "81870ca05d1b9c0a25caa34fc83019f629c46ce4c358f6f943ed3d7f7b89d670"
print(json.dumps({"version": "V265", "validated": True, "digest": a["digest"], "headline": a["headline"]}, sort_keys=True))

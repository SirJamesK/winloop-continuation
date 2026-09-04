#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v191 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v191.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V191'
assert a['base'] == {
    'version': 'V190',
    'digest': 'd90eb3a5fefb37142e4ea26763b90d6d50efd747b026ab6f94d9fd9b0de1d0b4',
    'implementation_sha256': 'eef135f15b319a66d43f23a74455f889211e67704ac7e6973a3b5e0a33d99280',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc142(), m.publication116(), m.membership60()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1310561280 // 2275280) == t['epoch141_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (9406172160, 2332880)
assert (
    t['epoch142_bound_fifty_seventh_source_handoff_states'],
    t['epoch142_bound_fifty_seventh_source_binding_states'],
    t['epoch142_bound_verifier_binding_states'],
) == (6718694400, 4031216640, 1343738880)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (60567644160 // 2190670) == s['bound_one_hundred_fifteenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_sixteenth_restart_recoveries'],
) == (683326651392, 2246839, 62120604672)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_sixteenth_restart_states'],
) == (559085442048, 434844232704, 310603023360, 186361814016)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1622938200 // 2135445) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (11654364400, 2190670)
assert (
    b['bound_root60_witness_rebind_states'],
    b['bound_root60_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (8324546000, 4994727600, 1664909200)
assert b['bad_acceptances'] == 0
assert all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,
    'max_lag':64,
    'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,
    'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v191.py',
    'winloop_v191.json',
    'winloop_v191_report.md',
    'winloop_v191_validate.py',
}
seen = set()
for line in (H / 'winloop_v191_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v191.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '74e491bd9d07ad9ad7ae4a2acf1015ab516f7d5ff146aa24416d47e3fa4c7e99'
print(json.dumps({
    'version':'V191',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

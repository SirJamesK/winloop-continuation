#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v193 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v193.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V193'
assert a['base'] == {
    'version': 'V192',
    'digest': '5d8a590b0829aab473c44a606c569f82a54d2c7c1b63654cbe9ec7b9fbcc1bdb',
    'implementation_sha256': 'd9c8ce72d61659e03af7875b7f0dcf1155facc52ce644eed7207975174ee0bd9',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc144(), m.publication118(), m.membership61()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1377471744 // 2391444) == t['epoch143_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (9882351360, 2450980)
assert (
    t['epoch144_bound_fifty_eighth_source_handoff_states'],
    t['epoch144_bound_fifty_eighth_source_binding_states'],
    t['epoch144_bound_verifier_binding_states'],
) == (7058822400, 4235293440, 1411764480)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (63699886080 // 2303960) == s['bound_one_hundred_seventeenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_eighteenth_restart_recoveries'],
) == (718362805248, 2362041, 65305709568)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_eighteenth_restart_states'],
) == (587751386112, 457139966976, 326528547840, 195917128704)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1707597640 // 2246839) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (12257067200, 2303960)
assert (
    b['bound_root61_witness_rebind_states'],
    b['bound_root61_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (8755048000, 5253028800, 1751009600)
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
    'distributed_winloop_v193.py',
    'winloop_v193.json',
    'winloop_v193_report.md',
    'winloop_v193_validate.py',
}
seen = set()
for line in (H / 'winloop_v193_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v193.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '17082b9af88ca3c8369c7ff6963056246b5785e6d327af54fb71e68f1d7ebee8'
print(json.dumps({
    'version':'V193',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

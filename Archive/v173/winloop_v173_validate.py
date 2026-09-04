#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v173 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v173.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V173'
assert a['base'] == {
    'version':'V172',
    'digest':'f0f264da8db532153695b93b1d5c46cffde03f395a474cd859d529e9e37481a2',
    'implementation_sha256':'71ff9651106ccb486a3232f2e438ae56cc6b7f1d7a694723cf350c254aea9bb2',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc124(),m.publication98(),m.membership51()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (803061504//1394204) == t['epoch123_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (5789226240,1435820)
assert (
    t['epoch124_bound_forty_eighth_source_handoff_states'],
    t['epoch124_bound_forty_eighth_source_binding_states'],
    t['epoch124_bound_verifier_binding_states'],
) == (4135161600,2481096960,827032320)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (36863078400//1333300) == s['bound_ninety_seventh_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_eighth_restart_recoveries'],
) == (417780937728,1373701,37980085248)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_eighth_restart_states'],
) == (341820767232,265860596736,189900426240,113940255744)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (983211240//1293699) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (7093156000,1333300)
assert (
    b['bound_root51_witness_rebind_states'],
    b['bound_root51_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (5066540000,3039924000,1013308000)
assert b['bad_acceptances'] == 0 and all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,'max_lag':64,'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v173.py',
    'winloop_v173.json',
    'winloop_v173_report.md',
    'winloop_v173_validate.py',
}
seen = set()
for line in (H/'winloop_v173_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v173.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '2f6217f31a28daba6c95abd5eee7e5832c31bf851603e209de326a9a8964cfd5'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V173',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

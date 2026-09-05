#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v197 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v197.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V197'
assert a['base'] == {
    'version': 'V196',
    'digest': 'd8b8c6225c2254ae4ba26b608e8fb79a3ba8e0fda342c32fd90d7ce8254cbd61',
    'implementation_sha256': '63279d0778a217a030a2974d57635e0010942774625e178e0573f868565a1a32',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc148(), m.publication122(), m.membership63()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1518048000 // 2635500) == t['epoch147_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (10882384128, 2699004)
assert (
    t['epoch148_bound_sixtieth_source_handoff_states'],
    t['epoch148_bound_sixtieth_source_binding_states'],
    t['epoch148_bound_verifier_binding_states'],
) == (7773131520, 4663878912, 1554626304)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (70284644352 // 2542124) == s['bound_one_hundred_twenty_first_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_second_restart_recoveries'],
) == (791987328000, 2604125, 71998848000)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_second_restart_states'],
) == (647989632000, 503991936000, 359994240000, 215996544000)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1885647400 // 2481115) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (13524099680, 2542124)
assert (
    b['bound_root63_witness_rebind_states'],
    b['bound_root63_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (9660071200, 5796042720, 1932014240)
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
    'distributed_winloop_v197.py',
    'winloop_v197.json',
    'winloop_v197_report.md',
    'winloop_v197_validate.py',
}
seen = set()
for line in (H / 'winloop_v197_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v197.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '51fd660f85de40d71d7a5058b2c363186cfc291fa37edc3dcfb38b2fb998e4b2'
print(json.dumps({
    'version':'V197',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

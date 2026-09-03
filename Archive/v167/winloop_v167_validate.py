#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v167 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v167.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V167'
assert a['base'] == {
    'version':'V166',
    'digest':'993479ae487202702932dddc0873e4a186a3f44e99e7946ceddb44db664986fe',
    'implementation_sha256':'f476f36f3eaeb7d2f1f333d59c665290538270775f38cf8dc57ebe15a48f26cc',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc118(),m.publication92(),m.membership48()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (668897280//1161280) == t['epoch117_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4830916608,1198144)
assert (
    t['epoch118_bound_forty_fifth_source_handoff_states'],
    t['epoch118_bound_forty_fifth_source_binding_states'],
    t['epoch118_bound_verifier_binding_states'],
) == (3450654720,2070392832,690130944)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (30617782272//1107414) == s['bound_ninety_first_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_second_restart_recoveries'],
) == (347659361280,1143135,31605396480)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_second_restart_states'],
) == (284448568320,221237775360,158026982400,94816189440)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (815058200//1072445) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (5891442480,1107414)
assert (
    b['bound_root48_witness_rebind_states'],
    b['bound_root48_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (4208173200,2524903920,841634640)
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
    'distributed_winloop_v167.py',
    'winloop_v167.json',
    'winloop_v167_report.md',
    'winloop_v167_validate.py',
}
seen = set()
for line in (H/'winloop_v167_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v167.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'afc726e917e537c41d479ccfcc1a5e542aa1adcefc449ce9cad6386ebeae7738'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V167',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

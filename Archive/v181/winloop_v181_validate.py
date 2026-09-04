#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v181 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v181.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V181'
assert a['base'] == {
    'version':'V180',
    'digest':'fb9c7c992e3a40990dee4924e8be1194dfbeaff449cd38b02f9b921b5482eb70',
    'implementation_sha256':'f2fb32072cac321d9ae2566cf3a66caa723786f3da5801045df3bdf3ea1ad130',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc132(),m.publication106(),m.membership55()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (1008311040//1750540) == t['epoch131_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (7253326080,1798940)
assert (
    t['epoch132_bound_fifty_second_source_handoff_states'],
    t['epoch132_bound_fifty_second_source_binding_states'],
    t['epoch132_bound_verifier_binding_states'],
) == (5180947200,3108568320,1036189440)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (46437027840//1679580) == s['bound_one_hundred_fifth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_sixth_restart_recoveries'],
) == (525128389632,1726669,47738944512)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_sixth_restart_states'],
) == (429650500608,334172611584,238694722560,143216833536)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1241349800//1633355) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (8935365600,1679580)
assert (
    b['bound_root55_witness_rebind_states'],
    b['bound_root55_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (6382404000,3829442400,1276480800)
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
    'distributed_winloop_v181.py',
    'winloop_v181.json',
    'winloop_v181_report.md',
    'winloop_v181_validate.py',
}
seen = set()
for line in (H/'winloop_v181_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v181.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '995b318e712c0d84d0ef6d7cbe716bf9ed1ba80938b3d7f7cb61c98184c8c201'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V181',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

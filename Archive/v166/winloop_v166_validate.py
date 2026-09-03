#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v166 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v166.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V166'
assert a['base'] == {
    'version':'V165',
    'digest':'2ce9e465accb92df1e7c88102df13a716a827798c34c81f3809fb24a34602723',
    'implementation_sha256':'58c9fe655298e48389bec9a03884f924b382c8d538296b8d3fef8145ece2be2c',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc117(),m.publication91(),m.membership48()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (648103680//1125180) == t['epoch116_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (6020075520,1161280)
assert (
    t['epoch117_bound_forty_fourth_lineage_rotation_states'],
    t['epoch117_bound_forty_fourth_lineage_binding_states'],
    t['epoch117_bound_handed_proof_rebind_states'],
    t['epoch117_bound_verifier_binding_states'],
) == (4682280960,3344486400,2006691840,668897280)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (29650959360//1072445) == s['bound_ninetieth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_first_restart_recoveries'],
) == (336795604992,1107414,30617782272)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_first_restart_states'],
) == (275560040448,214324475904,153088911360,91853346816)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (789047200//1038220) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (8965640200,1072445)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root48_rollover_states'],
    b['bound_root48_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (7335523800,4075291000,2445174600,815058200)
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
    'distributed_winloop_v166.py',
    'winloop_v166.json',
    'winloop_v166_report.md',
    'winloop_v166_validate.py',
}
seen = set()
for line in (H/'winloop_v166_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v166.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '993479ae487202702932dddc0873e4a186a3f44e99e7946ceddb44db664986fe'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V166',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

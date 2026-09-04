#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v177 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v177.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V177'
assert a['base'] == {
    'version':'V176',
    'digest':'de949b3d39a81afdd9231d464506ed6de8fbb9003cafa8dc88ac3720f9f68d92',
    'implementation_sha256':'15189eab2c3026217ba9eb12cac0ee009d066c9d7d5cc43388b0e0ad9c29ad8e',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc128(),m.publication102(),m.membership53()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (901797120//1565620) == t['epoch127_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (6493794048,1610564)
assert (
    t['epoch128_bound_fiftieth_source_handoff_states'],
    t['epoch128_bound_fiftieth_source_binding_states'],
    t['epoch128_bound_verifier_binding_states'],
) == (4638424320,2783054592,927684864)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (41466028032//1499784) == s['bound_one_hundred_first_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_second_restart_recoveries'],
) == (469410923520,1543465,42673720320)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_second_restart_states'],
) == (384063482880,298716042240,213368601600,128021160960)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1107270600//1456935) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (7978850880,1499784)
assert (
    b['bound_root53_witness_rebind_states'],
    b['bound_root53_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (5699179200,3419507520,1139835840)
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
    'distributed_winloop_v177.py',
    'winloop_v177.json',
    'winloop_v177_report.md',
    'winloop_v177_validate.py',
}
seen = set()
for line in (H/'winloop_v177_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v177.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'f7d0db87f3341bddd91179f3cfb4d0deea800750fb12e6b0bffcc350a9e8bcd2'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V177',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

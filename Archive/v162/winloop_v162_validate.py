#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v162 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v162.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V162'
assert a['base'] == {
    'version':'V161',
    'digest':'86c9f6d0247009fcb27d1fa3577c4a4c5d8e47d2bb681113b4abdeffb478dd6d',
    'implementation_sha256':'ec309f91f343346336ab04eec8c5741ed7da0011a5eed47faeb247a93fd619e1',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc113(),m.publication87(),m.membership46()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (569237760//988260) == t['epoch112_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (5294854656,1021384)
assert (
    t['epoch113_bound_forty_second_lineage_rotation_states'],
    t['epoch113_bound_forty_second_lineage_binding_states'],
    t['epoch113_bound_handed_proof_rebind_states'],
    t['epoch113_bound_verifier_binding_states'],
) == (4118220288,2941585920,1764951552,588317184)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (25987156992//939929) == s['bound_eighty_sixth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_seventh_restart_recoveries'],
) == (295603292160,971970,26873026560)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_seventh_restart_states'],
) == (241857239040,188111185920,134365132800,80619079680)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (690536000//908600) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (7857806440,939929)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root46_rollover_states'],
    b['bound_root46_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (6429114360,3571730200,2143038120,714346040)
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
    'distributed_winloop_v162.py',
    'winloop_v162.json',
    'winloop_v162_report.md',
    'winloop_v162_validate.py',
}
seen = set()
for line in (H/'winloop_v162_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v162.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '9727195879013d29b8f45b7a1388ec5d1e45209e0b2e8bd4fafca0ef95acd5b9'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V162',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

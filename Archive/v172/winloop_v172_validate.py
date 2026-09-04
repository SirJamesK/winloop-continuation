#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v172 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v172.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V172'
assert a['base'] == {
    'version':'V171',
    'digest':'f172d28c7de90221819e46a4117ea47ebc3d5c2d01019d71579ee7e4c9988b81',
    'implementation_sha256':'9afd36b7c73880cafea5b5bf822db8da592d6971ded0c5fb03f089dd99c72c11',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc123(),m.publication97(),m.membership51()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (779558400//1353400) == t['epoch122_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (7227553536,1394204)
assert (
    t['epoch123_bound_forty_seventh_lineage_rotation_states'],
    t['epoch123_bound_forty_seventh_lineage_binding_states'],
    t['epoch123_bound_handed_proof_rebind_states'],
    t['epoch123_bound_verifier_binding_states'],
) == (5621430528,4015307520,2409184512,803061504)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (35768189952//1293699) == s['bound_ninety_sixth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_seventh_restart_recoveries'],
) == (405493862400,1333300,36863078400)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_seventh_restart_states'],
) == (331767705600,258041548800,184315392000,110589235200)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (953716400//1254890) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (10815323640,1293699)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root51_rollover_states'],
    b['bound_root51_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (8848901160,4916056200,2949633720,983211240)
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
    'distributed_winloop_v172.py',
    'winloop_v172.json',
    'winloop_v172_report.md',
    'winloop_v172_validate.py',
}
seen = set()
for line in (H/'winloop_v172_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v172.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'f0f264da8db532153695b93b1d5c46cffde03f395a474cd859d529e9e37481a2'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V172',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

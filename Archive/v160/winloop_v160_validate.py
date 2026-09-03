#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v160 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v160.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V160'
assert a['base'] == {
    'version':'V159',
    'digest':'a0d1d498c0fae6bfc4d134c6f9db1560f66258ac31fc4ade99e81faeba13b004',
    'implementation_sha256':'c1e5d339dd6ec2a97d525b083fd9771a67831e486a1dc22129e15fdc4379a588',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc111(),m.publication85(),m.membership45()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (532325376//924176) == t['epoch110_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4955178240,955860)
assert (
    t['epoch111_bound_forty_first_lineage_rotation_states'],
    t['epoch111_bound_forty_first_lineage_binding_states'],
    t['epoch111_bound_handed_proof_rebind_states'],
    t['epoch111_bound_verifier_binding_states'],
) == (3854027520,2752876800,1651726080,550575360)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (24274252800//877975) == s['bound_eighty_fourth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_fifth_restart_recoveries'],
) == (276330700800,908600,25120972800)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_fifth_restart_states'],
) == (226088755200,175846809600,125604864000,75362918400)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (644514960//848046) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (7339871000,877975)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root45_rollover_states'],
    b['bound_root45_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (6005349000,3336305000,2001783000,667261000)
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
    'distributed_winloop_v160.py',
    'winloop_v160.json',
    'winloop_v160_report.md',
    'winloop_v160_validate.py',
}
seen = set()
for line in (H/'winloop_v160_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v160.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'bfe50fea5241d4d06161ae84b40c7ae64443aed6b1b54d875922b291df242284'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V160',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

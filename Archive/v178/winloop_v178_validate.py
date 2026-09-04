#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v178 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v178.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V178'
assert a['base'] == {
    'version':'V177',
    'digest':'f7d0db87f3341bddd91179f3cfb4d0deea800750fb12e6b0bffcc350a9e8bcd2',
    'implementation_sha256':'bd68377e1d4770f22f58a73e8ec629c947ebe8ccf6c1cb5771b8ab96a92de1e2',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc129(),m.publication103(),m.membership54()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (927684864//1610564) == t['epoch128_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (8586570240,1656360)
assert (
    t['epoch129_bound_fiftieth_lineage_rotation_states'],
    t['epoch129_bound_fiftieth_lineage_binding_states'],
    t['epoch129_bound_handed_proof_rebind_states'],
    t['epoch129_bound_verifier_binding_states'],
) == (6678443520,4770316800,2862190080,954063360)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (42673720320//1543465) == s['bound_one_hundred_second_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_third_restart_recoveries'],
) == (482951006208,1587986,43904636928)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_third_restart_states'],
) == (395141732352,307332458496,219523184640,131713910784)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1139835840//1499784) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (12903367400,1543465)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root54_rollover_states'],
    b['bound_root54_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (10557300600,5865167000,3519100200,1173033400)
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
    'distributed_winloop_v178.py',
    'winloop_v178.json',
    'winloop_v178_report.md',
    'winloop_v178_validate.py',
}
seen = set()
for line in (H/'winloop_v178_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v178.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '4322827075fb701a166d4eb76162355dbd77fe3d23745ca529c404183a35db08'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V178',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

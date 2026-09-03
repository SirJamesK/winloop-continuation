#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v157 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v157.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V157'
assert a['base'] == {
    'version':'V156',
    'digest':'3db99058ca4aefcf159517a3afec5b912f3ec19b25c8079f480d56b3db2f33da',
    'implementation_sha256':'90da6d7348aeb725e3b1c65b826ec6547e7761ac49ac26ed1480d1c0b47451ee',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc108(),m.publication82(),m.membership43()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (480003840//833340) == t['epoch107_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3479309568,862924)
assert (
    t['epoch108_bound_fortieth_source_handoff_states'],
    t['epoch108_bound_fortieth_source_binding_states'],
    t['epoch108_bound_verifier_binding_states'],
) == (2485221120,1491132672,497044224)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (21848666112//790244) == s['bound_eighty_first_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_second_restart_recoveries'],
) == (249021527040,818805,22638320640)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_second_restart_states'],
) == (203744885760,158468244480,113191603200,67914961920)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (579389800//762355) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (4204098080,790244)
assert (
    b['bound_root43_witness_rebind_states'],
    b['bound_root43_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3002927200,1801756320,600585440)
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
    'distributed_winloop_v157.py',
    'winloop_v157.json',
    'winloop_v157_report.md',
    'winloop_v157_validate.py',
}
seen = set()
for line in (H/'winloop_v157_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v157.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '3804b07e96cb5d35586c9472e4deff835af0fb966d340330b588d83fb6d43973'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V157',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

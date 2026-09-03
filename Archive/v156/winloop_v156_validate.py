#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v156 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v156.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V156'
assert a['base'] == {
    'version':'V155',
    'digest':'a2f8a8f3cfe1397b12cbb3367fc4c8ea148cfc863ed4be9b4e4fb6765677047e',
    'implementation_sha256':'c81688192fbea0611d688e2ef2e01cfbf972fbe7f2e71f2bc4b384e6d930a230',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc107(),m.publication81(),m.membership43()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (463357440//804440) == t['epoch106_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4320034560,833340)
assert (
    t['epoch107_bound_thirty_ninth_lineage_rotation_states'],
    t['epoch107_bound_thirty_ninth_lineage_binding_states'],
    t['epoch107_bound_handed_proof_rebind_states'],
    t['epoch107_bound_verifier_binding_states'],
) == (3360026880,2400019200,1440011520,480003840)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (21077591040//762355) == s['bound_eightieth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_first_restart_recoveries'],
) == (240335327232,790244,21848666112)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_first_restart_states'],
) == (196637995008,152940662784,109243330560,65545998336)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (558698800//735130) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (6373287800,762355)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root43_rollover_states'],
    b['bound_root43_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (5214508200,2896949000,1738169400,579389800)
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
    'distributed_winloop_v156.py',
    'winloop_v156.json',
    'winloop_v156_report.md',
    'winloop_v156_validate.py',
}
seen = set()
for line in (H/'winloop_v156_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v156.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '3db99058ca4aefcf159517a3afec5b912f3ec19b25c8079f480d56b3db2f33da'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V156',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

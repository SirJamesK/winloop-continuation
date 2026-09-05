#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v201 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v201.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V201'
assert a['base'] == {
    'version': 'V200',
    'digest': 'fb27d2d370d8ff674d8931d0e29914e00e4c1da719f317577ffc75e783bdec8a',
    'implementation_sha256': '28e0fce71b89b64e73ce779c3927c3365a2b8a1f1f3fdb0ff47bbd8d54bb1ee7',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc152(), m.publication126(), m.membership65()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1667877120 // 2895620) == t['epoch151_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (11947703040, 2963220)
assert (
    t['epoch152_bound_sixty_second_source_handoff_states'],
    t['epoch152_bound_sixty_second_source_binding_states'],
    t['epoch152_bound_verifier_binding_states'],
) == (8534073600, 5120444160, 1706814720)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (77308231680 // 2796160) == s['bound_one_hundred_twenty_fifth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_sixth_restart_recoveries'],
) == (870477898752, 2862209, 79134354432)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_sixth_restart_states'],
) == (712209189888, 553940481024, 395671772160, 237403063296)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (2075662600 // 2731135) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (14875571200, 2796160)
assert (
    b['bound_root65_witness_rebind_states'],
    b['bound_root65_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (10625408000, 6375244800, 2125081600)
assert b['bad_acceptances'] == 0
assert all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,
    'max_lag':64,
    'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,
    'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v201.py',
    'winloop_v201.json',
    'winloop_v201_report.md',
    'winloop_v201_validate.py',
}
seen = set()
for line in (H / 'winloop_v201_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v201.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '452003633bf644ddc617ae166900bf18d19595410343e46eab3c2770070ded00'
print(json.dumps({
    'version':'V201',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

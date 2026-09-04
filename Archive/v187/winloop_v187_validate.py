#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v187 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v187.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V187'
assert a['base'] == {
    'version': 'V186',
    'digest': '87af61bf894a0b673af7b8f20c3a877fd0670d0c5b8dc1148734d6a5babe1c86',
    'implementation_sha256': '0b735d0553e06959f8a6a60653e97fe6d3b6205f407487bc0e43ff64e4457ee0',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc138(), m.publication112(), m.membership58()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1183311360 // 2054360) == t['epoch137_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (8500197888, 2108184)
assert (
    t['epoch138_bound_fifty_fifth_source_handoff_states'],
    t['epoch138_bound_fifty_fifth_source_binding_states'],
    t['epoch138_bound_verifier_binding_states'],
) == (6071569920, 3642941952, 1214313984)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (54614587392 // 1975354) == s['bound_one_hundred_eleventh_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twelfth_restart_recoveries'],
) == (616709237760, 2027795, 56064476160)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twelfth_restart_states'],
) == (504580285440, 392451333120, 280322380800, 168193428480)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1462107000 // 1923825) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (10508883280, 1975354)
assert (
    b['bound_root58_witness_rebind_states'],
    b['bound_root58_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (7506345200, 4503807120, 1501269040)
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
    'distributed_winloop_v187.py',
    'winloop_v187.json',
    'winloop_v187_report.md',
    'winloop_v187_validate.py',
}
seen = set()
for line in (H / 'winloop_v187_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v187.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'b505e22669e9e070113c712e81b9359d1cda67604fda40e48ba8e8ea71c3a827'
print(json.dumps({
    'version':'V187',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

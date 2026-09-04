#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v194 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v194.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V194'
assert a['base'] == {
    'version': 'V193',
    'digest': '17082b9af88ca3c8369c7ff6963056246b5785e6d327af54fb71e68f1d7ebee8',
    'implementation_sha256': '18a47dfae29776de7231afc51b108169d0ff8dc8fdb97d8480f67781e078fbc8',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc145(), m.publication119(), m.membership62()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1411764480 // 2450980) == t['epoch144_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (13019595264, 2511496)
assert (
    t['epoch145_bound_fifty_eighth_lineage_rotation_states'],
    t['epoch145_bound_fifty_eighth_lineage_binding_states'],
    t['epoch145_bound_handed_proof_rebind_states'],
    t['epoch145_bound_verifier_binding_states'],
) == (10126351872, 7233108480, 4339865088, 1446621696)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (65305709568 // 2362041) == s['bound_one_hundred_eighteenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_nineteenth_restart_recoveries'],
) == (736321259520, 2421090, 66938296320)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_nineteenth_restart_states'],
) == (602444666880, 468568074240, 334691481600, 200814888960)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1751009600 // 2303960) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (19746662760, 2362041)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root62_rollover_states'],
    b['bound_root62_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (16156360440, 8975755800, 5385453480, 1795151160)
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
    'distributed_winloop_v194.py',
    'winloop_v194.json',
    'winloop_v194_report.md',
    'winloop_v194_validate.py',
}
seen = set()
for line in (H / 'winloop_v194_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v194.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'f10a0d3e935a0e68efd38997e26eb14be519f1d0d13ff5e269eda11eee7cd042'
print(json.dumps({
    'version':'V194',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

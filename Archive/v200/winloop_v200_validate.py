#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v200 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v200.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V200'
assert a['base'] == {
    'version': 'V199',
    'digest': '501c8219d470a49bbc8e25bbac739a1fc39f3aa4193b26f07908b1272f5b45a5',
    'implementation_sha256': '8fa3bcedd8ef97911088ed2657bbf560f5a8d354e10647253015e1e1026b1d9c',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc151(), m.publication125(), m.membership65()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1629536256 // 2829056) == t['epoch150_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (15010894080, 2895620)
assert (
    t['epoch151_bound_sixty_first_lineage_rotation_states'],
    t['epoch151_bound_sixty_first_lineage_binding_states'],
    t['epoch151_bound_handed_proof_rebind_states'],
    t['epoch151_bound_verifier_binding_states'],
) == (11675139840, 8339385600, 5003631360, 1667877120)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (75510420480 // 2731135) == s['bound_one_hundred_twenty_fourth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_fifth_restart_recoveries'],
) == (850390548480, 2796160, 77308231680)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_fifth_restart_states'],
) == (695774085120, 541157621760, 386541158400, 231924695040)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (2027015760 // 2667126) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (22832288600, 2731135)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root65_rollover_states'],
    b['bound_root65_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (18680963400, 10378313000, 6226987800, 2075662600)
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
    'distributed_winloop_v200.py',
    'winloop_v200.json',
    'winloop_v200_report.md',
    'winloop_v200_validate.py',
}
seen = set()
for line in (H / 'winloop_v200_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v200.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'fb27d2d370d8ff674d8931d0e29914e00e4c1da719f317577ffc75e783bdec8a'
print(json.dumps({
    'version':'V200',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v198 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v198.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V198'
assert a['base'] == {
    'version': 'V197',
    'digest': '51fd660f85de40d71d7a5058b2c363186cfc291fa37edc3dcfb38b2fb998e4b2',
    'implementation_sha256': '73c02e3b3861f351d6c31c54fc122d856a08ba4f4f069fe470eef14d80448826',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc149(), m.publication123(), m.membership64()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1554626304 // 2699004) == t['epoch148_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (14326087680, 2763520)
assert (
    t['epoch149_bound_sixtieth_lineage_rotation_states'],
    t['epoch149_bound_sixtieth_lineage_binding_states'],
    t['epoch149_bound_handed_proof_rebind_states'],
    t['epoch149_bound_verifier_binding_states'],
) == (11142512640, 7958937600, 4775362560, 1591787520)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (71998848000 // 2604125) == s['bound_one_hundred_twenty_second_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_third_restart_recoveries'],
) == (811147696128, 2667126, 73740699648)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_third_restart_states'],
) == (663666296832, 516184897536, 368703498240, 221222098944)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1932014240 // 2542124) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (21770485000, 2604125)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root64_rollover_states'],
    b['bound_root64_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (17812215000, 9895675000, 5937405000, 1979135000)
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
    'distributed_winloop_v198.py',
    'winloop_v198.json',
    'winloop_v198_report.md',
    'winloop_v198_validate.py',
}
seen = set()
for line in (H / 'winloop_v198_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v198.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'ca138afa9c8b6f868fda5bfd279cf4d5f083ea1dd7381dbed53d72601d9f0ff0'
print(json.dumps({
    'version':'V198',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

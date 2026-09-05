#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v204 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v204.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V204'
assert a['base'] == {
    'version': 'V203',
    'digest': '169ac3385a0f85e7c9c4c6d708ee64f3a37cd3bd1c9e4d1aa5938aebb0e411bc',
    'implementation_sha256': '8cfb26e9ef240e8a3e20f6546d3cb8715a54cd78bc0b1e2bbf6efc7a82739fb4',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc155(), m.publication129(), m.membership67()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1786498560 // 3101560) == t['epoch154_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (16445286144, 3172316)
assert (
    t['epoch155_bound_sixty_third_lineage_rotation_states'],
    t['epoch155_bound_sixty_third_lineage_binding_states'],
    t['epoch155_bound_handed_proof_rebind_states'],
    t['epoch155_bound_verifier_binding_states'],
) == (12790778112, 9136270080, 5481762048, 1827254016)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (82872419328 // 2997411) == s['bound_one_hundred_twenty_eighth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_ninth_restart_recoveries'],
) == (932632842240, 3066580, 84784803840)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_ninth_restart_states'],
) == (763063234560, 593493626880, 423924019200, 254354411520)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (2226260400 // 2929290) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (25058355960, 2997411)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root67_rollover_states'],
    b['bound_root67_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (20502291240, 11390161800, 6834097080, 2278032360)
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
    'distributed_winloop_v204.py',
    'winloop_v204.json',
    'winloop_v204_report.md',
    'winloop_v204_validate.py',
}
seen = set()
for line in (H / 'winloop_v204_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v204.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '0e6109cdd8cf63f2f75e25c996416750792ce26749266c55f17c1b46267beaa4'
print(json.dumps({
    'version':'V204',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

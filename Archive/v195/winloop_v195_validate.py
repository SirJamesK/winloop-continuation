#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v195 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v195.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V195'
assert a['base'] == {
    'version': 'V194',
    'digest': 'f10a0d3e935a0e68efd38997e26eb14be519f1d0d13ff5e269eda11eee7cd042',
    'implementation_sha256': '24405395df930ba9ea77f88fe7f0b93c1a4dfefb2b9cc1027f419cb49ffa1020',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc146(), m.publication120(), m.membership62()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1446621696 // 2511496) == t['epoch145_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (10374336000, 2573000)
assert (
    t['epoch146_bound_fifty_ninth_source_handoff_states'],
    t['epoch146_bound_fifty_ninth_source_binding_states'],
    t['epoch146_bound_verifier_binding_states'],
) == (7410240000, 4446144000, 1482048000)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (66938296320 // 2421090) == s['bound_one_hundred_nineteenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twentieth_restart_recoveries'],
) == (754576542720, 2481115, 68597867520)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twentieth_restart_states'],
) == (617380807680, 480185072640, 342989337600, 205793602560)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1795151160 // 2362041) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (12880198800, 2421090)
assert (
    b['bound_root62_witness_rebind_states'],
    b['bound_root62_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (9200142000, 5520085200, 1840028400)
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
    'distributed_winloop_v195.py',
    'winloop_v195.json',
    'winloop_v195_report.md',
    'winloop_v195_validate.py',
}
seen = set()
for line in (H / 'winloop_v195_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v195.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'da273f02429d022773cca5ecb8c28ed0ea127a309969e092cdb1190736259617'
print(json.dumps({
    'version':'V195',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

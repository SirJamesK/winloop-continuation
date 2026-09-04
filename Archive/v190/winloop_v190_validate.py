#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v190 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v190.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V190'
assert a['base'] == {
    'version': 'V189',
    'digest': '64ad3d3bb583af4d24658888168ef5a242b9d221f16db41925e2853ae9c58ee8',
    'implementation_sha256': '031d7f3731dff1d20d5c527b4a11cd5dbcfc3971a1b44303e197cdfdc7b7b2d3',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc141(), m.publication115(), m.membership60()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1277934336 // 2218636) == t['epoch140_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (11795051520, 2275280)
assert (
    t['epoch141_bound_fifty_sixth_lineage_rotation_states'],
    t['epoch141_bound_fifty_sixth_lineage_binding_states'],
    t['epoch141_bound_handed_proof_rebind_states'],
    t['epoch141_bound_verifier_binding_states'],
) == (9173928960, 6552806400, 3931683840, 1310561280)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (59040783360 // 2135445) == s['bound_one_hundred_fourteenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_fifteenth_restart_recoveries'],
) == (666244085760, 2190670, 60567644160)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_fifteenth_restart_states'],
) == (545108797440, 423973509120, 302838220800, 181702932480)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1581678560 // 2081156) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (17852320200, 2135445)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root60_rollover_states'],
    b['bound_root60_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (14606443800, 8114691000, 4868814600, 1622938200)
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
    'distributed_winloop_v190.py',
    'winloop_v190.json',
    'winloop_v190_report.md',
    'winloop_v190_validate.py',
}
seen = set()
for line in (H / 'winloop_v190_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v190.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'd90eb3a5fefb37142e4ea26763b90d6d50efd747b026ab6f94d9fd9b0de1d0b4'
print(json.dumps({
    'version':'V190',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

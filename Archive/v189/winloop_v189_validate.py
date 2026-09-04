#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v189 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v189.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V189'
assert a['base'] == {
    'version': 'V188',
    'digest': 'eac0be515ec185bc4a59aa8064cb29d6bddb3eff8ccaa393ae292e0cb2ba1d1f',
    'implementation_sha256': '429711fb884ee028f77f76d8a06fc87c3774ad47bb7ac4ff8b06c8f1c20a65ee',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc140(), m.publication114(), m.membership59()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1245853440 // 2162940) == t['epoch139_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (8945540352, 2218636)
assert (
    t['epoch140_bound_fifty_sixth_source_handoff_states'],
    t['epoch140_bound_fifty_sixth_source_binding_states'],
    t['epoch140_bound_verifier_binding_states'],
) == (6389671680, 3833803008, 1277934336)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (57539801088 // 2081156) == s['bound_one_hundred_thirteenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_fourteenth_restart_recoveries'],
) == (649448616960, 2135445, 59040783360)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_fourteenth_restart_states'],
) == (531367050240, 413285483520, 295203916800, 177122350080)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1541124200 // 2027795) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (11071749920, 2081156)
assert (
    b['bound_root59_witness_rebind_states'],
    b['bound_root59_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (7908392800, 4745035680, 1581678560)
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
    'distributed_winloop_v189.py',
    'winloop_v189.json',
    'winloop_v189_report.md',
    'winloop_v189_validate.py',
}
seen = set()
for line in (H / 'winloop_v189_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v189.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '64ad3d3bb583af4d24658888168ef5a242b9d221f16db41925e2853ae9c58ee8'
print(json.dumps({
    'version':'V189',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

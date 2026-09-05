#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v203 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v203.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V203'
assert a['base'] == {
    'version': 'V202',
    'digest': 'e194d32b893a6b83e899bb34a19462d0cb6826210541ab5c4ad689f7f31de56f',
    'implementation_sha256': 'e5581e938e57e04be1d114ba7ee50018500804f1adca6630a7f825e97c413909',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc154(), m.publication128(), m.membership66()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1746353664 // 3031864) == t['epoch153_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (12505489920, 3101560)
assert (
    t['epoch154_bound_sixty_third_source_handoff_states'],
    t['epoch154_bound_sixty_third_source_binding_states'],
    t['epoch154_bound_verifier_binding_states'],
) == (8932492800, 5359495680, 1786498560)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (80989009920 // 2929290) == s['bound_one_hundred_twenty_seventh_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_eighth_restart_recoveries'],
) == (911596612608, 2997411, 82872419328)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_eighth_restart_states'],
) == (745851773952, 580106935296, 414362096640, 248617257984)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (2175278840 // 2862209) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (15583822800, 2929290)
assert (
    b['bound_root66_witness_rebind_states'],
    b['bound_root66_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (11131302000, 6678781200, 2226260400)
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
    'distributed_winloop_v203.py',
    'winloop_v203.json',
    'winloop_v203_report.md',
    'winloop_v203_validate.py',
}
seen = set()
for line in (H / 'winloop_v203_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v203.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '169ac3385a0f85e7c9c4c6d708ee64f3a37cd3bd1c9e4d1aa5938aebb0e411bc'
print(json.dumps({
    'version':'V203',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

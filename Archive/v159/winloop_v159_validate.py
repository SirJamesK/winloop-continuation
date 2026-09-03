#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v159 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v159.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V159'
assert a['base'] == {
    'version':'V158',
    'digest':'f3d3df7343986d4f4ea79d6bb9d2024a923732a5bac4328e1c60f88792484a47',
    'implementation_sha256':'5638ca4cdc3402b9c474133bc34c0098c1be05ae565d71283ac843cf0437aabb',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc110(),m.publication84(),m.membership44()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (514483200//893200) == t['epoch109_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3726277632,924176)
assert (
    t['epoch110_bound_forty_first_source_handoff_states'],
    t['epoch110_bound_forty_first_source_binding_states'],
    t['epoch110_bound_verifier_binding_states'],
) == (2661626880,1596976128,532325376)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (23446775808//848046) == s['bound_eighty_third_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_fourth_restart_recoveries'],
) == (267016780800,877975,24274252800)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_fourth_restart_states'],
) == (218468275200,169919769600,121371264000,72822758400)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (622291800//818805) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (4511604720,848046)
assert (
    b['bound_root44_witness_rebind_states'],
    b['bound_root44_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3222574800,1933544880,644514960)
assert b['bad_acceptances'] == 0 and all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,'max_lag':64,'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v159.py',
    'winloop_v159.json',
    'winloop_v159_report.md',
    'winloop_v159_validate.py',
}
seen = set()
for line in (H/'winloop_v159_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v159.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'a0d1d498c0fae6bfc4d134c6f9db1560f66258ac31fc4ade99e81faeba13b004'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V159',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

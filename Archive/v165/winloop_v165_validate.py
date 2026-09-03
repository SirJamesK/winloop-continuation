#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v165 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v165.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V165'
assert a['base'] == {
    'version':'V164',
    'digest':'2b0092fc11df7b3cb3a8355d95c1821ada8082708567d73ceca71a26b7793166',
    'implementation_sha256':'4f1117801a46d52af44242e0fc86e506b301893576701b512b34661c265848e2',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc116(),m.publication90(),m.membership47()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (627745536//1089836) == t['epoch115_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4536725760,1125180)
assert (
    t['epoch116_bound_forty_fourth_source_handoff_states'],
    t['epoch116_bound_forty_fourth_source_binding_states'],
    t['epoch116_bound_verifier_binding_states'],
) == (3240518400,1944311040,648103680)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (28704706560//1038220) == s['bound_eighty_ninth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninetieth_restart_recoveries'],
) == (326160552960,1072445,29650959360)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninetieth_restart_states'],
) == (266858634240,207556715520,148254796800,88952878080)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (763595560//1004731) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (5523330400,1038220)
assert (
    b['bound_root47_witness_rebind_states'],
    b['bound_root47_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3945236000,2367141600,789047200)
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
    'distributed_winloop_v165.py',
    'winloop_v165.json',
    'winloop_v165_report.md',
    'winloop_v165_validate.py',
}
seen = set()
for line in (H/'winloop_v165_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v165.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '2ce9e465accb92df1e7c88102df13a716a827798c34c81f3809fb24a34602723'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V165',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

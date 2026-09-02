#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v139 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v139.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V139'
assert a['base'] == {
    'version':'V138',
    'digest':'263f2638cc720938c77a71d4cd80e2b43c623ef7d7b6585f0840a8fa557add5c',
    'implementation_sha256':'f69d6b6966d1a3fde7f3770bec192e35e363cb8c379f9932ac5fbff6f08ad53c',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc90(),m.publication64(),m.membership34()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (236183040//410040) == t['epoch89_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1727857152,428536)
assert (
    t['epoch90_bound_thirty_first_source_handoff_states'],
    t['epoch90_bound_thirty_first_source_binding_states'],
    t['epoch90_bound_verifier_binding_states'],
) == (1234183680,740510208,246836736)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (10597644288//383306) == s['bound_sixty_third_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_fourth_restart_recoveries'],
) == (121953807360,400995,11086709760)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_fourth_restart_states'],
) == (99780387840,77606968320,55433548800,33260129280)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (278270200//366145) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2039187920,383306)
assert (
    b['bound_root34_witness_rebind_states'],
    b['bound_root34_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (1456562800,873937680,291312560)
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
    'distributed_winloop_v139.py',
    'winloop_v139.json',
    'winloop_v139_report.md',
    'winloop_v139_validate.py',
}
seen = set()
for line in (H/'winloop_v139_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v139.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V139',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v123 as m
from winloop_v123_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V122',
    'digest': 'e64fb7c88abb7ab88dddc1c79153bfed0fc3de90563e5815c5662002907f012c',
    'implementation_sha256': '35e0a595c9d66c2103e88887fd84477a346980454162dc1d3e04fbfcf7529267',
}
a = json.loads((H / 'winloop_v123.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V123' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 91

t = m.gc74()
assert (104891904 // 182104) == t['epoch73_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (777853440, 192920)
assert (
    t['epoch74_bound_twenty_third_source_handoff_states'],
    t['epoch74_bound_twenty_third_source_binding_states'],
    t['epoch74_bound_verifier_binding_states'],
) == (
    555609600,
    333365760,
    111121920,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.successor_disappearance_forty_eighth_restart()
assert (4607539200 // 166650) == s['bound_forty_seventh_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_forty_eighth_restart_recoveries']) == (53785340928, 176851, 4889576448)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
) == (44006188032, 34227035136)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root26_witness_rebind_quorum_churn()
assert (119205240 // 156849) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (886578000, 166650)
assert (
    b['bound_root26_witness_rebind_states'],
    b['bound_root26_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    633270000,
    379962000,
    126654000,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '3cfe84048d6bb5a791b717806594df355dce4dc6ac07d8cf37785675cfbb058d'

for line in (H / 'winloop_v123_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v123.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V123', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

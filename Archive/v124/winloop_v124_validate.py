#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v124 as m
from winloop_v124_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V123',
    'digest': '3cfe84048d6bb5a791b717806594df355dce4dc6ac07d8cf37785675cfbb058d',
    'implementation_sha256': '1f9dd890d1414aa9654f29fb3247bdfbc1df16f06744676aa3209717f39a6186',
}
a = json.loads((H / 'winloop_v124.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V124' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 93

t = m.gc75()
assert (111121920 // 192920) == t['epoch74_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (1058344704, 204156)
assert (
    t['epoch75_bound_twenty_third_lineage_rotation_states'],
    t['epoch75_bound_twenty_third_lineage_binding_states'],
    t['epoch75_bound_handed_proof_rebind_states'],
    t['epoch75_bound_verifier_binding_states'],
) == (
    823156992,
    587969280,
    352781568,
    117593856,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.replacement_churn_forty_ninth_restart()
assert (4889576448 // 176851) == s['bound_forty_eighth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_forty_ninth_restart_recoveries']) == (57011834880, 187460, 5182894080)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
) == (46646046720, 36280258560)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root27_rollover_after_root26_witness_source_replacement()
assert (126654000 // 166650) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1478474360, 176851)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_replacement_source_binding_states'],
    b['bound_root27_rollover_states'],
    b['bound_root27_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    1209660840,
    940847320,
    672033800,
    403220280,
    134406760,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '7135cd1437db54d08faae59371bc01fd7d59abb2563059c1f2e364acc10d8f85'

for line in (H / 'winloop_v124_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v124.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V124', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

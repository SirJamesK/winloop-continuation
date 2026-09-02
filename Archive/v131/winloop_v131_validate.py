#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v131 as m
from winloop_v131_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V130',
    'digest': '9a1c7aa413c6648e4873d5502850aeb9db9239c6d146bd71f2f1b2c3fc87b4e9',
    'implementation_sha256': '56faff32575fe574625cad1cb83557e3ab6309f7e8b5710dbfa62e4c55bd161f',
}
a = json.loads((H / 'winloop_v131.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V131' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 111

t = m.gc82()
assert (161763840 // 280840) == t['epoch81_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (1190407680, 295240)
assert (
    t['epoch82_bound_twenty_seventh_source_handoff_states'],
    t['epoch82_bound_twenty_seventh_source_binding_states'],
    t['epoch82_bound_verifier_binding_states'],
) == (
    850291200,
    510174720,
    170058240,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.successor_disappearance_fifty_sixth_restart()
assert (7192074240 // 260130) == s['bound_fifty_fifth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fifty_sixth_restart_recoveries']) == (83276024832, 273819, 7570547712)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
) == (68134929408, 52993833984)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root30_witness_rebind_quorum_churn()
assert (187647800 // 246905) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1383891600, 260130)
assert (
    b['bound_root30_witness_rebind_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    988494000,
    197698800,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'fbe2af2075272e7bfe830cf3a452314603e7a9124bdfff9a7466ace7f691b448'

for line in (H / 'winloop_v131_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v131.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V131', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

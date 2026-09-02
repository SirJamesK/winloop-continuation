#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v130 as m
from winloop_v130_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V129',
    'digest': 'be84448facb110ea4fb9e4655ba9c4bc6208bd2ae3efcbc3fc696abcc267182a',
    'implementation_sha256': '36a4e35c3c201e89256e80c1ec5fd0f16f7046b938b63a097542a7adc784d0be',
}
a = json.loads((H / 'winloop_v130.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V130' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 108

t = m.gc81()
assert (153743616 // 266916) == t['epoch80_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (1455874560, 280840)
assert (
    t['epoch81_bound_twenty_sixth_lineage_rotation_states'],
    t['epoch81_bound_twenty_sixth_lineage_binding_states'],
    t['epoch81_bound_handed_proof_rebind_states'],
    t['epoch81_bound_verifier_binding_states'],
) == (
    1132346880,
    808819200,
    485291520,
    161763840,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.replacement_churn_fifty_fifth_restart()
assert (6826429440 // 246905) == s['bound_fifty_fourth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fifty_fifth_restart_recoveries']) == (79112816640, 260130, 7192074240)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
) == (64728668160, 50344519680)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root30_rollover_after_root29_witness_source_replacement()
assert (177943360 // 234136) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (2064125800, 246905)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root30_rollover_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    1688830200,
    938239000,
    187647800,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '9a1c7aa413c6648e4873d5502850aeb9db9239c6d146bd71f2f1b2c3fc87b4e9'

for line in (H / 'winloop_v130_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v130.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V130', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

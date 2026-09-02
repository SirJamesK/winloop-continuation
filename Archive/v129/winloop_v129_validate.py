#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v129 as m
from winloop_v129_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V128',
    'digest': '0feed1bdd265d16c22d76971ee1766e157d4d05b1614a381328d643425019b46',
    'implementation_sha256': 'bbb519df619e68c3346a4277381626ddbc27fb9cf5b8d500b2862c47eff17bce',
}
a = json.loads((H / 'winloop_v129.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V129' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 106

t = m.gc80()
assert (145992960 // 253460) == t['epoch79_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (1076205312, 266916)
assert (
    t['epoch80_bound_twenty_sixth_source_handoff_states'],
    t['epoch80_bound_twenty_sixth_source_binding_states'],
    t['epoch80_bound_verifier_binding_states'],
) == (
    768718080,
    461230848,
    153743616,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.successor_disappearance_fifty_fourth_restart()
assert (6473392128 // 234136) == s['bound_fifty_third_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fifty_fourth_restart_recoveries']) == (75090723840, 246905, 6826429440)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
) == (61437864960, 47785006080)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root29_witness_rebind_quorum_churn()
assert (168579400 // 221815) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1245603520, 234136)
assert (
    b['bound_root29_witness_rebind_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    889716800,
    177943360,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'be84448facb110ea4fb9e4655ba9c4bc6208bd2ae3efcbc3fc696abcc267182a'

for line in (H / 'winloop_v129_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v129.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V129', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

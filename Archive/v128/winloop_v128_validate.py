#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v128 as m
from winloop_v128_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V127',
    'digest': 'e504148379342f9d436b438211d9bd6a2538607bc9730145739227eaa36e3a81',
    'implementation_sha256': '640dd44b8701eb172a05f635664f8d7e88f3d2634b8a4e008edc1ac2b90d1837',
}
a = json.loads((H / 'winloop_v128.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V128' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 103

t = m.gc79()
assert (138507264 // 240464) == t['epoch78_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (1313936640, 253460)
assert (
    t['epoch79_bound_twenty_fifth_lineage_rotation_states'],
    t['epoch79_bound_twenty_fifth_lineage_binding_states'],
    t['epoch79_bound_handed_proof_rebind_states'],
    t['epoch79_bound_verifier_binding_states'],
) == (
    1021950720,
    729964800,
    437978880,
    145992960,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.replacement_churn_fifty_third_restart()
assert (6132741120 // 221815) == s['bound_fifty_second_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fifty_third_restart_recoveries']) == (71207313408, 234136, 6473392128)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
) == (58260529152, 45313744896)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root29_rollover_after_root28_witness_source_replacement()
assert (159549840 // 209934) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1854373400, 221815)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root29_rollover_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    1517214600,
    842897000,
    168579400,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '0feed1bdd265d16c22d76971ee1766e157d4d05b1614a381328d643425019b46'

for line in (H / 'winloop_v128_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v128.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V128', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

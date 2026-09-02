#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v127 as m
from winloop_v127_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V126',
    'digest': 'c5aa4ba69b62e5ae1b1c541792f915cce1a13e6a47705f6f3c1ee7f56dd2f32e',
    'implementation_sha256': '54260b049f90987b89bfa63e79aff4e4c0b731766e912e0d819f0f3fa345a8aa',
}
a = json.loads((H / 'winloop_v127.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V127' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 101

t = m.gc78()
assert (131281920 // 227920) == t['epoch77_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (969550848, 240464)
assert (
    t['epoch78_bound_twenty_fifth_source_handoff_states'],
    t['epoch78_bound_twenty_fifth_source_binding_states'],
    t['epoch78_bound_verifier_binding_states'],
) == (
    692536320,
    415521792,
    138507264,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.successor_disappearance_fifty_second_restart()
assert (5804255232 // 209934) == s['bound_fifty_first_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fifty_second_restart_recoveries']) == (67460152320, 221815, 6132741120)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
) == (55194670080, 42929187840)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root28_witness_rebind_quorum_churn()
assert (150848600 // 198485) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1116848880, 209934)
assert (
    b['bound_root28_witness_rebind_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    797749200,
    159549840,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'e504148379342f9d436b438211d9bd6a2538607bc9730145739227eaa36e3a81'

for line in (H / 'winloop_v127_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v127.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V127', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

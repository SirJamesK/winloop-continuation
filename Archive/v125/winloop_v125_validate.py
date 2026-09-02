#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v125 as m
from winloop_v125_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V124',
    'digest': '7135cd1437db54d08faae59371bc01fd7d59abb2563059c1f2e364acc10d8f85',
    'implementation_sha256': 'ec247db121f064b265444ca08981acb6f23d3258f91f72a870cadbdbe48441c3',
}
a = json.loads((H / 'winloop_v125.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V125' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 96

t = m.gc76()
assert (117593856 // 204156) == t['epoch75_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (870186240, 215820)
assert (
    t['epoch76_bound_twenty_fourth_source_handoff_states'],
    t['epoch76_bound_twenty_fourth_source_binding_states'],
    t['epoch76_bound_verifier_binding_states'],
) == (
    621561600,
    372936960,
    124312320,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.successor_disappearance_fiftieth_restart()
assert (5182894080 // 187460) == s['bound_forty_ninth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fiftieth_restart_recoveries']) == (60364846080, 198485, 5487713280)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
) == (49389419520, 38413992960)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root27_witness_rebind_quorum_churn()
assert (134406760 // 176851) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (997287200, 187460)
assert (
    b['bound_root27_witness_rebind_states'],
    b['bound_root27_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    712348000,
    427408800,
    142469600,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '10c0bbf37187997ae613078eaa0c889bf5413b05ea140817818617f9bc56c613'

for line in (H / 'winloop_v125_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v125.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V125', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v102 on main.
BASE_VERSION = 'V102'
BASE_DIGEST = '082d8a8d2a02e8c7576cc8f936881047c61439f7654049327852a1d6da1e1e33'
BASE_IMPL_SHA = '29d7cdecf96a0338d5f5b2a70e2aea7f9bf93db30b75f1a44df5eb5d447a7436'
BASE_EPOCH53_COMPLETE = 23998464
BASE_EPOCH53_DEADLINE_VECTORS = 41664
BASE_TWENTY_SEVENTH_RESTART_RECOVERIES = 995051520
BASE_PUB_DEADLINE_VECTORS = 35990
BASE_MEMBERSHIP_QUORUM_CHURN = 24706840
BASE_MEM_DEADLINE_VECTORS = 32509

assert BASE_EPOCH53_COMPLETE // BASE_EPOCH53_DEADLINE_VECTORS == 576
assert BASE_TWENTY_SEVENTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v103', H / 'distributed_winloop_v103.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v103.json').read_text())
assert a == m.run_validation() and a['version'] == 'V103'
assert a['base'] == {
    'version': BASE_VERSION,
    'digest': BASE_DIGEST,
    'implementation_sha256': BASE_IMPL_SHA,
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch54_thirteenth_source_handoff']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch53_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    116583436571692854676874466681100729314622576369280648391485963872889733120, 184504320, 4032, 576, 85070591730234615865843651857942052864, 45760, 3
)
assert (
    t['epoch54_thirteenth_source_handoff_states'],
    t['epoch54_bound_thirteenth_source_handoff_states'],
    t['epoch54_thirteenth_source_binding_states'],
    t['epoch54_bound_thirteenth_source_binding_states'],
    t['epoch54_verifier_binding_states'],
    t['epoch54_bound_verifier_binding_states'],
    t['epoch54_complete_states'],
) == (158146560, 131788800, 105431040, 79073280, 52715520, 26357760, 26357760)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_twenty_eighth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_seventh_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    131509356547959161972668448886283153938952262516736, 12077227008, 304128, 27648, 1329227995784915872903807060280344576, 39711, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_eighth_verifier_cold_restart_states'],
    s['bound_twenty_eighth_restart_states'],
    s['bound_twenty_eighth_restart_recoveries'],
) == (10979297280, 9881367552, 8783437824, 7685508096, 6587578368, 5489648640, 4391718912, 3293789184, 1097929728)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root16_witness_rebind']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    600447982609409500535033118285774745705300937932800, 191466800, 5320, 760, 83076749736557242056487941267521536, 35990, 3
)
assert (
    b['root16_witness_rebind_states'],
    b['bound_root16_witness_rebind_states'],
    b['root16_witness_binding_states'],
    b['bound_root16_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (164114400, 136762000, 109409600, 82057200, 54704800, 27352400)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {
    'statements': 513,
    'max_lag': 64,
    'shared_audit': '132 + 4*k',
    'frontier_storage_only': True,
    'trust_bearing_messages_unchanged': True,
}

EXPECTED_DIGEST = '856c15cb5a682ec56752deef1d89b86b7cb79779b3d7f58c823239c333170d6e'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v103_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v103.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V103', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

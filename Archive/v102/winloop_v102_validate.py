#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v101 on main.
BASE_VERSION = 'V101'
BASE_DIGEST = '8f743ab43afb36782270dd3e6cf23b88505c90e878cbcdd0122609241f445e61'
BASE_IMPL_SHA = '7740b8cf3343429d58835a818d016fc1bc5db3441bd5fc462f2f4797da6e639e'
BASE_EPOCH52_COMPLETE = 21784320
BASE_EPOCH52_DEADLINE_VECTORS = 37820
BASE_TWENTY_SIXTH_RESTART_RECOVERIES = 898808832
BASE_PUB_DEADLINE_VECTORS = 32509
BASE_MEMBERSHIP_QUORUM_CHURN = 22237600
BASE_MEM_DEADLINE_VECTORS = 29260

assert BASE_EPOCH52_COMPLETE // BASE_EPOCH52_DEADLINE_VECTORS == 576
assert BASE_TWENTY_SIXTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v102', H / 'distributed_winloop_v102.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v102.json').read_text())
assert a == m.run_validation() and a['version'] == 'V102'
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

t = a['tombstone_epoch53_twelfth_lineage_rotation']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch52_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    533109355389570145129719889707612054394335098454370097812902927019278336, 215986176, 5184, 576, 5316911983139663491615228241121378304, 41664, 3
)
assert (
    t['epoch53_twelfth_lineage_rotation_states'],
    t['epoch53_bound_twelfth_lineage_rotation_states'],
    t['epoch53_twelfth_lineage_binding_states'],
    t['epoch53_bound_twelfth_lineage_binding_states'],
    t['epoch53_handed_proof_rebind_states'],
    t['epoch53_bound_handed_proof_rebind_states'],
    t['epoch53_verifier_binding_states'],
    t['epoch53_bound_verifier_binding_states'],
    t['epoch53_complete_states'],
) == (191987712, 167989248, 143990784, 119992320, 95993856, 71995392, 47996928, 23998464, 23998464)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_twenty_seventh_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_sixth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    7449166701545305833705298083996453612133432688640, 10945566720, 304128, 27648, 83076749736557242056487941267521536, 35990, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_seventh_verifier_cold_restart_states'],
    s['bound_twenty_seventh_restart_states'],
    s['bound_twenty_seventh_restart_recoveries'],
) == (9950515200, 8955463680, 7960412160, 6965360640, 5970309120, 4975257600, 3980206080, 2985154560, 995051520)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root16_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    852298646977899527574434597173321014922676577239040, 271775240, 8360, 760, 5192296858534827628530496329220096, 32509, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root16_rollover_states'],
    b['bound_root16_rollover_states'],
    b['root16_binding_states'],
    b['bound_root16_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (247068400, 222361560, 197654720, 172947880, 148241040, 123534200, 98827360, 74120520, 49413680, 24706840)
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

EXPECTED_DIGEST = '082d8a8d2a02e8c7576cc8f936881047c61439f7654049327852a1d6da1e1e33'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v102_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v102.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V102', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

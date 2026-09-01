#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v100 on main.
BASE_VERSION = 'V100'
BASE_DIGEST = 'd19985578e5f5359d9860d06f552afb7d51c9e54d8f4124c92a2a6ee9c5b9b9a'
BASE_IMPL_SHA = '5a7be865df7a830061ddca3b3aa3dc513bb1325746b23433fbfbee5739c8cfc5'
BASE_EPOCH51_COMPLETE = 19710720
BASE_EPOCH51_DEADLINE_VECTORS = 34220
BASE_TWENTY_FIFTH_RESTART_RECOVERIES = 808980480
BASE_PUB_DEADLINE_VECTORS = 29260
BASE_MEMBERSHIP_QUORUM_CHURN = 19938600
BASE_MEM_DEADLINE_VECTORS = 26235

assert BASE_EPOCH51_COMPLETE // BASE_EPOCH51_DEADLINE_VECTORS == 576
assert BASE_TWENTY_FIFTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v101', H / 'distributed_winloop_v101.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v101.json').read_text())
assert a == m.run_validation() and a['version'] == 'V101'
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

t = a['tombstone_epoch52_twelfth_source_handoff']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch51_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    367563552051276073912589894298009070706453009775984880988080947855360, 152490240, 4032, 576, 332306998946228968225951765070086144, 37820, 3
)
assert (
    t['epoch52_twelfth_source_handoff_states'],
    t['epoch52_bound_twelfth_source_handoff_states'],
    t['epoch52_twelfth_source_binding_states'],
    t['epoch52_bound_twelfth_source_binding_states'],
    t['epoch52_verifier_binding_states'],
    t['epoch52_bound_verifier_binding_states'],
    t['epoch52_complete_states'],
) == (130705920, 108921600, 87137280, 65352960, 43568640, 21784320, 21784320)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_twenty_sixth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_fifth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    420542095548305687947911807815783395521057521664, 9886897152, 304128, 27648, 5192296858534827628530496329220096, 32509, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_sixth_verifier_cold_restart_states'],
    s['bound_twenty_sixth_restart_states'],
    s['bound_twenty_sixth_restart_recoveries'],
) == (8988088320, 8089279488, 7190470656, 6291661824, 5392852992, 4494044160, 3595235328, 2696426496, 898808832)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root15_witness_rebind']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    1906899916985547416128511070896621572326634291200, 155663200, 5320, 760, 324518553658426726783156020576256, 29260, 3
)
assert (
    b['root15_witness_rebind_states'],
    b['bound_root15_witness_rebind_states'],
    b['root15_witness_binding_states'],
    b['bound_root15_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (133425600, 111188000, 88950400, 66712800, 44475200, 22237600)
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

EXPECTED_DIGEST = '8f743ab43afb36782270dd3e6cf23b88505c90e878cbcdd0122609241f445e61'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v101_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v101.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V101', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v103 on main.
BASE_VERSION = 'V103'
BASE_DIGEST = '856c15cb5a682ec56752deef1d89b86b7cb79779b3d7f58c823239c333170d6e'
BASE_IMPL_SHA = '0f70dfaef73840331091e03a6073fba1d53f8ef62ea8f06177353288f8cbe53d'
BASE_EPOCH54_COMPLETE = 26357760
BASE_EPOCH54_DEADLINE_VECTORS = 45760
BASE_TWENTY_EIGHTH_RESTART_RECOVERIES = 1097929728
BASE_PUB_DEADLINE_VECTORS = 39711
BASE_MEMBERSHIP_QUORUM_CHURN = 27352400
BASE_MEM_DEADLINE_VECTORS = 35990

assert BASE_EPOCH54_COMPLETE // BASE_EPOCH54_DEADLINE_VECTORS == 576
assert BASE_TWENTY_EIGHTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v104', H / 'distributed_winloop_v104.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v104.json').read_text())
assert a == m.run_validation() and a['version'] == 'V104'
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

t = a['tombstone_epoch55_thirteenth_lineage_rotation']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch54_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    168101529079057364858744989249823448081469331743155471002883181103963801911296, 259801344, 5184, 576, 1361129467683753853853498429727072845824, 50116, 3
)
assert (
    t['epoch55_thirteenth_lineage_rotation_states'],
    t['epoch55_bound_thirteenth_lineage_rotation_states'],
    t['epoch55_thirteenth_lineage_binding_states'],
    t['epoch55_bound_thirteenth_lineage_binding_states'],
    t['epoch55_handed_proof_rebind_states'],
    t['epoch55_bound_handed_proof_rebind_states'],
    t['epoch55_verifier_binding_states'],
    t['epoch55_bound_verifier_binding_states'],
    t['epoch55_complete_states'],
) == (230934528, 202067712, 173200896, 144334080, 115467264, 86600448, 57733632, 28866816, 28866816)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_twenty_ninth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_eighth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    2314453403445838662321737693778690303060989580410880, 13284311040, 304128, 27648, 21267647932558653966460912964485513216, 43680, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_ninth_verifier_cold_restart_states'],
    s['bound_twenty_ninth_restart_states'],
    s['bound_twenty_ninth_restart_recoveries'],
) == (12076646400, 10868981760, 9661317120, 8453652480, 7245987840, 6038323200, 4830658560, 3622993920, 1207664640)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root17_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    266525629270530568264608056409533858649609918700584960, 331983960, 8360, 760, 1329227995784915872903807060280344576, 39711, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root17_rollover_states'],
    b['bound_root17_rollover_states'],
    b['root17_binding_states'],
    b['bound_root17_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (301803600, 271623240, 241442880, 211262520, 181082160, 150901800, 120721440, 90541080, 60360720, 30180360)
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

EXPECTED_DIGEST = '94102d09f48829cc3c34d00dfd1f936081c4dd040ac099af821d40aa5676c012'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v104_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v104.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V104', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

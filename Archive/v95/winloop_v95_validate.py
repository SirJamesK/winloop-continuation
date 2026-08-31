#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v94' / 'winloop_v94.json').read_text())
assert base['version'] == 'V94'
assert base['digest'] == '2ece9d9012b3c220c2c35cfb3bb31ab1c0b263d4ec03fd66f2f80a176406f2a2'
assert '7aa45061531ab883434bf93a868022d3aacc4049dc17fec284484382a467ae9d  distributed_winloop_v94.py' in (H.parent / 'v94' / 'winloop_v94_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V95.
t94 = base['tombstone_epoch45_eighth_lineage_handed_proof_rebind']
s94 = base['publication_replacement_churn_nineteenth_restart']
b94 = base['membership_witness_replacement_root12_rollover']
assert t94['deadline_vectors'] == 17296
assert t94['epoch45_complete_states'] == 9962496
assert t94['epoch45_complete_states'] // t94['deadline_vectors'] == 576
assert s94['deadline_vectors'] == 14190
assert s94['bound_nineteenth_restart_recoveries'] == 392325120
assert s94['bound_nineteenth_restart_recoveries'] // s94['deadline_vectors'] == 27648
assert b94['deadline_vectors'] == 12341
assert b94['bound_replication_quorum_churn_states'] == 9379160
assert b94['bound_replication_quorum_churn_states'] // b94['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v95', H / 'distributed_winloop_v95.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v95.json').read_text())
assert a == m.run_validation() and a['version'] == 'V95'
assert a['base'] == {
    'version': 'V94',
    'digest': '2ece9d9012b3c220c2c35cfb3bb31ab1c0b263d4ec03fd66f2f80a176406f2a2',
    'implementation_sha256': '7aa45061531ab883434bf93a868022d3aacc4049dc17fec284484382a467ae9d',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch46_ninth_source_handoff_binding']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch45_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    10574192705719915566784629090457419566432493187891200, 79027200, 4032, 576, 19807040628566084398385987584, 19600, 3
)
assert (
    t['epoch46_ninth_source_handoff_states'],
    t['epoch46_bound_ninth_source_handoff_states'],
    t['epoch46_ninth_source_binding_states'],
    t['epoch46_bound_ninth_source_binding_states'],
    t['epoch46_verifier_binding_states'],
    t['epoch46_bound_verifier_binding_states'],
    t['epoch46_complete_states'],
) == (67737600, 56448000, 45158400, 33868800, 22579200, 11289600, 11289600)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_twentieth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_nineteenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    12502674393829621154498366699778122711040, 4931435520, 304128, 27648, 309485009821345068724781056, 16215, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twentieth_verifier_cold_restart_states'],
    s['bound_twentieth_restart_states'],
    s['bound_twentieth_restart_recoveries'],
) == (4483123200, 4034810880, 3586498560, 3138186240, 2689873920, 2241561600, 1793249280, 1344936960, 448312320)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root12_witness_rebind_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    36388388003532430943978409318415545139200, 75490800, 5320, 760, 19342813113834066795298816, 14190, 3
)
assert (
    b['root12_witness_rebind_states'],
    b['bound_root12_witness_rebind_states'],
    b['root12_witness_binding_states'],
    b['bound_root12_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (64706400, 53922000, 43137600, 32353200, 21568800, 10784400)
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

# Digest is content-derived and pinned after the first exact run.
EXPECTED_DIGEST = '5a8ee21699259de7d8f500b4ddaf37f84f0e5767416efd4e5f749c7f1ebcd235'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v95_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V95', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

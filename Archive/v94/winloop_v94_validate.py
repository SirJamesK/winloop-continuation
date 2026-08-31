#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v93' / 'winloop_v93.json').read_text())
assert base['version'] == 'V93'
assert base['digest'] == '2c920279f12e75debfe52649e41fdd83a072b929d88ad66facecd1719b7877ff'
assert '864efa8cf146e104218e60404a4709b5a40094bbebf4318836e8915df363b03b  distributed_winloop_v93.py' in (H.parent / 'v93' / 'winloop_v93_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V94.
t93 = base['tombstone_epoch44_eighth_source_handoff_binding']
s93 = base['publication_successor_disappearance_eighteenth_restart']
b93 = base['membership_root11_witness_rebind_quorum_churn']
assert t93['deadline_vectors'] == 15180
assert t93['epoch44_complete_states'] == 8743680
assert t93['epoch44_complete_states'] // t93['deadline_vectors'] == 576
assert s93['deadline_vectors'] == 12341
assert s93['bound_eighteenth_restart_recoveries'] == 341203968
assert s93['bound_eighteenth_restart_recoveries'] // s93['deadline_vectors'] == 27648
assert b93['deadline_vectors'] == 10660
assert b93['bound_replication_quorum_churn_states'] == 8101600
assert b93['bound_replication_quorum_churn_states'] // b93['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v94', H / 'distributed_winloop_v94.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v94.json').read_text())
assert a == m.run_validation() and a['version'] == 'V94'
assert a['base'] == {
    'version': 'V93',
    'digest': '2c920279f12e75debfe52649e41fdd83a072b929d88ad66facecd1719b7877ff',
    'implementation_sha256': '864efa8cf146e104218e60404a4709b5a40094bbebf4318836e8915df363b03b',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch45_eighth_lineage_handed_proof_rebind']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch44_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    187456852831539829718016866656450865455214515716096, 89662464, 5184, 576, 1237940039285380274899124224, 17296, 3
)
assert (
    t['epoch45_eighth_lineage_rotation_states'],
    t['epoch45_bound_eighth_lineage_rotation_states'],
    t['epoch45_eighth_lineage_binding_states'],
    t['epoch45_bound_eighth_lineage_binding_states'],
    t['epoch45_handed_proof_rebind_states'],
    t['epoch45_bound_handed_proof_rebind_states'],
    t['epoch45_verifier_binding_states'],
    t['epoch45_bound_verifier_binding_states'],
    t['epoch45_complete_states'],
) == (79699968, 69737472, 59774976, 49812480, 39849984, 29887488, 19924992, 9962496, 9962496)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_nineteenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_eighteenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    683830364047341675078368113898595287040, 4315576320, 304128, 27648, 19342813113834066795298816, 14190, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['nineteenth_verifier_cold_restart_states'],
    s['bound_nineteenth_restart_states'],
    s['bound_nineteenth_restart_recoveries'],
) == (3923251200, 3530926080, 3138600960, 2746275840, 2353950720, 1961625600, 1569300480, 1176975360, 392325120)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_witness_replacement_root12_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    49730796938160988956770492735167911690240, 103170760, 8360, 760, 1208925819614629174706176, 12341, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root12_rollover_states'],
    b['bound_root12_rollover_states'],
    b['root12_binding_states'],
    b['bound_root12_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (93791600, 84412440, 75033280, 65654120, 56274960, 46895800, 37516640, 28137480, 18758320, 9379160)
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
EXPECTED_DIGEST = '2ece9d9012b3c220c2c35cfb3bb31ab1c0b263d4ec03fd66f2f80a176406f2a2'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v94_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V94', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v92' / 'winloop_v92.json').read_text())
assert base['version'] == 'V92'
assert base['digest'] == '16397218b4eb268e2a3ac0dc41be627f8df093ca8285ea129ac91d44d4b6f810'
assert '5199ab84663bbbbfd90f6c6c6a59e0bc96867805f26b236d69d23a93b014c907  distributed_winloop_v92.py' in (H.parent / 'v92' / 'winloop_v92_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V93.
t92 = base['tombstone_epoch43_seventh_lineage_handed_proof_rebind']
s92 = base['publication_replacement_churn_seventeenth_restart']
b92 = base['membership_witness_replacement_root11_rollover']
assert t92['deadline_vectors'] == 13244
assert t92['epoch43_complete_states'] == 7628544
assert t92['epoch43_complete_states'] // t92['deadline_vectors'] == 576
assert s92['deadline_vectors'] == 10660
assert s92['bound_seventeenth_restart_recoveries'] == 294727680
assert s92['bound_seventeenth_restart_recoveries'] // s92['deadline_vectors'] == 27648
assert b92['deadline_vectors'] == 9139
assert b92['bound_replication_quorum_churn_states'] == 6945640
assert b92['bound_replication_quorum_churn_states'] // b92['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v93', H / 'distributed_winloop_v93.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v93.json').read_text())
assert a == m.run_validation() and a['version'] == 'V93'
assert a['base'] == {
    'version': 'V92',
    'digest': '16397218b4eb268e2a3ac0dc41be627f8df093ca8285ea129ac91d44d4b6f810',
    'implementation_sha256': '5199ab84663bbbbfd90f6c6c6a59e0bc96867805f26b236d69d23a93b014c907',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch44_eighth_source_handoff_binding']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch43_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    124963445291969391417048450075378129156031119360, 61205760, 4032, 576, 77371252455336267181195264, 15180, 3
)
assert (
    t['epoch44_eighth_source_handoff_states'],
    t['epoch44_bound_eighth_source_handoff_states'],
    t['epoch44_eighth_source_binding_states'],
    t['epoch44_bound_eighth_source_binding_states'],
    t['epoch44_verifier_binding_states'],
    t['epoch44_bound_verifier_binding_states'],
    t['epoch44_complete_states'],
) == (52462080, 43718400, 34974720, 26231040, 17487360, 8743680, 8743680)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_eighteenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_seventeenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    37170324712421791808237054675927433216, 3753243648, 304128, 27648, 1208925819614629174706176, 12341, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['eighteenth_verifier_cold_restart_states'],
    s['bound_eighteenth_restart_states'],
    s['bound_eighteenth_restart_recoveries'],
) == (3412039680, 3070835712, 2729631744, 2388427776, 2047223808, 1706019840, 1364815872, 1023611904, 341203968)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root11_witness_rebind_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    90985764442073690968233540944973004800, 56711200, 5320, 760, 75557863725914323419136, 10660, 3
)
assert (
    b['root11_witness_rebind_states'],
    b['bound_root11_witness_rebind_states'],
    b['root11_witness_binding_states'],
    b['bound_root11_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (48609600, 40508000, 32406400, 24304800, 16203200, 8101600)
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
assert a['digest'] == '2c920279f12e75debfe52649e41fdd83a072b929d88ad66facecd1719b7877ff'

for line in (H / 'winloop_v93_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V93', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

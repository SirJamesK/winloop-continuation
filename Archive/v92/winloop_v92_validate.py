#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v91' / 'winloop_v91.json').read_text())
assert base['version'] == 'V91'
assert base['digest'] == '50e52b4852689a4394aa7ce81b006d72dacb67eaf8ed690972c25c6cec8c139d'
assert 'e23c1f92ab1960c00e293abd1679fc2b2db73ef98fca5900c6d3d62e0dd1d46b  distributed_winloop_v91.py' in (H.parent / 'v91' / 'winloop_v91_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V92.
t91 = base['tombstone_epoch42_seventh_source_handoff_binding']
s91 = base['publication_successor_disappearance_sixteenth_restart']
b91 = base['membership_root10_witness_rebind_quorum_churn']
assert t91['deadline_vectors'] == 11480
assert t91['epoch42_complete_states'] == 6612480
assert t91['epoch42_complete_states'] // t91['deadline_vectors'] == 576
assert s91['deadline_vectors'] == 9139
assert s91['bound_sixteenth_restart_recoveries'] == 252675072
assert s91['bound_sixteenth_restart_recoveries'] // s91['deadline_vectors'] == 27648
assert b91['deadline_vectors'] == 7770
assert b91['bound_replication_quorum_churn_states'] == 5905200
assert b91['bound_replication_quorum_churn_states'] // b91['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v92', H / 'distributed_winloop_v92.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v92.json').read_text())
assert a == m.run_validation() and a['version'] == 'V92'
assert a['base'] == {
    'version': 'V91',
    'digest': '50e52b4852689a4394aa7ce81b006d72dacb67eaf8ed690972c25c6cec8c139d',
    'implementation_sha256': 'e23c1f92ab1960c00e293abd1679fc2b2db73ef98fca5900c6d3d62e0dd1d46b',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch43_seventh_lineage_handed_proof_rebind']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch42_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    2190256038405441778912941584201600361566306304, 68656896, 5184, 576, 4835703278458516698824704, 13244, 3
)
assert (
    t['epoch43_seventh_lineage_rotation_states'],
    t['epoch43_bound_seventh_lineage_rotation_states'],
    t['epoch43_seventh_lineage_binding_states'],
    t['epoch43_bound_seventh_lineage_binding_states'],
    t['epoch43_handed_proof_rebind_states'],
    t['epoch43_bound_handed_proof_rebind_states'],
    t['epoch43_verifier_binding_states'],
    t['epoch43_bound_verifier_binding_states'],
    t['epoch43_complete_states'],
) == (61028352, 53399808, 45771264, 38142720, 30514176, 22885632, 15257088, 7628544, 7628544)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_seventeenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_sixteenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    2006703576667289424863296141142261760, 3242004480, 304128, 27648, 75557863725914323419136, 10660, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['seventeenth_verifier_cold_restart_states'],
    s['bound_seventeenth_restart_states'],
    s['bound_seventeenth_restart_recoveries'],
) == (2947276800, 2652549120, 2357821440, 2063093760, 1768366080, 1473638400, 1178910720, 884183040, 294727680)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_witness_replacement_root11_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    122577163141211820950757834865413980160, 76402040, 8360, 760, 4722366482869645213696, 9139, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root11_rollover_states'],
    b['bound_root11_rollover_states'],
    b['root11_binding_states'],
    b['bound_root11_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (69456400, 62510760, 55565120, 48619480, 41673840, 34728200, 27782560, 20836920, 13891280, 6945640)
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
assert a['digest'] == '16397218b4eb268e2a3ac0dc41be627f8df093ca8285ea129ac91d44d4b6f810'

for line in (H / 'winloop_v92_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V92', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

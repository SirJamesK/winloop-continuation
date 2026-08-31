#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v90' / 'winloop_v90.json').read_text())
assert base['version'] == 'V90'
assert base['digest'] == 'c929ba9482320badd2fc31a8592f7cbe5403666fa47a57dbb54d8a82ceaba3cb'
assert 'e5f4f9c2a1c557e9c104a77be9443a6e67a9f3fa89c327e38cf8e29a847258b4  distributed_winloop_v90.py' in (H.parent / 'v90' / 'winloop_v90_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V91.
t90 = base['tombstone_epoch41_sixth_lineage_handed_proof_rebind']
s90 = base['publication_replacement_churn_fifteenth_restart']
b90 = base['membership_witness_replacement_root10_rollover']
assert t90['deadline_vectors'] == 9880
assert t90['epoch41_complete_states'] == 5690880
assert t90['epoch41_complete_states'] // t90['deadline_vectors'] == 576
assert s90['deadline_vectors'] == 7770
assert s90['bound_fifteenth_restart_recoveries'] == 214824960
assert s90['bound_fifteenth_restart_recoveries'] // s90['deadline_vectors'] == 27648
assert b90['deadline_vectors'] == 6545
assert b90['bound_replication_quorum_churn_states'] == 4974200
assert b90['bound_replication_quorum_churn_states'] // b90['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v91', H / 'distributed_winloop_v91.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v91.json').read_text())
assert a == m.run_validation() and a['version'] == 'V91'
assert a['base'] == {
    'version': 'V90',
    'digest': 'c929ba9482320badd2fc31a8592f7cbe5403666fa47a57dbb54d8a82ceaba3cb',
    'implementation_sha256': 'e5f4f9c2a1c557e9c104a77be9443a6e67a9f3fa89c327e38cf8e29a847258b4',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch42_seventh_source_handoff_binding']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch41_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    1442026283507223833878424127415734616719360, 46287360, 4032, 576, 302231454903657293676544, 11480, 3
)
assert (
    t['epoch42_seventh_source_handoff_states'],
    t['epoch42_bound_seventh_source_handoff_states'],
    t['epoch42_seventh_source_binding_states'],
    t['epoch42_bound_seventh_source_binding_states'],
    t['epoch42_verifier_binding_states'],
    t['epoch42_bound_verifier_binding_states'],
    t['epoch42_complete_states'],
) == (39674880, 33062400, 26449920, 19837440, 13224960, 6612480, 6612480)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_sixteenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_fifteenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    107523827316852474518208627074924544, 2779425792, 304128, 27648, 4722366482869645213696, 9139, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['sixteenth_verifier_cold_restart_states'],
    s['bound_sixteenth_restart_states'],
    s['bound_sixteenth_restart_recoveries'],
) == (2526750720, 2274075648, 2021400576, 1768725504, 1516050432, 1263375360, 1010700288, 758025216, 252675072)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root10_witness_rebind_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    217680825284643493709864971429478400, 41336400, 5320, 760, 295147905179352825856, 7770, 3
)
assert (
    b['root10_witness_rebind_states'],
    b['bound_root10_witness_rebind_states'],
    b['root10_witness_binding_states'],
    b['bound_root10_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (35431200, 29526000, 23620800, 17715600, 11810400, 5905200)
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
assert a['digest'] == '50e52b4852689a4394aa7ce81b006d72dacb67eaf8ed690972c25c6cec8c139d'

for line in (H / 'winloop_v91_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V91', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

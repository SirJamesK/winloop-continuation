#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v81' / 'winloop_v81.json').read_text())
assert base['version'] == 'V81'
assert base['digest'] == '4638aaa1ca978b9c8a7e12c8b28c40d8be4f5e078371d02a98b1b7d7991bc0e3'
assert '5ff1412343c9df01766dcdc00401d7c0fa7b7186231600a5c6e3bb10cf7df465  distributed_winloop_v81.py' in (H.parent / 'v81' / 'winloop_v81_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V82.
t81 = base['tombstone_epoch32_second_failover_verifier_bound_consumption']
s81 = base['publication_rollback_source_disappearance_sixth_restart']
b81 = base['membership_witness_rotation_root6_rollover_quorum_churn']
assert t81['deadline_vectors'] == 2925
assert t81['epoch32_complete_states'] == 1684800
assert t81['epoch32_complete_states'] // t81['deadline_vectors'] == 576
assert s81['deadline_vectors'] == 2024
assert s81['bound_sixth_restart_recoveries'] == 55959552
assert s81['bound_sixth_restart_recoveries'] // s81['deadline_vectors'] == 27648
assert b81['deadline_vectors'] == 1540
assert b81['bound_replication_quorum_churn_states'] == 1170400
assert b81['bound_replication_quorum_churn_states'] // b81['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v82', H / 'distributed_winloop_v82.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v82.json').read_text())
assert a == m.run_validation() and a['version'] == 'V82'
assert a['base'] == {
    'version': 'V81',
    'digest': '4638aaa1ca978b9c8a7e12c8b28c40d8be4f5e078371d02a98b1b7d7991bc0e3',
    'implementation_sha256': '5ff1412343c9df01766dcdc00401d7c0fa7b7186231600a5c6e3bb10cf7df465',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch33_compaction_reissued_key_rotation']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch32_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    730979830249875252273217536, 13208832, 4032, 576, 1125899906842624, 3276, 3
)
assert (
    t['epoch33_tombstone_compaction_states'],
    t['epoch33_compaction_complete_states'],
    t['epoch33_verifier_bound_tombstone_compaction_states'],
    t['epoch33_bound_verifier_binding_states'],
    t['epoch33_reissued_key_rotation_states'],
    t['epoch33_bound_reissued_key_rotation_states'],
    t['epoch33_complete_states'],
) == (11321856, 9434880, 5660928, 5660928, 3773952, 1886976, 1886976)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_tombstone_compaction_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['unbound_or_conflicting_reissued_key_rotation_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_replacement_source_rollback_seventh_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_sixth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    137465136837283578642432000, 635904000, 276480, 27648, 17592186044416, 2300, 3
)
assert (
    s['replacement_source_rollback_states'],
    s['bound_replacement_source_rollback_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_dual_source_reconciliation_states'],
    s['seventh_verifier_cold_restart_states'],
    s['bound_seventh_restart_recoveries'],
) == (572313600, 508723200, 381542400, 254361600, 190771200, 63590400)
assert (
    s['cached_seventh_restart_authority_acceptances'],
    s['unbound_or_conflicting_replacement_source_rollback_acceptances'],
    s['unbound_or_conflicting_replacement_source_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_seventh_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_rotated_witness_source_replacement_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    3055079137045618769264640, 9421720, 5320, 760, 1099511627776, 1771, 3
)
assert (
    b['rotated_witness_source_replacement_states'],
    b['bound_rotated_witness_source_replacement_states'],
    b['witness_rebinding_states'],
    b['bound_witness_rebinding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (8075760, 6729800, 5383840, 4037880, 2691920, 1345960)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_source_replacement_acceptances'],
    b['unbound_or_conflicting_witness_rebinding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['witness_binding_discontinuity_acceptances'],
    b['active_byzantine_acceptances'],
    b['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert all(b['checks'])

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {
    'statements': 513,
    'max_lag': 64,
    'shared_audit': '132 + 4*k',
    'frontier_storage_only': True,
    'trust_bearing_messages_unchanged': True,
}
assert a['digest'] == '5c0b6dea19ae88dc42068c4d7b617c0a024474d9bc16e130fa6be4136747295c'

for line in (H / 'winloop_v82_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V82', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

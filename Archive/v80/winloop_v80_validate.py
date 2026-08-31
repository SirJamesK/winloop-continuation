#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v79' / 'winloop_v79.json').read_text())
assert base['version'] == 'V79'
assert base['digest'] == '968738223d2343e72f1670df27df2610806431b2022863fa0a7a320d58cfe453'
assert 'b2f8c5cad73a5947229c57a0b344bf93dcc1908fe80f8d24cb9a47dd31113984  distributed_winloop_v79.py' in (H.parent / 'v79' / 'winloop_v79_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V80.
t79 = base['tombstone_epoch30_lineage_resolution_key_retirement_reissuance']
s79 = base['publication_dual_source_reconciliation_fourth_restart']
b79 = base['membership_root_rollover_witness_reinstatement']
assert t79['deadline_vectors'] == 2300
assert t79['epoch30_complete_states'] == 1324800
assert t79['epoch30_complete_states'] // t79['deadline_vectors'] == 576
assert s79['deadline_vectors'] == 1540
assert s79['bound_fourth_restart_recoveries'] == 42577920
assert s79['bound_fourth_restart_recoveries'] // s79['deadline_vectors'] == 27648
assert b79['deadline_vectors'] == 1140
assert b79['bound_witness_reinstatement_states'] == 866400
assert b79['bound_witness_reinstatement_states'] // b79['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v80', H / 'distributed_winloop_v80.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v80.json').read_text())
assert a == m.run_validation() and a['version'] == 'V80'
assert a['base'] == {
    'version': 'V79',
    'digest': '968738223d2343e72f1670df27df2610806431b2022863fa0a7a320d58cfe453',
    'implementation_sha256': 'b2f8c5cad73a5947229c57a0b344bf93dcc1908fe80f8d24cb9a47dd31113984',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch31_reissued_key_consumption_failover_collection']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch30_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    25899228679488210468864000, 11980800, 4608, 576, 70368744177664, 2600, 3
)
assert (
    t['epoch31_bound_reissued_key_consumption_states'],
    t['epoch31_bound_source_failover_states'],
    t['epoch31_bound_old_key_tombstone_collection_states'],
    t['epoch31_complete_states'],
) == (8985600, 5990400, 2995200, 1497600)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_reissued_key_consumption_acceptances'],
    t['unbound_or_conflicting_source_failover_acceptances'],
    t['unbound_or_conflicting_old_key_tombstone_collection_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_reconciliation_rollback_fifth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_fourth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    4630856797205990555516928, 342752256, 193536, 27648, 1099511627776, 1771, 3
)
assert (
    s['bound_reconciliation_rollback_states'],
    s['bound_rollback_source_binding_states'],
    s['fifth_verifier_cold_restart_states'],
    s['bound_fifth_restart_recoveries'],
) == (244823040, 195858432, 146893824, 48964608)
assert (
    s['cached_fifth_restart_authority_acceptances'],
    s['unbound_or_conflicting_reconciliation_rollback_acceptances'],
    s['unbound_or_conflicting_rollback_source_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_fifth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_root5_split_view_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_witness_reinstatement_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    89622195534626291712000, 5054000, 3800, 760, 68719476736, 1330, 3
)
assert (
    b['bound_root5_split_view_states'],
    b['bound_root5_split_view_recovery_states'],
    b['bound_replication_quorum_churn_states'],
) == (3032400, 2021600, 1010800)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_root5_split_view_acceptances'],
    b['unbound_or_forked_root5_recovery_acceptances'],
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
assert a['digest'] == 'fd2fe31eeaa0047f7e320b03fa73305d5a546d310a886996e425079b24fae8ee'

for line in (H / 'winloop_v80_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V80', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

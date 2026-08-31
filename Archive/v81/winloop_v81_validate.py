#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v80' / 'winloop_v80.json').read_text())
assert base['version'] == 'V80'
assert base['digest'] == 'fd2fe31eeaa0047f7e320b03fa73305d5a546d310a886996e425079b24fae8ee'
assert '4a82699b7830cbb1fb63fd409736654c486611582e1f26b9e1653a7bf22fcc1a  distributed_winloop_v80.py' in (H.parent / 'v80' / 'winloop_v80_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V81.
t80 = base['tombstone_epoch31_reissued_key_consumption_failover_collection']
s80 = base['publication_reconciliation_rollback_fifth_restart']
b80 = base['membership_root5_split_view_quorum_churn']
assert t80['deadline_vectors'] == 2600
assert t80['epoch31_complete_states'] == 1497600
assert t80['epoch31_complete_states'] // t80['deadline_vectors'] == 576
assert s80['deadline_vectors'] == 1771
assert s80['bound_fifth_restart_recoveries'] == 48964608
assert s80['bound_fifth_restart_recoveries'] // s80['deadline_vectors'] == 27648
assert b80['deadline_vectors'] == 1330
assert b80['bound_replication_quorum_churn_states'] == 1010800
assert b80['bound_replication_quorum_churn_states'] // b80['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v81', H / 'distributed_winloop_v81.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v81.json').read_text())
assert a == m.run_validation() and a['version'] == 'V81'
assert a['base'] == {
    'version': 'V80',
    'digest': 'fd2fe31eeaa0047f7e320b03fa73305d5a546d310a886996e425079b24fae8ee',
    'implementation_sha256': '4a82699b7830cbb1fb63fd409736654c486611582e1f26b9e1653a7bf22fcc1a',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch32_second_failover_verifier_bound_consumption']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch31_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    116546529057696947109888000, 13478400, 4608, 576, 281474976710656, 2925, 3
)
assert (
    t['epoch32_bound_second_source_failover_states'],
    t['epoch32_bound_verifier_binding_states'],
    t['epoch32_bound_old_key_tombstone_consumption_states'],
    t['epoch32_complete_states'],
) == (10108800, 6739200, 3369600, 1684800)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_second_source_failover_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['unbound_or_conflicting_old_key_tombstone_consumption_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_rollback_source_disappearance_sixth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_fifth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    21169631072941671110934528, 391716864, 193536, 27648, 4398046511104, 2024, 3
)
assert (
    s['bound_rollback_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['sixth_verifier_cold_restart_states'],
    s['bound_sixth_restart_recoveries'],
) == (279797760, 223838208, 167878656, 55959552)
assert (
    s['cached_sixth_restart_authority_acceptances'],
    s['unbound_or_conflicting_rollback_source_disappearance_acceptances'],
    s['unbound_or_conflicting_replacement_source_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_sixth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_witness_rotation_root6_rollover_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    581129183677155744153600, 8192800, 5320, 760, 274877906944, 1540, 3
)
assert (
    b['bound_witness_rotation_states'],
    b['bound_root6_rollover_states'],
    b['bound_replication_quorum_churn_states'],
) == (5852000, 3511200, 1170400)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_witness_rotation_acceptances'],
    b['unbound_or_conflicting_root6_rollover_acceptances'],
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
assert a['digest'] == '4638aaa1ca978b9c8a7e12c8b28c40d8be4f5e078371d02a98b1b7d7991bc0e3'

for line in (H / 'winloop_v81_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V81', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

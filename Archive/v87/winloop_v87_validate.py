#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v86' / 'winloop_v86.json').read_text())
assert base['version'] == 'V86'
assert base['digest'] == '0f9655082f1caeb509cba215f43cd71dde5d42fb3bd607eade6cfa3b3cd5bea3'
assert '01c62ed700538acd35c501d93675ea4a333f44f0f1dfd1347b1d86a0f48ec4b7  distributed_winloop_v86.py' in (H.parent / 'v86' / 'winloop_v86_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V87.
t86 = base['tombstone_epoch37_fourth_lineage_root_rollover']
s86 = base['publication_successor_source_churn_eleventh_restart']
b86 = base['membership_root8_rollover_after_witness_replacement']
assert t86['deadline_vectors'] == 5456
assert t86['epoch37_complete_states'] == 3142656
assert t86['epoch37_complete_states'] // t86['deadline_vectors'] == 576
assert s86['deadline_vectors'] == 4060
assert s86['bound_eleventh_restart_recoveries'] == 112250880
assert s86['bound_eleventh_restart_recoveries'] // s86['deadline_vectors'] == 27648
assert b86['deadline_vectors'] == 3276
assert b86['bound_replication_quorum_churn_states'] == 2489760
assert b86['bound_replication_quorum_churn_states'] // b86['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v87', H / 'distributed_winloop_v87.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v87.json').read_text())
assert a == m.run_validation() and a['version'] == 'V87'
assert a['base'] == {
    'version': 'V86',
    'digest': '0f9655082f1caeb509cba215f43cd71dde5d42fb3bd607eade6cfa3b3cd5bea3',
    'implementation_sha256': '01c62ed700538acd35c501d93675ea4a333f44f0f1dfd1347b1d86a0f48ec4b7',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch38_fourth_proof_compaction_fifth_handoff']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch37_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    4400252917879727045607837457711104, 37914624, 6336, 576, 4611686018427387904, 5984, 3
)
assert (
    t['epoch38_fourth_proof_compaction_states'],
    t['epoch38_bound_fourth_proof_compaction_states'],
    t['epoch38_fourth_proof_binding_states'],
    t['epoch38_bound_fourth_proof_binding_states'],
    t['epoch38_fifth_source_handoff_states'],
    t['epoch38_bound_fifth_source_handoff_states'],
    t['epoch38_fifth_source_binding_states'],
    t['epoch38_bound_fifth_source_binding_states'],
    t['epoch38_verifier_binding_states'],
    t['epoch38_bound_verifier_binding_states'],
    t['epoch38_complete_states'],
) == (34467840, 31021056, 27574272, 24127488, 20680704, 17233920, 13787136, 10340352, 6893568, 3446784, 3446784)
assert (
    t['unbound_or_conflicting_fourth_proof_compaction_acceptances'],
    t['unbound_or_conflicting_fourth_proof_binding_acceptances'],
    t['unbound_or_conflicting_fifth_source_handoff_acceptances'],
    t['unbound_or_conflicting_fifth_source_binding_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['stale_or_conflicting_root_binding_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['unbound_or_conflicting_rotated_key_binding_acceptances'],
    t['unbound_or_conflicting_third_source_binding_acceptances'],
    t['unbound_or_conflicting_fourth_source_binding_acceptances'],
    t['unbound_or_conflicting_fourth_lineage_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_successor_disappearance_twelfth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_eleventh_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    806967051536412083835182776320, 1367055360, 304128, 27648, 72057594037927936, 4495, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twelfth_verifier_cold_restart_states'],
    s['bound_twelfth_restart_states'],
    s['bound_twelfth_restart_recoveries'],
) == (1242777600, 1118499840, 994222080, 869944320, 745666560, 621388800, 497111040, 372833280, 124277760)
assert (
    s['cached_twelfth_restart_authority_acceptances'],
    s['unbound_or_conflicting_successor_disappearance_acceptances'],
    s['unbound_or_conflicting_replacement_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_twelfth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_root8_witness_rebind_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    261413147467004666540111953920, 19439280, 5320, 760, 4503599627370496, 3654, 3
)
assert (
    b['root8_witness_rebind_states'],
    b['bound_root8_witness_rebind_states'],
    b['root8_witness_binding_states'],
    b['bound_root8_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (16662240, 13885200, 11108160, 8331120, 5554080, 2777040)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_root8_witness_rebind_acceptances'],
    b['unbound_or_conflicting_root8_witness_binding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['carried_membership_root_regression_acceptances'],
    b['target_membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['replacement_source_binding_discontinuity_acceptances'],
    b['active_byzantine_acceptances'],
    b['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
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
assert a['digest'] == '0429debf7ce2f300b49d31a608be562c0655c42ef652fb27e072a0b150f03145'

for line in (H / 'winloop_v87_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V87', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

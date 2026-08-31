#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v85' / 'winloop_v85.json').read_text())
assert base['version'] == 'V85'
assert base['digest'] == 'b6ba3ffd84e137cca1c1f84954b606cd574dafe1f9406e05a3bdecd13609c780'
assert 'b6c36b31c68d23c78471b947ac077d2c8bed3b76726999ed06c100b7d3784854  distributed_winloop_v85.py' in (H.parent / 'v85' / 'winloop_v85_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V86.
t85 = base['tombstone_epoch36_fourth_source_rollover']
s85 = base['publication_replacement_source_disappearance_tenth_restart']
b85 = base['membership_witness_source_replacement_quorum_churn']
assert t85['deadline_vectors'] == 4495
assert t85['epoch36_complete_states'] == 2589120
assert t85['epoch36_complete_states'] // t85['deadline_vectors'] == 576
assert s85['deadline_vectors'] == 3276
assert s85['bound_tenth_restart_recoveries'] == 90574848
assert s85['bound_tenth_restart_recoveries'] // s85['deadline_vectors'] == 27648
assert b85['deadline_vectors'] == 2600
assert b85['bound_replication_quorum_churn_states'] == 1976000
assert b85['bound_replication_quorum_churn_states'] // b85['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v86', H / 'distributed_winloop_v86.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v86.json').read_text())
assert a == m.run_validation() and a['version'] == 'V86'
assert a['base'] == {
    'version': 'V85',
    'digest': 'b6ba3ffd84e137cca1c1f84954b606cd574dafe1f9406e05a3bdecd13609c780',
    'implementation_sha256': 'b6c36b31c68d23c78471b947ac077d2c8bed3b76726999ed06c100b7d3784854',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch37_fourth_lineage_root_rollover']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch36_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    2005997653739287329615337664544768, 34569216, 6336, 576, 1152921504606846976, 5456, 3
)
assert (
    t['epoch37_fourth_source_lineage_rerotation_states'],
    t['epoch37_bound_fourth_source_lineage_rerotation_states'],
    t['epoch37_fourth_lineage_binding_states'],
    t['epoch37_bound_fourth_lineage_binding_states'],
    t['epoch37_root_rollover_states'],
    t['epoch37_bound_root_rollover_states'],
    t['epoch37_root_binding_states'],
    t['epoch37_bound_root_binding_states'],
    t['epoch37_verifier_binding_states'],
    t['epoch37_bound_verifier_binding_states'],
    t['epoch37_complete_states'],
) == (31426560, 28283904, 25141248, 21998592, 18855936, 15713280, 12570624, 9427968, 6285312, 3142656, 3142656)
assert (
    t['unbound_or_conflicting_fourth_source_lineage_rerotation_acceptances'],
    t['unbound_or_conflicting_fourth_lineage_binding_acceptances'],
    t['unbound_or_conflicting_root_rollover_acceptances'],
    t['unbound_or_conflicting_root_binding_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['stale_or_conflicting_root_choice_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['unbound_or_conflicting_rotated_key_binding_acceptances'],
    t['unbound_or_conflicting_third_source_binding_acceptances'],
    t['unbound_or_conflicting_fourth_source_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_successor_source_churn_eleventh_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_tenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    248479590649041843996170649600, 1122508800, 276480, 27648, 18014398509481984, 4060, 3
)
assert (
    s['successor_source_churn_states'],
    s['bound_successor_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_dual_source_reconciliation_states'],
    s['eleventh_verifier_cold_restart_states'],
    s['bound_eleventh_restart_recoveries'],
) == (1010257920, 898007040, 673505280, 449003520, 336752640, 112250880)
assert (
    s['cached_eleventh_restart_authority_acceptances'],
    s['unbound_or_conflicting_successor_churn_acceptances'],
    s['unbound_or_conflicting_successor_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_eleventh_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_root8_rollover_after_witness_replacement']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    260411564526518058622333747200, 17428320, 5320, 760, 1125899906842624, 3276, 3
)
assert (
    b['root8_rollover_states'],
    b['bound_root8_rollover_states'],
    b['root8_binding_states'],
    b['bound_root8_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (14938560, 12448800, 9959040, 7469280, 4979520, 2489760)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_root8_rollover_acceptances'],
    b['unbound_or_conflicting_root8_binding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['carried_membership_root_regression_acceptances'],
    b['target_membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['witness_binding_discontinuity_acceptances'],
    b['replacement_source_binding_discontinuity_acceptances'],
    b['active_byzantine_acceptances'],
    b['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
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
assert a['digest'] == '0f9655082f1caeb509cba215f43cd71dde5d42fb3bd607eade6cfa3b3cd5bea3'

for line in (H / 'winloop_v86_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V86', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

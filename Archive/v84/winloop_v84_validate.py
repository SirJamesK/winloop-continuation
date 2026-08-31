#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v83' / 'winloop_v83.json').read_text())
assert base['version'] == 'V83'
assert base['digest'] == '1d9cdbace8c3555694366a4a83ead54364c7629c31838b15fb70ccfd80045940'
assert '4b49130c86df34373ab445adfd8575947d3c1360fae7b1b0d339f2ff8b08fcea  distributed_winloop_v83.py' in (H.parent / 'v83' / 'winloop_v83_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V84.
t83 = base['tombstone_epoch34_revalidation_third_failover']
s83 = base['publication_replacement_source_disappearance_eighth_restart']
b83 = base['membership_rotated_witness_root7_rollover_quorum_churn']
assert t83['deadline_vectors'] == 3654
assert t83['epoch34_complete_states'] == 2104704
assert t83['epoch34_complete_states'] // t83['deadline_vectors'] == 576
assert s83['deadline_vectors'] == 2600
assert s83['bound_eighth_restart_recoveries'] == 71884800
assert s83['bound_eighth_restart_recoveries'] // s83['deadline_vectors'] == 27648
assert b83['deadline_vectors'] == 2024
assert b83['bound_replication_quorum_churn_states'] == 1538240
assert b83['bound_replication_quorum_churn_states'] // b83['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v84', H / 'distributed_winloop_v84.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v84.json').read_text())
assert a == m.run_validation() and a['version'] == 'V84'
assert a['base'] == {
    'version': 'V83',
    'digest': '1d9cdbace8c3555694366a4a83ead54364c7629c31838b15fb70ccfd80045940',
    'implementation_sha256': '4b49130c86df34373ab445adfd8575947d3c1360fae7b1b0d339f2ff8b08fcea',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch35_root_bound_revalidation']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch34_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    198783672519233475196936519680, 14031360, 3456, 576, 18014398509481984, 4060, 3
)
assert (
    t['epoch35_compacted_tombstone_proof_revalidation_states'],
    t['epoch35_bound_proof_revalidation_states'],
    t['epoch35_proof_root_binding_states'],
    t['epoch35_bound_proof_root_binding_states'],
    t['epoch35_verifier_binding_states'],
    t['epoch35_bound_verifier_binding_states'],
    t['epoch35_complete_states'],
) == (11692800, 9354240, 9354240, 7015680, 4677120, 2338560, 2338560)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_proof_revalidation_acceptances'],
    t['unbound_or_conflicting_proof_root_binding_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['unbound_or_conflicting_rotated_key_binding_acceptances'],
    t['unbound_or_conflicting_third_source_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_successor_source_churn_ninth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_eighth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    2797116697384726730637312000, 808704000, 276480, 27648, 281474976710656, 2925, 3
)
assert (
    s['successor_source_churn_states'],
    s['bound_successor_source_churn_states'],
    s['bound_successor_replacement_binding_states'],
    s['bound_dual_source_reconciliation_states'],
    s['ninth_verifier_cold_restart_states'],
    s['bound_ninth_restart_recoveries'],
) == (727833600, 646963200, 485222400, 323481600, 242611200, 80870400)
assert (
    s['cached_ninth_restart_authority_acceptances'],
    s['unbound_or_conflicting_successor_churn_acceptances'],
    s['unbound_or_conflicting_successor_replacement_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_ninth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_rotated_witness_rebinding_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    51012453123210703011840000, 8740000, 3800, 760, 17592186044416, 2300, 3
)
assert (
    b['rotated_witness_rebinding_states'],
    b['bound_rotated_witness_rebinding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (6992000, 5244000, 3496000, 1748000)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_witness_rebinding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['witness_binding_discontinuity_acceptances'],
    b['source_binding_discontinuity_acceptances'],
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
assert a['digest'] == '1b4a5b0744ca8a8f54e74f31b81c1e3b573298c1847ee82b697a933e1a5aefc2'

for line in (H / 'winloop_v84_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V84', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

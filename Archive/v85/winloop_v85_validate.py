#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v84' / 'winloop_v84.json').read_text())
assert base['version'] == 'V84'
assert base['digest'] == '1b4a5b0744ca8a8f54e74f31b81c1e3b573298c1847ee82b697a933e1a5aefc2'
assert '2316ee1c7d765f4262aa0d9c1beb744d390380603072e098005a9971615179fc  distributed_winloop_v84.py' in (H.parent / 'v84' / 'winloop_v84_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V85.
t84 = base['tombstone_epoch35_root_bound_revalidation']
s84 = base['publication_successor_source_churn_ninth_restart']
b84 = base['membership_rotated_witness_rebinding_quorum_churn']
assert t84['deadline_vectors'] == 4060
assert t84['epoch35_complete_states'] == 2338560
assert t84['epoch35_complete_states'] // t84['deadline_vectors'] == 576
assert s84['deadline_vectors'] == 2925
assert s84['bound_ninth_restart_recoveries'] == 80870400
assert s84['bound_ninth_restart_recoveries'] // s84['deadline_vectors'] == 27648
assert b84['deadline_vectors'] == 2300
assert b84['bound_replication_quorum_churn_states'] == 1748000
assert b84['bound_replication_quorum_churn_states'] // b84['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v85', H / 'distributed_winloop_v85.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v85.json').read_text())
assert a == m.run_validation() and a['version'] == 'V85'
assert a['base'] == {
    'version': 'V84',
    'digest': '1b4a5b0744ca8a8f54e74f31b81c1e3b573298c1847ee82b697a933e1a5aefc2',
    'implementation_sha256': '2316ee1c7d765f4262aa0d9c1beb744d390380603072e098005a9971615179fc',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch36_fourth_source_rollover']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch35_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    25822945649165186682725848842240, 28480320, 6336, 576, 72057594037927936, 4495, 3
)
assert (
    t['epoch36_compacted_tombstone_proof_revalidation_states'],
    t['epoch36_bound_proof_revalidation_states'],
    t['epoch36_proof_root_binding_states'],
    t['epoch36_bound_proof_root_binding_states'],
    t['epoch36_fourth_source_rollover_states'],
    t['epoch36_bound_fourth_source_rollover_states'],
    t['epoch36_fourth_source_binding_states'],
    t['epoch36_bound_fourth_source_binding_states'],
    t['epoch36_verifier_binding_states'],
    t['epoch36_bound_verifier_binding_states'],
    t['epoch36_complete_states'],
) == (25891200, 23302080, 20712960, 18123840, 15534720, 12945600, 10356480, 7767360, 5178240, 2589120, 2589120)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_proof_revalidation_acceptances'],
    t['unbound_or_conflicting_proof_root_binding_acceptances'],
    t['unbound_or_conflicting_fourth_source_rollover_acceptances'],
    t['unbound_or_conflicting_fourth_source_binding_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['unbound_or_conflicting_rotated_key_binding_acceptances'],
    t['unbound_or_conflicting_third_source_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_replacement_source_disappearance_tenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_ninth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    12531082804283575753255157760, 905748480, 276480, 27648, 1125899906842624, 3276, 3
)
assert (
    s['replacement_source_disappearance_states'],
    s['bound_replacement_source_disappearance_states'],
    s['bound_replacement_successor_binding_states'],
    s['bound_dual_source_reconciliation_states'],
    s['tenth_verifier_cold_restart_states'],
    s['bound_tenth_restart_recoveries'],
) == (815173632, 724598784, 543449088, 362299392, 271724544, 90574848)
assert (
    s['cached_tenth_restart_authority_acceptances'],
    s['unbound_or_conflicting_replacement_disappearance_acceptances'],
    s['unbound_or_conflicting_replacement_successor_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_tenth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_witness_source_replacement_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    1291724030389474497134592000, 13832000, 5320, 760, 70368744177664, 2600, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['bound_replacement_source_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (11856000, 9880000, 5928000, 3952000, 1976000)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_witness_source_replacement_acceptances'],
    b['unbound_or_conflicting_replacement_source_binding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['witness_binding_discontinuity_acceptances'],
    b['prior_source_binding_discontinuity_acceptances'],
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
assert a['digest'] == 'b6ba3ffd84e137cca1c1f84954b606cd574dafe1f9406e05a3bdecd13609c780'

for line in (H / 'winloop_v85_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V85', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

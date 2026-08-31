#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v82' / 'winloop_v82.json').read_text())
assert base['version'] == 'V82'
assert base['digest'] == '5c0b6dea19ae88dc42068c4d7b617c0a024474d9bc16e130fa6be4136747295c'
assert 'bd218e25cfe0dbcdd6d980b26ebb0273c360431030a60fa33a3e63e7d2edb79e  distributed_winloop_v82.py' in (H.parent / 'v82' / 'winloop_v82_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V83.
t82 = base['tombstone_epoch33_compaction_reissued_key_rotation']
s82 = base['publication_replacement_source_rollback_seventh_restart']
b82 = base['membership_rotated_witness_source_replacement_quorum_churn']
assert t82['deadline_vectors'] == 3276
assert t82['epoch33_complete_states'] == 1886976
assert t82['epoch33_complete_states'] // t82['deadline_vectors'] == 576
assert s82['deadline_vectors'] == 2300
assert s82['bound_seventh_restart_recoveries'] == 63590400
assert s82['bound_seventh_restart_recoveries'] // s82['deadline_vectors'] == 27648
assert b82['deadline_vectors'] == 1771
assert b82['bound_replication_quorum_churn_states'] == 1345960
assert b82['bound_replication_quorum_churn_states'] // b82['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v83', H / 'distributed_winloop_v83.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v83.json').read_text())
assert a == m.run_validation() and a['version'] == 'V83'
assert a['base'] == {
    'version': 'V82',
    'digest': '5c0b6dea19ae88dc42068c4d7b617c0a024474d9bc16e130fa6be4136747295c',
    'implementation_sha256': 'bd218e25cfe0dbcdd6d980b26ebb0273c360431030a60fa33a3e63e7d2edb79e',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch34_revalidation_third_failover']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch33_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    13045178509074696809798959104, 14732928, 4032, 576, 4503599627370496, 3654, 3
)
assert (
    t['epoch34_compacted_tombstone_proof_revalidation_states'],
    t['epoch34_bound_proof_revalidation_states'],
    t['epoch34_third_source_failover_states'],
    t['epoch34_bound_third_source_failover_states'],
    t['epoch34_verifier_binding_states'],
    t['epoch34_bound_verifier_binding_states'],
    t['epoch34_complete_states'],
) == (12628224, 10523520, 8418816, 6314112, 4209408, 2104704, 2104704)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_proof_revalidation_acceptances'],
    t['unbound_or_conflicting_third_source_failover_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['unbound_or_conflicting_rotated_key_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_replacement_source_disappearance_eighth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_seventh_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    621581488307717051252736000, 718848000, 276480, 27648, 70368744177664, 2600, 3
)
assert (
    s['replacement_source_disappearance_states'],
    s['bound_replacement_source_disappearance_states'],
    s['bound_successor_source_binding_states'],
    s['bound_dual_source_reconciliation_states'],
    s['eighth_verifier_cold_restart_states'],
    s['bound_eighth_restart_recoveries'],
) == (646963200, 575078400, 431308800, 287539200, 215654400, 71884800)
assert (
    s['cached_eighth_restart_authority_acceptances'],
    s['unbound_or_conflicting_source_disappearance_acceptances'],
    s['unbound_or_conflicting_successor_source_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_eighth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_rotated_witness_root7_rollover_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    62847342247795586110586880, 10767680, 5320, 760, 4398046511104, 2024, 3
)
assert (
    b['root7_rollover_states'],
    b['bound_root7_rollover_states'],
    b['bound_root7_verifier_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (9229440, 7691200, 4614720, 3076480, 1538240)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_root_rollover_acceptances'],
    b['unbound_or_conflicting_root_binding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['witness_binding_discontinuity_acceptances'],
    b['source_binding_discontinuity_acceptances'],
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
assert a['digest'] == '1d9cdbace8c3555694366a4a83ead54364c7629c31838b15fb70ccfd80045940'

for line in (H / 'winloop_v83_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V83', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

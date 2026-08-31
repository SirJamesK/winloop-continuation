#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v89' / 'winloop_v89.json').read_text())
assert base['version'] == 'V89'
assert base['digest'] == 'd82f57a7c7d52e38f1cadf55c3e388be974c420b1215dedb2f07e1b7d95caaf8'
assert '95270f32c07e1c5538cb8aaf6cef9f5a378c20cc71a4bcec05f4a5e415308b94  distributed_winloop_v89.py' in (H.parent / 'v89' / 'winloop_v89_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V90.
t89 = base['tombstone_epoch40_sixth_source_handoff_binding']
s89 = base['publication_successor_disappearance_fourteenth_restart']
b89 = base['membership_root9_witness_rebind_quorum_churn']
assert t89['deadline_vectors'] == 8436
assert t89['epoch40_complete_states'] == 4859136
assert t89['epoch40_complete_states'] // t89['deadline_vectors'] == 576
assert s89['deadline_vectors'] == 6545
assert s89['bound_fourteenth_restart_recoveries'] == 180956160
assert s89['bound_fourteenth_restart_recoveries'] // s89['deadline_vectors'] == 27648
assert b89['deadline_vectors'] == 5456
assert b89['bound_replication_quorum_churn_states'] == 4146560
assert b89['bound_replication_quorum_churn_states'] // b89['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v90', H / 'distributed_winloop_v90.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v90.json').read_text())
assert a == m.run_validation() and a['version'] == 'V90'
assert a['base'] == {
    'version': 'V89',
    'digest': 'd82f57a7c7d52e38f1cadf55c3e388be974c420b1215dedb2f07e1b7d95caaf8',
    'implementation_sha256': '95270f32c07e1c5538cb8aaf6cef9f5a378c20cc71a4bcec05f4a5e415308b94',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch41_sixth_lineage_handed_proof_rebind']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch40_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    24931747979689511127362313614089550561280, 51217920, 5184, 576, 18889465931478580854784, 9880, 3
)
assert (
    t['epoch41_sixth_lineage_rotation_states'],
    t['epoch41_bound_sixth_lineage_rotation_states'],
    t['epoch41_sixth_lineage_binding_states'],
    t['epoch41_bound_sixth_lineage_binding_states'],
    t['epoch41_handed_proof_rebind_states'],
    t['epoch41_bound_handed_proof_rebind_states'],
    t['epoch41_verifier_binding_states'],
    t['epoch41_bound_verifier_binding_states'],
    t['epoch41_complete_states'],
) == (45527040, 39836160, 34145280, 28454400, 22763520, 17072640, 11381760, 5690880, 5690880)
assert (
    t['unbound_or_conflicting_sixth_lineage_rotation_acceptances'],
    t['unbound_or_conflicting_sixth_lineage_binding_acceptances'],
    t['unbound_or_conflicting_handed_proof_rebind_acceptances'],
    t['unbound_or_conflicting_verifier_binding_acceptances'],
    t['stale_or_conflicting_root_binding_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_source_binding_acceptances'],
    t['unbound_or_conflicting_rotated_key_binding_acceptances'],
    t['unbound_or_conflicting_third_source_binding_acceptances'],
    t['unbound_or_conflicting_fourth_source_binding_acceptances'],
    t['unbound_or_conflicting_fourth_lineage_binding_acceptances'],
    t['unbound_or_conflicting_fourth_proof_binding_acceptances'],
    t['unbound_or_conflicting_fifth_source_binding_acceptances'],
    t['unbound_or_conflicting_fifth_lineage_binding_acceptances'],
    t['unbound_or_conflicting_fifth_proof_binding_acceptances'],
    t['unbound_or_conflicting_sixth_source_binding_acceptances'],
    t['unbound_or_conflicting_sixth_handoff_binding_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_replacement_churn_fifteenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_fourteenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    5713563698516958413163919960965120, 2363074560, 304128, 27648, 295147905179352825856, 7770, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['fifteenth_verifier_cold_restart_states'],
    s['bound_fifteenth_restart_states'],
    s['bound_fifteenth_restart_recoveries'],
) == (2148249600, 1933424640, 1718599680, 1503774720, 1288949760, 1074124800, 859299840, 644474880, 214824960)
assert (
    s['cached_fifteenth_restart_authority_acceptances'],
    s['unbound_or_conflicting_replacement_churn_acceptances'],
    s['unbound_or_conflicting_successor_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_fifteenth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_witness_replacement_root10_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    288139934112298369730496940946227200, 54716200, 8360, 760, 18446744073709551616, 6545, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root10_rollover_states'],
    b['bound_root10_rollover_states'],
    b['root10_binding_states'],
    b['bound_root10_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (49742000, 44767800, 39793600, 34819400, 29845200, 24871000, 19896800, 14922600, 9948400, 4974200)
assert (
    b['unbound_or_conflicting_witness_source_replacement_acceptances'],
    b['unbound_or_conflicting_replacement_source_binding_acceptances'],
    b['unbound_or_conflicting_root10_rollover_acceptances'],
    b['unbound_or_conflicting_root10_binding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['carried_membership_root_regression_acceptances'],
    b['target_membership_root_regression_acceptances'],
    b['below_replication_quorum_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['witness_binding_discontinuity_acceptances'],
    b['prior_source_binding_discontinuity_acceptances'],
    b['active_byzantine_acceptances'],
    b['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
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
assert a['digest'] == 'c929ba9482320badd2fc31a8592f7cbe5403666fa47a57dbb54d8a82ceaba3cb'

for line in (H / 'winloop_v90_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V90', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

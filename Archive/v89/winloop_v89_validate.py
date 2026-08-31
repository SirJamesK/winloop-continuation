#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v88' / 'winloop_v88.json').read_text())
assert base['version'] == 'V88'
assert base['digest'] == 'd9b8aea9217028786eaaa788dfb55cba937d47e634833013e6b941f4bace6076'
assert '7873fd99956adaafae3fef663ba446ad05f539f57f315ec25a02504bc90f61dc  distributed_winloop_v88.py' in (H.parent / 'v88' / 'winloop_v88_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V89.
t88 = base['tombstone_epoch39_fifth_lineage_compacted_proof_rebind']
s88 = base['publication_replacement_churn_thirteenth_restart']
b88 = base['membership_rebound_witness_replacement_root9_rollover']
assert t88['deadline_vectors'] == 7140
assert t88['epoch39_complete_states'] == 4112640
assert t88['epoch39_complete_states'] // t88['deadline_vectors'] == 576
assert s88['deadline_vectors'] == 5456
assert s88['bound_thirteenth_restart_recoveries'] == 150847488
assert s88['bound_thirteenth_restart_recoveries'] // s88['deadline_vectors'] == 27648
assert b88['deadline_vectors'] == 4495
assert b88['bound_replication_quorum_churn_states'] == 3416200
assert b88['bound_replication_quorum_churn_states'] // b88['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v89', H / 'distributed_winloop_v89.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v89.json').read_text())
assert a == m.run_validation() and a['version'] == 'V89'
assert a['base'] == {
    'version': 'V88',
    'digest': 'd9b8aea9217028786eaaa788dfb55cba937d47e634833013e6b941f4bace6076',
    'implementation_sha256': '7873fd99956adaafae3fef663ba446ad05f539f57f315ec25a02504bc90f61dc',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch40_sixth_source_handoff_binding']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch39_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    16169177500850318965311596619714527232, 34013952, 4032, 576, 1180591620717411303424, 8436, 3
)
assert (
    t['epoch40_sixth_source_handoff_states'],
    t['epoch40_bound_sixth_source_handoff_states'],
    t['epoch40_sixth_source_binding_states'],
    t['epoch40_bound_sixth_source_binding_states'],
    t['epoch40_verifier_binding_states'],
    t['epoch40_bound_verifier_binding_states'],
    t['epoch40_complete_states'],
) == (29154816, 24295680, 19436544, 14577408, 9718272, 4859136, 4859136)
assert (
    t['unbound_or_conflicting_sixth_source_handoff_acceptances'],
    t['unbound_or_conflicting_sixth_source_binding_acceptances'],
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
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_successor_disappearance_fourteenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirteenth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    300798539308184466008348263710720, 1990517760, 304128, 27648, 18446744073709551616, 6545, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['fourteenth_verifier_cold_restart_states'],
    s['bound_fourteenth_restart_states'],
    s['bound_fourteenth_restart_recoveries'],
) == (1809561600, 1628605440, 1447649280, 1266693120, 1085736960, 904780800, 723824640, 542868480, 180956160)
assert (
    s['cached_fourteenth_restart_authority_acceptances'],
    s['unbound_or_conflicting_successor_disappearance_acceptances'],
    s['unbound_or_conflicting_replacement_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_fourteenth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_root9_witness_rebind_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    493455714272840492644042801152000, 29025920, 5320, 760, 1152921504606846976, 5456, 3
)
assert (
    b['root9_witness_rebind_states'],
    b['bound_root9_witness_rebind_states'],
    b['root9_witness_binding_states'],
    b['bound_root9_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (24879360, 20732800, 16586240, 12439680, 8293120, 4146560)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_root9_witness_rebind_acceptances'],
    b['unbound_or_conflicting_root9_witness_binding_acceptances'],
    b['unbound_or_conflicting_replication_quorum_churn_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['carried_membership_root_regression_acceptances'],
    b['target_membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['replacement_source_binding_discontinuity_acceptances'],
    b['prior_source_binding_discontinuity_acceptances'],
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
assert a['digest'] == 'd82f57a7c7d52e38f1cadf55c3e388be974c420b1215dedb2f07e1b7d95caaf8'

for line in (H / 'winloop_v89_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V89', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

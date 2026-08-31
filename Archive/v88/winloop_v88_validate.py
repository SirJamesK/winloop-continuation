#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v87' / 'winloop_v87.json').read_text())
assert base['version'] == 'V87'
assert base['digest'] == '0429debf7ce2f300b49d31a608be562c0655c42ef652fb27e072a0b150f03145'
assert '8e6d7b5d8c170d4f5a8933f7151cda153ff4392597c7e0a16fc0265c05e4c660  distributed_winloop_v87.py' in (H.parent / 'v87' / 'winloop_v87_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V88.
t87 = base['tombstone_epoch38_fourth_proof_compaction_fifth_handoff']
s87 = base['publication_successor_disappearance_twelfth_restart']
b87 = base['membership_root8_witness_rebind_quorum_churn']
assert t87['deadline_vectors'] == 5984
assert t87['epoch38_complete_states'] == 3446784
assert t87['epoch38_complete_states'] // t87['deadline_vectors'] == 576
assert s87['deadline_vectors'] == 4495
assert s87['bound_twelfth_restart_recoveries'] == 124277760
assert s87['bound_twelfth_restart_recoveries'] // s87['deadline_vectors'] == 27648
assert b87['deadline_vectors'] == 3654
assert b87['bound_replication_quorum_churn_states'] == 2777040
assert b87['bound_replication_quorum_churn_states'] // b87['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v88', H / 'distributed_winloop_v88.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v88.json').read_text())
assert a == m.run_validation() and a['version'] == 'V88'
assert a['base'] == {
    'version': 'V87',
    'digest': '0429debf7ce2f300b49d31a608be562c0655c42ef652fb27e072a0b150f03145',
    'implementation_sha256': '8e6d7b5d8c170d4f5a8933f7151cda153ff4392597c7e0a16fc0265c05e4c660',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch39_fifth_lineage_compacted_proof_rebind']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch38_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    274924893050997822023101249423933440, 37013760, 5184, 576, 73786976294838206464, 7140, 3
)
assert (
    t['epoch39_fifth_lineage_rotation_states'],
    t['epoch39_bound_fifth_lineage_rotation_states'],
    t['epoch39_fifth_lineage_binding_states'],
    t['epoch39_bound_fifth_lineage_binding_states'],
    t['epoch39_compacted_proof_rebind_states'],
    t['epoch39_bound_compacted_proof_rebind_states'],
    t['epoch39_verifier_binding_states'],
    t['epoch39_bound_verifier_binding_states'],
    t['epoch39_complete_states'],
) == (32901120, 28788480, 24675840, 20563200, 16450560, 12337920, 8225280, 4112640, 4112640)
assert (
    t['unbound_or_conflicting_fifth_lineage_rotation_acceptances'],
    t['unbound_or_conflicting_fifth_lineage_binding_acceptances'],
    t['unbound_or_conflicting_compacted_proof_rebind_acceptances'],
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
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_replacement_churn_thirteenth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twelfth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    15671856669838182262619825504256, 1659322368, 304128, 27648, 1152921504606846976, 5456, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['thirteenth_verifier_cold_restart_states'],
    s['bound_thirteenth_restart_states'],
    s['bound_thirteenth_restart_recoveries'],
) == (1508474880, 1357627392, 1206779904, 1055932416, 905084928, 754237440, 603389952, 452542464, 150847488)
assert (
    s['cached_thirteenth_restart_authority_acceptances'],
    s['unbound_or_conflicting_replacement_churn_acceptances'],
    s['unbound_or_conflicting_successor_binding_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_thirteenth_restart_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_rebound_witness_replacement_root9_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    638848915799659566369519697920000, 37578200, 8360, 760, 72057594037927936, 4495, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root9_rollover_states'],
    b['bound_root9_rollover_states'],
    b['root9_binding_states'],
    b['bound_root9_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (34162000, 30745800, 27329600, 23913400, 20497200, 17081000, 13664800, 10248600, 6832400, 3416200)
assert (
    b['unbound_or_conflicting_witness_source_replacement_acceptances'],
    b['unbound_or_conflicting_replacement_source_binding_acceptances'],
    b['unbound_or_conflicting_root9_rollover_acceptances'],
    b['unbound_or_conflicting_root9_binding_acceptances'],
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
assert a['digest'] == 'd9b8aea9217028786eaaa788dfb55cba937d47e634833013e6b941f4bace6076'

for line in (H / 'winloop_v88_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V88', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

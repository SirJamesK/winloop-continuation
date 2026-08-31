#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v78' / 'winloop_v78.json').read_text())
assert base['version'] == 'V78'
assert base['digest'] == '0ff7fc1b7ff5988de8d6962246d37d9d72ead144122b2045981062960455433b'
assert 'ad7bb7826a9ecac618836aa54a7c9e493f819ea9f11fb87f380dbcddadda54ea  distributed_winloop_v78.py' in (H.parent / 'v78' / 'winloop_v78_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V79.
t78 = base['tombstone_epoch29_rollback_revalidation_lineage_split']
s78 = base['publication_third_restart_bounded_source_reappearance']
b78 = base['membership_third_generation_witness_eviction_replication_loss']
assert t78['deadline_vectors'] == 2024
assert t78['epoch29_bound_source_lineage_split_states'] == 1165824
assert t78['epoch29_bound_source_lineage_split_states'] // t78['deadline_vectors'] == 576
assert s78['deadline_vectors'] == 1330
assert s78['bound_third_restart_recoveries'] == 36771840
assert s78['bound_third_restart_recoveries'] // s78['deadline_vectors'] == 27648
assert b78['deadline_vectors'] == 969
assert b78['bound_replication_recovery_states'] == 736440
assert b78['bound_replication_recovery_states'] // b78['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v79', H / 'distributed_winloop_v79.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v79.json').read_text())
assert a == m.run_validation() and a['version'] == 'V79'
assert a['base'] == {
    'version': 'V78',
    'digest': '0ff7fc1b7ff5988de8d6962246d37d9d72ead144122b2045981062960455433b',
    'implementation_sha256': 'ad7bb7826a9ecac618836aa54a7c9e493f819ea9f11fb87f380dbcddadda54ea',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch30_lineage_resolution_key_retirement_reissuance']
assert (t['patterns'], t['accepted'], t['base_states'], t['source_lineage_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    6873256841864178932121600, 10598400, 4608, 576, 17592186044416, 2300, 3
)
assert (
    t['epoch30_lineage_split_resolution_states'],
    t['epoch30_bound_replacement_key_retirement_states'],
    t['epoch30_bound_replacement_key_reissuance_states'],
    t['epoch30_complete_states'],
) == (7948800, 5299200, 2649600, 1324800)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_or_conflicting_split_resolution_acceptances'],
    t['unbound_or_conflicting_key_retirement_acceptances'],
    t['unbound_or_conflicting_key_reissuance_acceptances'],
    t['unbound_or_conflicting_reissued_lineage_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_dual_source_reconciliation_fourth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_third_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    1006707999392606642503680, 298045440, 193536, 27648, 274877906944, 1540, 3
)
assert (
    s['bound_dual_source_reconciliation_states'],
    s['fourth_verifier_cold_restart_states'],
    s['bound_fourth_restart_recoveries'],
) == (170311680, 127733760, 42577920)
assert (
    s['cached_fourth_restart_authority_acceptances'],
    s['unbound_or_forked_dual_source_reconciliation_acceptances'],
    s['unbound_or_conflicting_dual_source_binding_acceptances'],
    s['unbound_or_forked_reconciliation_consumption_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_root_rollover_witness_reinstatement']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_replication_recovery_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    1200297261624459264000, 4332000, 3800, 760, 17179869184, 1140, 3
)
assert (
    b['bound_membership_root_rollover_states'],
    b['bound_witness_reinstatement_states'],
) == (2599200, 866400)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_membership_root_rollover_acceptances'],
    b['unbound_or_forked_witness_reinstatement_acceptances'],
    b['membership_generation_regression_acceptances'],
    b['membership_root_regression_acceptances'],
    b['tombstone_binding_discontinuity_acceptances'],
    b['active_byzantine_acceptances'],
    b['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0)
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
assert a['digest'] == '968738223d2343e72f1670df27df2610806431b2022863fa0a7a320d58cfe453'

for line in (H / 'winloop_v79_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V79', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

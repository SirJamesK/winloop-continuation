#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v77' / 'winloop_v77.json').read_text())
assert base['version'] == 'V77'
assert base['digest'] == '9ae29120c3eb08eebe92725585fb1e912d90271b59c62f155e9544995d914bb1'
assert 'bfbc14223d292bb76e862c9f5bd6bd4a57e7f7cafbc1fcd10aff5d4d7cce7029  distributed_winloop_v77.py' in (H.parent / 'v77' / 'winloop_v77_SHA256SUMS.txt').read_text()

sp = importlib.util.spec_from_file_location('v78', H / 'distributed_winloop_v78.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v78.json').read_text())
assert a == m.run_validation() and a['version'] == 'V78'
assert a['base'] == {
    'version': 'V77',
    'digest': '9ae29120c3eb08eebe92725585fb1e912d90271b59c62f155e9544995d914bb1',
    'implementation_sha256': 'bfbc14223d292bb76e862c9f5bd6bd4a57e7f7cafbc1fcd10aff5d4d7cce7029',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch29_rollback_revalidation_lineage_split']
assert (t['patterns'], t['accepted'], t['base_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (255720580668759003572958147442114560, 127176016, 62834, 4398046511104, 2024, 3)
assert (t['epoch29_tombstone_root_rollback_states'], t['epoch29_bound_tombstone_root_revalidation_states'], t['epoch29_bound_source_lineage_split_states']) == (2914560, 2331648, 1165824)
assert (
    t['stale_or_conflicting_root_choice_acceptances'],
    t['unbound_source_replacement_acceptances'],
    t['unbound_rerotation_acceptances'],
    t['unbound_key_recovery_acceptances'],
    t['unbound_or_conflicting_lineage_rollover_acceptances'],
    t['unbound_or_conflicting_lineage_rebind_acceptances'],
    t['tombstone_root_discontinuity_acceptances'],
    t['unbound_or_conflicting_tombstone_root_rollback_acceptances'],
    t['unbound_or_conflicting_tombstone_root_revalidation_acceptances'],
    t['unbound_or_conflicting_source_lineage_split_acceptances'],
    t['deadline_reset_acceptances'],
    t['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_third_restart_bounded_source_reappearance']
assert (s['patterns'], s['accepted'], s['base_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (3143919665310920500838400000000000, 119567000, 89900, 68719476736, 1330, 3)
assert (s['third_verifier_restart_states'], s['bounded_source_reappearance_states'], s['bound_third_restart_recoveries']) == (55157760, 36771840, 36771840)
assert (
    s['cached_third_restart_authority_acceptances'],
    s['unbound_or_forked_bounded_source_reappearance_acceptances'],
    s['unbound_or_conflicting_third_restart_binding_acceptances'],
    s['unbound_or_forked_cache_generation_recovery_acceptances'],
    s['below_publication_quorum_acceptances'],
    s['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_third_generation_witness_eviction_replication_loss']
assert (b['patterns'], b['accepted'], b['base_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (221176354159617638400000000000, 13682280, 14120, 4294967296, 969, 3)
assert (b['third_generation_witness_eviction_states'], b['temporary_replication_loss_states'], b['bound_replication_recovery_states']) == (736440, 1104660, 736440)
assert (
    b['below_replication_quorum_acceptances'],
    b['unbound_or_conflicting_rollback_acceptances'],
    b['unbound_or_forked_first_witness_churn_acceptances'],
    b['unbound_or_forked_second_witness_churn_acceptances'],
    b['unbound_or_conflicting_membership_compaction_acceptances'],
    b['unbound_or_forked_third_identity_reuse_acceptances'],
    b['unbound_or_conflicting_third_witness_eviction_acceptances'],
    b['unbound_or_conflicting_temporary_replication_loss_acceptances'],
    b['unbound_or_forked_replication_recovery_acceptances'],
    b['tombstone_generation_collapse_acceptances'],
    b['third_generation_collapse_acceptances'],
    b['unbound_membership_root_acceptances'],
    b['active_byzantine_acceptances'],
    b['bad_acceptances'],
) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert all(b['checks'])

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}

for line in (H / 'winloop_v78_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V78', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

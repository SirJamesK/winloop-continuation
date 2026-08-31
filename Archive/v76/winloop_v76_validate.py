#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v75' / 'winloop_v75.json').read_text())
assert base['version'] == 'V75'
assert base['digest'] == 'c7ad77c116f37569cd415b6c92c24f9332df44d8c05af0909a79275ffff329e2'
assert 'c225ba7efd03051cafbd91cecfe2dfed87a2e48d7d61c5730ede3f68d33ac055  distributed_winloop_v75.py' in (H.parent / 'v75' / 'winloop_v75_SHA256SUMS.txt').read_text()

sp = importlib.util.spec_from_file_location('v76', H / 'distributed_winloop_v76.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v76.json').read_text())
assert a == m.run_validation() and a['version'] == 'V76'
assert a['base'] == {
    'version': 'V75',
    'digest': 'c7ad77c116f37569cd415b6c92c24f9332df44d8c05af0909a79275ffff329e2',
    'implementation_sha256': 'c225ba7efd03051cafbd91cecfe2dfed87a2e48d7d61c5730ede3f68d33ac055',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch27_key_recovery_lineage_rollover']
assert (t['patterns'], t['accepted'], t['base_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (70973847823597499842560000, 49627488, 60818, 1073741824, 816, 3)
assert (t['epoch27_rerotated_key_loss_states'], t['epoch27_bound_key_recovery_states'], t['epoch27_replacement_source_lineage_rollover_states']) == (470016, 470016, 470016)
assert (t['stale_or_conflicting_root_choice_acceptances'], t['unbound_source_replacement_acceptances'], t['unbound_rerotation_acceptances'], t['unbound_key_recovery_acceptances'], t['unbound_or_conflicting_lineage_rollover_acceptances'], t['deadline_reset_acceptances'], t['bad_acceptances']) == (0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_second_restart_split_witness_rollback']
assert (s['patterns'], s['accepted'], s['base_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (2818572288000000000000000, 16137940, 35468, 16777216, 455, 3)
assert (s['second_verifier_restart_states'], s['split_witness_rollback_states'], s['bounded_split_witness_recoveries']) == (3144960, 2358720, 1572480)
assert (s['cached_second_restart_authority_acceptances'], s['unbound_or_conflicting_witness_rollback_acceptances'], s['unbound_or_forked_witness_recovery_acceptances'], s['below_publication_quorum_acceptances'], s['bad_acceptances']) == (0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_second_witness_churn_after_rollback']
assert (b['patterns'], b['accepted'], b['base_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (65384736620544000000, 3894800, 10700, 4194304, 364, 3)
assert (b['second_membership_witness_churn_states'], b['second_membership_witness_churn_recoveries']) == (276640, 276640)
assert (b['below_replication_quorum_acceptances'], b['unbound_or_conflicting_rollback_acceptances'], b['unbound_or_forked_first_witness_churn_acceptances'], b['unbound_or_forked_second_witness_churn_acceptances'], b['tombstone_generation_collapse_acceptances'], b['unbound_membership_root_acceptances'], b['active_byzantine_acceptances'], b['bad_acceptances']) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(b['checks'])

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}

for line in (H / 'winloop_v76_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V76', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

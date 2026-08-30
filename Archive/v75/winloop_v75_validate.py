#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v74' / 'winloop_v74.json').read_text())
assert base['version'] == 'V74'
assert base['digest'] == 'b56ea2b452bf5d2ed56737d8b59a3bed6c4b2cd42e45a6f64c4bef3d55ae30cd'
assert '32466596df72658d1f3c95369df372e586080205673c60e954f92a7e96b08d90  distributed_winloop_v74.py' in (H.parent / 'v74' / 'winloop_v74_SHA256SUMS.txt').read_text()

sp = importlib.util.spec_from_file_location('v75', H / 'distributed_winloop_v75.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v75.json').read_text())
assert a == m.run_validation() and a['version'] == 'V75'
assert a['base'] == {
    'version': 'V74',
    'digest': 'b56ea2b452bf5d2ed56737d8b59a3bed6c4b2cd42e45a6f64c4bef3d55ae30cd',
    'implementation_sha256': '32466596df72658d1f3c95369df372e586080205673c60e954f92a7e96b08d90',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch26_recovered_key_rerotation_rollback_resistance']
assert (t['patterns'], t['accepted'], t['base_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (262649930268247326720000, 40964560, 60242, 268435456, 680, 3)
assert (t['epoch26_bound_source_replacement_states'], t['epoch26_recovered_key_rerotation_states'], t['epoch26_rollback_resistant_root_choice_states']) == (195840, 195840, 195840)
assert (t['stale_or_conflicting_root_choice_acceptances'], t['unbound_source_replacement_acceptances'], t['unbound_rerotation_acceptances'], t['deadline_reset_acceptances'], t['bad_acceptances']) == (0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_restart_source_loss_bounded_reappearance']
assert (s['patterns'], s['accepted'], s['base_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (8808038400000000000000, 10394384, 28556, 4194304, 364, 3)
assert (s['verifier_restart_states'], s['source_disappearance_states'], s['bounded_source_reappearance_recoveries']) == (943488, 943488, 628992)
assert (s['cached_restart_authority_acceptances'], s['conflicting_source_loss_acceptances'], s['unbound_or_forked_reappearance_acceptances'], s['below_publication_quorum_acceptances'], s['bad_acceptances']) == (0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['two_generation_membership_root_rollback_witness_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (2972033482752000000, 2842840, 9940, 1048576, 286, 3)
assert (b['partial_replication_rollback_states'], b['membership_witness_churn_recoveries']) == (217360, 217360)
assert (b['below_replication_quorum_acceptances'], b['unbound_or_conflicting_rollback_acceptances'], b['unbound_or_forked_witness_churn_acceptances'], b['tombstone_generation_collapse_acceptances'], b['unbound_membership_root_acceptances'], b['active_byzantine_acceptances'], b['bad_acceptances']) == (0, 0, 0, 0, 0, 0, 0)
assert all(b['checks'])

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}

for line in (H / 'winloop_v75_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V75', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

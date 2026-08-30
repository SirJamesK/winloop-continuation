#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v73' / 'winloop_v73.json').read_text())
assert base['version'] == 'V73'
assert base['digest'] == '44d2f25f59474776030e3dfdcf1b44c7a348f2f6f668a4297560c038064a0b09'
assert 'a4f731a59b4f58c3018d13157b14bb7c043c799804b1303e3b2eb6fa644912bc  distributed_winloop_v73.py' in (H.parent / 'v73' / 'winloop_v73_SHA256SUMS.txt').read_text()

sp = importlib.util.spec_from_file_location('v74', H / 'distributed_winloop_v74.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v74.json').read_text())
assert a == m.run_validation() and a['version'] == 'V74'
assert a['base'] == {
    'version': 'V73',
    'digest': '44d2f25f59474776030e3dfdcf1b44c7a348f2f6f668a4297560c038064a0b09',
    'implementation_sha256': 'a4f731a59b4f58c3018d13157b14bb7c043c799804b1303e3b2eb6fa644912bc',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch25_key_loss_recovery_monotonic_root']
assert (t['patterns'], t['accepted'], t['base_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (968977607326433280000, 33574240, 59954, 67108864, 560, 3)
assert (t['epoch25_replacement_key_loss_states'], t['epoch25_bound_key_recovery_states'], t['monotonic_root_choice_evidence_states']) == (80640, 80640, 161280)
assert (t['stale_or_conflicting_root_choice_acceptances'], t['unbound_key_recovery_acceptances'], t['deadline_reset_acceptances'], t['bad_acceptances']) == (0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_split_view_delayed_root_convergence']
assert (s['patterns'], s['accepted'], s['base_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (6881280000000000000, 7425704, 25964, 1048576, 286, 3)
assert (s['witness_set_split_view_recoveries'], s['delayed_publication_root_convergence_recoveries'], s['bound_publication_root_convergence_recoveries']) == (494208, 247104, 247104)
assert (s['unbound_or_conflicting_split_view_acceptances'], s['forked_or_unbound_convergence_acceptances'], s['below_publication_quorum_acceptances'], s['cached_join_authority_promotions'], s['bad_acceptances']) == (0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['two_generation_recycled_identity_partial_compaction']
assert (b['patterns'], b['accepted'], b['base_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (33435376680960000, 2019600, 9180, 262144, 220, 3)
assert (b['two_tombstone_generation_reuse_recoveries'], b['partial_membership_root_replication_recoveries'], b['full_membership_root_replication_recoveries']) == (334400, 167200, 167200)
assert (b['below_replication_quorum_acceptances'], b['tombstone_generation_collapse_acceptances'], b['unbound_membership_root_acceptances'], b['active_byzantine_acceptances'], b['bad_acceptances']) == (0, 0, 0, 0, 0)
assert all(b['checks'])

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}

for line in (H / 'winloop_v74_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V74', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

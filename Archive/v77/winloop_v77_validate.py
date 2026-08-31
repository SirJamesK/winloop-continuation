#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v76' / 'winloop_v76.json').read_text())
assert base['version'] == 'V76'
assert base['digest'] == 'fb82071fb7deb52f5a8b74bfee4c01eb3f38169cd562fafe1f042b8f689ad584'
assert '2e24441c269693c69a375fa8f059932391255d0fdfc2336c60d1d48c41a4a732  distributed_winloop_v76.py' in (H.parent / 'v76' / 'winloop_v76_SHA256SUMS.txt').read_text()

sp = importlib.util.spec_from_file_location('v77', H / 'distributed_winloop_v77.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v77.json').read_text())
assert a == m.run_validation() and a['version'] == 'V77'
assert a['base'] == {
    'version': 'V76',
    'digest': 'fb82071fb7deb52f5a8b74bfee4c01eb3f38169cd562fafe1f042b8f689ad584',
    'implementation_sha256': '2e24441c269693c69a375fa8f059932391255d0fdfc2336c60d1d48c41a4a732',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch28_lineage_loss_rebind_continuity']
assert (t['patterns'], t['accepted'], t['base_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (1282470362637926400000, 81654020, 61394, 68719476736, 1330, 3)
assert (t['epoch28_replacement_source_lineage_loss_states'], t['epoch28_bound_lineage_rebind_states'], t['epoch28_tombstone_root_continuity_states']) == (766080, 766080, 766080)
assert (t['stale_or_conflicting_root_choice_acceptances'], t['unbound_source_replacement_acceptances'], t['unbound_rerotation_acceptances'], t['unbound_key_recovery_acceptances'], t['unbound_or_conflicting_lineage_rollover_acceptances'], t['unbound_or_conflicting_lineage_rebind_acceptances'], t['tombstone_root_discontinuity_acceptances'], t['deadline_reset_acceptances'], t['bad_acceptances']) == (0, 0, 0, 0, 0, 0, 0, 0, 0)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])

s = a['publication_renewed_source_loss_cache_generation_rollback']
assert (s['patterns'], s['accepted'], s['base_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (57724360458240000000000000000, 39517248, 48428, 1073741824, 816, 3)
assert (s['renewed_source_disappearance_states'], s['verifier_cache_generation_rollback_states'], s['bound_cache_generation_recoveries']) == (11280384, 8460288, 5640192)
assert (s['cached_second_restart_authority_acceptances'], s['unbound_or_conflicting_witness_rollback_acceptances'], s['unbound_or_forked_witness_recovery_acceptances'], s['unbound_renewed_source_disappearance_acceptances'], s['unbound_or_conflicting_cache_generation_rollback_acceptances'], s['unbound_or_forked_cache_generation_recovery_acceptances'], s['below_publication_quorum_acceptances'], s['bad_acceptances']) == (0, 0, 0, 0, 0, 0, 0, 0)
assert all(s['checks'])

b = a['membership_compaction_third_recycled_identity_generation']
assert (b['patterns'], b['accepted'], b['base_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (30909148220620800000000, 6843200, 12220, 67108864, 560, 3)
assert (b['membership_root_compaction_states'], b['bound_membership_root_compactions'], b['third_recycled_identity_generation_states'], b['third_recycled_identity_generation_recoveries']) == (425600, 425600, 425600, 425600)
assert (b['below_replication_quorum_acceptances'], b['unbound_or_conflicting_rollback_acceptances'], b['unbound_or_forked_first_witness_churn_acceptances'], b['unbound_or_forked_second_witness_churn_acceptances'], b['unbound_or_conflicting_membership_compaction_acceptances'], b['unbound_or_forked_third_identity_reuse_acceptances'], b['tombstone_generation_collapse_acceptances'], b['third_generation_collapse_acceptances'], b['unbound_membership_root_acceptances'], b['active_byzantine_acceptances'], b['bad_acceptances']) == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert all(b['checks'])

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}

for line in (H / 'winloop_v77_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d, n = line.split(maxsplit=1)
        assert hashlib.sha256((H / n.strip()).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V77', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

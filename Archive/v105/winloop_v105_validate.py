#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v104 on main.
BASE_VERSION = 'V104'
BASE_DIGEST = '94102d09f48829cc3c34d00dfd1f936081c4dd040ac099af821d40aa5676c012'
BASE_IMPL_SHA = 'e45302c42c52d2eed16e9d42ee773def8dca1ad918bb60d1ff167895b2f38838'
BASE_EPOCH55_COMPLETE = 28866816
BASE_EPOCH55_DEADLINE_VECTORS = 50116
BASE_TWENTY_NINTH_RESTART_RECOVERIES = 1207664640
BASE_PUB_DEADLINE_VECTORS = 43680
BASE_MEMBERSHIP_QUORUM_CHURN = 30180360
BASE_MEM_DEADLINE_VECTORS = 39711

assert BASE_EPOCH55_COMPLETE // BASE_EPOCH55_DEADLINE_VECTORS == 576
assert BASE_TWENTY_NINTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v105', H / 'distributed_winloop_v105.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v105.json').read_text())
assert a == m.run_validation() and a['version'] == 'V105'
assert a['base'] == {
    'version': BASE_VERSION,
    'digest': BASE_DIGEST,
    'implementation_sha256': BASE_IMPL_SHA,
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch56_fourteenth_source_handoff']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch55_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    36559104747216190600125308562072261912317865098659182308144001467410526471454720, 220711680, 4032, 576, 21778071482940061661655974875633165533184, 54740, 3
)
assert (
    t['epoch56_fourteenth_source_handoff_states'],
    t['epoch56_bound_fourteenth_source_handoff_states'],
    t['epoch56_fourteenth_source_binding_states'],
    t['epoch56_bound_fourteenth_source_binding_states'],
    t['epoch56_verifier_binding_states'],
    t['epoch56_bound_verifier_binding_states'],
    t['epoch56_complete_states'],
) == (189181440, 157651200, 126120960, 94590720, 63060480, 31530240, 31530240)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_thirtieth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_ninth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    40613146627132930812645730483687970317998793351495680, 14569251840, 304128, 27648, 340282366920938463463374607431768211456, 47905, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['thirtieth_verifier_cold_restart_states'],
    s['bound_thirtieth_restart_states'],
    s['bound_thirtieth_restart_recoveries'],
) == (13244774400, 11920296960, 10595819520, 9271342080, 7946864640, 6622387200, 5297909760, 3973432320, 1324477440)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root17_witness_rebind']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    186558971308058510356843098953070188064916129814937600, 232377600, 5320, 760, 21267647932558653966460912964485513216, 43680, 3
)
assert (
    b['root17_witness_rebind_states'],
    b['bound_root17_witness_rebind_states'],
    b['root17_witness_binding_states'],
    b['bound_root17_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (199180800, 165984000, 132787200, 99590400, 66393600, 33196800)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {
    'statements': 513,
    'max_lag': 64,
    'shared_audit': '132 + 4*k',
    'frontier_storage_only': True,
    'trust_bearing_messages_unchanged': True,
}

EXPECTED_DIGEST = '75043a86bdeafbc42ac05e4fcf027d8d917da7af8945a0c47ce5c63a5b062c6b'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v105_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v105.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V105', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

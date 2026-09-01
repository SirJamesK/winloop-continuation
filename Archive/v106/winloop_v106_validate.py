#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v105 on main.
BASE_VERSION = 'V105'
BASE_DIGEST = '75043a86bdeafbc42ac05e4fcf027d8d917da7af8945a0c47ce5c63a5b062c6b'
BASE_IMPL_SHA = 'ceffdfac9abe91537bd571aefa1bfcf626b72066200579d347aa34e25a7a5696'
BASE_EPOCH56_COMPLETE = 31530240
BASE_EPOCH56_DEADLINE_VECTORS = 54740
BASE_THIRTIETH_RESTART_RECOVERIES = 1324477440
BASE_PUB_DEADLINE_VECTORS = 47905
BASE_MEMBERSHIP_QUORUM_CHURN = 33196800
BASE_MEM_DEADLINE_VECTORS = 43680

assert BASE_EPOCH56_COMPLETE // BASE_EPOCH56_DEADLINE_VECTORS == 576
assert BASE_THIRTIETH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v106', H / 'distributed_winloop_v106.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v106.json').read_text())
assert a == m.run_validation() and a['version'] == 'V106'
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

t = a['tombstone_epoch57_fourteenth_lineage_rotation']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch56_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    52441224034799678390625342864315927447552259942702787098534994543323787174042664960, 309173760, 5184, 576, 348449143727040986586495598010130648530944, 59640, 3
)
assert (
    t['epoch57_fourteenth_lineage_rotation_states'],
    t['epoch57_bound_fourteenth_lineage_rotation_states'],
    t['epoch57_fourteenth_lineage_binding_states'],
    t['epoch57_bound_fourteenth_lineage_binding_states'],
    t['epoch57_handed_proof_rebind_states'],
    t['epoch57_bound_handed_proof_rebind_states'],
    t['epoch57_verifier_binding_states'],
    t['epoch57_bound_verifier_binding_states'],
    t['epoch57_complete_states'],
) == (274821120, 240468480, 206115840, 171763200, 137410560, 103057920, 68705280, 34352640, 34352640)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_thirty_first_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirtieth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    710701665172989133325627104632033405061260003376103424, 15934482432, 304128, 27648, 5444517870735015415413993718908291383296, 52394, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['thirty_first_verifier_cold_restart_states'],
    s['bound_thirty_first_restart_states'],
    s['bound_thirty_first_restart_recoveries'],
) == (14485893120, 13037303808, 11588714496, 10140125184, 8691535872, 7242946560, 5794357248, 4345767936, 1448589312)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root18_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    82309310497656073113628680446940953177810887859031244800, 400485800, 8360, 760, 340282366920938463463374607431768211456, 47905, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root18_rollover_states'],
    b['bound_root18_rollover_states'],
    b['root18_binding_states'],
    b['bound_root18_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (364078000, 327670200, 291262400, 254854600, 218446800, 182039000, 145631200, 109223400, 72815600, 36407800)
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

EXPECTED_DIGEST = 'e9e65a487d0effbc030f27d6791c470215f4b8b1580ff2e9e15ca9847c1730f5'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v106_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v106.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V106', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

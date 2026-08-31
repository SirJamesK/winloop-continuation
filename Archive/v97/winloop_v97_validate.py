#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v96' / 'winloop_v96.json').read_text())
assert base['version'] == 'V96'
assert base['digest'] == '5b5719a56d2c3a6469e499966eafd9e5e3db0df04140084c489fc03a739dac90'
assert '659e05188ca0fdd1e4146b4539f2bee73c6e67de0c6ac41331903d2fe543e559  distributed_winloop_v96.py' in (H.parent / 'v96' / 'winloop_v96_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V97.
t96 = base['tombstone_epoch47_ninth_lineage_handed_proof_rebind']
s96 = base['publication_replacement_churn_twenty_first_restart']
b96 = base['membership_witness_replacement_root13_rollover']
assert t96['deadline_vectors'] == 22100
assert t96['epoch47_complete_states'] == 12729600
assert t96['epoch47_complete_states'] // t96['deadline_vectors'] == 576
assert s96['deadline_vectors'] == 18424
assert s96['bound_twenty_first_restart_recoveries'] == 509386752
assert s96['bound_twenty_first_restart_recoveries'] // s96['deadline_vectors'] == 27648
assert b96['deadline_vectors'] == 16215
assert b96['bound_replication_quorum_churn_states'] == 12323400
assert b96['bound_replication_quorum_churn_states'] // b96['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v97', H / 'distributed_winloop_v97.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v97.json').read_text())
assert a == m.run_validation() and a['version'] == 'V97'
assert a['base'] == {
    'version': 'V96',
    'digest': '5b5719a56d2c3a6469e499966eafd9e5e3db0df04140084c489fc03a739dac90',
    'implementation_sha256': '659e05188ca0fdd1e4146b4539f2bee73c6e67de0c6ac41331903d2fe543e559',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch48_tenth_source_handoff_binding']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch47_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    3507945149304437924254962449224343183203403213025073692672, 100009728, 4032, 576, 5070602400912917605986812821504, 24804, 3
)
assert (
    t['epoch48_tenth_source_handoff_states'],
    t['epoch48_bound_tenth_source_handoff_states'],
    t['epoch48_tenth_source_binding_states'],
    t['epoch48_bound_tenth_source_binding_states'],
    t['epoch48_verifier_binding_states'],
    t['epoch48_bound_verifier_binding_states'],
    t['epoch48_complete_states'],
) == (85722624, 71435520, 57148416, 42861312, 28574208, 14287104, 14287104)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_twenty_second_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_first_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    4110654192314799648403434631505219105587200, 6333465600, 304128, 27648, 79228162514264337593543950336, 20825, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_second_verifier_cold_restart_states'],
    s['bound_twenty_second_restart_states'],
    s['bound_twenty_second_restart_recoveries'],
) == (5757696000, 5181926400, 4606156800, 4030387200, 3454617600, 2878848000, 2303078400, 1727308800, 575769600)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root13_witness_rebind_quorum_churn']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    14027286858866207859918935207168194149089280, 98015680, 5320, 760, 4951760157141521099596496896, 18424, 3
)
assert (
    b['root13_witness_rebind_states'],
    b['bound_root13_witness_rebind_states'],
    b['root13_witness_binding_states'],
    b['bound_root13_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (84013440, 70011200, 56008960, 42006720, 28004480, 14002240)
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

EXPECTED_DIGEST = 'fbdc509251dde7057cd18fffc534f63e2bdb819e32bb5c516a1e5ba7b17fb4b2'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v97_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v97.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V97', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

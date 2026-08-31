#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
base = json.loads((H.parent / 'v95' / 'winloop_v95.json').read_text())
assert base['version'] == 'V95'
assert base['digest'] == '5a8ee21699259de7d8f500b4ddaf37f84f0e5767416efd4e5f749c7f1ebcd235'
assert '92c519f3cb7794eee0cb0f9308a5cf8d6c58754533d7dc867922ded6ebfcfe44  distributed_winloop_v95.py' in (H.parent / 'v95' / 'winloop_v95_SHA256SUMS.txt').read_text()

# Re-derive the exact predecessor seed populations used by V96.
t95 = base['tombstone_epoch46_ninth_source_handoff_binding']
s95 = base['publication_successor_disappearance_twentieth_restart']
b95 = base['membership_root12_witness_rebind_quorum_churn']
assert t95['deadline_vectors'] == 19600
assert t95['epoch46_complete_states'] == 11289600
assert t95['epoch46_complete_states'] // t95['deadline_vectors'] == 576
assert s95['deadline_vectors'] == 16215
assert s95['bound_twentieth_restart_recoveries'] == 448312320
assert s95['bound_twentieth_restart_recoveries'] // s95['deadline_vectors'] == 27648
assert b95['deadline_vectors'] == 14190
assert b95['bound_replication_quorum_churn_states'] == 10784400
assert b95['bound_replication_quorum_churn_states'] // b95['deadline_vectors'] == 760

sp = importlib.util.spec_from_file_location('v96', H / 'distributed_winloop_v96.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v96.json').read_text())
assert a == m.run_validation() and a['version'] == 'V96'
assert a['base'] == {
    'version': 'V95',
    'digest': '5a8ee21699259de7d8f500b4ddaf37f84f0e5767416efd4e5f749c7f1ebcd235',
    'implementation_sha256': '92c519f3cb7794eee0cb0f9308a5cf8d6c58754533d7dc867922ded6ebfcfe44',
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch47_ninth_lineage_handed_proof_rebind']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch46_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    15697404485916295883258497314272509400916509071088025600, 114566400, 5184, 576, 316912650057057350374175801344, 22100, 3
)
assert (
    t['epoch47_ninth_lineage_rotation_states'],
    t['epoch47_bound_ninth_lineage_rotation_states'],
    t['epoch47_ninth_lineage_binding_states'],
    t['epoch47_bound_ninth_lineage_binding_states'],
    t['epoch47_handed_proof_rebind_states'],
    t['epoch47_bound_handed_proof_rebind_states'],
    t['epoch47_verifier_binding_states'],
    t['epoch47_bound_verifier_binding_states'],
    t['epoch47_complete_states'],
) == (101836800, 89107200, 76377600, 63648000, 50918400, 38188800, 25459200, 12729600, 12729600)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_twenty_first_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twentieth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    227294996516230098205836973742053291720704, 5603254272, 304128, 27648, 4951760157141521099596496896, 18424, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_first_verifier_cold_restart_states'],
    s['bound_twenty_first_restart_states'],
    s['bound_twenty_first_restart_recoveries'],
) == (5093867520, 4584480768, 4075094016, 3565707264, 3056320512, 2546933760, 2037547008, 1528160256, 509386752)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_witness_replacement_root13_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    19399983101092295491396632329155720406630400, 135557400, 8360, 760, 309485009821345068724781056, 16215, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root13_rollover_states'],
    b['bound_root13_rollover_states'],
    b['root13_binding_states'],
    b['bound_root13_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (123234000, 110910600, 98587200, 86263800, 73940400, 61617000, 49293600, 36970200, 24646800, 12323400)
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

EXPECTED_DIGEST = '5b5719a56d2c3a6469e499966eafd9e5e3db0df04140084c489fc03a739dac90'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v96_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v96.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V96', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

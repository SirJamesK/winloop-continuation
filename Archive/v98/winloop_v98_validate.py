#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v97 on main.
BASE_VERSION = 'V97'
BASE_DIGEST = 'fbdc509251dde7057cd18fffc534f63e2bdb819e32bb5c516a1e5ba7b17fb4b2'
BASE_IMPL_SHA = 'c82fc5c1cb51eb78e500b3cd9f1d8bc67117f0e8a3d9616133e0e7c016f9c4ac'
BASE_EPOCH48_COMPLETE = 14287104
BASE_EPOCH48_DEADLINE_VECTORS = 24804
BASE_TWENTY_SECOND_RESTART_RECOVERIES = 575769600
BASE_PUB_DEADLINE_VECTORS = 20825
BASE_MEMBERSHIP_QUORUM_CHURN = 14002240
BASE_MEM_DEADLINE_VECTORS = 18424

# Re-derive the exact predecessor static seed populations used by V98.
assert BASE_EPOCH48_COMPLETE // BASE_EPOCH48_DEADLINE_VECTORS == 576
assert BASE_TWENTY_SECOND_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v98', H / 'distributed_winloop_v98.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v98.json').read_text())
assert a == m.run_validation() and a['version'] == 'V98'
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

t = a['tombstone_epoch49_tenth_lineage_handed_proof_rebind']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch48_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    5161414331725496357173745620501698324244240988731928456724480, 143700480, 5184, 576, 81129638414606681695789005144064, 27720, 3
)
assert (
    t['epoch49_tenth_lineage_rotation_states'],
    t['epoch49_bound_tenth_lineage_rotation_states'],
    t['epoch49_tenth_lineage_binding_states'],
    t['epoch49_bound_tenth_lineage_binding_states'],
    t['epoch49_handed_proof_rebind_states'],
    t['epoch49_bound_handed_proof_rebind_states'],
    t['epoch49_verifier_binding_states'],
    t['epoch49_bound_verifier_binding_states'],
    t['epoch49_complete_states'],
) == (127733760, 111767040, 95800320, 79833600, 63866880, 47900160, 31933440, 15966720, 15966720)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_twenty_third_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_second_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    73985064189515675631019532045246588440805376, 7124502528, 304128, 27648, 1267650600228229401496703205376, 23426, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_third_verifier_cold_restart_states'],
    s['bound_twenty_third_restart_states'],
    s['bound_twenty_third_restart_recoveries'],
) == (6476820480, 5829138432, 5181456384, 4533774336, 3886092288, 3238410240, 2590728192, 1943046144, 647682048)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_witness_replacement_root14_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    7322102780060736873718617937368671531827200000, 174097000, 8360, 760, 79228162514264337593543950336, 20825, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root14_rollover_states'],
    b['bound_root14_rollover_states'],
    b['root14_binding_states'],
    b['bound_root14_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (158270000, 142443000, 126616000, 110789000, 94962000, 79135000, 63308000, 47481000, 31654000, 15827000)
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

EXPECTED_DIGEST = 'd8006fc584fa9551a1119b1c3f9093973d6d942090d3f07a646cfa7e8987a9ea'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v98_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v98.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V98', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

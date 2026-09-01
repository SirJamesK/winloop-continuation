#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v98 on main.
BASE_VERSION = 'V98'
BASE_DIGEST = 'd8006fc584fa9551a1119b1c3f9093973d6d942090d3f07a646cfa7e8987a9ea'
BASE_IMPL_SHA = '97354e6aae728d8c7108ee8da6db10b118cafe350a6246f6482a5c42b885a70a'
BASE_EPOCH49_COMPLETE = 15966720
BASE_EPOCH49_DEADLINE_VECTORS = 27720
BASE_TWENTY_THIRD_RESTART_RECOVERIES = 647682048
BASE_PUB_DEADLINE_VECTORS = 23426
BASE_MEMBERSHIP_QUORUM_CHURN = 15827000
BASE_MEM_DEADLINE_VECTORS = 20825

assert BASE_EPOCH49_COMPLETE // BASE_EPOCH49_DEADLINE_VECTORS == 576
assert BASE_TWENTY_THIRD_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v99', H / 'distributed_winloop_v99.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v99.json').read_text())
assert a == m.run_validation() and a['version'] == 'V99'
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

t = a['tombstone_epoch50_eleventh_source_handoff']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch49_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    1143959420837508709113916730800990552586345588854320157742333952, 124411392, 4032, 576, 1298074214633706907132624082305024, 30856, 3
)
assert (
    t['epoch50_eleventh_source_handoff_states'],
    t['epoch50_bound_eleventh_source_handoff_states'],
    t['epoch50_eleventh_source_binding_states'],
    t['epoch50_bound_eleventh_source_binding_states'],
    t['epoch50_verifier_binding_states'],
    t['epoch50_bound_verifier_binding_states'],
    t['epoch50_complete_states'],
) == (106638336, 88865280, 71092224, 53319168, 35546112, 17773056, 17773056)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_successor_disappearance_twenty_fourth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_third_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    1325705222581366857460802474656907195590901760, 7978798080, 304128, 27648, 20282409603651670423947251286016, 26235, 3
)
assert (
    s['successor_source_disappearance_states'],
    s['bound_successor_source_disappearance_states'],
    s['replacement_source_binding_states'],
    s['bound_replacement_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_fourth_verifier_cold_restart_states'],
    s['bound_twenty_fourth_restart_states'],
    s['bound_twenty_fourth_restart_recoveries'],
) == (7253452800, 6528107520, 5802762240, 5077416960, 4352071680, 3626726400, 2901381120, 2176035840, 725345280)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root14_witness_rebind']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    5241484483596724889342470398802093179666432000, 124626320, 5320, 760, 1267650600228229401496703205376, 23426, 3
)
assert (
    b['root14_witness_rebind_states'],
    b['bound_root14_witness_rebind_states'],
    b['root14_witness_binding_states'],
    b['bound_root14_witness_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (106822560, 89018800, 71215040, 53411280, 35607520, 17803760)
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

EXPECTED_DIGEST = 'a6afb2b427d9aa3ea6287d16c971d2ee3fdd2fa6439fde28bd65074c145e5e5a'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v99_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v99.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V99', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

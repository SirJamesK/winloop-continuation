#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V110'
BASE_DIGEST = 'bbac10e5e94ef6b25d49193b242880582a1e93f0b745a783959a8f01112a5783'
BASE_IMPL_SHA = 'ff3eac01f66a61f4a79da3aed126bf58caf81a0772750c61e35043be025799fd'
BASE_EPOCH61_COMPLETE = 47324160
BASE_EPOCH61_DEADLINE_VECTORS = 82160
BASE_THIRTY_FIFTH_RESTART_RECOVERIES = 2022451200
BASE_PUB_DEADLINE_VECTORS = 73150
BASE_MEMBERSHIP_QUORUM_CHURN = 51319000
BASE_MEM_DEADLINE_VECTORS = 67525

assert BASE_EPOCH61_COMPLETE // BASE_EPOCH61_DEADLINE_VECTORS == 576
assert BASE_THIRTY_FIFTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v111', H / 'distributed_winloop_v111.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v111.json').read_text())
assert a == m.run_validation() and a['version'] == 'V111'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc62()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch61_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    1065486945191575456068357530665188317474178429319920450417113033088179296700961489194522372997120, 357073920, 4032, 576, 365375409332725729550921208179070754913983135744, 88560, 3
)
assert (t['epoch62_seventeenth_source_handoff_states'], t['epoch62_bound_seventeenth_source_handoff_states'], t['epoch62_seventeenth_source_binding_states'], t['epoch62_bound_seventeenth_source_binding_states'], t['epoch62_verifier_binding_states'], t['epoch62_bound_verifier_binding_states'], t['epoch62_complete_states']) == (
    306063360, 255052800, 204042240, 153031680, 102021120, 51010560, 51010560
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.successor_disappearance_thirty_sixth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_fifth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    1124778119319115207310798693572679127488178828119301616041984, 24050138112, 304128, 27648, 5708990770823839524233143877797980545530986496, 79079, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_sixth_verifier_cold_restart_states'], s['bound_thirty_sixth_restart_states'], s['bound_thirty_sixth_restart_recoveries']) == (
    21863761920, 19677385728, 17491009536, 15304633344, 13118257152, 10931880960, 8745504768, 6559128576, 2186376192
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root20_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    5241646579326746276434725108911953312019835462691929980928000, 389158000, 5320, 760, 356811923176489970264571492362373784095686656, 73150, 3
)
assert (b['root20_witness_rebind_states'], b['bound_root20_witness_rebind_states'], b['root20_witness_binding_states'], b['bound_root20_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    333564000, 277970000, 222376000, 166782000, 111188000, 55594000
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '2b14b0a6d8e8b84bf1750e7f2b8ea3cc0a529cdddd987b7d5ebbb010aa481342'

for line in (H / 'winloop_v111_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v111.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V111', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

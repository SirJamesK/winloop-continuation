#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V108'
BASE_DIGEST = '2fee415ad926a46d561896d28bab0ac3d11f2c07abf05a12f1cda75ff2134e9b'
BASE_IMPL_SHA = 'aaecd62ab5f7f7c83486954d2e363a1ff140a9605423f6e240b9e439ac997979'
BASE_EPOCH59_COMPLETE = 40492800
BASE_EPOCH59_DEADLINE_VECTORS = 70300
BASE_THIRTY_THIRD_RESTART_RECOVERIES = 1719595008
BASE_PUB_DEADLINE_VECTORS = 62196
BASE_MEMBERSHIP_QUORUM_CHURN = 43437800
BASE_MEM_DEADLINE_VECTORS = 57155

assert BASE_EPOCH59_COMPLETE // BASE_EPOCH59_DEADLINE_VECTORS == 576
assert BASE_THIRTY_THIRD_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v109', H / 'distributed_winloop_v109.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v109.json').read_text())
assert a == m.run_validation() and a['version'] == 'V109'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc60()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch59_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    3491550057987287843382729747555329825073317920997634626918036810867888846730037810333483008, 306738432, 4032, 576, 1427247692705959881058285969449495136382746624, 76076, 3
)
assert (t['epoch60_sixteenth_source_handoff_states'], t['epoch60_bound_sixteenth_source_handoff_states'], t['epoch60_sixteenth_source_binding_states'], t['epoch60_bound_sixteenth_source_binding_states'], t['epoch60_verifier_binding_states'], t['epoch60_bound_verifier_binding_states'], t['epoch60_complete_states']) == (
    262918656, 219098880, 175279104, 131459328, 87639552, 43819776, 43819776
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.successor_disappearance_thirty_fourth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_third_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    3751719132678202650477572357601613086460576378168698470400, 20536243200, 304128, 27648, 22300745198530623141535718272648361505980416, 67525, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_fourth_verifier_cold_restart_states'], s['bound_thirty_fourth_restart_states'], s['bound_thirty_fourth_restart_recoveries']) == (
    18669312000, 16802380800, 14935449600, 13068518400, 11201587200, 9334656000, 7467724800, 5600793600, 1866931200
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root19_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    17409082933602097114722219052988713698008463262430967889920, 330882720, 5320, 760, 1393796574908163946345982392040522594123776, 62196, 3
)
assert (b['root19_witness_rebind_states'], b['bound_root19_witness_rebind_states'], b['root19_witness_binding_states'], b['bound_root19_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    283613760, 236344800, 189075840, 141806880, 94537920, 47268960
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '75de7563e42cc8fd5de633ee74780dc303db3d335141a68c02145546070e7ba0'

for line in (H / 'winloop_v109_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v109.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V109', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

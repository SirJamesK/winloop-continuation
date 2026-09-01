#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V112'
BASE_DIGEST = '8ceae300f4fd73bdd52090a785f6b6d8e4945dc471cf18e1d6916df28aa5a470'
BASE_IMPL_SHA = 'f2d0762cdf625f77c509dc2bf0254aad8bc1d2d5a24d8013a5a5e7338db7a8ac'
BASE_EPOCH63_COMPLETE = 54883584
BASE_EPOCH63_DEADLINE_VECTORS = 95284
BASE_THIRTY_SEVENTH_RESTART_RECOVERIES = 2358927360
BASE_PUB_DEADLINE_VECTORS = 85320
BASE_MEMBERSHIP_QUORUM_CHURN = 60100040
BASE_MEM_DEADLINE_VECTORS = 79079

assert BASE_EPOCH63_COMPLETE // BASE_EPOCH63_DEADLINE_VECTORS == 576
assert BASE_THIRTY_SEVENTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v113', H / 'distributed_winloop_v113.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v113.json').read_text())
assert a == m.run_validation() and a['version'] == 'V113'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc64()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch63_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    322772004729777986330515098018555320970275840426548364109655195385276622759201972539743270747420753920, 412634880, 4032, 576, 93536104789177786765035829293842113257979682750464, 102340, 3
)
assert (t['epoch64_eighteenth_source_handoff_states'], t['epoch64_bound_eighteenth_source_handoff_states'], t['epoch64_eighteenth_source_binding_states'], t['epoch64_bound_eighteenth_source_binding_states'], t['epoch64_verifier_binding_states'], t['epoch64_bound_verifier_binding_states'], t['epoch64_complete_states']) == (
    353687040, 294739200, 235791360, 176843520, 117895680, 58947840, 58947840
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.successor_disappearance_thirty_eighth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_seventh_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    334557961349749792446900120886995798045774325421995286442541056, 27943584768, 304128, 27648, 1461501637330902918203684832716283019655932542976, 91881, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_eighth_verifier_cold_restart_states'], s['bound_thirty_eighth_restart_states'], s['bound_thirty_eighth_restart_recoveries']) == (
    25403258880, 22862932992, 20322607104, 17782281216, 15241955328, 12701629440, 10161303552, 7620977664, 2540325888
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root21_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    1565107658973731319619755995226878623169819338199318103746150400, 453902400, 5320, 760, 91343852333181432387730302044767688728495783936, 85320, 3
)
assert (b['root21_witness_rebind_states'], b['bound_root21_witness_rebind_states'], b['root21_witness_binding_states'], b['bound_root21_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    389059200, 324216000, 259372800, 194529600, 129686400, 64843200
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '7577953c49ae7a820672908eafe13c55b73176705c4f4aeb1d4914835095c983'

for line in (H / 'winloop_v113_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v113.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V113', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

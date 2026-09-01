#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V106'
BASE_DIGEST = 'e9e65a487d0effbc030f27d6791c470215f4b8b1580ff2e9e15ca9847c1730f5'
BASE_IMPL_SHA = '52066546352d02a921dccc6eb6ecb47625924ad90f77cf1be20341a3d245f3ad'
BASE_EPOCH57_COMPLETE = 34352640
BASE_EPOCH57_DEADLINE_VECTORS = 59640
BASE_THIRTY_FIRST_RESTART_RECOVERIES = 1448589312
BASE_PUB_DEADLINE_VECTORS = 52394
BASE_MEMBERSHIP_QUORUM_CHURN = 36407800
BASE_MEM_DEADLINE_VECTORS = 47905

assert BASE_EPOCH57_COMPLETE // BASE_EPOCH57_DEADLINE_VECTORS == 576
assert BASE_THIRTY_FIRST_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v107', H / 'distributed_winloop_v107.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v107.json').read_text())
assert a == m.run_validation() and a['version'] == 'V107'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])
assert a['independence']['bad_acceptances'] == 0 and a['independence']['conservative_cross_role_credit'] == 12

t = m.gc58()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch57_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    11349232865792314998831999084691215627284724710779811692020223219702188602258167431168, 261370368, 4032, 576, 5575186299632655785383929568162090376495104, 64824, 3
)
assert (t['epoch58_fifteenth_source_handoff_states'], t['epoch58_bound_fifteenth_source_handoff_states'], t['epoch58_fifteenth_source_binding_states'], t['epoch58_bound_fifteenth_source_binding_states'], t['epoch58_verifier_binding_states'], t['epoch58_bound_verifier_binding_states'], t['epoch58_complete_states']) == (
    224031744, 186693120, 149354496, 112015872, 74677248, 37338624, 37338624
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)
assert a['epoch58']['accepted'] == t['accepted'] and a['epoch58']['bad_acceptances'] == 0

s = m.successor_disappearance_thirty_second_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_first_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    12404520723124691809054843582164024664282571437328302080, 17382435840, 304128, 27648, 87112285931760246646623899502532662132736, 57155, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_second_verifier_cold_restart_states'], s['bound_thirty_second_restart_states'], s['bound_thirty_second_restart_recoveries']) == (
    15802214400, 14221992960, 12641771520, 11061550080, 9481328640, 7901107200, 6320885760, 4740664320, 1580221440
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)
assert a['publication32']['accepted'] == s['accepted'] and a['publication32']['bad_acceptances'] == 0

b = m.root18_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    57286861495762154383217215100642692650392472999407124480, 278736080, 5320, 760, 5444517870735015415413993718908291383296, 52394, 3
)
assert (b['root18_witness_rebind_states'], b['bound_root18_witness_rebind_states'], b['root18_witness_binding_states'], b['bound_root18_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    238916640, 199097200, 159277760, 119458320, 79638880, 39819440
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)
assert a['membership18']['accepted'] == b['accepted'] and a['membership18']['bad_acceptances'] == 0

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '72f2c7b36e0aaf5380e35e440753fe4481e43b6b2e94057317eff306c8c738c5'

for line in (H / 'winloop_v107_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v107.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V107', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

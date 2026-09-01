#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V107'
BASE_DIGEST = '72f2c7b36e0aaf5380e35e440753fe4481e43b6b2e94057317eff306c8c738c5'
BASE_IMPL_SHA = '44f9ce6d0bf1c76c864b9a1ab91bdcab26bd7cf4016eae69936e26ba71342eaf'
BASE_EPOCH58_COMPLETE = 37338624
BASE_EPOCH58_DEADLINE_VECTORS = 64824
BASE_THIRTY_SECOND_RESTART_RECOVERIES = 1580221440
BASE_PUB_DEADLINE_VECTORS = 57155
BASE_MEMBERSHIP_QUORUM_CHURN = 39819440
BASE_MEM_DEADLINE_VECTORS = 52394

assert BASE_EPOCH58_COMPLETE // BASE_EPOCH58_DEADLINE_VECTORS == 576
assert BASE_THIRTY_SECOND_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v108', H / 'distributed_winloop_v108.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v108.json').read_text())
assert a == m.run_validation() and a['version'] == 'V108'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])
assert a['independence']['bad_acceptances'] == 0 and a['independence']['conservative_cross_role_credit'] == 12

t = m.gc59()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch58_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    16204305868653763254692419828161860903457798725997946400191692487465199225455105592524800, 364435200, 5184, 576, 89202980794122492566142873090593446023921664, 70300, 3
)
assert (t['epoch59_fifteenth_lineage_rotation_states'], t['epoch59_bound_fifteenth_lineage_rotation_states'], t['epoch59_fifteenth_lineage_binding_states'], t['epoch59_bound_fifteenth_lineage_binding_states'], t['epoch59_handed_proof_rebind_states'], t['epoch59_bound_handed_proof_rebind_states'], t['epoch59_verifier_binding_states'], t['epoch59_bound_verifier_binding_states'], t['epoch59_complete_states']) == (
    323942400, 283449600, 242956800, 202464000, 161971200, 121478400, 80985600, 40492800, 40492800
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)
assert a['epoch59']['accepted'] == t['accepted'] and a['epoch59']['bad_acceptances'] == 0

s = m.replacement_churn_thirty_third_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_second_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    215977344664988422851817003288957726328676423932414263296, 18915545088, 304128, 27648, 1393796574908163946345982392040522594123776, 62196, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_third_verifier_cold_restart_states'], s['bound_thirty_third_restart_states'], s['bound_thirty_third_restart_recoveries']) == (
    17195950080, 15476355072, 13756760064, 12037165056, 10317570048, 8597975040, 6878380032, 5158785024, 1719595008
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)
assert a['publication33']['accepted'] == s['accepted'] and a['publication33']['bad_acceptances'] == 0

b = m.root19_rollover_after_root18_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    25139828665532708733017816326519089986279344779652025548800, 477815800, 8360, 760, 87112285931760246646623899502532662132736, 57155, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root19_rollover_states'], b['bound_root19_rollover_states'], b['root19_binding_states'], b['bound_root19_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    434378000, 390940200, 347502400, 304064600, 260626800, 217189000, 173751200, 130313400, 86875600, 43437800
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)
assert a['membership19']['accepted'] == b['accepted'] and a['membership19']['bad_acceptances'] == 0

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '2fee415ad926a46d561896d28bab0ac3d11f2c07abf05a12f1cda75ff2134e9b'

for line in (H / 'winloop_v108_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v108.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V108', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

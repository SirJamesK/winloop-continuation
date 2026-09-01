#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V116'
BASE_DIGEST = '4048885296831bfca1c4e95ecf7a07f81a6b75fb77668677a7d0e56669bc8cf8'
BASE_IMPL_SHA = '9d2b383524acdb2b7362a3ec4502b8ebfca08b1123dfde2c9737dcd66eddfc05'
BASE_EPOCH67_COMPLETE = 72334080
BASE_EPOCH67_DEADLINE_VECTORS = 125580
BASE_FORTY_FIRST_RESTART_RECOVERIES = 3139817472
BASE_PUB_DEADLINE_VECTORS = 113564
BASE_MEMBERSHIP_QUORUM_CHURN = 80556200
BASE_MEM_DEADLINE_VECTORS = 105995

assert BASE_EPOCH67_COMPLETE // BASE_EPOCH67_DEADLINE_VECTORS == 576
assert BASE_FORTY_FIRST_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v117', H / 'distributed_winloop_v117.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v117.json').read_text())
assert a == m.run_validation() and a['version'] == 'V117'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc68()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch67_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    29052109341527562268873102790492993008806734575062905582801588367550775205227259044422600075177353471445897838592, 540465408, 4032, 576, 6129982163463555433433388108601236734474956488734408704, 134044, 3
)
assert (t['epoch68_twentieth_source_handoff_states'], t['epoch68_bound_twentieth_source_handoff_states'], t['epoch68_twentieth_source_binding_states'], t['epoch68_bound_twentieth_source_binding_states'], t['epoch68_verifier_binding_states'], t['epoch68_bound_verifier_binding_states'], t['epoch68_complete_states']) == (
    463256064, 386046720, 308837376, 231628032, 154418688, 77209344, 77209344
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.successor_disappearance_forty_second_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_forty_first_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    28990001943560309893195966821027821606960359858905834258093268008960, 36946990080, 304128, 27648, 95780971304118053647396689196894323976171195136475136, 121485, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['forty_second_verifier_cold_restart_states'], s['bound_forty_second_restart_states'], s['bound_forty_second_restart_recoveries']) == (
    33588172800, 30229355520, 26870538240, 23511720960, 20152903680, 16794086400, 13435269120, 10076451840, 3358817280
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root23_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    136525564708561801291888698447746407738762036600488159625721287802880, 604160480, 5320, 760, 5986310706507378352962293074805895248510699696029696, 113564, 3
)
assert (b['root23_witness_rebind_states'], b['bound_root23_witness_rebind_states'], b['root23_witness_binding_states'], b['bound_root23_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    517851840, 431543200, 345234560, 258925920, 172617280, 86308640
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'c3e35f2bc16e706874171cbad13aa7018322443d4e77a69eb8d29aa8ed4b3527'

for line in (H / 'winloop_v117_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v117.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V117', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

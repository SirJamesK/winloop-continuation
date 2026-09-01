#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V115'
BASE_DIGEST = 'e3c94f30261338016f4c9fafa47e898ebc1052e90848ac4fb1a77a00c62e2754'
BASE_IMPL_SHA = '2e0bdfcd0a01c3314068f90065b7ace228fee0e70d1d37d9c348e4e9b3f3ff60'
BASE_EPOCH66_COMPLETE = 67668480
BASE_EPOCH66_DEADLINE_VECTORS = 117480
BASE_FORTIETH_RESTART_RECOVERIES = 2930549760
BASE_PUB_DEADLINE_VECTORS = 105995
BASE_MEMBERSHIP_QUORUM_CHURN = 75065200
BASE_MEM_DEADLINE_VECTORS = 98770

assert BASE_EPOCH66_COMPLETE // BASE_EPOCH66_DEADLINE_VECTORS == 576
assert BASE_FORTIETH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v116', H / 'distributed_winloop_v116.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v116.json').read_text())
assert a == m.run_validation() and a['version'] == 'V116'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc67()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch66_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    136695832335226685242236550374579622969006893389765462256071946811330029826843041199172269464053532897186938880, 651006720, 5184, 576, 383123885216472214589586756787577295904684780545900544, 125580, 3
)
assert (t['epoch67_nineteenth_lineage_rotation_states'], t['epoch67_bound_nineteenth_lineage_rotation_states'], t['epoch67_nineteenth_lineage_binding_states'], t['epoch67_bound_nineteenth_lineage_binding_states'], t['epoch67_handed_proof_rebind_states'], t['epoch67_bound_handed_proof_rebind_states'], t['epoch67_verifier_binding_states'], t['epoch67_bound_verifier_binding_states'], t['epoch67_complete_states']) == (
    578672640, 506338560, 434004480, 361670400, 289336320, 217002240, 144668160, 72334080, 72334080
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.replacement_churn_forty_first_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_fortieth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    1693738208790428361891852273975801299014716995419589950243910713344, 34537992192, 304128, 27648, 5986310706507378352962293074805895248510699696029696, 113564, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['forty_first_verifier_cold_restart_states'], s['bound_forty_first_restart_states'], s['bound_forty_first_restart_recoveries']) == (
    31398174720, 28258357248, 25118539776, 21978722304, 18838904832, 15699087360, 12559269888, 9419452416, 3139817472
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root23_rollover_after_root22_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    200241147275197987047292613493785361270134527999512128182990091059200, 886118200, 8360, 760, 374144419156711147060143317175368453031918731001856, 105995, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root23_rollover_states'], b['bound_root23_rollover_states'], b['root23_binding_states'], b['bound_root23_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    805562000, 725005800, 644449600, 563893400, 483337200, 402781000, 322224800, 241668600, 161112400, 80556200
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '4048885296831bfca1c4e95ecf7a07f81a6b75fb77668677a7d0e56669bc8cf8'

for line in (H / 'winloop_v116_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v116.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V116', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

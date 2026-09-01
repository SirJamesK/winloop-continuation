#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V117'
BASE_DIGEST = 'c3e35f2bc16e706874171cbad13aa7018322443d4e77a69eb8d29aa8ed4b3527'
BASE_IMPL_SHA = 'a6de110016935bcba84fd12cf3f80e0dbdee5a28d4df5d7b342640c64cc39af3'
BASE_EPOCH68_COMPLETE = 77209344
BASE_EPOCH68_DEADLINE_VECTORS = 134044
BASE_FORTY_SECOND_RESTART_RECOVERIES = 3358817280
BASE_PUB_DEADLINE_VECTORS = 121485
BASE_MEMBERSHIP_QUORUM_CHURN = 86308640
BASE_MEM_DEADLINE_VECTORS = 113564

assert BASE_EPOCH68_COMPLETE // BASE_EPOCH68_DEADLINE_VECTORS == 576
assert BASE_FORTY_SECOND_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v118', H / 'distributed_winloop_v118.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v118.json').read_text())
assert a == m.run_validation() and a['version'] == 'V118'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc69()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch68_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    40770511353547122929503152001815147648279658994444520289888914682521426099267593409854337516039713903138148628561920, 740689920, 5184, 576, 98079714615416886934934209737619787751599303819750539264, 142880, 3
)
assert (t['epoch69_twentieth_lineage_rotation_states'], t['epoch69_bound_twentieth_lineage_rotation_states'], t['epoch69_twentieth_lineage_binding_states'], t['epoch69_bound_twentieth_lineage_binding_states'], t['epoch69_handed_proof_rebind_states'], t['epoch69_bound_handed_proof_rebind_states'], t['epoch69_verifier_binding_states'], t['epoch69_bound_verifier_binding_states'], t['epoch69_complete_states']) == (
    658391040, 576092160, 493793280, 411494400, 329195520, 246896640, 164597760, 82298880, 82298880
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.replacement_churn_forty_third_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_forty_second_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    495457591269117625860044328830390095718657356210333718676146818646016, 39465474048, 304128, 27648, 1532495540865888858358347027150309183618739122183602176, 129766, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['forty_third_verifier_cold_restart_states'], s['bound_forty_third_restart_states'], s['bound_forty_third_restart_recoveries']) == (
    35877703680, 32289933312, 28702162944, 25114392576, 21526622208, 17938851840, 14351081472, 10763311104, 3587770368
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root24_rollover_after_root23_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    58753070605615561383543826090616385123439662647382490763069023164825600, 1015614600, 8360, 760, 95780971304118053647396689196894323976171195136475136, 121485, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root24_rollover_states'], b['bound_root24_rollover_states'], b['root24_binding_states'], b['bound_root24_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    923286000, 830957400, 738628800, 646300200, 553971600, 461643000, 369314400, 276985800, 184657200, 92328600
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '7587b4d5fffe5e2ff827a56f2e3b723b21af0a9ccfa785d12f54932bd7c455e4'

for line in (H / 'winloop_v118_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v118.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V118', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

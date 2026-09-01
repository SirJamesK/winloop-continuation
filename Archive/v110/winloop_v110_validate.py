#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V109'
BASE_DIGEST = '75de7563e42cc8fd5de633ee74780dc303db3d335141a68c02145546070e7ba0'
BASE_IMPL_SHA = 'a6755e64b1b2d78a90f01f8d27dcb9f994048f374522ba90a858d772300f9720'
BASE_EPOCH60_COMPLETE = 43819776
BASE_EPOCH60_DEADLINE_VECTORS = 76076
BASE_THIRTY_FOURTH_RESTART_RECOVERIES = 1866931200
BASE_PUB_DEADLINE_VECTORS = 67525
BASE_MEMBERSHIP_QUORUM_CHURN = 47268960
BASE_MEM_DEADLINE_VECTORS = 62196

assert BASE_EPOCH60_COMPLETE // BASE_EPOCH60_DEADLINE_VECTORS == 576
assert BASE_THIRTY_FOURTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v110', H / 'distributed_winloop_v110.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v110.json').read_text())
assert a == m.run_validation() and a['version'] == 'V110'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc61()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch60_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    4964499368066510568117573969190750227052397497965475748486385221497351089357793669256199536640, 425917440, 5184, 576, 22835963083295358096932575511191922182123945984, 82160, 3
)
assert (t['epoch61_sixteenth_lineage_rotation_states'], t['epoch61_bound_sixteenth_lineage_rotation_states'], t['epoch61_sixteenth_lineage_binding_states'], t['epoch61_bound_sixteenth_lineage_binding_states'], t['epoch61_handed_proof_rebind_states'], t['epoch61_bound_handed_proof_rebind_states'], t['epoch61_verifier_binding_states'], t['epoch61_bound_verifier_binding_states'], t['epoch61_complete_states']) == (
    378593280, 331269120, 283944960, 236620800, 189296640, 141972480, 94648320, 47324160, 47324160
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.replacement_churn_thirty_fifth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_fourth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    65027946284880686888099973155674608758140815890538980966400, 22246963200, 304128, 27648, 356811923176489970264571492362373784095686656, 73150, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_fifth_verifier_cold_restart_states'], s['bound_thirty_fifth_restart_states'], s['bound_thirty_fifth_restart_recoveries']) == (
    20224512000, 18202060800, 16179609600, 14157158400, 12134707200, 10112256000, 8089804800, 6067353600, 2022451200
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root20_rollover_after_root19_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    7603484108894490704967879978072602521893434793088562233344000, 564509000, 8360, 760, 22300745198530623141535718272648361505980416, 67525, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root20_rollover_states'], b['bound_root20_rollover_states'], b['root20_binding_states'], b['bound_root20_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    513190000, 461871000, 410552000, 359233000, 307914000, 256595000, 205276000, 153957000, 102638000, 51319000
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'bbac10e5e94ef6b25d49193b242880582a1e93f0b745a783959a8f01112a5783'

for line in (H / 'winloop_v110_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v110.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V110', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

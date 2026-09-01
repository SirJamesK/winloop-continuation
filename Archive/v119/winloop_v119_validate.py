#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V118'
BASE_DIGEST = '7587b4d5fffe5e2ff827a56f2e3b723b21af0a9ccfa785d12f54932bd7c455e4'
BASE_IMPL_SHA = '5284baee9edf68dd0e31ff8af0cd91666df179087d64e92f4bb8420a8d59aa1d'
BASE_EPOCH69_COMPLETE = 82298880
BASE_EPOCH69_DEADLINE_VECTORS = 142880
BASE_FORTY_THIRD_RESTART_RECOVERIES = 3587770368
BASE_PUB_DEADLINE_VECTORS = 129766
BASE_MEMBERSHIP_QUORUM_CHURN = 92328600
BASE_MEM_DEADLINE_VECTORS = 121485

assert BASE_EPOCH69_COMPLETE // BASE_EPOCH69_DEADLINE_VECTORS == 576
assert BASE_FORTY_THIRD_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v119', H / 'distributed_winloop_v119.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v119.json').read_text())
assert a == m.run_validation() and a['version'] == 'V119'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc70()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch69_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    8641477539142211763314665641025564141244584019098317542580885519048292003077651304886188823068714053638302645597765632, 613251072, 4032, 576, 1569275433846670190958947355801916604025588861116008628224, 152096, 3
)
assert (t['epoch70_twenty_first_source_handoff_states'], t['epoch70_bound_twenty_first_source_handoff_states'], t['epoch70_twenty_first_source_binding_states'], t['epoch70_bound_twenty_first_source_binding_states'], t['epoch70_verifier_binding_states'], t['epoch70_bound_verifier_binding_states'], t['epoch70_complete_states']) == (
    525643776, 438036480, 350429184, 262821888, 175214592, 87607296, 87607296
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.successor_disappearance_forty_fourth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_forty_third_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    8455683306322447011811172205361459254214257412247071395657890282864640, 42095877120, 304128, 27648, 24519928653854221733733552434404946937899825954937634816, 138415, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['forty_fourth_verifier_cold_restart_states'], s['bound_forty_fourth_restart_states'], s['bound_forty_fourth_restart_recoveries']) == (
    38268979200, 34442081280, 30615183360, 26788285440, 22961387520, 19134489600, 15307591680, 11480693760, 3826897920
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root24_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    39936884629571299539021754990570838018534199015742051262986379927224320, 690355120, 5320, 760, 1532495540865888858358347027150309183618739122183602176, 129766, 3
)
assert (b['root24_witness_rebind_states'], b['bound_root24_witness_rebind_states'], b['root24_witness_binding_states'], b['bound_root24_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    591732960, 493110800, 394488640, 295866480, 197244320, 98622160
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '02eef35bac9f1b1ac5a23d34bda99f93447a517ed75677da0020af5d0497c32c'

for line in (H / 'winloop_v119_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v119.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V119', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

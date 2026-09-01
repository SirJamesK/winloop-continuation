#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V111'
BASE_DIGEST = '2b14b0a6d8e8b84bf1750e7f2b8ea3cc0a529cdddd987b7d5ebbb010aa481342'
BASE_IMPL_SHA = '0896b1df863db6e0e5b1cffec1f0f686e2ff9f63ec580726c576d140f2291bdb'
BASE_EPOCH62_COMPLETE = 51010560
BASE_EPOCH62_DEADLINE_VECTORS = 88560
BASE_THIRTY_SIXTH_RESTART_RECOVERIES = 2186376192
BASE_PUB_DEADLINE_VECTORS = 79079
BASE_MEMBERSHIP_QUORUM_CHURN = 55594000
BASE_MEM_DEADLINE_VECTORS = 73150

assert BASE_EPOCH62_COMPLETE // BASE_EPOCH62_DEADLINE_VECTORS == 576
assert BASE_THIRTY_SIXTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v112', H / 'distributed_winloop_v112.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v112.json').read_text())
assert a == m.run_validation() and a['version'] == 'V112'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc63()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch62_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    1509297774095373019369364054104928091312756217745977982030854515137175579753468648160347425429520384, 493952256, 5184, 576, 5846006549323611672814739330865132078623730171904, 95284, 3
)
assert (t['epoch63_seventeenth_lineage_rotation_states'], t['epoch63_bound_seventeenth_lineage_rotation_states'], t['epoch63_seventeenth_lineage_binding_states'], t['epoch63_bound_seventeenth_lineage_binding_states'], t['epoch63_handed_proof_rebind_states'], t['epoch63_bound_handed_proof_rebind_states'], t['epoch63_verifier_binding_states'], t['epoch63_bound_verifier_binding_states'], t['epoch63_complete_states']) == (
    439068672, 384185088, 329301504, 274417920, 219534336, 164650752, 109767168, 54883584, 54883584
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.replacement_churn_thirty_seventh_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_sixth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    19416749152681629153177424000934960362633097052848683241963520, 25948200960, 304128, 27648, 91343852333181432387730302044767688728495783936, 85320, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_seventh_verifier_cold_restart_states'], s['bound_thirty_seventh_restart_states'], s['bound_thirty_seventh_restart_recoveries']) == (
    23589273600, 21230346240, 18871418880, 16512491520, 14153564160, 11794636800, 9435709440, 7076782080, 2358927360
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root21_rollover_after_root20_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    2279550321820073486816552018973963031709375758321784608511754240, 661100440, 8360, 760, 5708990770823839524233143877797980545530986496, 79079, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root21_rollover_states'], b['bound_root21_rollover_states'], b['root21_binding_states'], b['bound_root21_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    601000400, 540900360, 480800320, 420700280, 360600240, 300500200, 240400160, 180300120, 120200080, 60100040
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '8ceae300f4fd73bdd52090a785f6b6d8e4945dc471cf18e1d6916df28aa5a470'

for line in (H / 'winloop_v112_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v112.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V112', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

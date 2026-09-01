#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V114'
BASE_DIGEST = 'b9510df85e0cf9e16198aff06256607d3c5df36a7c9acc59e567697a5bc5c17d'
BASE_IMPL_SHA = '05cfd2899aa07277fa7c5754299d05595f907ec5f56366a006262fb67eb40cd3'
BASE_EPOCH65_COMPLETE = 63207936
BASE_EPOCH65_DEADLINE_VECTORS = 109736
BASE_THIRTY_NINTH_RESTART_RECOVERIES = 2730792960
BASE_PUB_DEADLINE_VECTORS = 98770
BASE_MEMBERSHIP_QUORUM_CHURN = 69829560
BASE_MEM_DEADLINE_VECTORS = 91881

assert BASE_EPOCH65_COMPLETE // BASE_EPOCH65_DEADLINE_VECTORS == 576
assert BASE_THIRTY_NINTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v115', H / 'distributed_winloop_v115.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v115.json').read_text())
assert a == m.run_validation() and a['version'] == 'V115'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc66()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch65_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    97130205325758115050856430300592143724638950312224477677831222657913603214766334347992767997860641306050560, 473679360, 4032, 576, 23945242826029513411849172299223580994042798784118784, 117480, 3
)
assert (t['epoch66_nineteenth_source_handoff_states'], t['epoch66_bound_nineteenth_source_handoff_states'], t['epoch66_nineteenth_source_binding_states'], t['epoch66_bound_nineteenth_source_binding_states'], t['epoch66_verifier_binding_states'], t['epoch66_bound_verifier_binding_states'], t['epoch66_complete_states']) == (
    406010880, 338342400, 270673920, 203005440, 135336960, 67668480, 67668480
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.successor_disappearance_fortieth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_ninth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    98803197668683217293072013237065145363553221052390852721870110720, 32236047360, 304128, 27648, 374144419156711147060143317175368453031918731001856, 105995, 3
)
assert (s['successor_source_disappearance_states'], s['bound_successor_source_disappearance_states'], s['replacement_source_binding_states'], s['bound_replacement_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['fortieth_verifier_cold_restart_states'], s['bound_fortieth_restart_states'], s['bound_fortieth_restart_recoveries']) == (
    29305497600, 26374947840, 23444398080, 20513848320, 17583298560, 14652748800, 11722199040, 8791649280, 2930549760
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root22_witness_rebind_quorum_churn()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    463829523793599077172338076770171744166475179848691305337480806400, 525456400, 5320, 760, 23384026197294446691258957323460528314494920687616, 98770, 3
)
assert (b['root22_witness_rebind_states'], b['bound_root22_witness_rebind_states'], b['root22_witness_binding_states'], b['bound_root22_witness_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    450391200, 375326000, 300260800, 225195600, 150130400, 75065200
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'e3c94f30261338016f4c9fafa47e898ebc1052e90848ac4fb1a77a00c62e2754'

for line in (H / 'winloop_v115_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v115.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V115', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

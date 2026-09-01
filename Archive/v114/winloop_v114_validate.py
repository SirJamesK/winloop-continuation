#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V113'
BASE_DIGEST = '7577953c49ae7a820672908eafe13c55b73176705c4f4aeb1d4914835095c983'
BASE_IMPL_SHA = '37970b8ca52ab81d13c9a2e16dc683b95d8b24db6e116dcbad5ebd8a85e49212'
BASE_EPOCH64_COMPLETE = 58947840
BASE_EPOCH64_DEADLINE_VECTORS = 102340
BASE_THIRTY_EIGHTH_RESTART_RECOVERIES = 2540325888
BASE_PUB_DEADLINE_VECTORS = 91881
BASE_MEMBERSHIP_QUORUM_CHURN = 64843200
BASE_MEM_DEADLINE_VECTORS = 85320

assert BASE_EPOCH64_COMPLETE // BASE_EPOCH64_DEADLINE_VECTORS == 576
assert BASE_THIRTY_EIGHTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v114', H / 'distributed_winloop_v114.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v114.json').read_text())
assert a == m.run_validation() and a['version'] == 'V114'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc65()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch64_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    455663245038700226230504998187343511328594393456600836417494236510903377842145937996389628160108170051584, 568871424, 5184, 576, 1496577676626844588240573268701473812127674924007424, 109736, 3
)
assert (t['epoch65_eighteenth_lineage_rotation_states'], t['epoch65_bound_eighteenth_lineage_rotation_states'], t['epoch65_eighteenth_lineage_binding_states'], t['epoch65_bound_eighteenth_lineage_binding_states'], t['epoch65_handed_proof_rebind_states'], t['epoch65_bound_handed_proof_rebind_states'], t['epoch65_verifier_binding_states'], t['epoch65_bound_verifier_binding_states'], t['epoch65_complete_states']) == (
    505663488, 442455552, 379247616, 316039680, 252831744, 189623808, 126415872, 63207936, 63207936
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.replacement_churn_thirty_ninth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_thirty_eighth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    5754276047063447198002690426096115623117925163536395893284536320, 30038722560, 304128, 27648, 23384026197294446691258957323460528314494920687616, 98770, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['thirty_ninth_verifier_cold_restart_states'], s['bound_thirty_ninth_restart_states'], s['bound_thirty_ninth_restart_recoveries']) == (
    27307929600, 24577136640, 21846343680, 19115550720, 16384757760, 13653964800, 10923171840, 8192378880, 2730792960
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root22_rollover_after_root21_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    678037468335492912692384244997644817372769299521910447190216540160, 768125160, 8360, 760, 1461501637330902918203684832716283019655932542976, 91881, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root22_rollover_states'], b['bound_root22_rollover_states'], b['root22_binding_states'], b['bound_root22_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    698295600, 628466040, 558636480, 488806920, 418977360, 349147800, 279318240, 209488680, 139659120, 69829560
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'b9510df85e0cf9e16198aff06256607d3c5df36a7c9acc59e567697a5bc5c17d'

for line in (H / 'winloop_v114_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v114.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V114', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent

# Canonical predecessor binding verified from committed Archive/v99 on main.
BASE_VERSION = 'V99'
BASE_DIGEST = 'a6afb2b427d9aa3ea6287d16c971d2ee3fdd2fa6439fde28bd65074c145e5e5a'
BASE_IMPL_SHA = '1af8c1de21d2063013899df4eb6458f34f096d38b71ad8af6a1163905c3e8b4c'
BASE_EPOCH50_COMPLETE = 17773056
BASE_EPOCH50_DEADLINE_VECTORS = 30856
BASE_TWENTY_FOURTH_RESTART_RECOVERIES = 725345280
BASE_PUB_DEADLINE_VECTORS = 26235
BASE_MEMBERSHIP_QUORUM_CHURN = 17803760
BASE_MEM_DEADLINE_VECTORS = 23426

assert BASE_EPOCH50_COMPLETE // BASE_EPOCH50_DEADLINE_VECTORS == 576
assert BASE_TWENTY_FOURTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v100', H / 'distributed_winloop_v100.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v100.json').read_text())
assert a == m.run_validation() and a['version'] == 'V100'
assert a['base'] == {
    'version': BASE_VERSION,
    'digest': BASE_DIGEST,
    'implementation_sha256': BASE_IMPL_SHA,
}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = a['independence_certificate_gate']
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = a['tombstone_epoch51_eleventh_lineage_rotation']
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch50_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    1670303628689232909582270512547405496846159763335132813779397509120, 177396480, 5184, 576, 20769187434139310514121985316880384, 34220, 3
)
assert (
    t['epoch51_eleventh_lineage_rotation_states'],
    t['epoch51_bound_eleventh_lineage_rotation_states'],
    t['epoch51_eleventh_lineage_binding_states'],
    t['epoch51_bound_eleventh_lineage_binding_states'],
    t['epoch51_handed_proof_rebind_states'],
    t['epoch51_bound_handed_proof_rebind_states'],
    t['epoch51_verifier_binding_states'],
    t['epoch51_bound_verifier_binding_states'],
    t['epoch51_complete_states'],
) == (157685760, 137975040, 118264320, 98553600, 78842880, 59132160, 39421440, 19710720, 19710720)
assert t['deadline_origin'] == 'epoch12' and all(t['checks'])
assert t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = a['publication_replacement_churn_twenty_fifth_restart']
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_twenty_fourth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    23657029045309422831669498247965605972473282560, 8898785280, 304128, 27648, 324518553658426726783156020576256, 29260, 3
)
assert (
    s['replacement_source_churn_states'],
    s['bound_replacement_source_churn_states'],
    s['successor_source_binding_states'],
    s['bound_successor_source_binding_states'],
    s['dual_source_reconciliation_states'],
    s['bound_dual_source_reconciliation_states'],
    s['twenty_fifth_verifier_cold_restart_states'],
    s['bound_twenty_fifth_restart_states'],
    s['bound_twenty_fifth_restart_recoveries'],
) == (8089804800, 7280824320, 6471843840, 5662863360, 4853882880, 4044902400, 3235921920, 2426941440, 808980480)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = a['membership_root15_rollover']
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    2686762584431570164453893015304665249730894233600, 219324600, 8360, 760, 20282409603651670423947251286016, 26235, 3
)
assert (
    b['witness_source_replacement_states'],
    b['bound_witness_source_replacement_states'],
    b['replacement_source_binding_states'],
    b['bound_replacement_source_binding_states'],
    b['root15_rollover_states'],
    b['bound_root15_rollover_states'],
    b['root15_binding_states'],
    b['bound_root15_binding_states'],
    b['replication_quorum_churn_states'],
    b['bound_replication_quorum_churn_states'],
) == (199386000, 179447400, 159508800, 139570200, 119631600, 99693000, 79754400, 59815800, 39877200, 19938600)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {
    'statements': 513,
    'max_lag': 64,
    'shared_audit': '132 + 4*k',
    'frontier_storage_only': True,
    'trust_bearing_messages_unchanged': True,
}

EXPECTED_DIGEST = 'd19985578e5f5359d9860d06f552afb7d51c9e54d8f4124c92a2a6ee9c5b9b9a'
assert a['digest'] == EXPECTED_DIGEST

for line in (H / 'winloop_v100_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v100.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V100', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

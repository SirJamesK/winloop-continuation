#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v122 as m
from winloop_v122_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V121',
    'digest': '8ca8a9052bbece7190543f848d5ec799708f842df6063c9f07f513d40011f885',
    'implementation_sha256': '0f7a6367f5cefe63d4123fdf04e631990a2f5e0ad407847abd5f756c43a8db72',
}
a = json.loads((H / 'winloop_v122.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V122' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 88

t = m.gc73()
assert (98899200 // 171700) == t['epoch72_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (944027136, 182104)
assert (
    t['epoch73_bound_twenty_second_lineage_rotation_states'],
    t['epoch73_bound_twenty_second_lineage_binding_states'],
    t['epoch73_bound_handed_proof_rebind_states'],
    t['epoch73_bound_verifier_binding_states'],
) == (
    734243328,
    524459520,
    314675712,
    104891904,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.replacement_churn_forty_seventh_restart()
assert (4336561152 // 156849) == s['bound_forty_sixth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_forty_seventh_restart_recoveries']) == (50682931200, 166650, 4607539200)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
) == (41467852800, 32252774400)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root26_rollover_after_root25_witness_source_replacement()
assert (112054400 // 147440) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1311257640, 156849)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_replacement_source_binding_states'],
    b['bound_root26_rollover_states'],
    b['bound_root26_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    1072847160,
    834436680,
    596026200,
    357615720,
    119205240,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'e64fb7c88abb7ab88dddc1c79153bfed0fc3de90563e5815c5662002907f012c'

for line in (H / 'winloop_v122_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v122.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V122', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

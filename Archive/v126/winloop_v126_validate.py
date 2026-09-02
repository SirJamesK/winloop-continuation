#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v126 as m
from winloop_v126_core import CARRIED_NAMES

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V125',
    'digest': '10c0bbf37187997ae613078eaa0c889bf5413b05ea140817818617f9bc56c613',
    'implementation_sha256': '73929960ceeb848b6393f082d1ca299ecd9b73e3fb03e512d6fbeebcc5058188',
}
a = json.loads((H / 'winloop_v126.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V126' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])
assert len(CARRIED_NAMES) == 98

t = m.gc77()
assert (124312320 // 215820) == t['epoch76_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (1181537280, 227920)
assert (
    t['epoch77_bound_twenty_fourth_lineage_rotation_states'],
    t['epoch77_bound_twenty_fourth_lineage_binding_states'],
    t['epoch77_bound_handed_proof_rebind_states'],
    t['epoch77_bound_verifier_binding_states'],
) == (
    918973440,
    656409600,
    393845760,
    131281920,
)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.replacement_churn_fifty_first_restart()
assert (5487713280 // 198485) == s['bound_fiftieth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_fifty_first_restart_recoveries']) == (63846807552, 209934, 5804255232)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
) == (52238297088, 40629786624)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root28_rollover_after_root27_witness_source_replacement()
assert (142469600 // 187460) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (1659334600, 198485)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root28_rollover_states'],
    b['bound_replication_quorum_churn_states'],
) == (
    1357637400,
    754243000,
    150848600,
)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == 'c5aa4ba69b62e5ae1b1c541792f915cce1a13e6a47705f6f3c1ee7f56dd2f32e'

for line in (H / 'winloop_v126_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v126.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V126', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

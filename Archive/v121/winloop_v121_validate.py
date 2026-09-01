#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import distributed_winloop_v121 as m

H = Path(__file__).resolve().parent
BASE = {
    'version': 'V120',
    'digest': '7d958d0fc2e8e0c1d18c8a82c8f530aa48b8ed82b07086d91b71ea9d04acd382',
    'implementation_sha256': 'ed7f9bb69dd6857515ed1569ca17ba9d3c2e5b0699abde5c9d91b30cc628cdb4',
}
a = json.loads((H / 'winloop_v121.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V121' and a['base'] == BASE
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit']) == (150, 4, 12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

t = m.gc72()
assert (93139200 // 161700) == t['epoch71_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (692294400, 171700)
assert (t['epoch72_bound_twenty_second_source_handoff_states'], t['epoch72_bound_twenty_second_source_binding_states'], t['epoch72_bound_verifier_binding_states']) == (494496000, 296697600, 98899200)
assert t['deadline_origin'] == 'epoch12' and t['bad_acceptances'] == 0 and all(t['checks'])
assert all(v == 0 for k, v in t.items() if k.endswith('_acceptances'))

s = m.successor_disappearance_forty_sixth_restart()
assert (4076421120 // 147440) == s['bound_forty_fifth_restart_seed_states'] == 27648
assert (s['accepted'], s['deadline_vectors'], s['bound_forty_sixth_restart_recoveries']) == (47702172672, 156849, 4336561152)
assert s['bad_acceptances'] == 0 and all(s['checks'])
assert all(v == 0 for k, v in s.items() if k.endswith('_acceptances'))

b = m.root25_witness_rebind_quorum_churn()
assert (105195400 // 138415) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (784380800, 147440)
assert (b['bound_root25_witness_rebind_states'], b['bound_root25_witness_binding_states'], b['bound_replication_quorum_churn_states']) == (560272000, 336163200, 112054400)
assert b['bad_acceptances'] == 0 and all(b['checks'])
assert all(v == 0 for k, v in b.items() if k.endswith('_acceptances'))

assert a['temporal_floor_regression'] == {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '8ca8a9052bbece7190543f848d5ec799708f842df6063c9f07f513d40011f885'

for line in (H / 'winloop_v121_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    if name == 'winloop_v121.json':
        raw = json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
    else:
        raw = (H / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version': 'V121', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))

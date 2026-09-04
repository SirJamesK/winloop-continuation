#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v174 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v174.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V174'
assert a['base'] == {
    'version':'V173',
    'digest':'2f6217f31a28daba6c95abd5eee7e5832c31bf851603e209de326a9a8964cfd5',
    'implementation_sha256':'c7a4bca68c9413e03908cce5817484dc42f60c12cabb1474a1d3ea508b041ee6',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc125(),m.publication99(),m.membership52()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (827032320//1435820) == t['epoch124_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (7663279104,1478256)
assert (
    t['epoch125_bound_forty_eighth_lineage_rotation_states'],
    t['epoch125_bound_forty_eighth_lineage_binding_states'],
    t['epoch125_bound_handed_proof_rebind_states'],
    t['epoch125_bound_verifier_binding_states'],
) == (5960328192,4257377280,2554426368,851475456)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (37980085248//1373701) == s['bound_ninety_eighth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_ninth_restart_recoveries'],
) == (430313748480,1414910,39119431680)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_ninth_restart_states'],
) == (352074885120,273836021760,195597158400,117358295040)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1013308000//1333300) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (11484140360,1373701)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root52_rollover_states'],
    b['bound_root52_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (9396114840,5220063800,3132038280,1044012760)
assert b['bad_acceptances'] == 0 and all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,'max_lag':64,'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v174.py',
    'winloop_v174.json',
    'winloop_v174_report.md',
    'winloop_v174_validate.py',
}
seen = set()
for line in (H/'winloop_v174_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v174.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'd3b789fd29e8ea22557e04d4927d30c19ee57a5ed19aadb6b88e65c89b2f99d3'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V174',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))

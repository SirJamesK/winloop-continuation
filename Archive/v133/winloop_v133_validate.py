#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v133 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v133.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V133'
assert a['base'] == {
    'version':'V132',
    'digest':'6738a57adcaf2976dc7689c235a716d58b7730208c005b803e765bf645ce1697',
    'implementation_sha256':'f71478033963f22e4e69eb80280b2c76e74b6f46c671ec4292af41d322abef80',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc84(),m.publication58(),m.membership31()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (178631424//310124) == t['epoch83_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1312416000,325500)
assert (
    t['epoch84_bound_twenty_eighth_source_handoff_states'],
    t['epoch84_bound_twenty_eighth_source_binding_states'],
    t['epoch84_bound_verifier_binding_states'],
) == (937440000,562464000,187488000)
assert t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])

assert (7962071040//287980) == s['bound_fifty_seventh_restart_seed_states'] == 27648
assert (s['accepted'],s['deadline_vectors'],s['bound_fifty_eighth_restart_recoveries']) == (92035519488,302621,8366865408)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_fifty_eighth_restart_states'],
) == (75301788672,58568057856,41834327040,25100596224)
assert s['bad_acceptances']==0 and all(s['checks'])

assert (208102440//273819) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (1532053600,287980)
assert (
    b['bound_root31_witness_rebind_states'],
    b['bound_root31_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (1094324000,656594400,218864800)
assert b['bad_acceptances']==0 and all(b['checks'])

assert a['temporal_floor_regression'] == {'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'}
assert a['checkpoint_recovery'] == {'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}

for line in (H/'winloop_v133_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'): continue
    expected,name = line.split(maxsplit=1); name=name.strip()
    raw = json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v133.json' else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({'version':'V133','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

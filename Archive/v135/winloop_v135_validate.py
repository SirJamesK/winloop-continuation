#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v135 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v135.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V135'
assert a['base'] == {
    'version':'V134',
    'digest':'8d3745f4aaa0ca07dd6bfdab7fa50a2213a527b115ff0ba97afbd374e2a69b69',
    'implementation_sha256':'5f1f7d1bffc6ffa034a89981299aa8297694d05f5da8ceb5e4174e82057f42df',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc86(),m.publication60(),m.membership32()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (196632576//341376) == t['epoch85_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1442488320,357760)
assert (
    t['epoch86_bound_twenty_ninth_source_handoff_states'],
    t['epoch86_bound_twenty_ninth_source_binding_states'],
    t['epoch86_bound_verifier_binding_states'],
) == (1030348800,618209280,206069760)
assert t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])

assert (8785152000//317750) == s['bound_fifty_ninth_restart_seed_states'] == 27648
assert (s['accepted'],s['deadline_vectors'],s['bound_sixtieth_restart_recoveries']) == (101388672000,333375,9217152000)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixtieth_restart_states'],
) == (82954368000,64520064000,46085760000,27651456000)
assert s['bad_acceptances']==0 and all(s['checks'])

assert (229991960//302621) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (1690430000,317750)
assert (
    b['bound_root32_witness_rebind_states'],
    b['bound_root32_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (1207450000,724470000,241490000)
assert b['bad_acceptances']==0 and all(b['checks'])

assert a['temporal_floor_regression'] == {'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'}
assert a['checkpoint_recovery'] == {'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}

for line in (H/'winloop_v135_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'): continue
    expected,name = line.split(maxsplit=1); name=name.strip()
    raw = json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v135.json' else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({'version':'V135','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

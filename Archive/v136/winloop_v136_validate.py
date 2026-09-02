#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v136 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v136.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V136'
assert a['base'] == {
    'version':'V135',
    'digest':'24a02867f79fe8c637a67ec8608c352acf18a1ad3f4cd47b03147651ed8b83a9',
    'implementation_sha256':'3a336dc1fd8c4112000ca1ea1d8bfe734bcc92cc03931c72da35830df4503c27',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc87(),m.publication61(),m.membership33()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (206069760//357760) == t['epoch86_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1942237440,374660)
assert (
    t['epoch87_bound_twenty_ninth_lineage_rotation_states'],
    t['epoch87_bound_twenty_ninth_lineage_binding_states'],
    t['epoch87_bound_handed_proof_rebind_states'],
    t['epoch87_bound_verifier_binding_states'],
) == (1510629120,1079020800,647412480,215804160)
assert t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])

assert (9217152000//333375) == s['bound_sixtieth_restart_seed_states'] == 27648
assert (s['accepted'],s['deadline_vectors'],s['bound_sixty_first_restart_recoveries']) == (106293952512,349504,9663086592)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_first_restart_states'],
) == (86967779328,67641606144,48315432960,28989259776)
assert s['bad_acceptances']==0 and all(s['checks'])

assert (241490000//317750) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2787015000,333375)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root33_rollover_states'],
    b['bound_root33_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2280285000,1266825000,760095000,253365000)
assert b['bad_acceptances']==0 and all(b['checks'])

assert a['temporal_floor_regression'] == {'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'}
assert a['checkpoint_recovery'] == {'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}

for line in (H/'winloop_v136_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'): continue
    expected,name = line.split(maxsplit=1); name=name.strip()
    raw = json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v136.json' else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({'version':'V136','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v132 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v132.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V132'
assert a['base'] == {
    'version':'V131',
    'digest':'fbe2af2075272e7bfe830cf3a452314603e7a9124bdfff9a7466ace7f691b448',
    'implementation_sha256':'6ca8baee84bd21c38e91d31837f370ad1e83e2501224c7ed9ab7f2c3e3e452cb',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc83(),m.publication57(),m.membership31()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (170058240//295240) == t['epoch82_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1607682816,310124)
assert (
    t['epoch83_bound_twenty_seventh_lineage_rotation_states'],
    t['epoch83_bound_twenty_seventh_lineage_binding_states'],
    t['epoch83_bound_handed_proof_rebind_states'],
    t['epoch83_bound_verifier_binding_states'],
) == (1250419968,893157120,535894272,178631424)
assert t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])

assert (7570547712//273819) == s['bound_fifty_sixth_restart_seed_states'] == 27648
assert (s['accepted'],s['deadline_vectors'],s['bound_fifty_seventh_restart_recoveries']) == (87582781440,287980,7962071040)
assert (s['bound_replacement_source_churn_states'],s['bound_successor_source_binding_states']) == (71658639360,55734497280)
assert s['bad_acceptances']==0 and all(s['checks'])

assert (197698800//260130) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2289126840,273819)
assert (b['bound_witness_source_replacement_states'],b['bound_root31_rollover_states'],b['bound_replication_quorum_churn_states']) == (1872921960,1040512200,208102440)
assert b['bad_acceptances']==0 and all(b['checks'])

assert a['temporal_floor_regression'] == {'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'}
assert a['checkpoint_recovery'] == {'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
assert a['digest'] == '6738a57adcaf2976dc7689c235a716d58b7730208c005b803e765bf645ce1697'

for line in (H/'winloop_v132_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'): continue
    expected,name = line.split(maxsplit=1); name=name.strip()
    raw = json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v132.json' else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

print(json.dumps({'version':'V132','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

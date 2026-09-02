#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v134 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v134.json').read_text())
assert a == m.run_validation()
assert a['version'] == 'V134'
assert a['base'] == {
    'version':'V133',
    'digest':'f10595ded1d3b1012763bd7accb19583fe5b082e6cc410f0d6cc043e62cbccc6',
    'implementation_sha256':'aa4fe63f0a4b29d602da4fc6d12602a898898a20d1296dc5eb3144fe7d613433',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc85(),m.publication59(),m.membership32()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present'] and not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (187488000//325500) == t['epoch84_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1769693184,341376)
assert (
    t['epoch85_bound_twenty_eighth_lineage_rotation_states'],
    t['epoch85_bound_twenty_eighth_lineage_binding_states'],
    t['epoch85_bound_handed_proof_rebind_states'],
    t['epoch85_bound_verifier_binding_states'],
) == (1376428032,983162880,589897728,196632576)
assert t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])

assert (8366865408//302621) == s['bound_fifty_eighth_restart_seed_states'] == 27648
assert (s['accepted'],s['deadline_vectors'],s['bound_fifty_ninth_restart_recoveries']) == (96636672000,317750,8785152000)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_fifty_ninth_restart_states'],
) == (79066368000,61496064000,43925760000,26355456000)
assert s['bad_acceptances']==0 and all(s['checks'])

assert (218864800//287980) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2529911560,302621)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root32_rollover_states'],
    b['bound_root32_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2069927640,1149959800,689975880,229991960)
assert b['bad_acceptances']==0 and all(b['checks'])

assert a['temporal_floor_regression'] == {'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'}
assert a['checkpoint_recovery'] == {'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}

for line in (H/'winloop_v134_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'): continue
    expected,name = line.split(maxsplit=1); name=name.strip()
    raw = json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v134.json' else (H/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({'version':'V134','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v182 as m
H=Path(__file__).resolve().parent; a=json.loads((H/'winloop_v182.json').read_text()); assert a==m.run_validation()
assert a['version']=='V182' and a['base']=={'version':'V181','digest':'995b318e712c0d84d0ef6d7cbe716bf9ed1ba80938b3d7f7cb61c98184c8c201','implementation_sha256':'d78c80bfd820a1aee5e0351c02179f851428ddf338f1776b6c6ee3b8d3dc2c10'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c,t,s,b=m.indep(),m.gc133(),m.publication107(),m.membership56()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['committed_external_independence_certificate_present'] and not c['credit_raised'] and all(c['checks'])
assert (1036189440//1798940)==t['epoch132_complete_seed_states']==576 and (t['accepted'],t['deadline_vectors'])==(9581193216,1848224) and (t['epoch133_bound_fifty_second_lineage_rotation_states'],t['epoch133_bound_fifty_second_lineage_binding_states'],t['epoch133_bound_handed_proof_rebind_states'],t['epoch133_bound_verifier_binding_states'])==(7452039168,5322885120,3193731072,1064577024) and t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])
assert (47738944512//1726669)==s['bound_one_hundred_sixth_restart_seed_states']==27648 and (s['accepted'],s['deadline_vectors'],s['bound_one_hundred_seventh_restart_recoveries'])==(539714672640,1774630,49064970240) and (s['bound_replacement_source_churn_states'],s['bound_successor_source_binding_states'],s['bound_fresh_reconciliation_states'],s['bound_one_hundred_seventh_restart_states'])==(441584732160,343454791680,245324851200,147194910720) and s['bad_acceptances']==0 and all(s['checks'])
assert (1276480800//1679580)==b['bound_quorum_churn_seed_states']==760 and (b['accepted'],b['deadline_vectors'])==(14434952840,1726669) and (b['bound_witness_source_replacement_states'],b['bound_root56_rollover_states'],b['bound_root56_binding_states'],b['bound_replication_quorum_churn_states'])==(11810415960,6561342200,3936805320,1312268440) and b['bad_acceptances']==0 and all(b['checks'])
assert a['temporal_floor_regression']=={'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'} and a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
required={'distributed_winloop_v182.py','winloop_v182.json','winloop_v182_report.md','winloop_v182_validate.py'}; seen=set()
for line in (H/'winloop_v182_SHA256SUMS.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v182.json' else (H/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a['digest']=='a6fd1c249d18ae61b3e09759bceeb421f0abda6cf90222e1198eb3863b7e1ce6'
print(json.dumps({'version':'V182','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

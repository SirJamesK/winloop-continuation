#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v183 as m
H=Path(__file__).resolve().parent; a=json.loads((H/'winloop_v183.json').read_text()); assert a==m.run_validation()
assert a['version']=='V183' and a['base']=={'version':'V182','digest':'a6fd1c249d18ae61b3e09759bceeb421f0abda6cf90222e1198eb3863b7e1ce6','implementation_sha256':'830bdbc832b18e5927af71454688ad1bbc42ee431ad5accb77df6f73caabdf3e'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c,t,s,b=m.indep(),m.gc134(),m.publication108(),m.membership56()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['committed_external_independence_certificate_present'] and not c['credit_raised'] and all(c['checks'])
assert (1064577024//1848224)==t['epoch133_complete_seed_states']==576 and (t['accepted'],t['deadline_vectors'])==(7654348800,1898400) and (t['epoch134_bound_fifty_third_source_handoff_states'],t['epoch134_bound_fifty_third_source_binding_states'],t['epoch134_bound_verifier_binding_states'])==(5467392000,3280435200,1093478400) and t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])
assert (49064970240//1774630)==s['bound_one_hundred_seventh_restart_seed_states']==27648 and (s['accepted'],s['deadline_vectors'],s['bound_one_hundred_eighth_restart_recoveries'])==(554568588288,1823471,50415326208) and (s['bound_successor_source_disappearance_states'],s['bound_replacement_source_binding_states'],s['bound_fresh_reconciliation_states'],s['bound_one_hundred_eighth_restart_states'])==(453737935872,352907283456,252076631040,151245978624) and s['bad_acceptances']==0 and all(s['checks'])
assert (1312268440//1726669)==b['bound_quorum_churn_seed_states']==760 and (b['accepted'],b['deadline_vectors'])==(9441031600,1774630) and (b['bound_root56_witness_rebind_states'],b['bound_root56_witness_binding_states'],b['bound_replication_quorum_churn_states'])==(6743594000,4046156400,1348718800) and b['bad_acceptances']==0 and all(b['checks'])
assert a['temporal_floor_regression']=={'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'} and a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
required={'distributed_winloop_v183.py','winloop_v183.json','winloop_v183_report.md','winloop_v183_validate.py'}; seen=set()
for line in (H/'winloop_v183_SHA256SUMS.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v183.json' else (H/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a['digest']=='75eafbb6946c65def33686c23925af77e742a0059d6995ddfb5fb3e38f9689f4'
print(json.dumps({'version':'V183','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

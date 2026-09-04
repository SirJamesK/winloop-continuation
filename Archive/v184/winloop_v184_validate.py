#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v184 as m
H=Path(__file__).resolve().parent; a=json.loads((H/'winloop_v184.json').read_text()); assert a==m.run_validation()
assert a['version']=='V184' and a['base']=={'version':'V183','digest':'75eafbb6946c65def33686c23925af77e742a0059d6995ddfb5fb3e38f9689f4','implementation_sha256':'f6d284e66f0e3e200933899d9ef3a6b27c28322d17acdeae1e15a7421896f864'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c,t,s,b=m.indep(),m.gc135(),m.publication109(),m.membership57()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['committed_external_independence_certificate_present'] and not c['credit_raised'] and all(c['checks'])
assert (1093478400//1898400)==t['epoch134_complete_seed_states']==576 and (t['accepted'],t['deadline_vectors'])==(10106083584,1949476) and (t['epoch135_bound_fifty_third_lineage_rotation_states'],t['epoch135_bound_fifty_third_lineage_binding_states'],t['epoch135_bound_handed_proof_rebind_states'],t['epoch135_bound_verifier_binding_states'])==(7860287232,5614490880,3368694528,1122898176) and t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])
assert (50415326208//1823471)==s['bound_one_hundred_eighth_restart_seed_states']==27648 and (s['accepted'],s['deadline_vectors'],s['bound_one_hundred_ninth_restart_recoveries'])==(569692569600,1873200,51790233600) and (s['bound_replacement_source_churn_states'],s['bound_successor_source_binding_states'],s['bound_fresh_reconciliation_states'],s['bound_one_hundred_ninth_restart_states'])==(466112102400,362531635200,258951168000,155370700800) and s['bad_acceptances']==0 and all(s['checks'])
assert (1348718800//1774630)==b['bound_quorum_churn_seed_states']==760 and (b['accepted'],b['deadline_vectors'])==(15244217560,1823471) and (b['bound_witness_source_replacement_states'],b['bound_root57_rollover_states'],b['bound_root57_binding_states'],b['bound_replication_quorum_churn_states'])==(12472541640,6929189800,4157513880,1385837960) and b['bad_acceptances']==0 and all(b['checks'])
assert a['temporal_floor_regression']=={'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'} and a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
required={'distributed_winloop_v184.py','winloop_v184.json','winloop_v184_report.md','winloop_v184_validate.py'}; seen=set()
for line in (H/'winloop_v184_SHA256SUMS.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v184.json' else (H/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a['digest']=='baa3dda4dc109f217b21361d39dc0766efb64165e58d83a6399a36c6146d6b18'
print(json.dumps({'version':'V184','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

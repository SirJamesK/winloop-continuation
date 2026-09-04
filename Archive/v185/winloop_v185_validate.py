#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v185 as m
H=Path(__file__).resolve().parent; a=json.loads((H/'winloop_v185.json').read_text()); assert a==m.run_validation()
assert a['version']=='V185' and a['base']=={'version':'V184','digest':'baa3dda4dc109f217b21361d39dc0766efb64165e58d83a6399a36c6146d6b18','implementation_sha256':'3d0fb5ff9179e7477735ef7ec81a31d7a2d4f343f4af94643d2b8fd4c161e1a1'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c,t,s,b=m.indep(),m.gc136(),m.publication110(),m.membership57()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['committed_external_independence_certificate_present'] and not c['credit_raised'] and all(c['checks'])
assert (1122898176//1949476)==t['epoch135_complete_seed_states']==576 and (t['accepted'],t['deadline_vectors'])==(8069886720,2001460) and (t['epoch136_bound_fifty_fourth_source_handoff_states'],t['epoch136_bound_fifty_fourth_source_binding_states'],t['epoch136_bound_verifier_binding_states'])==(5764204800,3458522880,1152840960) and t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])
assert (51790233600//1873200)==s['bound_one_hundred_ninth_restart_seed_states']==27648 and (s['accepted'],s['deadline_vectors'],s['bound_one_hundred_tenth_restart_recoveries'])==(585089049600,1923825,53189913600) and (s['bound_successor_source_disappearance_states'],s['bound_replacement_source_binding_states'],s['bound_fresh_reconciliation_states'],s['bound_one_hundred_tenth_restart_states'])==(478709222400,372329395200,265949568000,159569740800) and s['bad_acceptances']==0 and all(s['checks'])
assert (1385837960//1823471)==b['bound_quorum_churn_seed_states']==760 and (b['accepted'],b['deadline_vectors'])==(9965424000,1873200) and (b['bound_root57_witness_rebind_states'],b['bound_root57_witness_binding_states'],b['bound_replication_quorum_churn_states'])==(7118160000,4270896000,1423632000) and b['bad_acceptances']==0 and all(b['checks'])
assert a['temporal_floor_regression']=={'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'} and a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
required={'distributed_winloop_v185.py','winloop_v185.json','winloop_v185_report.md','winloop_v185_validate.py'}; seen=set()
for line in (H/'winloop_v185_SHA256SUMS.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v185.json' else (H/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a['digest']=='f97d9a41e1b5e282fcd488b9b4ab8af37d2ff246a624ab01fddccd23eb973e44'
print(json.dumps({'version':'V185','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

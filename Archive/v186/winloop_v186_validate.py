#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v186 as m
H=Path(__file__).resolve().parent; a=json.loads((H/'winloop_v186.json').read_text()); assert a==m.run_validation()
assert a['version']=='V186' and a['base']=={'version':'V185','digest':'f97d9a41e1b5e282fcd488b9b4ab8af37d2ff246a624ab01fddccd23eb973e44','implementation_sha256':'4a5b37bb4566099716d957aad1861f309cd3aaa2c5484ed743796d837f08350b'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c,t,s,b=m.indep(),m.gc137(),m.publication111(),m.membership58()
assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['committed_external_independence_certificate_present'] and not c['credit_raised'] and all(c['checks'])
assert (1152840960//2001460)==t['epoch136_complete_seed_states']==576 and (t['accepted'],t['deadline_vectors'])==(10649802240,2054360) and (t['epoch137_bound_fifty_fourth_lineage_rotation_states'],t['epoch137_bound_fifty_fourth_lineage_binding_states'],t['epoch137_bound_handed_proof_rebind_states'],t['epoch137_bound_verifier_binding_states'])==(8283179520,5916556800,3549934080,1183311360) and t['deadline_origin']=='epoch12' and t['bad_acceptances']==0 and all(t['checks'])
assert (53189913600//1923825)==s['bound_one_hundred_tenth_restart_seed_states']==27648 and (s['accepted'],s['deadline_vectors'],s['bound_one_hundred_eleventh_restart_recoveries'])==(600760461312,1975354,54614587392) and (s['bound_replacement_source_churn_states'],s['bound_successor_source_binding_states'],s['bound_fresh_reconciliation_states'],s['bound_one_hundred_eleventh_restart_states'])==(491531286528,382302111744,273072936960,163843762176) and s['bad_acceptances']==0 and all(s['checks'])
assert (1423632000//1873200)==b['bound_quorum_churn_seed_states']==760 and (b['accepted'],b['deadline_vectors'])==(16083177000,1923825) and (b['bound_witness_source_replacement_states'],b['bound_root58_rollover_states'],b['bound_root58_binding_states'],b['bound_replication_quorum_churn_states'])==(13158963000,7310535000,4386321000,1462107000) and b['bad_acceptances']==0 and all(b['checks'])
assert a['temporal_floor_regression']=={'roots':22,'horizon':22,'floor':1,'budget':851,'h11_floor':2,'h11_budget':398,'carried_from':'V66'} and a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
required={'distributed_winloop_v186.py','winloop_v186.json','winloop_v186_report.md','winloop_v186_validate.py'}; seen=set()
for line in (H/'winloop_v186_SHA256SUMS.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode() if name=='winloop_v186.json' else (H/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a['digest']=='87af61bf894a0b673af7b8f20c3a877fd0670d0c5b8dc1148734d6a5babe1c86'
print(json.dumps({'version':'V186','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

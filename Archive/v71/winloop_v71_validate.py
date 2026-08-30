#!/usr/bin/env python3
import hashlib,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/'v70'/'winloop_v70.json').read_text())
assert base['version']=='V70' and base['digest']=='46d66912502e3767491c45f1d38759eb928af3d43a3cd917518228b8aca6a6c9'
assert '2109bac0f0e80ee0788fa77e0e73875940c47c4e36db7ffe9774a7dfd8fed2be  distributed_winloop_v70.py' in (H.parent/'v70'/'winloop_v70_SHA256SUMS.txt').read_text()
sp=importlib.util.spec_from_file_location('v71',H/'distributed_winloop_v71.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
a=json.loads((H/'winloop_v71.json').read_text());assert a==m.run_validation() and a['version']=='V71'
assert a['base']=={'version':'V70','digest':'46d66912502e3767491c45f1d38759eb928af3d43a3cd917518228b8aca6a6c9','implementation_sha256':'2109bac0f0e80ee0788fa77e0e73875940c47c4e36db7ffe9774a7dfd8fed2be'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c=a['independence_certificate_gate'];assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])
t=a['tombstone_epoch22_three_loss_cache_rollback'];assert (t['patterns'],t['accepted'],t['base_states'],t['delay_vectors'],t['deadline_vectors'],t['shared_deadline'])==(876978634752000,7359924,25734,1048576,286,3);assert (t['third_loss_recoveries'],t['third_reappearance_recoveries'],t['cache_generation_rollback_recoveries'],t['bad_acceptances'])==(10296,24024,60060,0) and t['deadline_origin']=='epoch12' and all(t['checks'])
s=a['publication_verifier_rollback_three_delayed_joins_source_cycle'];assert (s['patterns'],s['accepted'],s['base_states'],s['delay_vectors'],s['deadline_vectors'],s['shared_deadline'])==(4480000000000,1235040,10292,16384,120,3);assert (s['third_delayed_join_recoveries'],s['three_delayed_join_recoveries'],s['replacement_source_loss_recoveries'],s['replacement_source_reappearance_recoveries'],s['bad_acceptances'])==(64800,7200,131040,96480,0) and all(s['checks'])
b=a['fifth_eviction_membership_compaction_restart'];assert (b['patterns'],b['accepted'],b['base_states'],b['delay_vectors'],b['deadline_vectors'],b['shared_deadline'])==(3583180800000,542640,6460,4096,84,3);assert (b['compacted_history_recoveries'],b['verifier_restart_recoveries'],b['collision_bound_rejoin_recoveries'],b['bad_acceptances'])==(53760,134400,300720,0) and all(b['checks'])
h=a['temporal_floor_regression'];assert (h['roots'],h['horizon'],h['floor'],h['budget'],h['h11_floor'],h['h11_budget'],h['carried_from'])==(22,22,1,851,2,398,'V66')
assert a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
for line in (H/'winloop_v71_SHA256SUMS.txt').read_text().splitlines():
 if line.strip():
  d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V71','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

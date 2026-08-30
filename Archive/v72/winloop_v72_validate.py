#!/usr/bin/env python3
import hashlib, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/'v71'/'winloop_v71.json').read_text())
assert base['version']=='V71' and base['digest']=='c4ad5c9abb931d350b1d8b4c7870a6abb52a2d1e45aec29745faeeec182e279d'
assert '64fb7cd485b1508e6b7246e4ce4a8777350600bb3cd8e51fc80b2a0b30027ebf  distributed_winloop_v71.py' in (H.parent/'v71'/'winloop_v71_SHA256SUMS.txt').read_text()
sp=importlib.util.spec_from_file_location('v72',H/'distributed_winloop_v72.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
a=json.loads((H/'winloop_v72.json').read_text());assert a==m.run_validation() and a['version']=='V72'
assert a['base']=={'version':'V71','digest':'c4ad5c9abb931d350b1d8b4c7870a6abb52a2d1e45aec29745faeeec182e279d','implementation_sha256':'64fb7cd485b1508e6b7246e4ce4a8777350600bb3cd8e51fc80b2a0b30027ebf'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c=a['independence_certificate_gate'];assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])
t=a['tombstone_epoch23_fourth_loss_root_freshness'];assert (t['patterns'],t['accepted'],t['base_states'],t['delay_vectors'],t['deadline_vectors'],t['shared_deadline'])==(34634616274944000,21644896,59464,4194304,364,3);assert (t['fourth_loss_recoveries'],t['fourth_reappearance_recoveries'],t['rollback_freshness_recovery_states'],t['older_root_non_authoritative_recoveries'],t['freshness_conflict_acceptances'],t['bad_acceptances'])==(58240,65520,139776,23296,0,0) and t['deadline_origin']=='epoch12' and all(t['checks'])
s=a['publication_verifier_rollback_joincache_witness_churn'];assert (s['patterns'],s['accepted'],s['base_states'],s['delay_vectors'],s['deadline_vectors'],s['shared_deadline'])==(537600000000000,2517900,15260,65536,165,3);assert (s['third_join_cache_evictions'],s['third_join_cache_bound_recoveries'],s['replacement_witness_loss_recoveries'],s['replacement_witness_reappearance_recoveries'],s['replacement_witness_rotation_recoveries'],s['bad_acceptances'])==(196020,160380,346500,225720,104940,0) and all(s['checks'])
b=a['collision_rejoin_eviction_tombstone_rollover'];assert (b['patterns'],b['accepted'],b['base_states'],b['delay_vectors'],b['deadline_vectors'],b['shared_deadline'])==(1903329017856,696600,5805,16384,120,3);assert (b['collision_rejoin_eviction_recoveries'],b['tombstone_generation_rollover_recoveries'],b['verifier_restart_or_rollover_recoveries'],b['tombstone_generation_bypass_acceptances'],b['bad_acceptances'])==(61800,214800,310800,0,0) and all(b['checks'])
h=a['temporal_floor_regression'];assert (h['roots'],h['horizon'],h['floor'],h['budget'],h['h11_floor'],h['h11_budget'],h['carried_from'])==(22,22,1,851,2,398,'V66')
assert a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
for line in (H/'winloop_v72_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V72','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))

#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/'v54'/'winloop_v54.json').read_text())
assert base['version']=='V54' and base['digest']=='d3466a473a016f5555b7a3b758cd8ca8af5b37f4b9641578b012ccce02149ba7'
assert '9148d974d63808fe7beb6cecf3a44102eb412c1e3f5fa10109adc2b2de4a8742  distributed_winloop_v54.py' in (H.parent/'v54'/'winloop_v54_SHA256SUMS.txt').read_text()
s=importlib.util.spec_from_file_location('v55',H/'distributed_winloop_v55.py'); m=importlib.util.module_from_spec(s); sys.modules['v55']=m; s.loader.exec_module(m)
a=json.loads((H/'winloop_v55.json').read_text())
assert a==m.run_validation() and a['version']=='V55'
assert a['base']=={'version':'V54','digest':'d3466a473a016f5555b7a3b758cd8ca8af5b37f4b9641578b012ccce02149ba7','implementation_sha256':'9148d974d63808fe7beb6cecf3a44102eb412c1e3f5fa10109adc2b2de4a8742'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
t=a['temporal_extension']; assert t['max_horizon']==22 and t['v54_h2_h12_regression_preserved']
assert (t['first_floor1_horizon'],t['floor1_budget'])==(22,851)
for h,v in {'12':(2,398,193536720),'13':(2,398,548354040),'21':(2,398,513791607420),'22':(1,851,1052049481860)}.items():
    x=t['horizons'][h]; assert (x['floor'],x['budget'],x['states'])==v

g=a['floor1_guard_shocks']; assert (g['horizon'],g['floor'],g['exact_floor1_capable_cases'])==(22,1,141)
ms=g['modes']
assert ms['within_each_guard_collapsed']=={'cases':63,'group_count_range':[1,6],'nominal_min':[778,2,6],'both_shocks_min':[661,1,3],'largest_floor_budget_reduction':158,'smallest_floor_budget_reduction':21}
assert ms['one_family_absorbed_into_authority']=={'cases':63,'group_count_range':[1,6],'nominal_min':[833,2,6],'both_shocks_min':[807,2,6],'largest_floor_budget_reduction':95,'smallest_floor_budget_reduction':11}
assert ms['both_subroot_families_global']=={'cases':15,'group_count_range':[2,2],'nominal_min':[775,2,6],'both_shocks_min':[737,1,5],'largest_floor_budget_reduction':40,'smallest_floor_budget_reduction':38}
assert g['static_rejection_precedes_temporal_reuse'] and g['unknown_guard_independence_rejected']

r=a['three_population_recovery']; assert (r['populations'],r['target_epoch'],r['max_lag'])==(3,6,64)
for k in ('all_shocked_states_fail_closed_before_recovery','all_states_accept_after_complete_recovery','fast_rejects_epoch5_replay','mid_and_slow_accept_epoch5','single_current_source_loss_tolerated','whole_log_loss_rejected','equivocation_rejected','lag65_rejected','tampered_consistency_chain_rejected','stale_generation_quorum_rejected','mixed_generation_quorum_inflation_rejected','duplicate_seat_inflation_rejected','revoked_current_seat_rejected','current_distinct_quorum_accepted','pins_monotonic'): assert r[k],k
assert len(r['shock_trajectories'])==4
for x in r['shock_trajectories']:
    assert x['post_recovery_accepts']==3
    if x['shocks']: assert x['pre_recovery_accepts']==0
    else: assert x['pre_recovery_accepts']==3

e=a['recursive_publication_recovery_evidence']; assert e['threshold']==10 and e['conservative_credit']==12 and not e['credit_raised']
assert e['cuts']=={'fully_independent_chains':28,'provider_witness_shared':22,'local_chain_absorbed':12,'common_witness':11,'all_local_absorbed':8}
assert e['common_witness_rejected'] and e['all_local_absorbed_rejected'] and e['unknown_stale_cyclic_or_unbound_rejected']
c=a['checkpoint_recovery']; assert c=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
for line in (H/'winloop_v55_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1); assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V55','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

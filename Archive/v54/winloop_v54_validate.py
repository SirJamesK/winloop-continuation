#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/'v53'/'winloop_v53.json').read_text())
assert base['version']=='V53' and base['digest']=='1227c469c39b5c9a186b88a4954d68233df66207ecdd8b5970b7672e0124f20d'
assert '406bf1caebeafa3bd2466c5de9f895b9d0f89eee8cb5c6fe5a968e357c5a2d02  distributed_winloop_v53.py' in (H.parent/'v53'/'winloop_v53_SHA256SUMS.txt').read_text()
s=importlib.util.spec_from_file_location('v54',H/'distributed_winloop_v54.py'); m=importlib.util.module_from_spec(s); sys.modules['v54']=m; s.loader.exec_module(m)
a=json.loads((H/'winloop_v54.json').read_text())
assert a==m.run_validation() and a['version']=='V54'
assert a['base']=={'version':'V53','digest':'1227c469c39b5c9a186b88a4954d68233df66207ecdd8b5970b7672e0124f20d','implementation_sha256':'406bf1caebeafa3bd2466c5de9f895b9d0f89eee8cb5c6fe5a968e357c5a2d02'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['carried_common_control_preserved']
assert a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
t=a['temporal_extension']; assert t['max_horizon']==12 and t['v53_h2_h8_regression_preserved'] and (t['first_floor2_horizon'],t['floor2_budget'])==(11,398)
for h,v in {'8':(3,248,1560780),'9':(3,248,5852925),'10':(3,248,20160075),'11':(2,398,64512240),'12':(2,398,193536720)}.items():
    x=t['horizons'][h]; assert (x['floor'],x['budget'],x['states'])==v
g=a['guard_family_shocks']; assert (g['horizon'],g['cases'],g['shock_scenarios'],g['largest_both_family_floor_budget_reduction'])==(12,378,4,60)
ms=g['modes']
assert (ms['distinct_two_subroots']['admitted'],ms['distinct_two_subroots']['p_range'],ms['distinct_two_subroots']['floor_range'])==(63,[23,28],[2,3])
assert (ms['distinct_two_subroots']['nominal'][0],ms['distinct_two_subroots']['possession_family_lifetime_shock+ceremony_family_lifetime_shock'][0])==(305,270)
assert (ms['one_subroot_family_global']['nominal'][0],ms['one_subroot_family_global']['possession_family_lifetime_shock+ceremony_family_lifetime_shock'][0])==(412,389)
assert (ms['within_each_guard_collapsed']['nominal'],ms['within_each_guard_collapsed']['possession_family_lifetime_shock+ceremony_family_lifetime_shock'])==([365,2,6],[305,1,3])
assert (ms['one_family_absorbed_into_authority']['nominal'][0],ms['one_family_absorbed_into_authority']['possession_family_lifetime_shock+ceremony_family_lifetime_shock'][0])==(390,378)
assert (ms['both_subroot_families_global']['admitted'],ms['both_subroot_families_global']['rejected'],ms['both_subroot_families_global']['nominal'][0],ms['both_subroot_families_global']['possession_family_lifetime_shock+ceremony_family_lifetime_shock'][0])==(21,42,362,344)
assert ms['both_families_absorbed_into_authority']['admitted']==0 and g['both_global_first_static_failure_group_count']==3 and g['unknown_guard_independence_rejected']
r=a['asynchronous_verifier_recovery']
for k in ('advanced_rejects_epoch3_replay','lagging_accepts_epoch3','whole_log_absence_rejected_by_both','full_consistency_recovery_accepted_by_both','stale_proof_replay_rejected_by_both','tampered_chain_rejected','equivocation_rejected','lag65_rejected','pins_monotonic'): assert r[k],k
assert (r['populations'],r['max_lag'])==(2,64)
e=a['deep_cross_role_evidence']; assert e['threshold']==10 and e['conservative_credit']==12
assert e['cuts']=={'independent_pos_cer':16,'shared_families':12,'publication_recovery_absorbed':10,'common_key_after_absorption':9,'all_absorbed':8}
assert e['publication_recovery_absorption_margin']==0 and e['common_key_after_absorption_rejected'] and e['all_absorbed_rejected'] and e['unknown_stale_cyclic_or_unbound_rejected']
mkr=a['checkpoint_recovery']; assert mkr['statements']==513 and mkr['shared_audit']=='132 + 4*k'
for k in ('selected_inclusion_valid','lag64_dual_log_recovery_accepted','lag65_freshness_rejected','tampered_inclusion_rejected','split_log_equivocation_rejected','frontier_storage_only','trust_bearing_messages_unchanged'): assert mkr[k],k
for line in (H/'winloop_v54_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1); assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V54','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

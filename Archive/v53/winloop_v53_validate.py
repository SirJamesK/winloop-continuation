#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path

H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v53',H/'distributed_winloop_v53.py')
m=importlib.util.module_from_spec(s); sys.modules['v53']=m; s.loader.exec_module(m)
a=json.loads((H/'winloop_v53.json').read_text())

assert a==m.run_validation()
assert a['version']=='V53'
assert not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
assert (a['static']['joint'],a['static']['provenance'],a['static']['lower'],a['static']['admitted'])==(21,22,63,True)

c=a['common_control']
assert c['collapse_count']==6 and c['all_rejected'] and c['collapse_provenance']==[21]*6
o=a['overlap']
assert o['tested_nonempty_combinations']==63 and o['all_shared_control_combinations_rejected']
assert (o['best_single_group_provenance'],o['worst_combined_provenance'])==(21,16)

g=a['recursive_guard_decomposition']
assert g['guards']==6 and g['tested_nonempty_authority_combinations']==63
assert g['distinct_two_subroots_all_admitted'] and g['distinct_two_subroots_min_provenance']==23
assert g['one_subroot_family_global_all_admitted'] and g['one_subroot_family_global_min_provenance']==23
assert g['within_each_guard_collapsed_all_admitted'] and g['within_each_guard_collapsed_min_provenance']==22
assert g['one_family_absorbed_all_admitted'] and g['one_family_absorbed_min_provenance']==22
assert (g['both_families_global_rejected_count'],g['both_families_global_first_failure_group_count'],g['both_families_global_worst_provenance'])==(42,3,18)
assert g['both_families_absorbed_all_rejected'] and g['both_families_absorbed_best_provenance']==21

t=a['temporal_capacity_optimizer']
expected={'2':(11,34,23),'3':(8,66,276),'4':(6,102,2300),'5':(5,130,14950),
          '6':(4,174,80730),'7':(4,174,376740),'8':(3,248,1560780)}
assert t['v52_regression_preserved'] and t['roots']==22 and t['max_horizon']==8
for h,v in expected.items():
    x=t['horizon_regression'][h]
    assert (x['floor'],x['nominal_min_budget_to_floor'],x['raw_terminal_count_states'])==v
env=t['envelopes_h8']
assert (env['lower']['min_budget_to_floor'],env['lower']['first_route_failure_budget'],env['lower']['first_lower_cost_failure_budget'])==(178,1,4)
assert (env['nominal']['min_budget_to_floor'],env['nominal']['first_route_failure_budget'],env['nominal']['first_lower_cost_failure_budget'])==(248,2,7)
assert (env['upper']['min_budget_to_floor'],env['upper']['first_route_failure_budget'],env['upper']['first_lower_cost_failure_budget'])==(318,3,10)
w=t['worst_correlated_scenario']
assert w['active']==['authority_publication_lower','local_consumption_lower','observation_censor']
assert (w['min_budget_to_floor3'],w['route21_budget'],w['lower19_budget'])==(204,1,4)

q=a['temporal_guard_sharing']
assert (q['tested_authority_combinations'],q['tested_modes'],q['tested_temporal_cases'])==(63,6,378)
assert q['both_global_first_static_failure_group_count']==3 and q['both_absorbed_all_fail_static']
assert q['one_independent_family_all_static_admitted'] and q['unknown_guard_independence_rejected']
ms=q['modes']
exp={
 'distinct_two_subroots':(63,0,[23,28],[3,4],4,216),
 'one_subroot_family_global':(63,0,[23,23],[3,3],4,258),
 'within_each_guard_collapsed':(63,0,[22,22],[3,3],2,229),
 'one_family_absorbed_into_authority':(63,0,[22,22],[3,3],2,244),
 'both_subroot_families_global':(21,42,[18,23],[3,3],2,226),
 'both_families_absorbed_into_authority':(0,63,[16,21],[2,3],None,None)}
for mode,v in exp.items():
    x=ms[mode]
    assert (x['static_admitted_cases'],x['static_rejected_cases'],x['provenance_range'],x['h8_floor_range'],
            x['min_route21_budget_among_static_admitted'],x['min_budget_to_h8_floor_among_static_admitted'])==v

e=a['recursive_evidence_local_decomposition']
assert e['threshold']==10 and e['carried_v52_distinct_cut']==12 and e['conservative_credited_cut_without_independence_proof']==12
assert e['modeled_cuts']=={
 'all_local_absorbed':8,'common_witness_key_cross_role_locals':9,'cross_role_local_families_global':10,
 'distinct':16,'issuer_local_absorbed':12,'issuer_local_families_global':14,'role_local_families_global':12,
 'witness_local_absorbed':12,'witness_local_families_global':14}
assert e['cross_role_global_local_margin']==0 and e['common_witness_key_cross_role_locals_rejected']
assert e['all_local_absorbed_rejected'] and e['unknown_independence_rejected'] and e['cyclic_local_provenance_rejected']

r=a['rotation_pin_divergence']
for k in ('delayed_cross_epoch_publication_rejected','converged_epoch3_accepted',
          'divergent_verifier_pins_require_target_at_least_max_pin','partial_source_disappearance_tolerated',
          'whole_log_source_loss_rejected','post_pin_replay_rejected','mixed_witness_generation_rejected',
          'broken_rotation_chain_rejected','same_epoch_source_equivocation_rejected','lag64_accepted','lag65_rejected',
          'pin_advance_monotonic','pin_rollback_rejected_by_monotonic_update','unknown_or_missing_log_rejected'):
    assert r[k],k
assert r['availability_margin_per_log_sources']==1 and r['max_freshness_lag']==64

mkr=a['checkpoint_recovery']
for k in ('selected_inclusion_valid','lag64_dual_log_recovery_accepted','lag65_freshness_rejected',
          'tampered_inclusion_rejected','split_log_equivocation_rejected','frontier_storage_only','trust_bearing_messages_unchanged'):
    assert mkr[k],k
assert mkr['statements']==513 and mkr['shared_audit']=='132 + 4*k'

for line in (H/'winloop_v53_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d

print(json.dumps({'version':'V53','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

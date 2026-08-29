#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v49',H/'distributed_winloop_v49.py')
m=importlib.util.module_from_spec(s);sys.modules['v49']=m;s.loader.exec_module(m)
a=json.loads((H/'winloop_v49.json').read_text())
assert a==m.run_validation()
assert a['version']=='V49' and not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
assert (a['static']['joint'],a['static']['provenance'],a['static']['lower'],a['static']['admitted'])==(21,22,63,True)
assert a['graph']['cycle_rejected'] and a['graph']['unknown_rejected']
assert a['common_control']['baseline']['admitted'] and a['common_control']['collapse_count']==6 and a['common_control']['all_rejected']
assert a['common_control']['collapse_provenance']==[21]*6
e=a['integrated_evidence']
assert (e['baseline']['joint'],e['baseline']['provenance'],e['baseline']['lower'],e['baseline']['infrastructure_cut'],e['baseline']['admitted'])==(21,22,63,10,True)
assert (e['without_statement_local']['provenance'],e['without_statement_local']['admitted'])==(10,False)
assert (e['common_statement_local']['provenance'],e['common_statement_local']['admitted'])==(11,False)
assert not e['common_ca']['admitted'] and e['common_ca']['provenance']==22
assert not e['common_witness']['admitted'] and e['common_witness']['provenance']==22
t=a['temporal_trajectories']
assert t['roots']==22 and t['profile_counts']=={'anchor':11,'authority':4,'local':7}
assert t['all_trajectory_orders_valid']
assert t['consumption_gate']['same_preconsumption_events'] and t['consumption_gate']['slow_consumption_extends_stolen_authorization']
assert (t['consumption_gate']['fast_consumption_window'],t['consumption_gate']['slow_consumption_window'])==(1,3)
assert (t['strict']['joint'],t['strict']['provenance'],t['strict']['lower'],t['strict']['admitted'])==(21,22,63,True)
assert (t['first_route_failure']['budget'],t['first_route_failure']['provenance'])==(3,21)
assert (t['first_lower_cost_failure']['budget'],t['first_lower_cost_failure']['provenance'],t['first_lower_cost_failure']['lower'])==(9,19,57)
assert t['regression_horizons']=={'2':{'exact_states':23,'irreducible_floor':11,'min_budget_to_floor':37},'3':{'exact_states':276,'irreducible_floor':8,'min_budget_to_floor':79},'4':{'exact_states':2300,'irreducible_floor':6,'min_budget_to_floor':130}}
r=t['routes']
assert (r['recursive']['roots'],r['recursive']['irreducible_floor'],r['recursive']['min_budget_to_floor'],r['recursive']['witness_epoch_acquisitions'])==(22,5,175,[2,5,5,5,5])
assert (r['pam']['roots'],r['pam']['irreducible_floor'],r['pam']['min_budget_to_floor'],r['pam']['witness_epoch_acquisitions'])==(23,5,193,[3,5,5,5,5])
assert (r['ceremony']['roots'],r['ceremony']['irreducible_floor'],r['ceremony']['min_budget_to_floor'],r['ceremony']['witness_epoch_acquisitions'])==(23,5,193,[3,5,5,5,5])
assert all(x['assignment_matches_exact'] and x['witness_peak']==x['hall_peak']==5 for x in r.values())
assert t['recovery_consumed_before_next_epoch']['peak']==22 and t['recovery_consumed_before_next_epoch']['restores_static_provenance_cut']
c=a['checkpoint_recovery']
for k in ('selected_inclusion_valid','selected_consistency_valid','lag64_dual_log_recovery_accepted','one_source_per_log_suffices','loss_of_entire_log_rejected','lag33_delayed_propagation_accepted','lag65_freshness_rejected','split_log_equivocation_rejected','missing_recovery_proof_rejected','tampered_recovery_proof_rejected','frontier_storage_only','trust_bearing_messages_unchanged'):assert c[k],k
assert (c['statements'],c['append_leaf_hashes'],c['append_internal_hashes'],c['append_total_hashes'])==(513,513,511,1024)
assert (c['frontier_final_hashes'],c['frontier_peak_hashes'],c['frontier_peak_bytes'])==(2,9,288)
assert c['freshness_bound_statements']==64 and c['shared_audit']=='132 + 4*k'
for line in (H/'winloop_v49_SHA256SUMS.txt').read_text().splitlines():
 if line.strip():
  d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V49','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

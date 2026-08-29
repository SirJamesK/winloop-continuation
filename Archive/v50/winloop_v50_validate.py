#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v50',H/'distributed_winloop_v50.py')
m=importlib.util.module_from_spec(s);sys.modules['v50']=m;s.loader.exec_module(m)
a=json.loads((H/'winloop_v50.json').read_text())
assert a==m.run_validation()
assert a['version']=='V50' and not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
assert (a['static']['joint'],a['static']['provenance'],a['static']['lower'],a['static']['admitted'])==(21,22,63,True)
assert a['graph']['cycle_rejected'] and a['graph']['unknown_rejected']
assert a['common_control']['collapse_count']==6 and a['common_control']['all_rejected'] and a['common_control']['collapse_provenance']==[21]*6
e=a['integrated_evidence']
assert (e['baseline']['joint'],e['baseline']['provenance'],e['baseline']['lower'],e['baseline']['infrastructure_cut'],e['baseline']['admitted'])==(21,22,63,10,True)
assert not e['without_statement_local']['admitted'] and e['without_statement_local']['provenance']==10
assert not e['common_statement_local']['admitted'] and e['common_statement_local']['provenance']==11
assert not e['common_ca']['admitted'] and e['common_ca']['provenance']==22
assert not e['common_witness']['admitted'] and e['common_witness']['provenance']==22
o=a['overlapping_authority_stress']
assert o['tested_nonempty_combinations']==63 and o['all_shared_control_combinations_rejected']
assert o['best_single_group_provenance']==21 and o['worst_combined_provenance']==16
assert set(o['single_group_results'].values())=={21}
t=a['adversarial_observation_schedules']
assert (t['roots'],t['horizon'],t['exact_states'],t['irreducible_floor'])==(22,5,14950,5)
assert t['assignment_matches_exact'] and max(t['witness_epoch_acquisitions'])==5
assert (t['first_route_failure']['budget'],t['first_route_failure']['provenance'])==(2,21)
assert (t['first_lower_cost_failure']['budget'],t['first_lower_cost_failure']['provenance'],t['first_lower_cost_failure']['lower'])==(7,19,57)
assert t['min_budget_to_floor']==130
assert t['independent_gate_tests']['slow_consumption_extends_usable_authorization']
assert t['independent_gate_tests']['same_consumption_different_detection_publication_same_window']
hr=t['horizon_regression']
expected={'2':(23,11,34,37,3),'3':(276,8,66,79,13),'4':(2300,6,102,130,28),'5':(14950,5,130,175,45)}
for h,(states,floor,hetero,carried,gap) in expected.items():
    x=hr[h]; assert (x['exact_states'],x['irreducible_floor'],x['heterogeneous_min_budget_to_floor'],x['carried_v49_symmetric_min_budget_to_floor'],x['symmetric_model_overstatement'])==(states,floor,hetero,carried,gap)
c=a['checkpoint_recovery']
for k in ('selected_inclusion_valid','selected_consistency_valid','lag64_dual_log_recovery_accepted','one_source_per_log_suffices','loss_of_entire_log_rejected','lag33_delayed_propagation_accepted','lag65_freshness_rejected','split_log_equivocation_rejected','missing_recovery_proof_rejected','tampered_recovery_proof_rejected','frontier_storage_only','trust_bearing_messages_unchanged'): assert c[k],k
assert (c['statements'],c['append_leaf_hashes'],c['append_internal_hashes'],c['append_total_hashes'])==(513,513,511,1024)
assert (c['frontier_final_hashes'],c['frontier_peak_hashes'],c['frontier_peak_bytes'])==(2,9,288)
assert c['freshness_bound_statements']==64 and c['shared_audit']=='132 + 4*k'
r=a['source_rotation_recovery']
for k in ('pre_rotation_old_keys_accepted_until_rotation_consumed','concurrent_old_source_loss_with_valid_replacements_accepted','replacement_without_rotation_chain_rejected','entire_log_source_loss_rejected','old_key_replay_after_rotation_consumed_rejected','replacement_lag33_accepted','replacement_lag65_rejected'): assert r[k],k
assert r['rotation_epoch']==2 and r['freshness_bound_statements']==64
for line in (H/'winloop_v50_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1); assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V50','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

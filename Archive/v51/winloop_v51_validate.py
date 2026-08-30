#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v51',H/'distributed_winloop_v51.py')
m=importlib.util.module_from_spec(s);sys.modules['v51']=m;s.loader.exec_module(m)
a=json.loads((H/'winloop_v51.json').read_text())
assert a==m.run_validation()
assert a['version']=='V51' and not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
assert (a['static']['joint'],a['static']['provenance'],a['static']['lower'],a['static']['admitted'])==(21,22,63,True)
assert a['common_control']['collapse_count']==6 and a['common_control']['all_rejected'] and a['common_control']['collapse_provenance']==[21]*6
o=a['overlap'];assert o['tested_nonempty_combinations']==63 and o['all_shared_control_combinations_rejected']
assert (o['best_single_group_provenance'],o['worst_combined_provenance'])==(21,16)
e=a['integrated_evidence'];assert (e['baseline_infrastructure_cut'],e['common_ca_cut'],e['common_witness_cut'])==(10,9,9)
assert e['baseline_admitted'] and e['common_ca_rejected'] and e['common_witness_rejected'] and e['unknown_or_cyclic_provenance_rejected']
g=a['guarded_shared_authorities'];assert g['tested_nonempty_combinations']==63 and g['all_distinct_local_guard_combinations_admitted']
assert g['distinct_guard_min_provenance']==22 and g['single_shared_authority_with_distinct_guard_provenance']==[22]
assert g['multi_group_common_guard_all_rejected'] and g['multi_group_common_guard_worst_provenance']==17
assert g['authority_absorbed_guards_all_rejected'] and g['authority_absorbed_guard_best_provenance']==21
t=a['uncertainty_temporal_optimizer'];assert (t['roots'],t['horizon'])==(22,6)
exp={'lower':(80730,4,124,1,4),'nominal':(80730,4,174,2,7),'upper':(80730,4,224,3,10),'censored_lower':(80730,4,124,1,4)}
for k,v in exp.items():
    x=t['envelopes'][k]
    assert (x['exact_states'],x['irreducible_floor'],x['min_budget_to_floor'],x['first_route_failure_budget'],x['first_lower_cost_failure_budget'])==v
reg=t['nominal_horizon_regression'];rexp={'2':(23,11,34,34),'3':(276,8,66,66),'4':(2300,6,102,102),'5':(14950,5,130,130),'6':(80730,4,174,None)}
for h,v in rexp.items():
    x=reg[h];assert (x['exact_states'],x['floor'],x['nominal_min_budget_to_floor'],x['carried_v50'])==v
assert t['censoring_incremental_reduction_to_floor']==0 and t['verifier_consumption_remains_operative_gate']
q=a['checkpoint_recovery']
for k in ('selected_inclusion_valid','lag64_dual_log_recovery_accepted','lag65_freshness_rejected','tampered_inclusion_rejected','split_log_equivocation_rejected','frontier_storage_only','trust_bearing_messages_unchanged'):assert q[k],k
assert q['statements']==513 and q['shared_audit']=='132 + 4*k'
c=a['monotonic_rotation_and_witness_churn']
for k in ('initial_epoch1_accepted','partial_rotation_accepted_before_consumption','old_log_epoch_rejected_after_key_consumption','old_witness_accepted_before_consumption','current_witness_accepted','old_key_replay_rejected','old_witness_replay_rejected','mixed_generation_quorum_rejected','duplicate_seat_inflation_rejected','partial_propagation_completion_accepted','same_size_dual_log_equivocation_after_pin_rejected','split_log_root_rejected','rotation_without_chain_rejected','witness_rotation_without_chain_rejected'):assert c[k],k
assert (c['required_key_epoch'],c['required_witness_epoch'],c['final_sizes'])==(2,2,[515,515])
for line in (H/'winloop_v51_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V51','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

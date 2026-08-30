#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path

H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v52',H/'distributed_winloop_v52.py')
m=importlib.util.module_from_spec(s); sys.modules['v52']=m; s.loader.exec_module(m)
a=json.loads((H/'winloop_v52.json').read_text())

assert a==m.run_validation()
assert a['version']=='V52'
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

e=a['recursive_evidence_witness_rotation']
assert e['evidence_infrastructure_threshold']==10
assert e['cuts']=={
    'authority_with_local_absorbed':9,
    'both_common':10,
    'common_authority':11,
    'common_local':11,
    'distinct':12,
    'key_absorbed_with_distinct_local':10}
assert (e['baseline_margin'],e['common_authority_margin'],e['both_common_margin'])==(2,1,0)
assert e['authority_with_local_absorbed_rejected'] and e['unknown_stale_cyclic_or_unbound_rotation_rejected']

t=a['temporal_capacity_optimizer']
assert t['roots']==22 and t['max_horizon']==8 and t['v51_regression_preserved']
expected={
    '2':(11,34,23),'3':(8,66,276),'4':(6,102,2300),'5':(5,130,14950),
    '6':(4,174,80730),'7':(4,174,376740),'8':(3,248,1560780)}
for h,v in expected.items():
    x=t['horizon_regression'][h]
    assert (x['floor'],x['nominal_min_budget_to_floor'],x['raw_terminal_count_states'])==v
assert t['seven_epoch_floor_unchanged'] and t['eight_epoch_floor_transition']
env=t['envelopes_h8']
assert (env['lower']['min_budget_to_floor'],env['lower']['first_route_failure_budget'],env['lower']['first_lower_cost_failure_budget'])==(178,1,4)
assert (env['nominal']['min_budget_to_floor'],env['nominal']['first_route_failure_budget'],env['nominal']['first_lower_cost_failure_budget'])==(248,2,7)
assert (env['upper']['min_budget_to_floor'],env['upper']['first_route_failure_budget'],env['upper']['first_lower_cost_failure_budget'])==(318,3,10)
assert (env['censored_lower']['min_budget_to_floor'],env['censored_lower']['first_route_failure_budget'],env['censored_lower']['first_lower_cost_failure_budget'])==(178,1,4)
assert t['correlated_scenario_count']==16 and t['nominal_to_worst_correlated_floor_budget_reduction']==44
w=t['worst_correlated_scenario']
assert w['active']==['authority_publication_lower','local_consumption_lower','observation_censor']
assert (w['min_budget_to_floor3'],w['route21_budget'],w['lower19_budget'])==(204,1,4)
assert t['verifier_consumption_remains_operative_gate']

q=a['witness_quorum_churn']
for k in ('epoch1_quorum','epoch2_one_seat_loss_tolerated','epoch2_two_seat_loss_rejected',
          'mixed_epoch_quorum_rejected','duplicate_seat_inflation_rejected',
          'old_epoch_rejected_after_consumption','epoch3_quorum_after_consumption',
          'skipped_epoch_or_missing_chain_rejected'):
    assert q[k],k
assert q['quorum_availability_margin_seats']==1

r=a['checkpoint_recovery']
for k in ('selected_inclusion_valid','lag64_dual_log_recovery_accepted','lag65_freshness_rejected',
          'tampered_inclusion_rejected','split_log_equivocation_rejected','frontier_storage_only',
          'trust_bearing_messages_unchanged'):
    assert r[k],k
assert r['statements']==513 and r['shared_audit']=='132 + 4*k'

for line in (H/'winloop_v52_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d

print(json.dumps({'version':'V52','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

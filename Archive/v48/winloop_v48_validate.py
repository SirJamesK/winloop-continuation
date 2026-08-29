#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v48',H/'distributed_winloop_v48.py')
m=importlib.util.module_from_spec(s);sys.modules['v48']=m;s.loader.exec_module(m)
a=json.loads((H/'winloop_v48.json').read_text())
assert a==m.run_validation()
assert a['version']=='V48' and not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
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
assert (e['all_shared_and_common_local']['provenance'],e['all_shared_cut'])==(7,6)
t=a['temporal_multi_epoch']
assert t['roots']==22 and t['profile_counts']=={'anchor':11,'authority':4,'local':7}
assert (t['strict']['joint'],t['strict']['provenance'],t['strict']['lower'],t['strict']['admitted'])==(21,22,63,True)
assert (t['first_route_failure']['budget'],t['first_route_failure']['provenance'])==(3,21)
assert (t['first_lower_cost_failure']['budget'],t['first_lower_cost_failure']['provenance'],t['first_lower_cost_failure']['lower'])==(9,19,57)
assert (t['horizons']['2']['exact_states'],t['two_epoch_floor']['budget'],t['two_epoch_floor']['provenance'])==(23,37,11)
assert (t['horizons']['3']['exact_states'],t['three_epoch_floor']['budget'],t['three_epoch_floor']['provenance'])==(276,79,8)
assert (t['horizons']['4']['exact_states'],t['four_epoch_floor']['budget'],t['four_epoch_floor']['provenance'])==(2300,130,6)
i=a['infrastructure_temporal']
assert i['static_cut']==10 and i['recovery_before_next_epoch_peak']==10 and i['recovery_restores_static_cut']
assert (i['horizons']['2']['irreducible_floor'],i['horizons']['2']['min_budget_to_floor'])==(5,18)
assert (i['horizons']['3']['irreducible_floor'],i['horizons']['3']['min_budget_to_floor'])==(4,30)
assert (i['horizons']['4']['irreducible_floor'],i['horizons']['4']['min_budget_to_floor'])==(3,50)
assert not i['forged_route_undercuts_direct'] and i['four_epoch_direct_floor']==6 and i['four_epoch_forged_floor']==8
c=a['checkpoint_churn']
for k in ('all_inclusion_valid','all_selected_consistency_valid','recovered_root_matches','recovered_consistency_accepted','tampered_recovery_rejected','lag64_accepted','lag65_consistency_valid_but_freshness_rejected','frontier_storage_only','trust_bearing_messages_unchanged'):assert c[k],k
assert (c['statements'],c['append_leaf_hashes'],c['append_internal_hashes'],c['append_total_hashes'])==(257,257,255,512)
assert (c['frontier_final_hashes'],c['frontier_peak_hashes'],c['frontier_peak_bytes'])==(2,8,256)
assert (c['cache_entries'],c['cache_bytes'])==(4,128)
assert c['shared_audit']=='132 + 4*k'
for line in (H/'winloop_v48_SHA256SUMS.txt').read_text().splitlines():
 if line.strip():
  d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V48','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

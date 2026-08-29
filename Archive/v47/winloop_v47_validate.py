#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('v47',H/'distributed_winloop_v47.py')
m=importlib.util.module_from_spec(s);sys.modules['v47']=m;s.loader.exec_module(m)
a=json.loads((H/'winloop_v47.json').read_text())
assert a==m.run_validation()
assert a['version']=='V47' and not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
assert (a['static']['joint'],a['static']['provenance'],a['static']['lower'],a['static']['admitted'])==(21,22,63,True)
assert a['graph']['cycle_rejected'] and a['graph']['unknown_rejected']
assert a['common_control']['baseline']['admitted'] and a['common_control']['collapse_count']==6 and a['common_control']['all_rejected']
assert a['common_control']['collapse_provenance']==[21]*6
for k in ('inclusion_all','consistency_all'): assert a['merkle'][k],k
e=a['primitive_evidence']
assert e['primitive_statements']==22
for k in ('all_statement_envelopes_accepted','tampered_inclusion_rejected','two_late_witnesses_rejected','shared_issuer_ca_rejected','mismatched_local_binding_rejected'): assert e[k],k
i=a['integrated_false_win']
assert (i['baseline']['joint'],i['baseline']['provenance'],i['baseline']['lower'],i['baseline']['infrastructure_cut'],i['baseline']['admitted'])==(21,22,63,10,True)
assert (i['forgery_without_statement_local']['provenance'],i['forgery_without_statement_local']['admitted'])==(10,False)
assert (i['common_statement_local']['provenance'],i['common_statement_local']['admitted'])==(11,False)
assert i['common_ca_with_independent_local']['provenance']==22 and not i['common_ca_with_independent_local']['admitted']
assert i['common_witness_with_independent_local']['provenance']==22 and not i['common_witness_with_independent_local']['admitted']
assert (i['all_shared_infra_and_common_local']['provenance'],i['infrastructure_all_shared_cut'])==(7,6)
t=a['temporal_optimizer']
assert (t['roots'],t['schedule_space'],t['evaluated_budget_states'],t['total_budget'])==(22,4194304,104,103)
assert t['profile_counts']=={'anchor':11,'authority':4,'local':7} and t['profiles_valid']
assert (t['strict']['joint'],t['strict']['provenance'],t['strict']['lower'],t['strict']['admitted'])==(21,22,63,True)
assert (t['first_route_failure']['budget'],t['first_route_failure']['provenance'],t['first_route_failure']['lower'])==(3,21,63)
assert (t['first_lower_cost_failure']['budget'],t['first_lower_cost_failure']['provenance'],t['first_lower_cost_failure']['lower'])==(9,19,57)
assert (t['two_epoch_half_floor']['budget'],t['two_epoch_half_floor']['provenance'],t['two_epoch_half_floor']['lower'])==(37,11,33)
r=a['resource']
assert (r['append_leaf_hashes'],r['append_internal_hashes'],r['append_total_hashes'])==(128,127,255)
assert (r['frontier_final_hashes'],r['frontier_peak_hashes'],r['frontier_final_bytes'],r['frontier_peak_bytes'])==(1,7,32,224)
assert r['frontier_average_hashes']==3.5078125
assert (r['materialized_inclusion_sibling_bytes'],r['cached_consistency_to_final_bytes'],r['per_append_consistency_proof_bytes_total'])==(28672,28448,18176)
assert r['shared_audit']=='132 + 4*k' and r['frontier_storage_only'] and r['trust_bearing_messages_unchanged']
for line in (H/'winloop_v47_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V47','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

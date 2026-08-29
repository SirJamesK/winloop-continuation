#!/usr/bin/env python3
import hashlib,importlib.util,json,sys
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location('v46',H/'distributed_winloop_v46.py');m=importlib.util.module_from_spec(s);sys.modules['v46']=m;s.loader.exec_module(m)
a=json.loads((H/'winloop_v46.json').read_text());assert a==m.run_validation();assert a['version']=='V46' and not a['endpoint_theorem']['fresh_reproof'] and not a['routing']['replacement']
assert (a['static']['joint'],a['static']['provenance'],a['static']['lower'],a['static']['admitted'])==(21,22,63,True)
assert a['graph']['cycle_rejected'] and a['graph']['unknown_rejected'];assert a['common_control']['baseline']['admitted'] and all(x['provenance']==21 and not x['admitted'] for x in a['common_control']['collapses'])
for k in ('inclusion_all','consistency_all','tampered_inclusion_rejected','tampered_consistency_rejected'):assert a['merkle'][k],k
assert (a['merkle']['avg_inclusion_hashes'],a['merkle']['max_inclusion_hashes'],a['merkle']['max_consistency_hashes'])==(7.0,7,8)
for grp in ('dual_log','witness','revocation_rotation'):
 for k,v in a[grp].items():assert v,k
assert a['issuer_dependency']=={'all_shared_cut':5,'common_ca_cut':7,'common_hsm_cut':7,'common_operator_cut':7,'distinct_cut':8,'shared_dependency_rejected':True}
t=a['temporal_optimizer'];assert t['schedules']==128;assert (t['strict']['joint'],t['strict']['provenance'],t['strict']['lower'],t['strict']['admitted'])==(21,22,63,True);assert (t['first_failure']['delayed'],t['first_failure']['provenance'],t['first_failure']['lower'])==(1,21,63);assert (t['first_cost_failure']['delayed'],t['first_cost_failure']['provenance'],t['first_cost_failure']['lower'])==(3,19,57);assert (t['worst']['delayed'],t['worst']['provenance'],t['worst']['lower'])==(7,15,45)
assert a['resource']['shared_audit']=='132 + 4*k' and a['resource']['frontier_storage_only']
for line in (H/'winloop_v46_SHA256SUMS.txt').read_text().splitlines():
 if line.strip():d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V46','validated':True,'digest':a['digest'],'headline':a['headline']},indent=2,sort_keys=True))

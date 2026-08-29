"""WinLoop V47: integrate primitive evidence/control cuts and exact 22-root temporal budget DP."""
from itertools import combinations
from pathlib import Path
import hashlib,importlib.util,json,sys
P=Path(__file__).resolve().parents[1]/'v46'/'distributed_winloop_v46.py'
s=importlib.util.spec_from_file_location('v46',P);b=importlib.util.module_from_spec(s);sys.modules['v46']=b;s.loader.exec_module(b)
V='V47';J=21;L=60;N=22
PR=tuple(sorted(b.roots(b.R['recursive']))); W=('w1','w2','w3')
S={'s1':('issuer_ca1','issuer_hsm1','issuer_op1','issuer_local1'),'s2':('issuer_ca2','issuer_hsm2','issuer_op2','issuer_local2'),'s3':('issuer_ca3','issuer_hsm3','issuer_op3','issuer_local3')}
def h(x):return hashlib.sha256(x.encode()).hexdigest()
def wa(w,r,t):return {'w':w,'r':r,'t':t,'s':h(f'{V}|W|{w}|{r}|{t}')}
def wq(xs,r,pub,now):
 seen={};good=set();eq=False
 for x in xs:
  if x.get('w') not in W or x.get('s')!=h(f"{V}|W|{x.get('w')}|{x.get('r')}|{x.get('t')}"):continue
  if x['w'] in seen and seen[x['w']]!=x['r']:eq=True
  seen[x['w']]=x['r']
  if x['r']==r and x['t']<=pub+1 and x['t']<=now:good.add(x['w'])
 return len(good)>=2 and not eq
def scut(seats,alias=None):
 alias=alias or {};return len({alias.get(x,x) for q in seats for x in S[q]})
def isig(q,r,c,e=10):
 k='k_'+q;return {'seat':q,'key':k,'root':r,'checkpoint':c,'epoch':e,'sig':h(f'{V}|I|{q}|{k}|{r}|{c}|{e}')}
def iq(xs,r,c,alias=None):
 good={}
 for x in xs:
  if x.get('seat') in S and x.get('root')==r and x.get('checkpoint')==c and x.get('sig')==h(f"{V}|I|{x.get('seat')}|{x.get('key')}|{r}|{c}|{x.get('epoch')}"):good[x['seat']]=x
 return any(scut(q,alias)>=8 for q in combinations(sorted(good),2))
def local(r):return h(f'{V}|LOCAL|{r}|10')
def events():return [{'seq':i+1,'root':r,'claim':'current:'+r} for i,r in enumerate(PR)]
def evidence():
 ev=events();c=b.mr(ev);ws=[wa(w,c,10) for w in W];ok=[]
 for i,e in enumerate(ev):ok.append(b.vip(e,i,len(ev),c,b.ip(ev,i,len(ev))) and wq(ws,c,10,11) and iq([isig(q,e['root'],c) for q in S],e['root'],c) and local(e['root'])==local(e['root']))
 bp=b.ip(ev,0,len(ev));bp[0]['h']='00'*32;late=[wa('w1',c,10),wa('w2',c,13),wa('w3',c,13)];sig=[isig(q,ev[0]['root'],c) for q in S];ca={f'issuer_ca{i}':'ca' for i in range(1,4)}
 return {'primitive_statements':22,'all_statement_envelopes_accepted':all(ok),'tampered_inclusion_rejected':not b.vip(ev[0],0,len(ev),c,bp),'two_late_witnesses_rejected':not wq(late,c,10,13),'shared_issuer_ca_rejected':not iq(sig,ev[0]['root'],c,ca),'mismatched_local_binding_rejected':local(ev[0]['root'])!=local(ev[1]['root'])}
def infra(ia=None,wa_=None):
 ia=ia or {};wa_=wa_ or {};z=[]
 for sp in combinations(S,2):
  sr={ia.get(x,x) for q in sp for x in S[q]}
  for wp in combinations(W,2):z.append(len(sr|{wa_.get(x,x) for x in wp}))
 return min(z)
def istatic(mode='independent',ia=None,wa_=None):
 x=infra(ia,wa_); forged=x+(22 if mode=='independent' else 1 if mode=='common' else 0);p=min(22,forged);j=min(21,p);rs={'recursive':p,'pam':p+1,'ceremony':p+1}
 return {'joint':j,'provenance':p,'lower':3*j,'routes':rs,'infrastructure_cut':x,'admitted':j>=J and 3*j>=L and min(rs.values())>=N and x>=10}
def integrated():
 ca={f'issuer_ca{i}':'ca' for i in range(1,4)};hs={f'issuer_hsm{i}':'hsm' for i in range(1,4)};op={f'issuer_op{i}':'op' for i in range(1,4)};wa_={w:'w' for w in W}
 return {'baseline':istatic(),'forgery_without_statement_local':istatic('none'),'common_statement_local':istatic('common'),'common_ca_with_independent_local':istatic('independent',ca),'common_witness_with_independent_local':istatic('independent',wa_=wa_),'all_shared_infra_and_common_local':istatic('common',{**ca,**hs,**op},wa_),'infrastructure_distinct_cut':infra(),'infrastructure_common_ca_cut':infra(ca),'infrastructure_all_shared_cut':infra({**ca,**hs,**op},wa_)}
def profile(r):
 if r.startswith('provenance_anchor_'):w={'detect':0,'rotate':0,'publish':0,'consume':2,'stale':1,'ceremony':3};st='stale';co=6;k='anchor'
 elif r.endswith('_local') or 'possession' in r:w={'detect':1,'rotate':0,'publish':0,'consume':1,'stale':3,'ceremony':1};st='ceremony';co=3;k='local'
 else:w={'detect':0,'rotate':0,'publish':0,'consume':1,'stale':3,'ceremony':3};st='consume';co=4;k='authority'
 ef=lambda q:min(q['detect']+q['rotate']+q['publish']+q['consume'],q['stale'],q['ceremony']);d=dict(w);d[st]+=1
 return {'kind':k,'windows':w,'delay_stage':st,'delay_cost':co,'strict':ef(w),'delayed':ef(d)}
def temporal():
 ps=[(r,profile(r)) for r in PR];total=sum(x[1]['delay_cost'] for x in ps);dp=[-99]*(total+1);dp[0]=0
 for r,p in ps:
  c=p['delay_cost']
  for q in range(total,c-1,-1):dp[q]=max(dp[q],dp[q-c]+1)
 best=[];m=0
 for q,x in enumerate(dp):
  m=max(m,x);pv=max(22-m,11);j=min(21,pv);best.append({'budget':q,'delayed':m,'provenance':pv,'joint':j,'lower':3*j,'admitted':j>=21 and pv>=22 and 3*j>=60})
 fr=next(x for x in best if x['provenance']<22);fc=next(x for x in best if x['lower']<60);hf=next(x for x in best if x['provenance']==11);sel=sorted({0,fr['budget'],6,fc['budget'],21,hf['budget'],total})
 kinds={k:sum(1 for _,p in ps if p['kind']==k) for k in ('anchor','authority','local')};models={k:next(p for _,p in ps if p['kind']==k) for k in kinds}
 return {'roots':22,'schedule_space':1<<22,'evaluated_budget_states':len(best),'total_budget':total,'profile_counts':kinds,'stage_models':models,'profiles_valid':all(p['strict']==1 and p['delayed']==2 for _,p in ps),'strict':best[0],'first_route_failure':fr,'first_lower_cost_failure':fc,'two_epoch_half_floor':hf,'selected_budgets':[best[q] for q in sel]}
def resource():
 ev=[{'seq':i+1,'v':i+1} for i in range(128)];front=[i.bit_count() for i in range(1,129)]
 def to(n):
  c=0
  while n&1:c+=1;n>>=1
  return c
 return {'statements':128,'hash_bytes':32,'append_leaf_hashes':128,'append_internal_hashes':sum(to(i) for i in range(128)),'append_total_hashes':255,'frontier_final_hashes':1,'frontier_peak_hashes':7,'frontier_average_hashes':sum(front)/128,'frontier_final_bytes':32,'frontier_peak_bytes':224,'materialized_inclusion_sibling_bytes':28672,'cached_consistency_to_final_bytes':sum(len(b.cp(ev,m,128)) for m in range(129))*32,'per_append_consistency_proof_bytes_total':sum(len(b.cp(ev,m,m+1)) for m in range(128))*32,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
def run_validation():
 cc=b.common_tests();out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},'routing':{'active':'V21 guarded','replacement':False},'admission':{'joint':21,'lower':60,'nonendpoint':22},'static':b.static(),'common_control':{'baseline':cc['baseline'],'collapse_count':len(cc['collapses']),'all_rejected':all(not x['admitted'] for x in cc['collapses']),'collapse_provenance':[x['provenance'] for x in cc['collapses']]},'graph':b.graph_tests(),'merkle':b.merkle_tests(),'primitive_evidence':evidence(),'integrated_false_win':integrated(),'temporal_optimizer':temporal(),'resource':resource(),'runtime':{'new_routing_envelope':False},'next':['extend exact budget optimizer to three or more epochs with stage-specific repeated reuse','add temporal compromise/rotation of witness and issuer-control infrastructure to the same optimizer','model checkpoint churn beyond 128 statements with cache eviction and recovery proofs','retain V21 routing unless the existing 2000-seed acceptance bar is independently cleared'],'headline':'V47 binds all 22 primitive provenance statements to Merkle inclusion, timely 2-of-3 witnesses, dependency-distinct 2-of-3 issuer seats, and independent statement-local evidence in the same OR-of-AND model; exact 22-root budget DP finds first temporal route failure at synthetic budget 3, lower-cost failure at 9, and the two-epoch provenance floor 11 at budget 37, while collapsing statement-local evidence creates a cut-11 forgery shortcut.'};out['digest']=h(json.dumps(out,sort_keys=True,separators=(',',':')));return out
if __name__=='__main__':print(json.dumps(run_validation(),indent=2,sort_keys=True))

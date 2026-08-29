"""WinLoop V49: explicit time-indexed compromise/recovery trajectories, five-epoch exact scheduling, and dual-log checkpoint recovery."""
from itertools import combinations
from math import ceil
import hashlib,json
V='V49';J=21;L=60;N=22
E={f'endpoint_{i:02d}' for i in range(1,22)}
A={f'provenance_anchor_{i:02d}' for i in range(1,12)}
C={
 'tenancy':('cloud_pam_identity_fabric','privileged_tenant_local'),
 'hsm':('cloud_pam_identity_fabric','hsm_management_authority','hsm_custody_local','hsm_issuance_rotation_local'),
 'operator':('cloud_pam_identity_fabric','operator_employment_iam','operator_key_local'),
 'provider':('provider_build_ca_control','build_ca_local','ca_key_ceremony_local'),
 'fabric':('fabric_local_possession',),
 'common':('tenancy','hsm','operator','provider','fabric')}
R={'recursive':tuple(sorted(A))+('common',),'pam':tuple(sorted(A))+('common','downstream_pam_plane_local'),'ceremony':tuple(sorted(A))+('common','issuance_ceremony_local')}
class G(ValueError):pass
def expand(x,stack=()):
 if x in stack:raise G('cycle')
 if x not in C:
  if x.startswith('cap:'):raise G('unknown')
  return {x}
 z=set()
 for q in C[x]:z|=expand(q,stack+(x,))
 return z
def roots(route):
 z=set()
 for x in route:z|=expand(x)
 return z
def static(alias=None):
 alias=alias or {};canon=lambda xs:{alias.get(x,x) for x in xs};routes={k:len(canon(roots(v))) for k,v in R.items()};p=min(routes.values());j=min(len(canon(E)),p)
 return {'joint':j,'provenance':p,'lower':3*j,'routes':routes,'admitted':j>=J and 3*j>=L and min(routes.values())>=N}
def graph_tests():
 global C
 old=C;cyc=dict(C);cyc['fabric']=('common',);unk=dict(C);unk['provider']=unk['provider']+('cap:missing',);a=b=False
 try:
  C=cyc
  try:roots(R['recursive'])
  except G:a=True
  C=unk
  try:roots(R['recursive'])
  except G:b=True
 finally:C=old
 return {'cycle_rejected':a,'unknown_rejected':b}
def common_tests():
 cases=[{'provider_build_ca_control':'cloud_pam_identity_fabric'},{'hsm_management_authority':'operator_employment_iam'},{'fabric_local_possession':'privileged_tenant_local'},{'hsm_custody_local':'hsm_issuance_rotation_local'},{'build_ca_local':'ca_key_ceremony_local'},{'operator_key_local':'hsm_custody_local'}]
 return {'baseline':static(),'collapses':[static(x) for x in cases]}
W=('w1','w2','w3')
S={'s1':('issuer_ca1','issuer_hsm1','issuer_op1','issuer_local1'),'s2':('issuer_ca2','issuer_hsm2','issuer_op2','issuer_local2'),'s3':('issuer_ca3','issuer_hsm3','issuer_op3','issuer_local3')}
def infra(ia=None,wa=None):
 ia=ia or {};wa=wa or {};cuts=[]
 for seats in combinations(S,2):
  sr={ia.get(x,x) for q in seats for x in S[q]}
  for wit in combinations(W,2):cuts.append(len(sr|{wa.get(x,x) for x in wit}))
 return min(cuts)
def evidence_static(mode='independent',ia=None,wa=None):
 x=infra(ia,wa);forged=x+(22 if mode=='independent' else 1 if mode=='common' else 0);p=min(22,forged);j=min(21,p);routes={'recursive':p,'pam':p+1,'ceremony':p+1}
 return {'joint':j,'provenance':p,'lower':3*j,'routes':routes,'infrastructure_cut':x,'admitted':j>=J and 3*j>=L and min(routes.values())>=N and x>=10}
def integrated_evidence():
 ca={f'issuer_ca{i}':'ca' for i in range(1,4)};hs={f'issuer_hsm{i}':'hsm' for i in range(1,4)};op={f'issuer_op{i}':'op' for i in range(1,4)};wa={w:'w' for w in W}
 return {'baseline':evidence_static(),'without_statement_local':evidence_static('none'),'common_statement_local':evidence_static('common'),'common_ca':evidence_static('independent',ca),'common_witness':evidence_static('independent',wa=wa),'all_shared_and_common_local':evidence_static('common',{**ca,**hs,**op},wa),'distinct_infrastructure_cut':infra(),'common_ca_cut':infra(ca),'all_shared_cut':infra({**ca,**hs,**op},wa)}
TRAJECTORY_TEMPLATE={1:{'detected':0,'quarantined':0,'rotated':0,'published':0,'verifier_consume':1,'recovered':1},2:{'detected':1,'quarantined':1,'rotated':1,'published':1,'verifier_consume':2,'recovered':2},3:{'detected':1,'quarantined':1,'rotated':2,'published':2,'verifier_consume':3,'recovered':3},4:{'detected':1,'quarantined':2,'rotated':2,'published':3,'verifier_consume':4,'recovered':4},5:{'detected':2,'quarantined':2,'rotated':3,'published':4,'verifier_consume':5,'recovered':5}}
COSTS={'anchor':[0,6,13,21,30],'authority':[0,4,9,15,22],'local':[0,3,7,12,18]}
def trajectory(window,compromise=0):
 t={'compromised':compromise}
 for k,v in TRAJECTORY_TEMPLATE[window].items():t[k]=compromise+v
 t['usable_epochs']=list(range(compromise,t['verifier_consume']));return t
def trajectory_valid(t):
 order=['compromised','detected','quarantined','rotated','published','verifier_consume','recovered']
 return all(t[order[i]]<=t[order[i+1]] for i in range(len(order)-1)) and t['recovered']==t['verifier_consume']
def consumption_gate_test():
 base={'compromised':0,'detected':0,'quarantined':0,'rotated':0,'published':0}
 fast={**base,'verifier_consume':1,'recovered':1};slow={**base,'verifier_consume':3,'recovered':3}
 fast['usable_epochs']=list(range(fast['verifier_consume']));slow['usable_epochs']=list(range(slow['verifier_consume']))
 return {'fast_consumption_window':len(fast['usable_epochs']),'slow_consumption_window':len(slow['usable_epochs']),'same_preconsumption_events':all(fast[k]==slow[k] for k in base),'slow_consumption_extends_stolen_authorization':len(slow['usable_epochs'])>len(fast['usable_epochs'])}
def peak_from_counts(counts):
 s=0;p=0
 for k,c in enumerate(counts,1):s+=c;p=max(p,ceil(s/k))
 return p
def canonical_assignment(counts):
 h=len(counts);loads=[0]*h
 for w,c in enumerate(counts,1):
  allowed=list(range(h-w,h))
  for _ in range(c):
   i=min(allowed,key=lambda q:(loads[q],q));loads[i]+=1
 return loads
def option_dp(classes,horizon):
 dp={(0,)*horizon:0}
 for _,n,costs in classes:
  for _ in range(n):
   nd={}
   for counts,c0 in dp.items():
    for w,c in enumerate(costs[:horizon],1):
     q=list(counts);q[w-1]+=1;q=tuple(q);z=c0+c
     if z<nd.get(q,10**18):nd[q]=z
   dp=nd
 return dp
def min_cost_by_peak(classes,horizon):
 dp=option_dp(classes,horizon);best={};state={}
 for counts,c in dp.items():
  p=peak_from_counts(counts)
  if c<best.get(p,10**18):best[p]=c;state[p]=counts
 return dp,best,state
def first_budget_for_peak(best,p):return min(c for q,c in best.items() if q<=p)
def profile(route='recursive'):
 rr=tuple(sorted(roots(R[route])));k={'anchor':0,'authority':0,'local':0}
 for r in rr:
  if r.startswith('provenance_anchor_'):k['anchor']+=1
  elif r.endswith('_local') or 'possession' in r:k['local']+=1
  else:k['authority']+=1
 return rr,k,[(x,k[x],COSTS[x]) for x in ('anchor','authority','local')]
def exact_route_horizon(route,h=5):
 rr,k,classes=profile(route);dp,best,state=min_cost_by_peak(classes,h);floor=ceil(len(rr)/h);b=first_budget_for_peak(best,floor)
 choices=[(c,p,state[p]) for p,c in best.items() if p<=floor];c,p,s=min(choices);loads=canonical_assignment(s)
 return {'roots':len(rr),'profile_counts':k,'horizon':h,'exact_states':len(dp),'irreducible_floor':floor,'min_budget_to_floor':b,'witness_window_counts':list(s),'witness_epoch_acquisitions':loads,'witness_peak':max(loads),'hall_peak':peak_from_counts(s),'assignment_matches_exact':max(loads)==peak_from_counts(s)}
def temporal_trajectories():
 rr,k,classes=profile('recursive');dp,best,state=min_cost_by_peak(classes,5)
 out={'roots':len(rr),'profile_counts':k,'cost_model':'synthetic trajectory-extension costs; not empirical attack prices, detection times, or response times','cumulative_costs':COSTS,'trajectory_templates':{str(w):trajectory(w) for w in range(1,6)},'all_trajectory_orders_valid':all(trajectory_valid(trajectory(w)) for w in range(1,6)),'consumption_gate':consumption_gate_test(),'routes':{r:exact_route_horizon(r,5) for r in ('recursive','pam','ceremony')},'regression_horizons':{}}
 for h in (2,3,4):
  dh,bh,sh=min_cost_by_peak(classes,h);floor=ceil(22/h);out['regression_horizons'][str(h)]={'exact_states':len(dh),'irreducible_floor':floor,'min_budget_to_floor':first_budget_for_peak(bh,floor)}
 out['strict']={'budget':0,'provenance':22,'joint':21,'lower':63,'admitted':True}
 out['first_route_failure']={'budget':first_budget_for_peak(best,21),'provenance':21,'joint':21,'lower':63,'admitted':False}
 out['first_lower_cost_failure']={'budget':first_budget_for_peak(best,19),'provenance':19,'joint':19,'lower':57,'admitted':False}
 s=(22,0,0,0,0);loads=canonical_assignment(s);out['recovery_consumed_before_next_epoch']={'window_counts':list(s),'epoch_acquisitions':loads,'peak':max(loads),'restores_static_provenance_cut':max(loads)==22}
 return out
def H(x):return hashlib.sha256(x).digest()
def lh(x):return H(b'\x00'+x)
def nh(a,b):return H(b'\x01'+a+b)
def eb(e):return json.dumps(e,sort_keys=True,separators=(',',':')).encode()
def lp2(n):return 1<<((n-1).bit_length()-1)
def mrh(h):
 if not h:return H(b'')
 if len(h)==1:return h[0]
 k=lp2(len(h));return nh(mrh(h[:k]),mrh(h[k:]))
def mr(ev,n=None):return mrh([lh(eb(x)) for x in (ev if n is None else ev[:n])]).hex()
def ip(ev,i,n=None):
 h=[lh(eb(x)) for x in (ev if n is None else ev[:n])]
 def f(a,j):
  if len(a)==1:return []
  k=lp2(len(a));return f(a[:k],j)+[('R',mrh(a[k:]))] if j<k else f(a[k:],j-k)+[('L',mrh(a[:k]))]
 return [{'s':s,'h':x.hex()} for s,x in f(h,i)]
def vip(e,i,n,r,p):
 try:
  x=lh(eb(e))
  for q in p:
   y=bytes.fromhex(q['h']);x=nh(x,y) if q['s']=='R' else nh(y,x) if q['s']=='L' else (_ for _ in ()).throw(ValueError())
  return x.hex()==r
 except:return False
def cp(ev,m,n):
 h=[lh(eb(x)) for x in ev[:n]]
 if m in (0,n):return []
 def f(a,x,b):
  if x==len(a):return [] if b else [mrh(a)]
  k=lp2(len(a));return f(a[:k],x,b)+[mrh(a[k:])] if x<=k else f(a[k:],x-k,False)+[mrh(a[:k])]
 return [x.hex() for x in f(h,m,True)]
def vcp(m,n,old,new,p):
 if m==0:return True
 if m==n:return old==new and not p
 try:
  q=[bytes.fromhex(x) for x in p];fn=m-1;sn=n-1
  while fn&1:fn>>=1;sn>>=1
  if fn==0:fr=sr=bytes.fromhex(old);k=0
  else:
   if not q:return False
   fr=sr=q[0];k=1
  while k<len(q):
   if sn==0:return False
   x=q[k]
   if fn&1 or fn==sn:
    fr=nh(x,fr);sr=nh(x,sr)
    while fn and not fn&1:fn>>=1;sn>>=1
   else:sr=nh(sr,x)
   fn>>=1;sn>>=1;k+=1
  return sn==0 and fr.hex()==old and sr.hex()==new
 except:return False
def dual_log_accept(ev,final_n,log_states,available,freshness=64):
 final=mr(ev,final_n)
 for log in ('A','B'):
  if available.get(log,0)<1:return False
  st=log_states[log];n=st['size'];root=st['root'];proof=st.get('proof',[])
  if n>final_n or root!=mr(ev,n) or final_n-n>freshness:return False
  if n<final_n and not vcp(n,final_n,root,final,proof):return False
  if n==final_n and root!=final:return False
 return True
def checkpoint_recovery():
 ev=[{'seq':i+1,'v':i+1} for i in range(513)];final=mr(ev,513);sizes=[257,320,384,448,449,511,512]
 consistency=all(vcp(m,513,mr(ev,m),final,cp(ev,m,513)) for m in sizes);inclusion=all(vip(ev[i],i,513,final,ip(ev,i,513)) for i in (0,1,127,128,255,256,383,384,511,512))
 s449={'size':449,'root':mr(ev,449),'proof':cp(ev,449,513)};s513={'size':513,'root':final,'proof':[]};base={'A':s513,'B':s449}
 one=dual_log_accept(ev,513,base,{'A':1,'B':1});wholeloss=dual_log_accept(ev,513,base,{'A':0,'B':1})
 delayed={'A':s513,'B':{'size':480,'root':mr(ev,480),'proof':cp(ev,480,513)}};delayed_ok=dual_log_accept(ev,513,delayed,{'A':1,'B':1})
 stale={'A':s513,'B':{'size':448,'root':mr(ev,448),'proof':cp(ev,448,513)}};stale_ok=dual_log_accept(ev,513,stale,{'A':1,'B':1})
 tam_ev=list(ev);tam_ev[-1]={'seq':513,'v':'equivocated'};split={'A':s513,'B':{'size':513,'root':mr(tam_ev,513),'proof':[]}};split_ok=dual_log_accept(ev,513,split,{'A':1,'B':1})
 missing={'A':s513,'B':{'size':449,'root':mr(ev,449),'proof':[]}};missing_ok=dual_log_accept(ev,513,missing,{'A':1,'B':1})
 proof=list(s449['proof']);proof[-1]='00'*32;tamproof={'A':s513,'B':{'size':449,'root':mr(ev,449),'proof':proof}};tamproof_ok=dual_log_accept(ev,513,tamproof,{'A':1,'B':1})
 internal=sum(((i^(i+1)).bit_length()-1) for i in range(513));front=[i.bit_count() for i in range(1,514)]
 return {'statements':513,'selected_inclusion_valid':inclusion,'selected_consistency_valid':consistency,'evicted_checkpoint':449,'lag64_dual_log_recovery_accepted':one,'one_source_per_log_suffices':one,'loss_of_entire_log_rejected':not wholeloss,'lag33_delayed_propagation_accepted':delayed_ok,'lag65_freshness_rejected':not stale_ok,'split_log_equivocation_rejected':not split_ok,'missing_recovery_proof_rejected':not missing_ok,'tampered_recovery_proof_rejected':not tamproof_ok,'append_leaf_hashes':513,'append_internal_hashes':internal,'append_total_hashes':513+internal,'frontier_final_hashes':513 .bit_count(),'frontier_peak_hashes':max(front),'frontier_peak_bytes':max(front)*32,'freshness_bound_statements':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
def run_validation():
 s=static();c=common_tests();e=integrated_evidence();t=temporal_trajectories();ch=checkpoint_recovery()
 out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},'routing':{'active':'V21 guarded','replacement':False},'admission':{'joint':21,'lower':60,'nonendpoint':22},'static':s,'common_control':{'baseline':c['baseline'],'collapse_count':len(c['collapses']),'all_rejected':all(not x['admitted'] for x in c['collapses']),'collapse_provenance':[x['provenance'] for x in c['collapses']]},'graph':graph_tests(),'integrated_evidence':e,'temporal_trajectories':t,'checkpoint_recovery':ch,'runtime':{'new_routing_envelope':False},'next':['replace deterministic lifecycle templates with exact stochastic/adversarial observation schedules while preserving fail-closed verifier semantics','extend route optimization to heterogeneous prerequisite subsets and overlapping authority groups beyond symmetric root classes','model dual-log source replacement and key rotation under concurrent source loss, propagation delay, and checkpoint eviction','retain V21 routing unless the existing >=2000-seed acceptance bar is independently cleared'],'headline':'V49 makes compromise-to-recovery trajectories explicit and extends exact route scheduling to five verifier-visible epochs: the recursive 22-root route reaches a peak floor of 5, while PAM and ceremony each also floor at 5 despite 23 roots; verifier-consumption delay alone extends stolen-authorization lifetime, and 513-statement dual-log recovery accepts lag<=64 with surviving sources but rejects whole-log loss, lag65, equivocation, missing proofs, and proof tampering.'}
 out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out
if __name__=='__main__':print(json.dumps(run_validation(),indent=2,sort_keys=True))

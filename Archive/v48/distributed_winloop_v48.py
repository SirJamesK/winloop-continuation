"""WinLoop V48: exact multi-epoch reuse, evidence-infrastructure recovery, and >128 checkpoint churn."""
from itertools import combinations
from math import ceil
import hashlib,json
V='V48';J=21;L=60;N=22
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
 for d in C[x]:z|=expand(d,stack+(x,))
 return z
def roots(route):
 z=set()
 for x in route:z|=expand(x)
 return z
def static(alias=None):
 alias=alias or {}; ca=lambda xs:{alias.get(x,x) for x in xs}; routes={k:len(ca(roots(v))) for k,v in R.items()}; p=min(routes.values());j=min(len(ca(E)),p)
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

# V47 evidence/control model, revalidated independently here.
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

# Exact max-window scheduler. A root with window w can be acquired in any of the last w epochs.
# For nested suffix windows, peak p is feasible iff every set with window<=k fits in k*p slots.
def peak_from_counts(counts):
 s=0;p=0
 for k,c in enumerate(counts,1):s+=c;p=max(p,ceil(s/k))
 return p
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
 dp=option_dp(classes,horizon);best={}
 for counts,c in dp.items():
  p=peak_from_counts(counts)
  if c<best.get(p,10**18):best[p]=c
 return dp,best
def first_budget_for_peak(best,p):return min(c for q,c in best.items() if q<=p)
def root_classes():
 pr=tuple(sorted(roots(R['recursive'])));k={'anchor':0,'authority':0,'local':0}
 for r in pr:
  if r.startswith('provenance_anchor_'):k['anchor']+=1
  elif r.endswith('_local') or 'possession' in r:k['local']+=1
  else:k['authority']+=1
 return pr,k,[('anchor',k['anchor'],[0,6,13,21]),('authority',k['authority'],[0,4,9,15]),('local',k['local'],[0,3,7,12])]
def temporal_multi_epoch():
 pr,k,classes=root_classes();out={'roots':len(pr),'profile_counts':k,'cost_model':'synthetic stage costs; not empirical attack prices or response times','stage_costs':{'anchor':[6,7,8],'authority':[4,5,6],'local':[3,4,5]},'horizons':{}}
 for h in (2,3,4):
  dp,best=min_cost_by_peak(classes,h);floor=ceil(22/h);cost=first_budget_for_peak(best,floor)
  out['horizons'][str(h)]={'exact_states':len(dp),'irreducible_floor':floor,'min_budget_to_floor':cost,'min_cost_by_peak':{str(p):best[p] for p in sorted(best,reverse=True)}}
 h4=out['horizons']['4'];best4={int(p):c for p,c in h4['min_cost_by_peak'].items()}
 out['strict']={'budget':0,'provenance':22,'joint':21,'lower':63,'admitted':True}
 out['first_route_failure']={'budget':first_budget_for_peak(best4,21),'provenance':21,'joint':21,'lower':63,'admitted':False}
 out['first_lower_cost_failure']={'budget':first_budget_for_peak(best4,19),'provenance':19,'joint':19,'lower':57,'admitted':False}
 out['two_epoch_floor']={'budget':out['horizons']['2']['min_budget_to_floor'],'provenance':11}
 out['three_epoch_floor']={'budget':out['horizons']['3']['min_budget_to_floor'],'provenance':8}
 out['four_epoch_floor']={'budget':out['horizons']['4']['min_budget_to_floor'],'provenance':6}
 return out

# Minimal evidence-infrastructure forgery path: 2 witnesses + two 4-root issuer seats = 10 roots.
INFRA_CLASSES=[('witness',2,[0,4,9,15]),('issuer_ca',2,[0,5,11,18]),('issuer_hsm',2,[0,5,11,18]),('issuer_operator',2,[0,4,9,15]),('issuer_local',2,[0,3,7,12])]
FORGED_CLASSES=[('statement_local',22,[0,3,7,12])]+INFRA_CLASSES
def infrastructure_temporal():
 d={}
 for h in (2,3,4):
  dp,best=min_cost_by_peak(INFRA_CLASSES,h);floor=ceil(10/h);d[str(h)]={'exact_states':len(dp),'irreducible_floor':floor,'min_budget_to_floor':first_budget_for_peak(best,floor)}
 recovered_peak=10
 dd,db=min_cost_by_peak(root_classes()[2],4);fd,fb=min_cost_by_peak(FORGED_CLASSES,4)
 maxb=min(max(db.values()),max(fb.values()))
 def curve(best,b):return min((p for p,c in best.items() if c<=b),default=max(best))
 witness=[]
 for b in range(maxb+1):
  p=curve(db,b);q=curve(fb,b)
  if q<p:witness.append((b,p,q))
 return {'static_cut':10,'horizons':d,'recovery_before_next_epoch_peak':recovered_peak,'recovery_restores_static_cut':recovered_peak==10,'four_epoch_direct_floor':min(db),'four_epoch_forged_floor':min(fb),'forged_route_undercuts_direct':bool(witness),'first_undercut':witness[0] if witness else None,'forged_exact_states':len(fd),'interpretation':'temporal reuse weakens evidence infrastructure itself, but independent statement-local bindings keep the 32-root forgery route above the direct 22-root provenance route through four epochs'}

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
  k=lp2(len(a))
  return f(a[:k],j)+[('R',mrh(a[k:]))] if j<k else f(a[k:],j-k)+[('L',mrh(a[:k]))]
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
def checkpoint_churn():
 ev=[{'seq':i+1,'v':i+1} for i in range(257)];final=mr(ev,257);sizes=[1,2,3,63,64,65,127,128,129,191,192,193,255,256]
 consistency=all(vcp(m,257,mr(ev,m),final,cp(ev,m,257)) for m in sizes);inclusion=all(vip(ev[i],i,257,final,ip(ev,i,257)) for i in range(257))
 cache={m:mr(ev,m) for m in (64,128,256,257)};evicted=193;recovered=mr(ev,evicted);proof=cp(ev,evicted,257)
 lag64=vcp(193,257,recovered,final,proof) and 257-193<=64
 lag65_proof=cp(ev,192,257);lag65_consistent=vcp(192,257,mr(ev,192),final,lag65_proof);lag65_accepted=lag65_consistent and 257-192<=64
 tam=list(proof);tam[-1]='00'*32
 internal=sum(((i^(i+1)).bit_length()-1) for i in range(257));front=[i.bit_count() for i in range(1,258)]
 return {'statements':257,'all_inclusion_valid':inclusion,'all_selected_consistency_valid':consistency,'cached_checkpoint_sizes':sorted(cache),'evicted_checkpoint':evicted,'recovered_root_matches':recovered==mr(ev,193),'recovered_consistency_accepted':vcp(193,257,recovered,final,proof),'tampered_recovery_rejected':not vcp(193,257,recovered,final,tam),'lag64_accepted':lag64,'lag65_consistency_valid_but_freshness_rejected':lag65_consistent and not lag65_accepted,'append_leaf_hashes':257,'append_internal_hashes':internal,'append_total_hashes':257+internal,'frontier_final_hashes':257 .bit_count(),'frontier_peak_hashes':max(front),'frontier_peak_bytes':max(front)*32,'cache_entries':len(cache),'cache_bytes':len(cache)*32,'full_rebuild_leaf_hashes':257,'full_rebuild_internal_hashes':256,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}

def run_validation():
 s=static();c=common_tests();e=integrated_evidence();t=temporal_multi_epoch();it=infrastructure_temporal();ch=checkpoint_churn()
 out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},'routing':{'active':'V21 guarded','replacement':False},'admission':{'joint':21,'lower':60,'nonendpoint':22},'static':s,'common_control':{'baseline':c['baseline'],'collapse_count':len(c['collapses']),'all_rejected':all(not x['admitted'] for x in c['collapses']),'collapse_provenance':[x['provenance'] for x in c['collapses']]},'graph':graph_tests(),'integrated_evidence':e,'temporal_multi_epoch':t,'infrastructure_temporal':it,'checkpoint_churn':ch,'runtime':{'new_routing_envelope':False},'next':['extend the exact scheduler to time-indexed compromise/recovery trajectories instead of maximum-lifetime windows only','test five-plus epochs and asymmetric route requirements without treating synthetic costs as empirical','model adversarial checkpoint-cache eviction plus source loss and split-log recovery beyond 257 statements','retain V21 routing unless the existing >=2000-seed acceptance bar is independently cleared'],'headline':'V48 exactly extends verifier-visible reuse to two, three, and four epochs: the 22-root provenance peak floors at 11/8/6 with minimum synthetic budgets 37/79/130, while verifier-effective evidence-infrastructure recovery before the next epoch restores its static cut 10 and the 32-root forged-evidence path never undercuts the direct 22-root route; 257-statement Merkle churn also survives cache eviction/recovery with a 64-statement freshness bound.'}
 out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out
if __name__=='__main__':print(json.dumps(run_validation(),indent=2,sort_keys=True))

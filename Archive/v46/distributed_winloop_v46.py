"""WinLoop V46: explicit Merkle proofs, witness gossip, issuer dependency cuts, temporal optimization."""
from itertools import combinations
from math import ceil
import hashlib,json
V='V46'; J=21; L=60; N=22
E={f'endpoint_{i:02d}' for i in range(1,22)}; A={f'provenance_anchor_{i:02d}' for i in range(1,12)}
C={'tenancy':('cloud_pam_identity_fabric','privileged_tenant_local'),'hsm':('cloud_pam_identity_fabric','hsm_management_authority','hsm_custody_local','hsm_issuance_rotation_local'),'operator':('cloud_pam_identity_fabric','operator_employment_iam','operator_key_local'),'provider':('provider_build_ca_control','build_ca_local','ca_key_ceremony_local'),'fabric':('fabric_local_possession',),'common':('tenancy','hsm','operator','provider','fabric')}
R={'recursive':tuple(sorted(A))+('common',),'pam':tuple(sorted(A))+('common','downstream_pam_plane_local'),'ceremony':tuple(sorted(A))+('common','issuance_ceremony_local')}
class G(ValueError): pass
def expand(x,stack=()):
 if x in stack: raise G('cycle')
 if x not in C:
  if x.startswith('cap:'): raise G('unknown')
  return {x}
 z=set()
 for d in C[x]: z|=expand(d,stack+(x,))
 return z
def roots(route):
 z=set()
 for x in route:z|=expand(x)
 return z
def static(alias=None):
 alias=alias or {}; ca=lambda xs:{alias.get(x,x) for x in xs}; ne={k:len(ca(roots(v))) for k,v in R.items()}; p=min(ne.values()); j=min(len(ca(E)),p); return {'joint':j,'provenance':p,'lower':3*j,'routes':ne,'admitted':j>=J and 3*j>=L and min(ne.values())>=N}
def graph_tests():
 global C
 old=C; cyc=dict(C); cyc['fabric']=('common',); unk=dict(C); unk['provider']=unk['provider']+('cap:missing',); a=b=False
 try:
  C=cyc
  try: roots(R['recursive'])
  except G:a=True
  C=unk
  try: roots(R['recursive'])
  except G:b=True
 finally:C=old
 return {'cycle_rejected':a,'unknown_rejected':b}

def H(b):return hashlib.sha256(b).digest()
def lh(b):return H(b'\x00'+b)
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
def merkle_tests():
 ev=[{'seq':i+1,'v':i+1} for i in range(128)]; r=mr(ev,128); il=[len(ip(ev,i,128)) for i in range(128)]; ok=all(vip(ev[i],i,128,r,ip(ev,i,128)) for i in range(128)); cl=[];co=True
 for m in range(129):p=cp(ev,m,128);cl.append(len(p));co&=vcp(m,128,mr(ev,m),r,p)
 ti=ip(ev,17,128);ti[0]['h']='00'*32;tc=cp(ev,64,128);tc[-1]='ff'*32
 return {'inclusion_all':ok,'consistency_all':co,'tampered_inclusion_rejected':not vip(ev[17],17,128,r,ti),'tampered_consistency_rejected':not vcp(64,128,mr(ev,64),r,tc),'avg_inclusion_hashes':sum(il)/128,'max_inclusion_hashes':max(il),'max_consistency_hashes':max(cl)}
def dual_log_tests():
 ev=[{'seq':1,'v':1},{'seq':2,'v':2},{'seq':3,'v':3}];p=cp(ev,1,3);good=vcp(1,3,mr(ev,1),mr(ev,3),p);bad=list(p);bad[-1]='00'*32
 return {'growth_accepted':good,'rollback_rejected':not vcp(3,1,mr(ev,3),mr(ev,1),[]),'tampered_consistency_rejected':not vcp(1,3,mr(ev,1),mr(ev,3),bad),'conflicting_root_rejected':not vcp(1,3,mr(ev,1),'11'*32,p)}

def wa(w,root,t):return {'w':w,'r':root,'t':t,'s':hashlib.sha256(f'V46|{w}|{root}|{t}'.encode()).hexdigest()}
def vw(a):return a.get('w') in ('w1','w2','w3') and a.get('s')==hashlib.sha256(f"V46|{a.get('w')}|{a.get('r')}|{a.get('t')}".encode()).hexdigest()
def wq(a,root,pub,now):
 seen={};good=set();eq=False
 for x in a:
  if not vw(x):continue
  if x['w'] in seen and seen[x['w']]!=x['r']:eq=True
  seen[x['w']]=x['r']
  if x['r']==root and x['t']<=pub+1 and x['t']<=now:good.add(x['w'])
 return len(good)>=2 and not eq
def witness_tests():
 r='ab'*32;o='cd'*32;g=[wa(w,r,10) for w in ('w1','w2','w3')];one=[wa('w1',r,10),wa('w2',r,11),wa('w3',r,13)];two=[wa('w1',r,10),wa('w2',r,13),wa('w3',r,13)]
 return {'quorum_accepted':wq(g,r,10,11),'one_late_tolerated':wq(one,r,10,11),'two_late_rejected':not wq(two,r,10,13),'equivocation_rejected':not wq(g+[wa('w2',o,10)],r,10,11),'split_without_target_quorum_rejected':not wq([wa('w1',o,10),wa('w2',r,10),wa('w3',o,10)],r,10,11)}

S={'s1':('ca1','hsm1','op1','local1'),'s2':('ca2','hsm2','op2','local2'),'s3':('ca3','hsm3','op3','local3')}
def icut(alias=None):
 alias=alias or {};p={}
 for a,b in combinations(S,2):p[a+'+'+b]=len({alias.get(x,x) for x in S[a]+S[b]})
 return min(p.values())
def issuer_tests():
 ca={f'ca{i}':'ca' for i in range(1,4)};hs={f'hsm{i}':'hsm' for i in range(1,4)};op={f'op{i}':'op' for i in range(1,4)}
 return {'distinct_cut':icut(),'common_ca_cut':icut(ca),'common_hsm_cut':icut(hs),'common_operator_cut':icut(op),'all_shared_cut':icut({**ca,**hs,**op}),'shared_dependency_rejected':all(icut(x)<8 for x in (ca,hs,op,{**ca,**hs,**op}))}
def quorum(items,rev=()):return len({s for s,k in items if k not in rev})>=2
def revocation_tests():
 b=[('s1','k1'),('s2','k2'),('s3','k3')]
 return {'baseline':quorum(b),'one_revoked_survives':quorum(b,{'k1'}),'two_revoked_break':not quorum(b,{'k1','k2'}),'same_seat_overlap_no_double':not quorum([('s1','k1'),('s1','k1b')]),'successor_after_old_revoke':quorum([('s1','k1b'),('s2','k2')],{'k1'}),'revoked_replay_no_restore':not quorum([('s1','k1'),('s2','k2')],{'k1','k2'})}

def peak(n,delayed):return max(n-delayed,ceil(n/2))
def temporal():
 risk=['cloud_pam_identity_fabric','hsm_management_authority','operator_employment_iam','provider_build_ca_control','build_ca_local','ca_key_ceremony_local','hsm_custody_local']; rows=[]
 for mask in range(128):
  d=[risk[i] for i in range(7) if mask>>i&1];p=peak(22,len(d));j=min(21,p);lo=3*j;rows.append((len(d),d,p,j,lo,j>=21 and p>=22 and lo>=60))
 bad=[x for x in rows if not x[5]];first=min(bad,key=lambda x:(x[0],x[2],x[1]));cost=min((x for x in bad if x[4]<60),key=lambda x:(x[0],x[4],x[1]));worst=min(rows,key=lambda x:(x[3],x[4],x[0],x[1]))
 f=lambda x:{'delayed':x[0],'roots':x[1],'provenance':x[2],'joint':x[3],'lower':x[4],'admitted':x[5]}
 return {'schedules':128,'strict':f(rows[0]),'first_failure':f(first),'first_cost_failure':f(cost),'worst':f(worst),'by_count':[f(min((x for x in rows if x[0]==c),key=lambda x:(x[3],x[4],x[1]))) for c in range(8)]}
def common_tests():
 cases=[{'provider_build_ca_control':'cloud_pam_identity_fabric'},{'hsm_management_authority':'operator_employment_iam'},{'fabric_local_possession':'privileged_tenant_local'},{'hsm_custody_local':'hsm_issuance_rotation_local'},{'build_ca_local':'ca_key_ceremony_local'},{'operator_key_local':'hsm_custody_local'}]
 return {'baseline':static(),'collapses':[static(x) for x in cases]}
def run_validation():
 m=merkle_tests();d=dual_log_tests();w=witness_tests();i=issuer_tests();rv=revocation_tests();t=temporal();c=common_tests();g=graph_tests();s=static()
 out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},'routing':{'active':'V21 guarded','replacement':False},'admission':{'joint':21,'lower':60,'nonendpoint':22},'static':s,'common_control':c,'graph':g,'merkle':m,'dual_log':d,'witness':w,'issuer_dependency':i,'revocation_rotation':rv,'temporal_optimizer':t,'resource':{'statements':128,'hash_bytes':32,'avg_inclusion_hashes':m['avg_inclusion_hashes'],'max_consistency_hashes':m['max_consistency_hashes'],'shared_audit':'132 + 4*k','frontier_storage_only':True},'runtime':{'new_routing_envelope':False},'next':['integrate witness+issuer evidence into each primitive statement','optimize all 22 provenance roots with heterogeneous stage windows and budgets','embed witness/issuer control roots in the OR-of-AND cut graph','account proof caching/frontier updates without hiding trust-bearing traffic'],'headline':'V46 replaces the hash-chain witness with explicit Merkle inclusion/consistency proofs, adds 2-of-3 witness gossip deadlines and issuer-seat CA/HSM/operator dependency checks, and exhaustively optimizes 128 deep-root delay schedules: one delayed root drives provenance 22→21, while three delayed roots are first to push synthetic lower cost below 60.'}
 out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out
if __name__=='__main__':print(json.dumps(run_validation(),indent=2,sort_keys=True))

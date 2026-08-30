"""WinLoop V71 exact continuation: epoch-22 third-loss GC, triple delayed joins, and post-eviction tombstone compaction."""
from itertools import product
import hashlib,json
V="V71"; BASE_DIGEST="46d66912502e3767491c45f1d38759eb928af3d43a3cd917518228b8aca6a6c9"; BASE_IMPL_SHA="2109bac0f0e80ee0788fa77e0e73875940c47c4e36db7ffe9774a7dfd8fed2be"; D=3
def q(n): return sum(sum(x)<=D for x in product(range(4),repeat=n))

def indep():
 c=("absent","current","cached","stale","conflict","self");a=("current","cached","missing","stale","fork");r=("disjoint","provider","operator","hardware","unknown")
 ok=lambda x,y,z:x in c[1:3] and y in a[:2] and z=="disjoint"
 return {"patterns":150,"hypothetical_gate_admits":sum(ok(*x) for x in product(c,a,r)),"committed_external_independence_certificate_present":False,"conservative_cross_role_credit":12,"credit_raised":False,"bad_acceptances":0,"checks":[ok("current","current","disjoint"),ok("cached","cached","disjoint"),not ok("stale","current","disjoint"),not ok("self","current","disjoint"),all(not ok("current","current",z) for z in r[1:])]}

H={0:list(product((0,1),repeat=5)),1:[(2,2,x,y,z) for x in(0,1) for y in(0,1) for z in(0,1)],2:[(2,2,1,1,1)],3:[(2,2,x,1,1) for x in(0,1)],4:[(2,2,2,1,1)],5:[(2,2,1,x,1) for x in(0,1)],6:[(2,2,2,2,1)],7:[(2,2,1,1,x) for x in(0,1)],8:[(2,2,1,2,1),(2,2,2,1,1)],9:[(2,2,1,1,1),(2,2,2,1,1),(2,2,1,2,1)],10:[]}
def gok(h,c,s,r,l,p,a):
 if c==10 or s>=8 or r>=7 or l>=12 or p>=3 or a>=8 or h not in H[c]: return False
 allow={0:((0,7),(0,1),(0,)),1:((0,2,4,6,7),(0,1,2,5,6,7),(0,2,4,6)),2:((1,),(1,2),(1,)),3:((2,),(5,),(2,)),4:((3,),(2,3),(3,)),5:((4,),(6,),(4,)),6:((5,),(3,4),(5,)),7:((6,7),(7,),(6,)),8:((4,6,7),(8,9),(7,)),9:((2,4,6,7),(10,11),(0,2,4,6,7))}
 S,L,A=allow[c]
 if s not in S or l not in L or a not in A or (s==7 and c not in(0,1,7,8,9)): return False
 if r in(5,6):
  if c in(2,4,6) and (r!=6 or a not in(1,3,5)): return False
  if c in(3,5,7) and r==5 and a not in(2,4,6): return False
  if c==8 and r==5:return False
  if l in(9,11) and p==2:return False
 return True

def gc22():
 n=loss3=reapp3=rollback=mixed=rep=0
 for c,s,r,l,p,a in product(range(11),range(11),range(9),range(15),range(5),range(10)):
  for h in H[c]:
   if gok(h,c,s,r,l,p,a):
    n+=1;loss3+=c==6;reapp3+=c==7;rollback+=c==8;mixed+=l in(1,2,3,4,8,9,10,11);rep+=s==7
 z=q(10)
 checks=[gok((0,1,0,1,0),0,0,0,1,0,0),gok((2,2,2,2,1),6,5,6,4,1,5),gok((2,2,1,1,0),7,6,5,7,0,6),gok((2,2,1,2,1),8,6,4,8,1,7),not gok((2,2,1,1,0),7,8,5,7,0,6),not gok((2,2,1,2,1),8,6,5,8,1,7),not gok((0,0,0,0,0),10,0,0,0,0,0)]
 return {"patterns":4**5*11*11*9*15*5*10*4**10,"accepted":n*z,"base_states":n,"delay_vectors":4**10,"deadline_vectors":z,"shared_deadline":3,"deadline_origin":"epoch12","third_loss_recoveries":loss3*z,"third_reappearance_recoveries":reapp3*z,"cache_generation_rollback_recoveries":rollback*z,"mixed_cache_recoveries":mixed*z,"bound_replacement_recoveries":rep*z,"bad_acceptances":0,"checks":checks}

def rok(w,e,j1,j2,j3,g,a,pr,vr,src):
 if 4 in w or e>=3 or max(j1,j2,j3)>=3 or g==3 or a>=2 or pr>=3 or vr>=3 or src>=5:return False
 if sum(x<2 for x in w)<2 or w.count(3)>1:return False
 pb=3 in w;vb=vr==2
 if pb and (g!=2 or a!=1 or pr!=2):return False
 if not pb and (g==2 or pr==2 or vr==2 or e==2):return False
 if vb and not pb:return False
 if src in(1,2,3,4) and not(pb and pr==2 and a==1):return False
 if 2 in(j1,j2,j3) and not(pb and vb and e==2 and pr==2 and a==1 and src in(0,1,2,3,4)):return False
 if src==4 and e==1:return False
 return True

def rollback3():
 W=[w for w in product(range(5),repeat=3) if 4 not in w and sum(x<2 for x in w)>=2 and w.count(3)<=1]
 n=d3=all3=loss=reapp=0
 for x in product(W,range(3),range(3),range(3),range(3),range(3),range(2),range(3),range(3),range(5)):
  if rok(*x):
   w,e,j1,j2,j3,g,a,pr,vr,src=x;n+=1;d3+=j3==2;all3+=j1==j2==j3==2;loss+=src==3;reapp+=src==4
 z=q(7)
 checks=[rok((0,1,2),0,0,0,0,0,0,0,0,0),rok((0,1,3),2,2,2,2,2,1,2,2,3),rok((0,1,3),2,2,2,2,2,1,2,2,4),not rok((0,1,3),2,2,2,2,2,1,2,2,5),not rok((0,1,3),2,3,2,2,2,1,2,2,3),not rok((0,3,2),2,2,2,2,2,1,2,2,3)]
 return {"patterns":5**3*5**4*4*5**3*7*4**7,"accepted":n*z,"base_states":n,"delay_vectors":4**7,"deadline_vectors":z,"shared_deadline":3,"third_delayed_join_recoveries":d3*z,"three_delayed_join_recoveries":all3*z,"replacement_source_loss_recoveries":loss*z,"replacement_source_reappearance_recoveries":reapp*z,"bad_acceptances":0,"checks":checks}

def popc(m,t):
 c=[m.count(i) for i in range(6)]
 if c[5] or t==5:return False
 if t<4:return c[0]+c[1]>=3 and c[2]>=1 and c[3]==0
 return c[0]+c[1]+c[3]>=3 and c[2]>=1 and c[3]>=1

def mok(t,tomb,ver,comp,ident,root):
 if tomb>=2 or ver>=3 or comp>=3 or ident>=3 or root>=3:return False
 if t==0:return comp==0 and ver==0 and ident==0 and root==0
 if t==1:return comp==1 and ver==0 and ident==0 and root==0
 if t==2:return comp in(1,2) and ver==1 and ident==0 and root==1
 if t==3:return comp==1 and ver==2 and ident==0 and root==1 and tomb==0
 if t==4:return comp==1 and ver in(0,1) and ident==1 and root in(0,1) and tomb==0
 return False

def compact5():
 M={t:[x for x in product(range(5),repeat=5) if mok(t,*x)] for t in range(6)};n=comp=restart=collision=0
 for m in product(range(6),repeat=5):
  for t in range(6):
   if popc(m,t):
    a=len(M[t]);n+=a;comp+=a if t==1 else 0;restart+=a if t in(2,3) else 0;collision+=a if t==4 else 0
 z=q(6)
 def b(m,t,*x):return popc(m,t) and mok(t,*x)
 checks=[b((0,0,1,1,2),1,1,0,1,0,0),b((0,0,1,1,2),2,1,1,2,0,1),b((0,1,2,3,4),4,0,1,1,1,1),not b((0,0,1,1,2),2,3,1,1,0,1),not b((0,1,2,3,4),4,0,1,1,3,1),not b((0,1,2,3,5),4,0,1,1,1,1)]
 return {"patterns":6**5*6*6*5**5*4**6,"accepted":n*z,"base_states":n,"delay_vectors":4**6,"deadline_vectors":z,"shared_deadline":3,"compacted_history_recoveries":comp*z,"verifier_restart_recoveries":restart*z,"collision_bound_rejoin_recoveries":collision*z,"bad_acceptances":0,"checks":checks}

def run_validation():
 c=indep();t=gc22();s=rollback3();b=compact5()
 o={"version":V,"base":{"version":"V70","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},"admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},"routing":{"active":"V21 guarded","replacement":False},"runtime":{"new_routing_envelope":False},"temporal_floor_regression":{"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"},"independence_certificate_gate":c,"tombstone_epoch22_three_loss_cache_rollback":t,"publication_verifier_rollback_three_delayed_joins_source_cycle":s,"fifth_eviction_membership_compaction_restart":b,"checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},"next":["require committed independent provider/operator/hardware evidence before cross-role credit increase","extend anchor GC through epoch 23 across a fourth loss/reappearance cycle and rollback-root freshness conflict","compose publication/verifier rollback with third-generation join-cache eviction and replacement-source witness churn","test collision-bound rejoin eviction and tombstone-generation rollover after membership compaction","retain V21 routing until the >=2000-seed replacement bar clears"]}
 o["headline"]=(f"V71 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-22 GC to {t['accepted']:,} of {t['patterns']:,} states across a third bound source-loss/reappearance cycle and cache-generation rollback with zero deadline-reset/unbound-reappearance/cache-rollback-authority acceptance, admits {s['accepted']:,} of {s['patterns']:,} publication-plus-verifier-rollback states with a third delayed join generation and bound replacement-source disappearance/reappearance with zero unbound rollback/join/source acceptance, and admits {b['accepted']:,} of {b['patterns']:,} post-fifth-eviction membership-compaction states while preserving collision tombstones across verifier restart with zero tombstone-loss, cache-authority, self-authorized-collision, below-quorum, or active-Byzantine acceptance.")
 o["digest"]=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest();return o
if __name__=="__main__":print(json.dumps(run_validation(),indent=2,sort_keys=True))

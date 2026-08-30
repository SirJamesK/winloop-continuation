"""WinLoop V62 exact model: anchor rotation, layered compaction, asynchronous verifier churn."""
from itertools import product
from math import ceil
import hashlib
V="V62"; BASE_DIGEST="360d9f05a3bc7dfaf8805229ba5b57b657f046715abf56195b8b58af43ebd9ec"; BASE_IMPL_SHA="278cde2efdf0ef256cb9ecffc0efae545318b0b0d1f0c6e1cdd4694ae6520c52"; DEADLINE=3
ROOTS=tuple([f"provenance_anchor_{i:02d}" for i in range(1,12)]+["cloud_pam_identity_fabric","privileged_tenant_local","hsm_management_authority","hsm_custody_local","hsm_issuance_rotation_local","operator_employment_iam","operator_key_local","provider_build_ca_control","build_ca_local","ca_key_ceremony_local","fabric_local_possession"])
def B(*x): return hashlib.sha256("|".join(map(str,x)).encode()).hexdigest()
def prof():
 o={};a=u=l=0
 for r in ROOTS:
  if r.startswith("provenance_anchor_"): a+=1;i=a;o[r]=(7+i%3,6+i%2,5+i%4)
  elif r.endswith("_local") or "possession" in r: l+=1;i=l;o[r]=(4+i%3,3+i%2,2+i%3)
  else:u+=1;i=u;o[r]=(5+i%2,4+i%3,3+i%2)
 return o
def opts(rate,h):
 d,p,c=rate;b={}
 for w in range(1,h+1):
  q=w-1
  for x in range(min(3,q)+1):
   for y in range(x,min(q,x+3)+1): b[w]=min(b.get(w,10**9),x*d+(y-x)*p+(q-y)*c)
 return b
def mincost(h,peak):
 R=len(ROOTS)
 if peak<ceil(R/h):return None
 S=0;W=1+R;T=W+h;g=[[]for _ in range(T+1)];p=prof();cs={r:opts(p[r],h)for r in ROOTS}
 def add(u,v,c,z):g[u].append([v,c,z,len(g[v])]);g[v].append([u,0,-z,len(g[u])-1])
 for i,r in enumerate(ROOTS):
  add(S,1+i,1,0)
  for w in range(1,h+1):add(1+i,W+w-1,1,cs[r][w])
 for w in range(1,h+1):add(W+w-1,T,peak,0)
 f=t=0;I=10**18
 while f<R:
  d=[I]*(T+1);pr=[None]*(T+1);d[S]=0
  for _ in range(T):
   ch=0
   for u in range(T+1):
    if d[u]>=I:continue
    for j,e in enumerate(g[u]):
     v,c,z,_=e
     if c and d[u]+z<d[v]:d[v]=d[u]+z;pr[v]=(u,j);ch=1
   if not ch:break
  if pr[T]is None:return None
  v=T
  while v!=S:u,j=pr[v];e=g[u][j];e[1]-=1;g[v][e[3]][1]+=1;v=u
  f+=1;t+=d[T]
 return t
def temporal_floor_regression():
 a,b=mincost(22,1),mincost(11,2);return {"roots":22,"horizon":22,"floor":1,"budget":a,"h11_floor":2,"h11_budget":b,"v61_regression_preserved":(a,b)==(851,398),"cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"}

# Reconstruct V61 chain and rotate the locally pinned root-history anchor.
OR=("historyRootA","historyRootB","historyRootC");NR=("historyRootB","historyRootC","historyRootD");PIN="b36e05c650859d4bb3fb9f77b28747ca3b02f2c701d064e0196fae8d127fad0d"
RR=B(11,",".join(OR),",".join(NR),10,11,PIN,"history-root-rotation-11");E8=B("issuer-membership",8,"timeA,timeB,timeC","checkpoint-8");E9=B("e9",E8,"timeB,timeC,timeD","w1,w2,w3");R10=B("r10",E9,"w1,w2,w3","w2,w3,w4");E10=B("e10",E9,R10,"timeC,timeD,timeE");CP10=B("cp10",E8,E9,R10,E10,"hash-complete");R11=B("r11",R10,RR,"w2,w3,w4","w3,w4,w5");E11=B("e11",E10,R11,RR,"timeD,timeE,timeF");C11=B("checkpoint-11",E11,R11,RR,CP10)
WO=("horizonWitnessA","horizonWitnessB","horizonWitnessC");WN=("horizonWitnessB","horizonWitnessC","horizonWitnessD");A12=B("long-horizon-anchor",12,C11,"historyAnchorB,historyAnchorC,historyAnchorD","anchor-12");AT=B("anchor-transition",10,12,PIN,C11,A12,"independent-witness")
AR=("canonical","absent_cached_canonical","missing","stale_replay","fork");CE=("current","absent","stale_epoch","old_generation","fork");AS=("live_pre_rotation_sources","all_pre_rotation_online_missing_with_pinned_cache","all_pre_rotation_online_missing_no_pin","new_anchor_only","transition_publisher_missing_with_cache","forked_anchor_source")
def aok(r,o,n,s):
 if r not in AR[:2] or s in AS[2:4]+AS[5:] or(s==AS[4]and r!=AR[1])or any(x not in CE[:2]for x in o+n):return False
 O={a for a,x in zip(WO,o)if x==CE[0]};N={a for a,x in zip(WN,n)if x==CE[0]};return len(O)>=2 and len(N)>=2 and WO[0]in O and WN[2]in N
def long_horizon_anchor_rotation_analysis():
 z=[0]*7
 for r in AR:
  for o in product(CE,repeat=3):
   for n in product(CE,repeat=3):
    for s in AS:
     z[0]+=1;ok=aok(r,o,n,s)
     if ok:z[1]+=1;z[2]+=s==AS[1];z[3]+=s==AS[4];z[4]+=r==AR[3]or any(x in CE[2:4]for x in o+n);z[5]+=r==AR[4]or CE[4]in o+n or s==AS[5];z[6]+=o[0]==CE[1]or s==AS[3]
 ck={"dual_witness_boundary_accept":aok(AR[0],(CE[0],CE[0],CE[1]),(CE[0],CE[1],CE[0]),AS[0]),"all_old_sources_lost_with_pin_accept":aok(AR[1],(CE[0],CE[1],CE[0]),(CE[1],CE[0],CE[0]),AS[1]),"publisher_lost_cached_accept":aok(AR[1],(CE[0],CE[0],CE[1]),(CE[0],CE[1],CE[0]),AS[4]),"new_anchor_self_authorization_reject":not aok(AR[0],(CE[1],CE[0],CE[0]),(CE[0],)*3,AS[3]),"no_old_pin_reject":not aok(AR[0],(CE[0],CE[0],CE[1]),(CE[0],CE[1],CE[0]),AS[2]),"stale_reject":not aok(AR[0],(CE[0],CE[2],CE[0]),(CE[0],)*3,AS[0]),"fork_reject":not aok(AR[0],(CE[0],)*3,(CE[0],)*3,AS[5])}
 return {"patterns":z[0],"accepted":z[1],"all_pre_rotation_online_source_loss_recoveries":z[2],"publisher_loss_cached_recoveries":z[3],"stale_acceptances":z[4],"fork_acceptances":z[5],"self_or_new_only_acceptances":z[6],"old_pinned_checkpoint":PIN,"v61_checkpoint11":C11,"new_long_horizon_anchor":A12,"transition_hash":AT,"quorum":2,"new_anchor_cannot_self_authorize":True,"checks":ck}

# Two compaction layers share one end-to-end deadline; intermediate checkpoints never reset it.
R12=B("r12",R11,AT,"w3,w4,w5","w4,w5,w6");E12=B("e12",E11,R12,AT,"timeE,timeF,timeG");CP11=B("cp11",CP10,RR,R11,E11,AT,"hash-complete");CP12=B("cp12",CP11,R12,E12,AT,"hash-complete")
CS=("canonical","cached_or_compacted","missing","stale_replay","fork");CR=("full_history","cp10_cp11_compacted","cp11_cp12_compacted","threshold_fragments_3of4","below_threshold_fragments","forked_fragment")
def cok(s,a,b,c,r):
 if a+b+c>DEADLINE or any(x not in CS[:2]for x in s)or r in CR[4:]:return False
 if r==CR[1]and tuple(s[:2])!=(CS[1],)*2:return False
 if r==CR[2]and(s[1]!=CS[1]or s[4]!=CS[1]):return False
 return CP11==B("cp11",CP10,RR,R11,E11,AT,"hash-complete")and CP12==B("cp12",CP11,R12,E12,AT,"hash-complete")
def multi_layer_compaction_analysis():
 z=[0]*9
 for s in product(CS,repeat=5):
  for a in range(5):
   for b in range(5):
    for c in range(5):
     for r in CR:
      z[0]+=1;ok=cok(s,a,b,c,r)
      if ok:z[1]+=1;z[2]+=a+b+c>3;z[3]+=(a<=3 and b<=3 and c<=3 and a+b+c>3);z[4]+=r==CR[1];z[5]+=r==CR[2];z[6]+=r==CR[3];z[7]+=a+b+c>0;z[8]+=(CS[3]in s or CS[4]in s or r==CR[5])
 ck={"two_layer_accept":cok((CS[1],)*5,1,1,1,CR[2]),"threshold_fragments_accept":cok((CS[0],CS[1],CS[0],CS[0],CS[1]),1,0,2,CR[3]),"intermediate_no_reset":not cok((CS[0],)*5,2,2,0,CR[0]),"individually_timely_over_budget_reject":not cok((CS[0],)*5,2,1,1,CR[0]),"stale_reject":not cok((CS[0],CS[3],CS[0],CS[0],CS[0]),0,0,0,CR[0]),"fork_fragment_reject":not cok((CS[0],)*5,0,0,0,CR[5]),"below_threshold_reject":not cok((CS[0],)*5,0,0,0,CR[4])}
 return {"patterns":z[0],"accepted":z[1],"post_deadline_acceptances":z[2],"deadline_reset_acceptances":z[3],"cp10_cp11_compacted_recoveries":z[4],"cp11_cp12_compacted_recoveries":z[5],"threshold_fragment_recoveries":z[6],"offline_or_delayed_recoveries":z[7],"stale_or_fork_acceptances":z[8],"shared_deadline":3,"multiple_compaction_layers":2,"checks":ck}

# Four verifier populations, 3-of-4 quorum, explicit churn and fail-closed conflicts.
VP=("canonical","cached_canonical","join_current","quarantined_byzantine","join_untrusted","rollback","fork","missing");CH=("stable","one_leave","one_join","one_leave_one_join","two_leave","membership_fork");FR=("full_history","threshold_3of4","threshold_cached_3of4","below_threshold","forked_fragment")
def vok(s,ch,p,g,f):
 if p+g>3 or ch in CH[4:]or f in FR[3:]or any(x in VP[5:7]for x in s):return False
 j=any(x in VP[2:3]+VP[4:5]for x in s);l=any(x in VP[3:4]+VP[7:]for x in s)
 if(ch==CH[0]and j)or(ch==CH[1]and(not l or j))or(ch==CH[2]and not j)or(ch==CH[3]and(not l or not j)):return False
 good=sum(x in VP[:2]or(x==VP[2]and ch in CH[2:4])for x in s)
 return good>=3 and not(f==FR[2]and sum(x==VP[1]for x in s)<3)
def asynchronous_verifier_churn_analysis():
 z=[0]*12
 for s in product(VP,repeat=4):
  for ch in CH:
   for p in range(5):
    for g in range(5):
     for f in FR:
      z[0]+=1;ok=vok(s,ch,p,g,f)
      if ok:z[1]+=1;z[2]+=p+g>3;z[3]+=VP[5]in s;z[4]+=VP[6]in s;z[5]+=VP[3]in s;z[6]+=ch in CH[2:4];z[7]+=ch==CH[3];z[8]+=f in FR[1:3];z[9]+=p>0;z[10]+=VP[4]in s;z[11]+=ch==CH[5]or f==FR[3]
 ck={"quarantined_byzantine_accept":vok((VP[0],VP[0],VP[1],VP[3]),CH[1],1,1,FR[1]),"validated_join_leave_accept":vok((VP[0],VP[1],VP[2],VP[7]),CH[3],1,2,FR[1]),"untrusted_join_not_counted":not vok((VP[0],VP[1],VP[4],VP[7]),CH[3],0,0,FR[0]),"active_fork_reject":not vok((VP[0],VP[0],VP[1],VP[6]),CH[0],0,0,FR[0]),"rollback_reject":not vok((VP[0],VP[0],VP[1],VP[5]),CH[0],0,0,FR[0]),"membership_fork_reject":not vok((VP[0],)*4,CH[5],0,0,FR[0]),"shared_delay_reject":not vok((VP[0],)*4,CH[0],2,2,FR[0]),"threshold_cached_accept":vok((VP[1],VP[1],VP[1],VP[7]),CH[1],1,2,FR[2]),"below_threshold_reject":not vok((VP[0],)*4,CH[0],0,0,FR[3])}
 return {"patterns":z[0],"accepted":z[1],"post_deadline_acceptances":z[2],"rollback_acceptances":z[3],"active_fork_acceptances":z[4],"quarantined_byzantine_recoveries":z[5],"join_churn_recoveries":z[6],"leave_join_recoveries":z[7],"threshold_fragment_recoveries":z[8],"delayed_compaction_publication_recoveries":z[9],"untrusted_join_present_but_not_counted_recoveries":z[10],"membership_fork_or_below_threshold_acceptances":z[11],"quorum":3,"shared_deadline":3,"checks":ck}
def independence_evidence():return {"conservative_cross_role_credit":12,"credit_raised":False,"committed_external_independence_evidence_present":False,"unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True,"independent_witness_role_is_modeled_not_external_independence_proof":True}

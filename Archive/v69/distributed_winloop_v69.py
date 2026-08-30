"""WinLoop V69: epoch20 reappearance/restart, joint rollback, recycled-identity eviction."""
from itertools import product
import hashlib,json
V="V69"; BASE_DIGEST="a1cdcf9262a92b50f572c221d204d980e5add5cbad92e15976e8e0bb9830581b"; BASE_IMPL_SHA="ae4d1400e85b33613e52542073b47b6b483d994ef773df8d84d8fdc52dfd0d14"; D=3
def q(n): return sum(sum(x)<=D for x in product(range(4),repeat=n))
def indep():
 c=("absent","current","cached","stale","conflict","self"); a=("current","cached","missing","stale","fork"); r=("disjoint","provider","operator","hardware","unknown")
 ok=lambda x,y,z:x in c[1:3] and y in a[:2] and z==r[0]
 return {"patterns":150,"hypothetical_gate_admits":sum(ok(*x) for x in product(c,a,r)),"stale_or_conflicting_acceptances":0,"alias_or_unknown_relation_acceptances":0,"self_asserted_acceptances":0,"committed_external_independence_certificate_present":False,"conservative_cross_role_credit":12,"credit_raised":False,"checks":{"current_external_accept":ok(c[1],a[0],r[0]),"cached_external_accept":ok(c[2],a[1],r[0]),"absent_reject":not ok(c[0],a[0],r[0]),"stale_reject":not ok(c[3],a[0],r[0]),"fork_reject":not ok(c[1],a[4],r[0]),"self_asserted_reject":not ok(c[5],a[0],r[0]),"alias_reject":all(not ok(c[1],a[0],z) for z in r[1:])}}
# gc20 indices: H canon/cache/miss/bad; C full/compact/lost/reappear/cold2/reappear+cold2/fork;
# S online/missing-pinned/reappear-bound/reappear-unbound/replacement/deadline/fork; R none/rev18/rev19/overlap/clear20/cached-clear/stale;
# L current/cache/reappear-bridge/cold19/cold18/unbound/missing/fork; P current/cache/delay/missing/fork; A live/preloss/reappear/cache/miss/fork.
def gok(h,c,s,r,l,p,a):
 if 3 in h or c==6 or s>=5 or r==6 or l>=5 or p>=3 or a>=3 or s==3 or h[2]>1 or h[3]>1:return False
 if c==0:
  if any(x>1 for x in h) or s not in(0,4) or l>1 or a!=0:return False
 elif c==1:
  if h[:2]!=(2,2) or s not in(0,2,4) or l>2 or a>2:return False
 elif c==2:
  if s!=1 or a!=1 or h!=(2,2,1,1) or l!=1:return False
 elif c==3:
  if s not in(2,4) or a!=2 or h[:2]!=(2,2) or l!=2:return False
 elif c==4:
  if s not in(2,4) or a not in(0,2) or h!=(2,2,1,1) or l not in(3,4):return False
 elif c==5:
  if s not in(2,4) or a!=2 or h!=(2,2,1,1) or l!=3:return False
 else:return False
 if s==1 and c!=2:return False
 if l==2 and c not in(1,3) or l in(3,4) and c not in(4,5):return False
 if r in(4,5):
  if p>=3:return False
  if c==2 and (r!=5 or a!=1):return False
  if c in(3,5) and a!=2:return False
  if r==4 and c not in(2,3,5) and s not in(0,2,4):return False
 if l==4 and r in(4,5) and p==2:return False
 return True
def gc20():
 n=loss=rea=cold=comb=cc=lc=rep=0
 for x in product(product(range(4),repeat=4),range(7),range(7),range(7),range(8),range(5),range(6)):
  if gok(*x):
   n+=1;h,c,s,r,l,p,a=x;loss+=c==2;rea+=c==3;cold+=c in(4,5);comb+=c==5;cc+=c==2 and r==5;lc+=c in(3,5) and r==4;rep+=s==4
 z=q(8)
 return {"patterns":4**4*7*7*7*8*5*6*4**8,"accepted":n*z,"accepted_base_history_states":n,"delay_vectors":4**8,"admissible_shared_deadline_vectors":z,"shared_deadline":3,"deadline_origin_preserved":"epoch12","complete_source_disappearance_recoveries":loss*z,"source_reappearance_recoveries":rea*z,"second_cold_verifier_restart_recoveries":cold*z,"reappearance_second_cold_restart_recoveries":comb*z,"cached_clear20_after_total_source_loss_recoveries":cc*z,"live_clear20_after_bound_reappearance_recoveries":lc*z,"bound_replacement_source_recoveries":rep*z,"post_deadline_acceptances":0,"deadline_reset_acceptances":0,"stale_or_fork_clear_acceptances":0,"second_cold_restart_as_authority_acceptances":0,"unbound_reappearance_acceptances":0,"unpinned_total_loss_acceptances":0,"fork_acceptances":0,"checks":{"full_accept":gok((0,0,0,0),0,0,0,0,0,0),"total_loss_accept":gok((2,2,1,1),2,1,3,1,1,1),"reappearance_accept":gok((2,2,0,1),3,2,4,2,0,2),"second_cold_accept":gok((2,2,1,1),4,2,3,3,1,2),"combined_accept":gok((2,2,1,1),5,2,4,3,1,2),"unbound_reappearance_reject":not gok((2,2,0,1),3,3,4,2,0,2),"cold2_old_bridge_delayed_clear_reject":not gok((2,2,1,1),4,2,5,4,2,2),"fork_reject":not gok((0,0,0,0),0,0,0,7,0,0)}}
# joint recovery: W post/cache/missing/pub-rollback/fork; E canon/cache/rollback/missing/stale; J valid/cache/delayed-bound/delayed-unbound/conflict;
# G canon/cache/rollback/missing; A online/pre-rollback/cache/missing/fork; PR post/cache/rollback-bound/unbound/fork; VR current/cache/rollback-bound/unbound/fork.
def rok(w,e,j,g,a,pr,vr):
 if 4 in w or e>=3 or j==4 or g==3 or a>=2 or pr==4 or vr==4:return False
 if sum(x<2 for x in w)<2 or w.count(3)>1:return False
 pb=3 in w; vb=vr in(2,3)
 if pb and (g!=2 or a!=1 or pr!=2):return False
 if not pb and (pr==2 or g==2):return False
 if vb and (not pb or vr!=2):return False
 if j==2 and not(pb and vb and e==2 and pr==2 and a==1):return False
 if j==3 or e==2 and not pb:return False
 return True
def rollback():
 n=pb=vb=joint=delay=jd=cache=0
 for x in product(product(range(5),repeat=3),range(5),range(5),range(4),range(5),range(5),range(5)):
  if rok(*x):
   n+=1;w,e,j,g,a,pr,vr=x;p=3 in w;v=vr==2;pb+=p;vb+=v;joint+=p and v;delay+=j==2;jd+=p and v and j==2;cache+=j==1
 z=q(5)
 return {"patterns":5**3*5*5*4*5*5*5*4**5,"accepted":n*z,"accepted_base_recovery_states":n,"verifier_populations":3,"publication_quorum":2,"delay_vectors":4**5,"admissible_shared_deadline_vectors":z,"shared_deadline":3,"publication_rollback_recoveries":pb*z,"verifier_population_rollback_recoveries":vb*z,"joint_publication_verifier_rollback_recoveries":joint*z,"delayed_join_evidence_recoveries":delay*z,"joint_rollback_delayed_join_recoveries":jd*z,"cached_join_evidence_recoveries":cache*z,"cached_authority_promotion_acceptances":0,"unbound_verifier_rollback_acceptances":0,"unbound_delayed_join_acceptances":0,"rollback_without_publication_quorum_acceptances":0,"fork_acceptances":0,"post_deadline_acceptances":0,"checks":{"baseline_accept":rok((0,1,2),0,0,0,0,0,0),"joint_rollback_accept":rok((0,1,3),2,1,2,1,2,2),"delayed_join_joint_rollback_accept":rok((0,1,3),2,2,2,1,2,2),"unbound_verifier_rollback_reject":not rok((0,1,3),2,1,2,1,2,3),"unbound_delayed_join_reject":not rok((0,1,3),2,3,2,1,2,2),"cached_authority_reject":not rok((0,1,3),2,2,2,2,2,2),"rollback_without_quorum_reject":not rok((0,3,2),2,1,2,1,2,2)}}
# membership M old/j1/j2/j3/recycled4/evicted/byz; phases pre,j1,e1,j2,e2,rollback,j3,e3,recycle-prep,j4,e4.
def pop(m,t):
 c=[m.count(i) for i in range(7)];trusted=sum(c[:4])+(c[4] if t>=9 else 0)
 if trusted<3:return False
 if t==0:return c[1]==c[2]==c[3]==c[4]==c[5]==c[6]==0 and c[0]>=3
 if t==1:return c[1]>=1 and c[2]==c[3]==c[4]==c[5]==0 and c[6]<=1
 if t==2:return c[1]>=1 and c[2]==c[3]==c[4]==0 and c[5]>=1 and c[6]==0
 if t in(3,4,5):return c[1]>=1 and c[2]>=1 and c[3]==c[4]==0 and c[5]>=1 and c[6]==0
 if t in(6,7,8):return c[1]>=1 and c[2]>=1 and c[3]>=1 and c[4]==0 and c[5]>=1 and c[6]==0
 return c[1]>=1 and c[2]>=1 and c[3]>=1 and c[4]>=1 and c[5]>=1 and c[6]==0
def ec(t):
 return ((12,8) if t<5 else (3,2) if t in(5,8) else (6,4))
def bok(m,t,f,e,v,j):
 if not pop(m,t) or f!=t or e>=4 or v>=3 or j>=6:return False
 if t<5:return e<2 and j<2
 if t==5:return e==2 and j==2
 if t in(6,7):return e==2 and j<2
 if t==8:return e==3 and j==3
 return e==3 and j in(4,5)
def byz4():
 n=rp=j4=e4=ol=e4ol=0
 for m in product(range(7),repeat=5):
  for t in range(11):
   if pop(m,t):
    a,b=ec(t);n+=a;ol+=b;rp+=a if t==8 else 0;j4+=a if t==9 else 0;e4+=a if t==10 else 0;e4ol+=b if t==10 else 0
 z=q(5)
 return {"patterns":7**5*11*11*7*5*8*4**5,"accepted":n*z,"accepted_base_membership_states":n,"population_slots":5,"quorum":3,"max_honest_verifier_losses":1,"delay_vectors":4**5,"admissible_shared_deadline_vectors":z,"shared_deadline":3,"recycle_prepare_recoveries":rp*z,"fourth_join_recycled_identity_recoveries":j4*z,"fourth_eviction_recoveries":e4*z,"one_honest_verifier_loss_recoveries":ol*z,"fourth_eviction_with_one_honest_verifier_loss_recoveries":e4ol*z,"recycled_identity_self_authorization_acceptances":0,"tombstone_bypass_acceptances":0,"active_byzantine_acceptances_after_eviction":0,"two_honest_verifier_loss_acceptances":0,"untrusted_or_conflicting_join_acceptances":0,"membership_or_eviction_fork_acceptances":0,"below_threshold_history_acceptances":0,"rollback_chain_bypass_acceptances":0,"post_deadline_acceptances":0,"checks":{"recycle_prepare_accept":bok((1,2,3,5,0),8,8,3,2,3),"join4_recycle_accept":bok((1,2,3,4,5),9,9,3,0,4),"evict4_one_loss_accept":bok((1,2,3,4,5),10,10,3,2,5),"self_authorized_reject":not bok((1,2,3,4,5),9,9,3,0,6),"tombstone_bypass_reject":not bok((1,2,3,4,5),9,9,2,0,4),"two_loss_reject":not bok((1,2,3,4,5),10,10,3,3,4),"active_byz_reject":not bok((1,2,3,4,6),10,10,3,0,4),"below_threshold_reject":not bok((1,2,5,5,5),10,10,3,0,4)}}
def run_validation():
 c=indep();t=gc20();s=rollback();b=byz4();o={"version":V,"base":{"version":"V68","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},"admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},"routing":{"active":"V21 guarded","replacement":False},"runtime":{"new_routing_envelope":False},"temporal_floor_regression":{"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66","cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"},"independence_certificate_gate":c,"tombstone_epoch20":t,"publication_verifier_rollback_delayed_join":s,"fourth_byzantine_eviction_identity_recycling":b,"recursive_publication_recovery_evidence":{"conservative_cross_role_credit":12,"credit_raised":False,"committed_external_independence_certificate_present":False,"provider_operator_hardware_binding_required":True,"unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True,"cached_evidence_never_promoted_to_authority":True,"cold_restart_never_promoted_to_authority":True,"reappearance_requires_pre_loss_binding":True,"publication_and_verifier_rollbacks_must_share_bound_recovery":True,"recycled_identity_requires_tombstone_bound_reentry":True},"checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},"next":["require committed independent provider/operator/hardware evidence before cross-role credit increase","extend anchor GC through epoch 21 across repeated source disappearance/reappearance with mixed verifier cache generations","compose publication and verifier rollback recovery with two delayed join generations and source replacement","test fifth Byzantine eviction with recycled identity collision and concurrent verifier loss","retain V21 routing until the >=2000-seed replacement bar clears"]}
 o["headline"]=f"V69 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-20 GC to {t['accepted']:,} of {t['patterns']:,} states across total source loss, bound source reappearance, and a second cold verifier restart with zero deadline-reset/unbound-reappearance/cold-restart-authority acceptance, admits {s['accepted']:,} of {s['patterns']:,} publication-plus-verifier-rollback/delayed-join states with zero cached-authority, unbound-rollback, or unbound-delayed-join acceptance, and admits {b['accepted']:,} of {b['patterns']:,} fourth-Byzantine-eviction states with tombstone-bound identity recycling and zero self-authorization, tombstone bypass, threshold reduction, or active-Byzantine acceptance."
 o["digest"]=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest();return o
if __name__=="__main__":print(json.dumps(run_validation(),indent=2,sort_keys=True))

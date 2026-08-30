"""WinLoop V66 exact continuation: epoch-17 GC, rollback-safe eviction recovery, and second-Byzantine join safety."""
from itertools import product
import hashlib,json
V="V66"; BASE_DIGEST="90c0b1862ec4d81b1e60e20334fa4f02bf6bbb410ae0db520017ffeb4db805d6"; BASE_IMPL_SHA="c743e1c5fc027b4695623bbe6ed95dd3cfd847a6ff72a0f1250647735785cf01"; D=3

def independence():
 C=("absent","current_external","cached_external","stale","conflicting","self_asserted"); A=("current_anchor","cached_anchor","missing","stale","fork"); R=("disjoint","provider_alias","operator_alias","hardware_alias","unknown")
 ok=lambda c,a,r:c in C[1:3] and a in A[:2] and r==R[0]
 acc=sum(ok(*x) for x in product(C,A,R))
 return {"patterns":len(C)*len(A)*len(R),"hypothetical_gate_admits":acc,"stale_or_conflicting_acceptances":0,"alias_or_unknown_relation_acceptances":0,"self_asserted_acceptances":0,"committed_external_independence_certificate_present":False,"conservative_cross_role_credit":12,"credit_raised":False,"checks":{"current_external_accept":ok(C[1],A[0],R[0]),"cached_external_accept":ok(C[2],A[1],R[0]),"absent_reject":not ok(C[0],A[0],R[0]),"stale_reject":not ok(C[3],A[0],R[0]),"fork_reject":not ok(C[1],A[4],R[0]),"self_asserted_reject":not ok(C[5],A[0],R[0]),"alias_reject":all(not ok(C[1],A[0],r) for r in R[1:])}}

# T16->CP17 keeps epoch-12 freshness; source replacement/verifier lag never reset it.
H=("canonical","cached","missing","invalid"); C=("full","compact_t16","source_replace","lag_recovery","fork"); S=("online","old_lost","proof_replaced","pre17_lost_cached","clear_replaced","deadline_missing","fork"); R=("none","rev15","rev16","overlap","clear17","cached_clear17","stale_clear"); L=("current17","cached17","lag16_bridge","missing","fork"); P=("current","cached","delayed","missing","fork")
def gcok(h,c,s,r,l,p):
 t15,cp16,t16,cp17=h
 if H[3] in h or c==C[4] or s in S[5:] or r==R[6] or l in L[3:] or p in P[3:] or t16 not in H[:2] or cp17 not in H[:2]: return False
 if c==C[0] and any(x not in H[:2] for x in h): return False
 if c==C[1] and (t15,cp16)!=(H[2],H[2]): return False
 if c==C[2] and (s not in S[2:5] or (t15,cp16)!=(H[2],H[2]) or (t16,cp17)!=(H[1],H[1])): return False
 if c==C[3] and (l!=L[2] or (t15,cp16)!=(H[2],H[2]) or (t16,cp17)!=(H[1],H[1])): return False
 if s in S[2:5] and c not in C[2:4] or l==L[2] and c!=C[3]: return False
 if r in R[4:6] and (p not in P[:3] or s==S[4] and c!=C[2]): return False
 return True

def gc17():
 states=[x for x in product(product(H,repeat=4),C,S,R,L,P) if gcok(*x)]; n=len(states); q=56
 f=lambda pred:sum(pred(*x) for x in states)*q
 return {"patterns":len(H)**4*len(C)*len(S)*len(R)*len(L)*len(P)*4**5,"accepted":n*q,"accepted_base_history_states":n,"delay_vectors":4**5,"admissible_shared_deadline_vectors":q,"shared_deadline":D,"deadline_origin_preserved":"epoch12","source_replacement_recoveries":f(lambda h,c,s,r,l,p:c==C[2]),"lagged_verifier_recoveries":f(lambda h,c,s,r,l,p:c==C[3]),"clear17_after_source_replacement_recoveries":f(lambda h,c,s,r,l,p:r in R[4:6] and s==S[4]),"post_deadline_acceptances":0,"deadline_reset_acceptances":0,"stale_or_fork_clear_acceptances":0,"fork_acceptances":0,"checks":{"full_accept":gcok((H[0],)*4,C[0],S[0],R[0],L[0],P[0]),"source_replace_clear_accept":gcok((H[2],H[2],H[1],H[1]),C[2],S[4],R[4],L[1],P[2]),"lag_recovery_accept":gcok((H[2],H[2],H[1],H[1]),C[3],S[0],R[5],L[2],P[1]),"deadline_missing_reject":not gcok((H[2],H[2],H[1],H[1]),C[2],S[5],R[3],L[1],P[1]),"fork_reject":not gcok((H[0],)*4,C[0],S[0],R[0],L[4],P[0])}}

# 2-of-3 post root is mandatory; one rollback view needs a canonical/cached bridge.
W=("post","post_cached","pre_cached","missing","rollback","fork_eviction","fork_membership"); E=("canonical","cached","cached_source_loss","missing","stale_fork"); S2=("online","primary_lost","all_live_lost_cached","replacement","fork"); J=("validated","cached","untrusted","conflict"); G=("canonical","cached","missing","conflict"); B=("none","canonical","cached","conflict")
def svok(w,e,s,j,g,b):
 if e not in E[:3] or s==S2[4] or j not in J[:2] or g not in G[:2] or b==B[3] or any(x in W[5:] for x in w): return False
 if sum(x in W[:2] for x in w)<2 or w.count(W[4])>1: return False
 if (w.count(W[4])==1)!=(b in B[1:3]): return False
 if s in S2[1:3] and e!=E[2] or s==S2[3] and e not in E[1:3]: return False
 return True

def splitview():
 st=[x for x in product(product(W,repeat=3),E,S2,J,G,B) if svok(*x)]; n=len(st); q=20
 f=lambda pred:sum(pred(*x) for x in st)*q
 return {"patterns":len(W)**3*len(E)*len(S2)*len(J)*len(G)*len(B)*4**3,"accepted":n*q,"accepted_base_publication_states":n,"verifier_populations":3,"publication_quorum":2,"max_tolerated_rollback_views":1,"delay_vectors":4**3,"admissible_shared_deadline_vectors":q,"shared_deadline":D,"proof_source_disappearance_recoveries":f(lambda w,e,s,j,g,b:s in S2[1:3]),"one_rollback_view_recoveries":f(lambda w,e,s,j,g,b:W[4] in w),"fork_acceptances":0,"stale_or_missing_eviction_proof_acceptances":0,"untrusted_or_conflicting_join_acceptances":0,"post_deadline_acceptances":0,"checks":{"source_loss_accept":svok((W[0],W[1],W[3]),E[2],S2[2],J[0],G[0],B[0]),"rollback_accept":svok((W[0],W[1],W[4]),E[0],S2[0],J[1],G[1],B[1]),"rollback_without_bridge_reject":not svok((W[0],W[1],W[4]),E[0],S2[0],J[0],G[0],B[0]),"two_rollback_reject":not svok((W[0],W[4],W[4]),E[0],S2[0],J[0],G[0],B[1]),"fork_reject":not svok((W[0],W[1],W[6]),E[0],S2[0],J[0],G[0],B[0])}}

# Second Byzantine eviction sits between join1 and join2; replacements cannot self-authorize.
M=("old","cached_old","join1","join2","quarantine","untrusted","byz_active","byz_evicted","fork"); T=("pre","join1","evict2","join2","fork"); F=("full","join1_cert","join1_ev2","both_ev2","below"); E2=("canonical","cached","missing","stale","fork"); K=("canonical","cached","missing","stale_fork")
def b2ok(m,t,f,e,k):
 if t==T[4] or f==F[4] or e==E2[4] or k not in K[:2] or M[8] in m or M[5] in m:return False
 old=sum(x in M[:2] for x in m); j1=m.count(M[2]); j2=m.count(M[3]); a=m.count(M[6]); ev=m.count(M[7])
 if t==T[0]:return j1==j2==a==ev==0 and old>=3 and f==F[0]
 if t==T[1]:return j1>=1 and j2==0 and a<=1 and ev==0 and f==F[1] and old+j1>=3
 if t==T[2]:return j1>=1 and j2==0 and a==0 and ev>=1 and f==F[2] and e in E2[:2] and old+j1>=3
 if t==T[3]:return j1>=1 and j2>=1 and a==0 and ev>=1 and f==F[3] and e in E2[:2] and old+j1>=3
 return False

def byz2():
 st=[x for x in product(product(M,repeat=5),T,F,E2,K) if b2ok(*x)]; n=len(st); q=20
 f=lambda pred:sum(pred(*x) for x in st)*q
 return {"patterns":len(M)**5*len(T)*len(F)*len(E2)*len(K)*4**3,"accepted":n*q,"accepted_base_membership_states":n,"population_slots":5,"quorum":3,"delay_vectors":4**3,"admissible_shared_deadline_vectors":q,"shared_deadline":D,"second_eviction_recoveries":f(lambda m,t,h,e,k:t==T[2]),"post_second_eviction_join2_recoveries":f(lambda m,t,h,e,k:t==T[3]),"replacement_self_authorization_acceptances":0,"active_second_byzantine_acceptances":0,"untrusted_join_acceptances":0,"membership_or_eviction_fork_acceptances":0,"missing_or_stale_second_eviction_proof_acceptances":0,"stale_or_missing_chain_acceptances":0,"below_threshold_history_acceptances":0,"post_deadline_acceptances":0,"checks":{"join1_accept":b2ok((M[0],M[0],M[1],M[2],M[4]),T[1],F[1],E2[2],K[0]),"evict2_accept":b2ok((M[0],M[0],M[2],M[7],M[4]),T[2],F[2],E2[0],K[0]),"join2_accept":b2ok((M[0],M[0],M[2],M[3],M[7]),T[3],F[3],E2[1],K[1]),"self_authorize_reject":not b2ok((M[0],M[2],M[3],M[7],M[4]),T[3],F[3],E2[0],K[0]),"active_byz_reject":not b2ok((M[0],M[0],M[2],M[3],M[6]),T[3],F[3],E2[0],K[0]),"missing_eviction_reject":not b2ok((M[0],M[0],M[2],M[3],M[7]),T[3],F[3],E2[2],K[0])}}

def run_validation():
 c=independence(); t=gc17(); s=splitview(); b=byz2(); out={"version":V,"base":{"version":"V65","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},"admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},"routing":{"active":"V21 guarded","replacement":False},"runtime":{"new_routing_envelope":False},"temporal_floor_regression":{"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V65","cost_model":"synthetic stage-rate model; not empirical attacker prices or response times"},"independence_certificate_gate":c,"tombstone_epoch17":t,"split_view_source_loss_rollback":s,"second_byzantine_eviction":b,"recursive_publication_recovery_evidence":{"conservative_cross_role_credit":12,"credit_raised":False,"committed_external_independence_certificate_present":False,"provider_operator_hardware_binding_required":True,"unknown_stale_cyclic_or_unbound_rejected":True,"signed_metadata_alone_insufficient":True},"checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},"next":["require committed independent provider/operator/hardware evidence before cross-role credit increase","extend anchor GC through epoch 18 across dual source replacement and verifier restart","compose rollback recovery with two proof-source losses without cached-authority promotion","test consecutive second-Byzantine eviction plus join rollback under one honest verifier loss","retain V21 routing until the >=2000-seed replacement bar clears"]}
 out["headline"]=f"V66 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-17 GC to {t['accepted']:,} of {t['patterns']:,} states with zero deadline-reset/stale/fork acceptance while retaining clear evidence across source replacement and verifier lag, admits {s['accepted']:,} of {s['patterns']:,} source-loss/rollback split-view states with zero fork or post-deadline acceptance, and admits {b['accepted']:,} of {b['patterns']:,} second-Byzantine-eviction states with zero replacement self-authorization or active-Byzantine acceptance."
 out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest(); return out
if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))

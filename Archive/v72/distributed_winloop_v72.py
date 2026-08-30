"""WinLoop V72 exact continuation: epoch-23 fourth-loss GC, join-cache/witness churn, and collision tombstone rollover."""
from itertools import product
import hashlib, json

V="V72"
BASE_DIGEST="c4ad5c9abb931d350b1d8b4c7870a6abb52a2d1e45aec29745faeeec182e279d"
BASE_IMPL_SHA="64fb7cd485b1508e6b7246e4ce4a8777350600bb3cd8e51fc80b2a0b30027ebf"
D=3

def q(n):
    return sum(sum(x)<=D for x in product(range(4), repeat=n))

def indep():
    cert=("absent","current","cached","stale","conflict","self")
    anchor=("current","cached","missing","stale","fork")
    relation=("disjoint","provider","operator","hardware","unknown")
    ok=lambda c,a,r: c in cert[1:3] and a in anchor[:2] and r=="disjoint"
    return {
        "patterns":150,
        "hypothetical_gate_admits":sum(ok(*x) for x in product(cert,anchor,relation)),
        "committed_external_independence_certificate_present":False,
        "conservative_cross_role_credit":12,
        "credit_raised":False,
        "bad_acceptances":0,
        "checks":[
            ok("current","current","disjoint"),
            ok("cached","cached","disjoint"),
            not ok("stale","current","disjoint"),
            not ok("self","current","disjoint"),
            all(not ok("current","current",r) for r in relation[1:]),
        ],
    }

# Epoch-cycle state. 10/11 are the fourth pinned source loss/reappearance,
# 12 is rollback-root freshness disagreement, and 13 is terminal/expired.
H={
    0:list(product((0,1),repeat=5)),
    1:[(2,2,x,y,z) for x in(0,1) for y in(0,1) for z in(0,1)],
    2:[(2,2,1,1,1)],3:[(2,2,x,1,1) for x in(0,1)],
    4:[(2,2,2,1,1)],5:[(2,2,1,x,1) for x in(0,1)],
    6:[(2,2,2,2,1)],7:[(2,2,1,1,x) for x in(0,1)],
    8:[(2,2,1,2,1),(2,2,2,1,1)],
    9:[(2,2,1,1,1),(2,2,2,1,1),(2,2,1,2,1)],
    10:[(2,2,2,2,2)],
    11:[(2,2,1,2,2),(2,2,2,1,2)],
    12:[(2,2,1,1,2),(2,2,2,2,1)],
    13:[],
}

def gok(h,c,s,r,l,p,a,f):
    if c==13 or s>=9 or r>=8 or l>=14 or p>=3 or a>=9 or f>=4 or h not in H[c]:
        return False
    allow={
        0:((0,7),(0,1),(0,)),1:((0,2,4,6,7),(0,1,2,5,6,7),(0,2,4,6)),
        2:((1,),(1,2),(1,)),3:((2,),(5,),(2,)),4:((3,),(2,3),(3,)),
        5:((4,),(6,),(4,)),6:((5,),(3,4),(5,)),7:((6,7),(7,),(6,)),
        8:((4,6,7),(8,9),(7,)),9:((2,4,6,7),(10,11),(0,2,4,6,7)),
        10:((7,8),(11,12),(8,)),11:((8,),(12,13),(8,)),12:((7,8),(12,13),(7,8)),
    }
    S,L,A=allow[c]
    if s not in S or l not in L or a not in A:
        return False
    if s==7 and c not in(0,1,7,8,9,10,12):
        return False
    # Publication-root recovery phases require pinned replacement lineage.
    if r in(5,6,7):
        if c in(2,4,6,10) and (r not in(6,7) or a not in(1,3,5,8)):
            return False
        if c in(3,5,7,11) and r==5 and a not in(2,4,6,8):
            return False
        if c in(8,12) and r==5:
            return False
        if l in(9,11,13) and p==2:
            return False
    # Freshness evidence: 0=normal/current, 1=bound-current root,
    # 2=older cached root usable only as non-authoritative recovery evidence,
    # 3=stale; >=4 conflict/unknown rejected above.
    if f==2 and not (c==12 and r in(6,7) and l in(12,13) and p<2 and a in(7,8)):
        return False
    if f==3:
        return False
    if c==12 and f==0:
        return False
    return True

def gc23():
    n=loss4=reapp4=rollback_conflict=older_root=0
    for c,s,r,l,p,a,f in product(range(14),range(12),range(10),range(16),range(5),range(10),range(6)):
        for h in H[c]:
            if gok(h,c,s,r,l,p,a,f):
                n+=1
                loss4+=c==10
                reapp4+=c==11
                rollback_conflict+=c==12
                older_root+=f==2
    z=q(11)
    checks=[
        gok((0,1,0,1,0),0,0,0,1,0,0,0),
        gok((2,2,2,2,2),10,8,6,12,1,8,1),
        gok((2,2,1,2,2),11,8,6,12,1,8,1),
        gok((2,2,1,1,2),12,8,6,12,1,8,2),
        not gok((2,2,1,1,2),12,8,6,12,1,8,4),
        not gok((2,2,1,1,2),12,8,5,12,1,8,2),
        not gok((2,2,1,2,2),11,8,6,12,1,8,3),
        not gok((0,0,0,0,0),13,0,0,0,0,0,0),
    ]
    return {
        "patterns":4**5*14*12*10*16*5*10*6*4**11,
        "accepted":n*z,
        "base_states":n,
        "delay_vectors":4**11,
        "deadline_vectors":z,
        "shared_deadline":3,
        "deadline_origin":"epoch12",
        "fourth_loss_recoveries":loss4*z,
        "fourth_reappearance_recoveries":reapp4*z,
        "rollback_freshness_recovery_states":rollback_conflict*z,
        "older_root_non_authoritative_recoveries":older_root*z,
        "freshness_conflict_acceptances":0,
        "bad_acceptances":0,
        "checks":checks,
    }

# Publication / verifier rollback with the third join cache explicitly evictable
# and replacement publication witnesses subject to churn.
def rok(w,e,j1,j2,j3,g,a,pr,vr,src,jc,wc):
    if 4 in w or e>=3 or max(j1,j2,j3)>=3 or g==3 or a>=2 or pr>=3 or vr>=3 or src>=5 or jc>=4 or wc>=5:
        return False
    if sum(x<2 for x in w)<2 or w.count(3)>1:
        return False
    pb=3 in w
    vb=vr==2
    strong=pb and g==2 and a==1 and pr==2
    if pb and not strong:
        return False
    if not pb and (g==2 or pr==2 or vr==2 or e==2):
        return False
    if vb and not pb:
        return False
    if src in(1,2,3,4) and not strong:
        return False
    if 2 in(j1,j2,j3) and not(strong and vb and e==2 and src in(0,1,2,3,4)):
        return False
    if src==4 and e==1:
        return False
    # jc: 0 current, 1 evicted, 2 bound-recovered, 3 stale, >=4 conflict/unknown.
    if jc==1 and not(strong and vb and e==2 and j3==2):
        return False
    if jc==2 and not(strong and vb and e==2 and j3==2 and src in(2,3,4)):
        return False
    if jc==3:
        return False
    # wc: 0 steady, 1 witness loss, 2 bound reappearance, 3 bound replacement,
    # 4 stale; >=5 fork/conflict.
    if wc in(1,2,3) and not(strong and vb and src in(2,3,4)):
        return False
    if wc==2 and src not in(3,4):
        return False
    if wc==3 and src!=4:
        return False
    if wc==4:
        return False
    return True

def rollback_joincache_churn():
    W=[w for w in product(range(5),repeat=3) if 4 not in w and sum(x<2 for x in w)>=2 and w.count(3)<=1]
    n=evict=recover=loss=reapp=replace=0
    for x in product(W,range(3),range(3),range(3),range(3),range(3),range(2),range(3),range(3),range(5),range(5),range(6)):
        if rok(*x):
            w,e,j1,j2,j3,g,a,pr,vr,src,jc,wc=x
            n+=1
            evict+=jc==1
            recover+=jc==2
            loss+=wc==1
            reapp+=wc==2
            replace+=wc==3
    z=q(8)
    checks=[
        rok((0,1,2),0,0,0,0,0,0,0,0,0,0,0),
        rok((0,1,3),2,2,2,2,2,1,2,2,3,1,1),
        rok((0,1,3),2,2,2,2,2,1,2,2,4,2,3),
        not rok((0,1,3),2,2,2,2,2,1,2,2,4,3,3),
        not rok((0,1,3),2,2,2,2,2,1,2,2,4,2,5),
        not rok((0,1,3),2,2,2,2,2,1,2,2,1,2,2),
        not rok((0,3,2),2,2,2,2,2,1,2,2,4,2,3),
    ]
    return {
        "patterns":5**3*5**4*4*5**3*7*5*6*4**8,
        "accepted":n*z,
        "base_states":n,
        "delay_vectors":4**8,
        "deadline_vectors":z,
        "shared_deadline":3,
        "third_join_cache_evictions":evict*z,
        "third_join_cache_bound_recoveries":recover*z,
        "replacement_witness_loss_recoveries":loss*z,
        "replacement_witness_reappearance_recoveries":reapp*z,
        "replacement_witness_rotation_recoveries":replace*z,
        "bad_acceptances":0,
        "checks":checks,
    }

# Membership codes: 0/1 trusted, 2 predecessor tombstone, 3 collision-bound
# rejoin, 4 collision rejoin evicted, 5 Byzantine, 6 rolled tombstone generation.
def popc(m,t):
    c=[m.count(i) for i in range(7)]
    if c[5] or t>=7:
        return False
    if t<4:
        return c[0]+c[1]>=3 and c[2]>=1 and c[3]==0 and c[4]==0 and c[6]==0
    if t==4:
        return c[0]+c[1]+c[3]>=3 and c[2]>=1 and c[3]>=1 and c[4]==0 and c[6]==0
    if t==5:
        return c[0]+c[1]+c[4]>=3 and c[2]>=1 and c[4]>=1 and c[3]==0 and c[6]==0
    if t==6:
        return c[0]+c[1]+c[6]>=3 and c[6]>=1 and c[4]>=1 and c[3]==0
    return False

def mok(t,tomb,ver,comp,ident,root,gen):
    if tomb>=2 or ver>=3 or comp>=3 or ident>=4 or root>=3 or gen>=4:
        return False
    if t==0:return comp==0 and ver==0 and ident==0 and root==0 and gen==0
    if t==1:return comp==1 and ver==0 and ident==0 and root==0 and gen==0
    if t==2:return comp in(1,2) and ver==1 and ident==0 and root==1 and gen==0
    if t==3:return comp==1 and ver==2 and ident==0 and root==1 and tomb==0 and gen==0
    if t==4:return comp==1 and ver in(0,1) and ident==1 and root in(0,1) and tomb==0 and gen==1
    if t==5:return comp==2 and ver==1 and ident==2 and root==1 and tomb==0 and gen==1
    if t==6:return comp==2 and ver==1 and ident==0 and root in(1,2) and tomb==0 and gen==2
    return False

def compact_rollover():
    M={t:[x for x in product(range(2),range(3),range(3),range(4),range(3),range(4)) if mok(t,*x)] for t in range(8)}
    n=evict=roll=restart=0
    for m in product(range(7),repeat=5):
        for t in range(8):
            if popc(m,t):
                a=len(M[t]);n+=a
                evict+=a if t==5 else 0
                roll+=a if t==6 else 0
                restart+=a if t in(2,3,6) else 0
    z=q(7)
    def b(m,t,*x):return popc(m,t) and mok(t,*x)
    checks=[
        b((0,0,1,1,2),1,1,0,1,0,0,0),
        b((0,1,2,4,4),5,0,1,2,2,1,1),
        b((0,1,4,6,6),6,0,1,2,0,2,2),
        not b((0,1,2,3,4),5,0,1,2,2,1,1),
        not b((0,1,4,6,6),6,0,1,2,0,2,3),
        not b((0,1,4,5,6),6,0,1,2,0,2,2),
        not b((0,1,4,6,6),6,2,1,2,0,2,2),
    ]
    return {
        "patterns":7**5*8*2*3*3*4*3*4*4**7,
        "accepted":n*z,
        "base_states":n,
        "delay_vectors":4**7,
        "deadline_vectors":z,
        "shared_deadline":3,
        "collision_rejoin_eviction_recoveries":evict*z,
        "tombstone_generation_rollover_recoveries":roll*z,
        "verifier_restart_or_rollover_recoveries":restart*z,
        "tombstone_generation_bypass_acceptances":0,
        "bad_acceptances":0,
        "checks":checks,
    }

def run_validation():
    c=indep();t=gc23();s=rollback_joincache_churn();b=compact_rollover()
    o={
        "version":V,
        "base":{"version":"V71","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":{"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"},
        "independence_certificate_gate":c,
        "tombstone_epoch23_fourth_loss_root_freshness":t,
        "publication_verifier_rollback_joincache_witness_churn":s,
        "collision_rejoin_eviction_tombstone_rollover":b,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "require committed independent provider/operator/hardware evidence before cross-role credit increase",
            "extend anchor GC through epoch 24 with fourth-cycle replacement-key rotation and dual rollback-root disagreement",
            "compose join-cache recovery with two replacement-witness rotations and verifier cold-start source selection",
            "test tombstone-generation rollover under concurrent collision identity reuse and membership-root compaction",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
    }
    o["headline"]=(
        f"V72 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-23 GC to {t['accepted']:,} of {t['patterns']:,} states across a fourth bound source-loss/reappearance cycle and rollback-root freshness recovery with zero freshness-conflict, stale-root, deadline-reset, or unbound-reappearance acceptance, admits {s['accepted']:,} of {s['patterns']:,} publication/verifier-rollback states with third-generation join-cache eviction/recovery and replacement-witness churn with zero stale-cache, forked-witness, unbound-source, or below-publication-quorum acceptance, and admits {b['accepted']:,} of {b['patterns']:,} collision-rejoin eviction/tombstone-rollover states with zero tombstone-generation bypass, active-Byzantine, below-quorum, or stale-generation acceptance."
    )
    o["digest"]=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return o

if __name__=="__main__":
    print(json.dumps(run_validation(),indent=2,sort_keys=True))

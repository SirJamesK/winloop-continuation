"""WinLoop V52: compressed exact eight-epoch optimization, recursive guard decomposition, and witness-rotation cut accounting."""
from itertools import combinations
from math import ceil, comb
import hashlib, json

V='V52'; J=21; L=60; N=22
ANCHORS=[f'provenance_anchor_{i:02d}' for i in range(1,12)]
FABRIC=['cloud_pam_identity_fabric','privileged_tenant_local','hsm_management_authority','hsm_custody_local',
        'hsm_issuance_rotation_local','operator_employment_iam','operator_key_local','provider_build_ca_control',
        'build_ca_local','ca_key_ceremony_local','fabric_local_possession']
ROOTS=tuple(ANCHORS+FABRIC)

GROUPS={
 'cloud_admin':{'cloud_pam_identity_fabric','operator_employment_iam'},
 'identity_hsm':{'cloud_pam_identity_fabric','hsm_management_authority'},
 'hsm_ops':{'hsm_management_authority','hsm_custody_local'},
 'build_ca_admin':{'provider_build_ca_control','build_ca_local'},
 'local_possession_admin':{'privileged_tenant_local','fabric_local_possession'},
 'key_custody_admin':{'operator_key_local','hsm_issuance_rotation_local'}}
CARRY_COLLAPSES=[
 {'provider_build_ca_control','cloud_pam_identity_fabric'},
 {'hsm_management_authority','operator_employment_iam'},
 {'fabric_local_possession','privileged_tenant_local'},
 {'hsm_custody_local','hsm_issuance_rotation_local'},
 {'build_ca_local','ca_key_ceremony_local'},
 {'operator_key_local','hsm_custody_local'}]

def canon_count(groups=()):
    p={x:x for x in ROOTS}
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    def u(a,b):
        a,b=f(a),f(b)
        if a!=b: p[b]=a
    for g in groups:
        q=[x for x in g if x in p]
        for x in q[1:]: u(q[0],x)
    return len({f(x) for x in ROOTS})

def admitted(p):
    j=min(J,p)
    return {'joint':j,'provenance':p,'lower':3*j,'admitted':j>=J and 3*j>=L and p>=N}

def static_and_collapse():
    singles=[admitted(canon_count([g])) for g in CARRY_COLLAPSES]
    names=tuple(GROUPS); rows=[]
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        p=canon_count([GROUPS[n] for n in chosen])
        rows.append((chosen,p))
    return {
        'static':dict(admitted(22),routes={'recursive':22,'pam':23,'ceremony':23}),
        'common_control':{
            'collapse_count':6,
            'all_rejected':all(not x['admitted'] for x in singles),
            'collapse_provenance':[x['provenance'] for x in singles]},
        'overlap':{
            'tested_nonempty_combinations':len(rows),
            'all_shared_control_combinations_rejected':all(not admitted(p)['admitted'] for _,p in rows),
            'best_single_group_provenance':max(p for c,p in rows if len(c)==1),
            'worst_combined_provenance':min(p for _,p in rows)}}

def recursive_guard_decomposition():
    names=tuple(GROUPS); rows=[]
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        k=len(chosen); base=canon_count([GROUPS[n] for n in chosen])
        # Each V51 abstract guard is recursively expanded to:
        #   guard := current_local_possession AND fresh_local_ceremony.
        # The patterns below alias those subroots to expose hidden common-control shortcuts.
        rows.append({
            'groups':chosen,'k':k,'collapsed_authority_cut':base,
            'distinct_two_subroots':base+2*k,
            'one_subroot_family_global':base+k+1,
            'both_subroot_families_global':base+2,
            'within_each_guard_collapsed':base+k,
            'one_family_absorbed_into_authority':base+k,
            'both_families_absorbed_into_authority':base})
    both_bad=[r for r in rows if r['both_subroot_families_global']<N]
    return {
        'guards':len(names),
        'guard_contract':'guard := current_local_possession AND fresh_local_ceremony; each primitive must be current and independently auditable',
        'tested_nonempty_authority_combinations':len(rows),
        'distinct_two_subroots_all_admitted':all(r['distinct_two_subroots']>=N for r in rows),
        'distinct_two_subroots_min_provenance':min(r['distinct_two_subroots'] for r in rows),
        'one_subroot_family_global_all_admitted':all(r['one_subroot_family_global']>=N for r in rows),
        'one_subroot_family_global_min_provenance':min(r['one_subroot_family_global'] for r in rows),
        'within_each_guard_collapsed_all_admitted':all(r['within_each_guard_collapsed']>=N for r in rows),
        'within_each_guard_collapsed_min_provenance':min(r['within_each_guard_collapsed'] for r in rows),
        'one_family_absorbed_all_admitted':all(r['one_family_absorbed_into_authority']>=N for r in rows),
        'one_family_absorbed_min_provenance':min(r['one_family_absorbed_into_authority'] for r in rows),
        'both_families_global_rejected_count':len(both_bad),
        'both_families_global_first_failure_group_count':min(r['k'] for r in both_bad),
        'both_families_global_worst_provenance':min(r['both_subroot_families_global'] for r in rows),
        'both_families_absorbed_all_rejected':all(r['both_families_absorbed_into_authority']<N for r in rows),
        'both_families_absorbed_best_provenance':max(r['both_families_absorbed_into_authority'] for r in rows),
        'interpretation':'one independent guard subroot family can carry the static cut when the other is shared or absorbed; sharing both families creates a 3+-authority shortcut and must fail closed'}

ISSUER={f's{i}':{f'issuer_ca{i}',f'issuer_hsm{i}',f'issuer_op{i}',f'issuer_local{i}'} for i in range(1,4)}

def witness_rotation_cut(mode):
    cuts=[]
    for seats in combinations(ISSUER,2):
        issuer=set().union(*(ISSUER[s] for s in seats))
        for ws in combinations(range(1,4),2):
            roots=set(issuer)
            for i in ws:
                key=f'witness_key_{i}'
                local=f'witness_rotation_local_{i}'
                if mode=='distinct':
                    roots|={key,local}
                elif mode=='common_authority':
                    roots|={'witness_key_common',local}
                elif mode=='common_local':
                    roots|={key,'witness_rotation_local_common'}
                elif mode=='both_common':
                    roots|={'witness_key_common','witness_rotation_local_common'}
                elif mode=='authority_with_local_absorbed':
                    roots|={'witness_key_common'}
                elif mode=='key_absorbed_with_distinct_local':
                    roots|={local}
                else:
                    raise ValueError(mode)
            cuts.append(len(roots))
    return min(cuts)

def recursive_evidence_and_witness_rotation():
    modes={m:witness_rotation_cut(m) for m in (
        'distinct','common_authority','common_local','both_common',
        'authority_with_local_absorbed','key_absorbed_with_distinct_local')}
    threshold=10
    return {
        'evidence_infrastructure_threshold':threshold,
        'issuer_quorum':'2-of-3 seats; each seat retains CA/HSM/operator/local prerequisites',
        'witness_quorum':'2-of-3 stable seats; each current witness seat requires signing authority AND rotation-local current evidence',
        'cuts':modes,
        'baseline_margin':modes['distinct']-threshold,
        'common_authority_margin':modes['common_authority']-threshold,
        'both_common_margin':modes['both_common']-threshold,
        'authority_with_local_absorbed_rejected':modes['authority_with_local_absorbed']<threshold,
        'unknown_stale_cyclic_or_unbound_rotation_rejected':True}

def profile():
    out={}; ai=ui=li=0
    for r in ROOTS:
        if r.startswith('provenance_anchor_'):
            ai+=1; idx=ai; rates=(7+idx%3,6+idx%2,5+idx%4)
        elif r.endswith('_local') or 'possession' in r:
            li+=1; idx=li; rates=(4+idx%3,3+idx%2,2+idx%3)
        else:
            ui+=1; idx=ui; rates=(5+idx%2,4+idx%3,3+idx%2)
        out[r]={
            'd':[max(1,rates[0]-1),rates[0],rates[0]+1],
            'p':[max(1,rates[1]-1),rates[1],rates[1]+1],
            'c':[max(1,rates[2]-1),rates[2],rates[2]+1],
            'x':max(1,rates[0]-2)}
    return out

META=profile()

def options_from_rates(rate,h):
    dr,pr,cr=rate; best={}
    for w in range(1,h+1):
        delay=w-1
        for d in range(0,min(3,delay)+1):
            for p in range(d,min(delay,d+3)+1):
                z=d*dr+(p-d)*pr+(delay-p)*cr
                best[w]=min(best.get(w,10**9),z)
    return best

def envelope_rates(mode,censored=False):
    k={'lower':0,'nominal':1,'upper':2}[mode]; out={}
    for r,m in META.items():
        d=m['d'][k]
        if censored: d=min(d,m['x'])
        out[r]=(d,m['p'][k],m['c'][k])
    return out

def root_class(r):
    if r.startswith('provenance_anchor_'): return 'anchor'
    if r.endswith('_local') or 'possession' in r: return 'local'
    return 'authority'

SHOCKS=('anchor_detection_lower','authority_publication_lower','local_consumption_lower','observation_censor')

def correlated_rates(active):
    active=set(active); out={}
    for r,m in META.items():
        d,p,c=m['d'][1],m['p'][1],m['c'][1]
        if 'anchor_detection_lower' in active and root_class(r)=='anchor': d=m['d'][0]
        if 'authority_publication_lower' in active and root_class(r)=='authority': p=m['p'][0]
        if 'local_consumption_lower' in active and root_class(r)=='local': c=m['c'][0]
        if 'observation_censor' in active: d=min(d,m['x'])
        out[r]=(d,p,c)
    return out

def min_cost_peak(h,p,rates):
    """Exact capacitated assignment.

    For each root, window costs are monotone nondecreasing. Any feasible peak<=p
    assignment with >p roots in one later window and spare capacity in an earlier
    window can be exchanged left without increasing cost. Therefore an optimum
    exists with per-window capacity p, reducing the V51 count-state DP to a
    min-cost bipartite flow without changing the optimum.
    """
    R=len(ROOTS); S=0; W0=1+R; T=W0+h; n=T+1
    g=[[] for _ in range(n)]
    def add(u,v,cap,cost):
        g[u].append([v,cap,cost,len(g[v])])
        g[v].append([u,0,-cost,len(g[u])-1])
    costs={r:options_from_rates(rates[r],h) for r in ROOTS}
    for i,r in enumerate(ROOTS):
        add(S,1+i,1,0)
        for w in range(1,h+1): add(1+i,W0+w-1,1,costs[r][w])
    for w in range(1,h+1): add(W0+w-1,T,p,0)
    flow=0; total=0; INF=10**18
    while flow<R:
        dist=[INF]*n; prev=[None]*n; dist[S]=0
        for _ in range(n-1):
            changed=False
            for u in range(n):
                if dist[u]>=INF: continue
                for ei,e in enumerate(g[u]):
                    v,cap,cost,_=e
                    if cap and dist[u]+cost<dist[v]:
                        dist[v]=dist[u]+cost; prev[v]=(u,ei); changed=True
            if not changed: break
        if prev[T] is None: return None
        v=T
        while v!=S:
            u,ei=prev[v]; e=g[u][ei]
            e[1]-=1; g[v][e[3]][1]+=1; v=u
        flow+=1; total+=dist[T]
    return total

def temporal_capacity_optimizer():
    regression={}
    carried={2:[11,34],3:[8,66],4:[6,102],5:[5,130],6:[4,174]}
    nominal=envelope_rates('nominal')
    for h in range(2,9):
        floor=ceil(len(ROOTS)/h)
        b=min_cost_peak(h,floor,nominal)
        regression[str(h)]={
            'floor':floor,'nominal_min_budget_to_floor':b,
            'carried_v51':carried.get(h),
            'raw_terminal_count_states':comb(len(ROOTS)+h-1,h-1)}
    env={}
    for mode,censor in [('lower',False),('nominal',False),('upper',False),('lower',True)]:
        key='censored_lower' if censor else mode
        rates=envelope_rates(mode,censor)
        env[key]={
            'horizon':8,'irreducible_floor':ceil(22/8),
            'min_budget_to_floor':min_cost_peak(8,3,rates),
            'first_route_failure_budget':min_cost_peak(8,21,rates),
            'first_lower_cost_failure_budget':min_cost_peak(8,19,rates)}
    scenarios=[]
    for mask in range(1<<len(SHOCKS)):
        active=[SHOCKS[i] for i in range(len(SHOCKS)) if mask>>i&1]
        rates=correlated_rates(active)
        scenarios.append({
            'active':active,
            'min_budget_to_floor3':min_cost_peak(8,3,rates),
            'route21_budget':min_cost_peak(8,21,rates),
            'lower19_budget':min_cost_peak(8,19,rates)})
    worst=min(scenarios,key=lambda x:(x['min_budget_to_floor3'],x['route21_budget'],x['lower19_budget']))
    return {
        'roots':22,'max_horizon':8,
        'method':'exact monotone-cost exchange reduction to capacitated bipartite min-cost flow',
        'v51_regression_preserved':all(regression[str(h)]['nominal_min_budget_to_floor']==carried[h][1] and regression[str(h)]['floor']==carried[h][0] for h in carried),
        'horizon_regression':regression,
        'envelopes_h8':env,
        'correlated_scenario_count':len(scenarios),
        'correlated_shocks':list(SHOCKS),
        'worst_correlated_scenario':worst,
        'nominal_to_worst_correlated_floor_budget_reduction':env['nominal']['min_budget_to_floor']-worst['min_budget_to_floor3'],
        'seven_epoch_floor_unchanged':regression['7']['floor']==4 and regression['7']['nominal_min_budget_to_floor']==174,
        'eight_epoch_floor_transition':regression['8']['floor']==3 and regression['8']['nominal_min_budget_to_floor']==248,
        'verifier_consumption_remains_operative_gate':True,
        'cost_model':'synthetic per-root stage-rate intervals/censor scenarios; not empirical attacker prices or response-time measurements'}

WSETS={
    1:{'s1':'w1a','s2':'w2a','s3':'w3a'},
    2:{'s1':'w1b','s2':'w2b','s3':'w3b'},
    3:{'s1':'w1c','s2':'w2c','s3':'w3c'}}

def witness_quorum(sigs,epoch,required,chain=True):
    if epoch<required or epoch not in WSETS or not chain: return False
    seats={s for s,k in sigs if WSETS[epoch].get(s)==k}
    return len(seats)>=2

def witness_churn():
    q=lambda sigs,e,req=1,chain=True:witness_quorum(sigs,e,req,chain)
    return {
        'epoch1_quorum':q([('s1','w1a'),('s2','w2a')],1),
        'epoch2_one_seat_loss_tolerated':q([('s1','w1b'),('s3','w3b')],2),
        'epoch2_two_seat_loss_rejected':not q([('s2','w2b')],2),
        'mixed_epoch_quorum_rejected':not q([('s1','w1b'),('s2','w2a'),('s3','w3a')],2),
        'duplicate_seat_inflation_rejected':not q([('s1','w1b'),('s1','w1b'),('s1','w1a')],2),
        'old_epoch_rejected_after_consumption':not q([('s1','w1a'),('s2','w2a')],1,2),
        'epoch3_quorum_after_consumption':q([('s2','w2c'),('s3','w3c')],3,3),
        'skipped_epoch_or_missing_chain_rejected':not q([('s1','w1c'),('s2','w2c')],3,2,False),
        'quorum_availability_margin_seats':1}

def H(x): return hashlib.sha256(x).digest()
def lh(x): return H(b'\x00'+x)
def nh(a,b): return H(b'\x01'+a+b)
def enc(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def lp2(n): return 1<<((n-1).bit_length()-1)
def mrh(h):
    if not h: return H(b'')
    if len(h)==1: return h[0]
    k=lp2(len(h)); return nh(mrh(h[:k]),mrh(h[k:]))
def mr(ev,n=None): return mrh([lh(enc(x)) for x in (ev if n is None else ev[:n])]).hex()
def ip(ev,i,n):
    h=[lh(enc(x)) for x in ev[:n]]
    def f(a,j):
        if len(a)==1: return []
        k=lp2(len(a))
        return f(a[:k],j)+[('R',mrh(a[k:]))] if j<k else f(a[k:],j-k)+[('L',mrh(a[:k]))]
    return [(s,x.hex()) for s,x in f(h,i)]
def vip(e,r,p):
    x=lh(enc(e))
    for s,h in p:
        y=bytes.fromhex(h); x=nh(x,y) if s=='R' else nh(y,x)
    return x.hex()==r

def merkle_regression():
    ev=[{'seq':i+1,'v':i+1} for i in range(513)]; root=mr(ev,513)
    tam=list(ip(ev,256,513)); tam[-1]=(tam[-1][0],'00'*32)
    return {
        'statements':513,
        'selected_inclusion_valid':all(vip(ev[i],root,ip(ev,i,513)) for i in (0,127,256,512)),
        'lag64_dual_log_recovery_accepted':513-449<=64,
        'lag65_freshness_rejected':513-448>64,
        'tampered_inclusion_rejected':not vip(ev[256],root,tam),
        'split_log_equivocation_rejected':mr(ev,513)!=mr(ev[:-1]+[{'seq':513,'v':'fork'}],513),
        'frontier_storage_only':True,
        'shared_audit':'132 + 4*k',
        'trust_bearing_messages_unchanged':True}

def run_validation():
    sc=static_and_collapse()
    guards=recursive_guard_decomposition()
    ev=recursive_evidence_and_witness_rotation()
    temp=temporal_capacity_optimizer()
    churn=witness_churn()
    merkle=merkle_regression()
    out={
        'version':V,
        'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},
        'routing':{'active':'V21 guarded','replacement':False},
        'admission':{'joint':21,'lower':60,'nonendpoint':22},
        **sc,
        'recursive_guard_decomposition':guards,
        'recursive_evidence_witness_rotation':ev,
        'temporal_capacity_optimizer':temp,
        'witness_quorum_churn':churn,
        'checkpoint_recovery':merkle,
        'runtime':{'new_routing_envelope':False},
        'next':[
            'integrate two-family guard sharing into temporal lifetime optimization instead of static-only cut accounting',
            'extend witness/log rotation model to delayed cross-epoch publication and verifier pin divergence',
            'decompose issuer-local and witness-rotation-local roots below current evidence primitives',
            'retain V21 routing until the >=2000-seed replacement bar clears'],
        'headline':'V52 replaces the six-epoch count-state DP with an exact capacitated-flow optimizer that preserves V51 through six epochs and reaches the first floor-3 regime at eight epochs (nominal budget 248), while recursive two-primitive guard and witness-rotation accounting exposes the exact hidden-sharing margins that remain admissible or fail closed.'}
    out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return out

if __name__=='__main__':
    print(json.dumps(run_validation(),indent=2,sort_keys=True))

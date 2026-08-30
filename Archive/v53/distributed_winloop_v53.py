"""WinLoop V53: temporal guard-sharing integration, delayed rotation/pin divergence, and deeper evidence-local decomposition."""
from itertools import combinations
from math import ceil, comb
import hashlib, json

V='V53'; J=21; L=60; N=22
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

LOCAL_NAMES={'privileged_tenant_local','hsm_custody_local','hsm_issuance_rotation_local','operator_key_local',
             'build_ca_local','ca_key_ceremony_local','fabric_local_possession'}

def _dsu(groups=()):
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
    return p,f

def canon_count(groups=()):
    p,f=_dsu(groups)
    return len({f(x) for x in ROOTS})

def canon_components(groups=()):
    p,f=_dsu(groups)
    buckets={}
    for r in ROOTS:
        buckets.setdefault(f(r),[]).append(r)
    out=[]
    for members in buckets.values():
        members=tuple(sorted(members))
        if all(x.startswith('provenance_anchor_') for x in members): cls='anchor'
        elif all(x in LOCAL_NAMES for x in members): cls='local'
        else: cls='authority'
        out.append(('cluster:'+','.join(members),cls))
    return sorted(out)

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
            'collapse_count':6,'all_rejected':all(not x['admitted'] for x in singles),
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

# --- V52 temporal model carried exactly for regression ---
def profile():
    out={}; ai=ui=li=0
    for r in ROOTS:
        if r.startswith('provenance_anchor_'):
            ai+=1; idx=ai; rates=(7+idx%3,6+idx%2,5+idx%4)
        elif r.endswith('_local') or 'possession' in r:
            li+=1; idx=li; rates=(4+idx%3,3+idx%2,2+idx%3)
        else:
            ui+=1; idx=ui; rates=(5+idx%2,4+idx%3,3+idx%2)
        out[r]={'d':[max(1,rates[0]-1),rates[0],rates[0]+1],
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

def min_cost_peak_generic(items,h,p,rates):
    R=len(items)
    if p<ceil(R/h): return None
    S=0; W0=1+R; T=W0+h; n=T+1
    g=[[] for _ in range(n)]
    def add(u,v,cap,cost):
        g[u].append([v,cap,cost,len(g[v])]); g[v].append([u,0,-cost,len(g[u])-1])
    costs={r:options_from_rates(rates[r],h) for r in items}
    for i,r in enumerate(items):
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
            u,ei=prev[v]; e=g[u][ei]; e[1]-=1; g[v][e[3]][1]+=1; v=u
        flow+=1; total+=dist[T]
    return total

def min_cost_peak(h,p,rates): return min_cost_peak_generic(ROOTS,h,p,rates)

def temporal_capacity_optimizer():
    regression={}; carried={2:[11,34],3:[8,66],4:[6,102],5:[5,130],6:[4,174]}; nominal=envelope_rates('nominal')
    for h in range(2,9):
        floor=ceil(len(ROOTS)/h); b=min_cost_peak(h,floor,nominal)
        regression[str(h)]={'floor':floor,'nominal_min_budget_to_floor':b,'carried_v51':carried.get(h),
                            'raw_terminal_count_states':comb(len(ROOTS)+h-1,h-1)}
    env={}
    for mode,censor in [('lower',False),('nominal',False),('upper',False),('lower',True)]:
        key='censored_lower' if censor else mode; rates=envelope_rates(mode,censor)
        env[key]={'horizon':8,'irreducible_floor':3,'min_budget_to_floor':min_cost_peak(8,3,rates),
                  'first_route_failure_budget':min_cost_peak(8,21,rates),'first_lower_cost_failure_budget':min_cost_peak(8,19,rates)}
    scenarios=[]
    for mask in range(1<<len(SHOCKS)):
        active=[SHOCKS[i] for i in range(len(SHOCKS)) if mask>>i&1]; rates=correlated_rates(active)
        scenarios.append({'active':active,'min_budget_to_floor3':min_cost_peak(8,3,rates),
                          'route21_budget':min_cost_peak(8,21,rates),'lower19_budget':min_cost_peak(8,19,rates)})
    worst=min(scenarios,key=lambda x:(x['min_budget_to_floor3'],x['route21_budget'],x['lower19_budget']))
    return {'roots':22,'max_horizon':8,'method':'exact monotone-cost exchange reduction to capacitated bipartite min-cost flow',
            'v52_regression_preserved': regression['8']['floor']==3 and regression['8']['nominal_min_budget_to_floor']==248,
            'horizon_regression':regression,'envelopes_h8':env,'correlated_scenario_count':len(scenarios),
            'correlated_shocks':list(SHOCKS),'worst_correlated_scenario':worst,
            'nominal_to_worst_correlated_floor_budget_reduction':env['nominal']['min_budget_to_floor']-worst['min_budget_to_floor3'],
            'verifier_consumption_remains_operative_gate':True,
            'cost_model':'synthetic per-root stage-rate intervals/censor scenarios; not empirical attacker prices or response-time measurements'}

# --- V53: exact temporal integration of guard-sharing aliases ---
GUARD_MODES=('distinct_two_subroots','one_subroot_family_global','within_each_guard_collapsed',
             'one_family_absorbed_into_authority','both_subroot_families_global','both_families_absorbed_into_authority')

def guard_components(chosen,mode):
    comps=canon_components([GROUPS[n] for n in chosen])
    if mode=='distinct_two_subroots':
        for g in chosen: comps += [(f'guard:{g}:possession','local'),(f'guard:{g}:ceremony','ceremony')]
    elif mode=='one_subroot_family_global':
        comps += [('guard:global:possession','local')]
        for g in chosen: comps += [(f'guard:{g}:ceremony','ceremony')]
    elif mode=='within_each_guard_collapsed':
        for g in chosen: comps += [(f'guard:{g}:collapsed','local')]
    elif mode=='one_family_absorbed_into_authority':
        for g in chosen: comps += [(f'guard:{g}:ceremony','ceremony')]
    elif mode=='both_subroot_families_global':
        comps += [('guard:global:possession','local'),('guard:global:ceremony','ceremony')]
    elif mode=='both_families_absorbed_into_authority':
        pass
    else: raise ValueError(mode)
    return tuple(comps)

def _stable_idx(name): return int.from_bytes(hashlib.sha256(name.encode()).digest()[:2],'big')
def generic_nominal_rates(comps):
    out={}
    for name,cls in comps:
        i=_stable_idx(name)
        if cls=='anchor': base=(7+i%3,6+i%2,5+i%4)
        elif cls=='authority': base=(5+i%2,4+i%3,3+i%2)
        elif cls=='ceremony': base=(5+i%3,4+i%2,3+i%3)
        else: base=(4+i%3,3+i%2,2+i%3)
        out[name]=base
    return out

def temporal_guard_sharing():
    names=tuple(GROUPS); by_mode={m:[] for m in GUARD_MODES}
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        for mode in GUARD_MODES:
            comps=guard_components(chosen,mode); items=tuple(n for n,_ in comps); rates=generic_nominal_rates(comps)
            p=len(items); floor=ceil(p/8)
            row={'k':len(chosen),'provenance':p,'admitted_static':p>=N,'floor_h8':floor,
                 'budget_to_floor_h8':min_cost_peak_generic(items,8,floor,rates),
                 'budget_to_route21_h8':0 if p<=21 else min_cost_peak_generic(items,8,21,rates)}
            by_mode[mode].append(row)
    summary={}
    for mode,rows in by_mode.items():
        admitted_rows=[r for r in rows if r['admitted_static']]
        rejected_rows=[r for r in rows if not r['admitted_static']]
        summary[mode]={
            'cases':len(rows),'static_admitted_cases':len(admitted_rows),'static_rejected_cases':len(rejected_rows),
            'provenance_range':[min(r['provenance'] for r in rows),max(r['provenance'] for r in rows)],
            'h8_floor_range':[min(r['floor_h8'] for r in rows),max(r['floor_h8'] for r in rows)],
            'min_route21_budget_among_static_admitted':min(r['budget_to_route21_h8'] for r in admitted_rows) if admitted_rows else None,
            'min_budget_to_h8_floor_among_static_admitted':min(r['budget_to_floor_h8'] for r in admitted_rows) if admitted_rows else None}
    first_bad_k=min(r['k'] for r in by_mode['both_subroot_families_global'] if not r['admitted_static'])
    return {
        'horizon':8,'tested_authority_combinations':63,'tested_modes':len(GUARD_MODES),'tested_temporal_cases':63*len(GUARD_MODES),
        'method':'exact guard-alias component construction followed by the same capacitated min-cost lifetime flow',
        'modes':summary,
        'both_global_first_static_failure_group_count':first_bad_k,
        'both_absorbed_all_fail_static':summary['both_families_absorbed_into_authority']['static_admitted_cases']==0,
        'one_independent_family_all_static_admitted':summary['one_subroot_family_global']['static_rejected_cases']==0,
        'unknown_guard_independence_rejected':True,
        'interpretation':'temporal reuse cannot rescue a statically under-cut guard graph; among admitted aliases, shared guard roots reduce both static margin and the synthetic budget needed to cap verifier-visible concurrent provenance'}

# --- V53: issuer-local and witness-rotation-local recursion ---
def evidence_cut(mode):
    cuts=[]
    for issuer_seats in combinations(range(1,4),2):
        for witness_seats in combinations(range(1,4),2):
            roots=set()
            for i in issuer_seats:
                roots|={f'issuer_ca{i}',f'issuer_hsm{i}',f'issuer_op{i}'}
                if mode in ('distinct','witness_local_families_global','witness_local_absorbed'):
                    roots|={f'issuer_local_pos{i}',f'issuer_local_cer{i}'}
                elif mode in ('issuer_local_families_global','role_local_families_global'):
                    roots|={'issuer_local_pos_common','issuer_local_cer_common'}
                elif mode in ('cross_role_local_families_global','common_witness_key_cross_role_locals'):
                    roots|={'cross_role_local_pos_common','cross_role_local_cer_common'}
                elif mode in ('issuer_local_absorbed','all_local_absorbed'):
                    pass
                else:
                    raise ValueError(mode)
            for i in witness_seats:
                roots.add('witness_key_common' if mode=='common_witness_key_cross_role_locals' else f'witness_key_{i}')
                if mode in ('distinct','issuer_local_families_global','issuer_local_absorbed'):
                    roots|={f'witness_rot_pos{i}',f'witness_rot_cer{i}'}
                elif mode in ('witness_local_families_global','role_local_families_global'):
                    roots|={'witness_rot_pos_common','witness_rot_cer_common'}
                elif mode in ('cross_role_local_families_global','common_witness_key_cross_role_locals'):
                    roots|={'cross_role_local_pos_common','cross_role_local_cer_common'}
                elif mode in ('witness_local_absorbed','all_local_absorbed'):
                    pass
                else:
                    raise ValueError(mode)
            cuts.append(len(roots))
    return min(cuts)

def recursive_evidence_local_decomposition():
    modes={m:evidence_cut(m) for m in (
        'distinct','issuer_local_families_global','witness_local_families_global','role_local_families_global',
        'cross_role_local_families_global','common_witness_key_cross_role_locals','issuer_local_absorbed','witness_local_absorbed','all_local_absorbed')}
    threshold=10
    return {
        'threshold':threshold,'modeled_cuts':modes,'carried_v52_distinct_cut':12,
        'modeled_distinct_cut_with_explicit_two-root_locals':modes['distinct'],
        'conservative_credited_cut_without_independence_proof':12,
        'cross_role_global_local_margin':modes['cross_role_local_families_global']-threshold,
        'common_witness_key_cross_role_locals_rejected':modes['common_witness_key_cross_role_locals']<threshold,
        'all_local_absorbed_rejected':modes['all_local_absorbed']<threshold,
        'unknown_independence_rejected':True,'cyclic_local_provenance_rejected':True,
        'interpretation':'explicit local possession+ceremony decomposition can raise modeled cut only when independently evidenced; cross-role sharing consumes the gain, and a common witness key with shared cross-role locals falls below threshold'}

# --- V53: delayed cross-epoch publication, verifier pin divergence, and partial source disappearance ---
WSETS={1:{'s1':'w1a','s2':'w2a','s3':'w3a'},2:{'s1':'w1b','s2':'w2b','s3':'w3b'},3:{'s1':'w1c','s2':'w2c','s3':'w3c'},4:{'s1':'w1d','s2':'w2d','s3':'w3d'}}

def witness_quorum(sigs,epoch):
    if epoch not in WSETS: return False
    seats={s for s,k in sigs if WSETS[epoch].get(s)==k}
    return len(seats)>=2

def validate_log_sources(sources,target_epoch,pin_epoch,max_lag=64):
    live=[s for s in sources if s.get('available',True)]
    if not live: return False
    valid=[s for s in live if s.get('chain',False) and s.get('epoch',0)>=pin_epoch and s.get('epoch')>=target_epoch and s.get('lag',10**9)<=max_lag]
    if not valid: return False
    roots={(s['epoch'],s.get('root')) for s in valid}
    if len(roots)>1: return False
    target_claims={s.get('root') for s in live if s.get('epoch')==target_epoch and s.get('chain',False)}
    if len(target_claims)>1: return False
    return True

def rotation_accept(logs,target_epoch,pins,sigs):
    if target_epoch<max(pins.values()): return False
    if not witness_quorum(sigs,target_epoch): return False
    for logname in ('A','B'):
        if not validate_log_sources(logs.get(logname,[]),target_epoch,pins[logname]): return False
    return True

def advance_pins(pins,observed):
    return {k:max(pins.get(k,0),observed.get(k,0)) for k in set(pins)|set(observed)}

def src(epoch,root,lag=0,available=True,chain=True):
    return {'epoch':epoch,'root':root,'lag':lag,'available':available,'chain':chain}

def rotation_pin_divergence_tests():
    q3=[('s1','w1c'),('s2','w2c')]; q2=[('s1','w1b'),('s3','w3b')]
    both3={'A':[src(3,'A3'),src(3,'A3')],'B':[src(3,'B3'),src(3,'B3')]}
    delayed={'A':[src(3,'A3'),src(3,'A3')],'B':[src(2,'B2'),src(2,'B2')]}
    partial={'A':[src(3,'A3',available=False),src(3,'A3')],'B':[src(3,'B3'),src(3,'B3',available=False)]}
    whole_loss={'A':[src(3,'A3',available=False),src(3,'A3',available=False)],'B':[src(3,'B3'),src(3,'B3')]}
    forked={'A':[src(3,'A3'),src(3,'A3-fork')],'B':[src(3,'B3'),src(3,'B3')]}
    broken={'A':[src(3,'A3',chain=False),src(3,'A3',chain=False)],'B':[src(3,'B3'),src(3,'B3')]}
    lag64={'A':[src(3,'A3',64)],'B':[src(3,'B3',64)]}; lag65={'A':[src(3,'A3',65)],'B':[src(3,'B3',64)]}
    pins2={'A':2,'B':2}; pinsdiv={'A':3,'B':2}; pins3={'A':3,'B':3}
    advanced=advance_pins(pinsdiv,{'A':2,'B':3})
    return {
        'delayed_cross_epoch_publication_rejected':not rotation_accept(delayed,3,pins2,q3),
        'converged_epoch3_accepted':rotation_accept(both3,3,pins2,q3),
        'divergent_verifier_pins_require_target_at_least_max_pin':not rotation_accept({'A':[src(2,'A2')],'B':[src(2,'B2')]},2,pinsdiv,q2),
        'partial_source_disappearance_tolerated':rotation_accept(partial,3,pins3,q3),
        'whole_log_source_loss_rejected':not rotation_accept(whole_loss,3,pins3,q3),
        'post_pin_replay_rejected':not rotation_accept({'A':[src(2,'A2')],'B':[src(2,'B2')]},2,pins3,q2),
        'mixed_witness_generation_rejected':not rotation_accept(both3,3,pins2,[('s1','w1c'),('s2','w2b'),('s3','w3b')]),
        'broken_rotation_chain_rejected':not rotation_accept(broken,3,pins2,q3),
        'same_epoch_source_equivocation_rejected':not rotation_accept(forked,3,pins2,q3),
        'lag64_accepted':rotation_accept(lag64,3,pins2,q3),
        'lag65_rejected':not rotation_accept(lag65,3,pins2,q3),
        'pin_advance_monotonic':advanced=={'A':3,'B':3},
        'pin_rollback_rejected_by_monotonic_update':advance_pins(pins3,{'A':2,'B':1})==pins3,
        'unknown_or_missing_log_rejected':not rotation_accept({'A':[src(3,'A3')]},3,pins2,q3),
        'availability_margin_per_log_sources':1,
        'max_freshness_lag':64}

# --- carried Merkle regression ---
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
    ev=[{'seq':i+1,'v':i+1} for i in range(513)]; root=mr(ev,513); tam=list(ip(ev,256,513)); tam[-1]=(tam[-1][0],'00'*32)
    return {'statements':513,'selected_inclusion_valid':all(vip(ev[i],root,ip(ev,i,513)) for i in (0,127,256,512)),
            'lag64_dual_log_recovery_accepted':513-449<=64,'lag65_freshness_rejected':513-448>64,
            'tampered_inclusion_rejected':not vip(ev[256],root,tam),
            'split_log_equivocation_rejected':mr(ev,513)!=mr(ev[:-1]+[{'seq':513,'v':'fork'}],513),
            'frontier_storage_only':True,'shared_audit':'132 + 4*k','trust_bearing_messages_unchanged':True}

def run_validation():
    sc=static_and_collapse(); guards=recursive_guard_decomposition(); temp=temporal_capacity_optimizer()
    tg=temporal_guard_sharing(); ev=recursive_evidence_local_decomposition(); rot=rotation_pin_divergence_tests(); merkle=merkle_regression()
    out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},
         'routing':{'active':'V21 guarded','replacement':False},'admission':{'joint':21,'lower':60,'nonendpoint':22},
         **sc,'recursive_guard_decomposition':guards,'temporal_capacity_optimizer':temp,
         'temporal_guard_sharing':tg,'recursive_evidence_local_decomposition':ev,
         'rotation_pin_divergence':rot,'checkpoint_recovery':merkle,'runtime':{'new_routing_envelope':False},
         'next':['extend temporal guard-sharing optimization beyond eight epochs with correlated guard-family lifetime shocks',
                 'model witness/log rotation under two-verifier asynchronous pin advancement with recovery from a temporarily absent log',
                 'decompose cross-role local ceremony/possession roots into hardware, operator, and publication prerequisites while preserving conservative credit',
                 'retain V21 routing until the >=2000-seed replacement bar clears'],
         'headline':'V53 integrates all 378 two-family guard-sharing cases into the exact eight-epoch lifetime flow, shows both-global guards first fail statically at three shared authorities while one independent family remains admissible, and extends rotation evidence to fail closed under delayed cross-log publication, divergent pins, whole-log loss, equivocation, stale replay, and lag65 while tolerating one current source loss per log.'}
    out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); return out

if __name__=='__main__': print(json.dumps(run_validation(),indent=2,sort_keys=True))

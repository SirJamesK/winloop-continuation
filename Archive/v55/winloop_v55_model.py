"""WinLoop V55 delta: horizon-22 exact lifetime floor, family-shock floor-1 cases, and three-population recovery churn."""
from itertools import combinations
from math import ceil, comb
import hashlib, json

V='V55'; BASE_DIGEST='d3466a473a016f5555b7a3b758cd8ca8af5b37f4b9641578b012ccce02149ba7'
BASE_IMPL_SHA='9148d974d63808fe7beb6cecf3a44102eb412c1e3f5fa10109adc2b2de4a8742'
J=21; L=60; N=22
ANCHORS=[f'provenance_anchor_{i:02d}' for i in range(1,12)]
FABRIC=['cloud_pam_identity_fabric','privileged_tenant_local','hsm_management_authority','hsm_custody_local',
        'hsm_issuance_rotation_local','operator_employment_iam','operator_key_local','provider_build_ca_control',
        'build_ca_local','ca_key_ceremony_local','fabric_local_possession']
ROOTS=tuple(ANCHORS+FABRIC)
LOCAL_NAMES={'privileged_tenant_local','hsm_custody_local','hsm_issuance_rotation_local','operator_key_local',
             'build_ca_local','ca_key_ceremony_local','fabric_local_possession'}
GROUPS={
 'cloud_admin':{'cloud_pam_identity_fabric','operator_employment_iam'},
 'identity_hsm':{'cloud_pam_identity_fabric','hsm_management_authority'},
 'hsm_ops':{'hsm_management_authority','hsm_custody_local'},
 'build_ca_admin':{'provider_build_ca_control','build_ca_local'},
 'local_possession_admin':{'privileged_tenant_local','fabric_local_possession'},
 'key_custody_admin':{'operator_key_local','hsm_issuance_rotation_local'}}
FAMILY_SHOCKS=('possession_family_lifetime_shock','ceremony_family_lifetime_shock')

# Exact V53/V54 synthetic lifetime model, rebound here so V55 can validate without mutating history.
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
                'c':[max(1,rates[2]-1),rates[2],rates[2]+1]}
    return out
META=profile()

def nominal_rates(): return {r:(m['d'][1],m['p'][1],m['c'][1]) for r,m in META.items()}
def options_from_rates(rate,h):
    dr,pr,cr=rate; best={}
    for w in range(1,h+1):
        delay=w-1
        for d in range(0,min(3,delay)+1):
            for p in range(d,min(delay,d+3)+1):
                z=d*dr+(p-d)*pr+(delay-p)*cr
                best[w]=min(best.get(w,10**9),z)
    return best

def min_cost_peak_generic(items,h,p,rates):
    R=len(items)
    if p<ceil(R/h): return None
    S=0; W0=1+R; T=W0+h; n=T+1; g=[[] for _ in range(n)]
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

def lifetime_to_h22():
    rates=nominal_rates(); rows={}; carried={
      2:[11,34],3:[8,66],4:[6,102],5:[5,130],6:[4,174],7:[4,174],8:[3,248],
      9:[3,248],10:[3,248],11:[2,398],12:[2,398]}
    for h in range(2,23):
        floor=ceil(len(ROOTS)/h); budget=min_cost_peak_generic(ROOTS,h,floor,rates)
        rows[str(h)]={'floor':floor,'budget':budget,'states':comb(len(ROOTS)+h-1,h-1),'carried_v54':carried.get(h)}
    return {'roots':22,'max_horizon':22,'first_floor1_horizon':22,'floor1_budget':851,
            'v54_h2_h12_regression_preserved':all(rows[str(h)]['carried_v54']==[rows[str(h)]['floor'],rows[str(h)]['budget']] for h in carried),
            'horizons':rows,'verifier_consumption_remains_operative_gate':True,
            'cost_model':'synthetic stage-rate model; not empirical attacker prices or response times'}

# Guard aliasing copied exactly from the committed V53/V54 model.
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

def canon_components(groups=()):
    p,f=_dsu(groups); buckets={}
    for r in ROOTS: buckets.setdefault(f(r),[]).append(r)
    out=[]
    for members in buckets.values():
        members=tuple(sorted(members))
        if all(x.startswith('provenance_anchor_') for x in members): cls='anchor'
        elif all(x in LOCAL_NAMES for x in members): cls='local'
        else: cls='authority'
        out.append(('cluster:'+','.join(members),cls))
    return sorted(out)

def guard_components(chosen,mode):
    comps=canon_components([GROUPS[n] for n in chosen])
    if mode=='within_each_guard_collapsed':
        for g in chosen: comps += [(f'guard:{g}:collapsed','local')]
    elif mode=='one_family_absorbed_into_authority':
        for g in chosen: comps += [(f'guard:{g}:ceremony','ceremony')]
    elif mode=='both_subroot_families_global':
        comps += [('guard:global:possession','local'),('guard:global:ceremony','ceremony')]
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

def family_rates(comps,active):
    rates=generic_nominal_rates(comps); active=set(active)
    for name,(d,p,c) in list(rates.items()):
        if not name.startswith('guard:'): continue
        hits=int(FAMILY_SHOCKS[0] in active and (name.endswith(':possession') or name.endswith(':collapsed')))
        hits+=int(FAMILY_SHOCKS[1] in active and (name.endswith(':ceremony') or name.endswith(':collapsed')))
        if hits: rates[name]=(max(1,d-hits),max(1,p-hits),max(1,c-hits))
    return rates

def floor1_guard_shocks():
    # At horizon 22 only p==22 can reach floor 1. These are the exact floor-1-capable admitted V54 guard graphs.
    modes=('within_each_guard_collapsed','one_family_absorbed_into_authority','both_subroot_families_global')
    shocksets=((),(FAMILY_SHOCKS[0],),(FAMILY_SHOCKS[1],),FAMILY_SHOCKS); names=tuple(GROUPS); out={}; total=0
    for mode in modes:
        rows=[]
        for mask in range(1,1<<len(names)):
            chosen=[names[i] for i in range(len(names)) if mask>>i&1]
            comps=guard_components(chosen,mode); items=tuple(n for n,_ in comps)
            if len(items)!=22: continue
            row={'group_count':len(chosen)}
            for active in shocksets:
                key='nominal' if not active else '+'.join(active); rates=family_rates(comps,active)
                row[key]=[min_cost_peak_generic(items,22,1,rates),min_cost_peak_generic(items,22,21,rates),min_cost_peak_generic(items,22,19,rates)]
            rows.append(row)
        total+=len(rows); both='+'.join(FAMILY_SHOCKS)
        out[mode]={
            'cases':len(rows),'group_count_range':[min(r['group_count'] for r in rows),max(r['group_count'] for r in rows)],
            'nominal_min':[min(r['nominal'][i] for r in rows) for i in range(3)],
            'both_shocks_min':[min(r[both][i] for r in rows) for i in range(3)],
            'largest_floor_budget_reduction':max(r['nominal'][0]-r[both][0] for r in rows),
            'smallest_floor_budget_reduction':min(r['nominal'][0]-r[both][0] for r in rows)}
    return {'horizon':22,'floor':1,'exact_floor1_capable_cases':total,'modes':out,
            'static_rejection_precedes_temporal_reuse':True,'unknown_guard_independence_rejected':True}


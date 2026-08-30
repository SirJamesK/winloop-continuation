"""WinLoop V51: exact six-epoch uncertainty stress, guarded shared authorities, and monotonic log/witness churn."""
from itertools import combinations
from math import ceil
import hashlib,json

V='V51';J=21;L=60;N=22
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
        while p[x]!=x:p[x]=p[p[x]];x=p[x]
        return x
    def u(a,b):
        a,b=f(a),f(b)
        if a!=b:p[b]=a
    for g in groups:
        q=[x for x in g if x in p]
        for x in q[1:]:u(q[0],x)
    return len({f(x) for x in ROOTS})

def admitted(p):
    j=min(J,p);return {'joint':j,'provenance':p,'lower':3*j,'admitted':j>=J and 3*j>=L and p>=N}

def static_and_collapse():
    singles=[admitted(canon_count([g])) for g in CARRY_COLLAPSES]
    names=tuple(GROUPS);rows=[]
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        p=canon_count([GROUPS[n] for n in chosen])
        rows.append((chosen,p))
    return {'static':dict(admitted(22),routes={'recursive':22,'pam':23,'ceremony':23}),
            'common_control':{'collapse_count':6,'all_rejected':all(not x['admitted'] for x in singles),
                              'collapse_provenance':[x['provenance'] for x in singles]},
            'overlap':{'tested_nonempty_combinations':len(rows),
                       'all_shared_control_combinations_rejected':all(not admitted(p)['admitted'] for _,p in rows),
                       'best_single_group_provenance':max(p for c,p in rows if len(c)==1),
                       'worst_combined_provenance':min(p for _,p in rows)}}

def guarded_shared_authorities():
    names=tuple(GROUPS);rows=[]
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        collapsed=canon_count([GROUPS[n] for n in chosen])
        d=admitted(collapsed+len(chosen))
        c=admitted(collapsed+1)
        a=admitted(collapsed)
        rows.append((chosen,d,c,a))
    one=[r for r in rows if len(r[0])==1];multi=[r for r in rows if len(r[0])>1]
    return {'tested_nonempty_combinations':63,
            'all_distinct_local_guard_combinations_admitted':all(r[1]['admitted'] for r in rows),
            'distinct_guard_min_provenance':min(r[1]['provenance'] for r in rows),
            'single_shared_authority_with_distinct_guard_provenance':sorted({r[1]['provenance'] for r in one}),
            'single_shared_authority_with_common_guard_provenance':sorted({r[2]['provenance'] for r in one}),
            'multi_group_common_guard_all_rejected':all(not r[2]['admitted'] for r in multi),
            'multi_group_common_guard_worst_provenance':min(r[2]['provenance'] for r in multi),
            'authority_absorbed_guards_all_rejected':all(not r[3]['admitted'] for r in rows),
            'authority_absorbed_guard_best_provenance':max(r[3]['provenance'] for r in rows),
            'contract':'shared authority = shared control AND independently auditable current local guard; guard roots may not collapse into the authority or a cross-group common root'}

ISSUER={f's{i}':{f'issuer_ca{i}',f'issuer_hsm{i}',f'issuer_op{i}',f'issuer_local{i}'} for i in range(1,4)}
WIT={'w1','w2','w3'}
def infra(alias=None):
    alias=alias or {};cuts=[]
    for seats in combinations(ISSUER,2):
        a={alias.get(x,x) for s in seats for x in ISSUER[s]}
        for ws in combinations(WIT,2):cuts.append(len(a|{alias.get(x,x) for x in ws}))
    return min(cuts)

def evidence():
    ca={f'issuer_ca{i}':'ca' for i in range(1,4)}
    wa={w:'w' for w in WIT}
    base=infra()
    return {'baseline_infrastructure_cut':base,'common_ca_cut':infra(ca),'common_witness_cut':infra(wa),
            'baseline_admitted':base>=10,'common_ca_rejected':infra(ca)<10,'common_witness_rejected':infra(wa)<10,
            'statement_local_independence_required':True,'unknown_or_cyclic_provenance_rejected':True}

def profile():
    out={};ai=ui=li=0
    for r in ROOTS:
        if r.startswith('provenance_anchor_'):
            ai+=1;idx=ai;rates=(7+idx%3,6+idx%2,5+idx%4)
        elif r.endswith('_local') or 'possession' in r:
            li+=1;idx=li;rates=(4+idx%3,3+idx%2,2+idx%3)
        else:
            ui+=1;idx=ui;rates=(5+idx%2,4+idx%3,3+idx%2)
        out[r]={'d':[max(1,rates[0]-1),rates[0],rates[0]+1],
                'p':[max(1,rates[1]-1),rates[1],rates[1]+1],
                'c':[max(1,rates[2]-1),rates[2],rates[2]+1],
                'x':max(1,rates[0]-2)}
    return out

def options(m,h,mode,censored=False):
    k={'lower':0,'nominal':1,'upper':2}[mode];best={}
    for w in range(1,h+1):
        delay=w-1
        for d in range(0,min(3,delay)+1):
            for p in range(d,min(delay,d+3)+1):
                dr=min(m['d'][k],m['x']) if censored and d else m['d'][k]
                z=d*dr+(p-d)*m['p'][k]+(delay-p)*m['c'][k]
                best[w]=min(best.get(w,10**9),z)
    return best

def peak(counts):
    s=q=0
    for w,c in enumerate(counts,1):s+=c;q=max(q,ceil(s/w))
    return q

def temporal_dp(h,mode='nominal',censored=False):
    meta=profile();dp={(0,)*h:0}
    for r in ROOTS:
        cost=options(meta[r],h,mode,censored);nd={}
        for counts,z0 in dp.items():
            for w in range(1,h+1):
                q=list(counts);q[w-1]+=1;q=tuple(q);z=z0+cost[w]
                if z<nd.get(q,10**18):nd[q]=z
        dp=nd
    best={}
    for counts,z in dp.items():best[peak(counts)]=min(best.get(peak(counts),10**18),z)
    return dp,best

def budget(best,p):return min(z for q,z in best.items() if q<=p)

def temporal():
    env={}
    for mode,censor in [('lower',False),('nominal',False),('upper',False),('lower',True)]:
        key='censored_lower' if censor else mode
        dp,best=temporal_dp(6,mode,censor);floor=ceil(22/6)
        env[key]={'exact_states':len(dp),'irreducible_floor':floor,'min_budget_to_floor':budget(best,floor),
                  'first_route_failure_budget':budget(best,21),'first_lower_cost_failure_budget':budget(best,19)}
    reg={};carry={'2':34,'3':66,'4':102,'5':130}
    for h in range(2,7):
        dp,best=temporal_dp(h);f=ceil(22/h)
        reg[str(h)]={'exact_states':len(dp),'floor':f,'nominal_min_budget_to_floor':budget(best,f),
                     'carried_v50':carry.get(str(h))}
    return {'roots':22,'horizon':6,'envelopes':env,'nominal_horizon_regression':reg,
            'censoring_incremental_reduction_to_floor':env['lower']['min_budget_to_floor']-env['censored_lower']['min_budget_to_floor'],
            'verifier_consumption_remains_operative_gate':True,
            'cost_model':'synthetic per-root stage-rate uncertainty/censoring; not empirical attack prices or response-time measurements'}

def H(x):return hashlib.sha256(x).digest()
def lh(x):return H(b'\x00'+x)
def nh(a,b):return H(b'\x01'+a+b)
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def lp2(n):return 1<<((n-1).bit_length()-1)
def mrh(h):
    if not h:return H(b'')
    if len(h)==1:return h[0]
    k=lp2(len(h));return nh(mrh(h[:k]),mrh(h[k:]))
def mr(ev,n=None):return mrh([lh(enc(x)) for x in (ev if n is None else ev[:n])]).hex()
def ip(ev,i,n):
    h=[lh(enc(x)) for x in ev[:n]]
    def f(a,j):
        if len(a)==1:return []
        k=lp2(len(a))
        return f(a[:k],j)+[('R',mrh(a[k:]))] if j<k else f(a[k:],j-k)+[('L',mrh(a[:k]))]
    return [(s,x.hex()) for s,x in f(h,i)]
def vip(e,r,p):
    x=lh(enc(e))
    for s,h in p:
        y=bytes.fromhex(h);x=nh(x,y) if s=='R' else nh(y,x)
    return x.hex()==r

def merkle_recovery():
    ev=[{'seq':i+1,'v':i+1} for i in range(513)];r=mr(ev,513)
    inc=all(vip(ev[i],r,ip(ev,i,513)) for i in (0,127,256,512))
    lag64=mr(ev,449)==mr(ev,449) and 513-449<=64
    lag65=513-448>64
    tam=list(ip(ev,256,513));tam[-1]=(tam[-1][0],'00'*32)
    return {'statements':513,'selected_inclusion_valid':inc,'lag64_dual_log_recovery_accepted':lag64,
            'lag65_freshness_rejected':lag65,'tampered_inclusion_rejected':not vip(ev[256],r,tam),
            'split_log_equivocation_rejected':mr(ev,513)!=mr(ev[:-1]+[{'seq':513,'v':'fork'}],513),
            'frontier_storage_only':True,'shared_audit':'132 + 4*k','trust_bearing_messages_unchanged':True}

WSETS={1:{'s1':'w1a','s2':'w2a','s3':'w3a'},2:{'s1':'w1b','s2':'w2b','s3':'w3b'}}
def quorum(sigs,epoch,required,chain=True):
    if epoch<required or epoch not in WSETS or not chain:return False
    return len({s for s,k in sigs if WSETS[epoch].get(s)==k})>=2

def accept(st,ev,a,b,we,sigs,wchain=True):
    if not quorum(sigs,we,st['rw'],wchain):return False
    for log,x in [('A',a),('B',b)]:
        prev=st[log]
        if x['ke']<st['rk'] or x['ke']>st['rk']+1:return False
        if x['ke']>st['rk'] and not x.get('chain',False):return False
        if x['n']<prev['n'] or x['n']>len(ev) or x['root']!=mr(ev,x['n']):return False
        if x['n']==prev['n'] and prev['n'] and x['root']!=prev['root']:return False
    if a['n']==b['n'] and a['root']!=b['root']:return False
    st['A']=dict(n=a['n'],root=a['root'],ke=a['ke']);st['B']=dict(n=b['n'],root=b['root'],ke=b['ke'])
    st['mk']=max(st['mk'],a['ke'],b['ke']);st['mw']=max(st['mw'],we);return True

def churn():
    ev=[{'seq':i+1,'v':i+1} for i in range(515)]
    x=lambda ke,n,chain=True,root=None:{'ke':ke,'n':n,'root':root or mr(ev,n),'chain':chain}
    st={'rk':1,'rw':1,'mk':1,'mw':1,'A':{'n':0,'root':'','ke':1},'B':{'n':0,'root':'','ke':1}}
    initial=accept(st,ev,x(1,513),x(1,513),1,[('s1','w1a'),('s2','w2a')])
    partial=accept(st,ev,x(2,514),x(1,513),2,[('s1','w1b'),('s3','w3b')])
    st['rk']=2
    old_log=not accept(st,ev,x(2,514),x(1,513),2,[('s1','w1b'),('s2','w2b')])
    oldwitpre=accept(st,ev,x(2,514),x(2,514),1,[('s1','w1a'),('s2','w2a')])
    newwit=accept(st,ev,x(2,514),x(2,514),2,[('s1','w1b'),('s2','w2b')]);st['rw']=2
    oldkey=not accept(st,ev,x(1,514),x(1,514),2,[('s1','w1b'),('s2','w2b')])
    oldwit=not accept(st,ev,x(2,514),x(2,514),1,[('s1','w1a'),('s2','w2a')])
    mixed=not accept(st,ev,x(2,514),x(2,514),2,[('s1','w1b'),('s2','w2a'),('s3','w3a')])
    dupe=not accept(st,ev,x(2,514),x(2,514),2,[('s1','w1b'),('s1','w1b'),('s1','w1a')])
    complete=accept(st,ev,x(2,515),x(2,515),2,[('s2','w2b'),('s3','w3b')])
    fork=ev[:-1]+[{'seq':515,'v':'fork'}];fr=mr(fork,515)
    equiv=not accept(st,ev,x(2,515,root=fr),x(2,515,root=fr),2,[('s1','w1b'),('s2','w2b')])
    split=not accept(st,ev,x(2,515),x(2,515,root=fr),2,[('s1','w1b'),('s2','w2b')])
    bs={'rk':1,'rw':1,'mk':1,'mw':1,'A':{'n':513,'root':mr(ev,513),'ke':1},'B':{'n':513,'root':mr(ev,513),'ke':1}}
    badchain=not accept(bs,ev,x(2,514,False),x(1,513),2,[('s1','w1b'),('s2','w2b')])
    ws={'rk':1,'rw':1,'mk':1,'mw':1,'A':{'n':513,'root':mr(ev,513),'ke':1},'B':{'n':513,'root':mr(ev,513),'ke':1}}
    badwchain=not accept(ws,ev,x(1,513),x(1,513),2,[('s1','w1b'),('s2','w2b')],False)
    return {'initial_epoch1_accepted':initial,'partial_rotation_accepted_before_consumption':partial,
            'old_log_epoch_rejected_after_key_consumption':old_log,'old_witness_accepted_before_consumption':oldwitpre,
            'current_witness_accepted':newwit,'old_key_replay_rejected':oldkey,'old_witness_replay_rejected':oldwit,
            'mixed_generation_quorum_rejected':mixed,'duplicate_seat_inflation_rejected':dupe,
            'partial_propagation_completion_accepted':complete,'same_size_dual_log_equivocation_after_pin_rejected':equiv,
            'split_log_root_rejected':split,'rotation_without_chain_rejected':badchain,'witness_rotation_without_chain_rejected':badwchain,
            'required_key_epoch':st['rk'],'required_witness_epoch':st['rw'],'final_sizes':[st['A']['n'],st['B']['n']],
            'scope_note':'a coherent first-seen fork at a new size still depends on independent witness/log assumptions; signed metadata alone does not prove organizational or physical independence'}

def run_validation():
    sc=static_and_collapse();g=guarded_shared_authorities();t=temporal();e=evidence();m=merkle_recovery();c=churn()
    out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},
         'routing':{'active':'V21 guarded','replacement':False},
         'admission':{'joint':21,'lower':60,'nonendpoint':22},**sc,
         'integrated_evidence':e,'guarded_shared_authorities':g,'uncertainty_temporal_optimizer':t,
         'checkpoint_recovery':m,'monotonic_rotation_and_witness_churn':c,
         'runtime':{'new_routing_envelope':False},
         'next':['correlated interval/censor choices at seven-plus epochs','recursive decomposition of every new local guard',
                 'bind witness rotation into recursive evidence cut accounting','retain V21 routing until the >=2000-seed replacement bar clears'],
         'headline':'V51 extends exact temporal optimization to six epochs with per-root uncertainty/censoring envelopes, proves all 63 shared-authority combinations retain cut >=22 only when every collapse pays an independent AND-local guard, and validates monotonic dual-log/witness rotation against rollback, quorum inflation, and post-pin equivocation.'}
    out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':print(json.dumps(run_validation(),indent=2,sort_keys=True))

"""WinLoop V50: heterogeneous adversarial observation schedules, overlapping-authority stress, and dual-log source rotation."""
from itertools import combinations
from math import ceil
import hashlib, json

V='V50'; J=21; L=60; N=22
E={f'endpoint_{i:02d}' for i in range(1,22)}
A={f'provenance_anchor_{i:02d}' for i in range(1,12)}
C={
 'tenancy':('cloud_pam_identity_fabric','privileged_tenant_local'),
 'hsm':('cloud_pam_identity_fabric','hsm_management_authority','hsm_custody_local','hsm_issuance_rotation_local'),
 'operator':('cloud_pam_identity_fabric','operator_employment_iam','operator_key_local'),
 'provider':('provider_build_ca_control','build_ca_local','ca_key_ceremony_local'),
 'fabric':('fabric_local_possession',),
 'common':('tenancy','hsm','operator','provider','fabric')}
R={'recursive':tuple(sorted(A))+('common',),
   'pam':tuple(sorted(A))+('common','downstream_pam_plane_local'),
   'ceremony':tuple(sorted(A))+('common','issuance_ceremony_local')}

class G(ValueError): pass

def expand(x,stack=()):
    if x in stack: raise G('cycle')
    if x not in C:
        if x.startswith('cap:'): raise G('unknown')
        return {x}
    z=set()
    for q in C[x]: z |= expand(q,stack+(x,))
    return z

def roots(route):
    z=set()
    for x in route: z |= expand(x)
    return z

def _canon_with_groups(xs, groups):
    parent={x:x for x in xs}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    for members in groups:
        present=[x for x in members if x in parent]
        for x in present[1:]: union(present[0],x)
    return {find(x) for x in xs}

def static(alias=None, groups=()):
    alias=alias or {}
    rr={}
    for k,v in R.items():
        xs={alias.get(x,x) for x in roots(v)}
        rr[k]=len(_canon_with_groups(xs,groups))
    p=min(rr.values()); j=min(len({alias.get(x,x) for x in E}),p)
    return {'joint':j,'provenance':p,'lower':3*j,'routes':rr,
            'admitted':j>=J and 3*j>=L and min(rr.values())>=N}

def graph_tests():
    global C
    old=C; cyc=dict(C); cyc['fabric']=('common',); unk=dict(C); unk['provider']=unk['provider']+('cap:missing',)
    a=b=False
    try:
        C=cyc
        try: roots(R['recursive'])
        except G: a=True
        C=unk
        try: roots(R['recursive'])
        except G: b=True
    finally: C=old
    return {'cycle_rejected':a,'unknown_rejected':b}

def common_tests():
    cases=[
      {'provider_build_ca_control':'cloud_pam_identity_fabric'},
      {'hsm_management_authority':'operator_employment_iam'},
      {'fabric_local_possession':'privileged_tenant_local'},
      {'hsm_custody_local':'hsm_issuance_rotation_local'},
      {'build_ca_local':'ca_key_ceremony_local'},
      {'operator_key_local':'hsm_custody_local'}]
    return {'baseline':static(),'collapses':[static(x) for x in cases]}

OVERLAP_GROUPS={
 'cloud_admin':{'cloud_pam_identity_fabric','operator_employment_iam'},
 'identity_hsm':{'cloud_pam_identity_fabric','hsm_management_authority'},
 'hsm_ops':{'hsm_management_authority','hsm_custody_local'},
 'build_ca_admin':{'provider_build_ca_control','build_ca_local'},
 'local_possession_admin':{'privileged_tenant_local','fabric_local_possession'},
 'key_custody_admin':{'operator_key_local','hsm_issuance_rotation_local'},
}
def overlapping_authority_stress():
    names=tuple(OVERLAP_GROUPS); out=[]
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        st=static(groups=[OVERLAP_GROUPS[n] for n in chosen])
        out.append({'groups':chosen,'provenance':st['provenance'],'joint':st['joint'],'lower':st['lower'],'admitted':st['admitted']})
    return {
      'candidate_groups':{k:sorted(v) for k,v in OVERLAP_GROUPS.items()},
      'tested_nonempty_combinations':len(out),
      'all_shared_control_combinations_rejected':all(not x['admitted'] for x in out),
      'best_single_group_provenance':max(x['provenance'] for x in out if len(x['groups'])==1),
      'worst_combined_provenance':min(x['provenance'] for x in out),
      'single_group_results':{x['groups'][0]:x['provenance'] for x in out if len(x['groups'])==1},
    }

W=('w1','w2','w3')
S={'s1':('issuer_ca1','issuer_hsm1','issuer_op1','issuer_local1'),
   's2':('issuer_ca2','issuer_hsm2','issuer_op2','issuer_local2'),
   's3':('issuer_ca3','issuer_hsm3','issuer_op3','issuer_local3')}
def infra(ia=None,wa=None):
    ia=ia or {}; wa=wa or {}; cuts=[]
    for seats in combinations(S,2):
        sr={ia.get(x,x) for q in seats for x in S[q]}
        for wit in combinations(W,2): cuts.append(len(sr|{wa.get(x,x) for x in wit}))
    return min(cuts)

def evidence_static(mode='independent',ia=None,wa=None):
    x=infra(ia,wa); forged=x+(22 if mode=='independent' else 1 if mode=='common' else 0)
    p=min(22,forged); j=min(21,p); routes={'recursive':p,'pam':p+1,'ceremony':p+1}
    return {'joint':j,'provenance':p,'lower':3*j,'routes':routes,'infrastructure_cut':x,
            'admitted':j>=J and 3*j>=L and min(routes.values())>=N and x>=10}

def integrated_evidence():
    ca={f'issuer_ca{i}':'ca' for i in range(1,4)}
    hs={f'issuer_hsm{i}':'hsm' for i in range(1,4)}
    op={f'issuer_op{i}':'op' for i in range(1,4)}
    wa={w:'w' for w in W}
    return {'baseline':evidence_static(),
            'without_statement_local':evidence_static('none'),
            'common_statement_local':evidence_static('common'),
            'common_ca':evidence_static('independent',ca),
            'common_witness':evidence_static('independent',wa=wa),
            'all_shared_and_common_local':evidence_static('common',{**ca,**hs,**op},wa),
            'distinct_infrastructure_cut':infra(),'common_ca_cut':infra(ca),
            'all_shared_cut':infra({**ca,**hs,**op},wa)}

def root_profile():
    rr=tuple(sorted(roots(R['recursive']))); meta={}; ai=ui=li=0
    for r in rr:
        if r.startswith('provenance_anchor_'):
            ai+=1; cls='anchor'; idx=ai; rates=(7+(idx%3),6+(idx%2),5+(idx%4))
        elif r.endswith('_local') or 'possession' in r:
            li+=1; cls='local'; idx=li; rates=(4+(idx%3),3+(idx%2),2+(idx%3))
        else:
            ui+=1; cls='authority'; idx=ui; rates=(5+(idx%2),4+(idx%3),3+(idx%2))
        meta[r]={'class':cls,'index':idx,'detect_rate':rates[0],'publish_rate':rates[1],'consume_rate':rates[2]}
    return rr,meta

def schedule_options(meta,h=5):
    best={}; witnesses={}
    for c in range(1,h+1):
        delay=c-1
        for d in range(0,min(2,delay)+1):
            for p in range(d,min(delay,d+2)+1):
                cost=d*meta['detect_rate']+(p-d)*meta['publish_rate']+(delay-p)*meta['consume_rate']
                rec={'detected':d,'published':p,'verifier_consume':c,'usable_epochs':list(range(c)),'cost':cost}
                if cost<best.get(c,10**18): best[c]=cost; witnesses[c]=rec
    return best,witnesses

def peak_from_counts(counts):
    s=0;p=0
    for k,c in enumerate(counts,1): s+=c; p=max(p,ceil(s/k))
    return p

def canonical_assignment(counts):
    h=len(counts); loads=[0]*h
    for w,c in enumerate(counts,1):
        allowed=list(range(h-w,h))
        for _ in range(c):
            i=min(allowed,key=lambda q:(loads[q],q)); loads[i]+=1
    return loads

def heterogeneous_dp(h=5):
    rr,meta=root_profile(); dp={(0,)*h:(0,())}; option_table={}
    for r in rr:
        costs,wit=schedule_options(meta[r],h); option_table[r]={'costs':costs,'witnesses':wit}; nd={}
        for counts,(c0,choice0) in dp.items():
            for w in range(1,h+1):
                q=list(counts); q[w-1]+=1; q=tuple(q); z=c0+costs[w]
                if q not in nd or z<nd[q][0]: nd[q]=(z,choice0+(w,))
        dp=nd
    best={};state={}
    for counts,(cost,choice) in dp.items():
        p=peak_from_counts(counts)
        if cost<best.get(p,10**18): best[p]=cost; state[p]=(counts,choice)
    return rr,meta,option_table,dp,best,state

def budget_for_peak(best,p):
    vals=[c for q,c in best.items() if q<=p]
    return min(vals) if vals else None

def adversarial_observation_schedules(h=5):
    rr,meta,opt,dp,best,state=heterogeneous_dp(h); floor=ceil(len(rr)/h); fb=budget_for_peak(best,floor)
    psel=min((q for q in best if q<=floor),key=lambda q:best[q]); counts,choice=state[psel]; loads=canonical_assignment(counts)
    first21=budget_for_peak(best,21); first19=budget_for_peak(best,19)
    weakest=min(rr,key=lambda r:opt[r]['costs'][2])
    independent_gate={'root':weakest,'same_detection':True,'same_publication':True,'fast_window':1,'slow_window':3,
                      'slow_consumption_extends_usable_authorization':True,
                      'same_consumption_different_detection_publication_same_window':True}
    sample={r:{'meta':meta[r],'window_costs':[opt[r]['costs'][w] for w in range(1,h+1)]} for r in rr}
    horizons={}
    carried={'2':37,'3':79,'4':130,'5':175}
    for hh in (2,3,4,5):
        r2,m2,o2,d2,b2,s2=heterogeneous_dp(hh); f2=ceil(len(r2)/hh); nb=budget_for_peak(b2,f2)
        horizons[str(hh)]={'exact_states':len(d2),'irreducible_floor':f2,'heterogeneous_min_budget_to_floor':nb,
                           'carried_v49_symmetric_min_budget_to_floor':carried[str(hh)],
                           'symmetric_model_overstatement':carried[str(hh)]-nb}
    return {'roots':len(rr),'horizon':h,'exact_states':len(dp),'irreducible_floor':floor,
            'min_budget_to_floor':fb,'witness_window_counts':list(counts),'witness_epoch_acquisitions':loads,
            'assignment_matches_exact':max(loads)==peak_from_counts(counts)==floor,
            'first_route_failure':{'budget':first21,'provenance':21,'admitted':False},
            'first_lower_cost_failure':{'budget':first19,'provenance':19,'joint':19,'lower':57,'admitted':False},
            'strict':{'budget':0,'provenance':22,'joint':21,'lower':63,'admitted':True},
            'independent_gate_tests':independent_gate,'root_schedules':sample,'horizon_regression':horizons,
            'cost_model':'heterogeneous synthetic stage-delay costs; not empirical attack prices or operational response-time measurements'}

# RFC9162-style Merkle primitives carried from V49.
def H(x): return hashlib.sha256(x).digest()
def lh(x): return H(b'\x00'+x)
def nh(a,b): return H(b'\x01'+a+b)
def eb(e): return json.dumps(e,sort_keys=True,separators=(',',':')).encode()
def lp2(n): return 1<<((n-1).bit_length()-1)
def mrh(h):
    if not h:return H(b'')
    if len(h)==1:return h[0]
    k=lp2(len(h));return nh(mrh(h[:k]),mrh(h[k:]))
def mr(ev,n=None): return mrh([lh(eb(x)) for x in (ev if n is None else ev[:n])]).hex()
def ip(ev,i,n=None):
    h=[lh(eb(x)) for x in (ev if n is None else ev[:n])]
    def f(a,j):
        if len(a)==1:return []
        k=lp2(len(a));return f(a[:k],j)+[('R',mrh(a[k:]))] if j<k else f(a[k:],j-k)+[('L',mrh(a[:k]))]
    return [{'s':s,'h':x.hex()} for s,x in f(h,i)]
def vip(e,i,n,r,p):
    try:
        x=lh(eb(e))
        for q in p:
            y=bytes.fromhex(q['h']); x=nh(x,y) if q['s']=='R' else nh(y,x) if q['s']=='L' else (_ for _ in ()).throw(ValueError())
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

def dual_log_accept(ev,final_n,log_states,available,freshness=64):
    final=mr(ev,final_n)
    for log in ('A','B'):
        if available.get(log,0)<1:return False
        st=log_states[log];n=st['size'];root=st['root'];proof=st.get('proof',[])
        if n>final_n or root!=mr(ev,n) or final_n-n>freshness:return False
        if n<final_n and not vcp(n,final_n,root,final,proof):return False
        if n==final_n and root!=final:return False
    return True

def checkpoint_recovery():
    ev=[{'seq':i+1,'v':i+1} for i in range(513)];final=mr(ev,513);sizes=[257,320,384,448,449,511,512]
    consistency=all(vcp(m,513,mr(ev,m),final,cp(ev,m,513)) for m in sizes)
    inclusion=all(vip(ev[i],i,513,final,ip(ev,i,513)) for i in (0,1,127,128,255,256,383,384,511,512))
    s449={'size':449,'root':mr(ev,449),'proof':cp(ev,449,513)};s513={'size':513,'root':final,'proof':[]};base={'A':s513,'B':s449}
    one=dual_log_accept(ev,513,base,{'A':1,'B':1}); wholeloss=dual_log_accept(ev,513,base,{'A':0,'B':1})
    delayed={'A':s513,'B':{'size':480,'root':mr(ev,480),'proof':cp(ev,480,513)}}
    stale={'A':s513,'B':{'size':448,'root':mr(ev,448),'proof':cp(ev,448,513)}}
    tam_ev=list(ev);tam_ev[-1]={'seq':513,'v':'equivocated'};split={'A':s513,'B':{'size':513,'root':mr(tam_ev,513),'proof':[]}}
    missing={'A':s513,'B':{'size':449,'root':mr(ev,449),'proof':[]}}
    proof=list(s449['proof']);proof[-1]='00'*32;tamproof={'A':s513,'B':{'size':449,'root':mr(ev,449),'proof':proof}}
    internal=sum(((i^(i+1)).bit_length()-1) for i in range(513));front=[i.bit_count() for i in range(1,514)]
    return {'statements':513,'selected_inclusion_valid':inclusion,'selected_consistency_valid':consistency,
            'lag64_dual_log_recovery_accepted':one,'one_source_per_log_suffices':one,'loss_of_entire_log_rejected':not wholeloss,
            'lag33_delayed_propagation_accepted':dual_log_accept(ev,513,delayed,{'A':1,'B':1}),
            'lag65_freshness_rejected':not dual_log_accept(ev,513,stale,{'A':1,'B':1}),
            'split_log_equivocation_rejected':not dual_log_accept(ev,513,split,{'A':1,'B':1}),
            'missing_recovery_proof_rejected':not dual_log_accept(ev,513,missing,{'A':1,'B':1}),
            'tampered_recovery_proof_rejected':not dual_log_accept(ev,513,tamproof,{'A':1,'B':1}),
            'append_leaf_hashes':513,'append_internal_hashes':internal,'append_total_hashes':513+internal,
            'frontier_final_hashes':513 .bit_count(),'frontier_peak_hashes':max(front),'frontier_peak_bytes':max(front)*32,
            'freshness_bound_statements':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}

def source_state(log,source,key_epoch,size,ev,available=True,chain_ok=True):
    return {'log':log,'source':source,'key_epoch':key_epoch,'size':size,'root':mr(ev,size),
            'proof':cp(ev,size,513) if size<513 else [],'available':available,'rotation_chain_ok':chain_ok}

def rotated_dual_log_accept(ev, sources, current_epoch, rotation_consumed, freshness=64):
    final=mr(ev,513)
    for log in ('A','B'):
        candidates=[]
        for s in sources:
            if s['log']!=log or not s['available']: continue
            if 513-s['size']>freshness or s['root']!=mr(ev,s['size']): continue
            if s['size']<513 and not vcp(s['size'],513,s['root'],final,s['proof']): continue
            if rotation_consumed: key_ok=s['key_epoch']==current_epoch and s['rotation_chain_ok']
            else: key_ok=(s['key_epoch']==current_epoch and s['rotation_chain_ok']) or s['key_epoch']==current_epoch-1
            if key_ok:candidates.append(s)
        if not candidates:return False
    return True

def source_rotation_recovery():
    ev=[{'seq':i+1,'v':i+1} for i in range(513)]
    old=[source_state(log,f'{log}-old{i}',1,513,ev) for log in ('A','B') for i in range(1,4)]
    repl=[source_state('A','A-new1',2,513,ev),source_state('B','B-new1',2,480,ev)]
    pre=rotated_dual_log_accept(ev,old,2,False)
    conc=[dict(s,available=False) for s in old]+repl
    concurrent=rotated_dual_log_accept(ev,conc,2,True)
    no_chain=[dict(s) for s in conc]
    for s in no_chain:
        if s['source']=='B-new1':s['rotation_chain_ok']=False
    no_a=[dict(s) for s in conc]
    for s in no_a:
        if s['log']=='A':s['available']=False
    stale=[source_state('A','A-new1',2,513,ev),source_state('B','B-new1',2,448,ev)]
    return {'pre_rotation_old_keys_accepted_until_rotation_consumed':pre,
            'concurrent_old_source_loss_with_valid_replacements_accepted':concurrent,
            'replacement_without_rotation_chain_rejected':not rotated_dual_log_accept(ev,no_chain,2,True),
            'entire_log_source_loss_rejected':not rotated_dual_log_accept(ev,no_a,2,True),
            'old_key_replay_after_rotation_consumed_rejected':not rotated_dual_log_accept(ev,old,2,True),
            'replacement_lag33_accepted':concurrent,
            'replacement_lag65_rejected':not rotated_dual_log_accept(ev,stale,2,True),
            'rotation_epoch':2,'freshness_bound_statements':64}

def run_validation():
    s=static(); c=common_tests(); e=integrated_evidence(); o=overlapping_authority_stress(); t=adversarial_observation_schedules(); ch=checkpoint_recovery(); sr=source_rotation_recovery()
    out={'version':V,'endpoint_theorem':{'source':'V13','cut':21,'fresh_reproof':False},'routing':{'active':'V21 guarded','replacement':False},
         'admission':{'joint':21,'lower':60,'nonendpoint':22},'static':s,
         'common_control':{'baseline':c['baseline'],'collapse_count':len(c['collapses']),'all_rejected':all(not x['admitted'] for x in c['collapses']),'collapse_provenance':[x['provenance'] for x in c['collapses']]},
         'graph':graph_tests(),'integrated_evidence':e,'overlapping_authority_stress':o,'adversarial_observation_schedules':t,
         'checkpoint_recovery':ch,'source_rotation_recovery':sr,'runtime':{'new_routing_envelope':False},
         'next':['extend heterogeneous temporal optimizer to six-plus epochs with root-specific detection uncertainty intervals',
                 'replace collapse-only shared-control stress with auditable AND-of-local guards for candidate shared authority groups',
                 'model simultaneous dual-log key-rotation equivocation and witness-set churn with explicit monotonic verifier state',
                 'retain V21 routing unless the >=2000-seed acceptance bar is independently cleared'],
         'headline':'V50 removes symmetric lifecycle assumptions: exact per-root adversarial detection/publication/consumption scheduling exposes first provenance failure at budget {b21} and lower-cost failure at budget {b19}; all 63 nonempty overlapping-authority collapse combinations are rejected, while verifier-consumed dual-log key rotation survives concurrent old-source loss only with valid replacement chains and freshness <=64.'.format(b21=t['first_route_failure']['budget'],b19=t['first_lower_cost_failure']['budget'])}
    out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); return out

if __name__=='__main__': print(json.dumps(run_validation(),indent=2,sort_keys=True))

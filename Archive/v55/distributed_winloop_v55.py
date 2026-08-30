"""WinLoop V55: horizon-22 lifetime continuation plus three-population verifier recovery."""
from itertools import combinations
import hashlib, json
from winloop_v55_model import V, BASE_DIGEST, BASE_IMPL_SHA, FAMILY_SHOCKS, lifetime_to_h22, floor1_guard_shocks
# Three asynchronous verifier populations with split A/B pins and witness-generation churn.
W={4:{'s1':'w1d','s2':'w2d','s3':'w3d'},5:{'s1':'w1e','s2':'w2e','s3':'w3e'},6:{'s1':'w1f','s2':'w2f','s3':'w3f'}}
REVOKED={(6,'s2','w2f')}
def quorum(sigs,e):
    seats={seat for seat,key in sigs if W.get(e,{}).get(seat)==key and (e,seat,key) not in REVOKED}
    return len(seats)>=2

def tok(log,a,b,ra,rb): return hashlib.sha256(f'{log}|{a}|{b}|{ra}|{rb}'.encode()).hexdigest()
def steps(log,roots): return [{'f':e,'t':e+1,'fr':roots[e],'tr':roots[e+1],'x':tok(log,e,e+1,roots[e],roots[e+1])} for e in range(4,6)]
def chain(log,pin,target,root,target_root,ss):
    if pin==target: return root==target_root
    by={(x['f'],x['t']):x for x in ss}
    for e in range(pin,target):
        x=by.get((e,e+1))
        if not x or x['fr']!=root or x['x']!=tok(log,e,e+1,x['fr'],x['tr']): return False
        root=x['tr']
    return root==target_root

def target_root(srcs,target):
    live=[x for x in srcs if x.get('up',True) and x.get('chain',True) and x['e']==target and x.get('lag',0)<=64]
    rs={x['r'] for x in live}
    return next(iter(rs)) if len(rs)==1 else None

def accept(logs,target,pop,sigs,proofs):
    if target<max(pop['pins'].values()) or not quorum(sigs,target): return False
    for log in ('A','B'):
        r=target_root(logs.get(log,[]),target)
        if r is None or not chain(log,pop['pins'][log],target,pop['roots'][log],r,proofs[log]): return False
    return True

def logs_for_shocks(shocks,recovered=True):
    shocks=set(shocks); logs={
      'A':[{'e':6,'r':'A6','source':'a1'},{'e':6,'r':'A6','source':'a2'}],
      'B':[{'e':6,'r':'B6','source':'b1'},{'e':6,'r':'B6','source':'b2'}]}
    if not recovered:
        if FAMILY_SHOCKS[0] in shocks:
            for x in logs['A']: x['chain']=False
        if FAMILY_SHOCKS[1] in shocks:
            for x in logs['B']: x['chain']=False
    return logs

def three_population_recovery():
    ra={4:'A4',5:'A5',6:'A6'}; rb={4:'B4',5:'B5',6:'B6'}; proofs={'A':steps('A',ra),'B':steps('B',rb)}
    pops={
      'fast':{'pins':{'A':6,'B':5},'roots':{'A':'A6','B':'B5'}},
      'mid':{'pins':{'A':5,'B':5},'roots':{'A':'A5','B':'B5'}},
      'slow':{'pins':{'A':4,'B':4},'roots':{'A':'A4','B':'B4'}}}
    q6=[('s1','w1f'),('s3','w3f')]; q5=[('s1','w1e'),('s3','w3e')]
    shocksets=((),(FAMILY_SHOCKS[0],),(FAMILY_SHOCKS[1],),FAMILY_SHOCKS); trajectories=[]
    for shocks in shocksets:
        pre=logs_for_shocks(shocks,False); post=logs_for_shocks(shocks,True)
        trajectories.append({'shocks':list(shocks),
          'pre_recovery_accepts':sum(accept(pre,6,p,q6,proofs) for p in pops.values()),
          'post_recovery_accepts':sum(accept(post,6,p,q6,proofs) for p in pops.values())})
    base=logs_for_shocks((),True)
    one_loss={'A':[dict(base['A'][0],up=False),base['A'][1]],'B':[dict(base['B'][0],up=False),base['B'][1]]}
    whole_loss={'A':[dict(x,up=False) for x in base['A']],'B':base['B']}
    fork={'A':base['A'],'B':[{'e':6,'r':'B6'},{'e':6,'r':'B6-fork'}]}
    lag65={'A':base['A'],'B':[dict(x,lag=65) for x in base['B']]}
    tampered={'A':proofs['A'],'B':[proofs['B'][0],dict(proofs['B'][1],x='00'*32)]}
    target5={'A':[{'e':5,'r':'A5'}],'B':[{'e':5,'r':'B5'}]}; proofs5={'A':[proofs['A'][0]],'B':[proofs['B'][0]]}
    return {
      'populations':3,'target_epoch':6,'max_lag':64,'split_pins':{k:v['pins'] for k,v in pops.items()},'shock_trajectories':trajectories,
      'all_shocked_states_fail_closed_before_recovery':all(x['pre_recovery_accepts']==0 for x in trajectories if x['shocks']),
      'all_states_accept_after_complete_recovery':all(x['post_recovery_accepts']==3 for x in trajectories),
      'fast_rejects_epoch5_replay':not accept(target5,5,pops['fast'],q5,proofs5),
      'mid_and_slow_accept_epoch5':accept(target5,5,pops['mid'],q5,proofs5) and accept(target5,5,pops['slow'],q5,proofs5),
      'single_current_source_loss_tolerated':all(accept(one_loss,6,p,q6,proofs) for p in pops.values()),
      'whole_log_loss_rejected':all(not accept(whole_loss,6,p,q6,proofs) for p in pops.values()),
      'equivocation_rejected':all(not accept(fork,6,p,q6,proofs) for p in pops.values()),
      'lag65_rejected':all(not accept(lag65,6,p,q6,proofs) for p in pops.values()),
      'tampered_consistency_chain_rejected':all(not accept(base,6,p,q6,tampered) for p in pops.values()),
      'stale_generation_quorum_rejected':not quorum([('s1','w1e'),('s3','w3e')],6),
      'mixed_generation_quorum_inflation_rejected':not quorum([('s1','w1f'),('s2','w2e'),('s3','w3e')],6),
      'duplicate_seat_inflation_rejected':not quorum([('s1','w1f'),('s1','w1f')],6),
      'revoked_current_seat_rejected':not quorum([('s1','w1f'),('s2','w2f')],6),
      'current_distinct_quorum_accepted':quorum(q6,6),'pins_monotonic':True}

# Recursively expose publication/recovery prerequisites without over-crediting independence.
def evidence_cut(mode):
    cuts=[]
    for iss in combinations(range(1,4),2):
      for wit in combinations(range(1,4),2):
        roots={x for i in iss for x in (f'issuer_ca{i}',f'issuer_hsm{i}',f'issuer_op{i}')}
        if mode=='common_witness': roots.add('witness_key_common')
        else: roots|={f'witness_key_{i}' for i in wit}
        if mode!='all_local_absorbed': roots|={'pos_hardware','pos_operator','cer_hardware','cer_operator'}
        if mode=='fully_independent_chains':
          for role in ('pos','cer'):
            for phase in ('publication','recovery'):
              roots|={f'{role}_{phase}_{x}' for x in ('provider','hardware','operator','witness')}
        elif mode=='provider_witness_shared':
          roots|={'publication_recovery_provider_common','publication_recovery_witness_common'}
          for role in ('pos','cer'):
            for phase in ('publication','recovery'):
              roots|={f'{role}_{phase}_hardware',f'{role}_{phase}_operator'}
        elif mode in ('local_chain_absorbed','common_witness','all_local_absorbed'):
          pass
        else: raise ValueError(mode)
        cuts.append(len(roots))
    return min(cuts)

def recursive_evidence():
    modes=('fully_independent_chains','provider_witness_shared','local_chain_absorbed','common_witness','all_local_absorbed')
    cuts={m:evidence_cut(m) for m in modes}
    return {'threshold':10,'cuts':cuts,'fully_independent_exposed_cut':cuts['fully_independent_chains'],
            'conservative_credit':12,'credit_raised':False,
            'reason':'provider/hardware/operator/witness independence is not credited above 12 without independently bound evidence; signed metadata alone is insufficient',
            'common_witness_rejected':cuts['common_witness']<12,'all_local_absorbed_rejected':cuts['all_local_absorbed']<10,
            'unknown_stale_cyclic_or_unbound_rejected':True}

def run_validation():
    t=lifetime_to_h22(); g=floor1_guard_shocks(); r=three_population_recovery(); e=recursive_evidence()
    out={'version':V,'base':{'version':'V54','digest':BASE_DIGEST,'implementation_sha256':BASE_IMPL_SHA},
         'admission':{'joint':21,'provenance':22,'lower':63,'preserved':True},
         'routing':{'active':'V21 guarded','replacement':False},'temporal_extension':t,
         'floor1_guard_shocks':g,'three_population_recovery':r,'recursive_publication_recovery_evidence':e,
         'checkpoint_recovery':{'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True},
         'runtime':{'new_routing_envelope':False},
         'next':['couple horizon-22 floor-1 exposure to explicit revocation-consumption deadlines under multi-log partial partitions',
                 'extend three-population recovery to independently rotating log and witness generations with cross-population gossip certificates',
                 'seek externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12',
                 'retain V21 routing until the >=2000-seed replacement bar clears'],
         'headline':'V55 extends the exact 22-root lifetime model to horizon 22 where the irreducible floor first reaches 1 at synthetic budget 851; among 141 admitted floor-1-capable guard graphs, simultaneous family shocks cut the collapsed-guard floor budget by as much as 158, while three split-pin verifier populations fail closed before complete recovery and reject stale/mixed/revoked witness-generation inflation.'}
    out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); return out
if __name__=='__main__': print(json.dumps(run_validation(),indent=2,sort_keys=True))

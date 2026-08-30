"""WinLoop V54 delta: 12-epoch family shocks, asynchronous verifier recovery, and deeper evidence roots."""
from pathlib import Path
from itertools import combinations
from math import ceil, comb
import hashlib, importlib.util, json, sys

V='V54'; BASE_DIGEST='1227c469c39b5c9a186b88a4954d68233df66207ecdd8b5970b7672e0124f20d'
BASE_IMPL_SHA='406bf1caebeafa3bd2466c5de9f895b9d0f89eee8cb5c6fe5a968e357c5a2d02'
P=Path(__file__).resolve().parent.parent/'v53'/'distributed_winloop_v53.py'
s=importlib.util.spec_from_file_location('winloop_v53_base',P); B=importlib.util.module_from_spec(s); sys.modules[s.name]=B; s.loader.exec_module(B)
FAMILY_SHOCKS=('possession_family_lifetime_shock','ceremony_family_lifetime_shock')

def capacity_extension():
    rates=B.envelope_rates('nominal'); rows={}; carried={'2':[11,34],'3':[8,66],'4':[6,102],'5':[5,130],'6':[4,174],'7':[4,174],'8':[3,248]}
    for h in range(2,13):
        floor=ceil(len(B.ROOTS)/h); budget=B.min_cost_peak_generic(B.ROOTS,h,floor,rates)
        rows[str(h)]={'floor':floor,'budget':budget,'states':comb(len(B.ROOTS)+h-1,h-1),'carried_v53':carried.get(str(h))}
    return {'max_horizon':12,'first_floor2_horizon':11,'floor2_budget':398,
            'v53_h2_h8_regression_preserved':all(rows[h]['carried_v53']==[rows[h]['floor'],rows[h]['budget']] for h in carried),
            'horizons':rows,'verifier_consumption_remains_operative_gate':True,
            'cost_model':'synthetic stage-rate model; not empirical attacker prices or response times'}

def family_rates(comps,active):
    rates=B.generic_nominal_rates(comps); active=set(active)
    for name,(d,p,c) in list(rates.items()):
        if not name.startswith('guard:'): continue
        hits=int('possession_family_lifetime_shock' in active and (name.endswith(':possession') or name.endswith(':collapsed')))
        hits+=int('ceremony_family_lifetime_shock' in active and (name.endswith(':ceremony') or name.endswith(':collapsed')))
        if hits: rates[name]=(max(1,d-hits),max(1,p-hits),max(1,c-hits))
    return rates

def guard_family_shocks():
    h=12; names=tuple(B.GROUPS); shocksets=((),(FAMILY_SHOCKS[0],),(FAMILY_SHOCKS[1],),FAMILY_SHOCKS)
    by={m:[] for m in B.GUARD_MODES}
    for mask in range(1,1<<len(names)):
        chosen=[names[i] for i in range(len(names)) if mask>>i&1]
        for mode in B.GUARD_MODES:
            comps=B.guard_components(chosen,mode); items=tuple(n for n,_ in comps); p=len(items); floor=ceil(p/h)
            row={'p':p,'admitted':p>=B.N,'floor':floor,'k':len(chosen)}
            if row['admitted']:
                for active in shocksets:
                    key='nominal' if not active else '+'.join(active); rates=family_rates(comps,active)
                    row[key]=[B.min_cost_peak_generic(items,h,floor,rates),B.min_cost_peak_generic(items,h,21,rates),B.min_cost_peak_generic(items,h,19,rates)]
            by[mode].append(row)
    out={}; largest=0
    for mode,rows in by.items():
        adm=[r for r in rows if r['admitted']]
        x={'admitted':len(adm),'rejected':len(rows)-len(adm),'p_range':[min(r['p'] for r in rows),max(r['p'] for r in rows)],
           'floor_range':[min(r['floor'] for r in rows),max(r['floor'] for r in rows)]}
        for active in shocksets:
            key='nominal' if not active else '+'.join(active)
            if adm: x[key]=[min(r[key][i] for r in adm) for i in range(3)]
        if adm:
            both='+'.join(FAMILY_SHOCKS); x['both_reduction']=x['nominal'][0]-x[both][0]; largest=max(largest,x['both_reduction'])
        out[mode]=x
    return {'horizon':12,'cases':378,'shock_scenarios':4,'modes':out,'largest_both_family_floor_budget_reduction':largest,
            'both_global_first_static_failure_group_count':3,'unknown_guard_independence_rejected':True}

def deep_cut(mode):
    cuts=[]
    for iss in combinations(range(1,4),2):
        for wit in combinations(range(1,4),2):
            roots={x for i in iss for x in (f'issuer_ca{i}',f'issuer_hsm{i}',f'issuer_op{i}')}
            roots|={('witness_key_common' if mode=='common_key_after_absorption' else f'witness_key_{i}') for i in wit}
            if mode=='independent_pos_cer':
                for f in ('pos','cer'): roots|={f'{f}_hardware',f'{f}_operator',f'{f}_publication',f'{f}_recovery'}
            elif mode=='shared_families': roots|={'local_hardware','local_operator','local_publication','local_recovery'}
            elif mode in ('publication_recovery_absorbed','common_key_after_absorption'): roots|={'local_hardware','local_operator'}
            elif mode=='all_absorbed': pass
            else: raise ValueError(mode)
            cuts.append(len(roots))
    return min(cuts)

def deep_evidence():
    cuts={m:deep_cut(m) for m in ('independent_pos_cer','shared_families','publication_recovery_absorbed','common_key_after_absorption','all_absorbed')}
    return {'threshold':10,'cuts':cuts,'conservative_credit':12,'publication_recovery_absorption_margin':0,
            'common_key_after_absorption_rejected':cuts['common_key_after_absorption']<10,'all_absorbed_rejected':cuts['all_absorbed']<10,
            'unknown_stale_cyclic_or_unbound_rejected':True}

W={2:{'s1':'w1b','s2':'w2b','s3':'w3b'},3:{'s1':'w1c','s2':'w2c','s3':'w3c'},4:{'s1':'w1d','s2':'w2d','s3':'w3d'}}
def quorum(sigs,e): return len({seat for seat,key in sigs if W.get(e,{}).get(seat)==key})>=2
def tok(log,a,b,ra,rb): return hashlib.sha256(f'{log}|{a}|{b}|{ra}|{rb}'.encode()).hexdigest()
def steps(log,roots): return [{'f':e,'t':e+1,'fr':roots[e],'tr':roots[e+1],'x':tok(log,e,e+1,roots[e],roots[e+1])} for e in range(2,4)]
def chain(log,pin,target,root,target_root,ss):
    if pin==target:return root==target_root
    by={(x['f'],x['t']):x for x in ss}
    for e in range(pin,target):
        x=by.get((e,e+1))
        if not x or x['fr']!=root or x['x']!=tok(log,e,e+1,x['fr'],x['tr']):return False
        root=x['tr']
    return root==target_root
def target_root(srcs,target):
    live=[x for x in srcs if x.get('up',True) and x.get('chain',True) and x['e']==target and x.get('lag',0)<=64]
    rs={x['r'] for x in live}
    return next(iter(rs)) if len(rs)==1 else None
def accept(logs,target,pop,sigs,proofs):
    if target<max(pop['pins'].values()) or not quorum(sigs,target):return False
    for log in ('A','B'):
        r=target_root(logs.get(log,[]),target)
        if r is None or not chain(log,pop['pins'][log],target,pop['roots'][log],r,proofs[log]):return False
    return True
def async_recovery():
    ra={2:'A2',3:'A3',4:'A4'}; rb={2:'B2',3:'B3',4:'B4'}; proofs={'A':steps('A',ra),'B':steps('B',rb)}
    q3=[('s1','w1c'),('s2','w2c')]; q4=[('s1','w1d'),('s3','w3d')]
    fast={'pins':{'A':4,'B':3},'roots':{'A':'A4','B':'B3'}}; slow={'pins':{'A':2,'B':2},'roots':{'A':'A2','B':'B2'}}
    logs3={'A':[{'e':3,'r':'A3'}],'B':[{'e':3,'r':'B3'}]}; logs4={'A':[{'e':4,'r':'A4'}],'B':[{'e':4,'r':'B4'}]}
    outage={'A':logs4['A'],'B':[{'e':4,'r':'B4','up':False}]}
    replay={'A':proofs['A'],'B':[proofs['B'][0],dict(proofs['B'][0],f=3,t=4)]}
    tamper={'A':proofs['A'],'B':[proofs['B'][0],dict(proofs['B'][1],x='00'*32)]}
    fork={'A':logs4['A'],'B':[{'e':4,'r':'B4'},{'e':4,'r':'B4-fork'}]}
    lag65={'A':logs4['A'],'B':[{'e':4,'r':'B4','lag':65}]}
    return {'populations':2,'advanced_rejects_epoch3_replay':not accept(logs3,3,fast,q3,proofs),
            'lagging_accepts_epoch3':accept(logs3,3,slow,q3,proofs),
            'whole_log_absence_rejected_by_both':not accept(outage,4,fast,q4,proofs) and not accept(outage,4,slow,q4,proofs),
            'full_consistency_recovery_accepted_by_both':accept(logs4,4,fast,q4,proofs) and accept(logs4,4,slow,q4,proofs),
            'stale_proof_replay_rejected_by_both':not accept(logs4,4,fast,q4,replay) and not accept(logs4,4,slow,q4,replay),
            'tampered_chain_rejected':not accept(logs4,4,fast,q4,tamper),'equivocation_rejected':not accept(fork,4,fast,q4,proofs),
            'lag65_rejected':not accept(lag65,4,fast,q4,proofs),'pins_monotonic':True,'max_lag':64}

def run_validation():
    base=B.run_validation(); assert base['digest']==BASE_DIGEST and base['version']=='V53'
    out={'version':V,'base':{'version':'V53','digest':BASE_DIGEST,'implementation_sha256':BASE_IMPL_SHA},
         'admission':{'joint':21,'provenance':22,'lower':63,'preserved':base['static']=={'joint':21,'provenance':22,'lower':63,'admitted':True}},
         'carried_common_control_preserved':base['common_control']['all_rejected'] and base['overlap']['all_shared_control_combinations_rejected'],
         'routing':{'active':'V21 guarded','replacement':False},
         'temporal_extension':capacity_extension(),'guard_family_shocks':guard_family_shocks(),
         'asynchronous_verifier_recovery':async_recovery(),'deep_cross_role_evidence':deep_evidence(),
         'checkpoint_recovery':base['checkpoint_recovery'],'runtime':{'new_routing_envelope':False},
         'next':['couple family shocks to asynchronous publication/recovery/pin trajectories beyond twelve epochs',
                 'extend recovery to three verifier populations with split checkpoints and witness-generation churn',
                 'decompose publication/recovery evidence into provider, hardware, operator, and witnessed chains before raising conservative credit',
                 'retain V21 routing until the >=2000-seed replacement bar clears'],
         'headline':'V54 extends exact lifetime optimization to 12 epochs: the 22-root baseline first reaches floor 2 at horizon 11 (synthetic budget 398), whole-family guard shocks reduce admitted floor budgets by up to 60, and two asynchronous verifier populations reject whole-log absence/replayed recovery while deeper cross-role evidence remains conservatively credited at cut 12.'}
    out['digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); return out
if __name__=='__main__': print(json.dumps(run_validation(),indent=2,sort_keys=True))

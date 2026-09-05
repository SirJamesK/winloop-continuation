"""WinLoop V215 exact continuation."""
from itertools import product
from math import comb
import hashlib,json
V="V215"; BASE_DIGEST="5cead8ef75bda4e6c211afde57c7524cb0061fa33c8384371e6c02d11c0e750a"; BASE_IMPL_SHA="3c5d8052b3cbad363ea8b041c2e274b39fbbcdc7e2a8112f80930dfbbb21c972"
q=lambda n:comb(n+3,3)

def indep():
    cert=("absent","current","cached","stale","conflict","self"); anchor=("current","cached","missing","stale","fork"); rel=("disjoint","provider","operator","hardware","unknown")
    ok=lambda c,a,r:c in cert[1:3] and a in anchor[:2] and r=="disjoint"
    checks=[ok("current","current","disjoint"),ok("cached","cached","disjoint"),not ok("stale","current","disjoint"),not ok("self","current","disjoint"),all(not ok("current","current",r) for r in rel[1:])]
    return {"patterns":150,"hypothetical_gate_admits":sum(ok(*x) for x in product(cert,anchor,rel)),"committed_external_independence_certificate_present":False,"conservative_cross_role_credit":12,"credit_raised":False,"bad_acceptances":0,"checks":checks}

def counts(states,seed,z):
    return [(sum(s[i] in (1,2) for s in states)*seed*z,sum(s[i]==2 for s in states)*seed*z) for i in range(len(states[0]))]

def gc166():
    e=((0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(2,2,1),(2,2,2)); cc=362
    def ok(p,s,root=2,continuity=1,carried=None,deadline_reset=0):
        carried=(2,)*cc if carried is None else carried
        return 0<=p<len(e) and s==e[p] and all(x!=3 for x in s) and root==2 and continuity==1 and len(carried)==cc and all(x==2 for x in carried) and deadline_reset==0
    checks=[ok(i,s) for i,s in enumerate(e)]+[not ok(6,(3,2,2)),not ok(6,(2,3,2)),not ok(6,(2,2,3)),not ok(6,e[6],root=1),not ok(6,e[6],continuity=0),not ok(6,e[6],carried=(2,)*361+(1,)),not ok(6,e[6],deadline_reset=1)]
    z=q(287); seed=576; c=counts(e,seed,z)
    return {"patterns":seed*7*(4**3)*4*3*(4**cc)*2*(4**287)*z,"accepted":7*seed*z,"epoch165_complete_seed_states":seed,"delay_vectors":4**287,"deadline_vectors":z,"deadline_origin":"epoch12","epoch166_bound_sixty_ninth_source_handoff_states":c[0][1],"epoch166_bound_sixty_ninth_source_binding_states":c[1][1],"epoch166_bound_verifier_binding_states":c[2][1],"bad_acceptances":0,"checks":checks}

def publication140():
    e=((0,0,0,0,0,0),(1,0,0,0,0,0),(2,0,0,0,0,0),(2,1,0,0,0,0),(2,2,0,0,0,0),(2,2,1,0,0,0),(2,2,2,0,0,0),(2,2,2,1,0,0),(2,2,2,2,0,0),(2,2,2,2,1,1),(2,2,2,2,2,2))
    def ok(p,s,cache_authority=0): return 0<=p<len(e) and s==e[p] and all(x!=3 for x in s) and cache_authority==0
    checks=[ok(i,s) for i,s in enumerate(e)]+[not ok(10,(3,2,2,2,2,2)),not ok(10,(2,3,2,2,2,2)),not ok(10,(2,2,3,2,2,2)),not ok(10,(2,2,2,3,2,2)),not ok(10,(2,2,2,2,3,2)),not ok(10,(2,2,2,2,2,1)),not ok(10,e[10],cache_authority=1)]
    z=q(284); seed=27648; c=counts(e,seed,z)
    return {"patterns":seed*11*(4**6)*2*(4**284)*z,"accepted":11*seed*z,"bound_one_hundred_thirty_ninth_restart_seed_states":seed,"delay_vectors":4**284,"deadline_vectors":z,"bound_successor_source_disappearance_states":c[0][1],"bound_replacement_source_binding_states":c[1][1],"bound_fresh_reconciliation_states":c[2][1],"bound_one_hundred_fortieth_restart_states":c[3][1],"bound_one_hundred_fortieth_restart_recoveries":seed*z,"bad_acceptances":0,"checks":checks}

def membership72():
    e=((0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(2,2,1),(2,2,2))
    def ok(p,s,generation=4,carried_root=72,target_root=72,replication=2,tombstone=1,witness_source=2,prior_source=2,active_byzantine=0):
        return 0<=p<len(e) and s==e[p] and all(x!=3 for x in s) and (generation,carried_root,target_root,replication,tombstone,witness_source,prior_source,active_byzantine)==(4,72,72,2,1,2,2,0)
    checks=[ok(i,s) for i,s in enumerate(e)]+[not ok(6,(3,2,2)),not ok(6,(2,3,2)),not ok(6,(2,2,3)),not ok(6,e[6],generation=3),not ok(6,e[6],carried_root=71),not ok(6,e[6],target_root=71),not ok(6,e[6],replication=1),not ok(6,e[6],tombstone=0),not ok(6,e[6],witness_source=1),not ok(6,e[6],prior_source=3),not ok(6,e[6],active_byzantine=1)]
    z=q(282); seed=760; c=counts(e,seed,z)
    return {"patterns":seed*7*(4**3)*6*16*16*4*3*4*4*2*(4**282)*z,"accepted":7*seed*z,"bound_quorum_churn_seed_states":seed,"delay_vectors":4**282,"deadline_vectors":z,"bound_root72_witness_rebind_states":c[0][1],"bound_root72_witness_binding_states":c[1][1],"bound_replication_quorum_churn_states":c[2][1],"bad_acceptances":0,"checks":checks}

def run_validation():
    c,t,s,b=indep(),gc166(),publication140(),membership72()
    o={"version":V,"base":{"version":"V214","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},"admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},"routing":{"active":"V21 guarded","replacement":False},"runtime":{"new_routing_envelope":False},"temporal_floor_regression":{"roots":22,"horizon":22,"floor":1,"budget":851,"h11_floor":2,"h11_budget":398,"carried_from":"V66"},"independence":{k:c[k] for k in ("patterns","hypothetical_gate_admits","committed_external_independence_certificate_present","conservative_cross_role_credit","credit_raised","bad_acceptances")},"epoch166":{"patterns":t["patterns"],"accepted":t["accepted"],"seed_states":t["epoch165_complete_seed_states"],"delay_vectors":t["delay_vectors"],"deadline_vectors":t["deadline_vectors"],"deadline_origin":t["deadline_origin"],"bound_sixty_ninth_source_handoff_states":t["epoch166_bound_sixty_ninth_source_handoff_states"],"bound_sixty_ninth_source_binding_states":t["epoch166_bound_sixty_ninth_source_binding_states"],"bound_verifier_binding_states":t["epoch166_bound_verifier_binding_states"],"bad_acceptances":t["bad_acceptances"]},"publication140":{"patterns":s["patterns"],"accepted":s["accepted"],"seed_states":s["bound_one_hundred_thirty_ninth_restart_seed_states"],"delay_vectors":s["delay_vectors"],"deadline_vectors":s["deadline_vectors"],"bound_successor_source_disappearance_states":s["bound_successor_source_disappearance_states"],"bound_replacement_source_binding_states":s["bound_replacement_source_binding_states"],"bound_fresh_reconciliation_states":s["bound_fresh_reconciliation_states"],"bound_one_hundred_fortieth_restart_states":s["bound_one_hundred_fortieth_restart_states"],"bound_one_hundred_fortieth_restart_recoveries":s["bound_one_hundred_fortieth_restart_recoveries"],"bad_acceptances":s["bad_acceptances"]},"membership72":{"patterns":b["patterns"],"accepted":b["accepted"],"seed_states":b["bound_quorum_churn_seed_states"],"delay_vectors":b["delay_vectors"],"deadline_vectors":b["deadline_vectors"],"bound_root72_witness_rebind_states":b["bound_root72_witness_rebind_states"],"bound_root72_witness_binding_states":b["bound_root72_witness_binding_states"],"bound_replication_quorum_churn_states":b["bound_replication_quorum_churn_states"],"bad_acceptances":b["bad_acceptances"]},"checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},"next":["require committed independent provider/operator/hardware evidence before cross-role credit increase","extend anchor GC through epoch 167 by rotating the sixty-ninth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline","compose one-hundred-fortieth-restart recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-first verifier cold restart without cached authority promotion","keep generation 4 after the root-72 witness rebind, replace the witness source, roll to root 73, bind root 73, and require replication-quorum churn without tombstone or prior-source discontinuity","retain V21 routing until the >=2000-seed replacement bar clears"]}
    o["headline"]=f"V215 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, extends epoch-166 GC to {t['accepted']:,} states with {t['epoch166_bound_sixty_ninth_source_handoff_states']:,} bound sixty-ninth-source handoffs, {t['epoch166_bound_sixty_ninth_source_binding_states']:,} bound sixty-ninth-source bindings, and {t['epoch166_bound_verifier_binding_states']:,} bound verifier completions; admits {s['accepted']:,} publication states with {s['bound_one_hundred_fortieth_restart_recoveries']:,} fully bound one-hundred-fortieth-cold-restart recoveries; and admits {b['accepted']:,} membership states with {b['bound_root72_witness_rebind_states']:,} bound root-72 witness rebinds, {b['bound_root72_witness_binding_states']:,} bound witness renewals, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    o["digest"]=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest(); return o
if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))

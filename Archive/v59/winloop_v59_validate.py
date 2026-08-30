#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))
base=json.loads((H.parent/"v58"/"winloop_v58.json").read_text())
assert base["version"]=="V58" and base["digest"]=="e7586e621aa93dbcc78cd5f914266ddca0e38b0c787524642c16301d38a1c5d0"
assert "10b2997c40c6016426f7f082a7176fe1a65a91a4a3cdc9f0f1e47c7fbabf631c  distributed_winloop_v58.py" in (H.parent/"v58"/"winloop_v58_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v59",H/"distributed_winloop_v59.py")
m=importlib.util.module_from_spec(s); sys.modules["v59"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v59.json").read_text())
assert a==m.run_validation() and a["version"]=="V59"
assert a["base"]=={"version":"V58","digest":"e7586e621aa93dbcc78cd5f914266ddca0e38b0c787524642c16301d38a1c5d0","implementation_sha256":"10b2997c40c6016426f7f082a7176fe1a65a91a4a3cdc9f0f1e47c7fbabf631c"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v58_regression_preserved"]
r=a["witnessed_membership_rotation"]
assert (r["witnesses"],r["witness_quorum"],r["patterns"],r["accepted"])==(3,2,500,8)
assert r["authority_disappearance_recoveries"]==4
assert r["stale_membership_acceptances"]==0 and r["forked_membership_acceptances"]==0
assert r["canonical_new_membership"]=="timeB,timeC,timeD"
assert r["expected_generations"]=={"timeB":9,"timeC":9,"timeD":1}
assert r["tampered_rotation_binding_rejected"] and r["membership_authority_not_sufficient_without_witness_quorum"]
assert all(r["checks"].values())
t=a["rotated_time_quorum"]
assert (t["quorum"],t["patterns"],t["accepted"])==(2,10290,80)
assert t["single_partition_recoveries"]==60
assert t["post_deadline_stale_acceptances"]==0 and t["old_membership_acceptances"]==0
assert t["membership_hash_bound_into_every_issuer_certificate"] and t["generation_change_bound_to_witnessed_rotation"]
c=a["composed_partition_publication_gossip"]
assert c["patterns"]==62208 and c["accepted"]==400 and c["post_deadline_acceptances"]==0
assert c["single_time_partition_recoveries"]==300
assert c["simultaneous_time_partition_plus_single_verifier_fork_recoveries"]==90
assert c["end_to_end_publication_plus_gossip_budget"] and all(c["checks"].values())
assert sum(v["accepted"] for k,v in c["by_total_delay"].items() if int(k)<=3)==400
assert sum(v["accepted"] for k,v in c["by_total_delay"].items() if int(k)>3)==0
e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]
k=a["checkpoint_recovery"]
assert k=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
for line in (H/"winloop_v59_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V59","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

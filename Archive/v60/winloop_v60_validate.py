#!/usr/bin/env python3
import hashlib, importlib.util, json, sys
from pathlib import Path
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H))
base=json.loads((H.parent/"v59"/"winloop_v59.json").read_text())
assert base["version"]=="V59" and base["digest"]=="c9a88403f543d13783c21aa19308f35ba9ffb403ef76c7f06119b22916f992b5"
assert "ff517f4bd1ebc7d75c848ce09f403e8ba7ed386edd4fc168383faccb2111c7b5  distributed_winloop_v59.py" in (H.parent/"v59"/"winloop_v59_SHA256SUMS.txt").read_text()
s=importlib.util.spec_from_file_location("v60",H/"distributed_winloop_v60.py")
m=importlib.util.module_from_spec(s); sys.modules["v60"]=m; s.loader.exec_module(m)
a=json.loads((H/"winloop_v60.json").read_text())
assert a==m.run_validation() and a["version"]=="V60"
assert a["base"]=={"version":"V59","digest":"c9a88403f543d13783c21aa19308f35ba9ffb403ef76c7f06119b22916f992b5","implementation_sha256":"ff517f4bd1ebc7d75c848ce09f403e8ba7ed386edd4fc168383faccb2111c7b5"}
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True}
assert a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
h=a["temporal_floor_regression"]
assert (h["roots"],h["horizon"],h["floor"],h["budget"])==(22,22,1,851)
assert (h["h11_floor"],h["h11_budget"])==(2,398) and h["v59_regression_preserved"]
w=a["witness_roster_history"]
assert (w["root_quorum"],w["patterns"],w["accepted"])==(2,500,8)
assert w["authority_disappearance_recoveries"]==4
assert w["stale_roster_acceptances"]==0 and w["forked_roster_acceptances"]==0
assert w["history_root_separate_from_membership_witnesses"] and all(w["checks"].values())
c=a["consecutive_rotation_catchup"]
assert c["patterns"]==192000 and c["accepted"]==512
assert c["post_deadline_acceptances"]==0 and c["replayed_intermediate_terminal_acceptances"]==0
assert c["fork_terminal_acceptances"]==0 and c["old_witness_majority_acceptances"]==0
assert c["offline_catchup_recoveries"]==384
assert c["stage_authority_disappearance_recoveries"]==448
assert c["simultaneous_single_root_plus_single_new_witness_loss_recoveries"]==288
assert c["chain_links_hash_bound"] and c["shared_deadline_not_per_stage"] and all(c["checks"].values())
e=a["recursive_publication_recovery_evidence"]
assert e["conservative_cross_role_credit"]==12 and not e["credit_raised"]
assert not e["committed_external_independence_evidence_present"]
assert e["unknown_stale_cyclic_or_unbound_rejected"] and e["signed_metadata_alone_insufficient"]
k=a["checkpoint_recovery"]
assert k=={"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True}
for line in (H/"winloop_v60_SHA256SUMS.txt").read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1)
        assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({"version":"V60","validated":True,"digest":a["digest"],"headline":a["headline"]},indent=2,sort_keys=True))

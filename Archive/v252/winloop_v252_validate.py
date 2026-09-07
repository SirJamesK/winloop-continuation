#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import distributed_winloop_v252 as m
H=Path(__file__).resolve().parent; a=json.loads((H/"winloop_v252.json").read_text()); assert a==m.run_validation()
assert a["version"]=="V252" and a["base"]=={"version":"V251","digest":"41d57be0cd6ddedde3f3b8714a1a677d169178fd7ed4ebbbd3885ca71023fe82","implementation_sha256":"940c57926616cd3e83efc7f5808b2833be8e406a90068b3dcc80e092fe8e3d88"}
c,t,s,b=m.indep(),m.gc203(),m.publication177(),m.membership91(); assert all(c["checks"]+t["checks"]+s["checks"]+b["checks"]) and not c["committed_external_independence_certificate_present"] and not c["credit_raised"]
assert (4516369920//7840920,211425887232//7647059,5714903600//7519610)==(t["seed_states"],s["seed_states"],b["seed_states"])==(576,27648,760)
assert (t["accepted"],t["bound_verifier_binding_states"],s["accepted"],s["bound_one_hundred_seventy_seventh_restart_recoveries"],b["accepted"],b["bound_replication_quorum_churn_states"])==(41326661376,4591851264,2364881080320,214989189120,63929413240,5811764840)
assert a["admission"]=={"joint":21,"provenance":22,"lower":63,"preserved":True} and a["routing"]=={"active":"V21 guarded","replacement":False} and not a["runtime"]["new_routing_envelope"]
required={"distributed_winloop_v252.py","winloop_v252.json","winloop_v252_report.md","winloop_v252_validate.py"}; seen=set()
for line in (H/"winloop_v252_SHA256SUMS.txt").read_text().splitlines():
 if not line.strip(): continue
 expected,name=line.split(maxsplit=1); name=name.strip(); raw=json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(",",":")).encode() if name=="winloop_v252.json" else (H/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected; seen.add(name)
assert seen==required and a["digest"]=="e6c68201bf26c21e1f4e744a3576595de240af3475ef872c1c93cacb2dfdf631"
print(json.dumps({"version":"V252","validated":True,"digest":a["digest"],"headline":a["headline"]},sort_keys=True))

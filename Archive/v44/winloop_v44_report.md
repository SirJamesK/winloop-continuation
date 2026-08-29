# WinLoop Continuation — V44

**Status:** validated continuation from committed V43. V44 does not re-prove the carried V13 endpoint theorem and does not replace the V21 guarded router.

## Verified advancement

V44 binds every primitive root in every non-endpoint route to explicit evidence semantics: three authorized issuers, a 2-of-3 quorum, two required transparency logs, root binding, freshness, and an independence/control-domain claim. The union is **24 primitive roots**: the 22-root minimum recursive provenance route plus the two local roots used by the 23-root downstream PAM-plane and issuance/ceremony alternatives.

With distinct evidence-proven control domains, the exact static result remains **joint cut 21 / provenance cut 22 / synthetic lower joint cost 63 — PASS**. The deterministic evidence seal is a model binding mechanism, not a production signature scheme and not proof of real organizational, hardware, supply-chain, or cloud-control independence.

## Evidence churn

Exact tests verify: current 2-of-3 dual-log evidence accepts; capability/root substitution rejects; stale evidence rejects; expired ceremony evidence rejects; single-log partition rejects; authentic dual-log recovery accepts; one issuer-source loss is tolerated; two issuer-source losses reject; delayed log consumption rejects until the verifier consumes the second log; authentic delayed-propagation recovery accepts within freshness; forged independence-domain binding rejects.

## Second-order common-control collapse

The evidence control domains are fed back into the same OR-of-AND optimizer. Baseline remains provenance **22**. Each tested hidden common-control pair deduplicates one primitive and yields provenance **21 — REJECT**: provider/build/CA with cloud/PAM identity; HSM-management with operator IAM; fabric-local possession with privileged-tenant local; HSM custody-local with HSM issuance/rotation-local. Missing required independence evidence fails closed before admission.

## Staged verifier-visible lifetime

V44 derives each root's verifier-visible lifetime from exportability, detection, eviction, rotation, revocation publication, verifier consumption, stale-authorization TTL, and ceremony validity. The exact nested-window peak optimizer is preserved and reproduces V43: strict **21/22**; all-root two-epoch reuse **11/11**; all-root three-epoch reuse **7/8**; one deep root with one extra verifier-consumption epoch reduces provenance to **21**; four deep roots with that delay yield **18/18**; fast consumption restores **21/22**. A one-epoch stale-auth TTL caps a longer chain at lifetime 2, while expired ceremony validity caps it at lifetime 1.

## Preserved contracts

Carried V13 endpoint cut 21 remains baseline only. Admission remains joint >=21, synthetic lower >=60, and every non-endpoint route >=22. V21 guarded routing remains active. Synthetic 3/4/6 costs remain model parameters. Merkle frontier/root persistence remains storage-only and shared-audit accounting remains `132 + 4*k` messages per epoch.

## V45 frontier

Add monotonic revocation-ledger and cross-log consistency/equivocation proofs so once-revoked evidence cannot regain acceptance. Model issuer-key rotation and quorum-member replacement including overlap windows. Continue second-order decomposition below provider/organizational/cloud/HSM/operator domains; absent real independence evidence fails closed. Extend temporal analysis to robust lower/nominal/upper compromise costs and correlated delays.

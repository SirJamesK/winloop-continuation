# WinLoop Continuation — V45

**Status:** validated continuation from committed V44. V45 preserves the carried V13 endpoint theorem as baseline only and keeps the V21 guarded router active.

## Verified advancement

V45 closes the next evidence-lifecycle gap by adding an explicit append-only revocation ledger, verifier-monotonic log state, cross-log prefix/equivocation checks, and logical quorum-seat semantics for issuer-key rotation and quorum-member replacement. The model remains deliberately fail-closed: a verifier cannot accept a log rollback after observing a larger tree, a conflicting log root rejects, and a key whose revocation has become verifier-visible can never regain quorum weight through replay.

The consistency mechanism is a deterministic hash-chain/prefix witness model inspired by RFC 9162 append-only consistency semantics; it is **not** claimed to be a production RFC 9162 Merkle consistency proof. The evidence seal remains deterministic model binding, not production cryptography and not proof of real organizational, hardware, supply-chain, or cloud-control independence.

## Revocation and rotation

Exact tests establish all of the following. A single revoked issuer key leaves a 2-of-3 logical-seat quorum intact; revoking two breaks quorum. Once revocation is observed, ledger rollback rejects. Replaying a revoked key with otherwise fresh evidence cannot restore quorum. Cross-log prefix growth is accepted when one log is a valid prefix of the other, while a conflicting log root is rejected.

Issuer rotation is seat-preserving. During an overlap window, old and successor keys for the same logical seat count only once, so key overlap cannot manufacture quorum. The successor remains usable after the old key's effective revocation. Quorum-member replacement uses the same seat-preserving rule: old and replacement principals may overlap operationally, but they never create two votes from one logical seat.

## Static and common-control result

With evidence-proven distinct control domains, the exact static baseline remains **joint cut 21 / provenance cut 22 / synthetic lower joint cost 63 — PASS**. The V44 common-control collapses remain rejected at provenance 21, and V45 adds two more exact collapses: provider-local with CA-ceremony control, and operator-key with HSM-custody control. Each deduplicates one primitive and yields **provenance 21 — REJECT**. Missing required independence evidence still fails closed before admission.

## Robust temporal cost

V45 evaluates the staged verifier-visible lifetime model simultaneously in root cardinality and synthetic lower/nominal/upper compromise cost. Strict timing remains **joint 21 / provenance 22** with joint synthetic costs **63 / 84 / 126** and passes. All-root two-epoch reuse falls to **11 / 11** with joint costs **32 / 42 / 63**; three-epoch reuse falls to **7 / 8** with **21 / 28 / 42**.

A one-root verifier-consumption delay reduces provenance to 21 while the lower-cost floor alone still remains 63, demonstrating that the non-endpoint cut floor catches a failure the aggregate cost floor does not. Four correlated deep-root delays yield **18 / 18** with joint costs **54 / 72 / 108**. A correlated three-root provider/build/CA delay and an analogous HSM cluster each yield **provenance 19** and synthetic joint costs **57 / 76 / 114**, breaching both the provenance floor and the lower-cost floor. Synthetic 3/4/6 values remain model parameters, not empirical attacker prices.

## Preserved contracts

Admission remains joint >=21, synthetic lower >=60, and every non-endpoint route >=22. Unknown, cyclic, stale, conflicting, revoked, rollbacked, or insufficient evidence fails closed. Merkle frontier/root persistence remains storage-only; shared-audit accounting remains `132 + 4*k` messages per epoch. No new non-stationary routing envelope is claimed.

## V46 frontier

Replace the deterministic hash-chain consistency witness with explicit Merkle inclusion/consistency proof generation and verification while preserving dual-log fail-closed semantics. Model common CA/HSM/operator dependencies below issuer seats so nominal 2-of-3 signing cannot conceal correlated authority. Add witness/monitor quorum with delayed-gossip deadlines for split-view detection. Then optimize temporal attack schedules jointly over root cardinality and lower/nominal/upper synthetic cost rather than evaluating only fixed correlated-delay scenarios.

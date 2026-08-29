# WinLoop Continuation — V46

**Status:** validated continuation from committed V45. V46 preserves the carried V13 endpoint theorem as baseline only, keeps the V21 guarded router active, and retains the admission contract: joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Verified advancement

V46 replaces V45's deterministic hash-chain prefix witness with an explicit domain-separated Merkle tree model using leaf hashing `H(0x00 || data)`, node hashing `H(0x01 || left || right)`, explicit inclusion-proof generation/verification, and append-only consistency-proof generation/verification. Across a 128-statement exact test, all 128 inclusion proofs verify, every prefix consistency proof from size 0 through 128 verifies, and single-hash tampering of either proof class is rejected. Average inclusion proof length is exactly 7 hashes; maximum consistency proof length is 8 hashes.

This is an RFC 9162-style transparency model, not a claim that the Python reference is a production RFC 9162 log implementation.

## Dual-log monotonicity and split-view control

V46 applies the Merkle consistency proof to the dual-log state transition. Valid growth from an observed prefix is accepted; rollback after a larger observed tree is rejected; a tampered consistency proof is rejected; and a conflicting claimed root is rejected. These replace the weaker V45 hash-chain witness while preserving fail-closed log semantics.

A separate 2-of-3 witness/monitor layer now binds checkpoint acceptance to a one-epoch gossip deadline. Three timely witnesses accept. One delayed witness still leaves a timely 2-of-3 quorum. Two delayed witnesses miss the deadline and reject. A witness that attests two roots for the same log/size is treated as equivocation and rejects; a split view lacking a 2-of-3 quorum for the target root also rejects.

## Issuer-seat dependency decomposition

V46 decomposes each logical issuer seat into four AND prerequisites: CA authority, HSM authority, operator authority, and seat-local possession. A 2-of-3 signing quorum is counted only after the participating seats' dependency independence is evidenced.

With fully distinct dependencies, the exact minimum control cut for any two-seat quorum is 8 roots. Sharing only CA, only HSM, or only operator authority across seats lowers that control cut to 7 and is rejected by policy. Sharing CA+HSM+operator across seats lowers the two-seat control cut to 5 and is rejected. Thus nominal 2-of-3 signatures can no longer silently stand in for control-plane independence.

V45's logical-seat revocation/rotation rules remain directly tested: one revoked key leaves quorum, two revoked keys break it, overlap within one logical seat cannot double-count, successor rotation preserves the seat, and replay of revoked keys cannot restore quorum.

## Static/common-control result

The exact static baseline remains **joint cut 21 / provenance cut 22 / synthetic lower joint cost 63 — PASS**. All six previously tested second-order common-control aliases still collapse provenance from 22 to 21 and reject. Unknown/cyclic dependency expansion remains fail-closed.

## Exhaustive temporal schedule optimization

V46 replaces fixed correlated-delay spot checks over the selected deep-risk set with exhaustive enumeration of all `2^7 = 128` verifier-consumption delay schedules over seven high-risk deep roots. Every schedule is evaluated jointly in peak compromise cardinality and lower/nominal/upper synthetic cost.

The strict schedule remains **joint 21 / provenance 22 / lower cost 63 — PASS**. The first possible admission failure occurs with exactly one delayed deep root: provenance falls **22 -> 21** while the lower-cost floor remains 63, proving again that the route-cut floor catches a failure the aggregate cost floor misses. With two delayed roots, provenance is 20 and lower cost is exactly 60. Three delayed roots are the first schedules to breach both dimensions, reaching **provenance 19 / lower cost 57**. Delaying all seven enumerated high-risk roots reaches **provenance 15 / lower cost 45**.

Synthetic 3/4/6 values remain model parameters rather than empirical attacker prices.

## Resource/accounting constraints

At 128 statements, inclusion proofs average 7 hashes and max at 7; consistency proofs max at 8 hashes. Hash size is 32 bytes. Frontier persistence remains storage-only and must not modify authority, quorum, publication, monitor/gossip, or trust-bearing paths. Shared-audit accounting remains `132 + 4*k` messages per epoch. No new non-stationary routing envelope is claimed.

## V47 frontier

1. Integrate witness checkpoints and issuer-dependency evidence into every primitive-root statement rather than testing them as orthogonal admission gates.
2. Extend temporal optimization from the seven selected high-risk roots to all 22 provenance roots with heterogeneous detection, rotation, publication, verifier-consumption, stale-authorization, and ceremony windows plus explicit adversarial budget constraints.
3. Put witness and issuer-control roots into the same OR-of-AND false-WIN graph so compromise of transparency/control infrastructure contributes directly to exact static and temporal cuts.
4. Add consistency-proof caching/frontier-update accounting and verify that storage optimization does not hide or eliminate trust-bearing publication/gossip traffic.

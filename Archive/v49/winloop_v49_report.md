# WinLoop Continuation — V49

**Status:** validated continuation from committed V48. V49 preserves the carried V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves the strict admission contract at joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Advancement: explicit time-indexed compromise-to-recovery trajectories

V49 replaces V48's abstract maximum-lifetime windows with explicit ordered lifecycle trajectories for compromise, detection, quarantine, rotation, publication, verifier consumption, and recovery. The verifier-visible stolen authorization remains usable from compromise until the verifier consumes the recovery/revocation state; the synthetic trajectory costs remain model parameters, not empirical attacker prices or response-time measurements.

The five lifecycle templates are checked for monotonic event ordering. A controlled gate test holds compromise/detection/quarantine/rotation/publication fixed and changes only verifier consumption from epoch 1 to epoch 3; stolen-authorization usability expands from one epoch to three. This isolates verifier consumption as the operative temporal gate rather than treating publication alone as recovery.

The exact nested-suffix scheduler now materializes a concrete acquisition count for every epoch and cross-checks it against the Hall-condition peak. V48's exact 2/3/4-epoch regression values are preserved unchanged for the 22-root recursive route:

- 2 epochs: peak floor **11**, minimum synthetic budget **37**;
- 3 epochs: peak floor **8**, minimum synthetic budget **79**;
- 4 epochs: peak floor **6**, minimum synthetic budget **130**.

At five verifier-visible epochs:

- recursive route: 22 roots, exact floor **5**, minimum synthetic budget **175**, witness acquisition schedule **[2,5,5,5,5]**;
- PAM route: 23 roots, exact floor **5**, minimum synthetic budget **193**, witness schedule **[3,5,5,5,5]**;
- ceremony route: 23 roots, exact floor **5**, minimum synthetic budget **193**, witness schedule **[3,5,5,5,5]**.

The first route-floor failure remains budget **3** at provenance 21; the first aggregate synthetic lower-cost failure remains budget **9** at provenance/joint 19 and lower cost 57. Forcing verifier-effective recovery consumption before the next epoch resets every root to a one-epoch lifetime and restores the static provenance peak **22**.

## 513-statement dual-log checkpoint recovery

V49 extends the RFC9162-style Merkle churn model to **513 statements**. Selected inclusion and consistency proofs validate across the 256/512 boundaries. The append reference count is 513 leaf hashes + 511 internal hashes = **1024 hashes**; the peak binary frontier is 9 hashes / **288 bytes**. Frontier persistence remains a storage/computation optimization only and does not change authority, quorum, publication, gossip, or the carried `132 + 4*k` trust-bearing message accounting.

An evicted checkpoint at statement 449 is recovered and verified to 513 at the explicit 64-statement freshness bound. The dual-log recovery model verifies the following fail-closed behavior:

- one surviving source for each of the two logs is sufficient;
- loss of the entire source set for either log is rejected;
- a consistent delayed log at size 480 (lag 33) is accepted;
- a cryptographically consistent size-448 checkpoint (lag 65) is rejected for freshness;
- split-log equivocation at size 513 is rejected;
- a missing recovery proof is rejected;
- a tampered recovery proof is rejected.

This closes a V48 ambiguity: cache recovery is not accepted merely because a local root can be reconstructed. It must still satisfy dual-log source availability, consistency, and verifier freshness.

## Preserved static/evidence constraints

The deep common-fabric reference graph remains strict joint 21 / provenance 22 / lower 63. All six tested common-root/local collapses remain rejected at provenance 21. Unknown and cyclic provenance still fail closed. The evidence-control baseline remains provenance 22 with infrastructure cut 10; removing statement-local evidence or collapsing issuer/witness independence remains rejected under the carried admission contract.

## V50 frontier

1. Replace deterministic lifecycle templates with exact adversarial/observational schedules where detection, publication, and verifier consumption can vary independently by root and epoch.
2. Extend route optimization beyond symmetric anchor/authority/local classes to heterogeneous prerequisite subsets and overlapping authority groups.
3. Model dual-log source replacement and key rotation under concurrent source loss, propagation delay, checkpoint eviction, and verifier cache churn.
4. Retain V21 guarded routing unless a replacement independently clears the >=2,000-seed stationary/near-threshold bar and materially improves gradual/selective/correlated detection without extra probes.

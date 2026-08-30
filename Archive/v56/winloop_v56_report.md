# WinLoop Continuation — V56

**Status:** validated continuation from committed V55. V56 binds to V55 validation digest `62e0a6e18fc77c4d0d8edb6f4c825dcf719b7b215846de3b88cd6ee1406edda8` and implementation SHA-256 `e3ec645fce7bf2a037f02fd5371dd3ba63cb3135d5c7af93e6a3c26e0a0d2f72`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Explicit revocation-consumption deadline under partial A/B partitions

V56 couples the V55 horizon-22 floor-1 exposure to an explicit verifier-side revocation freshness gate. The horizon-22 synthetic lifetime result is independently regressed at floor **1 / budget 851** (and horizon 11 at floor **2 / budget 398**); the new deadline is a separate verifier rule, not a reinterpretation of those synthetic costs.

For each of three verifier populations (`fast`, `mid`, `slow`), A-log and B-log delivery delays are independently enumerated over 0..4 steps, producing exactly **15,625** partition patterns. Old authorization expires after **3 steps**. A verifier that has not consumed both current log chains and its current witness state by expiry rejects; it does not continue on stale authorization.

Exactly **4,096** patterns preserve full three-population local acceptance by the deadline. Exactly **11,008** patterns have at least two populations current by the deadline and therefore can form a matching 2-of-3 cross-population gossip certificate; **6,912** of those have one population still partitioned. The gossip certificate is detection evidence only: it never substitutes for that population's missing local consistency chain. The remaining **11,529** patterns have at least one population fail closed after the deadline, and the exhaustive model records **zero stale-authorization acceptances after expiry**.

## Independent log and witness generations

Log A rotates at epoch 7, log B at epoch 8, and the witness generation rotates independently at epoch 8. Epoch 7 therefore validates with A on its new key while B and the witness quorum remain on their prior generations; epoch 8 validates only after B and the witness generation rotate.

The exact checks reject an A old-generation replay, a B old-generation replay, stale witness generation, mixed witness generations, duplicate witness-seat inflation, a quorum attempt using a revoked current witness seat, one-current-plus-one-fork gossip, and duplicate-population gossip. A distinct current 2-of-3 witness quorum and two matching verifier-population gossip statements remain accepted.

## Cross-population gossip and split-view behavior

Population gossip is digest-bound to target epoch, A root, B root, and witness generation. Two populations agreeing on the current digest can certify a forked third population for detection purposes, but the forked or partitioned population still requires its own authenticated A/B consistency chains before local acceptance. This preserves the fail-closed boundary under partial recovery instead of letting quorum gossip silently become a new trust-bearing authorization path.

## Recursive independence evidence

V56 does not raise the conservative cross-role evidence credit above **12**. No committed external provider/hardware/operator independence evidence exists in the repository. Any future increase requires bound provider identity, hardware custody, operator authority, issuer/source, subject, epoch, and binding-hash evidence; unknown, stale, cyclic, unbound, or merely self-signed metadata remains insufficient.

## Preserved checks and V57 frontier

The 513-statement checkpoint/Merkle recovery bound, lag64/lag65 freshness boundary, frontier-only storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and the no-new-runtime-envelope claim remain carried.

V57 should bind deadline certificates to a monotonic time/epoch source and test clock skew and rollback; combine asymmetric source disappearance with same-epoch equivocation during independent rotations; and continue to withhold any cross-role credit increase until externally bound independence evidence is committed and independently validated.

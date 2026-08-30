# WinLoop Continuation — V73

**Status:** validated continuation from committed V72. V73 binds to V72 validation digest `df8018a5257fb3cd129b2849b5a55f44fb7a3781cd5646bcbb65f29d5fcfbe98` and implementation SHA-256 `0e88efa9e47f86aeaff35e22b28a15642f553c33a37a68fad83f75bdbec5a46a`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V73 keeps cross-role credit at **12**. The executable certificate gate still spans **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit; signed metadata alone still does not prove physical, organizational, hardware, supply-chain, cloud-control, or operator independence.

## Epoch-24 anchor GC: replacement-key rotation and dual rollback-root disagreement

V73 extends the anchor/tombstone model through epoch 24 by adding a fourth-cycle replacement-key rotation phase after bound source reappearance, followed by a dual rollback-root disagreement phase. The replacement key is accepted only after it is bound to the surviving pinned publication lineage. During dual-root disagreement, each root must remain lineage-bound, at least one root is explicitly non-authoritative older recovery evidence, the rotated key must already be bound, and the original shared epoch-12 deadline remains unchanged. Stale/conflicting roots, unbound rotations, and deadline resets fail closed. The modeled nominal state space is **4,749,890,231,992,320,000** states; exactly **27,148,030** admit, including **4,550** fourth-cycle replacement-key-rotation recoveries, **87,360** dual rollback-root disagreement recoveries, and **29,120** cases where both rollback roots are older but remain non-authoritative and lineage-bound.

## Publication/verifier rollback: two witness rotations plus cold-start source selection

V73 composes rollback recovery with two replacement-witness generations and an explicit verifier cold-start source-selection state. A second witness-generation rotation is reachable only after the first witness is already bound and rotated; cold-start recovery may select only a bound primary or secondary witness while the surviving publication quorum and rollback branch remain intact. Cached or evicted delayed-join material never becomes authority, and a cold verifier may consume bound evidence without promoting cache state. The modeled nominal state space is **107,520,000,000,000,000** states; exactly **5,331,920** admit, including **1,354,320** first replacement-witness-rotation recoveries, **190,080** second replacement-witness-rotation recoveries, **1,330,560** bound verifier cold-start selections, and **665,280** secondary-witness cold-start selections. Cached-join authority promotion, unbound source selection, and below-publication-quorum acceptance remain zero.

## Concurrent collision identity reuse plus membership-root compaction

V73 advances tombstone-generation rollover by allowing one concurrent recycled collision identity only in a dedicated phase where the prior rolled tombstone generation survives, the membership basis remains trusted, verifier consumption is current, and the compacted membership root is explicitly bound. Two simultaneous recycled identities, stale or unbound membership roots, active Byzantine identities, and tombstone-generation bypasses fail closed. The modeled nominal state space is **267,181,325,549,568** states; exactly **1,343,100** admit, including **116,325** concurrent collision-identity-reuse recoveries, **707,025** membership-root-compaction recoveries, and **839,025** verifier-restart-or-compaction recoveries.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. These remain synthetic stage-rate model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V74 frontier

V74 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 25 with replacement-key loss/recovery after dual-root disagreement and monotonic root-choice evidence; compose cold-start source selection with witness-set split view and delayed publication-root convergence; and test concurrent recycled identities across two tombstone generations while membership-root compaction is only partially replicated. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

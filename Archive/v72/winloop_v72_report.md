# WinLoop Continuation — V72

**Status:** validated continuation from committed V71. V72 binds to V71 validation digest `c4ad5c9abb931d350b1d8b4c7870a6abb52a2d1e45aec29745faeeec182e279d` and implementation SHA-256 `64fb7cd485b1508e6b7246e4ce4a8777350600bb3cd8e51fc80b2a0b30027ebf`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V72 keeps cross-role credit at **12**. The executable certificate gate still spans **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit. Signed metadata remains insufficient to prove physical, organizational, hardware, supply-chain, cloud-control, or operator independence.

## Epoch-23 anchor GC: fourth source cycle plus rollback-root freshness

V72 extends the anchor/tombstone model through epoch 23 with a fourth pinned publication-source loss/reappearance cycle and explicit rollback-root freshness states. A prior root may be used only as non-authoritative recovery evidence when it remains bound to the surviving pinned lineage; stale, conflicting, unknown, or unbound rollback roots fail closed and cannot reset the shared epoch-12 freshness deadline. The modeled nominal state space is **34,634,616,274,944,000** states; exactly **21,644,896** admit. This includes **58,240** fourth-loss recoveries, **65,520** fourth bound-reappearance recoveries, **139,776** rollback-freshness recovery states, and **23,296** older-root non-authoritative recoveries, with zero freshness-conflict acceptance.

## Publication/verifier rollback: third join-cache eviction and witness churn

V72 composes the third delayed-join generation with an explicit third-generation join-cache eviction/recovery state and replacement-source witness churn. Join-cache recovery is accepted only inside the already-bound rollback/publication recovery branch; cached or evicted join evidence never becomes authority. Replacement witness loss, bound reappearance, and bound rotation likewise require the surviving publication quorum and common rollback-root binding. The modeled nominal state space is **537,600,000,000,000** states; exactly **2,517,900** admit, including **196,020** third-join-cache eviction recoveries, **160,380** bound cache recoveries, **346,500** replacement-witness-loss recoveries, **225,720** bound witness reappearances, and **104,940** bound witness rotations. Stale cache, forked witness, unbound source recovery, and below-publication-quorum acceptance remain rejected.

## Collision rejoin eviction and tombstone-generation rollover

V72 advances post-fifth-eviction membership handling through explicit collision-bound rejoin eviction and tombstone-generation rollover. Rollover requires a surviving prior-generation tombstone marker, a trusted 3-of-5 membership basis, bound root evidence, and a monotonic generation transition; it cannot erase collision history or admit an active Byzantine identity. The modeled nominal state space is **1,903,329,017,856** states; exactly **696,600** admit, including **61,800** collision-rejoin eviction recoveries, **214,800** tombstone-generation rollover recoveries, and **310,800** verifier-restart-or-rollover recoveries. Tombstone-generation bypass, stale-generation replay, active-Byzantine membership, and below-quorum history fail closed.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. These remain synthetic stage-rate model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V73 frontier

V73 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 24 with fourth-cycle replacement-key rotation and dual rollback-root disagreement; compose join-cache recovery with two replacement-witness rotations and verifier cold-start source selection; and test tombstone-generation rollover under concurrent collision identity reuse plus membership-root compaction. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

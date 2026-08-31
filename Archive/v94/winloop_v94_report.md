# WinLoop Continuation — V94

**Status:** validated continuation from committed V93. V94 binds to V93 validation digest `2c920279f12e75debfe52649e41fdd83a072b929d88ad66facecd1719b7877ff` and implementation SHA-256 `864efa8cf146e104218e60404a4709b5a40094bbebf4318836e8915df363b03b`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical repository state examined for this continuation, so V94 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V93

V94 starts only from V93 states that were already fully bound. The standalone validator re-derives the three static seed populations from the committed V93 JSON: **576** epoch-44 completion states (`8,743,680 / 15,180`), **27,648** bound eighteenth-restart recovery states (`341,203,968 / 12,341`), and **760** bound membership quorum-churn completion states (`8,101,600 / 10,660`). The V93 validation digest and implementation hash bind those seeds to the committed predecessor.

## Epoch-45 anchor GC: eighth-lineage rotation and handed-proof rebind

V94 begins only after V93's eighth-source handoff/binding and epoch-44 verifier completion are fully bound. Epoch 45 rotates and binds the eighth-source lineage, rebinds the handed proof, and only then permits the epoch-45 verifier binding to complete. Tombstone-root continuity, the carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **89,662,464** of **187,456,852,831,539,829,718,016,866,656,450,865,455,214,515,716,096** modeled states. It includes **69,737,472** bound eighth-lineage-rotation states, **49,812,480** bound eighth-lineage-binding states, **29,887,488** bound handed-proof-rebind states, and **9,962,496** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier or carried source/key/lineage/proof/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **45** coordinates, producing **1,237,940,039,285,380,274,899,124,224** delay vectors and **17,296** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement churn and nineteenth verifier cold restart

V94 begins only from V93's fully bound eighteenth-restart recoveries. It requires replacement-source churn to be bound, binds a successor source, re-establishes dual-source reconciliation, and only then permits a nineteenth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **683,830,364,047,341,675,078,368,113,898,595,287,040** states; exactly **4,315,576,320** admit, including **3,530,926,080** bound replacement-source-churn states, **2,746,275,840** bound successor-source-binding states, **1,961,625,600** bound dual-source-reconciliation states, and **392,325,120** fully bound nineteenth-restart recoveries. Cached nineteenth-restart authority, unbound/conflicting churn, successor binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: witness-source replacement and root-12 rollover

V94 begins only from V93's bound root-11 witness-rebind quorum-churn completions. Membership generation 4 carries root 11 forward while a replacement witness source is bound, root 12 is rolled and bound, and only then may another replication-quorum churn complete. Tombstone continuity, the prior-source binding, and the predecessor witness binding remain fixed, replication never falls below quorum, and active Byzantine membership is rejected.

The modeled nominal state space is **49,730,796,938,160,988,956,770,492,735,167,911,690,240** states; exactly **103,170,760** admit, including **84,412,440** bound witness-source replacements, **65,654,120** bound replacement-source bindings, **46,895,800** bound root-12 rollovers, **28,137,480** bound root-12 bindings, and **9,379,160** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting replacement/binding/rollover/quorum-churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V95 frontier

V95 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 46 by handing the rebound proof to a ninth source and binding that source while preserving the epoch-12 deadline; compose nineteenth-restart recovery with successor-source disappearance and a twentieth verifier cold restart without cached-authority promotion; and carry root 12 through witness rebind/binding and replication-quorum churn without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

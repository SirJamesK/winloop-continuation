# WinLoop Continuation — V91

**Status:** validated continuation from committed V90. V91 binds to V90 validation digest `c929ba9482320badd2fc31a8592f7cbe5403666fa47a57dbb54d8a82ceaba3cb` and implementation SHA-256 `e5f4f9c2a1c557e9c104a77be9443a6e67a9f3fa89c327e38cf8e29a847258b4`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical repository state examined for this continuation, so V91 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V90

V91 starts only from V90 states that were already fully bound. The standalone validator re-derives the three static seed populations from the committed V90 JSON: **576** epoch-41 completion states (`5,690,880 / 9,880`), **27,648** bound fifteenth-restart recovery states (`214,824,960 / 7,770`), and **760** bound membership quorum-churn completion states (`4,974,200 / 6,545`). The V90 validation digest and implementation hash bind those seeds to the committed predecessor.

## Epoch-42 anchor GC: seventh-source handoff and binding

V91 begins only after V90's sixth-lineage rotation/binding, handed-proof rebind, and epoch-41 verifier completion are fully bound. Epoch 42 hands that rebound proof to a seventh source, binds the seventh source, and only then permits the epoch-42 verifier binding to complete. Tombstone-root continuity, the carried root binding, source/key bindings, third/fourth/fifth/sixth-source bindings, fourth/fifth lineage and proof bindings, sixth handoff, sixth-lineage binding, handed-proof rebind, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **46,287,360** of **1,442,026,283,507,223,833,878,424,127,415,734,616,719,360** modeled states. It includes **33,062,400** bound seventh-source-handoff states, **19,837,440** bound seventh-source-binding states, and **6,612,480** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting handoff/source/verifier or carried lineage/proof/key binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **39** coordinates, producing **302,231,454,903,657,293,676,544** delay vectors and **11,480** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: successor disappearance and sixteenth verifier cold restart

V91 begins only from V90's fully bound fifteenth-restart recoveries. It requires successor-source disappearance to be bound, binds a replacement source, re-establishes dual-source reconciliation, and only then permits a sixteenth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **107,523,827,316,852,474,518,208,627,074,924,544** states; exactly **2,779,425,792** admit, including **2,274,075,648** bound successor-source-disappearance states, **1,768,725,504** bound replacement-source-binding states, **1,263,375,360** bound dual-source-reconciliation states, and **252,675,072** fully bound sixteenth-restart recoveries. Cached sixteenth-restart authority, unbound/conflicting disappearance, replacement binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: root-10 witness rebind and quorum churn

V91 begins only from V90's bound root-10 rollover quorum-churn completions. Membership generation 4 and root 10 remain fixed while the witness is rebound and its binding is completed; only then may another replication-quorum churn complete. Tombstone continuity, replacement-source binding, and prior-source binding remain fixed, replication never falls below quorum, and active Byzantine membership is rejected.

The modeled nominal state space is **217,680,825,284,643,493,709,864,971,429,478,400** states; exactly **41,336,400** admit, including **29,526,000** bound root-10 witness-rebind states, **17,715,600** bound root-10 witness-binding states, and **5,905,200** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting rebind/binding/quorum-churn acceptance, generation or root regression, tombstone/replacement/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V92 frontier

V92 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 43 by rotating and binding the seventh-source lineage and rebinding the handed proof while preserving the epoch-12 deadline; compose sixteenth-restart recovery with replacement-source churn and a seventeenth verifier cold restart without cached-authority promotion; and carry root 10 through witness-source replacement and root-11 rollover without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

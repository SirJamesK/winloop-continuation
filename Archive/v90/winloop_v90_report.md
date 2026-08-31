# WinLoop Continuation — V90

**Status:** validated continuation from committed V89. V90 binds to V89 validation digest `d82f57a7c7d52e38f1cadf55c3e388be974c420b1215dedb2f07e1b7d95caaf8` and implementation SHA-256 `95270f32c07e1c5538cb8aaf6cef9f5a378c20cc71a4bcec05f4a5e415308b94`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical repository state examined for this continuation, so V90 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V89

V90 starts only from V89 states that were already fully bound. The standalone validator re-derives the three static seed populations from the committed V89 JSON: **576** epoch-40 completion states (`4,859,136 / 8,436`), **27,648** bound fourteenth-restart recovery states (`180,956,160 / 6,545`), and **760** bound membership quorum-churn completion states (`4,146,560 / 5,456`). The V89 validation digest and implementation hash bind those seeds to the committed predecessor.

## Epoch-41 anchor GC: sixth-lineage rotation, binding, and handed-proof rebind

V90 begins only after V89's sixth-source handoff/binding and epoch-40 verifier completion are fully bound. Epoch 41 rotates the sixth-source lineage, binds that lineage, rebinds the handed-off proof, and only then permits the epoch-41 verifier binding to complete. Tombstone-root continuity, the carried root binding, source/key bindings, third/fourth-source bindings, fourth-lineage/proof bindings, fifth-source/lineage/proof bindings, the sixth-source binding and handoff binding, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **51,217,920** of **24,931,747,979,689,511,127,362,313,614,089,550,561,280** modeled states. It includes **39,836,160** bound sixth-lineage-rotation states, **28,454,400** bound sixth-lineage-binding states, **17,072,640** bound handed-proof-rebind states, and **5,690,880** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier binding, carried source/key/lineage/proof binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **37** coordinates, producing **18,889,465,931,478,580,854,784** delay vectors and **9,880** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement churn and fifteenth verifier cold restart

V90 begins only from V89's fully bound fourteenth-restart recoveries. It requires replacement-source churn to be bound, binds a successor source, re-establishes dual-source reconciliation, and only then permits a fifteenth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **5,713,563,698,516,958,413,163,919,960,965,120** states; exactly **2,363,074,560** admit, including **1,933,424,640** bound replacement-source-churn states, **1,503,774,720** bound successor-source-binding states, **1,074,124,800** bound dual-source-reconciliation states, and **214,824,960** fully bound fifteenth-restart recoveries. Cached fifteenth-restart authority, unbound/conflicting churn, successor binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: witness-source replacement through root-10 rollover

V90 begins only from V89's bound root-9 witness-rebind quorum-churn completions. Membership generation 4 and carried root 9 remain fixed while a new witness source is bound; only then may root 10 roll over, bind, and complete another replication-quorum churn. Tombstone continuity, the current witness binding, and prior-source binding remain fixed, and replication never falls below quorum.

The modeled nominal state space is **288,139,934,112,298,369,730,496,940,946,227,200** states; exactly **54,716,200** admit, including **44,767,800** bound witness-source-replacement states, **34,819,400** bound replacement-source-binding states, **24,871,000** bound root-10-rollover states, **14,922,600** bound root-10-binding states, and **4,974,200** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting replacement/binding/rollover/root-binding/quorum-churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V91 frontier

V91 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 42 by handing the rebound sixth-source proof to a seventh source and binding it while preserving the epoch-12 deadline; compose fifteenth-restart recovery with successor-source disappearance and a sixteenth verifier cold restart without cached-authority promotion; and carry root 10 through witness rebind and another replication-quorum churn without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

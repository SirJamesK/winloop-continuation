# WinLoop Continuation — V104

**Status:** validated continuation from committed V103. V104 binds to V103 validation digest `856c15cb5a682ec56752deef1d89b86b7cb79779b3d7f58c823239c333170d6e` and implementation SHA-256 `0f70dfaef73840331091e03a6073fba1d53f8ef62ea8f06177353288f8cbe53d`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V104 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V103

V104 starts only from V103 states that were already fully bound. The validator binds the three static seed populations to the committed V103 validation result: **576** epoch-54 completion states (`26,357,760 / 45,760`), **27,648** bound twenty-eighth-restart recovery states (`1,097,929,728 / 39,711`), and **760** bound membership quorum-churn completion states (`27,352,400 / 35,990`). The V103 validation digest and implementation hash identify the exact committed predecessor used for those seeds.

## Epoch-55 anchor GC: thirteenth-lineage rotation, binding, and handed-proof rebind

V104 begins only after V103's thirteenth-source handoff, thirteenth-source binding, and epoch-54 verifier completion are fully bound. Epoch 55 rotates the thirteenth-source lineage, binds that lineage, rebinds the handed proof, and only then permits the epoch-55 verifier binding to complete. Tombstone-root continuity, carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **259,801,344** of **168,101,529,079,057,364,858,744,989,249,823,448,081,469,331,743,155,471,002,883,181,103,963,801,911,296** modeled states. It includes **202,067,712** bound thirteenth-lineage-rotation states, **144,334,080** bound thirteenth-lineage-binding states, **86,600,448** bound handed-proof-rebind states, and **28,866,816** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **65** coordinates, producing **1,361,129,467,683,753,853,853,498,429,727,072,845,824** delay vectors and **50,116** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement-source churn and twenty-ninth verifier cold restart

V104 begins only from V103's fully bound twenty-eighth-restart recoveries. It requires replacement-source churn to be bound, binds a successor source, re-establishes dual-source reconciliation, and only then permits a twenty-ninth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **2,314,453,403,445,838,662,321,737,693,778,690,303,060,989,580,410,880** states; exactly **13,284,311,040** admit, including **10,868,981,760** bound replacement-source-churn states, **8,453,652,480** bound successor-source-binding states, **6,038,323,200** bound dual-source-reconciliation states, and **1,207,664,640** fully bound twenty-ninth-restart recoveries. Cached twenty-ninth-restart authority, unbound/conflicting churn, successor binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: root-17 rollover after witness-source replacement

V104 begins only from V103's bound root-16 witness-rebind quorum-churn completions. Membership generation 4 and carried root 16 remain fixed while the witness source is replaced and bound, root 17 is rolled over and bound, and only then may another replication-quorum churn complete. Tombstone continuity, witness binding, prior-source binding, and replication quorum remain intact, and active Byzantine membership is rejected.

The modeled nominal state space is **266,525,629,270,530,568,264,608,056,409,533,858,649,609,918,700,584,960** states; exactly **331,983,960** admit, including **271,623,240** bound witness-source-replacement states, **211,262,520** bound replacement-source-binding states, **150,901,800** bound root-17-rollover states, **90,541,080** bound root-17-binding states, and **30,180,360** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting replacement/binding/rollover/churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V105 frontier

V105 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 56 by handing the rebound proof to a fourteenth source, binding that source, and preserving the epoch-12 deadline; compose twenty-ninth-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a thirtieth verifier cold restart without cached-authority promotion; and carry root 17 through witness rebind, witness binding, and replication-quorum churn without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

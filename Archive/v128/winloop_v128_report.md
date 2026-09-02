# WinLoop Continuation — V128

**Status:** validated continuation from committed V127. V128 binds to V127 validation digest `e504148379342f9d436b438211d9bd6a2538607bc9730145739227eaa36e3a81` and implementation SHA-256 `640dd44b8701eb172a05f635664f8d7e88f3d2634b8a4e008edc1ac2b90d1837`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V128 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V127

V128 starts only from V127 states that were already fully bound. The validator binds the three static seed populations to the committed V127 validation result: **576** epoch-78 completion states (`138,507,264 / 240,464`), **27,648** bound fifty-second-restart recovery states (`6,132,741,120 / 221,815`), and **760** bound membership quorum-churn completion states (`159,549,840 / 209,934`). The V127 validation digest and implementation hash identify the exact committed predecessor used for those seeds.

## Epoch-79 anchor GC: twenty-fifth-lineage rotation

V128 begins only after V127's twenty-fifth-source handoff, source binding, and epoch-78 verifier completion are fully bound. Epoch 79 rotates that source lineage, binds the lineage, rebinds the handed proof, and only then permits the epoch-79 verifier binding to complete. Tombstone-root continuity, carried root binding, every prior source/key/lineage/proof/handoff binding, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **1,313,936,640** of **89,533,127,927,142,757,924,614,963,600,784,703,828,755,134,489,986,510,881,648,001,859,781,869,307,097,813,096,080,602,484,960,509,476,937,002,200,993,573,573,090,368,542,591,293,964,943,360** modeled states. It includes **1,167,943,680** twenty-fifth-lineage-rotation states, **1,021,950,720** bound rotations, **875,957,760** lineage-binding states, **729,964,800** bound lineage bindings, **583,971,840** handed-proof-rebind states, **437,978,880** bound proof rebinds, **291,985,920** verifier-binding states, and **145,992,960** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **113** coordinates, producing **107,839,786,668,602,559,178,668,060,348,078,522,694,548,577,690,162,289,924,414,440,996,864** delay vectors and **253,460** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement-source churn and fifty-third verifier cold restart

V128 begins only from V127's fully bound fifty-second-restart recoveries. It requires replacement-source churn, successor-source binding, fresh dual-source reconciliation, and only then permits a fifty-third cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **982,909,630,356,869,461,097,764,306,074,250,871,821,358,236,756,994,930,819,934,685,560,936,805,523,521,536** states; exactly **71,207,313,408** admit, including **64,733,921,280** replacement-source-churn states, **58,260,529,152** bound churn states, **51,787,137,024** successor-source-binding states, **45,313,744,896** bound successor bindings, **38,840,352,768** dual-source reconciliations, **32,366,960,640** bound reconciliations, **25,893,568,512** fifty-third-restart states, **19,420,176,384** bound restart states, and **6,473,392,128** fully bound fifty-third-restart recoveries. Cached fifty-third-restart authority, unbound churn/successor/reconciliation/restart/consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: root-29 rollover

V128 begins only from V127's bound root-28 witness-rebind quorum-churn completions. Membership generation 4 is retained while the witness source is replaced and bound, the membership root rolls from 28 to 29, root 29 is bound, and only then may replication-quorum churn complete. Tombstone continuity, witness binding, and prior-source binding remain intact, and active Byzantine membership is rejected.

The modeled nominal state space is **117,950,191,156,552,060,647,219,598,907,909,340,028,246,744,582,601,672,561,151,138,178,274,870,241,420,902,400** states; exactly **1,854,373,400** admit, including **1,685,794,000** witness-source-replacement states, **1,517,214,600** bound replacements, **1,348,635,200** replacement-source-binding states, **1,180,055,800** bound replacement bindings, **1,011,476,400** root-29-rollover states, **842,897,000** bound rollovers, **674,317,600** root-29-binding states, **505,738,200** bound root bindings, **337,158,800** replication-quorum-churn states, and **168,579,400** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting witness-source replacement/replacement binding/root rollover/root binding/churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V129 frontier

V129 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 80 by handing the rebound twenty-fifth-lineage proof to a twenty-sixth source, binding that source, and preserving the epoch-12 deadline; compose fifty-third-restart recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a fifty-fourth verifier cold restart without cached-authority promotion; and keep generation 4 after the root-29 rollover while rebinding the witness to root 29, renewing the witness binding, and requiring replication-quorum churn without tombstone or source-binding discontinuity. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

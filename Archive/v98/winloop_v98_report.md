# WinLoop Continuation — V98

**Status:** validated continuation from committed V97. V98 binds to V97 validation digest `fbdc509251dde7057cd18fffc534f63e2bdb819e32bb5c516a1e5ba7b17fb4b2` and implementation SHA-256 `c82fc5c1cb51eb78e500b3cd9f1d8bc67117f0e8a3d9616133e0e7c016f9c4ac`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V98 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V97

V98 starts only from V97 states that were already fully bound. The validator binds the three static seed populations to the committed V97 validation result: **576** epoch-48 completion states (`14,287,104 / 24,804`), **27,648** bound twenty-second-restart recovery states (`575,769,600 / 20,825`), and **760** bound membership quorum-churn completion states (`14,002,240 / 18,424`). The V97 validation digest and implementation hash identify the exact committed predecessor used for those seeds.

## Epoch-49 anchor GC: tenth-lineage rotation and handed-proof rebind

V98 begins only after V97's tenth-source handoff, tenth-source binding, and epoch-48 verifier completion are fully bound. Epoch 49 rotates the tenth-source lineage, binds that lineage, rebinds the handed proof to the rotated lineage, and only then permits the epoch-49 verifier binding to complete. Tombstone-root continuity, the carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **143,700,480** of **5,161,414,331,725,496,357,173,745,620,501,698,324,244,240,988,731,928,456,724,480** modeled states. It includes **111,767,040** bound tenth-lineage-rotation states, **79,833,600** bound tenth-lineage-binding states, **47,900,160** bound handed-proof-rebind states, and **15,966,720** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **53** coordinates, producing **81,129,638,414,606,681,695,789,005,144,064** delay vectors and **27,720** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement-source churn and twenty-third verifier cold restart

V98 begins only from V97's fully bound twenty-second-restart recoveries. It requires replacement-source churn to be bound, binds the successor source, re-establishes dual-source reconciliation, and only then permits a twenty-third cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **73,985,064,189,515,675,631,019,532,045,246,588,440,805,376** states; exactly **7,124,502,528** admit, including **5,829,138,432** bound replacement-source-churn states, **4,533,774,336** bound successor-source-binding states, **3,238,410,240** bound dual-source-reconciliation states, and **647,682,048** fully bound twenty-third-restart recoveries. Cached twenty-third-restart authority, unbound/conflicting churn, successor binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: witness-source replacement and root-14 rollover

V98 begins only from V97's bound root-13 witness-rebind quorum-churn completions. Membership generation 4 remains fixed while a new witness source is bound, root 13 rolls to root 14, root 14 is bound, and only then may another replication-quorum churn complete. Tombstone continuity, witness binding, prior-source binding, and replication quorum remain intact, and active Byzantine membership is rejected.

The modeled nominal state space is **7,322,102,780,060,736,873,718,617,937,368,671,531,827,200,000** states; exactly **174,097,000** admit, including **142,443,000** bound witness-source-replacement states, **110,789,000** bound replacement-source-binding states, **79,135,000** bound root-14-rollover states, **47,481,000** bound root-14-binding states, and **15,827,000** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting replacement/rollover/binding/churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V99 frontier

V99 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 50 by handing the rebound proof to an eleventh source, binding that source, and preserving the epoch-12 deadline; compose twenty-third-restart recovery with successor-source disappearance and a twenty-fourth verifier cold restart without cached-authority promotion; and carry root 14 through witness rebind, witness binding, and replication-quorum churn without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

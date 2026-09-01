# WinLoop Continuation — V121

**Status:** validated continuation from committed V120. V121 binds to V120 validation digest `7d958d0fc2e8e0c1d18c8a82c8f530aa48b8ed82b07086d91b71ea9d04acd382` and implementation SHA-256 `ed7f9bb69dd6857515ed1569ca17ba9d3c2e5b0699abde5c9d91b30cc628cdb4`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V121 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V120

V121 starts only from V120 states that were already fully bound. The validator binds the three static seed populations to the committed V120 validation result: **576** epoch-71 completion states (`93,139,200 / 161,700`), **27,648** bound forty-fifth-restart recovery states (`4,076,421,120 / 147,440`), and **760** bound membership quorum-churn completion states (`105,195,400 / 138,415`). The V120 validation digest and implementation hash identify the exact committed predecessor used for those seeds.

## Epoch-72 anchor GC: twenty-second-source handoff and binding

V121 begins only after V120's twenty-first-lineage rotation, lineage binding, handed-proof rebind, and epoch-71 verifier completion are fully bound. Epoch 72 hands that rebound proof to a twenty-second source, binds that source, and only then permits the epoch-72 verifier binding to complete. Tombstone-root continuity, carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **692,294,400** of **2,557,292,647,362,112,326,522,861,628,003,580,909,345,568,285,975,310,698,911,180,907,498,398,381,846,774,861,428,375,557,034,293,725,869,016,253,803,687,156,121,600** modeled states. It includes **593,395,200** twenty-second-source-handoff states, **494,496,000** bound handoffs, **395,596,800** twenty-second-source-binding states, **296,697,600** bound source bindings, **197,798,400** verifier-binding states, and **98,899,200** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting handoff/source/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **99** coordinates, producing **401,734,511,064,747,568,885,490,523,085,290,650,630,550,748,445,698,208,825,344** delay vectors and **171,700** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: successor disappearance and forty-sixth verifier cold restart

V121 begins only from V120's fully bound forty-fifth-restart recoveries. It requires successor-source disappearance, binds a replacement source, re-establishes fresh dual-source reconciliation, and only then permits a forty-sixth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **2,452,941,953,934,346,637,192,689,091,537,169,510,359,776,957,544,388,041,342,422,243,558,293,504** states; exactly **47,702,172,672** admit, including **43,365,611,520** successor-source-disappearance states, **39,029,050,368** bound disappearances, **34,692,489,216** replacement-source-binding states, **30,355,928,064** bound replacement bindings, **26,019,366,912** dual-source reconciliations, **21,682,805,760** bound reconciliations, **17,346,244,608** forty-sixth-restart states, **13,009,683,456** bound restart states, and **4,336,561,152** fully bound forty-sixth-restart recoveries. Cached forty-sixth-restart authority, unbound disappearance/replacement/reconciliation/restart/consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: root-25 witness rebind

V121 begins only from V120's bound root-25 rollover quorum-churn completions. Membership generation 4 and root 25 remain fixed while the witness is rebound and bound to root 25, and only then may another replication-quorum churn complete. Tombstone continuity, replacement-source binding, prior-source binding, and replication quorum remain intact, and active Byzantine membership is rejected.

The modeled nominal state space is **11,616,319,629,677,281,070,793,136,062,507,125,714,808,861,100,269,238,920,695,453,626,191,052,800** states; exactly **784,380,800** admit, including **672,326,400** root-25-witness-rebind states, **560,272,000** bound witness rebinds, **448,217,600** root-25-witness-binding states, **336,163,200** bound witness bindings, **224,108,800** replication-quorum-churn states, and **112,054,400** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting witness rebind/binding/churn acceptance, generation or root regression, tombstone/replacement-source/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V122 frontier

V122 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 73 by rotating the twenty-second-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline; compose forty-sixth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a forty-seventh verifier cold restart without cached-authority promotion; and keep generation 4 while replacing and binding the witness source, rolling root 25 to root 26, binding root 26, and requiring replication-quorum churn without tombstone or prior-source discontinuity. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

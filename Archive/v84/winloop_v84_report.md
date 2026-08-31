# WinLoop Continuation — V84

**Status:** validated continuation from committed V83. V84 binds to V83 validation digest `1d9cdbace8c3555694366a4a83ead54364c7629c31838b15fb70ccfd80045940` and implementation SHA-256 `4b49130c86df34373ab445adfd8575947d3c1360fae7b1b0d339f2ff8b08fcea`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical repository state examined for this continuation, so V84 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V83

V84 starts only from V83 states that were already fully bound. The standalone validator recomputes the three static seed populations from the committed V83 JSON: **576** epoch-34 completion states (`2,104,704 / 3,654`), **27,648** bound eighth-restart recovery states (`71,884,800 / 2,600`), and **760** bound quorum-churn completion states (`1,538,240 / 2,024`). The V83 validation digest and implementation hash bind those seeds to the committed predecessor.

## Epoch-35 anchor GC: root-bound compacted-proof revalidation

V84 begins only after V83's third-source failover and epoch-34 verifier binding are complete. Epoch 35 requires the compacted-tombstone proof to be revalidated, then explicitly binds that proof to the carried root, and only then permits the epoch-35 verifier binding to complete. Root state, reissued lineage, tombstone-root continuity, source binding, rotated-key binding, and the bound third-source failover remain fixed to their predecessor values, while the original epoch-12 shared deadline remains immutable. The modeled nominal state space is **198,783,672,519,233,475,196,936,519,680** states; exactly **14,031,360** admit, including **9,354,240** bound proof-revalidation states, **7,015,680** bound proof-root-binding states, and **2,338,560** bound verifier-binding / epoch-completion states. Stale/conflicting root choice, unbound/conflicting proof revalidation, proof-root binding, verifier binding, lineage, source binding, rotated-key binding, third-source binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The exact temporal combinator extends to **27** coordinates, producing **18,014,398,509,481,984** delay vectors and **4,060** deadline vectors under `sum(vector) <= 3`; this expands validation coverage only and does not create authority or relax quorum.

## Publication recovery: successor-source churn and ninth verifier cold restart

V84 begins only from V83's fully bound eighth-restart recoveries. It requires successor-source churn to become bound, binds the replacement successor source, re-establishes dual-source reconciliation, and only then permits a ninth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden. The modeled nominal state space is **2,797,116,697,384,726,730,637,312,000** states; exactly **808,704,000** admit, including **646,963,200** bound successor-source-churn states, **485,222,400** bound successor-replacement states, **323,481,600** bound dual-source-reconciliation states, and **80,870,400** fully bound ninth-restart recoveries. Cached ninth-restart authority, unbound/conflicting churn, replacement binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: rotated-witness rebinding and another quorum-churn cycle

V84 begins only from V83's bound root-7 quorum-churn completions. Membership root 7 and generation 4 remain fixed while the rotated witness is explicitly rebound and then carried through another replication-quorum churn cycle. Replication remains at quorum, and tombstone, witness, and source bindings remain continuous. The modeled nominal state space is **51,012,453,123,210,703,011,840,000** states; exactly **8,740,000** admit, including **5,244,000** bound rotated-witness-rebinding states and **1,748,000** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting witness rebinding or churn, generation regression, root regression, tombstone/witness/source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V85 frontier

V85 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 36 with a fourth-source rollover after the root-bound compacted-proof revalidation while preserving the epoch-12 deadline; compose ninth-restart recovery with replacement-source disappearance and a tenth verifier cold restart without cached-authority promotion; and carry root-7 membership through witness-source replacement and another replication-quorum churn cycle without generation or root regression. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

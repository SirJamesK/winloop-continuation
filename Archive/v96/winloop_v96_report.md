# WinLoop Continuation — V96

**Status:** validated continuation from committed V95. V96 binds to V95 validation digest `5a8ee21699259de7d8f500b4ddaf37f84f0e5767416efd4e5f749c7f1ebcd235` and implementation SHA-256 `92c519f3cb7794eee0cb0f9308a5cf8d6c58754533d7dc867922ded6ebfcfe44`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical repository state examined for this continuation, so V96 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V95

V96 starts only from V95 states that were already fully bound. The standalone validator re-derives the three static seed populations from the committed V95 JSON: **576** epoch-46 completion states (`11,289,600 / 19,600`), **27,648** bound twentieth-restart recovery states (`448,312,320 / 16,215`), and **760** bound membership quorum-churn completion states (`10,784,400 / 14,190`). The V95 validation digest and implementation hash bind those seeds to the committed predecessor.

## Epoch-47 anchor GC: ninth-lineage rotation and handed-proof rebind

V96 begins only after V95's ninth-source handoff, ninth-source binding, and epoch-46 verifier completion are fully bound. Epoch 47 rotates and binds the ninth-source lineage, rebinds the handed proof, and only then permits the epoch-47 verifier binding to complete. Tombstone-root continuity, the carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **114,566,400** of **15,697,404,485,916,295,883,258,497,314,272,509,400,916,509,071,088,025,600** modeled states. It includes **89,107,200** bound ninth-lineage-rotation states, **63,648,000** bound ninth-lineage-binding states, **38,188,800** bound handed-proof-rebind states, and **12,729,600** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **49** coordinates, producing **316,912,650,057,057,350,374,175,801,344** delay vectors and **22,100** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement-source churn and twenty-first verifier cold restart

V96 begins only from V95's fully bound twentieth-restart recoveries. It requires replacement-source churn to be bound, binds a successor source, re-establishes dual-source reconciliation, and only then permits a twenty-first cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **227,294,996,516,230,098,205,836,973,742,053,291,720,704** states; exactly **5,603,254,272** admit, including **4,584,480,768** bound replacement-source-churn states, **3,565,707,264** bound successor-source-binding states, **2,546,933,760** bound dual-source-reconciliation states, and **509,386,752** fully bound twenty-first-restart recoveries. Cached twenty-first-restart authority, unbound/conflicting churn, successor binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: witness-source replacement and root-13 rollover

V96 begins only from V95's bound root-12 witness-rebind quorum-churn completions. Membership generation 4 / root 12 remain the carried state while a new witness source is bound, root 13 is rolled and bound, and only then may another replication-quorum churn complete. Tombstone continuity, witness binding, and the prior-source binding remain fixed, replication never falls below quorum, and active Byzantine membership is rejected.

The modeled nominal state space is **19,399,983,101,092,295,491,396,632,329,155,720,406,630,400** states; exactly **135,557,400** admit, including **110,910,600** bound witness-source replacements, **86,263,800** bound replacement-source bindings, **61,617,000** bound root-13 rollovers, **36,970,200** bound root-13 bindings, and **12,323,400** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting replacement/binding/rollover/root-binding/quorum-churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V97 frontier

V97 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 48 by handing the rebound proof to a tenth source and binding that source while preserving the epoch-12 deadline; compose twenty-first-restart recovery with successor-source disappearance and a twenty-second verifier cold restart without cached-authority promotion; and carry root 13 through witness rebind and witness binding, then replication-quorum churn without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

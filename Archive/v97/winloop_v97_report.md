# WinLoop Continuation — V97

**Status:** validated continuation from committed V96. V97 binds to V96 validation digest `5b5719a56d2c3a6469e499966eafd9e5e3db0df04140084c489fc03a739dac90` and implementation SHA-256 `659e05188ca0fdd1e4146b4539f2bee73c6e67de0c6ac41331903d2fe543e559`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V97 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V96

V97 starts only from V96 states that were already fully bound. The standalone validator re-derives the three static seed populations from the committed V96 JSON: **576** epoch-47 completion states (`12,729,600 / 22,100`), **27,648** bound twenty-first-restart recovery states (`509,386,752 / 18,424`), and **760** bound membership quorum-churn completion states (`12,323,400 / 16,215`). The V96 validation digest and implementation hash bind those seeds to the committed predecessor.

## Epoch-48 anchor GC: tenth-source handoff and binding

V97 begins only after V96's ninth-lineage rotation, ninth-lineage binding, handed-proof rebind, and epoch-47 verifier completion are fully bound. Epoch 48 hands the rebound proof to a tenth source, binds that source, and only then permits the epoch-48 verifier binding to complete. Tombstone-root continuity, the carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **100,009,728** of **3,507,945,149,304,437,924,254,962,449,224,343,183,203,403,213,025,073,692,672** modeled states. It includes **71,435,520** bound tenth-source-handoff states, **42,861,312** bound tenth-source-binding states, and **14,287,104** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting handoff/source/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **51** coordinates, producing **5,070,602,400,912,917,605,986,812,821,504** delay vectors and **24,804** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: successor-source disappearance and twenty-second verifier cold restart

V97 begins only from V96's fully bound twenty-first-restart recoveries. It requires successor-source disappearance to be bound, binds a replacement source, re-establishes dual-source reconciliation, and only then permits a twenty-second cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **4,110,654,192,314,799,648,403,434,631,505,219,105,587,200** states; exactly **6,333,465,600** admit, including **5,181,926,400** bound successor-source-disappearance states, **4,030,387,200** bound replacement-source-binding states, **2,878,848,000** bound dual-source-reconciliation states, and **575,769,600** fully bound twenty-second-restart recoveries. Cached twenty-second-restart authority, unbound/conflicting disappearance, replacement binding, reconciliation, restart, reconciliation consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: root-13 witness rebind and quorum churn

V97 begins only from V96's bound root-13 rollover quorum-churn completions. Membership generation 4 / root 13 remain fixed while the witness is rebound and bound to root 13, and only then may another replication-quorum churn complete. Tombstone continuity and replacement/prior-source bindings remain fixed, replication never falls below quorum, and active Byzantine membership is rejected.

The modeled nominal state space is **14,027,286,858,866,207,859,918,935,207,168,194,149,089,280** states; exactly **98,015,680** admit, including **70,011,200** bound root-13 witness-rebind states, **42,006,720** bound witness-binding states, and **14,002,240** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting witness rebind/binding/quorum-churn acceptance, generation or root regression, tombstone/replacement/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V98 frontier

V98 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 49 by rotating and binding the tenth-source lineage, rebinding the handed proof, and preserving the epoch-12 deadline; compose twenty-second-restart recovery with replacement-source churn and a twenty-third verifier cold restart without cached-authority promotion; and carry root 13 through witness-source replacement and root-14 rollover without generation regression or quorum loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

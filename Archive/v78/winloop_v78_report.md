# WinLoop Continuation — V78

**Status:** validated continuation from committed V77. V78 binds to V77 validation digest `9ae29120c3eb08eebe92725585fb1e912d90271b59c62f155e9544995d914bb1` and implementation SHA-256 `bfbc14223d292bb76e862c9f5bd6bd4a57e7f7cafbc1fcd10aff5d4d7cce7029`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V78 keeps cross-role credit at **12**. The executable certificate gate still spans **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Epoch-29 anchor GC: tombstone-root rollback/revalidation and source-lineage split

V78 carries V77's epoch-28 lineage-loss/rebind continuity forward and adds epoch 29 after a fully bound lineage rebind. A tombstone-root rollback is fail-closed; source-lineage split states are considered only after full tombstone-root revalidation, while the original epoch-12 shared deadline remains immutable. The modeled nominal state space is **255,720,580,668,759,003,572,958,147,442,114,560** states; exactly **127,176,016** admit, including **2,914,560** rollback states, **2,331,648** bound revalidation states, and **1,165,824** bound lineage-split states. Stale/conflicting root choice, unbound source replacement/re-rotation/key recovery/lineage rebind, tombstone-root discontinuity, unbound/conflicting rollback or revalidation, unbound/conflicting lineage split, deadline reset, and aggregate bad acceptance are all zero.

The exact temporal-vector combinator extends to 21 coordinates, producing **4,398,046,511,104** delay vectors and **2,024** deadline vectors under `sum(vector) <= 3`; this expands validation coverage only and does not create authority or relax quorum.

## Publication recovery: bounded source reappearance under a third verifier restart

V78 starts only after V77 cache-generation recovery is fully lineage-bound, then models a third verifier restart followed by bounded source reappearance and explicit binding. The modeled nominal state space is **3,143,919,665,310,920,500,838,400,000,000,000** states; exactly **119,567,000** admit, including **55,157,760** third-restart states, **36,771,840** bounded source-reappearance states, and **36,771,840** bound third-restart recoveries. Cached third-restart authority, unbound/forked source reappearance, unbound/conflicting restart binding, unbound/forked cache-generation recovery, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: third-generation witness eviction and temporary replication loss

V78 carries the third recycled-identity generation through witness eviction and temporary replication loss. Eviction is admitted only after generation 4 and membership root 4 are fully bound; temporary replication loss is fail-closed and recovery cannot regress generation, reuse, or root indices. The modeled nominal state space is **221,176,354,159,617,638,400,000,000,000** states; exactly **13,682,280** admit, including **736,440** third-generation witness-eviction states, **1,104,660** temporary-replication-loss states, and **736,440** bound replication recoveries. Below-replication-quorum acceptance, unbound/conflicting rollback/compaction/eviction/loss, unbound/forked witness churn/identity reuse/recovery, generation collapse, unbound membership root, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V79 frontier

V79 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 30 with lineage-split resolution plus replacement-key retirement/reissuance while preserving the epoch-12 deadline and tombstone-root continuity; compose third-restart bounded source reappearance with dual-source reconciliation and a fourth verifier cold restart without cached-authority promotion; and carry third-generation witness eviction through replication recovery into membership-root rollover and witness reinstatement without generation regression. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

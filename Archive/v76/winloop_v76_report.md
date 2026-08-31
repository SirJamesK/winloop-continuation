# WinLoop Continuation — V76

**Status:** validated continuation from committed V75. V76 binds to V75 validation digest `c7ad77c116f37569cd415b6c92c24f9332df44d8c05af0909a79275ffff329e2` and implementation SHA-256 `c225ba7efd03051cafbd91cecfe2dfed87a2e48d7d61c5730ede3f68d33ac055`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V76 keeps cross-role credit at **12**. The executable certificate gate still spans **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Epoch-27 anchor GC: re-rotated-key recovery and source-lineage rollover

V76 carries V75's epoch-26 state machine forward and adds an epoch-27 phase for re-rotated-key loss, independently bound recovery, and replacement-source lineage rollover while preserving rollback-resistant root choice. The original epoch-12 shared deadline remains immutable. The modeled nominal state space is **70,973,847,823,597,499,842,560,000** states; exactly **49,627,488** admit, including **470,016** re-rotated-key-loss states, **470,016** bound recovery states, and **470,016** lineage-rollover states. Stale/conflicting root choice, unbound source replacement, unbound re-rotation, unbound key recovery, unbound/conflicting lineage rollover, deadline reset, and aggregate bad acceptance are all zero.

The delay/deadline-vector combinator now evaluates the same `sum(vector) <= 3` state count by the closed-form stars-and-bars identity `C(n+3,3)` rather than enumerating all `4^n` vectors. This changes validation cost only; it does not change authority, admission, quorum, or message semantics.

## Publication recovery: second restart and split-witness rollback

V76 composes V75's bounded source reappearance with a second verifier restart and split-witness rollback after reappearance. Recovery remains admissible only on the already-bound publication lineage and only through lineage-bound witness recovery. The modeled nominal state space is **2,818,572,288,000,000,000,000,000** states; exactly **16,137,940** admit, including **3,144,960** second-verifier-restart states, **2,358,720** split-witness rollback states, and **1,572,480** bounded split-witness recoveries. Cached second-restart authority, unbound/conflicting witness rollback, unbound/forked witness recovery, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: second witness-set churn generation

V76 carries V75's two-generation recycled-identity rollback recovery forward through a second witness-set churn generation. Admission at the new phase requires the first rollback recovery to be fully bound, current tombstone generation, the same bound membership-root lineage, and quorum-sufficient replication. The modeled nominal state space is **65,384,736,620,544,000,000** states; exactly **3,894,800** admit, including **276,640** second-churn states and **276,640** bound second-churn recoveries. Below-replication-quorum acceptance, unbound/conflicting rollback, unbound/forked first or second witness churn, tombstone-generation collapse, unbound membership root, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V77 frontier

V77 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 28 with replacement-source lineage loss/rebind and tombstone-root continuity without deadline reset; compose second-restart split-witness recovery with renewed source disappearance and verifier cache-generation rollback; and test second witness-churn recovery through membership-root compaction and a third recycled-identity generation. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

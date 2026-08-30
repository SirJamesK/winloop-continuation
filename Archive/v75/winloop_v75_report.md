# WinLoop Continuation — V75

**Status:** validated continuation from committed V74. V75 binds to V74 validation digest `b56ea2b452bf5d2ed56737d8b59a3bed6c4b2cd42e45a6f64c4bef3d55ae30cd` and implementation SHA-256 `32466596df72658d1f3c95369df372e586080205673c60e954f92a7e96b08d90`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V75 keeps cross-role credit at **12**. The executable certificate gate still spans **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit; signed metadata alone still does not establish physical, organizational, hardware, supply-chain, cloud-control, or operator independence.

## Epoch-26 anchor GC: recovered-key re-rotation after bound source replacement

V75 carries the V74 epoch-25 state machine forward and adds an epoch-26 phase requiring independently bound source replacement after recovered-key availability, a bound re-rotation step, and rollback-resistant monotonic-root evidence before admission. The original epoch-12 shared deadline remains immutable. The modeled nominal state space is **262,649,930,268,247,326,720,000** states; exactly **40,964,560** admit, including **195,840** bound source-replacement states, **195,840** recovered-key re-rotation states, and **195,840** rollback-resistant root-choice states. Stale/conflicting root-choice acceptance, unbound source replacement, unbound re-rotation, deadline reset, and aggregate bad acceptance are all zero.

## Publication recovery: verifier restart, source disappearance, bounded reappearance

V75 composes V74 split-witness publication-root convergence with verifier restart and complete selected-source disappearance. Recovery remains admissible only after the split witness set has already converged on the bound publication lineage, the verifier restart is explicit, source loss is represented rather than silently cached, and source reappearance is independently lineage-bound. The modeled nominal state space is **8,808,038,400,000,000,000,000** states; exactly **10,394,384** admit, including **943,488** verifier-restart states, **943,488** source-disappearance states, and **628,992** bounded source-reappearance recoveries. Cached-restart authority, conflicting source-loss, unbound/forked reappearance, below-publication-quorum, and aggregate bad acceptance are all zero.

## Membership-root rollback with witness churn

V75 carries V74's two-generation recycled-identity basis forward into quorum-sufficient partial membership-root replication rollback. A rollback recovery is admissible only with verifier-current tombstone generation, a bound membership-root lineage, quorum-sufficient partial replication, and bound membership-witness churn/recovery; below-quorum replication, unbound/conflicting rollback, unbound/forked witness churn, tombstone-generation collapse, unbound membership roots, and active Byzantine membership fail closed. The modeled nominal state space is **2,972,033,482,752,000,000** states; exactly **2,842,840** admit, including **217,360** partial-replication rollback/witness-churn recoveries. Every modeled unsafe acceptance counter remains zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. These remain synthetic stage-rate model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V76 frontier

V76 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 27 with re-rotated-key loss/recovery and replacement-source lineage rollover without deadline reset; compose bounded source reappearance with a second verifier restart and split witness-set rollback after reappearance; and test two-generation recycled identities through membership-root rollback recovery followed by a second witness-set churn generation. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

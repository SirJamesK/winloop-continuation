# WinLoop Continuation — V74

**Status:** validated continuation from committed V73. V74 binds to V73 validation digest `44d2f25f59474776030e3dfdcf1b44c7a348f2f6f668a4297560c038064a0b09` and implementation SHA-256 `a4f731a59b4f58c3018d13157b14bb7c043c799804b1303e3b2eb6fa644912bc`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V74 keeps cross-role credit at **12**. The executable certificate gate still spans **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit; signed metadata alone still does not establish physical, organizational, hardware, supply-chain, cloud-control, or operator independence.

## Epoch-25 anchor GC: replacement-key loss/recovery with monotonic root choice

V74 carries the V73 epoch-24 state machine forward and adds an epoch-25 phase after dual rollback-root disagreement. The new phase distinguishes replacement-key loss/quarantine from independently bound key recovery, and requires monotonic root-choice evidence anchored to the surviving publication lineage before either state is admitted. The shared deadline remains the original epoch-12 deadline; stale/conflicting root-choice evidence, unbound key recovery, and deadline reset all fail closed. The modeled nominal state space is **968,977,607,326,433,280,000** states; exactly **33,574,240** admit, including **80,640** epoch-25 key-loss/quarantine states, **80,640** bound key-recovery states, and **161,280** monotonic-root-choice evidence states. Stale/conflicting root-choice acceptance, unbound recovery acceptance, deadline-reset acceptance, and aggregate bad acceptance are all zero.

## Publication/verifier rollback: split witness sets and delayed root convergence

V74 composes V73 cold-start source selection with an explicit witness-set split view and delayed publication-root convergence. Split-view recovery is allowed only after both replacement-witness generations are bound, the cold verifier selects a bound source, the rollback branch remains verifier-bound, and the publication quorum remains intact. A delayed root may remain recoverable only while it is lineage-bound; the converged state is separately represented. Unbound/conflicting witness sets, forked or unbound convergence, cached-join authority promotion, and below-publication-quorum states fail closed. The modeled nominal state space is **6,881,280,000,000,000,000** states; exactly **7,425,704** admit, including **494,208** split-view recoveries, **247,104** delayed publication-root convergence recoveries, and **247,104** bound converged-root recoveries. All modeled unsafe acceptance counters remain zero.

## Two tombstone generations with partially replicated membership-root compaction

V74 extends recycled-identity recovery to two distinct recycled identities carried from successive tombstone generations. The new state requires a five-member basis containing both recycled-generation markers, at least a three-member current quorum including a surviving trusted member, verifier-current tombstone generation 3, a bound membership root, and replication state that is either quorum-sufficient partial replication or full replication. Below-quorum partial replication, generation collapse, unbound roots, duplicate same-generation recycling, and active Byzantine membership fail closed. The modeled nominal state space is **33,435,376,680,960,000** states; exactly **2,019,600** admit, including **334,400** two-generation recycled-identity recoveries, split evenly between **167,200** quorum-sufficient partial-replication and **167,200** full-replication recoveries. Below-replication-quorum, tombstone-generation-collapse, unbound-root, active-Byzantine, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. These remain synthetic stage-rate model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V75 frontier

V75 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 26 with recovered-key re-rotation after source replacement and explicit rollback resistance for monotonic root choice; compose witness-set split-view convergence with verifier restart, source disappearance, and bounded source reappearance; and test two-generation recycled identities under partial membership-root replication rollback plus membership-witness churn. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

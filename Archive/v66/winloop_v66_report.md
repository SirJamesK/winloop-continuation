# WinLoop Continuation — V66

**Status:** validated continuation from committed V65. V66 binds to V65 validation digest `90c0b1862ec4d81b1e60e20334fa4f02bf6bbb410ae0db520017ffeb4db805d6` and implementation SHA-256 `c743e1c5fc027b4695623bbe6ed95dd3cfd847a6ff72a0f1250647735785cf01`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V66 keeps cross-role credit at **12**. The executable gate evaluates **150** certificate/anchor/relation combinations and admits only **4** hypothetical states requiring current or canonically cached external evidence, a current/cached independent anchor, and an explicitly disjoint external relation. There are zero stale/conflicting, alias/unknown-relation, or self-asserted acceptances. Modeled role labels and signed metadata are not treated as proof of physical, organizational, hardware, supply-chain, cloud-control, or operator independence.

## Epoch-17 anchor GC with source replacement and verifier lag

V66 extends the compaction model through epoch 17. `T16 -> CP17` preserves the original epoch-12 freshness origin. Source replacement, clear-source replacement, and verifier lag may recover only from canonical/cached evidence; they cannot mint a new freshness origin or erase uncleared revocation state.

The exact matrix contains **1,605,632,000** history/compaction/source/revocation/verifier/publication/delay states, of which **91,392** admit. The accepted set includes **6,048** source-replacement recoveries, **4,704** lagged-verifier recoveries, and **672** epoch-17 clear recoveries specifically after clear-source replacement. The shared end-to-end freshness budget remains **3 steps** from epoch 12 across five modeled propagation legs. There are **zero** post-deadline acceptances, **zero** deadline-reset acceptances, **zero** stale/fork-clear acceptances, and **zero** fork acceptances.

## Split-view eviction recovery with proof-source loss and one rollback population

V66 composes V65's split-view eviction publication with proof-source disappearance and one verifier-population rollback. Acceptance still requires a 2-of-3 post-transition publication quorum, canonical/cached eviction evidence, a validated/cached join, and a canonical/cached bridge. If proof sources disappear, only the explicitly cached source-loss evidence form is accepted. A rollback population contributes no post-transition quorum credit and is tolerated only when a canonical/cached rollback bridge binds it to the same post-membership root.

The exact matrix contains **35,123,200** publication/source/rollback/delay states, of which **31,360** admit. It includes **8,960** proof-source-disappearance recoveries and **13,440** one-rollback-view recoveries. There are **zero** fork acceptances, **zero** stale/missing eviction-proof acceptances, **zero** untrusted/conflicting-join acceptances, and **zero** post-deadline acceptances.

## Second Byzantine eviction during the two-generation join sequence

V66 inserts a second Byzantine eviction between join-1 and join-2 in the carried 3-of-5 membership model. Active Byzantine and evicted populations never count toward quorum. Join-2 can count only after old/cached members plus join-1 independently form the carried 3-of-5 quorum and the second-eviction evidence is canonical/cached. Replacement populations therefore cannot create the quorum that authorizes their own transition.

The exact matrix contains **1,889,568,000** membership/history/eviction-chain/delay states, of which **361,680** admit. It includes **71,600** second-eviction recoveries and **30,400** post-second-eviction join-2 recoveries. There are **zero** replacement-self-authorization acceptances, **zero** active-second-Byzantine acceptances, **zero** untrusted-join acceptances, **zero** membership/eviction-fork acceptances, **zero** missing/stale second-eviction-proof acceptances, **zero** stale/missing-chain acceptances, **zero** below-threshold-history acceptances, and **zero** post-deadline acceptances.

## Preserved bounds and evidence ceiling

The V65-validated temporal regression is carried unchanged: horizon 22 floor **1 / synthetic budget 851**, horizon 11 floor **2 / budget 398**. These are synthetic model parameters, not empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged. Unknown, stale, conflicting, cyclic, aliased, self-asserted, or unbound provenance fails closed.

## V67 frontier

V67 should continue to require committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 18 across dual source replacement and verifier restart; compose rollback recovery with two proof-source losses without promoting cached evidence into a new authority root; and test consecutive second-Byzantine eviction plus join rollback under one honest verifier-population loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed acceptance bar with honest message accounting.

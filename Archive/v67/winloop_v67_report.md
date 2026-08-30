# WinLoop Continuation — V67

**Status:** validated continuation from committed V66. V67 binds to V66 validation digest `df35c786955dd2f202c493be6a67a6eee32be8f37ede43a204b8be72a16c0c62` and implementation SHA-256 `dfd71b33ba7fbef697d3c2a256b5ce7b314110fd323e21f200d8d8cca92fa835`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate exists in the canonical repository state examined for this continuation, so V67 keeps cross-role credit at **12**. The executable gate evaluates **150** certificate/anchor/relation combinations and admits only **4** hypothetical states requiring current or canonically cached external evidence, a current/cached independent anchor, and an explicitly disjoint external relation. There are zero stale/conflicting, alias/unknown-relation, or self-asserted acceptances. Signed metadata and modeled role labels remain insufficient to prove physical, organizational, hardware, supply-chain, cloud-control, or operator independence.

## Epoch-18 anchor GC across dual source replacement and verifier restart

V67 extends the compaction model through epoch 18. `T17 -> CP18` preserves the original epoch-12 freshness origin while explicitly allowing two old proof sources to disappear, their replacements to come online, and a verifier to restart from a bounded bridge. Neither source replacement nor restart may mint a new freshness origin, erase uncleared revocation state, or promote delayed/cached evidence into a new authority root.

The exact matrix contains **8,808,038,400** history/compaction/source/revocation/verifier/publication/delay states, of which **206,808** admit. The accepted set contains **9,072** dual-source-replacement recoveries, **16,296** verifier-restart recoveries, **5,880** recoveries after both old sources are lost with canonical cached continuity, and **1,008** epoch-18 clear recoveries after clear-source replacement. The shared end-to-end freshness budget remains **3 steps** from epoch 12 across six modeled propagation legs. There are **zero** post-deadline acceptances, **zero** deadline-reset acceptances, **zero** stale/fork-clear acceptances, **zero** restart-as-new-authority acceptances, and **zero** fork acceptances.

## Two proof-source losses with rollback recovery and no cached-authority promotion

V67 composes split-view rollback recovery with loss of both eviction-proof sources. Acceptance still requires a 2-of-3 post-transition publication quorum, validated/cached join evidence, canonical/cached bridge state, and an authority root that is either live or explicitly pinned before source loss. If both proof sources disappear, recovery is permitted only from the pre-loss dual-attested cached proof form bound to that pinned authority root. A cache may preserve evidence but cannot become the authority that validates itself.

The exact matrix contains **63,221,760** publication/evidence/source/join/bridge/authority/delay states, of which **88,000** admit. It includes **3,520** two-proof-source-loss recoveries, **24,000** one-rollback-view recoveries, and **21,120** replacement-source recoveries. There are **zero** cached-authority-promotion acceptances, **zero** fork acceptances, **zero** stale/missing eviction-proof acceptances, **zero** untrusted/conflicting-join acceptances, and **zero** post-deadline acceptances.

## Consecutive Byzantine evictions plus join rollback under one honest verifier loss

V67 extends the carried 3-of-5 membership model through two consecutive Byzantine evictions and a subsequent join-2 rollback. Evicted or active Byzantine populations never count toward the trusted 3-of-5 threshold. A rollback is accepted only when an explicit rollback bridge binds the same membership chain and at most one honest verifier population is lost; the loss does not reduce the quorum threshold. Replacement populations therefore cannot authorize their own transition, and rollback recovery cannot resurrect an evicted Byzantine population.

The exact matrix contains **900,000,000** population/phase/history/evidence/verifier/join/delay states, of which **187,800** admit. It includes **28,800** second-eviction recoveries, **9,600** join-rollback recoveries, and **128,400** recoveries while one honest verifier population is unavailable. There are **zero** replacement-self-authorization acceptances, **zero** active-Byzantine acceptances after eviction, **zero** two-honest-verifier-loss acceptances, **zero** untrusted/conflicting-join acceptances, **zero** membership/eviction-fork acceptances, **zero** below-threshold-history acceptances, and **zero** post-deadline acceptances.

## Preserved bounds and evidence ceiling

The V66-carried temporal regression remains unchanged: horizon 22 floor **1 / synthetic budget 851**, horizon 11 floor **2 / budget 398**. These remain synthetic stage-rate model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint-recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged. Unknown, stale, conflicting, cyclic, aliased, self-asserted, unbound, or cache-promoted provenance fails closed.

## V68 frontier

V68 should continue to require committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 19 across complete dual-source disappearance and cold verifier restart; compose two proof-source losses with simultaneous publication-root rollback without cached-authority promotion; and test a third Byzantine eviction after rollback recovery with one honest verifier loss. V21 routing remains active unless a replacement independently clears the >=2,000-seed acceptance bar with honest message accounting.

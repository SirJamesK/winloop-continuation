# WinLoop Continuation — V65

**Status:** validated continuation from committed V64. V65 binds to V64 validation digest `e3e090ea32f151975631636e7fc62e3c5784fa29d62cfeb4a9c73a0b983bd810` and implementation SHA-256 `08e3e20a809d7df1600f9117238a8da1747333daaffed9d4c3f7838b5c256540`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence certificate remains fail closed

V64 made provider/operator/hardware independence an executable evidence gate and explicitly refused to convert modeled role separation into real cross-role credit. No new committed independently validated external independence certificate exists between the V64 parent and this continuation, so V65 keeps cross-role credit at **12**.

The V65 certificate state machine tests **150** certificate/anchor/relation combinations. Only **4** hypothetical combinations satisfy the model gate, all requiring a current or canonical-cached external certificate, a current or canonical-cached independent anchor, and an explicitly externally established disjoint relation. There are **zero** stale/conflicting, alias/unknown-relation, or self-asserted acceptances. These hypothetical admits are not evidence that the real deployment is independent.

## Epoch-16 tombstone garbage collection with revocation-clear overlap and proof-source churn

V65 extends the anchor chain through epoch 16. `T15` binds the prior super-tombstone chain, `CP15`, all modeled live revocation obligations through epoch 15, and the original epoch-12 freshness origin. `CP16` binds `T15`. Storage may compact older proof objects only behind a canonical/cached `T15 -> CP16` chain; proof-source replacement and delayed publication cannot mint a new freshness origin.

The exact matrix contains **47,185,920** history/source/revocation/publication/delay states, of which **22,050** admit. It includes **4,200** compact-behind-`T15` recoveries, **525** recoveries after modeled pre-16 source disappearance, **525** proof-source-churn recoveries, **4,410** overlapping-revocation recoveries, and **4,410** canonical epoch-16 clear recoveries.

The shared end-to-end freshness budget remains **3 steps** from epoch 12 across four modeled propagation legs. There are **zero** post-deadline acceptances, **zero** deadline-reset acceptances, **zero** stale/fork-clear acceptances, **zero** invalid-history acceptances, and **zero** forked source/compaction/publication acceptances.

## Split-view eviction-proof publication before and after a validated join

V64 required a canonical/cached Byzantine eviction proof before a validated join could replace the evicted population. V65 adds three verifier-publication populations that can temporarily disagree between cached pre-transition and post-transition roots. Acceptance requires a 2-of-3 post-transition publication quorum, a canonical/cached eviction proof, a validated/cached-validated join certificate, and a canonical/cached gossip bridge. Forked eviction or membership views contribute no credit.

The exact matrix contains **884,736** publication states, of which **5,120** admit. It includes **1,920** recoveries with one cached pre-transition view and **1,920** recoveries with one missing verifier view.

There are **zero** fork acceptances, **zero** stale/missing eviction-proof acceptances, **zero** untrusted/conflicting-join acceptances, **zero** pre-eviction/pre-join acceptances, and **zero** post-deadline acceptances.

## Two consecutive joining populations without transient quorum inflation

V65 then composes two join generations in a 3-of-5 membership. The second join may count only after the carried membership—canonical/cached old members plus the first validated join—already independently satisfies quorum. A pair of transient joiners therefore cannot create the quorum that authorizes their own transition.

The exact matrix contains **26,891,200** membership/history/chain/delay states, of which **196,140** admit. It includes **25,500** fully authorized two-generation join recoveries and **7,600** recoveries with one quarantine.

There are **zero** transient-membership quorum-inflation acceptances, **zero** untrusted-join quorum-credit acceptances, **zero** active-Byzantine acceptances, **zero** stale/missing-chain acceptances, **zero** membership-fork acceptances, **zero** below-threshold-history acceptances, and **zero** post-deadline acceptances.

## Preserved bounds and evidence ceiling

The horizon-22 lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These are synthetic model parameters, not empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

Unknown, stale, conflicting, cyclic, aliased, self-asserted, or unbound provenance fails closed. Signed metadata does not prove physical, organizational, hardware, supply-chain, or cloud-control independence.

## V66 frontier

V66 should still require a committed independently validated provider/operator/hardware independence certificate before any cross-role-credit increase. It should extend anchor garbage collection through epoch 17 while retaining canonical revocation-clear evidence across source replacement and verifier lag. It should compose split-view eviction publication with proof-source disappearance and one verifier-population rollback, then test a second Byzantine eviction during the two-generation join sequence without allowing replacement populations to self-authorize. V21 routing remains active unless a replacement independently clears the >=2,000-seed acceptance bar with honest message accounting.

# WinLoop Continuation — V64

**Status:** validated continuation from committed V63. V64 binds to V63 validation digest `6bebeb48bcda3d1dd9f093727e416f92b692e898d54236f9dde95dbe2f3269a9` and implementation SHA-256 `48feb8ecaa02a39725333c300ef848eff045fb25cf567f057665652359e49813`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Externally-bound provider/operator/hardware identity gate

V63 ended with disjoint modeled long-horizon witness identities but explicitly did not treat those role labels as proof of independent providers, operators, hardware, custody, or organizational control. V64 makes that evidence ceiling executable instead of narrative-only. The gate independently tracks provider, operator, and hardware binding evidence for both sides of the witness handoff, an external bridge record, the old/new independence relation, and binding-source loss/fork modes.

The exact matrix contains **5,832,000** evidence states. Only **145** hypothetical states satisfy the complete gate. A passing state requires every provider/operator/hardware binding on both sides to be current or cached external evidence, a current/cached external bridge, and an explicitly externally established disjoint relation. Source-loss recovery is permitted only from canonical cached evidence: **8** old-side loss states, **8** new-side loss states, and **1** both-sides loss state recover.

There are **zero** stale/conflicting acceptances, **zero** alias-or-unknown-relation acceptances, **zero** self-asserted acceptances, and **zero** binding-source-fork acceptances. Most importantly, the repository still contains no committed independently validated external provider/operator/hardware independence certificate. Therefore V64 does **not** raise cross-role credit; the conservative credit remains **12**. The 145 passing states are model-level gate states, not a claim that such evidence exists in the real deployment.

## Epoch-15 tombstone compaction with concurrent revocation and source disappearance

V64 extends the anchor history through epoch 15. A new epoch-14 super-tombstone `T14` binds the prior `T12`/`T13` tombstones, `CP14`, all modeled still-live revocation obligations, and the original deadline origin. `CP15` then binds `T14`. This allows individual pre-15 proof objects to disappear only when the canonical/cached `T14 -> CP15` proof remains available. Compaction therefore removes storage objects without minting a new authority origin or freshness budget.

The exact state space contains **14,155,776** history/source/revocation/delay cases, of which **29,100** admit. The shared freshness budget remains one **3-step** end-to-end deadline rooted at epoch 12. V64 admits **1,000** compact-behind-`T14` recoveries, **100** pre-15-source-disappearance recoveries, **5,820** concurrent-revocation recoveries overall, and **20** cases where concurrent revocation remains recoverable after all modeled pre-15 sources disappear behind cached `T14` and `CP15`.

There are **zero** post-deadline acceptances, **zero** deadline-reset acceptances, **zero** stale/fork-clear acceptances, **zero** invalid-history acceptances, and **zero** forked-source/compaction acceptances. Missing deadline origin fails closed.

## 3-of-5 recovery after one Byzantine fork, two quarantines, and a validated join

V63 validated two-quarantine recovery but did not separately require proof that a Byzantine population had been evicted before a joiner could replace it. V64 adds an explicit Byzantine-eviction proof state. The post-reconfiguration five-slot set can contain two quarantined populations and one validated joiner only after a canonical or cached eviction proof removes the Byzantine population from the active membership. Active Byzantine/fork state contributes no quorum credit.

The exact matrix contains **9,953,280** membership/eviction-proof/history/delay cases, of which **237,320** admit. It includes **9,000** one-Byzantine/two-quarantine/validated-join recoveries under a 3-of-5 threshold and a shared 3-step publication/gossip deadline. **116,400** accepted states contain an untrusted joiner only because three other trusted/current populations independently satisfy quorum; the untrusted joiner contributes no credit.

There are **zero** active-Byzantine acceptances, **zero** stale/missing-eviction-proof acceptances in Byzantine-evicting recovery, **zero** membership-fork acceptances, **zero** below-threshold-history acceptances, **zero** untrusted-join quorum-credit acceptances, and **zero** post-deadline acceptances.

## Preserved results and evidence ceiling

The exact horizon-22 lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These remain synthetic model parameters rather than empirical attacker prices, response times, or real-world compromise costs. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

V64 does not claim that signed metadata proves physical, organizational, hardware, supply-chain, or cloud-control independence. Unknown, stale, conflicting, cyclic, aliased, self-asserted, or unbound provenance fails closed.

## V65 frontier

V65 should require an actually committed, independently validated provider/operator/hardware independence certificate before any cross-role-credit increase. It should extend tombstone garbage-collection proof through anchor epoch 16 with overlapping revocation clear, delayed publication, and proof-source churn. It should split-view test Byzantine eviction-proof publication across verifier populations before and after a validated join, and test two consecutive joining populations without allowing transient membership to inflate the 3-of-5 quorum. Cross-role credit remains 12 absent committed external evidence, and V21 routing remains active unless a replacement independently clears the >=2,000-seed acceptance bar with honest message accounting.

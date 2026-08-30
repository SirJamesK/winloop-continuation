# WinLoop Continuation — V62

**Status:** validated continuation from committed V61. V62 binds to V61 validation digest `360d9f05a3bc7dfaf8805229ba5b57b657f046715abf56195b8b58af43ebd9ec` and implementation SHA-256 `278cde2efdf0ef256cb9ecffc0efae545318b0b0d1f0c6e1cdd4694ae6520c52`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Long-horizon rotation of the locally pinned root-history anchor

V61 rotated the online root-history authority set while retaining the epoch-10 root-history checkpoint as a verifier-local trust anchor. V62 rotates that pinned anchor through a distinct long-horizon witness role. The transition hash binds the old pinned checkpoint, the V61 epoch-11 checkpoint, the new epoch-12 anchor, and the 10→12 transition. The witness handoff uses old and new 2-of-3 witness quorums and additionally requires the leaving witness `horizonWitnessA` and joining witness `horizonWitnessD`, so the overlapping B/C witnesses cannot authorize the change by themselves.

The exhaustive matrix contains **468,750** cases across five transition-record states, five states for each of three old and three new long-horizon witnesses, and six source/retention modes. Exactly **45** admit. This includes **18** recoveries after all pre-rotation online root sources disappear while the old pinned checkpoint and canonical transition remain retained, plus **9** recoveries after the transition publisher disappears and only a cached canonical transition remains. There are **zero** stale acceptances, **zero** fork acceptances, **zero** new-anchor-only acceptances, and **zero** self-authorized new-anchor acceptances. Removing the old pin fails closed.

The long-horizon witness role is modeled as separate from the root-history authorities, but V62 does not treat role separation or signed metadata as proof of physical, organizational, hardware, provider, or operator independence. Conservative cross-role provenance credit therefore remains 12.

## Multi-layer compaction beyond epoch 11 without deadline reset

V62 extends the hash chain through roster/issuer epoch 12 and adds two explicit compaction layers. `CP11` binds the prior `CP10`, V61 root rotation, epoch-11 roster and issuer state, and the long-horizon anchor transition. `CP12` then binds `CP11`, epoch-12 roster and issuer state, and the same anchor transition. The accepted chain therefore cannot substitute a compacted checkpoint that is detached from the anchor transition or its predecessor.

The exact matrix contains **2,343,750** cases across five states for each of `CP10`, `CP11`, `R12`, `E12`, and `CP12`; three independent delay segments 0..4; and six retention modes. Exactly **1,600** admit. Of those, **160** use CP10→CP11 compaction recovery, **160** use CP11→CP12 compaction recovery, **640** recover from an explicit 3-of-4 threshold-fragment retention mode, and **1,520** involve nonzero publication/recovery delay.

The revocation window remains one shared **3-step** end-to-end deadline. V62 sums CP11 publication delay, CP12 publication delay, and verifier recovery delay; no checkpoint grants a new budget. Consequently there are **zero** post-deadline admissions and **zero** deadline-reset admissions, including cases where every individual delay segment is at most three but the combined path exceeds three. Stale intermediate state, forked fragments, and below-threshold fragments fail closed.

## Asynchronous verifier churn, Byzantine quarantine, and delayed compaction publication

V62 expands checkpoint recovery to four verifier populations with a 3-of-4 acceptance quorum. Population states distinguish canonical and cached evidence, a validated joining population, a quarantined Byzantine population, an untrusted joiner, rollback, active fork, and missing state. Churn modes cover stable membership, one leave, one join, simultaneous leave/join, two leaves, and membership fork. History retention separately distinguishes full history, threshold 3-of-4 fragments, threshold cached fragments, below-threshold fragments, and forked fragments.

The exhaustive matrix contains **3,072,000** cases. Exactly **12,710** admit. Accepted recovery includes **4,400** states with a quarantined Byzantine population, **9,620** join-churn recoveries, **3,040** simultaneous leave/join recoveries, **6,500** threshold-fragment recoveries, and **7,626** recoveries with delayed compaction publication. **2,200** accepted states contain an untrusted joiner only because three other populations satisfy quorum; the untrusted joiner contributes no quorum credit.

There are **zero** post-deadline admissions, **zero** rollback admissions, **zero** active-fork admissions, **zero** membership-fork admissions, and **zero** below-threshold-fragment admissions. Delayed compaction publication and gossip consume the same 3-step deadline rather than receiving independent windows. A validated joining population may count only in explicit join/reconfiguration modes; an untrusted joiner never counts.

## Preserved results and evidence ceiling

The exact horizon-22 lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These remain synthetic model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

The conservative cross-role evidence credit remains **12**. No committed externally bound provider/hardware/operator independence evidence exists, so V62 does not raise that credit.

## V63 frontier

V63 should rotate the long-horizon witness set itself without overlap self-bootstrap and test simultaneous loss of a witness provider and pre-rotation root sources. It should extend compacted anchor history across multiple anchor generations with deletion/tombstone proofs that cannot erase a still-live revocation obligation or reset its original deadline. Verifier recovery should test two simultaneous quarantined populations and threshold reconfiguration without counting untrusted joiners. Cross-role credit remains 12 absent committed independently validated external provider/hardware/operator evidence, and V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

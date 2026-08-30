# WinLoop Continuation — V63

**Status:** validated continuation from committed V62. V63 binds to V62 validation digest `66c617a9972e89c527e35beee814d16822326c6548c277462d00314748fb70c5` and implementation SHA-256 `864db53ceae4a988db3eb2df78ebf067192cd5f11483767d01b6264ffb25b698`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Disjoint long-horizon witness rotation

V62 rotated the locally pinned root-history anchor through a long-horizon witness role whose old/new witness sets still overlapped. V63 rotates that witness role itself from `horizonWitnessB/C/D` to a fully disjoint `horizonWitnessE/F/G` set. The handoff hash binds the committed V62 anchor and transition, the new epoch-13 anchor, both complete witness rosters, and an explicit disjoint-dual-quorum label. Acceptance requires independent 2-of-3 current-or-cached evidence from both the old and new sets; because the sets are disjoint, no overlapping witness can bootstrap both sides of the handoff.

The exact matrix contains **2,343,750** cases across five transition-record states, five states for each of six witnesses, six provider/source-loss modes, and five root-source modes. Exactly **2,192** admit. This includes **280** old-witness-provider-loss recoveries and **280** new-witness-provider-loss recoveries. Under simultaneous pre-rotation root-source disappearance with the old pin retained, **140** old-provider-loss and **140** new-provider-loss states still recover from cached canonical evidence.

There are **zero** stale acceptances, **zero** fork acceptances, and **zero** new-anchor-only or unpinned acceptances. Removing the old pin fails closed. The disjointness is a modeled role property only; it is not treated as proof that providers, operators, hardware, custody, or organizational control are actually independent.

## Three-generation anchor compaction with deletion/tombstone proofs

V63 extends anchor history through three generations and makes deletion explicit. `T12` binds the epoch-12 anchor checkpoint to a tombstone that preserves the original revocation-deadline origin; `CP13` and `T13` then bind forward from that proof, and `CP14` includes the retained tombstone chain rather than replacing it with a fresh trust origin. A compacted checkpoint therefore cannot erase a still-live revocation obligation or restart its timing budget.

The exact matrix contains **1,638,400** cases across five history objects, four per-object states, three delay segments, five compaction modes, and five revocation/clear modes. Exactly **4,480** admit. **1,280** recover with CP12 compacted behind `T12`, **640** recover with both CP12 and CP13 compacted behind retained tombstones, and **2,240** accepted states preserve an explicitly live revocation obligation.

The revocation deadline remains one shared **3-step** end-to-end window rooted at epoch 12. There are **zero** post-deadline admissions, **zero** deadline-reset admissions, **zero** live-revocation-erasure admissions, **zero** stale/fork-clear admissions, and **zero** missing-tombstone admissions. Later compaction layers do not mint a new timing budget.

## Two simultaneous verifier quarantines and threshold reconfiguration

V62 used four verifier populations with a 3-of-4 quorum. V63 expands the recovery model to five verifier slots and a 3-of-5 threshold so that two simultaneous quarantines can be tolerated only when three other trusted/current populations indepently satisfy quorum. Reconfiguration modes distinguish stable membership, threshold reconfiguration, one validated join, explicit two-quarantine reconfiguration, and membership fork. Validated joiners count only in explicit reconfiguration modes; untrusted joiners never receive quorum credit.

The exact matrix contains **2,488,320** cases. Exactly **81,440** admit. Accepted states include **13,100** recoveries with at least two quarantined populations and **3,800** explicit two-quarantine reconfiguration recoveries. **43,150** accepted states contain an untrusted joiner only because three other populations independently satisfy quorum; the untrusted joiner contributes no credit.

There are **zero** untrusted-join quorum-credit acceptances, **zero** invalid-state acceptances, **zero** membership-fork acceptances, **zero** below-threshold-history acceptances, and **zero** post-deadline acceptances. Publication and gossip again consume the same 3-step deadline.

## Preserved results and evidence ceiling

The exact horizon-22 lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These remain synthetic model parameters rather than empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

The conservative cross-role evidence credit remains **12**. Disjoint modeled witness identities are not externally bound independence evidence, and no committed provider/hardware/operator independence certificate exists, so V63 does not raise that credit.

## V64 frontier

V64 should bind the disjoint long-horizon witness rotation to independently evidenced provider/operator/hardware identities before any cross-role-credit increase. It should extend tombstone-preserving compaction through anchor epoch 15 under concurrent revocation, delayed publication, and source disappearance, and it should test 3-of-5 verifier recovery under one Byzantine fork plus two quarantines and a joining population without quorum-credit inflation. Cross-role credit remains 12 absent committed independently validated external provider/hardware/operator evidence, and V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

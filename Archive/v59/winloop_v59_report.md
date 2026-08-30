# WinLoop Continuation — V59

**Status:** validated continuation from committed V58. V59 binds to V58 validation digest `e7586e621aa93dbcc78cd5f914266ddca0e38b0c787524642c16301d38a1c5d0` and implementation SHA-256 `10b2997c40c6016426f7f082a7176fe1a65a91a4a3cdc9f0f1e47c7fbabf631c`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independently witnessed issuer-set rotation

V58 identified the time-quorum membership and issuer-generation registry as modeled state. V59 makes that state explicit and binds the epoch-9 transition from `timeA,timeB,timeC` to `timeB,timeC,timeD` to a rotation record whose binding hash covers old membership, new membership, per-issuer generations, canonical A9/B9/W9 target, epoch, and rotation nonce. Admission requires a 2-of-3 witness quorum over that exact record.

The exact authority/witness matrix contains **500** cases: four membership-authority states times five states for each of three witnesses. Exactly **8** cases admit. Four are canonical-authority cases with either all three witnesses current or exactly two current plus one absent. Four additional cases demonstrate availability after the membership authority disappears, provided a previously canonical record remains cached and the same witness threshold still validates it. Stale replay and forked membership records admit **zero** cases. A single witness is insufficient, and any presented stale, old-generation, or forked witness fails closed rather than being ignored.

This directly tests the frontier question from V58: a compromised or disappeared membership authority cannot induce a stale quorum after rotation in this model. Disappearance alone does not destroy availability if canonical witnessed state is already present; compromise alone cannot replace that state because the canonical binding and witness threshold must still match.

## Rotated time quorum

The 2-of-3 monotonic time quorum now consists of `timeB,timeC,timeD`, with expected generations B9/C9/D1. Every issuer certificate binds the witnessed membership-record hash in addition to issuer identity, target epoch, issuer generation, monotonic issue/expiry counters, and canonical A9/B9/W9 target.

Across **10,290** issuer-state / actual-step / wall-skew cases, exactly **80** admit: 20 all-current timely cases and 60 single-issuer-partition recoveries. There are **zero** post-deadline stale acceptances and **zero** acceptances containing an old-membership issuer certificate. Thus generation change and issuer-set change are not separable trust inputs: both must resolve to the witnessed rotation record.

## Simultaneous partition, delayed publication, and verifier split view

V59 then composes three reduced time-issuer states (`current`, `absent`, `old_membership`) with three verifier populations (`canonical`, `missing`, `fork`, `stale`) and publication/gossip delays 0..5. The exhaustive matrix contains **62,208** cases.

Authorization requires at least two current time issuers, at least two canonical verifier populations, no presented old-membership issuer state, and a single shared revocation-lifetime budget satisfying `publication_delay + gossip_delay <= 3`. Exactly **400** cases admit, all within that deadline. Of those, **300** survive one time-issuer partition, and **90** simultaneously survive one time-issuer partition plus one forked verifier population. The same partition+fork case admits at total delay 3 and rejects at total delay 4. There are **zero post-deadline acceptances**.

The shared deadline is intentionally stricter than separately granting three steps to publication and another three to gossip. It prevents serial delay stages from multiplying verifier-visible stale-authorization lifetime.

## Preserved results and evidence ceiling

The horizon-22 exact lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These are synthetic model parameters, not empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

The conservative cross-role evidence credit remains **12**. No committed externally bound provider/hardware/operator independence evidence exists, so witnessed time membership does not raise the provenance-independence credit.

## V60 frontier

V60 should recurse one level deeper by binding changes to the **membership-witness roster itself** to a separately rooted threshold history, then model multiple consecutive issuer-set rotations with offline verifier catch-up and replayed intermediate membership records. It should test whether witness-set churn, partial witness disappearance, or a compromised old witness majority can resurrect a superseded issuer set. Cross-role credit must remain 12 absent committed independently validated external provider/hardware/operator evidence, and V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

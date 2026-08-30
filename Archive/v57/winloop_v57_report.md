# WinLoop Continuation — V57

**Status:** validated continuation from committed V56. V57 binds to V56 validation digest `c3527721770a05486cf17700f2642ae97cd491900fef9d523a50ce3a67a26273` and implementation SHA-256 `3908b88731cd3dacc6b9be5bd9438af5910e81f4e3811908bfe2bf2c839e0635`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Monotonic deadline certificates

V56's 3-step verifier revocation deadline is now bound to an explicit epoch-scoped time certificate containing issuer identity, target epoch, issued monotonic counter, expiry monotonic counter, wall-step evidence, and a binding hash. Security freshness is determined by the trusted monotonic counter and target epoch; wall clock is bounded consistency evidence only, so ordinary wall-clock skew cannot extend authorization lifetime.

The model exhaustively enumerates **180** combinations of actual step 0..5, wall-clock skew -2..+2, rollback 0..2, and old/current epoch 7/8. Exactly **20** current, non-rolled-back cases at or before the deadline are accepted (four timely steps across each of five skew values). All **10** current post-deadline cases are rejected, all **60** current rollback cases are rejected, all **90** old-epoch cases are rejected, and there are **zero stale acceptances after the deadline**. A certificate whose expiry field is modified without recomputing its binding hash is rejected.

This closes the V56 ambiguity where a deadline existed as a verifier rule but was not itself bound to a monotonic source. It does not claim physical clock independence: the time issuer remains a modeled authority and is not credited as an externally independent provider/hardware/operator root.

## Asymmetric source disappearance and same-epoch equivocation

V57 separately enumerates **144** dual-log source states: presence/absence of two sources for log A and two for log B, crossed with no-fork/source-1-fork/source-2-fork modes on each log. The target A8/B8 roots are bound by the consumed epoch certificate and verifier gossip digest.

A single honest source loss on either log remains available when the surviving source presents the canonical target root; the exhaustive table contains **24** accepted states with asymmetric single-source loss and **25** accepted states total. All **63** states with whole-log loss fail closed. Across the matrix, **80** states in which an actually present source equivocates are rejected. Explicit checks reject A or B same-epoch conflicting roots, a sole surviving fork, and whole-log disappearance while accepting one-current-source recovery.

The rotation sequence remains A at epoch 7, B at epoch 8, witness generation at epoch 8. A source cannot authorize merely because it presents a syntactically valid same-epoch checkpoint; the root must equal the target root already bound into the consumed epoch certificate/gossip state. Unknown or conflicting source state fails closed.

## Preserved results

The horizon-22 exact lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These remain synthetic model parameters, not empirical attacker prices or response times. The 513-statement checkpoint/Merkle recovery bound, lag64/lag65 freshness boundary, frontier-only storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and the no-new-runtime-envelope claim are carried unchanged.

The conservative cross-role evidence credit remains **12**. No committed externally bound provider/hardware/operator independence evidence exists in the repository, so no additional independence credit is claimed from signed metadata or from the new time-source model.

## V58 frontier

V58 should compose the monotonic deadline rule with multiple time issuers and explicit issuer disagreement/partition/rotation; test verifier-population split views under same-epoch log equivocation with delayed gossip convergence; and continue to fail closed on unknown provenance. Cross-role credit must remain at 12 unless externally bound provider identity, hardware custody, operator authority, issuer/source, subject, epoch, and binding-hash evidence is committed and independently validated. V21 routing remains active unless a candidate independently clears the >=2,000-seed replacement bar and honest message accounting.

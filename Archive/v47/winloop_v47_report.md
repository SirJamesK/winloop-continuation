# WinLoop Continuation — V47

**Status:** validated continuation from committed V46. V47 carries the V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves admission at joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Advancement

V47 moves V46's transparency, witness, and issuer checks inside all **22 primitive provenance statements**. Every statement now binds its exact Merkle inclusion proof and checkpoint, a timely non-equivocating 2-of-3 witness quorum, a 2-of-3 issuer quorum whose selected seats retain the 8-root CA/HSM/operator/seat-local dependency cut, and an independent root-specific local binding. All 22 envelopes validate; tampered inclusion, two late witnesses, shared issuer-CA control, and mismatched local binding reject.

Those control roots are also in the same OR-of-AND false-WIN model. Distinct issuer+witness infrastructure has cut 10. With independent per-statement local bindings the direct 22-root provenance compromise remains the winning route, so the integrated baseline is **joint 21 / provenance 22 / lower 63 — PASS**. Removing statement-local bindings opens cut 10; collapsing all 22 locals into one common root opens cut 11; common issuer-CA or witness control lowers the infrastructure cut to 9 and rejects; fully shared issuer CA+HSM+operator, witness, and local control reaches cut 7. The local factor therefore has to be genuinely independent, not merely present in metadata.

## Exact temporal budget optimization

V47 extends the delay model from seven selected roots to all **22** provenance roots and solves the full `2^22 = 4,194,304` binary schedule space by exact 0/1 dynamic programming over budgets 0..103. The reference classes are 11 anchors (stale-authorization delay, synthetic cost 6), 4 authority/control roots (verifier-consumption delay, cost 4), and 7 local/ceremony roots (ceremony-validity delay, cost 3). Strict windows give one verifier-visible epoch; the modeled delay gives two. These windows and 3/4/6 costs are model parameters, not empirical response times or attack prices.

Exact thresholds are: budget 0 => 21/22/lower63 PASS; budget 3 => provenance 21, first route-floor failure; budget 6 => provenance20/lower60; budget 9 => provenance19/lower57, first aggregate-cost failure; budget 21 => provenance15/lower45; budget 37 => exact two-epoch floor provenance11/joint11/lower33. More budget cannot reduce the two-epoch peak below 11.

## Frontier/cache accounting

At 128 statements: 128 leaf + 127 internal hashes = 255 append hashes; final frontier 1 hash/32 bytes, peak 7 hashes/224 bytes, average 3.5078125 hashes; materialized inclusion siblings 28,672 bytes; all prefix-to-final consistency proofs 28,448 bytes; summed per-append consistency proofs 18,176 bytes. These are storage/computation figures only. Trust-bearing publication/gossip/issuer paths remain unchanged and shared-audit accounting remains `132 + 4*k` messages/epoch.

## V48 frontier

Extend the exact optimizer to three-or-more epochs with repeated stage-specific reuse; add temporal compromise/rotation/recovery of witness and issuer infrastructure to the same optimizer; extend checkpoint churn beyond 128 statements with cache eviction/recovery and delayed consistency propagation; retain V21 routing unless a replacement independently clears its >=2,000-seed acceptance bar.

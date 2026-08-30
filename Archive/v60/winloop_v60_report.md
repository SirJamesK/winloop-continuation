# WinLoop Continuation — V60

**Status:** validated continuation from committed V59. V60 binds to V59 validation digest `c9a88403f543d13783c21aa19308f35ba9ffb403ef76c7f06119b22916f992b5` and implementation SHA-256 `ff517f4bd1ebc7d75c848ce09f403e8ba7ed386edd4fc168383faccb2111c7b5`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Separately rooted witness-roster history

V59 bound issuer-set rotation to a 2-of-3 witness roster but left changes to that roster as the next recursive trust frontier. V60 adds a separate three-authority threshold history for the epoch-10 witness transition from `witness1,witness2,witness3` to `witness2,witness3,witness4`. The transition record binds old/new roster, old/new generations, previous history root, epoch, nonce, and a content hash; two of three distinct history-root authorities must attest that exact record.

The exact matrix contains **500** authority/root-certificate cases: four transition-authority states times five states for each of three history-root authorities. Exactly **8** admit. Four survive disappearance of the transition authority by using a previously cached canonical record. Stale or forked roster records admit **zero** cases. Any presented stale-generation, stale-epoch, or forked root certificate fails closed rather than being ignored. A single root authority is insufficient.

This does not assert physical or organizational independence merely because the metadata is threshold-signed. The separate root removes one circular logical dependency; cross-role provenance credit remains capped at 12 absent externally bound evidence.

## Two consecutive issuer rotations with offline catch-up

V60 then composes the epoch-9 issuer transition `timeA,timeB,timeC → timeB,timeC,timeD`, the separately rooted epoch-10 witness-roster transition, and the epoch-10 issuer transition `timeB,timeC,timeD → timeC,timeD,timeE`. The epoch-10 issuer record must hash-bind both the canonical epoch-9 membership record and the canonical epoch-10 witness-roster record. Offline verifiers may recover from cached canonical stage records, but the terminal state must be the epoch-10 issuer membership; an epoch-9 intermediate record is never accepted as current.

The exact composed matrix contains **192,000** cases across five states for each of the three chain stages, four verifier terminal states, catch-up delay 0..5, eight root-history availability/adversary modes, and eight new-witness availability/adversary modes. Exactly **512** admit, all within the single shared three-step revocation/catch-up deadline. Of those, **384** are delayed/offline recoveries, **448** include disappearance of at least one stage authority with cached canonical state, and **288** simultaneously tolerate one missing history-root source and one missing new-witness source.

There are **zero** post-deadline admissions, **zero** replayed-intermediate terminal admissions, **zero** fork-terminal admissions, and **zero** admissions in the old-witness-majority mode. The same canonical chain accepts at delay 3 and rejects at delay 4. Missing the roster-transition link, presenting forked history-root evidence, or trying to terminate on the superseded epoch-9 membership fails closed.

The deadline is end-to-end, not per stage. Publication, witness-roster change, issuer rotation, and verifier catch-up cannot each claim a fresh three-step stale-authorization allowance; otherwise serial stages would multiply the effective stale window.

## Preserved results and evidence ceiling

The exact horizon-22 lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These are synthetic model parameters, not empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

The conservative cross-role evidence credit remains **12**. No committed externally bound provider/hardware/operator independence evidence exists; V60 therefore does not raise that credit.

## V61 frontier

V61 should rotate the separate witness-history root authorities themselves and test recursive root-of-root churn without circular trust. It should then extend catch-up across at least three consecutive issuer/witness rotations with compacted checkpoints, mixed-generation recovery, verifier checkpoint rollback/equivocation, and partial history retention/source disappearance. Cross-role credit must remain 12 absent committed independently validated external provider/hardware/operator evidence, and V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

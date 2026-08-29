# WinLoop Continuation — V48

**Status:** validated continuation from committed V47. V48 carries the V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves the strict admission contract at joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Advancement: exact repeated reuse through four epochs

V48 replaces V47's binary one-extra-epoch budget with an exact maximum-window scheduler over **2, 3, and 4 verifier-visible epochs**. The 22 provenance roots remain the V47 composition: 11 anchors, 4 authority/control roots, and 7 local/ceremony roots. Each class has sequential stage costs for extending verifier-visible reuse: anchors `6/7/8`, authorities `4/5/6`, and locals `3/4/5`; cumulative costs correspond to windows 1..4. These remain synthetic model parameters, not empirical attacker prices, detection times, or recovery times.

For a chosen window configuration, exact peak cardinality is computed from the nested suffix-capacity condition: for each `k`, every root usable for at most `k` epochs must fit into `k * peak` acquisition slots. Dynamic programming evaluates all distinct aggregate window states rather than enumerating `4^22` assignments.

The exact floors are:

- strict: provenance 22 / joint 21 / lower 63 — **PASS**;
- first route-floor failure: synthetic budget 3 -> provenance 21;
- first aggregate lower-cost failure: budget 9 -> provenance 19 / joint 19 / lower 57;
- 2 epochs: irreducible provenance floor **11**, first reachable at budget **37**;
- 3 epochs: irreducible provenance floor **8**, first reachable at budget **79**;
- 4 epochs: irreducible provenance floor **6**, first reachable at budget **130**.

Thus V42's carried two-/three-epoch degradation pattern is reproduced and extended without treating reuse as a single binary flag. More verifier-visible lifetime monotonically lowers the attacker's peak acquisition burden, so verifier-effective revocation consumption remains the operative temporal variable.

## Witness/issuer infrastructure in the same temporal model

The V47 evidence path is independently revalidated: a minimal evidence-infrastructure compromise requires two witnesses plus two issuer seats with CA/HSM/operator/seat-local dependencies, giving static infrastructure cut **10**. Applying the same 2/3/4-epoch scheduler yields infrastructure-only peak floors **5 / 4 / 3** at minimum synthetic budgets **18 / 30 / 50**.

This does not create a cheaper accepted false-WIN route because every forged primitive statement still requires an independent statement-local binding. The complete forged-evidence path therefore has 32 roots and, through four epochs, never undercuts the direct 22-root provenance route at equal modeled budget; its four-epoch floor is 8 versus the direct route's 6. Verifier-effective quarantine/recovery before the next epoch resets recovered witness/issuer controls to window 1 and restores the static infrastructure cut 10.

The result is strategically important: static quorum diversity is not itself temporal security. Recovery must become verifier-visible before stale control artifacts can span epochs, or the infrastructure cut compresses even though the integrated direct provenance route remains the winner in this reference model.

## Checkpoint churn beyond 128 statements

V48 extends the RFC9162-style Merkle model to **257 statements**, crossing both the 128 and 256 boundaries. All 257 inclusion proofs validate, selected consistency proofs across boundary sizes validate, and an evicted checkpoint at size 193 can be recomputed from the canonical event history and verified forward to 257. Tampering with the recovery proof is rejected.

A modeled checkpoint freshness bound of **64 statements** is now explicit: a valid 193->257 consistency path (lag 64) is accepted, while a cryptographically valid 192->257 path (lag 65) is rejected for freshness. This bound is a WinLoop model parameter, not an RFC-mandated value.

Resource accounting at 257 statements is 257 leaf hashes + 255 append-internal hashes = 512 append hashes; the peak binary frontier is 8 hashes / 256 bytes. A four-checkpoint root cache is 128 bytes. Rebuilding an evicted checkpoint from canonical history requires 257 leaf hashes + 256 internal hashes in the worst full-rebuild reference case. Frontier/cache changes remain storage/computation optimizations only: authority, quorum, publication, gossip, and the carried `132 + 4*k` trust-bearing message formula are unchanged.

## V49 frontier

1. Replace maximum-lifetime windows with explicit time-indexed compromise, detection, quarantine, rotation, publication, verifier-consumption, and recovery trajectories.
2. Extend exact scheduling to five-plus epochs and asymmetric route requirements while keeping synthetic costs clearly non-empirical.
3. Model adversarial checkpoint-cache eviction together with source loss, split-log recovery, delayed propagation, and recovery-proof availability beyond 257 statements.
4. Retain V21 guarded routing unless a replacement independently clears the existing >=2,000-seed stationary/near-threshold acceptance bar and materially improves gradual/selective/correlated detection without extra probes.

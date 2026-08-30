# WinLoop Continuation — V52

**Status:** validated continuation from committed V51. V52 preserves the carried V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves admission at joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Exact compressed temporal optimization through eight epochs

V51's six-epoch optimizer enumerated 80,730 terminal window-count states. V52 proves an exchange reduction for the same monotone per-root window costs: if a later window holds more than peak cap `p` while an earlier window has spare capacity, shifting one root left cannot increase cost. Therefore an exact peak-`p` optimum exists with capacity `p` on each lifetime window, and the problem reduces to a small integer min-cost bipartite flow over 22 roots and `h` windows.

The compressed solver exactly reproduces every V51 nominal floor/budget pair through six epochs: `11/34`, `8/66`, `6/102`, `5/130`, `4/174`. Seven epochs still have irreducible floor **4** and nominal budget **174**. At eight epochs the first new phase appears: the irreducible floor becomes **3**, with minimum budgets **178 / 248 / 318** under lower / nominal / upper envelopes. A raw eight-window count-state enumeration would contain **1,560,780** terminal states; the exact flow construction reaches the same optimization target without enumerating that state space.

At eight epochs first provenance failure (`22 -> 21`) remains at budgets **1 / 2 / 3** and first lower-cost failure (peak 19, lower 57) at **4 / 7 / 10** for lower / nominal / upper envelopes. Verifier-visible consumption remains the operative lifetime gate.

V52 also enumerates **16** correlated semantic shock combinations over anchor detection, authority publication, local-guard consumption, and observation censoring. The strongest modeled correlated case combines authority-publication lowering, local-consumption lowering, and observation censoring; it reaches floor 3 at budget **204**, a **44** reduction from nominal 248, and reaches route-21 / lower-19 at budgets **1 / 4**. These are synthetic model parameters, not empirical attack prices or measured response times.

## Recursive decomposition of V51 local guards

Each V51 abstract local guard is now expanded as an AND:

`current_local_possession AND fresh_local_ceremony`

across all six candidate shared-authority groups and all **63** non-empty group combinations.

With both subroots distinct per guard, every combination remains admitted and minimum provenance rises to **23**. If one entire subroot family is globally shared, every combination still remains admitted with minimum provenance **23** because the other family remains independent. If the two primitives collapse within each guard, or one family is absorbed into the associated shared authority while the other stays distinct, the minimum returns to exactly **22** and remains admitted.

The critical hidden-sharing boundary is sharper than the V51 abstraction: if **both** guard subroot families become global common roots, all combinations of three or more shared authorities fail; **42 of 63** combinations are rejected and the worst provenance cut is **18**. If both families are absorbed into the authority fabric, all 63 cases fail and the best provenance cut is **21**. This is graph-theoretic cut accounting only; it does not prove physical, organizational, hardware, supply-chain, or cloud independence.

## Witness-set rotation bound into recursive evidence cuts

V52 replaces the abstract witness root in evidence accounting with a current witness seat requiring:

`witness signing authority AND witness-rotation-local current evidence`

under stable 2-of-3 witness seats, while retaining 2-of-3 issuer seats with CA/HSM/operator/local prerequisites.

The recursive evidence-infrastructure cut is **12**, giving margin +2 over the carried cut-10 threshold. A common witness signing authority with distinct rotation-local roots gives cut **11** (+1). Making both witness authority and rotation-local control common gives cut **10** (zero margin). Absorbing rotation-local evidence into the common witness authority produces cut **9** and is rejected. This quantifies exactly where witness rotation consumes the remaining provenance margin.

Three witness epochs are exercised explicitly: one lost seat is tolerated by 2-of-3 quorum, two lost seats reject, mixed-generation signatures reject, duplicate-seat inflation rejects, old epochs reject after verifier consumption, a current epoch-3 quorum accepts, and skipped/missing rotation chains reject. The availability margin is exactly one witness seat.

## Preserved checks

Static reference remains **joint 21 / provenance 22 / lower 63**. Six carried common-control collapse tests remain provenance 21 and rejected; all 63 collapse-only overlap combinations remain rejected, worst provenance 16. Unknown/stale/cyclic/unbound provenance fails closed.

The 513-statement Merkle regression preserves selected inclusion verification, lag64 acceptance, lag65 rejection, proof tamper and split-log equivocation rejection, frontier-only persistence, and shared-audit accounting `132 + 4*k`. No trust-bearing message path is removed. V21 routing is unchanged and V52 claims no new runtime envelope.

## V53 frontier

1. Integrate the two-family local-guard sharing cases into the temporal lifetime optimizer instead of static-only cut accounting.
2. Extend witness/log rotation to delayed cross-epoch publication, verifier pin divergence, and partial source disappearance.
3. Recursively decompose issuer-local and witness-rotation-local primitives below today's evidence roots, failing closed on unknown independence.
4. Retain V21 routing unless a replacement independently clears the >=2,000-seed stationary/near-threshold bar and materially improves gradual/selective/correlated detection without extra probes.

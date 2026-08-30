# WinLoop Continuation — V53

**Status:** validated continuation from committed V52. V53 preserves the carried V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves admission at joint cut >=21, synthetic lower cost >=60, and every non-endpoint false-WIN route >=22.

## Temporal integration of recursive two-family guards

V52 decomposed each of six candidate local guards into `current_local_possession AND fresh_local_ceremony` but evaluated hidden-sharing aliases statically. V53 now constructs the exact aliased trust-root component set for every one of the **63** non-empty authority-group combinations under six guard-sharing modes and feeds each set into the same exact eight-epoch capacitated min-cost lifetime flow. This yields **378** guard/lifetime cases without changing V52's base temporal optimizer.

The static boundary remains sharp inside the temporal model. Distinct two-subroot guards admit all 63 combinations with provenance **23..28**; one globally shared subroot family also admits all 63 at provenance **23**; within-guard collapse and one-family absorption admit all 63 at exactly **22**. If both guard families are global, only **21 of 63** combinations remain statically admissible and the first failure occurs at **three shared authorities**; if both families are absorbed into the authority fabric, **all 63** cases fail before temporal reuse is considered.

For the statically admitted cases, the exact eight-epoch lifetime flow gives minimum synthetic budgets to cap verifier-visible concurrent provenance at 21 of **4** for distinct guards, **4** for one global family, **2** for within-guard collapse, **2** for one-family absorption, and **2** for the admitted both-global cases. The minimum modeled budgets to each case's irreducible eight-epoch floor are **216 / 258 / 229 / 244 / 226** respectively. These are synthetic model parameters, not empirical attacker prices or measured response times. Temporal reuse cannot rehabilitate a graph that already violates the static provenance cut.

## Delayed witness/log rotation, verifier pin divergence, and source disappearance

V53 extends the witness/log rotation model through four witness epochs and makes verifier pins monotonic per log. Acceptance now requires: a same-epoch 2-of-3 witness quorum; target epoch not below any verifier pin; a valid rotation chain; freshness lag <=64; at least one current source for each of both logs; and no same-epoch source equivocation.

The regression set verifies that delayed cross-log publication rejects until both logs reach the target epoch, a converged epoch-3 state accepts, replay below a consumed pin rejects, mixed witness generations reject, broken rotation chains reject, same-epoch source forks reject, lag64 accepts, and lag65 rejects. One current source may disappear from each log while the surviving source preserves continuity, but loss of the entire source set for either log fails closed. Pin updates are monotonic and cannot be rolled back by stale observations.

## Recursive issuer-local and witness-rotation-local decomposition

V52 credited each issuer-local and witness-rotation-local prerequisite as one root. V53 recursively expands each modeled local prerequisite into `current possession AND fresh ceremony` and evaluates sharing aliases under the 2-of-3 issuer-seat and 2-of-3 witness-seat structure.

With explicit independence, the modeled evidence-infrastructure cut rises from the V52 abstract **12** to **16**. Sharing both issuer-local families globally gives **14**; sharing both witness-local families globally gives **14**; sharing each role's local families separately gives **12**; and collapsing the local possession/ceremony families across issuer and witness roles gives exactly **10**, consuming all margin above the carried evidence threshold. Adding a common witness signing key to those cross-role shared locals drops the cut to **9** and is rejected; absorbing all local evidence gives **8** and is rejected.

The conservative credited cut remains **12** unless the new subroots are independently evidenced. Signed metadata is not treated as proof of physical, organizational, cloud, hardware, supply-chain, operator, or custody independence. Unknown, stale, cyclic, or unbound local provenance fails closed.

## Preserved checks

V52's exact temporal regression is unchanged through eight epochs: nominal floor/budget pairs remain `11/34`, `8/66`, `6/102`, `5/130`, `4/174`, `4/174`, and `3/248` for horizons 2..8. At eight epochs, first provenance failure remains synthetic budget **2**, first lower-cost failure remains **7**, and the strongest carried correlated shock reaches floor 3 at budget **204**.

Static reference remains **joint 21 / provenance 22 / lower 63**. The six carried common-control collapses remain provenance 21 and rejected; all 63 collapse-only overlap combinations remain rejected with worst provenance 16. The 513-statement Merkle regression preserves selected inclusion verification, lag64 recovery, lag65 rejection, proof-tamper and split-log-equivocation rejection, frontier-only persistence, and shared-audit accounting `132 + 4*k`. V21 routing is unchanged and V53 claims no new runtime envelope.

## V54 frontier

1. Extend the temporal guard-sharing optimizer beyond eight epochs and add correlated lifetime shocks that target an entire guard family rather than root classes independently.
2. Model two verifier populations advancing pins asynchronously, including temporary whole-log absence followed by authenticated recovery and consistency proof replay.
3. Recursively decompose the cross-role local possession/ceremony roots into hardware custody, operator authority, publication, and recovery prerequisites while retaining conservative credit until independence is demonstrated.
4. Retain V21 routing unless a replacement independently clears the >=2,000-seed stationary/near-threshold bar and materially improves gradual/selective/correlated detection without extra probes.

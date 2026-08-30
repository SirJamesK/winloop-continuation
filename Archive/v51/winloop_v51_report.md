# WinLoop Continuation — V51

**Status:** validated continuation from committed V50. V51 preserves the carried V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves admission at joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Six-epoch uncertainty/censoring optimization

V51 extends V50's exact heterogeneous temporal optimizer from five to **six epochs** over the same 22 recursive-route roots. Each detection/publication/verifier-consumption stage now has a per-root integer uncertainty interval `[nominal-1, nominal, nominal+1]` (lower-bounded at one). These remain synthetic model parameters, not measured attack prices or response-time SLAs.

The six-epoch exact state space contains **80,730** terminal window-count states with irreducible peak floor **4**. Minimum synthetic budgets to reach that floor are **124 / 174 / 224** for lower / nominal / upper envelopes. First provenance failure (`22 -> 21`) occurs at budgets **1 / 2 / 3**; first lower-cost admission failure (peak 19, lower 57) occurs at **4 / 7 / 10**.

Nominal regression exactly preserves V50 through five epochs: `11/34`, `8/66`, `6/102`, `5/130` for floor/budget at 2/3/4/5 epochs. Observation censoring adds no further reduction beyond the lower envelope in the exact optimum; verifier consumption remains the operative lifetime gate.

## Guarded shared-authority construction

V50 showed all **63** non-empty combinations of six candidate shared-control collapses fail admission. V51 tests a constructive repair: each shared authority must be an **AND** with its own independently auditable, current local guard.

All 63 combinations with distinct guard roots remain admitted and the minimum provenance cut is **22**. Independence is necessary: if multiple collapsed authority groups share one common guard, every multi-group case fails and the worst provenance cut is **17**; if guards collapse back into their associated authorities, all 63 cases fail and the best provenance cut is **21**.

This is a graph-theoretic condition, not proof that real organizations or hardware are independent. The new guard roots must be recursively decomposed in V52.

## Monotonic transparency-log and witness churn

V51 adds explicit state for key epochs, witness-set epochs, log sizes/roots, and stable witness seats. Under partial propagation the verifier accepts a valid rotation before consumption, but after epoch consumption it rejects old log keys and old witness sets. Mixed-generation witness signatures cannot form a quorum, duplicate signatures from one seat cannot inflate quorum, valid propagation completion is accepted, and same-size post-pin dual-log equivocation, split roots, and missing key/witness rotation chains are rejected.

A coherent first-seen fork at a previously unseen size still depends on independent log/witness assumptions; signed metadata alone cannot prove organizational or physical independence.

## Preserved checks

Static reference remains **joint 21 / provenance 22 / lower 63**. Six carried common-control collapse tests remain provenance 21 and rejected. The 63 collapse-only overlap combinations remain rejected, worst provenance 16. Evidence infrastructure remains cut **10**; common issuer-CA or common witness control reduces it to **9** and is rejected. Unknown/cyclic provenance fails closed.

The 513-statement Merkle regression preserves selected inclusion verification, lag64 acceptance, lag65 rejection, tamper/equivocation rejection, frontier-only persistence, and shared-audit accounting `132 + 4*k`. V21 routing is unchanged and V51 claims no new runtime envelope.

## V52 frontier

1. Extend interval/censor optimization to correlated choices and seven-plus epochs without state explosion.
2. Recursively decompose every new local guard and reject hidden shared guard roots.
3. Bind witness-set rotation into recursive evidence-cut accounting and quantify quorum-churn margins.
4. Retain V21 routing unless a replacement independently clears the >=2,000-seed stationary/near-threshold bar and materially improves gradual/selective/correlated detection without extra probes.

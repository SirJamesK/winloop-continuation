# WinLoop Continuation — V55

**Status:** validated continuation from committed V54. V55 binds to V54 validation digest `d3466a473a016f5555b7a3b758cd8ca8af5b37f4b9641578b012ccce02149ba7` and implementation SHA-256 `9148d974d63808fe7beb6cecf3a44102eb412c1e3f5fa10109adc2b2de4a8742`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Horizon-22 exact lifetime floor

The exact 22-root capacitated min-cost lifetime flow is extended from 12 to **22 horizons**. Every V54 horizon-2..12 floor/budget pair is reproduced exactly. The floor remains 2 from horizons 11 through 21 at synthetic minimum budget 398 and first reaches the mathematical irreducible **floor 1 at horizon 22**, where the exact synthetic minimum budget is **851**. The corresponding raw terminal-composition count is 1,052,049,481,860; the solver uses capacitated min-cost flow rather than enumerating those states. These costs are model parameters, not empirical attacker prices or measured response times.

## Family shocks on floor-1-capable guard graphs

At horizon 22, only admitted guard graphs with exactly 22 verifier-distinct components can reach floor 1. V55 evaluates the **141 exact floor-1-capable cases** carried from V54: 63 within-guard-collapsed cases, 63 one-family-absorbed cases, and 15 admitted both-global cases.

For within-guard-collapsed graphs, the minimum nominal floor-1 budget is 778 and the simultaneous possession+ceremony-family shock minimum is 661; depending on the authority-sharing combination, the reduction ranges from 21 to **158**. One-family-absorbed graphs move from a minimum 833 to 807 under both shocks, with per-case reductions of 11..95. The 15 both-global floor-1 graphs move from minimum 775 to 737, with per-case reductions of 38..40. Route-21/lower-19 minima remain explicitly tracked; static rejection still precedes temporal reuse, so no rejected graph is rehabilitated by a long horizon.

## Three asynchronous verifier populations and witness churn

Recovery now models **three verifier populations** with independently monotonic split A/B pins: fast `{A:6,B:5}`, mid `{A:5,B:5}`, and slow `{A:4,B:4}`. Four family-shock trajectories are tested. Any affected population fails closed before the shocked log's authenticated consistency chain is available; after complete publication/recovery, all three populations accept the same epoch-6 roots.

The fast population rejects epoch-5 replay while the mid and slow populations may still accept epoch 5 according to their own pins. One current source loss per log is tolerated, but whole-log loss, same-epoch equivocation, lag65, or a tampered consistency token rejects for all populations.

Witness generation rotates across epochs 4/5/6 with seat identity preserved. Epoch-5 signatures cannot satisfy epoch 6, mixed-generation signatures cannot inflate quorum, duplicate signatures from one seat do not count twice, and a revoked current key cannot combine with one honest current seat to form quorum. A distinct current 2-of-3 quorum remains accepted.

## Recursive publication/recovery evidence

Publication/recovery is decomposed into provider, hardware, operator, and witnessed prerequisites. A fully independent modeled chain exposes cut 28, provider/witness sharing exposes cut 22, and collapsing publication/recovery back into already-counted local hardware/operator roots returns cut 12. A common witness key drops the modeled cut to 11; absorbing all local prerequisites drops to 8.

V55 therefore **does not raise** the conservative credited cross-role evidence above 12. Cryptographically signed metadata is not treated as proof of physical, organizational, provider, HSM, or operator independence. Unknown, stale, cyclic, or unbound independence claims fail closed.

## Preserved checks and V56 frontier

The 513-statement checkpoint/Merkle recovery bound, lag64/lag65 freshness boundary, frontier-only storage, unchanged trust-bearing message paths, and shared-audit accounting `132 + 4*k` remain carried. V21 routing is unchanged and V55 claims no new runtime envelope.

V56 should couple the horizon-22 floor-1 exposure directly to explicit revocation-consumption deadlines under partial multi-log partitions, rotate log and witness generations independently across the three verifier populations with cross-population gossip certificates, and seek externally bound provider/hardware/operator independence evidence before any increase above conservative cut 12.

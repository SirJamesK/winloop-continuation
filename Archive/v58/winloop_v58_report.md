# WinLoop Continuation — V58

**Status:** validated continuation from committed V57. V58 binds to V57 validation digest `bb5eec783aa363ef049af847df3e9924c21bc7c0d75fe9f4a3b09ad0c3395790` and implementation SHA-256 `018a2f9307098fe5130ca4bbabfaa73b6d9c53e93609946abfea9b7e5cafa79f`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Multi-issuer monotonic deadline quorum

V57 bound the three-step revocation deadline to one epoch-scoped monotonic issuer. V58 replaces that single modeled source with a **2-of-3 time-issuer quorum** (`timeA`, `timeB`, `timeC`) at target epoch 8. Every issuer certificate binds issuer identity, epoch, issuer generation, issued/expiry monotonic counters, advisory wall-step evidence, and the canonical A8/B8/W8 target.

The model exhaustively enumerates **10,290** issuer-state / actual-step / wall-skew cases: seven states per issuer (`current`, `absent`, `old_epoch`, `future_epoch`, `rollback`, `old_generation`, `fork`), actual steps 0..5, and wall skew -2..+2. Exactly **80** cases authorize: **20** with all three issuers current and **60** where exactly one issuer is absent and the other two current. There are **zero post-deadline stale acceptances**.

Absence is the only tolerated minority fault. A presented stale epoch, future epoch, rollback, old generation, or current same-epoch conflicting target causes the time gate to fail closed instead of being silently ignored. Modifying the expiry field without recomputing the binding hash is rejected. Wall time remains advisory consistency evidence; the security lifetime is still the monotonic counter plus target epoch/generation.

This improves partition availability over a single issuer without crediting three time sources as physically or organizationally independent roots. The quorum-membership and issuer-generation registry is still modeled state and therefore becomes part of the next frontier.

## Split-view verifier gossip convergence

V58 also models three verifier populations under same-epoch A/B log split views. Each population starts in one of seven states: canonical A8/B8, missing A, missing B, A fork, B fork, both forks, or stale epoch. Across gossip delay 0..5, the exact matrix contains **2,058** population-view/delay cases.

Authorization is evaluated only after gossip convergence. The epoch certificate already pre-binds the canonical A8/B8/W8 target; therefore a fork cannot win by presenting a syntactically valid same-epoch root. Recovery requires at least **two canonical population views**, and convergence must complete by the three-step deadline. The matrix yields **76** accepted post-convergence cases: **4** all-canonical cases and **72** split-view recoveries, including **36** one-population fork recoveries, **24** one-population missing-log recoveries, and **12** one-population stale-epoch recoveries. There are **zero acceptances after delay 3**.

Explicit checks accept two canonical populations plus one A-fork at delay 3, reject the same state at delay 4, accept two canonical plus one missing-B population at delay 2, and reject both one-canonical/two-fork and two-fork/one-missing configurations. Thus a noncanonical majority never authorizes; a canonical quorum may repair one divergent population only while the revocation window is still live.

## Composed gate and preserved results

The composed authorization gate requires both the time-issuer quorum and canonical-log gossip convergence. The independent exhaustive domains span **21,176,820** pattern pairs, of which **6,080** are the product of the individually admitted timely states; the composed model records **zero post-deadline stale acceptance** and keeps unknown, stale, conflicting, or unbound evidence fail-closed.

The horizon-22 exact lifetime regression remains floor **1 / synthetic budget 851**, with horizon 11 at floor **2 / budget 398**. These are model parameters, not empirical attacker prices or response times. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing message paths, shared-audit accounting `132 + 4*k`, V21 routing, and no-new-runtime-envelope claim remain unchanged.

The conservative cross-role evidence credit remains **12**. No committed externally bound provider/hardware/operator independence evidence exists, so the new issuer quorum and gossip behavior do not raise the provenance-independence credit.

## V59 frontier

V59 should bind time-quorum membership and issuer-generation changes to independently witnessed rotation records, then compose simultaneous time-issuer partition with delayed revocation publication and verifier split-view convergence. It should continue testing whether a compromised or disappeared membership authority can induce a stale quorum after rotation. Cross-role credit must remain 12 unless externally bound provider identity, hardware custody, operator authority, issuer/source, subject, epoch, and binding-hash evidence is committed and independently validated. V21 routing remains active unless a candidate independently clears the >=2,000-seed replacement bar and honest message accounting.

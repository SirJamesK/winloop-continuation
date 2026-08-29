# WinLoop Continuation — V50

**Status:** validated continuation from committed V49. V50 preserves the carried V13 endpoint theorem as baseline only, keeps V21 guarded routing, and preserves the strict static admission contract at joint cut >=21, synthetic lower cost >=60, and every non-endpoint route >=22.

## Advancement: heterogeneous adversarial observation schedules

V49 used symmetric class-level lifecycle extension costs. V50 replaces that symmetry with explicit per-root schedules in which detection, publication, and verifier consumption vary independently. Every one of the 22 recursive-route roots has distinct synthetic stage-delay rates, and the exact optimizer enumerates root-specific usable-authorization windows before solving the same Hall-condition peak-acquisition problem. These costs remain model parameters, not empirical attacker prices or operational response times.

The static graph remains **joint 21 / provenance 22 / lower 63**. Under the heterogeneous temporal model, the weakest root reaches a two-epoch verifier-visible window at synthetic budget **2**, so the first non-endpoint provenance failure is now **22 -> 21 at budget 2**. Three selected root extensions reduce the joint/provenance floor to **19** at aggregate budget **7**, crossing the lower-cost admission floor at **57**. This is a stricter result than V49's symmetric thresholds of 3 and 9.

Exact minimum budgets to reach the irreducible recursive-route peak floors are:

- 2 epochs: floor **11**, heterogeneous budget **34** vs V49 symmetric **37**;
- 3 epochs: floor **8**, heterogeneous budget **66** vs **79**;
- 4 epochs: floor **6**, heterogeneous budget **102** vs **130**;
- 5 epochs: floor **5**, heterogeneous budget **130** vs **175**.

The symmetric class model therefore overstated the minimum synthetic budget by **3 / 13 / 28 / 45** across the 2/3/4/5-epoch horizons. This is a model-tightening result, not a claim about measured real-world attack cost.

A gate-isolation test holds detection and publication equal while moving only verifier consumption from one to three epochs; stolen authorization remains verifier-usable for the full three epochs. A complementary test changes detection and publication while holding verifier consumption fixed and preserves the same verifier-visible window. Verifier consumption therefore remains the operative temporal security gate.

## Advancement: overlapping authority-group stress

V50 adds six heterogeneous candidate shared-control groups spanning cloud identity, HSM administration/custody, provider/build-CA control, local possession, and key custody. The optimizer evaluates all **63 non-empty combinations** with union-find canonicalization so overlaps are counted once rather than double-collapsed.

Every actual shared-control collapse is rejected. Each single candidate group reduces provenance from 22 to **21**, and the most aggressive combined overlap reaches provenance **16**. The accepted reference graph therefore continues to require independently auditable local/current factors; shared administrative naming or signed metadata cannot be treated as independence.

## Advancement: dual-log source replacement and key rotation

V50 extends the 513-statement RFC9162-style dual-log recovery model with source replacement and key epochs. Before verifier consumption of a rotation, epoch-1 sources remain usable. After the verifier consumes epoch 2, only epoch-2 sources with a valid rotation chain count.

The exact recovery tests show:

- concurrent loss of all old sources is accepted when each log has a valid epoch-2 replacement and checkpoint lag is <=64;
- an epoch-2 replacement without a valid rotation chain is rejected;
- loss of the entire source set for either log is rejected;
- replay of epoch-1 sources after the verifier consumed epoch 2 is rejected;
- replacement lag 33 is accepted;
- replacement lag 65 is rejected.

The carried Merkle checks remain valid at 513 statements: selected inclusion and consistency proofs verify; whole-log loss, split-log equivocation, missing recovery proofs, proof tampering, and lag 65 all fail closed. Frontier persistence remains storage-only and the carried trust-bearing message accounting remains `132 + 4*k`.

## Preserved constraints

The six V42/V49 common-control collapse tests remain rejected at provenance 21. Evidence infrastructure remains accepted only at cut 10 with independent statement-local evidence; common issuer-CA or common witness control is rejected even when the provenance route itself still counts 22. Unknown and cyclic provenance fail closed. V21 guarded routing remains unchanged; V50 does not claim a new runtime envelope.

## V51 frontier

1. Extend the heterogeneous temporal optimizer beyond five epochs with root-specific uncertainty intervals and adversarial observation censoring.
2. Replace collapse-only shared-control stress with explicit AND-of-local guard constructions and prove which guarded shared authorities can restore cut 22 without hidden common roots.
3. Model simultaneous dual-log key-rotation equivocation, witness-set churn, and monotonic verifier state under partial propagation.
4. Retain V21 routing unless a replacement independently clears the >=2,000-seed stationary/near-threshold acceptance bar and materially improves gradual/selective/correlated detection without extra probes.

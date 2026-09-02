# WinLoop Continuation — V127

**Status:** validated continuation from committed V126. V127 binds to V126 validation digest `c5aa4ba69b62e5ae1b1c541792f915cce1a13e6a47705f6f3c1ee7f56dd2f32e` and implementation SHA-256 `54260b049f90987b89bfa63e79aff4e4c0b731766e912e0d819f0f3fa345a8aa`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V127 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V126

V127 starts only from V126 states that were already fully bound. The validator binds the three static seed populations to the committed V126 validation result: **576** epoch-77 completion states (`131,281,920 / 227,920`), **27,648** bound fifty-first-restart recovery states (`5,804,255,232 / 209,934`), and **760** bound membership quorum-churn completion states (`150,848,600 / 198,485`). The V126 validation digest and implementation hash identify the exact committed predecessor used for those seeds.

## Epoch-78 anchor GC: twenty-fifth-source handoff

V127 begins only after V126's twenty-fourth-source lineage rotation, lineage binding, handed-proof rebind, and epoch-77 verifier completion are fully bound. Epoch 78 hands that rebound proof to a twenty-fifth source, binds the source, and only then permits the epoch-78 verifier binding to complete. Tombstone-root continuity, carried root binding, every prior source/key/lineage/proof/handoff binding, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **969,550,848** of **64,517,862,075,809,679,877,326,057,473,547,718,992,042,673,932,702,309,099,575,861,326,838,170,804,363,520,207,734,452,560,077,557,702,112,509,004,209,017,480,088,259,336,520,280,834,048** modeled states. It includes **831,043,584** twenty-fifth-source-handoff states, **692,536,320** bound handoffs, **554,029,056** source-binding states, **415,521,792** bound source bindings, **277,014,528** verifier-binding states, and **138,507,264** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting handoff/source/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **111** coordinates, producing **6,739,986,666,787,659,948,666,753,771,754,907,668,409,286,105,635,143,120,275,902,562,304** delay vectors and **240,464** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: successor disappearance and fifty-second verifier cold restart

V127 begins only from V126's fully bound fifty-first-restart recoveries. It requires successor-source disappearance, replacement-source binding, fresh dual-source reconciliation, and only then permits a fifty-second cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **58,199,107,478,561,872,029,878,091,566,402,634,882,358,591,076,941,614,750,567,995,811,648,784,658,595,840** states; exactly **67,460,152,320** admit, including **61,327,411,200** successor-source-disappearance states, **55,194,670,080** bound disappearance states, **49,061,928,960** replacement-source-binding states, **42,929,187,840** bound replacement bindings, **36,796,446,720** dual-source reconciliations, **30,663,705,600** bound reconciliations, **24,530,964,480** fifty-second-restart states, **18,398,223,360** bound restart states, and **6,132,741,120** fully bound fifty-second-restart recoveries. Cached fifty-second-restart authority, unbound disappearance/replacement/reconciliation/restart/consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: root-28 witness rebind

V127 begins only from V126's bound root-28 rollover quorum-churn completions. Membership generation 4 and root 28 remain fixed while the witness is rebound to root 28, the witness binding is renewed, and only then may replication-quorum churn complete. Tombstone continuity, replacement-source binding, and prior-source binding remain intact, and active Byzantine membership is rejected.

The modeled nominal state space is **277,495,476,388,456,779,380,342,345,682,871,084,546,854,515,171,752,106,158,811,642,303,632,070,965,985,280** states; exactly **1,116,848,880** admit, including **957,299,040** root-28-witness-rebind states, **797,749,200** bound rebinds, **638,199,360** witness-binding states, **478,649,520** bound witness bindings, **319,099,680** replication-quorum-churn states, and **159,549,840** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting witness rebind/binding/churn acceptance, generation or root regression, tombstone/replacement-source/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V128 frontier

V128 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 79 by rotating the twenty-fifth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline; compose fifty-second-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a fifty-third verifier cold restart without cached-authority promotion; and keep generation 4 after the root-28 witness rebind while replacing the witness source, rolling to root 29, binding root 29, and requiring replication-quorum churn without tombstone or prior-source discontinuity. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

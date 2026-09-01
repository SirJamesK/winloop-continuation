# WinLoop Continuation — V120

**Status:** validated continuation from committed V119. V120 binds to V119 validation digest `02eef35bac9f1b1ac5a23d34bda99f93447a517ed75677da0020af5d0497c32c` and implementation SHA-256 `7b45b652ddf936f2f1bce679aa8834337e398cf2369d8d2fd9033ae4b464f22d`, preserves V21 guarded routing, and keeps the carried admission baseline at joint 21 / provenance 22 / synthetic lower 63.

## Independence evidence remains fail closed

No committed independently validated provider/operator/hardware independence certificate is present in the canonical predecessor state, so V120 keeps cross-role credit at **12**. The executable certificate gate remains **150** certificate/anchor/relation states and admits only **4** hypothetical current-or-cached externally anchored disjoint states. Stale, conflicting, aliased, unknown-relation, or self-asserted authority does not increase cross-role credit.

## Exact continuation seeds from V119

V120 starts only from V119 states that were already fully bound. The validator binds the three static seed populations to the committed V119 validation result: **576** epoch-70 completion states (`87,607,296 / 152,096`), **27,648** bound forty-fourth-restart recovery states (`3,826,897,920 / 138,415`), and **760** bound membership quorum-churn completion states (`98,622,160 / 129,766`). The V119 validation digest and implementation hash identify the exact committed predecessor used for those seeds.

## Epoch-71 anchor GC: twenty-first-lineage rotation and handed-proof rebind

V120 begins only after V119's twenty-first-source handoff, twenty-first-source binding, and epoch-70 verifier completion are fully bound. Epoch 71 rotates the twenty-first-source lineage, binds that lineage, rebinds the handed proof, and only then permits the epoch-71 verifier binding to complete. Tombstone-root continuity, carried root binding, all prior source/key/lineage/proof/handoff bindings, and the original epoch-12 shared deadline remain fixed throughout the accepted chain.

The exact symbolic OR-of-AND optimizer admits **838,252,800** of **12,095,523,200,590,218,055,750,012,113,741,820,559,409,208,618,190,045,644,284,055,371,580,996,641,715,758,174,026,264,885,779,831,865,357,647,767,858,787,123,200** modeled states. It includes **745,113,600** twenty-first-lineage-rotation states, **651,974,400** bound rotations, **558,835,200** lineage-binding states, **465,696,000** bound lineage bindings, **372,556,800** handed-proof-rebind states, **279,417,600** bound handed-proof rebinds, **186,278,400** verifier-binding states, and **93,139,200** bound verifier-binding / epoch-completion states. Stale/conflicting root binding, unbound/conflicting rotation/lineage/proof/verifier or carried source/key/lineage/proof/handoff/provenance binding, tombstone-root discontinuity, deadline reset, and aggregate bad acceptance are all zero.

The temporal combinator extends to **97** coordinates, producing **25,108,406,941,546,723,055,343,157,692,830,665,664,409,421,777,856,138,051,584** delay vectors and **161,700** deadline vectors under `sum(vector) <= 3`; this increases exact validation coverage only and does not create authority or relax quorum.

## Publication recovery: replacement-source churn and forty-fifth verifier cold restart

V120 begins only from V119's fully bound forty-fourth-restart recoveries. It requires replacement-source churn, binds the successor source, re-establishes fresh dual-source reconciliation, and only then permits a forty-fifth cold verifier restart followed by bound reconciliation consumption at publication quorum. Cached verifier authority promotion remains forbidden.

The modeled nominal state space is **144,112,236,007,274,539,600,065,221,828,095,920,522,064,818,161,234,918,940,958,635,212,144,640** states; exactly **44,840,632,320** admit, including **40,764,211,200** replacement-source-churn states, **36,687,790,080** bound churn states, **32,611,368,960** successor-source-binding states, **28,534,947,840** bound successor bindings, **24,458,526,720** dual-source reconciliations, **20,382,105,600** bound reconciliations, **16,305,684,480** forty-fifth-restart states, **12,229,263,360** bound restart states, and **4,076,421,120** fully bound forty-fifth-restart recoveries. Cached forty-fifth-restart authority, unbound churn/successor/reconciliation/restart/consumption, below-publication-quorum acceptance, and aggregate bad acceptance are all zero.

## Membership recovery: witness-source replacement and root-25 rollover

V120 begins only from V119's bound root-24 witness-rebind quorum-churn completions. Membership generation 4 remains fixed while the witness source is replaced and bound, membership root 24 rolls to root 25, root 25 is bound, and only then may another replication-quorum churn complete. Tombstone continuity, witness binding, prior-source binding, and replication quorum remain intact, and active Byzantine membership is rejected.

The modeled nominal state space is **17,136,851,500,813,492,610,603,975,669,532,557,421,874,228,355,487,398,028,533,324,306,605,670,400** states; exactly **1,157,149,400** admit, including **1,051,954,000** witness-source-replacement states, **946,758,600** bound witness-source replacements, **841,563,200** replacement-source-binding states, **736,367,800** bound replacement-source bindings, **631,172,400** root-25-rollover states, **525,977,000** bound root-25 rollovers, **420,781,600** root-25-binding states, **315,586,200** bound root bindings, **210,390,800** replication-quorum-churn states, and **105,195,400** bound quorum-churn completions. Below-replication-quorum acceptance, unbound/conflicting replacement/source/root/churn acceptance, generation or root regression, tombstone/witness/prior-source discontinuity, active Byzantine membership, and aggregate bad acceptance are all zero.

## Preserved bounds

The V66-carried temporal regression remains horizon 22 floor **1 / synthetic budget 851**, with horizon 11 floor **2 / budget 398**. The 513-statement checkpoint recovery bound, maximum lag 64, frontier-only Merkle storage, unchanged trust-bearing paths, shared-audit accounting `132 + 4*k`, V21 guarded routing, and no-new-runtime-envelope claim remain unchanged.

## V121 frontier

V121 should continue requiring committed independently validated provider/operator/hardware evidence before any cross-role-credit increase; extend anchor GC through epoch 72 by handing the rebound proof to a twenty-second source, binding that source, and preserving the epoch-12 deadline; compose forty-fifth-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a forty-sixth verifier cold restart without cached-authority promotion; and keep generation 4 / root 25 fixed while rebinding and binding the witness to root 25 before replication-quorum churn, without tombstone or source-binding discontinuity. V21 routing remains active unless a replacement independently clears the >=2,000-seed bar with honest message accounting.

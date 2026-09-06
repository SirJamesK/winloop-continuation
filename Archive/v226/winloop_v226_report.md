# WinLoop V226 validation report

## Verified result

V226 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-177 GC to 25,989,050,880 states with 20,213,706,240 bound seventy-fourth-lineage rotations, 14,438,361,600 bound lineage bindings, 8,663,016,960 bound handed-proof rebinds, and 2,887,672,320 bound verifier completions; admits 1,480,992,049,152 publication states with 134,635,640,832 fully bound one-hundred-fifty-first-cold-restart recoveries; and admits 39,922,218,600 membership states with 32,663,633,400 bound witness-source replacements, 18,146,463,000 bound root-78 rollovers, 10,887,877,800 bound root-78 bindings, and 3,629,292,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `28ba0ac5011094061962ae84c33557e5fdcf50f57e50434b171df865d853a593`.

## Predecessor binding

V226 continues from committed V225 on `main`: V225 digest `35d53f4b0c77714b37b84dec8d148cbeb9fc8f27ee587dcfd1b458f1f97e56eb`, implementation SHA-256 `a0713101dd488665b6a7f6d90413a6066084a2512198ef822db6cb76e69f1daf`, validator SHA-256 `ad9be40b61c2b517af1aff2831194caf3f372ebb8ef3db461e2e3b988262eca4`. V226 implementation SHA-256 is `680e5d510e2fbe06505e0a60f1ba80967e99c49b4f1460c656bdaa56461b679c` and standalone validator SHA-256 is `a686588c6cebcbb4c7a09a1a337500358f24552b25e9e422485092e584304bcd`.

Seed transitions are exact from V225: 576 epoch-176 completions (`2,832,318,720 / 4,917,220`), 27,648 restart recoveries (`132,029,844,480 / 4,775,385`), and 760 quorum-churn completions (`3,558,593,600 / 4,682,360`).

## Continuation gates

Epoch 177 rotates the seventy-fourth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 151 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-fifty-first cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-77 witness rebind, rolls to root 78, binds root 78, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v226_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V227

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a seventy-fifth source in epoch 178, bind that source, and preserve the epoch-12 deadline; compose publication-151 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-fifty-second cold restart without cached-authority promotion; rebind the witness to root 78 after the root-78 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.

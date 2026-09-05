# WinLoop V204 validation report

## Verified result

V204 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-155 GC to 16,445,286,144 states with 12,790,778,112 bound sixty-third-lineage rotations, 9,136,270,080 bound lineage bindings, 5,481,762,048 bound handed-proof rebinds, and 1,827,254,016 bound verifier completions; admits 932,632,842,240 publication states with 84,784,803,840 fully bound one-hundred-twenty-ninth-cold-restart recoveries; and admits 25,058,355,960 membership states with 20,502,291,240 bound witness-source replacements, 11,390,161,800 bound root-67 rollovers, 6,834,097,080 bound root-67 bindings, and 2,278,032,360 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `0e6109cdd8cf63f2f75e25c996416750792ce26749266c55f17c1b46267beaa4`.

## Predecessor binding

V204 continues from committed V203 on `main`: V203 digest `169ac3385a0f85e7c9c4c6d708ee64f3a37cd3bd1c9e4d1aa5938aebb0e411bc`, implementation SHA-256 `8cfb26e9ef240e8a3e20f6546d3cb8715a54cd78bc0b1e2bbf6efc7a82739fb4`, validator SHA-256 `2c461edbad2f2e12f2970981731d745d8a1fbada1536f3ad746653d645f9803a`. V204 implementation SHA-256 is `1905abfdd9ce4f9ba6e34f0fcb87777a230455a6d34e1466cd4c10b65b0d460d` and standalone validator SHA-256 is `97e6f60a3085922446cc10497e517e2434655297c76f5ed5a415c987341fcbe2`.

Seed transitions are exact from V203: 576 epoch-154 completions (`1,786,498,560 / 3,101,560`), 27,648 restart recoveries (`82,872,419,328 / 2,997,411`), and 760 quorum-churn completions (`2,226,260,400 / 2,929,290`).

## Continuation gates

Epoch 155 rotates the sixty-third-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 129 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-twenty-ninth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-66 witness rebind, rolls to root 67, binds root 67, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v204_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V205

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a sixty-fourth source in epoch 156, bind that source, and preserve the epoch-12 deadline; compose publication-129 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-thirtieth cold restart without cached-authority promotion; rebind the witness to root 67 after the root-67 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.

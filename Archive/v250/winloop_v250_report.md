# WinLoop V250 validation report

## Verified result

V250 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-201 GC to 39,975,482,880 states with 31,092,042,240 bound eighty-sixth-lineage rotations, 22,208,601,600 bound lineage bindings, 13,325,160,960 bound handed-proof rebinds, and 4,441,720,320 bound verifier completions; admits 2,286,923,950,080 publication states with 207,902,177,280 fully bound one-hundred-seventy-fifth-cold-restart recoveries; and admits 61,810,370,600 membership states with 50,572,121,400 bound witness-source replacements, 28,095,623,000 bound root-90 rollovers, 16,857,373,800 bound root-90 bindings, and 5,619,124,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `d23b85e71f6792aa0fa159af5cd5c76170beff3f2d50dc8dce8ed662336c1b95`.

## Predecessor binding

V250 continues from committed V249 on `main`: V249 digest `8cf21664fe3ffffbd48f0a71a6d92f7c5b87a48a3fddaef99107399fd52632bc`, implementation SHA-256 `36e7e10f5b7157496c633e8c5dfea9fa5b73e59674ee79c8b84c002e12e2242a`, validator SHA-256 `389cd01713e3efe16e2ae22df11fcac5a7be81b22b003e2ce4be75f2569c2f14`. V250 implementation SHA-256 is `f61d8efcf9d68136b056aaa4f38457b2b5321a268d6562fcead98a235cdad58b` and standalone validator SHA-256 is `dea3d48f1e739e9175ae1c0cb85d459907146567d6e37c06529a88908f899602`.

Seed transitions are exact from V249: 576 epoch-201 completions (`4,367,897,856 / 7,583,156`), 27,648 restart recoveries (`204,417,838,080 / 7,393,585`), and 760 quorum-churn completions (`5,524,421,760 / 7,268,976`).

## Continuation gates

Epoch 201 rotates the eighty-sixth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 175 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-fifth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-89 witness rebind, replaces the witness source, rolls to root 90, binds root 90, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v250_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V251

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eighty-seventh source in epoch 202, bind that source, and preserve the epoch-12 deadline; compose publication-175 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-sixth cold restart without cached-authority promotion; keep generation 4 after the root-90 rollover, rebind the witness to root 90, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.

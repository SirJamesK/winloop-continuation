# WinLoop V246 validation report

## Verified result

V246 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-197 GC to 37,362,124,800 states with 29,059,430,400 bound eighty-fourth-lineage rotations, 20,756,736,000 bound lineage bindings, 12,454,041,600 bound handed-proof rebinds, and 4,151,347,200 bound verifier completions; admits 2,136,187,164,672 publication states with 194,198,833,152 fully bound one-hundred-seventy-first-cold-restart recoveries; and admits 57,713,803,400 membership states with 47,220,384,600 bound witness-source replacements, 26,233,547,000 bound root-88 rollovers, 15,740,128,200 bound root-88 bindings, and 5,246,709,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `1e84da39dd605279a3b8a3aa354da47a6e1c0f9104d3c4ed61162b0c27bfc526`.

## Predecessor binding

V246 continues from committed V245 on `main`: V245 digest `59f194517a3f39aacf941ffeec5de7c24c9e589e45906a9d352bb0b63143ca07`, implementation SHA-256 `33ac05919ba1de4cb871ca7885a49108e4959262958b734d68bbc03aceaee519`, validator SHA-256 `00e7503fbdab7d9c481b6be548b41c70e8bf8bb512a0071d99e91b9294749f14`. V246 implementation SHA-256 is `8a67a9d7812a4063663251db86c46c04b6850406e3d848b2d3555d0cbe817f8e` and standalone validator SHA-256 is `c875bff76850ea0a8aa1a0ac9c352c96c1cf76eaef9ab90c9b868e226374eec9`.

Seed transitions are exact from V245: 576 epoch-197 completions (`4,080,787,200 / 7,084,700`), 27,648 restart recoveries (`190,869,765,120 / 6,903,565`), and 760 quorum-churn completions (`5,156,250,400 / 6,784,540`).

## Continuation gates

Epoch 197 rotates the eighty-fourth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 171 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-first cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-87 witness rebind, replaces the witness source, rolls to root 88, binds root 88, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v246_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V247

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eighty-fifth source in epoch 198, bind that source, and preserve the epoch-12 deadline; compose publication-171 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-second cold restart without cached-authority promotion; keep generation 4 after the root-88 rollover, rebind the witness to root 88, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.

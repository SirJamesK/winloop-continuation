# WinLoop Continuation Agent

This repository is the canonical state for the scheduled WinLoop continuation agent.

## Bootstrap

For every run:

1. Read `SCHEDULED_TASK_PROMPT.md` and `GITHUB_POLICY.md` from `main`.
2. List `Archive/`, identify the highest numeric `vNN`, and inspect that version's implementation, validation, report, validator, and manifest.
3. Continue from the unresolved frontier documented in that latest committed version.
4. Produce and validate exactly one next version under `Archive/v(NN+1)/`.
5. Commit directly to `main` only after validation succeeds.
6. Re-read the committed state and report the resulting commit SHA.

## Hard invariants

- Repository: only `SirJamesK/winloop-continuation`.
- Branch: only the default branch when it is `main` or `master`; current branch is `main`.
- No PRs and no auxiliary branches.
- No persistence of WinLoop artifacts to ChatGPT Library/conversation files/files folder.
- GitHub is the durable source of truth.
- Earlier `Archive/vNN/` directories are immutable history.
- Unknown/stale/conflicting provenance fails closed.
- Never report a version as complete without exact validation and successful GitHub publication.

## Output discipline

The GitHub archive contains the full implementation and technical report. The scheduled ChatGPT response contains only the version, headline finding, commit SHA/blocker, and archive path.

The scheduler cannot force a fresh top-level ChatGPT conversation for every recurrence; do not claim otherwise. Version separation is provided by `Archive/vNN/` and commit history.

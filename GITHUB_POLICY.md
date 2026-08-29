# GitHub policy for WinLoop Continuation

Target repository: `SirJamesK/winloop-continuation`

## Branch policy

- Use **only** the repository default branch when it is `main` or `master`.
- Current canonical branch: **`main`**.
- Do not create feature branches, release branches, or pull requests for scheduled continuation work.
- Do not write to any other repository if this target repo is missing or inaccessible.

## Persistence policy

- GitHub is the durable source of truth.
- WinLoop version artifacts must **not** be persisted to ChatGPT Library, conversation files, or a ChatGPT files folder.
- Transient execution scratch is permitted only when needed for validation; it is not canonical state.
- Historical artifacts are immutable under `Archive/vNN/`.
- Each successful scheduled run creates exactly one next version directory under `Archive/` and commits the validated artifact set there.
- Root files are project-control metadata only; do not duplicate large version artifacts at repository root.

## Authentication

- Use the connected GitHub App for repository access and writes.
- Access persists while the GitHub App installation remains authorized for `SirJamesK/winloop-continuation`.
- If repository access or write authorization fails, the agent must fail closed and report the blocker rather than falling back to another repository.

## Scheduled output

- Scheduled ChatGPT output should be concise: version, verified headline, commit SHA or blocker, and `Archive/vNN/` path.
- GitHub version directories, not separate ChatGPT conversations, are the authoritative per-version record.

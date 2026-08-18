# GitHub policy for WinLoop Continuation

Target repository: `SirJamesK/winloop-continuation`

- Use **only** the repository default branch when it is `main` or `master`.
- Prefer `main` for a newly created repository.
- Do not create feature branches or pull requests for scheduled continuation work.
- Do not write to any other repository if the target repo is missing or inaccessible.
- Each scheduled run should update latest artifacts and append a timestamped run note under `runs/`.
- GitHub App authentication is used; access persists while the GitHub App installation remains authorized for the repository.

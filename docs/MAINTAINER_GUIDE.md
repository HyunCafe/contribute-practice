# Maintainer guide

This is a low-friction teaching repository: the goal is for beginners to complete a first meaningful pull request using Git Bash while keeping the exercise as small as a single Markdown edit.

## Maintenance principles

1. Preserve every historical contributor entry, personal goal, and associated link unless its author requests a correction or removal, or moderation requires it.
2. Keep the **contributor list** in `contributing.md`. Don't duplicate entries in `README.md`. Sorting is by the exact GitHub handle in the profile link, ignoring case, character by character.
3. Use `.github/CONTRIBUTING.md` for the onboarding rules GitHub links to in the repository UI.
4. Keep default first contributions small: one Markdown entry, no executable code, no new dependencies.
5. Review submissions for spam, suspicious URLs, impersonation, leaked secrets, and changes to unrelated entries. Do not run code from untrusted contributions.
6. Explain requested changes kindly and briefly; contributors are here to learn.
7. If the project is temporarily not accepting PRs, say so prominently in the README and update repository settings accordingly.

## Reviewing a first-contribution PR

- Confirm the PR targets the intended repository/branch.
- Check the **Files changed** tab: usually only `contributing.md`.
- Verify that the profile link is plausible and uses HTTPS (do not require the maintainer to click unknown external links).
- Ensure the entry has a short goal, the two-line Markdown format, and case-insensitive alphabetical placement by GitHub username.
- To audit after large reorganizations, use the optional no-dependency `tools/check_contributors.py` script (maintainer utility; first-time contributors do not need Python).
- Avoid requesting unnecessary revisions for purely cosmetic variations.
- Merge when ready or explain why the change is deferred.

## Spam and privacy

Never ask contributors for passwords, 2FA codes, account access, payment details, or identity documents. A public GitHub username is sufficient for the exercise. A PR containing exposed credentials should be handled carefully: simply deleting them in a subsequent commit does not guarantee they disappear from history.

## Repository change policy

For larger updates, use a separate branch and a pull request so the teaching materials can be reviewed. Keep archives of old documentation if restructuring contributor records; don't force-push or delete contributors' history.

## References

- [GitHub contribution guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [GitHub pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [GitHub first contributions](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

## Contributor examples and presentation

When instructions use placeholders such as `YOUR_USERNAME`, show an understandable completed example alongside them. The README and contribution guide use `@HyunCafe` as a **clearly labeled illustrative contributor entry**; never imply its sample goal is the maintainer's real goal or that it has been added to the wall. For clone/remote examples, `HyunCafe` identifies the **original repository owner**, not a newcomer's fork. Always tell contributors to use their own handle for push access.

Keep the original GIFs and screenshots in `assests/` (historical directory spelling). See [visual guidelines](VISUAL_STYLE.md). Screenshots can become dated, so always provide written instructions and label differences such as SSH versus HTTPS.

## Automatic contributor checks

The GitHub Actions workflow reads `contributing.md` from incoming PRs but runs the checker from the **trusted base commit**. It does not run contributor-supplied Python code or install dependencies. The workflow has read-only permissions and checks sorting, links, duplicate handles, goals and preservation of existing entries.

For a maintainer test: `python -m unittest discover -s tests -v` then `python tools/check_contributors.py`. Review PRs manually even when checks pass; software validation is not a substitute for checking content and intent.

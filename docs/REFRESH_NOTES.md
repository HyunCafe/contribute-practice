# 2026 documentation and design refresh

## Overview

Modernize this first-contribution tutorial for beginners, retaining its public contribution history while improving clarity, presentation, accessibility, and alphabetical consistency.

## What's changed

- The README is now a clean landing page with Git Bash as the primary hands-on workflow: fork, clone, branch, edit, commit, push, PR.
- The contributor wall is the single authoritative directory; no duplicate list in README.
- Historical contributors are sorted **by the actual GitHub username in their profile URL**, case-insensitively from the first letter to the last.
- Display names remain visible even when they differ from the username. Digit-prefixed usernames use a separate section.
- Consistent Markdown formatting for each entry; original goal wording is retained.
- Empty letter sections are omitted for easier navigation. A new contributor can create a missing section.
- New `.github/CONTRIBUTING.md` and simplified PR/issue templates teach the exact two-line format.
- Added a glossary, troubleshooting, maintainer notes, and optional Python standard-library validator.
- Original files are archived and their contents compared to protect historical entries.

## Preservation rules

- Preserve old names, links, original learning-goal text, and PR history.
- Do not silently deduplicate entries, rewrite someone else's goals, delete old assets, or change the license/code of conduct.
- Merge any missing README-only contributor entries only when they can be parsed reliably.
- Keep archives and record discrepancies that need manual review.

## Notes for maintainers

- Review `docs/CONTRIBUTOR_AUDIT.md` generated at apply time.
- Check a pending PR against the new sorted list before merging to avoid conflicts.
- Newcomers need Git for Windows / Git Bash, a GitHub account, and a text editor. No Python, Node.js, SSH, or project build dependencies are required for a first contribution.
- A standard entry only changes `contributing.md`.

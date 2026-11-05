# Contribution guidelines

Welcome! This is a **Git Bash-first, documentation-only** exercise for learning how to contribute to open source. You do **not** need programming experience, Python, or a package manager.

## Your first PR

1. [Fork this repository](https://github.com/HyunCafe/contribute-practice/fork) on GitHub.
2. **Clone your own fork** into Git Bash using HTTPS and create a new branch.
3. Edit **only `contributing.md`** to add your GitHub profile and a short learning goal.
4. Review the diff, stage that one file, **make one commit**, and push your branch.
5. Open a pull request against `HyunCafe/contribute-practice:main`.

Follow the [step-by-step Git Bash tutorial](../README.md#your-first-contribution-step-by-step) for the complete commands and screenshots-independent instructions.

## Entry format

Use the following **two-line Markdown format**:

```md
- **ExampleUser** ([`@ExampleUser`](https://github.com/ExampleUser))
  > "My goal is to learn how to collaborate on open source."
```

Replace the handle, URL, and goal with your own values. You may use a different display name, but the `@handle` from your profile URL determines where the entry goes. A date is optional; do not rewrite old years or personal goals.

### Alphabetical-order rules

- Sort by **actual GitHub username**, not display name, case-insensitively (A–Z).
- Compare the full username **one character at a time**, from first to second to third and beyond. Example: `anna`, `anne`, `anton`.
- Use the corresponding `## A`–`## Z` section, creating a missing section in sequence if necessary.
- Place digit-prefixed usernames in `## 0–9 and symbols` at the end.
- **Do not reorganize anyone else's entry** in your first PR. If you notice a mistake, open a separate issue.
- Don't add a second entry for the same handle; ask for help updating yours if needed.

## First contribution checklist

- [ ] I used **Git Bash** and created a branch in my fork.
- [ ] I changed **only `contributing.md`**.
- [ ] I included my real GitHub profile URL and a short, public-safe learning goal.
- [ ] I placed my entry in the correct case-insensitive username order.
- [ ] I ran `git diff --check` and inspected the diff.
- [ ] I made one commit, pushed my branch, and opened a PR targeting `HyunCafe/contribute-practice:main`.
- [ ] I preserved existing contributor records and included no private credentials.

## Other improvements

Documentation fixes and accessibility improvements are welcome in **separate, focused PRs**. For substantial changes, open an [issue](https://github.com/HyunCafe/contribute-practice/issues) first to discuss the approach.

We follow the [Code of Conduct](../CODE_OF_CONDUCT.md). The maintainer may request changes or defer merging; a submitted PR is a real learning experience even if it is not immediately merged.

**Safety:** Never share passwords, personal access tokens, recovery codes, SSH private keys, or private personal information in a PR, commit, screenshot, or issue. Do not run unfamiliar scripts to complete this exercise.

Need help? See [Git Bash troubleshooting](../docs/TROUBLESHOOTING.md) or open an issue with sensitive details removed.

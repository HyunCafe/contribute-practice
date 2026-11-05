# Contribution guidelines

Welcome! This little practice repository is here to help you try the real Git and GitHub workflow. You'll use **Git Bash** for commands and **VS Code** to edit one Markdown file. You don't need programming experience or extra packages.

## Your first PR

1. [Fork this repository](https://github.com/HyunCafe/contribute-practice/fork) on GitHub.
2. **Clone your own fork** using Git Bash (HTTPS), open it in VS Code with `code .`, and create a branch.
3. Edit **only `contributing.md`** to add your GitHub profile and a short learning goal.
4. Review the diff, stage that one file, **make one commit**, and push your branch.
5. Open a pull request against `HyunCafe/contribute-practice:main`.

Follow the [step-by-step walkthrough](../README.md#your-first-contribution-step-by-step) for the commands, VS Code steps, and screenshots.

## Entry format

Use this two-line format, then compare it with a complete sample entry.

**Template — replace the placeholders:**

```md
- **YOUR_DISPLAY_NAME** ([`@YOUR_USERNAME`](https://github.com/YOUR_USERNAME))
  > "YOUR_LEARNING_GOAL"
```

**Completed example — using `HyunCafe` as the sample username:**

```md
- **HyunCafe** ([`@HyunCafe`](https://github.com/HyunCafe))
  > "My goal is to practice Git, make a small change, and open a pull request."
```

**What GitHub displays:**

- **HyunCafe** ([`@HyunCafe`](https://github.com/HyunCafe))
  > "My goal is to practice Git, make a small change, and open a pull request."

This example demonstrates the format using the project owner's username. The learning goal is illustrative, not a claim about the maintainer. **Don't copy the example**—add your own information instead.

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

<div align="center">

# Your First Open-Source Contribution

**Learn Git and GitHub by making one real pull request.**

A guided, beginner-friendly practice project. No programming experience needed—just Git Bash, a GitHub account, and one Markdown edit.

**[Start the Git Bash walkthrough](#your-first-contribution-step-by-step)** · [Contributor wall](contributing.md) · [Contribution rules](.github/CONTRIBUTING.md) · [Troubleshooting](docs/TROUBLESHOOTING.md)

</div>

---

## Welcome

This repository exists to teach the skills behind open-source collaboration: **fork → clone → branch → edit → commit → push → pull request**.

You'll introduce yourself on our contributor wall and share a learning goal. That is a real, small documentation contribution. The purpose is to practice **Git Bash and GitHub**, not to write code.

> **Your first challenge:** Change **one file** (`contributing.md`), create **one commit**, and open **one pull request**. There is no need to edit the README or install a build system.

## The journey

```text
GitHub website                 Your computer (Git Bash)                  GitHub website
┌──────────────────┐           ┌────────────────────────────┐           ┌─────────────────────┐
│ Fork the project │ ────────► │ Clone your fork            │           │                     │
└──────────────────┘           │ Create your branch         │           │                     │
                               │ Edit contributing.md only  │           │                     │
                               │ Review → Commit → Push     │ ────────► │ Open pull request   │
                               └────────────────────────────┘           │ Get feedback        │
                                                                        └─────────────────────┘
```

| Term | What it means |
| --- | --- |
| **Fork** | Your personal copy of this GitHub repository. |
| **Clone** | Download your fork with Git history to your computer. |
| **Branch** | A safe place to work on your edit without changing `main`. |
| **Commit** | Record your change in local Git history. |
| **Push** | Send your branch and commit to your fork on GitHub. |
| **Pull request (PR)** | Ask the original repository to review and merge your contribution. |

More definitions are in the [glossary](docs/GLOSSARY.md).

## Before you begin

You will need:

1. A [GitHub account](https://github.com/signup) that you can sign in to.
2. **Git for Windows**, from the [official Git website](https://git-scm.com/downloads/win). It includes **Git Bash**. If you already use Git Bash, you can skip installation.
3. Any text editor. **Windows Notepad** is enough for this exercise.

Open **Git Bash** and verify Git is installed:

```bash
git --version
```

**Commit identity:** Git might ask for your name/email when you make your first commit. For privacy, consider using your [GitHub no-reply email address](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address). Don't copy another person's identity.

## Your first contribution: step by step

### 1. Fork this repository on GitHub

1. Sign in to GitHub and open **[HyunCafe/contribute-practice](https://github.com/HyunCafe/contribute-practice)**.
2. Select **Fork** → **Create fork**.
3. Confirm the address now starts with `https://github.com/YOUR_USERNAME/contribute-practice` where `YOUR_USERNAME` is **your own** GitHub username.

> You need write access to your fork. You do not need write access to the original repository.

### 2. Clone **your fork** using Git Bash

Open Git Bash in a folder where you'd like to keep your practice project (your home directory is fine).

Replace `YOUR_USERNAME` with your real GitHub username **before running the command**:

```bash
git clone https://github.com/YOUR_USERNAME/contribute-practice.git
cd contribute-practice
```

**Check that you cloned the right repository:**

```bash
git remote -v
```

Both `origin` URLs should refer to **your fork**. Do not clone `HyunCafe/contribute-practice` when you intend to push to your own fork.

> `git clone` creates the project folder itself. If you see `destination path ... already exists`, see [troubleshooting](docs/TROUBLESHOOTING.md) rather than deleting a folder.

### 3. Create a branch for your change

```bash
git switch -c add-my-first-contribution
```

This creates and switches to a separate branch. Your local `main` stays unchanged.

### 4. Edit **only** `contributing.md`

If you're using Git Bash on Windows, open the file in Notepad:

```bash
notepad.exe contributing.md
```

Find the letter matching **the first character of your GitHub username**, not your display name. Insert your entry in case-insensitive alphabetical order: compare the first character, then the second, third, and so on. If a letter section is missing, create it in the proper position. Handles starting with digits belong in `## 0–9 and symbols` at the end.

Use this **two-line Markdown format**, replacing the example handle, profile URL, and goal with your own information:

```md
- **ExampleUser** ([`@ExampleUser`](https://github.com/ExampleUser))
  > "My goal is to learn how to contribute to open source."
```

For example, `@anna` comes before `@anne`, and `@anne` comes before `@anton`. Your display name can be different from your `@handle`; the **handle in your profile link** determines the order.

**Keep your edit limited to your entry.** Don't edit `README.md`, rewrite anyone else's goal, or reorganize existing records in your first PR. The contributor list is public, so don't include private contact information or passwords.

Save the file in Notepad when done.

### 5. Review the change before committing

Return to Git Bash:

```bash
git status --short
git diff -- contributing.md
git diff --check
```

You should see **only `contributing.md` changed**. Check your spelling, GitHub profile URL, Markdown formatting, and alphabetical placement. If other files changed, investigate before staging or committing.

### 6. Make **one commit**

Stage **only the contributor file**, review the staged change, and commit it:

```bash
git add contributing.md
git diff --cached --name-only
git diff --cached --check
git commit -m "docs: add my contributor profile"
```

The staged-file list should contain only `contributing.md`. If Git asks you to configure your author identity, see [troubleshooting](docs/TROUBLESHOOTING.md#git-doesnt-know-who-i-am).

### 7. Push your branch to your fork

```bash
git push -u origin HEAD
```

If a sign-in window opens, use the official GitHub authentication flow. **GitHub account passwords are not used for Git over HTTPS.** Never paste a token or a two-factor code into a GitHub issue or public PR comment.

### 8. Open your pull request

1. Open **your fork** on GitHub and look for **Compare & pull request**. Alternatively select **Pull requests → New pull request**.
2. Confirm the **base** is `HyunCafe/contribute-practice` on `main` and the **head** is your fork's new branch.
3. Confirm the **Files changed** tab shows **only `contributing.md`**.
4. Give the PR a clear title, such as `docs: add YOUR_USERNAME to contributors`.
5. Briefly describe what you learned, then click **Create pull request**.

**That's the complete exercise: one file → one commit → one PR.** Your request may remain open while a maintainer reviews it. Watch for comments and follow up if changes are requested.

## Our contributor wall

Meet the [community contributors and their learning goals](contributing.md). New names are sorted by **GitHub username**, case-insensitively and character-by-character. Older goals and years are part of this project's history and should not be rewritten.

The wall is maintained in **`contributing.md` alone**. The README contains instructions, not a second contributor list.

## Frequently asked questions

**Do I need to know programming?** No. Your first PR is a small Markdown edit.

**Do I need Python, Node.js, SSH keys, or build tools?** No. Git Bash, GitHub, and a text editor are enough. HTTPS is the default in this tutorial; SSH is optional for experienced users.

**Why use a branch?** It lets you propose an isolated change that the maintainer can review safely.

**Can I edit more than one file?** For this beginner exercise, change only `contributing.md`. Larger documentation fixes are welcome as separate, focused PRs—open an issue first to discuss them.

**Why hasn't my PR merged yet?** Reviews depend on maintainer availability. Creating a correct PR and participating in review are the learning goals; merging is not guaranteed.

## Help and further learning

- [Contribution rules and entry format](.github/CONTRIBUTING.md)
- [Common Git Bash and GitHub problems](docs/TROUBLESHOOTING.md)
- [Plain-language Git glossary](docs/GLOSSARY.md)
- [Community code of conduct](CODE_OF_CONDUCT.md)
- [Maintainer guide](docs/MAINTAINER_GUIDE.md)
- [MIT license](LICENSE)

**Learn more:** [GitHub: Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) · [Git: Getting started](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) · [Pro Git (free book)](https://git-scm.com/book/en/v2)

---

Made and maintained by [HyunCafe](https://github.com/HyunCafe), with thanks to everyone who has practiced their first open-source contribution here.

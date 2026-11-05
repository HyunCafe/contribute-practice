# Troubleshooting your first Git Bash contribution

These instructions assume you forked `HyunCafe/contribute-practice`, cloned **your fork**, and created a feature branch. If something fails, stop at that step. Don't delete folders or force-push just to get past an error.

## Git Bash isn't installed or `git` is not found

Install **Git for Windows** from the [official download page](https://git-scm.com/downloads/win). Reopen Git Bash and check:

```bash
git --version
```

## I cloned the original repository, not my fork

Check your remote:

```bash
git remote -v
```

The URL named `origin` should be `https://github.com/YOUR_USERNAME/contribute-practice.git`, where `YOUR_USERNAME` is **your own** GitHub handle.

**Real output example — the original project (not your fork):** If you see this, you cloned the maintainer's repository:

```text
origin  https://github.com/HyunCafe/contribute-practice.git (fetch)
origin  https://github.com/HyunCafe/contribute-practice.git (push)
```

That is a complete, real URL, but **it is the wrong remote for a new contributor's fork**. Your `origin` should say `YOUR_USERNAME` with **your own** handle substituted. If it shows `HyunCafe`, stop and ask for help before pushing.

## `fatal: destination path 'contribute-practice' already exists`

A directory with that name is already present. **Do not delete it** to make the command succeed. Inspect the existing folder, or clone your fork to a distinct new directory:

```bash
git clone https://github.com/YOUR_USERNAME/contribute-practice.git my-contribution-practice
cd my-contribution-practice
```

Replace `YOUR_USERNAME` with your own handle before running. Compare it with the original project's URL, `https://github.com/HyunCafe/contribute-practice.git`: your clone URL should have **your own account name instead of `HyunCafe`**.

## Git doesn't know who I am

Git requires a commit author name and email. You can configure them **for this repository only** (substitute your own values):

```bash
git config user.name "YOUR NAME"
git config user.email "YOUR_GITHUB_NOREPLY_EMAIL"
```

**Filled-in name example:** The project owner could use `git config user.name "HyunCafe"`. **You should set your own name**, not the owner's. For the email, copy the exact no-reply address from [your own GitHub email settings](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)—it differs between users. Never paste a password into these commands.

## The branch already exists

Check the current branch using `git branch --show-current`. Choose a different descriptive branch name with `git switch -c add-my-first-contribution-2` rather than resetting or deleting existing work.

## Git says `nothing to commit`

Confirm you saved `contributing.md` in the cloned project, then run:

```bash
git status --short
git diff -- contributing.md
```

You may have edited a different copy of the file, or already committed your change.

## `git diff --check` reports whitespace errors

Review the affected lines in your editor and remove trailing spaces. Re-run `git diff --check` before staging and committing. Don't overwrite unrelated contributor records.

## My commit contains other files

Before you commit, inspect `git diff --cached --name-only`. In this exercise it should show **only** `contributing.md`. If it doesn't, stop and ask for help; don't blindly run `git add .`.

## GitHub refuses the password or push (401 / 403)

GitHub does **not** accept account passwords for HTTPS Git operations. Git for Windows usually includes Git Credential Manager, which can open GitHub's browser sign-in flow. Confirm you are signed into your own fork and check `git remote -v`. Do not paste authentication tokens into a command, commit, public message, or issue. See [GitHub's authentication guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).

## My pull request includes unrelated files or commits

Check the **base** repository and **head** branch in GitHub's comparison page. The intended base is `HyunCafe/contribute-practice:main`; the head is the new branch in your fork. If unexpected changes appear, pause and ask for help rather than force-pushing.

## My pull request has merge conflicts

Someone may have edited the same contributor section. Ask for help in the PR. Don't overwrite others' entries or force-push just to bypass a conflict.

## My pull request hasn't been merged

This project is reviewed by a maintainer. A delay is not necessarily an error; wait for feedback and avoid opening duplicate PRs.

## GitHub looks different from the tutorial

The names and placement of controls can change. Look for **Fork**, **Compare & pull request**, **Files changed**, and **Create pull request**. Refer to the [official GitHub contribution guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project).

## The contributor check has a red X

Open your PR and choose **Details** beside the failed check. The message should say what needs fixing and which line to check. Common problems are a username in the wrong letter section, a missing learning goal or a duplicate profile.

In VS Code, fix `contributing.md`, press **Ctrl+S**, and then run this in Git Bash:

```bash
git diff -- contributing.md
git add contributing.md
git commit -m "docs: fix my contributor entry"
git push
```

**Example outcome:** The same pull request updates with your fix. You don't need to open a second PR or install Python. If GitHub says the check is waiting for approval, a maintainer may need to authorize the first-time contributor workflow.

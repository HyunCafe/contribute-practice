#!/usr/bin/env python3
"""Check the public contributor wall without modifying it.

Requires only Python's standard library. Maintainers can run it locally;
first-time contributors do not need Python because GitHub runs the check.

    python tools/check_contributors.py
    python tools/check_contributors.py --file path/to/contributing.md
    python tools/check_contributors.py --file proposed.md --baseline original.md
"""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

DEFAULT_FILE = Path(__file__).resolve().parent.parent / "contributing.md"
SECTION = re.compile(r"## ([A-Z])|## 0–9 and symbols")
ENTRY = re.compile(
    r"- \*\*(?P<display>.+?)\*\* "
    r"\(\[`@(?P<handle>[A-Za-z0-9-]+)`\]"
    r"\((?P<url>https://github\.com/[A-Za-z0-9-]+(?:/[^)]*)?)\)\)"
)
PROFILE = re.compile(r"https://github\.com/(?P<owner>[A-Za-z0-9-]+)(?P<extra>/.*)?")

# One original contributor linked to a repository instead of their profile.
# Leave that historical link untouched; require direct profile links for new entries.
HISTORICAL_LINKS = {"suyashsahu00": "https://github.com/suyashsahu00/CODING"}


def check_text(content: str) -> tuple[int, list[tuple[int, str]], list[tuple[int, str]]]:
    """Return (entry count, errors, notices), without changing any text."""
    lines = content.splitlines()
    errors: list[tuple[int, str]] = []
    notices: list[tuple[int, str]] = []
    section: str | None = None
    previous_section_rank = -1
    previous_handle: str | None = None
    seen: set[str] = set()
    count = 0
    current_goal_found = True
    current_entry_line = 0

    for number, line in enumerate(lines, start=1):
        match_section = SECTION.fullmatch(line)
        if match_section:
            if not current_goal_found:
                errors.append((current_entry_line, "Add a learning goal on the next line, starting with `  > `."))
            section = match_section.group(1) or "0-9"
            section_rank = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(section) if section != "0-9" else 26
            if section_rank <= previous_section_rank:
                errors.append((number, f"Section {section} is repeated or out of alphabetical order."))
            previous_section_rank = section_rank
            previous_handle = None
            current_goal_found = True
            continue

        match_entry = ENTRY.fullmatch(line)
        if match_entry:
            if not current_goal_found:
                errors.append((current_entry_line, "Add a learning goal on the next line, starting with `  > `."))
            handle = match_entry.group("handle")
            url = match_entry.group("url")
            key = handle.casefold()
            wanted = handle[0].upper() if handle[0].isalpha() else "0-9"
            if wanted != section:
                errors.append((number, f"@{handle} belongs in section {wanted}, not {section or 'outside the A–Z list'}."))
            if previous_handle is not None and key < previous_handle.casefold():
                errors.append((number, f"Move @{handle} above @{previous_handle}; sort by GitHub username, not display name."))
            if key in seen:
                errors.append((number, f"@{handle} already appears in the list. Add only one entry per username."))
            profile = PROFILE.fullmatch(url)
            if not profile or profile.group("owner").casefold() != key:
                errors.append((number, f"The GitHub link must point to @{handle}'s own profile."))
            elif profile.group("extra"):
                if HISTORICAL_LINKS.get(key) == url:
                    notices.append((number, f"@{handle} has a preserved historical repository link."))
                else:
                    errors.append((number, f"Use the direct profile link https://github.com/{handle} (no repository path)."))
            seen.add(key)
            previous_handle = handle
            current_entry_line = number
            current_goal_found = False
            count += 1
            continue

        if line.lstrip().startswith("- **") and section is not None:
            errors.append((number, "This entry doesn't match the two-line template in CONTRIBUTING.md."))
        elif section is not None and "github.com/" in line:
            errors.append((number, "This GitHub link isn't in a recognized contributor entry; use the template."))
        elif not current_goal_found and line.lstrip().startswith(">"):
            goal_text = line.lstrip()[1:].strip()
            if goal_text and goal_text not in ("<br>", "<br />"):
                current_goal_found = True

    if not current_goal_found:
        errors.append((current_entry_line, "Add a learning goal on the next line, starting with `  > `."))
    if count == 0:
        errors.append((1, "No contributor entries found. Check the formatting in contributing.md."))
    return count, errors, notices


def historical_records(content: str) -> dict[str, str]:
    """Map usernames to their unmodified visible entry blocks.

    Headings, introductory copy and trailing instructions are not part of a
    person's entry. This prevents a newcomer from changing someone else's
    saved goal while adding their own name.
    """
    lines = content.splitlines()
    records: dict[str, str] = {}
    for index, line in enumerate(lines):
        match = ENTRY.fullmatch(line)
        if not match:
            continue
        end = index + 1
        while end < len(lines):
            other = lines[end]
            if ENTRY.fullmatch(other) or SECTION.fullmatch(other) or other.strip() == '---':
                break
            end += 1
        block = '\n'.join(lines[index:end]).strip()
        records[match.group('handle').casefold()] = block
    return records


def check_preservation(baseline: str, proposed: str) -> list[tuple[int, str]]:
    """Protect existing contributors in PRs, but allow adding new entries."""
    old = historical_records(baseline)
    new = historical_records(proposed)
    errors = []
    for handle, old_record in old.items():
        if handle not in new:
            errors.append((1, f'Existing contributor @{handle} was removed. Please keep earlier entries.'))
        elif new[handle] != old_record:
            errors.append((1, f'Existing contributor @{handle} was changed. Please edit only your own new entry.'))
    return errors


def run(path: Path, *, baseline: Path | None = None, actions: bool = False) -> int:
    if path.is_symlink():
        print("ERROR: contributor file is a symbolic link; use a regular Markdown file.")
        return 1
    try:
        if path.stat().st_size > 512 * 1024:
            print("ERROR: contributor file is unexpectedly large (>512 KiB).")
            return 1
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: Can't read contributor file: {exc}")
        return 1
    count, errors, notices = check_text(content)
    if baseline is not None:
        try:
            baseline_text = baseline.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            print(f'ERROR: Cannot read the original contributor list: {exc}')
            return 1
        errors.extend(check_preservation(baseline_text, content))
    for line, message in notices:
        if actions:
            print(f"::notice file=contributing.md,line={line}::{message}")
        else:
            print(f"NOTE line {line}: {message}")
    for line, message in errors:
        if actions:
            print(f"::error file=contributing.md,line={line}::{message}")
        else:
            print(f"ERROR line {line}: {message}")
    if errors:
        print(f"FAIL: {len(errors)} issue(s). See the entry example in .github/CONTRIBUTING.md.")
        return 1
    print(f"PASS: {count} contributor entries are in order, without duplicate usernames.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the contributor wall, read-only.")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="Path to contributing.md")
    parser.add_argument('--baseline', type=Path, default=None, help='Original contributor wall (for PR preservation checks)')
    args = parser.parse_args()
    return run(args.file, baseline=args.baseline, actions=os.getenv("GITHUB_ACTIONS") == "true")


if __name__ == "__main__":
    raise SystemExit(main())

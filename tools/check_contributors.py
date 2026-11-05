#!/usr/bin/env python3
"""Read-only standard-library checker for the public contributor wall.

Optional maintainer utility: newcomers following the Git Bash tutorial do not
need Python or this script. Run: python tools/check_contributors.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / 'contributing.md'
ENTRY = re.compile(r'^- \*\*(?P<display>.+?)\*\* \(\[`@(?P<handle>[A-Za-z0-9-]+)`\]\((?P<url>https://github\.com/[A-Za-z0-9-]+(?:/[^)]*)?)\)\)$')
HEAD = re.compile(r'^## ([A-Z])$|^## 0–9 and symbols$')


def run() -> int:
    lines = PATH.read_text(encoding='utf-8').splitlines()
    section = None
    prev = ''
    previous_section_rank = -1
    seen = set()
    errors = []
    count = 0
    for lineno, line in enumerate(lines, 1):
        m = HEAD.fullmatch(line)
        if m:
            section = m.group(1) or '0-9'
            rank = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(section) if section != '0-9' else 26
            if rank <= previous_section_rank:
                errors.append(f'line {lineno}: section {section} is out of order or repeated')
            previous_section_rank = rank
            prev = ''
            continue
        m = ENTRY.fullmatch(line)
        if m:
            handle = m.group('handle')
            desired = handle[0].upper() if handle[0].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else '0-9'
            if desired != section:
                errors.append(f'line {lineno}: @{handle} is under {section}, should be {desired}')
            if prev and (handle.lower(), handle) < (prev.lower(), prev):
                errors.append(f'line {lineno}: @{handle} is out of order after @{prev}')
            if handle.casefold() in seen:
                errors.append(f'line {lineno}: duplicate @{handle}')
            # The author may have contributed a link to a specific repository in the old list.
            # Keep it for historical accuracy; warn rather than silently changing it.
            if m.group('url').rstrip('/').split('github.com/', 1)[1].count('/'):
                print(f'NOTE line {lineno}: @{handle} links to more than a profile; review manually')
            seen.add(handle.casefold())
            prev = handle
            count += 1
        elif section is not None and 'github.com/' in line and not m:
            errors.append(f'line {lineno}: unrecognized contributor link or entry; follow the required template')
    if count == 0:
        errors.append('No formatted contributors found')
    for message in errors:
        print('ERROR:', message, file=sys.stderr)
    if errors:
        print(f'FAIL: {len(errors)} issues across {count} contributors', file=sys.stderr)
        return 1
    print(f'PASS: {count} contributor entries in alphabetical GitHub-username order; no duplicate handles')
    return 0


if __name__ == '__main__':
    sys.exit(run())

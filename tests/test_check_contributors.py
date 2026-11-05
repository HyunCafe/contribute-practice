"""Regression tests for contributor validation. Run with unittest; no downloads."""
from __future__ import annotations

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('checker', ROOT / 'tools' / 'check_contributors.py')
checker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(checker)


def entry(handle, goal='My goal is to understand Git better.', display=None, url=None):
    display = display or handle
    url = url or f'https://github.com/{handle}'
    return f'- **{display}** ([`@{handle}`]({url}))\n  > "{goal}"\n'


class ContributorChecks(unittest.TestCase):
    def test_sorted_names_and_goals(self):
        text = '# Wall\n## A\n' + entry('anna') + entry('anne') + '\n## B\n' + entry('bob')
        count, errors, notices = checker.check_text(text)
        self.assertEqual((count, errors, notices), (3, [], []))

    def test_sorts_by_full_handle_not_display_name(self):
        text = '## A\n' + entry('anne', display='Zoe') + entry('anna', display='Amy')
        self.assertIn('sort by GitHub username', str(checker.check_text(text)[1]))

    def test_rejects_duplicate(self):
        text = '## A\n' + entry('anna') + entry('Anna')
        self.assertIn('already appears', str(checker.check_text(text)[1]))

    def test_rejects_wrong_letter(self):
        text = '## A\n' + entry('bob')
        self.assertIn('belongs in section B', str(checker.check_text(text)[1]))

    def test_rejects_profile_mismatch(self):
        text = '## A\n' + entry('anna', url='https://github.com/not-anna')
        self.assertIn('own profile', str(checker.check_text(text)[1]))

    def test_rejects_unapproved_repo_link(self):
        text = '## A\n' + entry('anna', url='https://github.com/anna/sample')
        self.assertIn('direct profile link', str(checker.check_text(text)[1]))

    def test_preserves_one_historical_repo_link(self):
        text = '## S\n' + entry('suyashsahu00', url='https://github.com/suyashsahu00/CODING')
        count, errors, notices = checker.check_text(text)
        self.assertEqual(count, 1)
        self.assertFalse(errors)
        self.assertEqual(len(notices), 1)

    def test_rejects_missing_goal(self):
        text = '## A\n' + entry('anna').splitlines()[0] + '\n## B\n' + entry('bob')
        self.assertIn('learning goal', str(checker.check_text(text)[1]))

    def test_accepts_legacy_br_and_multiple_goals(self):
        text = '## A\n' + entry('anna').replace('  >', '  > <br>\n  >', 1)
        self.assertFalse(checker.check_text(text)[1])

    def test_bad_template_gives_advice(self):
        text = '## A\n- **anna** (https://github.com/anna)\n  > hello\n'
        self.assertIn('two-line template', str(checker.check_text(text)[1]))

    def test_duplicate_letter_section(self):
        text = '## A\n' + entry('anna') + '\n## A\n' + entry('amber')
        self.assertIn('repeated', str(checker.check_text(text)[1]))

    def test_preserves_existing_profiles(self):
        old = '## A\n' + entry('anna') + '## B\n' + entry('bob')
        new = '## A\n' + entry('anna') + entry('anne') + '## B\n' + entry('bob')
        self.assertEqual(checker.check_preservation(old, new), [])

    def test_blocks_removal_of_historical_entry(self):
        old = '## A\n' + entry('anna') + entry('anne')
        new = '## A\n' + entry('anne')
        self.assertIn('was removed', str(checker.check_preservation(old, new)))

    def test_blocks_altering_historical_goal(self):
        old = '## A\n' + entry('anna', goal='Keep learning.')
        new = '## A\n' + entry('anna', goal='Changed without permission.')
        self.assertIn('was changed', str(checker.check_preservation(old, new)))

    def test_baseline_cli_guard(self):
        with tempfile.TemporaryDirectory() as d:
            old = Path(d) / 'old.md'
            new = Path(d) / 'new.md'
            old.write_text('## A\n' + entry('anna'), encoding='utf-8')
            new.write_text('## A\n' + entry('anna', goal='overwritten'), encoding='utf-8')
            with redirect_stdout(io.StringIO()):
                code = checker.run(new, baseline=old)
            self.assertEqual(code, 1)

    def test_cli_file_selection(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'contributing.md'
            p.write_text('## A\n' + entry('anna'), encoding='utf-8')
            out = io.StringIO()
            with redirect_stdout(out):
                code = checker.run(p)
            self.assertEqual(code, 0)
            self.assertIn('PASS:', out.getvalue())


if __name__ == '__main__':
    unittest.main()

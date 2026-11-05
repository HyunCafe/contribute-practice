"""Offline content checks, including examples, visual preservation and CI trust."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'README.md').read_text(encoding='utf-8')
GUIDE = (ROOT / '.github/CONTRIBUTING.md').read_text(encoding='utf-8')
WORKFLOW = (ROOT / '.github/workflows/check-contributors.yml').read_text(encoding='utf-8')
TROUBLE = (ROOT / 'docs/TROUBLESHOOTING.md').read_text(encoding='utf-8')
ASSETS = {'flamey.gif', 'Coffee.gif', 'studiogif.gif', 'forkrepo.JPG',
          'createforkrepo.JPG', 'clonestep1.JPG', 'prstep1.JPG',
          'prstep2.JPG', 'totoro.gif', 'borderseperator.gif'}

class QualityPassTests(unittest.TestCase):
    def test_all_original_assets_still_referenced(self):
        self.assertEqual(set(re.findall(r'src="assests/([^\"]+)"', README)), ASSETS)

    def test_original_visual_widths_remain_consistent(self):
        for asset in ASSETS:
            self.assertRegex(README, rf'<img[^>]+src="assests/{re.escape(asset)}"\s+width="\d+"')

    def test_vs_code_stays_primary_editor(self):
        self.assertIn('Visual Studio Code (VS Code)', README)
        self.assertIn('code .', README)
        self.assertIn('Ctrl+S', README)
        self.assertNotIn('notepad.exe', README.lower())
        self.assertIn('VS Code', GUIDE)

    def test_examples_are_consistent(self):
        for data in (README, GUIDE):
            self.assertIn('YOUR_DISPLAY_NAME', data)
            self.assertIn('YOUR_USERNAME', data)
            self.assertIn('YOUR_LEARNING_GOAL', data)
            self.assertIn('**HyunCafe**', data)
            self.assertIn('https://github.com/HyunCafe', data)
            self.assertIn('practice Git, make a small change', data)
            self.assertIn('illustrative', data.lower())
        self.assertNotIn('greenfoxdev', README)
        self.assertNotIn('greenfoxdev', TROUBLE)
        self.assertIn('HyunCafe/contribute-practice.git', TROUBLE)
        self.assertIn('git remote -v', TROUBLE)

    def test_maintainer_example_appears_raw_and_rendered(self):
        for data in (README, GUIDE):
            self.assertGreaterEqual(data.count('**HyunCafe**'), 2)
            self.assertGreaterEqual(data.count('```md'), 2)

    def test_read_only_trusted_workflow(self):
        self.assertIn('pull_request:', WORKFLOW)
        self.assertNotIn('pull_request_target:', WORKFLOW)
        self.assertIn('contents: read', WORKFLOW)
        self.assertNotIn('contents: write', WORKFLOW)
        self.assertIn('checkout@11d5960a326750d5838078e36cf38b85af677262', WORKFLOW)
        self.assertIn('git show "$BASE_SHA:tools/check_contributors.py"', WORKFLOW)
        self.assertIn('git show "$BASE_SHA:contributing.md"', WORKFLOW)
        self.assertIn('--baseline', WORKFLOW)
        self.assertNotIn('secrets.', WORKFLOW)

    def test_git_technical_steps_retained(self):
        for command in ('git clone https://github.com/YOUR_USERNAME/',
                        'git switch -c add-my-first-contribution',
                        'git diff --check', 'git add contributing.md',
                        'git commit -m', 'git push -u origin HEAD'):
            self.assertIn(command, README)

if __name__ == '__main__':
    unittest.main()

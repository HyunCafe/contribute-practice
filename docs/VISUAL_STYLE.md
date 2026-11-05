# README visual style guide

The pictures and GIFs are part of this project's personality. Keep them in place when editing the tutorial.

## Layout rules

- **Original artwork:** Reference images from `assests/` (historical spelling retained). Do not rename or remove the folder during a documentation refresh.
- **Widths:** Coffee hero `640`, decorative header flames `48`, walkthrough screenshots `540`, studio cat `360`, Totoro celebration `640`, separator `680`. Browser rendering will scale them down on narrower screens.
- **Alignment:** Center illustrations, use consistent widths within each category, and caption screenshots consistently. Keep Git commands and numbered steps left aligned for readability.
- **Alt text:** Describe instructional images. Use empty `alt=""` only for repeated decorative visuals.
- **Screenshots:** Put each beside the matching step. If GitHub changes its UI, update the caption; don't quietly teach obsolete controls. The legacy clone screenshot shows SSH, so label it clearly and keep the HTTPS instruction prominent.
- **Tone:** Friendly and practical. Write as if you're guiding someone at the same computer. Avoid corporate slogans, forced enthusiasm, filler, or explaining the same action twice.
- **Accessibility:** Keep meaningful headings in order, and don't convey an instruction through an image alone.
- **Contributor list:** `contributing.md` is the single source of truth; never recreate a duplicate A–Z list in README.

## Asset note

The original assets are intentionally preserved, even if some are not currently displayed. `assests/congrats.gif` is around 13 MiB, so don't embed it in every pull request template by default. A link to it is fine.

Before merging a visual change, preview the README on GitHub in both light and dark themes and check it at a narrow window width. Automated tests can check links and markup, but they cannot guarantee that animated images feel visually balanced.

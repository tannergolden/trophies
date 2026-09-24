# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The README block between `<!-- trophies:start -->` and `<!-- trophies:end -->`.

The action owns only what sits between the markers. The first run appends
the block if the markers are missing; every later run rewrites what is
between them and nothing else. Each image exists twice, a Night file and a
Day file, and by default they are embedded in one `<picture>` element whose
`prefers-color-scheme` source picks the Night file on a dark system, the way
GitHub documents. `theme: fragment` writes the older `#gh-dark-mode-only`
and `#gh-light-mode-only` pair instead; GitHub's own CSS no longer hides
the other one on a repository page, so both cards show, and it is kept only
for a README rendered somewhere that still honours the fragments.

Every card links to its entry in the catalogue, so a viewer can find what a
trophy or achievement is for and how it is earned in one click. The link
goes through `blob/HEAD`, the default branch, so it never waits on a tag.
"""
from __future__ import annotations

from html import escape
from pathlib import Path

START, END = "<!-- trophies:start -->", "<!-- trophies:end -->"
CATALOGUE = "https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md"


def _img(base: str, alt: str, theme: str, width: int | None = None) -> str:
    w = f' width="{width}"' if width else ""
    alt = escape(alt, quote=True)
    if theme == "picture":
        return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{base}.svg">'
                f'<img src="{base}-day.svg" alt="{alt}"{w}></picture>')
    return (f'<img src="{base}.svg#gh-dark-mode-only" alt="{alt}"{w}>'
            f'<img src="{base}-day.svg#gh-light-mode-only" alt="{alt}"{w}>')


def block(out: str, mode: str, cores: list, alts: dict, pins: list, groups: list, summary: str, theme: str = "picture",
          banner: bool = True) -> str:
    """The Markdown/HTML between the markers.

    `alts` maps each file base name to its alt text; `pins` is a list of
    (group index, base, alt) for achievements in display order.
    """
    lines = [START, ""]
    if banner:
        lines += ['<p align="center">', "  " + _img(f"{out}/level", alts.get("level", "Level"), theme),
                  "  " + _img(f"{out}/next-up", alts.get("next-up", "Next up"), theme), "</p>", ""]
    lines.append('<p align="center">')
    for c in cores:
        lines.append(f'  <a href="{CATALOGUE}#{mode}-{c.key}">' + _img(f"{out}/{c.key}", alts.get(c.key, c.title), theme) + "</a>")
    lines += ["</p>", "", "<details>", f"<summary><b>Achievements</b> · {summary}</summary>", ""]
    for gi, g in enumerate(groups):
        mine = [(b, a) for (gg, b, a) in pins if gg == gi]
        if not mine:
            continue
        lines += [f'<p align="center"><b>{g}</b></p>', '<p align="center">']
        for base, alt in mine:
            lines.append(f'  <a href="{CATALOGUE}#{mode}-{base}">' + _img(f"{out}/achievements/{base}", alt, theme) + "</a>")
        lines += ["</p>", ""]
    lines += ["</details>", "",
              '<p align="center"><sub>Refreshed daily by <a href="https://github.com/tannergolden/trophies">tannergolden/trophies</a>'
              f' · Every trophy and achievement, what it is for and how to earn it: <a href="{CATALOGUE}#{mode}">the catalogue</a>.'
              ' Click any card for its entry.</sub></p>',

              END]
    return "\n".join(lines)


def apply(path: Path, content: str) -> bool:
    """Write `content` between the markers, appending the block on the first run. Returns True if the file changed."""
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if START in text and END in text:
        a, b = text.index(START), text.index(END) + len(END)
        new = text[:a] + content + text[b:]
    else:
        new = text.rstrip("\n") + ("\n\n" if text.strip() else "") + content + "\n"
    if new == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(new, encoding="utf-8")
    return True

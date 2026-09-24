# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The README block between `<!-- trophies:start -->` and `<!-- trophies:end -->`.

The action owns only what sits between the markers. The first run appends
the block if the markers are missing; every later run rewrites what is
between them and nothing else. Each image is embedded twice, a Night file
with `#gh-dark-mode-only` and a Day file with `#gh-light-mode-only`, which
follow the viewer's GitHub theme rather than their operating system. With
`theme: picture` a `<picture>` element is written instead.
"""
from __future__ import annotations

from html import escape
from pathlib import Path

START, END = "<!-- trophies:start -->", "<!-- trophies:end -->"
CATALOGUE = "https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md"


def _img(base: str, alt: str, theme: str, width: int | None = None) -> str:
    w = f' width="{width}"' if width else ""
    alt = escape(alt, quote=True)
    if theme == "picture":
        return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{base}.svg">'
                f'<img src="{base}-day.svg" alt="{alt}"{w}></picture>')
    return (f'<img src="{base}.svg#gh-dark-mode-only" alt="{alt}"{w}>'
            f'<img src="{base}-day.svg#gh-light-mode-only" alt="{alt}"{w}>')


def block(out: str, mode: str, cores: list, alts: dict, pins: list, groups: list, summary: str, theme: str = "fragment",
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
        lines.append(f'  <a href="{CATALOGUE}#{c.key}">' + _img(f"{out}/{c.key}", alts.get(c.key, c.title), theme) + "</a>")
    lines += ["</p>", "", "<details>", f"<summary><b>Achievements</b> · {summary}</summary>", ""]
    for gi, g in enumerate(groups):
        mine = [(b, a) for (gg, b, a) in pins if gg == gi]
        if not mine:
            continue
        lines += [f'<p align="center"><b>{g}</b></p>', '<p align="center">']
        for base, alt in mine:
            lines.append("  " + _img(f"{out}/achievements/{base}", alt, theme))
        lines += ["</p>", ""]
    lines += ["</details>", "",
              '<p align="center"><sub>Refreshed daily by <a href="https://github.com/tannergolden/trophies">tannergolden/trophies</a></sub></p>',
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

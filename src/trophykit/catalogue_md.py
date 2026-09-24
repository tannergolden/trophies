# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""docs/Catalogue.md, generated from the catalogue so it cannot drift."""
from __future__ import annotations

from .catalogue import MODES, RARITY_NAMES, TIER_NAMES

HEAD = """<!--
title: '🏆 CATALOGUE'
description: 'Every trophy and achievement the kit can award, in both modes, with the threshold and the GitHub data behind each one.'
tags: [trophies, achievements, catalogue, reference]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🏆 CATALOGUE

<a name="top"></a>

**Every trophy and achievement, and what earns it.**

_Generated from the data by `make catalogue`. Do not edit by hand._

</div>

---

## 🎯 How Tiers Work

A **core trophy** counts something that only grows. It is cut into five tiers,
Bronze to Diamond, and the card shows progress from the tier you hold to the
next one. Past Diamond it earns a **star** each time the Diamond number
doubles, up to five.

An **achievement** is earned or not. A **tiered** one is earned several times,
at each threshold listed, and the pin shows the numeral you hold. Its
**rarity** decides the metal it is drawn in. **Secret** ones show a question
mark until earned. Anything marked **heavy** reads individual commits rather
than a single count, so it runs under a budget and catches up over a week.

"""

FOOT = """
---

<div align="center">

[↑ Back to Top](#top)

</div>
"""


def _fmt(n) -> str:
    return f"{n:,}"


def _core_table(mode: str, cores) -> str:
    rows = ["| Trophy | Counts | Enamel | Bronze | Silver | Gold | Platinum | Diamond | Source |", "| :-- | :-- | :-- | --: | --: | --: | --: | --: | :-- |"]
    for c in cores:
        unit = f" {c.unit}" if c.unit else ""
        rows.append(f'| <a name="{mode}-{c.key}"></a>**{c.title}** | {c.counts} | `{c.tok}` | '
                    + " | ".join(_fmt(s) + unit for s in c.steps) + f" | `{c.src}` |")
    return "\n".join(rows)


def _ach_table(mode: str, ach, groups) -> str:
    out = []
    for gi, g in enumerate(groups):
        mine = [a for a in ach if a.g == gi]
        if not mine:
            continue
        out.append(f"### {g}\n")
        out.append("| Achievement | Earned by | Rarity | Source |")
        out.append("| :-- | :-- | :-- | :-- |")
        for a in mine:
            flags = []
            if a.goals:
                flags.append("tiers " + " / ".join(_fmt(x) for x in a.goals))
            if a.secret:
                flags.append("secret")
            if a.heavy:
                flags.append("heavy")
            if a.only:
                flags.append(f"owner of `{a.only}` only")
            name = f'<a name="{mode}-{a.slug}"></a>**{a.name}**' + (f" <sub>{', '.join(flags)}</sub>" if flags else "")
            rarity = " → ".join(RARITY_NAMES[r] for r in a.rarities)
            out.append(f"| {name} | {a.how} | {rarity} | `{a.src}` |")
        out.append("")
    return "\n".join(out)


def page() -> str:
    parts = [HEAD]
    for mode, label, intro in (
        ("profile", "Profile Mode", "The subject is a person. Counts run across every repository the account owns, with the profile repository, bot commits, forks and self-stars left out."),
        ("repository", "Repository Mode", "The subject is one repository: the one the stub runs in. Health is binary here, Reach draws on the ledger and the traffic API, and stars exclude the owner and, for an organization, its members."),
    ):
        m = MODES[mode]
        public = [a for a in m["ach"] if not a.only]
        parts.append(f'<a name="{mode}"></a>\n\n## {"👤" if mode == "profile" else "📦"} {label}\n\n{intro}\n')
        parts.append(f"### The {len(m['core'])} core trophies\n")
        parts.append(_core_table(mode, m["core"]) + "\n")
        parts.append(f"### The {len(public)} achievements\n")
        parts.append(_ach_table(mode, m["ach"], m["groups"]))
        parts.append("---\n")
    parts.append("## 🏅 Tiers and Rarities\n")
    parts.append("| Tier | " + " | ".join(TIER_NAMES) + " |\n| :-- | " + " | ".join(":--" for _ in TIER_NAMES) + " |\n"
                 "| Metal | ghost | bronze | silver | gold | platinum | diamond |\n")
    parts.append("| Rarity | " + " | ".join(RARITY_NAMES[1:]) + " |\n| :-- | " + " | ".join(":--" for _ in RARITY_NAMES[1:]) + " |\n"
                 "| Metal | bronze | silver | gold | platinum | diamond |")
    parts.append(FOOT)
    return "\n".join(parts)

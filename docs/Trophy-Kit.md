<!--
title: '🏆 TROPHY KIT'
description: 'The specification for the trophy generator: the case, the tiers, the two modes, the files it writes, the ledger, and the contract every consumer relies on.'
tags: [trophies, specification, svg, automation]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🏆 TROPHY KIT

<a name="top"></a>

**The specification: what a run measures, what it draws, and what it promises.**

_Earned, never claimed._

</div>

---

## 🎯 Intent

A trophy here is a **committed SVG** rendered from a measurement the action
took over GitHub's API. That removes any third-party dependency from the
README, removes any rate-limit risk at view time, and puts the metal, the
lettering and the geometry under one generator.

The kit is one Python package with no dependencies, driven by one command:

| Module              | Job                                                                        |
| :------------------ | :------------------------------------------------------------------------- |
| `catalogue.py`      | Every trophy and achievement as data, plus the tier arithmetic.            |
| `measure_profile.py`, `measure_repo.py`, `scan.py`, `calendar.py` | Measurement: GraphQL, REST, the commit scanner, date maths. |
| `art.py`, `styles.py`, `text.py` | Drawing: five card styles, the pin, the level and next-up cards, outlined lettering. |
| `render.py`, `readme.py`, `ledger.py`, `config.py` | The plan of files, the README block, the ledger, the config. |
| `trophy-kit.py`     | The command line the action runs.                                          |

---

## 🧱 The Case

A case is what one run produces for one **subject**: a person in profile mode,
a repository in repository mode.

| Piece         | Files                                              | Size            |
| :------------ | :------------------------------------------------- | :-------------- |
| Core trophies | `<key>.svg`, `<key>-day.svg`, eight of each        | 164x222 (drawn at 180x244) |
| Level card    | `level.svg`, `level-day.svg`                       | 420x152         |
| Next-up card  | `next-up.svg`, `next-up-day.svg`                   | 328x152         |
| Achievements  | `achievements/<slug>.svg`, `achievements/<slug>-day.svg` | 104x124   |

Everything lands under `assets/trophies/` (configurable as `out`). Night files
carry no suffix; Day files carry `-day`. Rendering **prunes**: a file nothing
in the plan names is deleted, so the folder mirrors the catalogue.

### Tiers

A core value is cut at five thresholds into Unranked, Bronze, Silver, Gold,
Platinum and Diamond. The card shows progress from the tier held to the next.
Past Diamond a trophy earns a **star** each time the Diamond threshold doubles,
to a maximum of five, after which it reads ALL STARS.

### Achievements

An achievement has a **goal** (or several, for a tiered one) and a **rarity**
per tier, Common to Legendary, which decides its metal. Its state at a value
`cur` is one of:

- **secret**: `secret: true` and not yet earned. Drawn as a question mark; the
  alt text says only "Secret achievement".
- **unearned**: below the first goal. A ghost pin with a progress ring.
- **earned**: at or past a goal. The pin wears the tier's metal and, for a
  tiered one, the numeral held (I, II, III) and a ring toward the next tier.
- **not measured**: the run returned `None`. Drawn as unearned with the
  caption NOT MEASURED YET and listed in the run summary. Never as zero.

Owner-only entries (`only: owner/repo`) exist only when the subject owns that
repository, resolved live on each run. For anyone else they are dropped
before counting, so every other subject's total is exactly one hundred.

### The level card

XP is the sum over trophies of a tier schedule (0, 100, 300, 700, 1,500,
3,100, then 400 per star) and over achievements of a rarity schedule (50,
100, 200, 400, 800 per tier earned). Level `L` needs `15·L·(L+1)` XP. The
card also shows **case completion**, the mean of each trophy's tier fraction
and each achievement's earned state, and a footer line: the current streak in
profile mode, days since the last release in repository mode.

### Card details

Three optional details, all on by default (`card: [rank, weekly, new]`):

- **rank**: a TOP N% chip, the share of the reference population at or above
  the value, read from `calibration.py`: 122,914 located GitHub accounts for a
  profile, starred public repositories for a repository. Measured where a
  dataset holds the count, derived or estimated and labelled so where it does
  not; the catalogue's calibration section says which is which.
- **weekly**: a green `+N` beside the value when the ledger shows growth over
  the last seven days.
- **new**: a NEW corner ribbon and a one-time light burst for seven days after
  a tier or star is first reached, dated by the ledger.

---

## 🎨 Drawing Rules

**Deterministic.** The same measurement and options produce byte-identical
output. No date, time or random value is ever drawn.

**Self-contained.** No `<text>` elements, no web fonts, no external
references, no scripts. Lettering is placed with `<use>` from glyph outlines
embedded once per file in `<defs>`. Titles and tier names use Cinzel Bold;
numbers and captions use Barlow Condensed. Both are under the SIL Open Font
License, which permits embedding outlines in a document.

**Two cases.** Night for a dark theme, Day for a light one. The README shows
one of them through a `<picture>` element (`theme: picture`, the default)
whose `prefers-color-scheme` source follows the viewer's system theme, the
method GitHub documents. `theme: fragment` writes the older
`#gh-dark-mode-only` and `#gh-light-mode-only` pair instead; GitHub's CSS no
longer hides the other file on a repository page, so both cards show, and the
option stays only for a README rendered somewhere that still honours it.

**Every card is a link.** Each trophy and achievement links to its entry in
`docs/Catalogue.md` on the default branch, under a mode-specific anchor
(`#profile-commits`, `#repository-first-star`), and the footer links to the
mode's section, so how to earn a thing is one click from the card.

**Motion, gently.** Gold and above shine every few seconds; Platinum and above
sparkle. All of it is CSS inside the SVG, and all of it stops under
`prefers-reduced-motion`.

**Versioned.** Every SVG carries `<!--trophy-kit vN night|day-->`. `check`
hard-fails only same-version drift and treats a version difference as
"regenerate on the next run", so a kit release can never wedge a schedule.
The self-test pins one canonical render to `GOLDEN_SHA`; output cannot change
without bumping `KIT_VERSION` knowingly.

**Accessible.** Every image has `role="img"`, a `<title>`, and an
`aria-label` that says what the picture says: tier, value, progress, rank,
weekly change, and whether it was newly reached.

---

## 📏 Measurement

Everything is recomputed on every run. The ledger adds dates and history;
deleting it loses those and nothing else.

### Profile mode

One query for the account, one per year of history for the contribution
calendar (GitHub answers at most a year at a time), pages of repositories the
account owns, one query of ten searches, and the commit scanner. Counting
rules:

- Repositories are the account's own, not forks. Private ones count only with
  `private: true` and a token that can see them.
- Stars exclude the account's own star on its repositories.
- Commits are contribution counts from GitHub's calendar, which already
  excludes bots and unattributed commits.
- Searches (merged pull requests, upstream merges, reviews, issues elsewhere)
  use `-user:<login>` to mean "not in your own repositories".

### Repository mode

One query for the repository and its files, one privileged query that
degrades if the token cannot see collaborators, alerts or rulesets, pages of
issues, merged pull requests, forks, stargazers and discussions, the traffic
API where the token has push access, and the commit scanner over the default
branch. "Someone else" means not the owner and, for an organization, not a
member.

### The commit scanner

Heavy achievements read commits a hundred at a time under `scan_pages` per
run. Results are cached in the ledger keyed by the branch head, so a
repository whose head has not moved costs nothing, and a large account is
fully read within about a week of daily runs. Timestamps use `author.date`,
which keeps the author's offset, so "between midnight and 5 a.m." means the
author's midnight.

### Budget

A typical profile run makes about 15 GraphQL queries plus the scanner's pages
plus one REST call per recently pushed repository for workflow runs, a few
percent of `GITHUB_TOKEN`'s hourly allowance. Partial GraphQL errors (a field
the token cannot see) keep the data that came back and are reported in the
run notes.

---

## 📒 The Ledger

`.github/trophies.lock.json`, when `ledger: true`:

```json
{
  "version": 1,
  "reached": { "commits": { "4.0": "2026-03-14" }, "ach:polyglot": { "2": "2026-05-02" } },
  "history": { "commits": { "2026-09-01": 5606, "2026-09-18": 5730 } },
  "scan": { "octo/toolkit": { "head": "…", "complete": true, "stats": { "…": 0 } } },
  "snapshot": "2026-09-22"
}
```

- `reached` dates the first time each tier (`tier.stars`) or achievement tier
  was held. It drives the NEW ribbon.
- `history` is **sparse**: a value is recorded only when it changed, and
  points older than 400 days are dropped. The weekly change reads the last
  point at or before seven days ago.
- `scan` is the commit scanner's cache.
- `snapshot` is the last weekly write.

The ledger is written when a card changed, when a tier was reached, or when
seven days have passed since the last snapshot. That weekly write is a real
commit, which keeps GitHub from disabling the schedule after sixty days
without one.

---

## 📝 The README Block

With `readme: manage`, the run owns what sits between
`<!-- trophies:start -->` and `<!-- trophies:end -->`. If the markers are
missing, the first run appends the block; every later run rewrites only what
is between them. The block holds the two banner cards, the trophies (each
linked to its entry in the catalogue), and a `<details>` dropdown of
achievements grouped and ordered: earned first by rarity, then in progress by
how close, then secrets. The summary line says how many are earned and what
is closest.

---

## 🧭 The Command Line

```bash
python3 src/trophy-kit.py run      --root . [--mode …] [--subject …] [--save m.json]
python3 src/trophy-kit.py measure  --mode … --subject … > m.json
python3 src/trophy-kit.py render   --root . --from m.json
python3 src/trophy-kit.py check    --root . --from m.json
python3 src/trophy-kit.py preview  --root out/ [--mode …] [--style …] [--owner]
python3 src/trophy-kit.py catalogue > docs/Catalogue.md
python3 src/trophy-kit.py self-test
```

`--today YYYY-MM-DD` fixes the date for reproducible runs. The action calls
`run`; `preview` renders the built-in sample with no network and is what the
tests and `make preview` use.

---

## 🤝 The Contract

What a consumer pinned to `v1` can rely on:

1. The stub is the only file in their repository with behavior in it, and it
   has none: a schedule and a `uses:`.
2. The output tree mirrors the catalogue; nothing else under `out` is touched.
3. The README is edited only between the markers.
4. Commits are authored by the kit's author (the workflow's `author` input)
   and committed by `github-actions[bot]`, as Conventional Commits with the
   required scope and body, and each one is unique to the run: the subject
   names what happened and the body carries the values, the date and the run
   id. The scanner recognises that scope and sets those commits aside, so a
   refresh never counts toward the author's own trophies, or anyone's.
5. A kit release never breaks a scheduled run: a version stamp difference is
   tolerated and regenerated, and the self-test guards the golden render.
6. Everyone's public total is exactly one hundred achievements per mode.

---

<div align="center">

[↑ Back to Top](#top)

</div>

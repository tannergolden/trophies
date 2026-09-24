<!--
title: '🏆 TROPHIES'
description: 'Trophies and achievements a GitHub profile or repository earns for itself: measured on a schedule, drawn as committed SVGs, never fetched.'
tags: [trophies, achievements, svg, github-actions, profile-readme]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🏆 TROPHIES

<a name="top"></a>

**Trophies a GitHub profile or repository earns for itself.**

_Earned, never claimed._

</div>

---

## 💡 What This Is

A scheduled action measures a GitHub profile, or a single repository, and
draws the result as **committed SVGs**: eight tiered trophies, Bronze to
Diamond, a level card, and one hundred achievements in a dropdown. Nothing is
fetched when someone views the README, so nothing can be slow, rate-limited or
down.

It is built the way [`tannergolden/emblems`](https://github.com/tannergolden/emblems)
builds badges and the way [`tannergolden/standards`](https://github.com/tannergolden/standards)
delivers automation: **called, never copied**. Your repository holds a stub
that names the schedule. The measuring, drawing and committing happen here,
so a fix lands once and reaches every case pinned to `v1`.

| Part                     | Job                                                                       |
| :----------------------- | :------------------------------------------------------------------------ |
| `src/trophy-kit.py`      | **The kit.** Measures over GitHub's API and renders the SVGs. Stdlib only. |
| `action.yml`             | **The action.** Runs the kit against the calling repository.              |
| `.github/workflows/trophies.yml` | **The workflow.** Checkout, kit, commit as the bot. What your stub calls. |
| `src/trophykit/catalogue.py` | **The catalogue.** Every trophy and achievement, as data.               |

---

## 🖼️ What It Looks Like

This repository's own case is below, in **repository mode**. It is refreshed
every day by [`🏆 Case`](.github/workflows/case.yml), which calls the same
workflow you would.

<!-- trophies:start -->
<!-- trophies:end -->

Two things to notice. Every card exists twice, a **Night** file for GitHub's
dark theme and a **Day** file for its light theme, and the README picks one
with `#gh-dark-mode-only` links that follow the viewer's GitHub setting. And the
lettering is drawn as paths from two open-licensed typefaces, Cinzel and
Barlow Condensed, so a trophy looks the same on every device.

Cards are 164 px wide so two fit across a phone; pins are 104 px so three do.
The level card and the next-up card sit side by side on a desktop and stack on
a phone.

### Five styles

`trophy` is the default: a cup on a plinth, with an enamel boss carrying the
trophy's icon and five pips counting the tiers. The others are `crest` (a
hexagonal shield whose ornaments change with the tier: rivets, a gem, wings, a
crown), `medallion` (a struck medal on a ribbon, with a progress ring),
`crystal` (glass that fills with light), and `plaque` (emblems' own flat look,
for a row of badges). One key in the config switches all of them.

---

## 🚀 Use It On Your Profile

Add this as `.github/workflows/trophies.yml` in your **profile repository**,
the one named after your account. That stub is the whole interface.

```yaml
name: Trophies
on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

permissions: {}

jobs:
  trophies:
    permissions:
      contents: write
      pull-requests: write
    uses: tannergolden/trophies/.github/workflows/trophies.yml@v1
    with:
      mode: profile
```

Run it once from the Actions tab. The first run writes a block between
`<!-- trophies:start -->` and `<!-- trophies:end -->` at the end of your README
(move the markers wherever you like; later runs rewrite only what is between
them), renders into `assets/trophies/`, and commits as `github-actions[bot]`.
Nothing is copied into your repository except that stub.

The bot commits, never you, because a commit authored by you would count
toward your own Commits and Streak trophies every day.

### Or a repository

The same stub with `mode: repository` gives any repository a case of its own,
measured from that repository: stars from other people, forks, contributors,
commits, releases, merged pull requests, issues resolved and active days, with
its own hundred achievements. `GITHUB_TOKEN` already reads everything about
its own repository, so private repositories need nothing extra.
[`examples/stub-repository.yml`](examples/stub-repository.yml) shows it with
`commit: pr`, which opens one evolving pull request instead of pushing.

### Options

Everything is optional. A [`.github/trophies.yml`](examples/trophies.yml)
in your repository can set:

| Key            | Default                | Meaning                                                                                        |
| :------------- | :--------------------- | :--------------------------------------------------------------------------------------------- |
| `mode`         | `profile`              | `profile` or `repository`.                                                                     |
| `style`        | `trophy`               | `trophy`, `crest`, `medallion`, `crystal` or `plaque`.                                         |
| `case`         | `both`                 | `night`, `day` or `both`.                                                                      |
| `theme`        | `fragment`             | `fragment` uses `#gh-*-mode-only` links (follows the GitHub theme); `picture` uses `<picture>`. |
| `banner`       | `true`                 | The level card and the next-up card.                                                           |
| `streak`       | `current`              | `current` or `longest`. The current streak changes daily while you are active.                 |
| `core`         | all eight              | Which trophies, in order.                                                                      |
| `enamel`       | `{}`                   | Recolor a trophy with any [emblems](https://github.com/tannergolden/emblems) color token.       |
| `achievements` | `all`                  | `all`, `none`, or a list of slugs.                                                             |
| `card`         | `[rank, weekly, new]`  | The Top % chip, the weekly change, the NEW ribbon.                                             |
| `ledger`       | `true`                 | Keep `.github/trophies.lock.json`.                                                             |
| `readme`       | `manage`               | Manage the block between the markers, or `none`.                                               |
| `private`      | `false`                | Count private contributions too. Needs a read-only personal token saved as `TROPHIES_TOKEN`.   |
| `scan_pages`   | `30`                   | Commits read per run for the heavy achievements, in pages of 100.                              |

The workflow also takes `mode`, `subject`, `style`, `commit` (`push` or `pr`)
and `commit-branch` as inputs, for the common cases without a config file.

---

## 🎯 What Gets Measured

Every trophy counts something that only grows. Tier thresholds rise about
five times per step, and past Diamond a trophy earns a **star** each time the
Diamond number doubles, up to five. Counting is honest by design: the profile
repository's own commits, bot commits, forks and stars you gave your own
repositories are all left out.

**[`docs/Catalogue.md`](docs/Catalogue.md)** lists every trophy and every
achievement in both modes, with its threshold and the exact GitHub data it is
read from. It is generated from the catalogue by `make catalogue` and checked
by `make check`, so it cannot drift from what the kit awards.

Achievements come in groups. Profile mode has **Milestones, Craft, Rhythm,
Community, Housekeeping and Secret**; repository mode has **Launch, Health,
Craft, Community, Reach, Rhythm and Secret**. Some are **tiered**: Polyglot is
earned at 5, 10 and 20 languages, and the pin shows the numeral you hold.
**Secret** ones show a question mark until earned. Ones marked **heavy** read
individual commits rather than a single count, so they run under a per-run
budget and catch up over about a week.

Four more exist only for the account that owns this repository and its
siblings. Everyone else's total is exactly one hundred.

---

## 🔁 How It Runs

Once a day, on the hour at midnight. Nothing on a trophy changes faster
than daily, and GitHub may delay a scheduled run when it is busy, which
costs nothing here.

**Every run recomputes everything from GitHub.** Nothing depends on the last
run, so a delayed or skipped one loses nothing. A run costs about fifteen
GraphQL queries plus the commit scanner's budget, a few percent of the hourly
limit for `GITHUB_TOKEN`.

**Every commit is a Conventional Commit, and no two read alike.** The bot
commits as `chore(trophies): 🏆 …` with a subject naming the most notable
thing that happened (a tier reached, an achievement earned, or which values
moved) and a body carrying the measured values, the date and the run, per the
[commit standard](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md).

**No date lives in an image.** A file only changes when its number does, so a
quiet day makes no commit. The **ledger**, `.github/trophies.lock.json`,
records the day each tier was first reached (for the NEW ribbon), a sparse
history of the core values (for the weekly change), and the scanner's cache.
It is written when a card changed, when a tier was reached, and once a week
regardless. That weekly commit is what keeps GitHub from switching the
schedule off after sixty quiet days.

---

## 🧭 Layout

```bash
trophies/
├── action.yml                      the composite action
├── .github/workflows/trophies.yml  the reusable workflow your stub calls
├── .github/workflows/case.yml      this repository's own case, by local path
├── .github/trophies.yml            this repository's own config
├── src/
│   ├── trophy-kit.py               the command line
│   ├── trophykit/                  catalogue, art, styles, measurement, ledger, README
│   └── fonts/                      glyph outlines and their OFL licences
├── assets/trophies/                this repository's committed case
├── examples/                       stubs and a starter config to copy
├── tests/                          the unit tests
└── docs/
    ├── Trophy-Kit.md               the full specification
    └── Catalogue.md                every trophy and achievement, generated
```

---

## 🛠️ Working On It

For developing the kit itself, in a clone. Consuming it needs none of this,
only the stub above.

```bash
make help                # list every target
make preview             # render the sample profile case into preview/ (no network)
make preview-repository  # the sample repository case
make catalogue           # regenerate docs/Catalogue.md from the data
make check               # CI gate: self-test, catalogue current, sample renders clean
make test                # the gate plus the unit tests
```

Rendering is deterministic and **prunes**: an SVG nothing names anymore is
deleted, so the output folder always mirrors the catalogue. Every SVG carries
a kit version stamp. `check` hard-fails only same-version drift and treats a
version difference as "regenerate next time", so a kit release can never
wedge a consumer's schedule. The self-test pins one canonical render to a
golden hash, so output cannot change unless someone bumps `KIT_VERSION`
knowingly.

To measure a real account locally:

```bash
GITHUB_TOKEN=... python3 src/trophy-kit.py measure --mode profile --subject octocat > m.json
python3 src/trophy-kit.py render --root /tmp/case --from m.json
```

Full specification: [`docs/Trophy-Kit.md`](docs/Trophy-Kit.md).

---

## 📄 License

MIT. See [`LICENSE`](LICENSE).

The glyph outlines in `src/fonts/glyphs.json` are from
[Cinzel](https://github.com/NDISCOVER/Cinzel) and
[Barlow](https://github.com/jpt/barlow), both under the SIL Open Font License
1.1, which permits embedding them in a document. [`NOTICE`](NOTICE) records
the attribution; the licences travel in `src/fonts/`.

---

## 🔗 See also

> [!TIP]
> [`tannergolden/emblems`](https://github.com/tannergolden/emblems) draws the
> badges; this draws the trophies, in the same palette. The engineering
> standards this repository follows are published in
> [`tannergolden/standards`](https://github.com/tannergolden/standards), and it
> was generated from [`tannergolden/path`](https://github.com/tannergolden/path),
> which is why it earns **Follows the Standards** and **Golden Path** itself.

---

<div align="center">

**Measured daily. Drawn once. Never fetched.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

<!--
title: '🏆 TROPHIES'
description: 'Trophies and achievements a GitHub profile or repository earns for itself: measured on a schedule, drawn as committed SVGs, never fetched.'
tags: [github-trophies, github-profile-trophies, github-achievements, profile-readme, github-profile, readme-stats, github-actions, reusable-workflow, svg, badges, gamification]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🏆 TROPHIES

<a name="top"></a>

**Trophies a GitHub profile or repository earns for itself.**

_Earned, never claimed._

[![Status: Active](assets/badges/static/status.svg)](./)
[![Role: Workflow](assets/badges/static/role.svg)](./)
[![Context: Trophies](assets/badges/static/context.svg)](./)
[![License: MIT](assets/badges/static/license.svg)](./LICENSE)

[![Achievements: 100 per mode](assets/badges/static/achievements.svg)](./docs/Catalogue.md)
[![Styles: 5](assets/badges/static/styles.svg)](#five-styles)
[![Uptime: 24/7/365](assets/badges/static/uptime.svg)](#-what-this-is)
[![Dependencies: None](assets/badges/static/dependencies.svg)](./)
[![Use this workflow](assets/badges/static/use-workflow.svg)](#-use-it-on-your-profile)

</div>

---

## 💡 What This Is

A trophy card fetched from someone's server is a request on every page view,
and a dependency on their uptime for your README to render. This draws them
instead.

A trophy here is a **committed SVG**, rendered by a scheduled action from a
measurement it took over GitHub's API: eight tiered trophies, Bronze to
Diamond with stars beyond, a level card, a next-up card, and **one hundred
achievements** in a dropdown, each pinned to real data about how many people
or projects reach it. No request at view time, nothing to rate-limit, and the
metal, the lettering and the geometry are yours.

It is one stub in your repository and one kit here:

| Part                                | Job                                                                             |
| :---------------------------------- | :------------------------------------------------------------------------------ |
| `.github/workflows/trophies.yml`    | **The workflow.** Checkout, kit, commit, push. What your stub calls.            |
| `action.yml`                        | **The action.** Runs the kit against the calling repository.                    |
| `src/trophy-kit.py`                 | **The kit.** Measures over GitHub's API and renders the SVGs. Stdlib only.      |
| `src/trophykit/catalogue.py`        | **The catalogue.** Every trophy and achievement, as data.                       |
| `src/trophykit/calibration.py`      | **The calibration.** Where every tier and rarity sits against real GitHub data. |
| `.github/workflows/cut-release.yml` | **The release.** Cuts `vX.Y.Z` and moves `v1`, by calling the standards.        |

**Called, never copied.** Your repository holds a stub that names the
schedule. The measuring, drawing and committing happen here, so a fix lands
once and reaches every case pinned to `v1`. That is how
[`tannergolden/emblems`](https://github.com/tannergolden/emblems) draws
badges and how [`tannergolden/standards`](https://github.com/tannergolden/standards)
delivers automation; this is the trophy half of the pair, in the same palette,
under the same rule.

Every trophy and achievement is explained in the
[**catalogue**](docs/Catalogue.md): what it counts, how it is earned, how rare
it is, and against what data. Every card in a rendered case links to its own
entry, so the question "what is that one for?" is one click away.

---

## 🟢 Up 24/7/365

Most trophy services are a **live request on every page view**. Your README
renders only while their server answers, so their outages, cold starts and
rate limits land on your page as broken images, and nothing on your side can
fix it. It is a dependency you cannot see until the moment it fails.

A trophy here has **no server to be down**. It is a committed SVG, served by
GitHub with the rest of your repository, so it is up exactly as long as your
repository is: every hour of every day, all year round, with no third party
in the path. The only thing that runs on a schedule is the refresh, and a
refresh that is delayed or skipped changes nothing you can see: yesterday's
trophies stay on the page until the next one lands. That is not an uptime
promise to take on trust; it is a property of a committed file.

|                  | Hosted trophy service                   | Trophies drawn here                                         |
| :--------------- | :-------------------------------------- | :---------------------------------------------------------- |
| **A trophy is**  | An HTTP response, answered at view time | A file in your repository                                   |
| **Down when**    | Their service is                        | Never on its own, only with the page                        |
| **Slow when**    | Their service is busy                   | Never, it is a static file                                  |
| **Rate limits**  | Yes, and not yours to raise             | None at view time; one scheduled run a day                  |
| **Changes when** | Their side deploys                      | The nightly run commits                                     |
| **The numbers**  | Thresholds nobody explains              | Every tier and rarity pinned to a stated share of real data |

---

## 🖼️ What It Looks Like

There is one live example of each mode.

- **Profile mode** is on [**@tannergolden's profile**](https://github.com/tannergolden):
  the case a person earns across every repository they own, with the
  profile's own hundred achievements. It is refreshed daily by the same stub
  shown [below](#-use-it-on-your-profile).
- **Repository mode** is this repository's own case, right here. It is
  refreshed every day by [`🏆 Case`](.github/workflows/case.yml), which calls
  the same workflow you would.

<!-- trophies:start -->

<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/level.svg"><img src="assets/trophies/level-day.svg" alt="tannergolden/trophies: level 20, 6,564 XP, case 25% complete, released 0 days ago"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/next-up.svg"><img src="assets/trophies/next-up-day.svg" alt="Next up: Contributors to Bronze 50%, Label Maker 48%, Commits to Bronze 31%"></picture>
</p>

<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-stars"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/stars.svg"><img src="assets/trophies/stars-day.svg" alt="Stars trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-forks"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/forks.svg"><img src="assets/trophies/forks-day.svg" alt="Forks trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-contributors"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/contributors.svg"><img src="assets/trophies/contributors-day.svg" alt="Contributors trophy: Unranked, 1, 50% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-commits"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/commits.svg"><img src="assets/trophies/commits-day.svg" alt="Commits trophy: Unranked, 31, 31% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-releases"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/releases.svg"><img src="assets/trophies/releases-day.svg" alt="Releases trophy: Bronze, 1, 0% to Silver, top 10%, newly reached"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-merged"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/merged.svg"><img src="assets/trophies/merged-day.svg" alt="Merged PRs trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-resolved"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/resolved.svg"><img src="assets/trophies/resolved-day.svg" alt="Issues Resolved trophy: Unranked, 3, 30% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-active"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/active.svg"><img src="assets/trophies/active-day.svg" alt="Active Days trophy: Unranked, 1 days, 3% to Bronze"></picture></a>
</p>

<details>
<summary><b>Achievements</b> · 27 of 100 earned · next: Contributors to Bronze, 50%</summary>

<p align="center"><b>Launch</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-first-release"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-release.svg"><img src="assets/trophies/achievements/first-release-day.svg" alt="First Release: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-filed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/filed.svg"><img src="assets/trophies/achievements/filed-day.svg" alt="Filed: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-first-tag"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-tag.svg"><img src="assets/trophies/achievements/first-tag-day.svg" alt="First Tag: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-stranger-report"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/stranger-report.svg"><img src="assets/trophies/achievements/stranger-report-day.svg" alt="Stranger Report: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-named"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/named.svg"><img src="assets/trophies/achievements/named-day.svg" alt="Named: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-first-fork"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-fork.svg"><img src="assets/trophies/achievements/first-fork-day.svg" alt="First Fork: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-first-merge"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-merge.svg"><img src="assets/trophies/achievements/first-merge-day.svg" alt="First Merge: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-first-star"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-star.svg"><img src="assets/trophies/achievements/first-star-day.svg" alt="First Star: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-first-watcher"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-watcher.svg"><img src="assets/trophies/achievements/first-watcher-day.svg" alt="First Watcher: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-front-door"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/front-door.svg"><img src="assets/trophies/achievements/front-door-day.svg" alt="Front Door: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-outside-help"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/outside-help.svg"><img src="assets/trophies/achievements/outside-help-day.svg" alt="Outside Help: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-poster"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/poster.svg"><img src="assets/trophies/achievements/poster-day.svg" alt="Poster: 0% (0 of 1)"></picture></a>
</p>

<p align="center"><b>Health</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-gatekeeper"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/gatekeeper.svg"><img src="assets/trophies/achievements/gatekeeper-day.svg" alt="Gatekeeper: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-locksmith"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/locksmith.svg"><img src="assets/trophies/achievements/locksmith-day.svg" alt="Locksmith: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-paperwork"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/paperwork.svg"><img src="assets/trophies/achievements/paperwork-day.svg" alt="Paperwork: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-support-line"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/support-line.svg"><img src="assets/trophies/achievements/support-line-day.svg" alt="Support Line: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-town-hall"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/town-hall.svg"><img src="assets/trophies/achievements/town-hall-day.svg" alt="Town Hall: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-auto-pilot"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/auto-pilot.svg"><img src="assets/trophies/achievements/auto-pilot-day.svg" alt="Auto-pilot: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-form-filler"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/form-filler.svg"><img src="assets/trophies/achievements/form-filler-day.svg" alt="Form Filler: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-house-rules"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/house-rules.svg"><img src="assets/trophies/achievements/house-rules-day.svg" alt="House Rules: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-welcome-mat"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/welcome-mat.svg"><img src="assets/trophies/achievements/welcome-mat-day.svg" alt="Welcome Mat: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-well-formed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/well-formed.svg"><img src="assets/trophies/achievements/well-formed-day.svg" alt="Well-Formed: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-clean-bill"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/clean-bill.svg"><img src="assets/trophies/achievements/clean-bill-day.svg" alt="Clean Bill: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-documented"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/documented.svg"><img src="assets/trophies/achievements/documented-day.svg" alt="Documented: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-licensed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/licensed.svg"><img src="assets/trophies/achievements/licensed-day.svg" alt="Licensed: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-label-maker"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/label-maker.svg"><img src="assets/trophies/achievements/label-maker-day.svg" alt="Label Maker: 48% (12 of 25)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-changelog"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/changelog.svg"><img src="assets/trophies/achievements/changelog-day.svg" alt="Changelog: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-open-hand"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/open-hand.svg"><img src="assets/trophies/achievements/open-hand-day.svg" alt="Open Hand: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-protected"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/protected.svg"><img src="assets/trophies/achievements/protected-day.svg" alt="Protected: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-roadmap"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/roadmap.svg"><img src="assets/trophies/achievements/roadmap-day.svg" alt="Roadmap: 0% (0 of 5)"></picture></a>
</p>

<p align="center"><b>Craft</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-follows-the-standards"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/follows-the-standards.svg"><img src="assets/trophies/achievements/follows-the-standards-day.svg" alt="Follows the Standards: earned, Legendary"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-golden-path"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/golden-path.svg"><img src="assets/trophies/achievements/golden-path-day.svg" alt="Golden Path: earned, Legendary"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-ready-room"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/ready-room.svg"><img src="assets/trophies/achievements/ready-room-day.svg" alt="Ready Room: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-green-machine"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/green-machine.svg"><img src="assets/trophies/achievements/green-machine-day.svg" alt="Green Machine I: earned, Rare, 17% to Green Machine II"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-test-suite"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/test-suite.svg"><img src="assets/trophies/achievements/test-suite-day.svg" alt="Test Suite: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-wired"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/wired.svg"><img src="assets/trophies/achievements/wired-day.svg" alt="Wired: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-squeaky"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/squeaky.svg"><img src="assets/trophies/achievements/squeaky-day.svg" alt="Squeaky: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-by-the-book"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/by-the-book.svg"><img src="assets/trophies/achievements/by-the-book-day.svg" alt="By the Book: 31% (31 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-signed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/signed.svg"><img src="assets/trophies/achievements/signed-day.svg" alt="Signed: 19% (19 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-release-notes"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/release-notes.svg"><img src="assets/trophies/achievements/release-notes-day.svg" alt="Release Notes: 10% (1 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-semver"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/semver.svg"><img src="assets/trophies/achievements/semver-day.svg" alt="Semver: 10% (1 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-containerized"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/containerized.svg"><img src="assets/trophies/achievements/containerized-day.svg" alt="Containerized: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-gitmoji"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/gitmoji.svg"><img src="assets/trophies/achievements/gitmoji-day.svg" alt="Gitmoji: 0% (0 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-packager"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/packager.svg"><img src="assets/trophies/achievements/packager-day.svg" alt="Packager: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-prerelease"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/prerelease.svg"><img src="assets/trophies/achievements/prerelease-day.svg" alt="Prerelease: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-small-steps"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/small-steps.svg"><img src="assets/trophies/achievements/small-steps-day.svg" alt="Small Steps: 0% (0 of 1)"></picture></a>
</p>

<p align="center"><b>Community</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-triage"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/triage.svg"><img src="assets/trophies/achievements/triage-day.svg" alt="Triage: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-crew"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/crew.svg"><img src="assets/trophies/achievements/crew-day.svg" alt="Crew: 20% (1 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-regulars"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/regulars.svg"><img src="assets/trophies/achievements/regulars-day.svg" alt="Regulars: 20% (1 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-ten-strong"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/ten-strong.svg"><img src="assets/trophies/achievements/ten-strong-day.svg" alt="Ten Strong: 10% (1 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-long-thread"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/long-thread.svg"><img src="assets/trophies/achievements/long-thread-day.svg" alt="Long Thread: 4% (4 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-talkative"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/talkative.svg"><img src="assets/trophies/achievements/talkative-day.svg" alt="Talkative: 0% (6 of 1,000)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-answered"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/answered.svg"><img src="assets/trophies/achievements/answered-day.svg" alt="Answered: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-fast-reply"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/fast-reply.svg"><img src="assets/trophies/achievements/fast-reply-day.svg" alt="Fast Reply: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-good-first-issues"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/good-first-issues.svg"><img src="assets/trophies/achievements/good-first-issues-day.svg" alt="Good First Issues: 0% (0 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-help-wanted"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/help-wanted.svg"><img src="assets/trophies/achievements/help-wanted-day.svg" alt="Help Wanted: 0% (0 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-mentor"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/mentor.svg"><img src="assets/trophies/achievements/mentor-day.svg" alt="Mentor: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-org-backed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/org-backed.svg"><img src="assets/trophies/achievements/org-backed-day.svg" alt="Org Backed: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-outside-merges"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/outside-merges.svg"><img src="assets/trophies/achievements/outside-merges-day.svg" alt="Outside Merges: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-popular-opinion"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/popular-opinion.svg"><img src="assets/trophies/achievements/popular-opinion-day.svg" alt="Popular Opinion: 0% (0 of 50)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-reviewed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/reviewed.svg"><img src="assets/trophies/achievements/reviewed-day.svg" alt="Reviewed: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-well-maintained"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/well-maintained.svg"><img src="assets/trophies/achievements/well-maintained-day.svg" alt="Well Maintained: 0% (0 of 25)"></picture></a>
</p>

<p align="center"><b>Reach</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-big-name"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/big-name.svg"><img src="assets/trophies/achievements/big-name-day.svg" alt="Big Name: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-cloned"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/cloned.svg"><img src="assets/trophies/achievements/cloned-day.svg" alt="Cloned: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-downloaded"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/downloaded.svg"><img src="assets/trophies/achievements/downloaded-day.svg" alt="Downloaded: 0% (0 of 1,000)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-fork-magnet"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/fork-magnet.svg"><img src="assets/trophies/achievements/fork-magnet-day.svg" alt="Fork Magnet: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-forked-far"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/forked-far.svg"><img src="assets/trophies/achievements/forked-far-day.svg" alt="Forked Far: 0% (0 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-living-forks"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/living-forks.svg"><img src="assets/trophies/achievements/living-forks-day.svg" alt="Living Forks: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-referred"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/referred.svg"><img src="assets/trophies/achievements/referred-day.svg" alt="Referred: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-registry"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/registry.svg"><img src="assets/trophies/achievements/registry-day.svg" alt="Registry: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-star-of-the-week"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/star-of-the-week.svg"><img src="assets/trophies/achievements/star-of-the-week-day.svg" alt="Star of the Week: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-stargazer-streak"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/stargazer-streak.svg"><img src="assets/trophies/achievements/stargazer-streak-day.svg" alt="Stargazer Streak: 0% (0 of 12)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-trending"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/trending.svg"><img src="assets/trophies/achievements/trending-day.svg" alt="Trending: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-used-by"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/used-by.svg"><img src="assets/trophies/achievements/used-by-day.svg" alt="Used By: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-visited"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/visited.svg"><img src="assets/trophies/achievements/visited-day.svg" alt="Visited: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-watched"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/watched.svg"><img src="assets/trophies/achievements/watched-day.svg" alt="Watched: 0% (0 of 25)"></picture></a>
</p>

<p align="center"><b>Rhythm</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-alive"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/alive.svg"><img src="assets/trophies/achievements/alive-day.svg" alt="Alive: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-long-game"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/long-game.svg"><img src="assets/trophies/achievements/long-game-day.svg" alt="Long Game: 33% (1 of 3)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-same-day-fix"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/same-day-fix.svg"><img src="assets/trophies/achievements/same-day-fix-day.svg" alt="Same-Day Fix: 30% (3 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-monthly-release"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/monthly-release.svg"><img src="assets/trophies/achievements/monthly-release-day.svg" alt="Monthly Release: 8% (1 of 12)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-streak"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/streak.svg"><img src="assets/trophies/achievements/streak-day.svg" alt="Streak: 3% (1 of 30)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-marathon-day"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/marathon-day.svg"><img src="assets/trophies/achievements/marathon-day-day.svg" alt="Marathon Day: 2% (1 of 50)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-night-shift"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/night-shift.svg"><img src="assets/trophies/achievements/night-shift-day.svg" alt="Night Shift: 2% (1 of 50)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-weekly-beat"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/weekly-beat.svg"><img src="assets/trophies/achievements/weekly-beat-day.svg" alt="Weekly Beat: 1% (1 of 52)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-big-week"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/big-week.svg"><img src="assets/trophies/achievements/big-week-day.svg" alt="Big Week: 1% (1 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-comeback"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/comeback.svg"><img src="assets/trophies/achievements/comeback-day.svg" alt="Comeback: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-friday-deploy"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/friday-deploy.svg"><img src="assets/trophies/achievements/friday-deploy-day.svg" alt="Friday Deploy: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-weekend-project"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/weekend-project.svg"><img src="assets/trophies/achievements/weekend-project-day.svg" alt="Weekend Project: 0% (0 of 26)"></picture></a>
</p>

<p align="center"><b>Secret</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-birthday"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/birthday.svg"><img src="assets/trophies/achievements/birthday-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-constellation"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/constellation.svg"><img src="assets/trophies/achievements/constellation-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-friday-the-13th"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/friday-the-13th.svg"><img src="assets/trophies/achievements/friday-the-13th-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-full-house"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/full-house.svg"><img src="assets/trophies/achievements/full-house-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-ghost"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/ghost.svg"><img src="assets/trophies/achievements/ghost-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-green-wall"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/green-wall.svg"><img src="assets/trophies/achievements/green-wall-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-leap-day"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/leap-day.svg"><img src="assets/trophies/achievements/leap-day-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-midnight-oil"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/midnight-oil.svg"><img src="assets/trophies/achievements/midnight-oil-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-new-year"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/new-year.svg"><img src="assets/trophies/achievements/new-year-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-palindrome"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/palindrome.svg"><img src="assets/trophies/achievements/palindrome-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-round-number"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/round-number.svg"><img src="assets/trophies/achievements/round-number-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository-the-answer"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/the-answer.svg"><img src="assets/trophies/achievements/the-answer-day.svg" alt="Secret achievement"></picture></a>
</p>

</details>

<p align="center"><sub>Refreshed daily by <a href="https://github.com/tannergolden/trophies">tannergolden/trophies</a> · Every trophy and achievement, what it is for and how to earn it: <a href="https://github.com/tannergolden/trophies/blob/HEAD/docs/Catalogue.md#repository">the catalogue</a>. Click any card for its entry.</sub></p>
<!-- trophies:end -->

Two things to notice. Every card exists twice, a **Night** file for a dark
theme and a **Day** file for a light one, and the README shows one of them
through a `<picture>` element that follows the viewer's system theme, the
method GitHub documents. And the lettering is drawn as paths from two
open-licensed typefaces, Cinzel and Barlow Condensed, so a trophy looks the
same on every device.

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
them), renders into `assets/trophies/`, and commits. Nothing is copied into
your repository except that stub.

**Who the commit is by.** Each refresh is authored by
[@tannergolden](https://github.com/tannergolden), the author of every trophy
on the page, and committed by `github-actions[bot]`, which is what pushed
it. Neither is you, so nothing here can count toward your own Commits or
Streak. The kit also recognises its own commits by their `chore(trophies)`
scope and sets them aside when it measures, so they count toward nobody's
trophies, its author's included. The `author` input on the workflow
changes the name if you want a different one.

### Or a repository

The same stub with `mode: repository` gives any repository a case of its own,
measured from that repository: stars from other people, forks, contributors,
commits, releases, merged pull requests, issues resolved and active days, with
its own hundred achievements. `GITHUB_TOKEN` already reads everything about
its own repository, so private repositories need nothing extra.
[`examples/stub-repository.yml`](examples/stub-repository.yml) shows it with
`commit: pr`, which opens one evolving pull request instead of pushing.

### Or gate on it

A case is committed files, so it can be checked like any other. With
`check: true` the same workflow measures nothing and commits nothing: it
redraws the case from the measurement the ledger remembers and fails if any
card or the README block differs from what the kit draws. No token is used,
so it runs on a pull request from a fork. Put it in a repository case's CI
so a hand-edited card, a stale README block or a missing file is caught
before it lands: [`examples/stub-check.yml`](examples/stub-check.yml).

### Options

Everything is optional. A [`.github/trophies.yml`](examples/trophies.yml)
in your repository can set:

| Key            | Default               | Meaning                                                                                                                                      |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`         | `profile`             | `profile` or `repository`.                                                                                                                   |
| `subject`      | this repository       | A login in profile mode, `owner/name` in repository mode. Empty means the repository's owner, or the repository.                             |
| `style`        | `trophy`              | `trophy`, `crest`, `medallion`, `crystal` or `plaque`.                                                                                       |
| `case`         | `both`                | `night`, `day` or `both`.                                                                                                                    |
| `theme`        | `picture`             | `picture` uses one `<picture>` per card (follows the system theme); `fragment` uses `#gh-*-mode-only` links, which GitHub no longer honours. |
| `banner`       | `true`                | The level card and the next-up card.                                                                                                         |
| `streak`       | `current`             | `current` or `longest`. The current streak changes daily while you are active.                                                               |
| `core`         | all eight             | Which trophies, in order.                                                                                                                    |
| `enamel`       | `{}`                  | Recolor a trophy with any [emblems](https://github.com/tannergolden/emblems) color token.                                                    |
| `achievements` | `all`                 | `all`, `none`, or a list of slugs.                                                                                                           |
| `card`         | `[rank, weekly, new]` | The Top % chip, the weekly change, the NEW ribbon.                                                                                           |
| `ledger`       | `true`                | Keep `.github/trophies.lock.json`.                                                                                                           |
| `readme`       | `manage`              | Manage the block between the markers, or `none`.                                                                                             |
| `readme_path`  | `README.md`           | The file that holds the markers.                                                                                                             |
| `out`          | `assets/trophies`     | Where the SVGs are written.                                                                                                                  |
| `private`      | `false`               | Count private contributions too. Needs a read-only personal token saved as `TROPHIES_TOKEN`.                                                 |
| `scan_pages`   | `30`                  | Commits read per run for the heavy achievements, in pages of 100.                                                                            |

The workflow also takes `mode`, `subject`, `style`, `commit` (`push` or `pr`),
`commit-branch`, `kit-ref` (the trophies ref to run, `v1` by default),
`author` (who the refresh commit is by) and `check` (verify the committed
case instead of refreshing it) as inputs, for the common cases without a
config file.

---

## 🎯 What Gets Measured

Every trophy counts something that only grows. Tier thresholds rise by three
to five times a step, and past Diamond a trophy earns a **star** each time the
Diamond number doubles, up to five. Counting is honest by design: the profile
repository's own commits, bot commits, the kit's own refresh commits, forks
and stars you gave your own repositories are all left out.

**Every number is pinned to real data.** A tier name and a rarity are claims
about how many people or projects reach a number, so each threshold carries
the share of a reference population at or above it, and each achievement the
share expected to earn it. Profile mode is calibrated against 122,914 located
GitHub accounts refreshed on 2026-09-24 (followers and yearly activity
measured; the rest derived or estimated and labelled as such). Repository
mode is measured against starred public repositories through GitHub's own
API: the **📐 Calibrate** workflow counts stars and forks exactly, samples
repositories from five star bands for the rest, weights the bands by their
population, and commits the shares to `data/calibration/repositories.json`
once a quarter, with the catalogue and this repository's own case
regenerated from the same table. Rarity follows the share: Common is 40% or
more, Legendary under 1%. The **Top N%** chip reads the same table.
The catalogue's [calibration section](docs/Catalogue.md#-how-the-numbers-were-set)
lays it all out, and `src/trophykit/calibration.py` holds it.

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
run, so a delayed or skipped one loses nothing. A profile run costs a few
dozen API calls (one per year of history, one per page of repositories, one
per recently pushed repository for workflow runs) plus the commit scanner's
budget, a few percent of the hourly limit for `GITHUB_TOKEN`.

**Every commit is a Conventional Commit, and no two read alike.** Each
refresh is a `chore(trophies): 🏆 …` commit, authored by the kit's author and
committed by the bot, with a subject naming the most notable thing that
happened (a tier reached, an achievement earned, or which values moved) and a
body carrying the measured values, the date and the run, per the
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
├── action.yml                        the composite action
├── .github/workflows/trophies.yml    the reusable workflow your stub calls
├── .github/workflows/case.yml        this repository's own case, at its own commit
├── .github/workflows/cut-release.yml cuts a version and moves v1, via the standards
├── .github/workflows/badges.yml      redraws the README's badges through emblems
├── .github/workflows/calibrate.yml   measures the repository population, quarterly
├── .github/trophies.yml              this repository's own config
├── .github/trophies.lock.json        this repository's ledger
├── .github/badges.yml                the README's badges, as data
├── src/
│   ├── trophy-kit.py                 the command line
│   ├── calibrate.py                  the repository sampler behind the numbers
│   ├── trophykit/
│   │   ├── catalogue.py              every trophy and achievement, as data
│   │   ├── calibration.py            where every number sits against real data
│   │   ├── art.py, styles.py         the renderer and the five styles
│   │   ├── measure_profile.py        profile mode, over GitHub's API
│   │   ├── measure_repo.py           repository mode
│   │   ├── scan.py                   the commit scanner behind the heavy achievements
│   │   ├── ledger.py, readme.py      what persists between runs, and the README block
│   │   └── render.py                 plan, write, check, and the commit message
│   └── fonts/                        glyph outlines and their OFL licences
├── assets/trophies/                  this repository's committed case
├── assets/badges/                    the README's badges, drawn by emblems
├── data/calibration/                 the measured repository sample the kit reads
├── examples/                         stubs and a starter config to copy
├── tests/                            the unit tests, and the GraphQL document check
└── docs/
    ├── Trophy-Kit.md                 the full specification
    └── Catalogue.md                  every trophy and achievement, generated, with the calibration
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
make check               # CI gate: self-test, every GraphQL document well formed, catalogue current, this case and the sample check clean
make calibrate           # measure the repository population through the API (GITHUB_TOKEN), then regenerate what reads it
make test                # the gate plus the unit tests
make badges              # redraw the README's badges from .github/badges.yml (emblems kit at .emblems/)
```

The badges in the header are drawn by [`tannergolden/emblems`](https://github.com/tannergolden/emblems)
from `.github/badges.yml`, the same way the trophies are drawn here: committed
SVGs, no request at view time. Pushing a change to that file re-renders them
through the **🏷️ Badges** workflow; locally, check the emblems kit out at
`.emblems/` (or point `EMBLEMS_KIT` at it) and run `make badges`.

The GraphQL check also validates every field and argument against GitHub's
schema when `GITHUB_GRAPHQL_SCHEMA` points at the `schema.json` from the
`@octokit/graphql-schema` npm package; without it, the structural checks run.
The API is otherwise the only thing that ever parses the queries, one run at
a time, so this is how a typo in a field name is caught before a case is.

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

### Releasing

Every stub pins `@v1`, a moving major tag, and the reusable workflow fetches
the kit at that same tag. A version is cut by dispatching **🏷️ Cut Release**
with `vX.Y.Z`: the stub calls the standards' release workflow, which refuses a
commit that is not on the default branch or a version that does not move
forward, proves the workflow, the action, the kit and the catalogue exist at
the commit and that `make check` passes, then tags the immutable version,
force-moves `v1`, publishes the release with generated notes and prunes the
pages it superseded. Version tags are never deleted, so a full-version pin
keeps resolving. A release that changes what a card looks like bumps
`KIT_VERSION`, and every case redraws its cards on its next run.

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
> The full specification is [`docs/Trophy-Kit.md`](docs/Trophy-Kit.md).
> [`tannergolden/emblems`](https://github.com/tannergolden/emblems) is the
> other half of the pair: it draws the badges in this header the way this
> draws the trophies, in the same palette, under the same rule. The
> engineering standards this repository follows are published in
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

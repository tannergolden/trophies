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

<p align="center">
  <img src="assets/trophies/level.svg#gh-dark-mode-only" alt="tannergolden/trophies: level 13, 2,966 XP, case 21% complete, no release yet"><img src="assets/trophies/level-day.svg#gh-light-mode-only" alt="tannergolden/trophies: level 13, 2,966 XP, case 21% complete, no release yet">
  <img src="assets/trophies/next-up.svg#gh-dark-mode-only" alt="Next up: Contributors to Bronze 50%, Label Maker 48%, Green Machine I 39%"><img src="assets/trophies/next-up-day.svg#gh-light-mode-only" alt="Next up: Contributors to Bronze 50%, Label Maker 48%, Green Machine I 39%">
</p>

<p align="center">
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#stars"><img src="assets/trophies/stars.svg#gh-dark-mode-only" alt="Stars trophy: Unranked, 0, 0% to Bronze"><img src="assets/trophies/stars-day.svg#gh-light-mode-only" alt="Stars trophy: Unranked, 0, 0% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#forks"><img src="assets/trophies/forks.svg#gh-dark-mode-only" alt="Forks trophy: Unranked, 0, 0% to Bronze"><img src="assets/trophies/forks-day.svg#gh-light-mode-only" alt="Forks trophy: Unranked, 0, 0% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#contributors"><img src="assets/trophies/contributors.svg#gh-dark-mode-only" alt="Contributors trophy: Unranked, 1, 50% to Bronze"><img src="assets/trophies/contributors-day.svg#gh-light-mode-only" alt="Contributors trophy: Unranked, 1, 50% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#commits"><img src="assets/trophies/commits.svg#gh-dark-mode-only" alt="Commits trophy: Unranked, 13, 13% to Bronze"><img src="assets/trophies/commits-day.svg#gh-light-mode-only" alt="Commits trophy: Unranked, 13, 13% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#releases"><img src="assets/trophies/releases.svg#gh-dark-mode-only" alt="Releases trophy: Unranked, 0, 0% to Bronze"><img src="assets/trophies/releases-day.svg#gh-light-mode-only" alt="Releases trophy: Unranked, 0, 0% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#merged"><img src="assets/trophies/merged.svg#gh-dark-mode-only" alt="Merged PRs trophy: Unranked, 0, 0% to Bronze"><img src="assets/trophies/merged-day.svg#gh-light-mode-only" alt="Merged PRs trophy: Unranked, 0, 0% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#resolved"><img src="assets/trophies/resolved.svg#gh-dark-mode-only" alt="Issues Resolved trophy: Unranked, 0, 0% to Bronze"><img src="assets/trophies/resolved-day.svg#gh-light-mode-only" alt="Issues Resolved trophy: Unranked, 0, 0% to Bronze"></a>
  <a href="https://github.com/tannergolden/trophies/blob/v1/docs/Catalogue.md#active"><img src="assets/trophies/active.svg#gh-dark-mode-only" alt="Active Days trophy: Unranked, 1 days, 3% to Bronze"><img src="assets/trophies/active-day.svg#gh-light-mode-only" alt="Active Days trophy: Unranked, 1 days, 3% to Bronze"></a>
</p>

<details>
<summary><b>Achievements</b> · 23 of 100 earned · next: Contributors to Bronze, 50%</summary>

<p align="center"><b>Launch</b></p>
<p align="center">
  <img src="assets/trophies/achievements/stranger-report.svg#gh-dark-mode-only" alt="Stranger Report: earned, Uncommon"><img src="assets/trophies/achievements/stranger-report-day.svg#gh-light-mode-only" alt="Stranger Report: earned, Uncommon">
  <img src="assets/trophies/achievements/named.svg#gh-dark-mode-only" alt="Named: earned, Common"><img src="assets/trophies/achievements/named-day.svg#gh-light-mode-only" alt="Named: earned, Common">
  <img src="assets/trophies/achievements/filed.svg#gh-dark-mode-only" alt="Filed: 0% (0 of 3)"><img src="assets/trophies/achievements/filed-day.svg#gh-light-mode-only" alt="Filed: 0% (0 of 3)">
  <img src="assets/trophies/achievements/first-fork.svg#gh-dark-mode-only" alt="First Fork: 0% (0 of 1)"><img src="assets/trophies/achievements/first-fork-day.svg#gh-light-mode-only" alt="First Fork: 0% (0 of 1)">
  <img src="assets/trophies/achievements/first-merge.svg#gh-dark-mode-only" alt="First Merge: 0% (0 of 1)"><img src="assets/trophies/achievements/first-merge-day.svg#gh-light-mode-only" alt="First Merge: 0% (0 of 1)">
  <img src="assets/trophies/achievements/first-release.svg#gh-dark-mode-only" alt="First Release: 0% (0 of 1)"><img src="assets/trophies/achievements/first-release-day.svg#gh-light-mode-only" alt="First Release: 0% (0 of 1)">
  <img src="assets/trophies/achievements/first-star.svg#gh-dark-mode-only" alt="First Star: 0% (0 of 1)"><img src="assets/trophies/achievements/first-star-day.svg#gh-light-mode-only" alt="First Star: 0% (0 of 1)">
  <img src="assets/trophies/achievements/first-tag.svg#gh-dark-mode-only" alt="First Tag: 0% (0 of 1)"><img src="assets/trophies/achievements/first-tag-day.svg#gh-light-mode-only" alt="First Tag: 0% (0 of 1)">
  <img src="assets/trophies/achievements/first-watcher.svg#gh-dark-mode-only" alt="First Watcher: 0% (0 of 1)"><img src="assets/trophies/achievements/first-watcher-day.svg#gh-light-mode-only" alt="First Watcher: 0% (0 of 1)">
  <img src="assets/trophies/achievements/front-door.svg#gh-dark-mode-only" alt="Front Door: 0% (0 of 1)"><img src="assets/trophies/achievements/front-door-day.svg#gh-light-mode-only" alt="Front Door: 0% (0 of 1)">
  <img src="assets/trophies/achievements/outside-help.svg#gh-dark-mode-only" alt="Outside Help: 0% (0 of 1)"><img src="assets/trophies/achievements/outside-help-day.svg#gh-light-mode-only" alt="Outside Help: 0% (0 of 1)">
  <img src="assets/trophies/achievements/poster.svg#gh-dark-mode-only" alt="Poster: 0% (0 of 1)"><img src="assets/trophies/achievements/poster-day.svg#gh-light-mode-only" alt="Poster: 0% (0 of 1)">
</p>

<p align="center"><b>Health</b></p>
<p align="center">
  <img src="assets/trophies/achievements/clean-bill.svg#gh-dark-mode-only" alt="Clean Bill: earned, Rare"><img src="assets/trophies/achievements/clean-bill-day.svg#gh-light-mode-only" alt="Clean Bill: earned, Rare">
  <img src="assets/trophies/achievements/auto-pilot.svg#gh-dark-mode-only" alt="Auto-pilot: earned, Uncommon"><img src="assets/trophies/achievements/auto-pilot-day.svg#gh-light-mode-only" alt="Auto-pilot: earned, Uncommon">
  <img src="assets/trophies/achievements/form-filler.svg#gh-dark-mode-only" alt="Form Filler: earned, Uncommon"><img src="assets/trophies/achievements/form-filler-day.svg#gh-light-mode-only" alt="Form Filler: earned, Uncommon">
  <img src="assets/trophies/achievements/gatekeeper.svg#gh-dark-mode-only" alt="Gatekeeper: earned, Uncommon"><img src="assets/trophies/achievements/gatekeeper-day.svg#gh-light-mode-only" alt="Gatekeeper: earned, Uncommon">
  <img src="assets/trophies/achievements/house-rules.svg#gh-dark-mode-only" alt="House Rules: earned, Uncommon"><img src="assets/trophies/achievements/house-rules-day.svg#gh-light-mode-only" alt="House Rules: earned, Uncommon">
  <img src="assets/trophies/achievements/locksmith.svg#gh-dark-mode-only" alt="Locksmith: earned, Uncommon"><img src="assets/trophies/achievements/locksmith-day.svg#gh-light-mode-only" alt="Locksmith: earned, Uncommon">
  <img src="assets/trophies/achievements/paperwork.svg#gh-dark-mode-only" alt="Paperwork: earned, Uncommon"><img src="assets/trophies/achievements/paperwork-day.svg#gh-light-mode-only" alt="Paperwork: earned, Uncommon">
  <img src="assets/trophies/achievements/support-line.svg#gh-dark-mode-only" alt="Support Line: earned, Uncommon"><img src="assets/trophies/achievements/support-line-day.svg#gh-light-mode-only" alt="Support Line: earned, Uncommon">
  <img src="assets/trophies/achievements/town-hall.svg#gh-dark-mode-only" alt="Town Hall: earned, Uncommon"><img src="assets/trophies/achievements/town-hall-day.svg#gh-light-mode-only" alt="Town Hall: earned, Uncommon">
  <img src="assets/trophies/achievements/welcome-mat.svg#gh-dark-mode-only" alt="Welcome Mat: earned, Uncommon"><img src="assets/trophies/achievements/welcome-mat-day.svg#gh-light-mode-only" alt="Welcome Mat: earned, Uncommon">
  <img src="assets/trophies/achievements/documented.svg#gh-dark-mode-only" alt="Documented: earned, Common"><img src="assets/trophies/achievements/documented-day.svg#gh-light-mode-only" alt="Documented: earned, Common">
  <img src="assets/trophies/achievements/licensed.svg#gh-dark-mode-only" alt="Licensed: earned, Common"><img src="assets/trophies/achievements/licensed-day.svg#gh-light-mode-only" alt="Licensed: earned, Common">
  <img src="assets/trophies/achievements/well-formed.svg#gh-dark-mode-only" alt="Well-Formed: earned, Common"><img src="assets/trophies/achievements/well-formed-day.svg#gh-light-mode-only" alt="Well-Formed: earned, Common">
  <img src="assets/trophies/achievements/label-maker.svg#gh-dark-mode-only" alt="Label Maker: 48% (12 of 25)"><img src="assets/trophies/achievements/label-maker-day.svg#gh-light-mode-only" alt="Label Maker: 48% (12 of 25)">
  <img src="assets/trophies/achievements/changelog.svg#gh-dark-mode-only" alt="Changelog: 0% (0 of 1)"><img src="assets/trophies/achievements/changelog-day.svg#gh-light-mode-only" alt="Changelog: 0% (0 of 1)">
  <img src="assets/trophies/achievements/open-hand.svg#gh-dark-mode-only" alt="Open Hand: 0% (0 of 1)"><img src="assets/trophies/achievements/open-hand-day.svg#gh-light-mode-only" alt="Open Hand: 0% (0 of 1)">
  <img src="assets/trophies/achievements/protected.svg#gh-dark-mode-only" alt="Protected: 0% (0 of 1)"><img src="assets/trophies/achievements/protected-day.svg#gh-light-mode-only" alt="Protected: 0% (0 of 1)">
  <img src="assets/trophies/achievements/roadmap.svg#gh-dark-mode-only" alt="Roadmap: 0% (0 of 5)"><img src="assets/trophies/achievements/roadmap-day.svg#gh-light-mode-only" alt="Roadmap: 0% (0 of 5)">
</p>

<p align="center"><b>Craft</b></p>
<p align="center">
  <img src="assets/trophies/achievements/follows-the-standards.svg#gh-dark-mode-only" alt="Follows the Standards: earned, Epic"><img src="assets/trophies/achievements/follows-the-standards-day.svg#gh-light-mode-only" alt="Follows the Standards: earned, Epic">
  <img src="assets/trophies/achievements/golden-path.svg#gh-dark-mode-only" alt="Golden Path: earned, Epic"><img src="assets/trophies/achievements/golden-path-day.svg#gh-light-mode-only" alt="Golden Path: earned, Epic">
  <img src="assets/trophies/achievements/squeaky.svg#gh-dark-mode-only" alt="Squeaky: earned, Rare"><img src="assets/trophies/achievements/squeaky-day.svg#gh-light-mode-only" alt="Squeaky: earned, Rare">
  <img src="assets/trophies/achievements/ready-room.svg#gh-dark-mode-only" alt="Ready Room: earned, Uncommon"><img src="assets/trophies/achievements/ready-room-day.svg#gh-light-mode-only" alt="Ready Room: earned, Uncommon">
  <img src="assets/trophies/achievements/test-suite.svg#gh-dark-mode-only" alt="Test Suite: earned, Uncommon"><img src="assets/trophies/achievements/test-suite-day.svg#gh-light-mode-only" alt="Test Suite: earned, Uncommon">
  <img src="assets/trophies/achievements/wired.svg#gh-dark-mode-only" alt="Wired: earned, Common"><img src="assets/trophies/achievements/wired-day.svg#gh-light-mode-only" alt="Wired: earned, Common">
  <img src="assets/trophies/achievements/green-machine.svg#gh-dark-mode-only" alt="Green Machine: 39% (39 of 100)"><img src="assets/trophies/achievements/green-machine-day.svg#gh-light-mode-only" alt="Green Machine: 39% (39 of 100)">
  <img src="assets/trophies/achievements/by-the-book.svg#gh-dark-mode-only" alt="By the Book: 13% (13 of 100)"><img src="assets/trophies/achievements/by-the-book-day.svg#gh-light-mode-only" alt="By the Book: 13% (13 of 100)">
  <img src="assets/trophies/achievements/signed.svg#gh-dark-mode-only" alt="Signed: 12% (12 of 100)"><img src="assets/trophies/achievements/signed-day.svg#gh-light-mode-only" alt="Signed: 12% (12 of 100)">
  <img src="assets/trophies/achievements/containerized.svg#gh-dark-mode-only" alt="Containerized: 0% (0 of 1)"><img src="assets/trophies/achievements/containerized-day.svg#gh-light-mode-only" alt="Containerized: 0% (0 of 1)">
  <img src="assets/trophies/achievements/gitmoji.svg#gh-dark-mode-only" alt="Gitmoji: 0% (0 of 100)"><img src="assets/trophies/achievements/gitmoji-day.svg#gh-light-mode-only" alt="Gitmoji: 0% (0 of 100)">
  <img src="assets/trophies/achievements/packager.svg#gh-dark-mode-only" alt="Packager: 0% (0 of 1)"><img src="assets/trophies/achievements/packager-day.svg#gh-light-mode-only" alt="Packager: 0% (0 of 1)">
  <img src="assets/trophies/achievements/prerelease.svg#gh-dark-mode-only" alt="Prerelease: 0% (0 of 1)"><img src="assets/trophies/achievements/prerelease-day.svg#gh-light-mode-only" alt="Prerelease: 0% (0 of 1)">
  <img src="assets/trophies/achievements/release-notes.svg#gh-dark-mode-only" alt="Release Notes: 0% (0 of 10)"><img src="assets/trophies/achievements/release-notes-day.svg#gh-light-mode-only" alt="Release Notes: 0% (0 of 10)">
  <img src="assets/trophies/achievements/semver.svg#gh-dark-mode-only" alt="Semver: 0% (0 of 10)"><img src="assets/trophies/achievements/semver-day.svg#gh-light-mode-only" alt="Semver: 0% (0 of 10)">
  <img src="assets/trophies/achievements/small-steps.svg#gh-dark-mode-only" alt="Small Steps: 0% (0 of 1)"><img src="assets/trophies/achievements/small-steps-day.svg#gh-light-mode-only" alt="Small Steps: 0% (0 of 1)">
</p>

<p align="center"><b>Community</b></p>
<p align="center">
  <img src="assets/trophies/achievements/triage.svg#gh-dark-mode-only" alt="Triage: earned, Rare"><img src="assets/trophies/achievements/triage-day.svg#gh-light-mode-only" alt="Triage: earned, Rare">
  <img src="assets/trophies/achievements/crew.svg#gh-dark-mode-only" alt="Crew: 20% (1 of 5)"><img src="assets/trophies/achievements/crew-day.svg#gh-light-mode-only" alt="Crew: 20% (1 of 5)">
  <img src="assets/trophies/achievements/regulars.svg#gh-dark-mode-only" alt="Regulars: 20% (1 of 5)"><img src="assets/trophies/achievements/regulars-day.svg#gh-light-mode-only" alt="Regulars: 20% (1 of 5)">
  <img src="assets/trophies/achievements/ten-strong.svg#gh-dark-mode-only" alt="Ten Strong: 10% (1 of 10)"><img src="assets/trophies/achievements/ten-strong-day.svg#gh-light-mode-only" alt="Ten Strong: 10% (1 of 10)">
  <img src="assets/trophies/achievements/long-thread.svg#gh-dark-mode-only" alt="Long Thread: 3% (3 of 100)"><img src="assets/trophies/achievements/long-thread-day.svg#gh-light-mode-only" alt="Long Thread: 3% (3 of 100)">
  <img src="assets/trophies/achievements/talkative.svg#gh-dark-mode-only" alt="Talkative: 0% (3 of 1,000)"><img src="assets/trophies/achievements/talkative-day.svg#gh-light-mode-only" alt="Talkative: 0% (3 of 1,000)">
  <img src="assets/trophies/achievements/answered.svg#gh-dark-mode-only" alt="Answered: 0% (0 of 10)"><img src="assets/trophies/achievements/answered-day.svg#gh-light-mode-only" alt="Answered: 0% (0 of 10)">
  <img src="assets/trophies/achievements/fast-reply.svg#gh-dark-mode-only" alt="Fast Reply: 0% (0 of 1)"><img src="assets/trophies/achievements/fast-reply-day.svg#gh-light-mode-only" alt="Fast Reply: 0% (0 of 1)">
  <img src="assets/trophies/achievements/good-first-issues.svg#gh-dark-mode-only" alt="Good First Issues: 0% (0 of 5)"><img src="assets/trophies/achievements/good-first-issues-day.svg#gh-light-mode-only" alt="Good First Issues: 0% (0 of 5)">
  <img src="assets/trophies/achievements/help-wanted.svg#gh-dark-mode-only" alt="Help Wanted: 0% (0 of 5)"><img src="assets/trophies/achievements/help-wanted-day.svg#gh-light-mode-only" alt="Help Wanted: 0% (0 of 5)">
  <img src="assets/trophies/achievements/mentor.svg#gh-dark-mode-only" alt="Mentor: 0% (0 of 1)"><img src="assets/trophies/achievements/mentor-day.svg#gh-light-mode-only" alt="Mentor: 0% (0 of 1)">
  <img src="assets/trophies/achievements/org-backed.svg#gh-dark-mode-only" alt="Org Backed: 0% (0 of 1)"><img src="assets/trophies/achievements/org-backed-day.svg#gh-light-mode-only" alt="Org Backed: 0% (0 of 1)">
  <img src="assets/trophies/achievements/outside-merges.svg#gh-dark-mode-only" alt="Outside Merges: 0% (0 of 10)"><img src="assets/trophies/achievements/outside-merges-day.svg#gh-light-mode-only" alt="Outside Merges: 0% (0 of 10)">
  <img src="assets/trophies/achievements/popular-opinion.svg#gh-dark-mode-only" alt="Popular Opinion: 0% (0 of 50)"><img src="assets/trophies/achievements/popular-opinion-day.svg#gh-light-mode-only" alt="Popular Opinion: 0% (0 of 50)">
  <img src="assets/trophies/achievements/reviewed.svg#gh-dark-mode-only" alt="Reviewed: 0% (0 of 1)"><img src="assets/trophies/achievements/reviewed-day.svg#gh-light-mode-only" alt="Reviewed: 0% (0 of 1)">
  <img src="assets/trophies/achievements/well-maintained.svg#gh-dark-mode-only" alt="Well Maintained: 0% (0 of 25)"><img src="assets/trophies/achievements/well-maintained-day.svg#gh-light-mode-only" alt="Well Maintained: 0% (0 of 25)">
</p>

<p align="center"><b>Reach</b></p>
<p align="center">
  <img src="assets/trophies/achievements/big-name.svg#gh-dark-mode-only" alt="Big Name: 0% (0 of 1)"><img src="assets/trophies/achievements/big-name-day.svg#gh-light-mode-only" alt="Big Name: 0% (0 of 1)">
  <img src="assets/trophies/achievements/cloned.svg#gh-dark-mode-only" alt="Cloned: not measured yet"><img src="assets/trophies/achievements/cloned-day.svg#gh-light-mode-only" alt="Cloned: not measured yet">
  <img src="assets/trophies/achievements/downloaded.svg#gh-dark-mode-only" alt="Downloaded: 0% (0 of 1,000)"><img src="assets/trophies/achievements/downloaded-day.svg#gh-light-mode-only" alt="Downloaded: 0% (0 of 1,000)">
  <img src="assets/trophies/achievements/fork-magnet.svg#gh-dark-mode-only" alt="Fork Magnet: not measured yet"><img src="assets/trophies/achievements/fork-magnet-day.svg#gh-light-mode-only" alt="Fork Magnet: not measured yet">
  <img src="assets/trophies/achievements/forked-far.svg#gh-dark-mode-only" alt="Forked Far: 0% (0 of 100)"><img src="assets/trophies/achievements/forked-far-day.svg#gh-light-mode-only" alt="Forked Far: 0% (0 of 100)">
  <img src="assets/trophies/achievements/living-forks.svg#gh-dark-mode-only" alt="Living Forks: 0% (0 of 10)"><img src="assets/trophies/achievements/living-forks-day.svg#gh-light-mode-only" alt="Living Forks: 0% (0 of 10)">
  <img src="assets/trophies/achievements/referred.svg#gh-dark-mode-only" alt="Referred: not measured yet"><img src="assets/trophies/achievements/referred-day.svg#gh-light-mode-only" alt="Referred: not measured yet">
  <img src="assets/trophies/achievements/registry.svg#gh-dark-mode-only" alt="Registry: not measured yet"><img src="assets/trophies/achievements/registry-day.svg#gh-light-mode-only" alt="Registry: not measured yet">
  <img src="assets/trophies/achievements/star-of-the-week.svg#gh-dark-mode-only" alt="Star of the Week: not measured yet"><img src="assets/trophies/achievements/star-of-the-week-day.svg#gh-light-mode-only" alt="Star of the Week: not measured yet">
  <img src="assets/trophies/achievements/stargazer-streak.svg#gh-dark-mode-only" alt="Stargazer Streak: 0% (0 of 12)"><img src="assets/trophies/achievements/stargazer-streak-day.svg#gh-light-mode-only" alt="Stargazer Streak: 0% (0 of 12)">
  <img src="assets/trophies/achievements/trending.svg#gh-dark-mode-only" alt="Trending: not measured yet"><img src="assets/trophies/achievements/trending-day.svg#gh-light-mode-only" alt="Trending: not measured yet">
  <img src="assets/trophies/achievements/used-by.svg#gh-dark-mode-only" alt="Used By: not measured yet"><img src="assets/trophies/achievements/used-by-day.svg#gh-light-mode-only" alt="Used By: not measured yet">
  <img src="assets/trophies/achievements/visited.svg#gh-dark-mode-only" alt="Visited: not measured yet"><img src="assets/trophies/achievements/visited-day.svg#gh-light-mode-only" alt="Visited: not measured yet">
  <img src="assets/trophies/achievements/watched.svg#gh-dark-mode-only" alt="Watched: 0% (0 of 25)"><img src="assets/trophies/achievements/watched-day.svg#gh-light-mode-only" alt="Watched: 0% (0 of 25)">
</p>

<p align="center"><b>Rhythm</b></p>
<p align="center">
  <img src="assets/trophies/achievements/alive.svg#gh-dark-mode-only" alt="Alive: earned, Common"><img src="assets/trophies/achievements/alive-day.svg#gh-light-mode-only" alt="Alive: earned, Common">
  <img src="assets/trophies/achievements/long-game.svg#gh-dark-mode-only" alt="Long Game: 33% (1 of 3)"><img src="assets/trophies/achievements/long-game-day.svg#gh-light-mode-only" alt="Long Game: 33% (1 of 3)">
  <img src="assets/trophies/achievements/streak.svg#gh-dark-mode-only" alt="Streak: 3% (1 of 30)"><img src="assets/trophies/achievements/streak-day.svg#gh-light-mode-only" alt="Streak: 3% (1 of 30)">
  <img src="assets/trophies/achievements/marathon-day.svg#gh-dark-mode-only" alt="Marathon Day: 2% (1 of 50)"><img src="assets/trophies/achievements/marathon-day-day.svg#gh-light-mode-only" alt="Marathon Day: 2% (1 of 50)">
  <img src="assets/trophies/achievements/night-shift.svg#gh-dark-mode-only" alt="Night Shift: 2% (1 of 50)"><img src="assets/trophies/achievements/night-shift-day.svg#gh-light-mode-only" alt="Night Shift: 2% (1 of 50)">
  <img src="assets/trophies/achievements/weekly-beat.svg#gh-dark-mode-only" alt="Weekly Beat: 1% (1 of 52)"><img src="assets/trophies/achievements/weekly-beat-day.svg#gh-light-mode-only" alt="Weekly Beat: 1% (1 of 52)">
  <img src="assets/trophies/achievements/big-week.svg#gh-dark-mode-only" alt="Big Week: 1% (1 of 100)"><img src="assets/trophies/achievements/big-week-day.svg#gh-light-mode-only" alt="Big Week: 1% (1 of 100)">
  <img src="assets/trophies/achievements/comeback.svg#gh-dark-mode-only" alt="Comeback: 0% (0 of 1)"><img src="assets/trophies/achievements/comeback-day.svg#gh-light-mode-only" alt="Comeback: 0% (0 of 1)">
  <img src="assets/trophies/achievements/friday-deploy.svg#gh-dark-mode-only" alt="Friday Deploy: 0% (0 of 1)"><img src="assets/trophies/achievements/friday-deploy-day.svg#gh-light-mode-only" alt="Friday Deploy: 0% (0 of 1)">
  <img src="assets/trophies/achievements/monthly-release.svg#gh-dark-mode-only" alt="Monthly Release: 0% (0 of 12)"><img src="assets/trophies/achievements/monthly-release-day.svg#gh-light-mode-only" alt="Monthly Release: 0% (0 of 12)">
  <img src="assets/trophies/achievements/same-day-fix.svg#gh-dark-mode-only" alt="Same-Day Fix: 0% (0 of 10)"><img src="assets/trophies/achievements/same-day-fix-day.svg#gh-light-mode-only" alt="Same-Day Fix: 0% (0 of 10)">
  <img src="assets/trophies/achievements/weekend-project.svg#gh-dark-mode-only" alt="Weekend Project: 0% (0 of 26)"><img src="assets/trophies/achievements/weekend-project-day.svg#gh-light-mode-only" alt="Weekend Project: 0% (0 of 26)">
</p>

<p align="center"><b>Secret</b></p>
<p align="center">
  <img src="assets/trophies/achievements/birthday.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/birthday-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/constellation.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/constellation-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/friday-the-13th.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/friday-the-13th-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/full-house.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/full-house-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/ghost.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/ghost-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/green-wall.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/green-wall-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/leap-day.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/leap-day-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/midnight-oil.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/midnight-oil-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/new-year.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/new-year-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/palindrome.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/palindrome-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/round-number.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/round-number-day.svg#gh-light-mode-only" alt="Secret achievement">
  <img src="assets/trophies/achievements/the-answer.svg#gh-dark-mode-only" alt="Secret achievement"><img src="assets/trophies/achievements/the-answer-day.svg#gh-light-mode-only" alt="Secret achievement">
</p>

</details>

<p align="center"><sub>Refreshed daily by <a href="https://github.com/tannergolden/trophies">tannergolden/trophies</a></sub></p>
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

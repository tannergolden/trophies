# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Streaks, weeks and anniversaries over a hand-built calendar."""
from __future__ import annotations

import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trophykit import calendar as cal  # noqa: E402
from trophykit.scan import CONVENTIONAL, EMOJI, SEMVER, classify, empty_stats  # noqa: E402

D = dt.date


def days(*spans):
    """Build {date: 1} from (start, length) spans."""
    out = {}
    for start, n in spans:
        for i in range(n):
            out[start + dt.timedelta(days=i)] = 1
    return out


class Streaks(unittest.TestCase):
    def test_longest_streak(self):
        self.assertEqual(cal.longest_streak(days((D(2026, 1, 1), 5), (D(2026, 2, 1), 9))), 9)
        self.assertEqual(cal.longest_streak({}), 0)

    def test_current_streak_allows_today_not_yet_done(self):
        d = days((D(2026, 9, 20), 4))  # 20..23
        self.assertEqual(cal.current_streak(d, D(2026, 9, 24)), 4)
        self.assertEqual(cal.current_streak(d, D(2026, 9, 23)), 4)
        self.assertEqual(cal.current_streak(d, D(2026, 9, 26)), 0)

    def test_gaps_and_comebacks(self):
        d = days((D(2025, 1, 1), 1), (D(2025, 5, 1), 1))
        self.assertTrue(cal.came_back_after(d, 90))
        self.assertFalse(cal.came_back_after(d, 365))


class Periods(unittest.TestCase):
    def test_perfect_month_and_seasons(self):
        d = days((D(2026, 2, 1), 28))
        self.assertEqual(cal.perfect_months(d), 1)
        self.assertFalse(cal.all_twelve_months(d))
        year = days((D(2026, 1, 1), 365))
        self.assertTrue(cal.all_twelve_months(year))
        self.assertEqual(cal.max_days_in_a_year(year), 365)

    def test_weekends_and_weekdays(self):
        d = days((D(2026, 1, 1), 365))
        self.assertGreaterEqual(cal.weekends_in_a_year(d), 52)
        self.assertGreaterEqual(cal.weekdays_in_a_year(d), 260)

    def test_every_week_of_a_completed_year_only(self):
        d = days((D(2025, 1, 1), 365))
        self.assertTrue(cal.every_week_of_a_year(d, D(2026, 9, 24)))
        self.assertFalse(cal.every_week_of_a_year(days((D(2026, 1, 1), 265)), D(2026, 9, 24)))

    def test_special_dates(self):
        d = {D(2024, 2, 29): 1, D(2026, 1, 1): 1, D(2026, 2, 13): 1}
        self.assertTrue(cal.on_date(d, 2, 29))
        self.assertTrue(cal.on_date(d, 1, 1))
        self.assertTrue(cal.on_friday_13th(d))
        self.assertTrue(cal.on_anniversary(d, D(2020, 1, 1)))
        self.assertFalse(cal.on_anniversary(d, D(2026, 1, 1)))

    def test_consecutive_weeks_and_months(self):
        d = days((D(2026, 1, 5), 7 * 10))
        self.assertEqual(cal.consecutive_weeks(cal.weeks_of(d)), 10)
        self.assertEqual(cal.consecutive_months({(2026, 1), (2026, 2), (2026, 4)}), 2)

    def test_max_in_periods(self):
        d = {D(2026, 3, 2): 40, D(2026, 3, 3): 70, D(2026, 3, 10): 5}
        self.assertEqual(cal.max_in_a_day(d), 70)
        self.assertEqual(cal.max_in_a_week(d), 110)
        self.assertEqual(cal.max_in_a_month(d), 115)


class Scanner(unittest.TestCase):
    def test_message_patterns(self):
        self.assertTrue(CONVENTIONAL.match("feat(scope)!: add"))
        self.assertTrue(CONVENTIONAL.match("fix: it"))
        self.assertFalse(CONVENTIONAL.match("Fixed it"))
        self.assertTrue(EMOJI.match("\U0001F389 initialise"))
        self.assertTrue(EMOJI.match(":tada: initialise"))
        self.assertTrue(SEMVER.match("v1.2.3"))
        self.assertTrue(SEMVER.match("2.0.0-rc.1"))
        self.assertFalse(SEMVER.match("v1"))

    def test_classify_counts_what_it_should(self):
        st = empty_stats()
        classify({"message": "fix: \U0001F41B squash", "author": {"date": "2026-03-01T03:12:00-05:00", "user": {"login": "octo"}},
                  "signature": {"isValid": True}, "authors": {"totalCount": 2}, "changedFilesIfAvailable": 1, "additions": 900, "deletions": 200}, st)
        classify({"message": "Revert \"fix\"", "author": {"date": "2026-03-01T00:00:00Z", "user": None, "name": "bot"},
                  "signature": None, "authors": {"totalCount": 1}, "changedFilesIfAvailable": 60, "additions": 1, "deletions": 1}, st)
        self.assertEqual((st["total"], st["conventional"], st["fix"], st["emoji"], st["signed"], st["coauthored"]), (2, 1, 1, 0, 1, 1))
        self.assertEqual((st["onefile"], st["heavy"], st["sweeping"], st["night"], st["midnight"], st["revert"]), (1, 1, 1, 2, 1, 1))
        self.assertEqual(st["days"], ["2026-03-01"])
        self.assertEqual(st["authors"], {"octo": 1, "bot": 1})

    def test_refresh_commits_are_set_aside(self):
        from trophykit.scan import merge_stats, without_refreshes
        st = empty_stats()
        classify({"message": "chore(trophies): \U0001F3C6 reach Gold in Commits", "author": {"date": "2026-03-02T00:00:00Z", "user": {"login": "tannergolden"}},
                  "changedFilesIfAvailable": 220, "additions": 5000, "deletions": 5000}, st)
        classify({"message": "feat: real work", "author": {"date": "2026-03-02T09:00:00Z", "user": {"login": "tannergolden"}},
                  "changedFilesIfAvailable": 1, "additions": 1, "deletions": 0}, st)
        self.assertEqual((st["refresh"], st["total"], st["midnight"], st["sweeping"], st["heavy"]), (1, 1, 0, 0, 0))
        self.assertEqual(st["refresh_days"], {"2026-03-02": 1})
        self.assertEqual(st["authors"], {"tannergolden": 1})
        merged = merge_stats([{"stats": st}, {"stats": st}])
        self.assertEqual((merged["refresh"], merged["refresh_days"]), (2, {"2026-03-02": 2}))
        days = {D(2026, 3, 2): 3, D(2026, 3, 3): 1}
        self.assertEqual(without_refreshes(days, merged), {D(2026, 3, 2): 1, D(2026, 3, 3): 1})
        self.assertEqual(without_refreshes({D(2026, 3, 2): 2}, merged), {})


if __name__ == "__main__":
    unittest.main()

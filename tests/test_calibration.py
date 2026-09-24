# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Every threshold and rarity is pinned to a share of a reference population."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trophykit import art, calibration as cal, catalogue as c  # noqa: E402


class Coverage(unittest.TestCase):
    def test_every_achievement_has_a_share_and_nothing_else_does(self):
        for mode, ach in (("profile", c.ACH), ("repository", c.RACH)):
            slugs = {a.slug for a in ach}
            self.assertEqual(set(cal.SHARE[mode]), slugs, mode)
            for a in ach:
                self.assertEqual(len(cal.shares(mode, a.slug)), len(a.tiers), a.slug)
                self.assertIn(cal.basis(mode, a.slug), cal.BASIS_NAMES)

    def test_every_core_has_anchors_on_its_steps(self):
        for mode, cores in (("profile", c.CORE), ("repository", c.RCORE)):
            for core in cores:
                pts, b, note = cal.CORE_PCT[(mode, core.key)]
                self.assertEqual(tuple(x for x, _ in pts), tuple(core.steps), core.key)
                shares = [p for _, p in pts]
                self.assertEqual(shares, sorted(shares, reverse=True), core.key)
                self.assertIn(b, cal.BASIS_NAMES)
                self.assertTrue(note)


class RarityFollowsTheShare(unittest.TestCase):
    def test_bands(self):
        self.assertEqual([cal.rarity_of(x) for x in (100, 40, 39.9, 15, 14.9, 4, 3.9, 1, 0.9, 0)], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    def test_every_rarity_in_the_catalogue_is_its_share_banded(self):
        for mode, ach in (("profile", c.ACH), ("repository", c.RACH)):
            for a in ach:
                self.assertEqual(a.rarities, tuple(cal.rarity_of(x) for x in cal.shares(mode, a.slug)), a.slug)

    def test_a_higher_tier_is_never_more_common(self):
        for mode, ach in (("profile", c.ACH), ("repository", c.RACH)):
            for a in ach:
                sh = cal.shares(mode, a.slug)
                self.assertEqual(list(sh), sorted(sh, reverse=True), a.slug)


class TheChip(unittest.TestCase):
    def test_measured_followers(self):
        f = next(k for k in c.CORE if k.key == "followers")
        self.assertAlmostEqual(art.top_pct(f, 25), 57.96)
        self.assertAlmostEqual(art.top_pct(f, 1000), 3.35)
        self.assertEqual(art.top_pct(f, 0), 100.0)

    def test_between_and_beyond_anchors(self):
        f = next(k for k in c.CORE if k.key == "followers")
        self.assertTrue(29.03 < art.top_pct(f, 50) < 57.96)
        self.assertTrue(art.top_pct(f, 100000) < 0.2)
        self.assertGreaterEqual(art.top_pct(f, 10**9), 0.001)

    def test_modes_that_share_a_key_read_their_own_anchors(self):
        pc = next(k for k in c.CORE if k.key == "commits")
        rc = next(k for k in c.RCORE if k.key == "commits")
        self.assertNotEqual(art.top_pct(pc, 500), art.top_pct(rc, 500))

    def test_label_formats(self):
        self.assertEqual(art.pct_label(57.96), "TOP 58%")
        self.assertEqual(art.pct_label(3.35), "TOP 3.4%")
        self.assertEqual(art.pct_label(1.0), "TOP 1%")
        self.assertEqual(art.pct_label(0.081), "TOP 0.081%")
        self.assertEqual(art.pct_label(0.001), "TOP 0.001%")


if __name__ == "__main__":
    unittest.main()

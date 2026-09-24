# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The catalogue's promises: exactly one hundred public achievements a mode,
unique slugs, valid icons and tokens, and tier arithmetic that holds."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trophykit import catalogue as c  # noqa: E402


class CatalogueShape(unittest.TestCase):
    def test_exactly_one_hundred_public_achievements_per_mode(self):
        self.assertEqual(len([a for a in c.ACH if not a.only]), 100)
        self.assertEqual(len([a for a in c.RACH if not a.only]), 100)

    def test_owner_only_entries_name_their_repository(self):
        makers = [a for a in c.ACH if a.only]
        self.assertEqual({a.only for a in makers},
                         {"tannergolden/trophies", "tannergolden/emblems", "tannergolden/standards", "tannergolden/path"})

    def test_slugs_unique_and_url_safe(self):
        for ach in (c.ACH, c.RACH):
            slugs = [a.slug for a in ach]
            self.assertEqual(len(slugs), len(set(slugs)))
            for s in slugs:
                self.assertRegex(s, r"^[a-z0-9]+(-[a-z0-9]+)*$")

    def test_every_icon_and_token_exists(self):
        for a in c.ACH + c.RACH:
            self.assertIn(a.icon, c.ICONS, a.name)
            self.assertIn(a.tok, c.PAL, a.name)
        for core in c.CORE + c.RCORE:
            self.assertIn(core.icon, c.ICONS)
            self.assertIn(core.tok, c.PAL)

    def test_tiered_entries_have_one_rarity_per_tier(self):
        for a in c.ACH + c.RACH:
            self.assertEqual(len(a.tiers), len(a.rarities), a.name)
            self.assertEqual(list(a.tiers), sorted(a.tiers), a.name)

    def test_eight_core_trophies_with_rising_thresholds(self):
        for cores in (c.CORE, c.RCORE):
            self.assertEqual(len(cores), 8)
            for core in cores:
                self.assertEqual(list(core.steps), sorted(core.steps))


class Measured(unittest.TestCase):
    """Every achievement has a line in its mode's measurer.

    The measurers need GitHub to run, so this reads their source: a slug
    that never appears as a key there is one a live run would refuse."""

    def test_every_profile_achievement_is_measured(self):
        src = (Path(__file__).resolve().parents[1] / "src/trophykit/measure_profile.py").read_text(encoding="utf-8")
        self.assertEqual([a.slug for a in c.ACH if f'"{a.slug}"' not in src], [])

    def test_every_repository_achievement_is_measured(self):
        src = (Path(__file__).resolve().parents[1] / "src/trophykit/measure_repo.py").read_text(encoding="utf-8")
        self.assertEqual([a.slug for a in c.RACH if f'"{a.slug}"' not in src], [])


class TierMaths(unittest.TestCase):
    def test_measure_walks_the_tiers(self):
        core = c.CORE[0]  # commits: 100, 500, 2000, 5000, 10000
        self.assertEqual(c.measure(core, 0)["t"], 0)
        self.assertEqual(c.measure(core, 99)["next"], "Bronze")
        self.assertEqual(c.measure(core, 100)["t"], 1)
        self.assertEqual(c.measure(core, 3610)["t"], 3)
        self.assertAlmostEqual(c.measure(core, 3610)["pct"], (3610 - 2000) / 3000)

    def test_stars_past_diamond_double_each_time(self):
        core = c.CORE[0]
        self.assertEqual(c.measure(core, 10000)["stars"], 0)
        self.assertEqual(c.measure(core, 20000)["stars"], 1)
        self.assertEqual(c.measure(core, 23500)["next"], "star 2")
        self.assertEqual(c.measure(core, 320000)["stars"], 5)
        self.assertIsNone(c.measure(core, 320000)["next"])

    def test_ach_state_tiers(self):
        poly = next(a for a in c.ACH if a.name == "Polyglot")  # 5, 10, 20
        st = c.ach_state(poly, 12)
        self.assertTrue(st["earned"])
        self.assertEqual((st["k"], st["tier"], st["next_tier"], st["next"]), (2, "II", "III", 20))
        self.assertEqual(st["rarity"], 3)
        self.assertFalse(st["done"])
        self.assertTrue(c.ach_state(poly, 20)["done"])
        self.assertFalse(c.ach_state(poly, 4)["earned"])

    def test_unmeasured_is_not_earned_and_not_secret_leaking(self):
        secret = next(a for a in c.ACH if a.secret)
        st = c.ach_state(secret, None)
        self.assertFalse(st["measured"])
        self.assertTrue(st["secret"])

    def test_secret_reveals_once_earned(self):
        secret = next(a for a in c.ACH if a.secret)
        self.assertFalse(c.ach_state(secret, 1)["secret"])


if __name__ == "__main__":
    unittest.main()

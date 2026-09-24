# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The renderer's contract: deterministic, self-contained SVG, sized for a
phone, with the lettering embedded and no date anywhere."""
from __future__ import annotations

import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trophykit import art, catalogue as c, sample, styles  # noqa: E402,F401


def parse(svg: str):
    return ET.fromstring(svg)


class Cards(unittest.TestCase):
    def test_every_style_is_well_formed_xml_in_both_cases(self):
        for name, fn in art.STYLES.items():
            for theme in (art.NIGHT, art.DAY):
                for v in (0, 42, 3610, 23500):
                    svg = fn(theme, c.CORE[0], v, {"rank": True, "delta": 7, "new": True})
                    root = parse(svg)
                    self.assertTrue(root.tag.endswith("svg"), name)

    def test_cards_declare_the_phone_size_on_the_design_viewbox(self):
        svg = art.STYLES["trophy"](art.NIGHT, c.CORE[0], 3610)
        root = parse(svg)
        self.assertEqual((root.get("width"), root.get("height"), root.get("viewBox")), ("164", "222", "0 0 180 244"))

    def test_deterministic(self):
        a = art.crest(art.DAY, c.CORE[4], 312, {"rank": True, "delta": 9})
        b = art.crest(art.DAY, c.CORE[4], 312, {"rank": True, "delta": 9})
        self.assertEqual(a, b)

    def test_no_external_references_and_no_text_elements(self):
        svg = art.crest(art.NIGHT, c.CORE[0], 5730, {"rank": True})
        self.assertNotIn("http://", svg.replace('xmlns="http://www.w3.org/2000/svg"', ""))
        self.assertNotIn("<text", svg)
        self.assertNotIn("@font-face", svg)
        self.assertNotIn("<script", svg)

    def test_glyphs_embedded_once_and_used(self):
        svg = art.crest(art.NIGHT, c.CORE[0], 5730)
        ids = re.findall(r'<path id="([snm]\d+)"', svg)
        self.assertEqual(len(ids), len(set(ids)))
        for gid in ids:
            self.assertIn(f'href="#{gid}"', svg)

    def test_alt_text_says_tier_value_and_progress(self):
        svg = art.crest(art.NIGHT, c.CORE[0], 5730, {"rank": True, "delta": 124, "new": True})
        label = parse(svg).get("aria-label")
        self.assertIn("Platinum", label)
        self.assertIn("5,730", label)
        self.assertIn("to Diamond", label)
        self.assertIn("up 124 this week", label)
        self.assertIn("newly reached", label)

    def test_version_stamp_present(self):
        svg = art.crest(art.NIGHT, c.CORE[0], 5730)
        self.assertIn("<!--trophy-kit v", svg)

    def test_animation_only_from_gold_and_respects_reduced_motion(self):
        silver = art.crest(art.NIGHT, c.CORE[0], 1240)
        gold = art.crest(art.NIGHT, c.CORE[0], 3610)
        self.assertNotIn("<style", silver)
        self.assertIn("prefers-reduced-motion", gold)


class Pins(unittest.TestCase):
    def test_every_state_renders(self):
        poly = next(a for a in c.ACH if a.name == "Polyglot")
        for cur in (None, 0, 3, 5, 12, 20, 99):
            parse(art.pin(art.NIGHT, poly, cur))

    def test_secret_shows_question_marks_until_earned(self):
        secret = next(a for a in c.ACH if a.secret)
        hidden = art.pin(art.NIGHT, secret, 0)
        shown = art.pin(art.NIGHT, secret, 1)
        self.assertEqual(parse(hidden).get("aria-label"), "Secret achievement")
        self.assertIn(secret.name, parse(shown).get("aria-label"))

    def test_tier_numeral_in_label(self):
        poly = next(a for a in c.ACH if a.name == "Polyglot")
        self.assertIn("Polyglot II", parse(art.pin(art.DAY, poly, 12)).get("aria-label"))


class Banners(unittest.TestCase):
    def test_level_and_next_up_render_for_both_samples(self):
        for mode, s in sample.SAMPLES.items():
            cores, ach = c.MODES[mode]["core"], c.MODES[mode]["ach"]
            lv = art.level_card(art.NIGHT, cores, s["values"], ach, s["curs"], s["subject"], ("flame", "#FF0000", "12-DAY STREAK", " x"))
            nu = art.next_up_card(art.DAY, cores, s["values"], ach, s["curs"])
            self.assertIn("level", parse(lv).get("aria-label"))
            self.assertTrue(parse(nu).get("aria-label").startswith("Next up: "))

    def test_long_subject_still_fits(self):
        s = sample.PROFILE
        svg = art.level_card(art.NIGHT, c.CORE, s["values"], c.ACH, s["curs"], "a-very-long-organization-name/toolkit", ("tag", "#000", "X", ""))
        parse(svg)

    def test_next_up_skips_passive_and_secret(self):
        s = sample.PROFILE
        items = art.next_up_items(c.CORE, s["values"], c.ACH, s["curs"], 200)
        names = {i["name"].split(" ")[0] for i in items}
        self.assertNotIn("Veteran", names)
        self.assertNotIn("Leap", names)


if __name__ == "__main__":
    unittest.main()

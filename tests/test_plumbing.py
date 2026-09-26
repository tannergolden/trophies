# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Config, ledger, README block and the render plan, end to end without a network."""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from trophykit import KIT_VERSION  # noqa: E402
from trophykit import catalogue as c, config, ledger, readme, render, sample  # noqa: E402

KIT = [sys.executable, str(ROOT / "src" / "trophy-kit.py")]


class Config(unittest.TestCase):
    def test_defaults(self):
        cfg = config.load(None)
        self.assertEqual((cfg["mode"], cfg["style"], cfg["case"]), ("profile", "trophy", "both"))

    def test_reader_handles_the_documented_shapes(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "t.yml"
            p.write_text("mode: repository # comment\nstyle: crest\ncore: [stars, forks]\nenamel: {stars: amber}\ncard:\n  - rank\n  - new\nscan_pages: 5\n")
            cfg = config.load(p)
            self.assertEqual(cfg["mode"], "repository")
            self.assertEqual(cfg["core"], ["stars", "forks"])
            self.assertEqual(cfg["enamel"], {"stars": "amber"})
            self.assertEqual(cfg["card"], ["rank", "new"])
            self.assertEqual(cfg["scan_pages"], 5)

    def test_unknown_key_and_bad_value_fail_loudly(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "t.yml"
            p.write_text("colour: red\n")
            with self.assertRaises(config.ConfigError):
                config.load(p)
            p.write_text("style: neon\n")
            with self.assertRaises(config.ConfigError):
                config.load(p)
            p.write_text("mode: profile\ncore: [stars, forks]\n")
            with self.assertRaises(config.ConfigError):
                config.load(p)  # forks is a repository trophy


class Ledger(unittest.TestCase):
    def test_new_ribbon_for_seven_days_then_quiet(self):
        led = ledger.load(Path("/nonexistent/trophies.lock.json"))
        result = json.loads(json.dumps(sample.PROFILE))
        today = dt.date(2026, 9, 24)
        f = ledger.update(led, result, c.CORE, c.ACH, today)
        self.assertTrue(f["new"]["commits"])
        f = ledger.update(led, result, c.CORE, c.ACH, today + dt.timedelta(days=8))
        self.assertFalse(f["new"]["commits"])

    def test_history_is_sparse_and_weekly_delta_uses_it(self):
        led = ledger.load(Path("/nonexistent"))
        result = json.loads(json.dumps(sample.PROFILE))
        d0 = dt.date(2026, 9, 1)
        ledger.update(led, result, c.CORE, c.ACH, d0)
        ledger.update(led, result, c.CORE, c.ACH, d0 + dt.timedelta(days=1))  # unchanged: no new point
        self.assertEqual(len(led["history"]["commits"]), 1)
        result["values"]["commits"] += 50
        f = ledger.update(led, result, c.CORE, c.ACH, d0 + dt.timedelta(days=8))
        self.assertEqual(f["delta"]["commits"], 50)

    def test_remember_keeps_what_check_needs(self):
        result = json.loads(json.dumps(sample.PROFILE))
        result["scan"] = {"huge": "cache"}
        led = {}
        ledger.remember(led, result)
        self.assertEqual(set(ledger.last(led)) <= set(ledger.LAST_KEYS), True)
        self.assertNotIn("scan", ledger.last(led))
        self.assertEqual(ledger.last(led)["values"], result["values"])
        self.assertIsNone(ledger.last({}))

    def test_save_only_when_changed(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "l.json"
            led = ledger.load(p)
            self.assertTrue(ledger.save(p, led))
            self.assertFalse(ledger.save(p, led))


class Readme(unittest.TestCase):
    def test_first_run_appends_then_replaces_between_markers(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "README.md"
            p.write_text("# Hi\n\nintro\n")
            self.assertTrue(readme.apply(p, f"{readme.START}\nA\n{readme.END}"))
            text = p.read_text()
            self.assertTrue(text.startswith("# Hi\n\nintro\n\n"))
            self.assertTrue(readme.apply(p, f"{readme.START}\nB\n{readme.END}"))
            text = p.read_text()
            self.assertIn("B", text)
            self.assertNotIn("\nA\n", text)
            self.assertEqual(text.count(readme.START), 1)
            self.assertFalse(readme.apply(p, f"{readme.START}\nB\n{readme.END}"))

    def test_picture_is_the_default_and_fragment_still_exists(self):
        cfg = config.load(None)
        planned = render.plan(json.loads(json.dumps(sample.PROFILE)), cfg)
        self.assertIn("<picture>", planned["readme"])
        self.assertNotIn("#gh-dark-mode-only", planned["readme"])
        cfg["theme"] = "fragment"
        planned = render.plan(json.loads(json.dumps(sample.PROFILE)), cfg)
        self.assertIn("#gh-dark-mode-only", planned["readme"])

    def test_every_card_links_to_its_catalogue_entry(self):
        planned = render.plan(json.loads(json.dumps(sample.PROFILE)), config.load(None))
        block = planned["readme"]
        self.assertIn(f'href="{readme.CATALOGUE}#profile-commits"', block)
        self.assertIn(f'href="{readme.CATALOGUE}#profile-polyglot"', block)
        self.assertIn(f'href="{readme.CATALOGUE}#profile">the catalogue</a>', block)
        self.assertNotIn("blob/v1/", block)


class ReachedToday(unittest.TestCase):
    def test_a_tier_lost_to_a_raised_threshold_is_not_reported(self):
        import datetime as dt
        cores = [next(k for k in c.CORE if k.key == "followers")]
        today = dt.date(2026, 9, 24)
        result = {"values": {"followers": 13}, "curs": {}}
        led = {"reached": {"followers": {"1.0": "2026-09-24"}}}  # Bronze recorded when Bronze was 10; now it is 25
        self.assertEqual(ledger.reached_on(led, result, cores, [], today)["tiers"], [])
        result["values"]["followers"] = 30
        self.assertEqual(ledger.reached_on(led, result, cores, [], today)["tiers"], [("Bronze", "Followers")])
        led["reached"]["followers"]["1.0"] = "2026-09-20"
        self.assertEqual(ledger.reached_on(led, result, cores, [], today)["tiers"], [])


class Plan(unittest.TestCase):
    def test_owner_only_pins_appear_only_for_the_owner(self):
        cfg = config.load(None)
        result = json.loads(json.dumps(sample.PROFILE))
        planned = render.plan(result, cfg, {})
        self.assertEqual(planned["total"], 100)
        owners = {a.only: "octo-dev" for a in c.ACH if a.only}
        planned = render.plan(result, cfg, owners)
        self.assertEqual(planned["total"], 104)
        self.assertIn("assets/trophies/achievements/trophy-maker.svg", planned["files"])

    def test_core_subset_and_enamel(self):
        cfg = config.load(None)
        cfg["core"] = ["stars", "commits"]
        cfg["enamel"] = {"stars": "crimson"}
        planned = render.plan(json.loads(json.dumps(sample.PROFILE)), cfg, {})
        cores = [k for k in ("stars", "commits", "pulls") if f"assets/trophies/{k}.svg" in planned["files"]]
        self.assertEqual(cores, ["stars", "commits"])
        self.assertIn(c.PAL["crimson"], planned["files"]["assets/trophies/stars.svg"])

    def test_write_then_check_is_clean_and_prunes(self):
        cfg = config.load(None)
        planned = render.plan(json.loads(json.dumps(sample.PROFILE)), cfg, {})
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            orphan = root / "assets/trophies/orphan.svg"
            orphan.parent.mkdir(parents=True)
            orphan.write_text("<svg/>")
            changed = render.write(root, planned)
            self.assertFalse(orphan.exists())
            self.assertIn("assets/trophies/orphan.svg", changed)
            self.assertEqual(render.check(root, planned), [])
            (root / "assets/trophies/commits.svg").write_text(f"<!--trophy-kit v{KIT_VERSION} night--><svg/>")
            self.assertEqual(render.check(root, planned), ["assets/trophies/commits.svg"])
            (root / "assets/trophies/commits.svg").write_text("<!--trophy-kit v0 night--><svg/>")
            self.assertEqual(render.check(root, planned), [])  # another version: tolerated

    def test_cli_check_reads_the_ledgers_last_measurement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = subprocess.run(KIT + ["preview", "--root", tmp, "--mode", "repository", "--today", "2026-09-24"], capture_output=True, text=True)
            self.assertEqual(out.returncode, 0, out.stderr)
            lock = root / ".github" / "trophies.lock.json"
            self.assertEqual(set(json.loads(lock.read_text())), {"version", "last"})  # a preview remembers, nothing more
            lock.unlink()
            chk = subprocess.run(KIT + ["check", "--root", tmp, "--mode", "repository"], capture_output=True, text=True)
            self.assertEqual(chk.returncode, 2, chk.stdout)  # nothing remembered
            led = {}
            ledger.remember(led, json.loads(json.dumps(sample.SAMPLES["repository"])))
            ledger.save(root / ".github" / "trophies.lock.json", led)
            chk = subprocess.run(KIT + ["check", "--root", tmp, "--mode", "repository"], capture_output=True, text=True)
            self.assertEqual(chk.returncode, 0, chk.stdout + chk.stderr)
            self.assertIn("README block current", chk.stdout)
            page = root / "README.md"
            page.write_text(page.read_text().replace(readme.END, "hand edit\n" + readme.END))
            chk = subprocess.run(KIT + ["check", "--root", tmp, "--mode", "repository"], capture_output=True, text=True)
            self.assertEqual(chk.returncode, 1)
            self.assertIn("README.md (block differs)", chk.stdout)
            page.write_text("no markers")
            chk = subprocess.run(KIT + ["check", "--root", tmp, "--mode", "repository"], capture_output=True, text=True)
            self.assertIn("README.md (markers missing)", chk.stdout)
            chk = subprocess.run(KIT + ["check", "--root", tmp, "--mode", "profile"], capture_output=True, text=True)
            self.assertEqual(chk.returncode, 2, chk.stdout)  # another mode's memory is not this case's

    def test_cli_preview_and_check_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = subprocess.run(KIT + ["preview", "--root", tmp, "--mode", "repository", "--today", "2026-09-24"], capture_output=True, text=True)
            self.assertEqual(out.returncode, 0, out.stderr)
            self.assertIn("repository case for octo-dev/toolkit", out.stdout)
            self.assertTrue((Path(tmp) / "README.md").exists())
            chk = subprocess.run(KIT + ["check", "--root", tmp, "--mode", "repository", "--today", "2026-09-24"], capture_output=True, text=True)
            self.assertEqual(chk.returncode, 0, chk.stdout + chk.stderr)


if __name__ == "__main__":
    unittest.main()


class CommitMessage(unittest.TestCase):
    def _msg(self, day, changed, reached, run):
        cfg = config.load(None)
        result = json.loads(json.dumps(sample.PROFILE))
        planned = render.plan(result, cfg, {})
        return render.commit_message(planned, result, changed, day, reached, run)

    def test_conventional_shape_and_no_em_dash(self):
        msg = self._msg(dt.date(2026, 9, 24), ["assets/trophies/commits.svg"], {"tiers": [("Platinum", "Commits")], "achievements": []}, "1")
        subject, blank, body = msg.split("\n", 2)
        self.assertRegex(subject, r"^chore\(trophies\): \U0001F3C6 [a-z]")
        self.assertLessEqual(len(subject), 72)
        self.assertEqual(blank, "")
        self.assertTrue(body.strip())
        self.assertNotIn("\u2014", msg)  # the em dash, by code point
        self.assertTrue(all(len(line) <= 72 for line in body.splitlines()))

    def test_two_runs_never_read_alike(self):
        a = self._msg(dt.date(2026, 9, 24), ["assets/trophies/stars.svg"], {"tiers": [], "achievements": []}, "100")
        b = self._msg(dt.date(2026, 9, 25), ["assets/trophies/stars.svg"], {"tiers": [], "achievements": []}, "101")
        self.assertNotEqual(a, b)
        self.assertIn("2026-09-24", a)
        self.assertIn("run 101", b)

    def test_subject_prefers_a_tier_then_an_achievement_then_movement(self):
        tier = self._msg(dt.date(2026, 9, 24), [], {"tiers": [("Gold", "Stars Earned")], "achievements": ["Polyglot II"]}, "1")
        ach = self._msg(dt.date(2026, 9, 24), [], {"tiers": [], "achievements": ["Polyglot II"]}, "1")
        move = self._msg(dt.date(2026, 9, 24), [], {"tiers": [], "achievements": []}, "1")
        self.assertIn("reach Gold on Stars Earned", tier.splitlines()[0])
        self.assertIn("earn Polyglot II", ach.splitlines()[0])
        self.assertIn("commits +124", move.splitlines()[0])

# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The repository sampler's arithmetic, and how its file reaches the calibration."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import calibrate  # noqa: E402
from trophykit import calibration as cal, catalogue as c  # noqa: E402


class Arithmetic(unittest.TestCase):
    def test_link_header_gives_the_count(self):
        link = '<https://api.github.com/repositories/1/commits?per_page=1&page=2>; rel="next", <https://api.github.com/repositories/1/commits?per_page=1&page=1234>; rel="last"'
        self.assertEqual(calibrate.link_last(link), 1234)
        self.assertIsNone(calibrate.link_last(""))

    def test_band_queries(self):
        self.assertEqual(calibrate.band_query(10, 99), "stars:10..99")
        self.assertEqual(calibrate.band_query(10000, None), "stars:>=10000")
        self.assertEqual(calibrate.BANDS[0][0], 1)
        self.assertIsNone(calibrate.BANDS[-1][1])

    def test_stratified_shares_weight_by_band_and_never_rise(self):
        bands = [
            {"weight": 0.9, "repos": [{"commits": 5}, {"commits": 150}]},
            {"weight": 0.1, "repos": [{"commits": 3000}]},
            {"weight": 0.5, "repos": []},  # an empty band contributes nothing and takes no weight
        ]
        out = calibrate.estimate(bands, {"commits": (100, 500, 2000, 5000)})
        self.assertEqual(out["commits"], [[100, 55.0], [500, 10.0], [2000, 10.0], [5000, 0.0]])
        noisy = [{"weight": 1.0, "repos": [{"commits": 600}, {"commits": None}]}]
        self.assertEqual(calibrate.estimate(noisy, {"commits": (100, 500)})["commits"], [[100, 100.0], [500, 100.0]])

    def test_exact_shares_from_the_population_counts(self):
        pop = {"base": 1000, "stars": {"10": 250, "100": 40, "500": 45}}
        self.assertEqual(calibrate.exact_shares(pop, "stars", (10, 100, 500)), [[10, 25.0], [100, 4.0], [500, 4.0]])

    def test_the_measured_keys_are_repository_cores(self):
        keys = {x.key for x in c.RCORE}
        self.assertTrue(set(calibrate.MEASURED) <= keys)
        self.assertNotIn("active", calibrate.MEASURED)  # cannot be read from the API


class Loader(unittest.TestCase):
    def setUp(self):
        self.saved = dict(cal.CORE_PCT)

    def tearDown(self):
        cal.CORE_PCT.clear()
        cal.CORE_PCT.update(self.saved)

    def _sample(self, cores):
        return {"date": "2026-10-01", "base": 38000000, "n": 200,
                "bands": [{"band": "1-9", "weight": 0.9, "population": 1, "sampled": 40}],
                "cores": cores}

    def test_missing_file_leaves_the_estimates(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(cal.load_repository_sample(Path(tmp) / "none.json"))
        self.assertEqual(cal.CORE_PCT[("repository", "stars")][1], "e")

    def test_matching_steps_become_measured_and_mismatched_are_ignored(self):
        stars = [x for x in c.RCORE if x.key == "stars"][0]
        anchors = [[t, p] for t, p in zip(stars.steps, (9.0, 1.2, 0.3, 0.05, 0.01))]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "repositories.json"
            path.write_text(json.dumps(self._sample({
                "stars": {"anchors": anchors},
                "commits": {"anchors": [[1, 50.0], [2, 40.0]]},  # not the catalogue's steps: stale sample
                "nonsense": {"anchors": [[1, 1.0]]},
            })))
            data = cal.load_repository_sample(path)
        self.assertEqual(data["n"], 200)
        pts, basis, note = cal.CORE_PCT[("repository", "stars")]
        self.assertEqual(basis, "m")
        self.assertEqual(pts, tuple((int(t), float(p)) for t, p in anchors))
        self.assertIn("2026-10-01", note)
        self.assertEqual(cal.CORE_PCT[("repository", "commits")][1], "e")
        self.assertNotIn(("repository", "nonsense"), cal.CORE_PCT)


if __name__ == "__main__":
    unittest.main()

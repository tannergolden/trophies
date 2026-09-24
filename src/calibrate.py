#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Measure the repository population the repository-mode tiers are set against.

The catalogue says a Bronze in stars is the top 10% of starred public
repositories, and until this ran that figure was a model. This asks
GitHub: it counts the population directly where the search API can count
it (stars, forks: `stars:>=N` answers with a total), and where it cannot
(contributors, commits, releases, merged pull requests, resolved issues)
it samples repositories from each star band, measures each one the way
the kit measures a case, and weights the bands by their population.

Stratified by star band on purpose. A uniform sample of starred
repositories is almost entirely one-star repositories, so it could never
see the tail where Diamond lives; forty repositories from the 10,000-star
band, weighted by how few such repositories there are, can.

Runs in Actions with GITHUB_TOKEN (search: 30 calls a minute; REST: 1,000
an hour), which is why the default is 40 repositories a band and the
script sleeps on the limits rather than failing. Writes one JSON file the
kit's calibration reads at import, so the words on the cards follow the
numbers without anyone editing code.

    GITHUB_TOKEN=... python3 src/calibrate.py --out data/calibration/repositories.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from trophykit.catalogue import RCORE  # noqa: E402

API = "https://api.github.com"
BANDS = ((1, 9), (10, 99), (100, 999), (1000, 9999), (10000, None))
MEASURED = ("stars", "forks", "contributors", "commits", "releases", "merged", "resolved")


class Client:
    """The smallest REST client that respects the two rate limits."""

    def __init__(self, token: str, quiet: bool = False):
        self.token = token
        self.quiet = quiet
        self.calls = 0

    def get(self, path: str, params: dict | None = None):
        """Return (json body or None, headers). Sleeps through rate limits; None on 404/409/422."""
        url = path if path.startswith("http") else API + path
        if params:
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
        for attempt in range(10):
            req = urllib.request.Request(url, headers={
                "Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
                "User-Agent": "tannergolden-trophies-calibrate", "X-GitHub-Api-Version": "2022-11-28"})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    self.calls += 1
                    body = r.read()
                    headers = {k.lower(): v for k, v in r.headers.items()}
                    self._pace(headers)
                    return (json.loads(body) if body else None), headers
            except urllib.error.HTTPError as e:
                headers = {k.lower(): v for k, v in e.headers.items()}
                if e.code in (403, 429):
                    if "too large" in (e.read() or b"").decode("utf-8", "replace").lower():
                        return {"too_large": True}, headers
                    self._wait(headers, attempt)
                    continue
                if e.code in (404, 409, 422, 451):
                    return None, headers
                if e.code == 202:  # statistics being computed
                    time.sleep(3)
                    continue
                time.sleep(2 + attempt)
            except (urllib.error.URLError, TimeoutError, ConnectionError):
                time.sleep(2 + attempt)
        return None, {}

    def _pace(self, headers: dict) -> None:
        if headers.get("x-ratelimit-remaining") in ("0", "1") and headers.get("x-ratelimit-reset"):
            self._sleep(int(headers["x-ratelimit-reset"]) - time.time() + 2)

    def _wait(self, headers: dict, attempt: int) -> None:
        if headers.get("retry-after"):
            self._sleep(int(headers["retry-after"]) + 1)
        elif headers.get("x-ratelimit-reset"):
            self._sleep(int(headers["x-ratelimit-reset"]) - time.time() + 2)
        else:
            self._sleep(min(120, 15 * (attempt + 1)))

    def _sleep(self, seconds: float) -> None:
        seconds = max(1.0, min(seconds, 3600))
        if not self.quiet:
            print(f"  rate limit: sleeping {seconds:.0f}s", file=sys.stderr, flush=True)
        time.sleep(seconds)

    def count(self, kind: str, q: str) -> int | None:
        data, _ = self.get(f"/search/{kind}", {"q": q, "per_page": 1})
        return None if data is None else data.get("total_count")

    def last_page(self, path: str, params: dict) -> int | None:
        """The item count behind a paged endpoint, from the Link header's last page."""
        data, headers = self.get(path, dict(params, per_page=1))
        if isinstance(data, dict) and data.get("too_large"):
            return 500  # GitHub refuses to list more than 500 contributors
        if data is None:
            return 0
        n = link_last(headers.get("link", ""))
        return n if n is not None else (len(data) if isinstance(data, list) else 0)


def link_last(link: str) -> int | None:
    m = re.search(r'[?&]page=(\d+)>;\s*rel="last"', link or "")
    return int(m.group(1)) if m else None


def band_query(lo: int, hi: int | None) -> str:
    return f"stars:>={lo}" if hi is None else f"stars:{lo}..{hi}"


def population(client: Client, thresholds: dict) -> dict:
    """Population counts the search API can answer directly."""
    out = {"base": client.count("repositories", "stars:>=1 fork:false"), "bands": {}, "stars": {}, "forks": {}}
    for lo, hi in BANDS:
        out["bands"][f"{lo}-{hi or ''}"] = client.count("repositories", band_query(lo, hi) + " fork:false")
    for n in thresholds["stars"]:
        out["stars"][str(n)] = client.count("repositories", f"stars:>={n} fork:false")
    for n in thresholds["forks"]:
        out["forks"][str(n)] = client.count("repositories", f"forks:>={n} stars:>=1 fork:false")
    return out


def sample_band(client: Client, lo: int, hi: int | None, n: int, rng: random.Random, today: dt.date) -> list:
    """Up to `n` repository names from one star band, spread over creation months."""
    names: list = []
    seen: set = set()
    months = [(y, m) for y in range(2009, today.year + 1) for m in range(1, 13) if (y, m) <= (today.year, today.month)]
    rng.shuffle(months)
    for y, m in months:
        if len(names) >= n:
            break
        end = (dt.date(y + (m == 12), (m % 12) + 1, 1) - dt.timedelta(days=1)).isoformat()
        q = f"{band_query(lo, hi)} fork:false created:{y}-{m:02d}-01..{end}"
        data, _ = client.get("/search/repositories", {"q": q, "per_page": 30, "page": rng.randint(1, 3)})
        items = [r["full_name"] for r in (data or {}).get("items", []) if not r.get("archived")]
        rng.shuffle(items)
        for full in items[:8]:
            if full not in seen:
                seen.add(full)
                names.append(full)
    return names[:n]


def measure_repository(client: Client, full: str) -> dict | None:
    """The repository the way a case counts it: the seven measurable cores."""
    r, _ = client.get(f"/repos/{full}")
    if not r or r.get("fork"):
        return None
    return {
        "full_name": full,
        "stars": r.get("stargazers_count", 0),
        "forks": r.get("forks_count", 0),
        "contributors": client.last_page(f"/repos/{full}/contributors", {"anon": "true"}),
        "commits": client.last_page(f"/repos/{full}/commits", {}),
        "releases": client.last_page(f"/repos/{full}/releases", {}),
        "merged": client.count("issues", f"repo:{full} is:pr is:merged"),
        "resolved": client.count("issues", f"repo:{full} is:issue is:closed reason:completed"),
    }


def estimate(bands: list, thresholds: dict) -> dict:
    """Stratified shares: Σ over bands of weight × the band's fraction at or above each threshold.

    `bands` is a list of {"weight": share of the population, "repos": [measured dicts]}.
    A band with no measured repositories contributes nothing and is reported."""
    out = {}
    total_weight = sum(b["weight"] for b in bands if b["repos"])
    for key, steps in thresholds.items():
        anchors = []
        for t in steps:
            share = 0.0
            for b in bands:
                if not b["repos"]:
                    continue
                vals = [x[key] for x in b["repos"] if x.get(key) is not None]
                if not vals:
                    continue
                frac = sum(1 for v in vals if v >= t) / len(vals)
                share += (b["weight"] / total_weight) * frac
            anchors.append([t, round(100 * share, 4)])
        # a share can never rise with the threshold; smooth any sampling noise downward
        for i in range(1, len(anchors)):
            anchors[i][1] = min(anchors[i][1], anchors[i - 1][1])
        out[key] = anchors
    return out


def exact_shares(pop: dict, key: str, steps: tuple) -> list:
    base = pop["base"] or 1
    anchors = [[t, round(100 * (pop[key].get(str(t)) or 0) / base, 4)] for t in steps]
    for i in range(1, len(anchors)):
        anchors[i][1] = min(anchors[i][1], anchors[i - 1][1])
    return anchors


def run(client: Client, per_band: int, seed: int, today: dt.date, log=print) -> dict:
    thresholds = {c.key: tuple(c.steps) for c in RCORE if c.key in MEASURED}
    log("counting the population")
    pop = population(client, thresholds)
    base = pop["base"] or 1
    rng = random.Random(seed)
    bands = []
    for lo, hi in BANDS:
        label = f"{lo}-{hi or ''}"
        weight = (pop["bands"][label] or 0) / base
        log(f"sampling band {label}: weight {weight:.5f}")
        repos = []
        for full in sample_band(client, lo, hi, per_band, rng, today):
            m = measure_repository(client, full)
            if m:
                repos.append(m)
        log(f"  measured {len(repos)} repositories")
        bands.append({"band": label, "weight": weight, "population": pop["bands"][label], "sampled": len(repos), "repos": repos})
    sampled = {k: v for k, v in thresholds.items() if k not in ("stars", "forks")}
    cores = {k: {"anchors": a} for k, a in estimate(bands, sampled).items()}
    cores["stars"] = {"anchors": exact_shares(pop, "stars", thresholds["stars"])}
    cores["forks"] = {"anchors": exact_shares(pop, "forks", thresholds["forks"])}
    return {
        "date": today.isoformat(),
        "population": "public, non-fork repositories with at least one star",
        "base": pop["base"],
        "n": sum(b["sampled"] for b in bands),
        "bands": [{k: b[k] for k in ("band", "weight", "population", "sampled")} for b in bands],
        "cores": cores,
        "calls": client.calls,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default="data/calibration/repositories.json")
    ap.add_argument("--per-band", type=int, default=40)
    ap.add_argument("--seed", type=int, default=None, help="default: today's ordinal, so a re-run on a day repeats it")
    ap.add_argument("--today", default="")
    args = ap.parse_args(argv)
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("GITHUB_TOKEN is required", file=sys.stderr)
        return 2
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    result = run(Client(token), args.per_band, args.seed if args.seed is not None else today.toordinal(), today)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {out}: {result['n']} repositories in {len(result['bands'])} bands, {result['calls']} API calls")
    for key, spec in result["cores"].items():
        print(f"  {key:13} " + "  ".join(f"{t}: {p:g}%" for t, p in spec["anchors"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Trophy Kit: the command line the action runs, and the one you run locally.

  python3 src/trophy-kit.py run --root . [--mode profile|repository] [--subject octo-dev]
      measure over GitHub's API, render, write the README block and the ledger
  python3 src/trophy-kit.py render --root . --from measurement.json
      re-render a saved measurement, no network
  python3 src/trophy-kit.py check --root . --from measurement.json
      fail if the committed SVGs differ from a fresh render of that measurement
  python3 src/trophy-kit.py preview --root . [--mode ...] [--style ...]
      render the built-in sample measurement, for a look at every style
  python3 src/trophy-kit.py measure --mode ... --subject ... > measurement.json
      measure only, print the JSON
  python3 src/trophy-kit.py catalogue > docs/Catalogue.md
      the catalogue page, generated from the data
  python3 src/trophy-kit.py self-test
      renderer invariants and the golden hash, no repository or network needed

Stdlib only. GITHUB_TOKEN (or TROPHIES_TOKEN) is read from the environment
for anything that talks to GitHub.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from trophykit import KIT_VERSION, art, catalogue, config, ledger as ledger_mod, render, sample, styles  # noqa: E402,F401
from trophykit.readme import apply as apply_readme  # noqa: E402

# sha256 of one canonical render. The self-test fails when output changes while
# KIT_VERSION did not: bump both together, knowingly.
GOLDEN_SHA = "07eaad9137edec066598d9a4c3cc409a891a36ca906e3a5881a6eae9370cda7c"


def _today(args) -> dt.date:
    return dt.date.fromisoformat(args.today) if getattr(args, "today", None) else dt.datetime.now(dt.timezone.utc).date()


def _cfg(args) -> dict:
    root = Path(args.root)
    cfg = config.load(root / args.config if args.config else root / ".github" / "trophies.yml")
    for key in ("mode", "subject", "style", "case", "out"):
        v = getattr(args, key, None)
        if v:
            cfg[key] = v
    return cfg


def _subject(cfg: dict) -> tuple[str, str | None]:
    """(login, owner/name) from the config or the Actions environment."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if cfg["mode"] == "repository":
        full = cfg["subject"] or repo
        if "/" not in full:
            raise SystemExit("repository mode needs subject: owner/name (or GITHUB_REPOSITORY)")
        return full.split("/")[0], full
    login = cfg["subject"] or os.environ.get("GITHUB_REPOSITORY_OWNER") or repo.split("/")[0]
    if not login:
        raise SystemExit("profile mode needs subject: a login (or GITHUB_REPOSITORY_OWNER)")
    return login, None


def cmd_measure(args, cfg: dict, root: Path):
    from trophykit.github import GitHub
    from trophykit import measure_profile, measure_repo

    gh = GitHub()
    today = _today(args)
    ledger_path = root / ".github" / "trophies.lock.json"
    led = ledger_mod.load(ledger_path) if cfg["ledger"] else {"scan": {}, "history": {}, "reached": {}}
    login, full = _subject(cfg)
    if cfg["mode"] == "repository":
        owner, name = full.split("/", 1)
        result = measure_repo.measure(gh, owner, name, led, today=today, scan_pages=cfg["scan_pages"])
    else:
        result = measure_profile.measure(gh, login, led, today=today, private=bool(cfg["private"]), scan_pages=cfg["scan_pages"])
    owners = {}
    for a in catalogue.MODES[cfg["mode"]]["ach"]:
        if a.only and a.only not in owners:
            owners[a.only] = measure_profile.owner_of(gh, a.only)
    result["owners"] = owners
    result["today"] = today.isoformat()
    return result, led, ledger_path


def finish(result: dict, cfg: dict, root: Path, led: dict, ledger_path: Path | None, today: dt.date, write: bool, commit_file: str = "") -> int:
    cores = render._cores(cfg)
    ach = catalogue.MODES[cfg["mode"]]["ach"]
    reached_today = {"tiers": [], "achievements": []}
    if led is not None:
        folded = ledger_mod.update(led, result, cores, ach, today)
        result.setdefault("delta", folded["delta"])
        result.setdefault("new", folded["new"])
        key = today.isoformat()
        for c in cores:
            for stamp, day in folded["reached"].get(c.key, {}).items():
                if day == key:
                    t, stars = stamp.split(".")
                    reached_today["tiers"].append((catalogue.TIER_NAMES[int(t)] + (f" star {stars}" if stars != "0" else ""), c.title))
        for a in ach:
            for k, day in folded["reached"].get("ach:" + a.slug, {}).items():
                if day == key:
                    reached_today["achievements"].append(a.name + (f" {catalogue.ROMAN[int(k)]}" if a.goals else ""))
    planned = render.plan(result, cfg, result.get("owners"))
    print(render.describe(planned, result))
    if not write:
        return 0
    changed = render.write(root, planned)
    if cfg["readme"] == "manage" and apply_readme(root / cfg["readme_path"], planned["readme"]):
        changed.append(cfg["readme_path"])
    if led is not None and ledger_path is not None:
        # The scanner cache moves whenever a head moves; on its own that is
        # not worth a commit. The ledger is written when a card changed, when
        # a tier was reached, or for the weekly snapshot that keeps the
        # schedule alive.
        due = ledger_mod.snapshot_due(led, today)
        if due:
            ledger_mod.mark_snapshot(led, today)
        if (changed or due or not ledger_path.exists()) and ledger_mod.save(ledger_path, led):
            changed.append(ledger_path.relative_to(root).as_posix())
    print(f"{len(changed)} files changed" if changed else "nothing changed")
    if commit_file and changed:
        msg = render.commit_message(planned, result, changed, today, reached_today, os.environ.get("GITHUB_RUN_ID", ""))
        Path(commit_file).write_text(msg, encoding="utf-8")
        print(msg.splitlines()[0])
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"### Trophies\n\n{render.describe(planned, result)}\n\n{len(changed)} files changed\n")
    return 0


def cmd_run(args) -> int:
    root = Path(args.root)
    cfg = _cfg(args)
    result, led, ledger_path = cmd_measure(args, cfg, root)
    if args.save:
        Path(args.save).write_text(json.dumps(result, indent=1, default=str) + "\n", encoding="utf-8")
    return finish(result, cfg, root, led if cfg["ledger"] else None, ledger_path, _today(args), write=True, commit_file=args.commit_file)


def cmd_measure_only(args) -> int:
    root = Path(args.root)
    cfg = _cfg(args)
    result, _, _ = cmd_measure(args, cfg, root)
    print(json.dumps(result, indent=1, default=str))
    return 0


def _load_result(args, cfg: dict) -> dict:
    if args.source:
        return json.loads(Path(args.source).read_text(encoding="utf-8"))
    return json.loads(json.dumps(sample.SAMPLES[cfg["mode"]]))


def cmd_render(args) -> int:
    root = Path(args.root)
    cfg = _cfg(args)
    result = _load_result(args, cfg)
    return finish(result, cfg, root, None, None, _today(args), write=True)


def cmd_check(args) -> int:
    root = Path(args.root)
    cfg = _cfg(args)
    result = _load_result(args, cfg)
    planned = render.plan(result, cfg, result.get("owners"))
    stale = render.check(root, planned)
    if stale:
        print("stale: " + ", ".join(stale))
        return 1
    print(f"{len(planned['files'])} files current")
    return 0


def cmd_preview(args) -> int:
    root = Path(args.root)
    cfg = _cfg(args)
    cfg["ledger"] = False
    cfg["readme"] = "manage"
    cfg["readme_path"] = args.readme or "README.md"
    result = json.loads(json.dumps(sample.SAMPLES[cfg["mode"]]))
    if args.owner:
        result["owners"] = {a.only: result["subject"].split("/")[0] for a in catalogue.ACH if a.only}
    return finish(result, cfg, root, None, None, _today(args), write=True)


def cmd_catalogue(args) -> int:
    from trophykit.catalogue_md import page

    sys.stdout.write(page())
    return 0


def canonical_render() -> str:
    p = sample.PROFILE
    return art.STYLES["trophy"](art.NIGHT, catalogue.CORE[0], p["values"]["commits"], {"rank": True, "delta": 124, "new": True})


def cmd_self_test(args) -> int:
    failures = []
    # every icon and token referenced by the catalogue exists
    for a in catalogue.ACH + catalogue.RACH:
        if a.icon not in catalogue.ICONS:
            failures.append(f"icon {a.icon} ({a.name})")
        if a.tok not in catalogue.PAL:
            failures.append(f"token {a.tok} ({a.name})")
    if len([a for a in catalogue.ACH if not a.only]) != 100 or len(catalogue.RACH) != 100:
        failures.append("each mode must hold exactly one hundred public achievements")
    if len({a.slug for a in catalogue.ACH}) != len(catalogue.ACH) or len({a.slug for a in catalogue.RACH}) != len(catalogue.RACH):
        failures.append("achievement slugs must be unique within a mode")
    # every style renders every tier, both cases, deterministically
    for name, fn in art.STYLES.items():
        for th in (art.NIGHT, art.DAY):
            for v in (0, 42, 310, 1240, 3610, 7420, 23500, 640000):
                a = fn(th, catalogue.CORE[0], v, {"rank": True, "delta": 5, "new": True})
                b = fn(th, catalogue.CORE[0], v, {"rank": True, "delta": 5, "new": True})
                if a != b:
                    failures.append(f"{name} is not deterministic at {v}")
                if "<svg" not in a or not a.endswith("</svg>"):
                    failures.append(f"{name} produced a malformed document at {v}")
    # every achievement pin renders in every state
    for a in catalogue.ACH + catalogue.RACH:
        for cur in (None, 0, a.tiers[0], a.tiers[-1]):
            art.pin(art.NIGHT, a, cur)
    # the level and next-up cards render for both samples
    for mode, s in sample.SAMPLES.items():
        cores = catalogue.MODES[mode]["core"]
        ach = catalogue.MODES[mode]["ach"]
        art.level_card(art.DAY, cores, s["values"], ach, s["curs"], s["subject"], ("flame", "#000000", "X", "Y"))
        art.next_up_card(art.NIGHT, cores, s["values"], ach, s["curs"])
    # the measurement sample covers the catalogue
    for mode, s in sample.SAMPLES.items():
        for a in catalogue.MODES[mode]["ach"]:
            if a.slug not in s["curs"]:
                failures.append(f"sample {mode} lacks {a.slug}")
    # the golden hash
    sha = hashlib.sha256(canonical_render().encode("utf-8")).hexdigest()
    if sha != GOLDEN_SHA:
        failures.append(f"golden render changed: {sha} (bump KIT_VERSION and GOLDEN_SHA together if intended)")
    if failures:
        print("self-test failed:\n  " + "\n  ".join(failures))
        return 1
    print(f"self-test passed (kit v{KIT_VERSION}, {len(art.STYLES)} styles, {len(catalogue.ACH)}+{len(catalogue.RACH)} achievements)")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="trophy-kit", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--root", default=".", help="repository root (default: .)")
        sp.add_argument("--config", default="", help="config path relative to root (default: .github/trophies.yml)")
        sp.add_argument("--mode", choices=list(catalogue.MODES))
        sp.add_argument("--subject", default="", help="login, or owner/name in repository mode")
        sp.add_argument("--style", choices=list(art.STYLES))
        sp.add_argument("--case", choices=["night", "day", "both"])
        sp.add_argument("--out", default="")
        sp.add_argument("--today", default="", help="YYYY-MM-DD, for reproducible runs")

    sp = sub.add_parser("run", help="measure, render, write");  common(sp)
    sp.add_argument("--save", default="", help="also save the measurement JSON here")
    sp.add_argument("--commit-file", default="", help="write a Conventional Commit message for this run here, when something changed")
    sp = sub.add_parser("measure", help="measure only, print JSON");  common(sp)
    sp = sub.add_parser("render", help="render a saved measurement");  common(sp)
    sp.add_argument("--from", dest="source", default="", help="measurement JSON (default: the built-in sample)")
    sp = sub.add_parser("check", help="verify committed SVGs against a measurement");  common(sp)
    sp.add_argument("--from", dest="source", default="")
    sp = sub.add_parser("preview", help="render the sample measurement");  common(sp)
    sp.add_argument("--readme", default="", help="README path to manage (default: README.md under root)")
    sp.add_argument("--owner", action="store_true", help="include the owner-only Maker achievements")
    sub.add_parser("catalogue", help="print docs/Catalogue.md")
    sub.add_parser("self-test", help="renderer invariants and the golden hash")
    args = p.parse_args(argv)
    return {"run": cmd_run, "measure": cmd_measure_only, "render": cmd_render, "check": cmd_check, "preview": cmd_preview,
            "catalogue": cmd_catalogue, "self-test": cmd_self_test}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())

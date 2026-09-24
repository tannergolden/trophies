# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""From one measurement to a folder of SVGs, a README block and a ledger entry.

`plan(result, cfg, extras)` decides every file and its content; `write()` and
`check()` compare that plan with the tree. Nothing here talks to GitHub, so
a measurement saved as JSON can be re-rendered forever, which is how the
tests and `--preview` work.
"""
from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from . import KIT_VERSION, art, styles  # noqa: F401  (styles registers itself)
from .catalogue import MODES, PAL, RARITY_NAMES, TIER_NAMES, ach_state, measure
from .readme import block


def _visible(ach: list, cfg: dict, owner_login: str, subject_login: str) -> list:
    if cfg["achievements"] == "none":
        return []
    chosen = None if cfg["achievements"] == "all" else set(cfg["achievements"])
    out = []
    for a in ach:
        if a.only:
            # Owner-only entries exist only when the measured subject owns
            # the named repository; the measurement resolved those owners.
            if not owner_login or owner_login.lower() != subject_login.lower():
                continue
        if chosen is not None and a.slug not in chosen:
            continue
        out.append(a)
    return out


def _cores(cfg: dict) -> list:
    cores = list(MODES[cfg["mode"]]["core"])
    if cfg["core"]:
        order = {k: i for i, k in enumerate(cfg["core"])}
        cores = sorted([c for c in cores if c.key in order], key=lambda c: order[c.key])
    for i, c in enumerate(cores):
        tok = cfg["enamel"].get(c.key)
        if tok:
            if tok not in PAL:
                raise ValueError(f"enamel: {tok!r} is not an emblems color token")
            cores[i] = replace(c, tok=tok)
    return cores


def _sort_key(a, st):
    rank = 0 if st["earned"] else 2 if st["secret"] else 1
    return (rank, -st["rarity"] if st["earned"] else -st["pct"], a.name)


def plan(result: dict, cfg: dict, owners: dict | None = None) -> dict:
    """Everything a run writes: {"files": {relative path: content}, "readme": text, "summary": ...}."""
    mode = cfg["mode"]
    cores = _cores(cfg)
    subject = result["subject"]
    subject_login = subject.split("/")[0]
    owners = owners or {}
    ach_all = MODES[mode]["ach"]
    groups = MODES[mode]["groups"]
    ach = []
    for a in ach_all:
        if a.only and (not owners.get(a.only) or owners[a.only].lower() != subject_login.lower()):
            continue
        ach.append(a)
    if cfg["achievements"] == "none":
        ach = []
    elif cfg["achievements"] != "all":
        chosen = set(cfg["achievements"])
        ach = [a for a in ach if a.slug in chosen]
    curs = result["curs"]
    values = result["values"]
    delta = result.get("delta", {}) if "weekly" in cfg["card"] else {}
    new = result.get("new", {}) if "new" in cfg["card"] else {}
    rank = "rank" in cfg["card"]
    cases = ["night", "day"] if cfg["case"] == "both" else [cfg["case"]]
    draw = art.STYLES[cfg["style"]]
    out = cfg["out"].strip("/")
    files: dict[str, str] = {}
    alts: dict[str, str] = {}

    def put(base: str, render):
        for case in cases:
            theme = art.CASES[case]
            svg = render(theme)
            # A committed text file ends with a newline; the repository's own
            # validator, and most editors' diffs, insist on it.
            files[f"{out}/{base}{'-day' if case == 'day' else ''}.svg"] = svg.rstrip("\n") + "\n"
            if base not in alts:
                a = svg.split('aria-label="', 1)[1].split('"', 1)[0]
                alts[base] = a.replace("&quot;", '"').replace("&amp;", "&")

    for c in cores:
        o = {"rank": rank, "delta": delta.get(c.key, 0), "new": bool(new.get(c.key))}
        put(c.key, lambda th, c=c, o=o: draw(th, c, values[c.key], o))
    if cfg["banner"]:
        extra = result.get("extra", {})
        if mode == "profile":
            streak = extra.get("currentStreak", 0) if cfg["streak"] == "current" else extra.get("streak", 0)
            head = f"{streak}-DAY STREAK" if cfg["streak"] == "current" else f"LONGEST STREAK {streak} DAYS"
            tail = f"  ·  LONGEST {extra.get('streak', 0)} DAYS" if cfg["streak"] == "current" else ""
            foot = ("flame", PAL["tangerine"], head, tail)
        else:
            lr = extra.get("lastRelease")
            head = f"RELEASED {lr} DAYS AGO" if lr is not None else "NO RELEASE YET"
            foot = ("tag", PAL["teal"], head, f"  ·  {extra.get('commits30', 0):,} COMMITS THIS MONTH")
        put("level", lambda th: art.level_card(th, cores, values, ach, curs, subject, foot))
        put("next-up", lambda th: art.next_up_card(th, cores, values, ach, curs))
    pins = []
    earned = 0
    for a in ach:
        st = ach_state(a, curs.get(a.slug))
        earned += st["earned"]
        put(f"achievements/{a.slug}", lambda th, a=a: art.pin(th, a, curs.get(a.slug)))
        pins.append((a.g, a.slug, alts[f"achievements/{a.slug}"], st))
    pins.sort(key=lambda p: (p[0], _sort_key(next(x for x in ach if x.slug == p[1]), p[3])))
    nxt = art.next_up_items(cores, values, [a for a in ach], curs, 1)
    unmeasured = [a.name for a in ach if curs.get(a.slug) is None]
    summary = f"{earned} of {len(ach)} earned"
    if nxt:
        summary += f" · next: {nxt[0]['name']}, {int(nxt[0]['pct'] * 100)}%"
    readme = block(out, mode, cores, alts, [(g, b, a) for g, b, a, _ in pins], groups, summary, cfg["theme"], cfg["banner"])
    tiers = {c.key: TIER_NAMES[measure(c, values[c.key])["t"]] for c in cores}
    return {"files": files, "readme": readme, "summary": summary, "tiers": tiers, "earned": earned, "total": len(ach),
            "unmeasured": unmeasured, "out": out}


def write(root: Path, planned: dict, prune: bool = True) -> list[str]:
    """Write every planned file under `root`; prune SVGs nothing names. Returns the paths that changed."""
    changed = []
    for rel, content in planned["files"].items():
        p = root / rel
        if p.exists() and p.read_text(encoding="utf-8") == content:
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        changed.append(rel)
    if prune:
        outdir = root / planned["out"]
        keep = set(planned["files"])
        if outdir.exists():
            for p in sorted(outdir.rglob("*.svg")):
                rel = p.relative_to(root).as_posix()
                if rel not in keep:
                    p.unlink()
                    changed.append(rel)
    return changed


def check(root: Path, planned: dict) -> list[str]:
    """Paths whose committed content differs from the plan at the same kit version."""
    stale = []
    stamp = f"<!--trophy-kit v{KIT_VERSION} "
    for rel, content in planned["files"].items():
        p = root / rel
        if not p.exists():
            stale.append(rel + " (missing)")
            continue
        have = p.read_text(encoding="utf-8")
        if have == content:
            continue
        if stamp not in have:
            continue  # another kit version drew it; it regenerates on the next run
        stale.append(rel)
    return stale


def describe(planned: dict, result: dict) -> str:
    lines = [f"{result['mode']} case for {result['subject']}: {planned['earned']} of {planned['total']} achievements, "
             + ", ".join(f"{k} {v}" for k, v in planned["tiers"].items())]
    if planned["unmeasured"]:
        lines.append("not measured yet: " + ", ".join(planned["unmeasured"]))
    for n in result.get("notes", []):
        lines.append("note: " + n)
    api = result.get("api") or {}
    if api.get("calls"):
        lines.append(f"api: {api['calls']} calls, {api.get('points', 0)} GraphQL points")
    return "\n".join(lines)


def rarity_name(r: int) -> str:
    return RARITY_NAMES[r]


def commit_message(planned: dict, result: dict, changed: list, today, reached_today: dict, run_id: str = "") -> str:
    """A Conventional Commit for this run, unique to what this run measured.

    Follows tannergolden/standards' Conventional Commits: `type(scope): subject`
    with a required scope, a required body wrapped at 72 columns that says
    why, and never an em dash. The subject names the most notable thing that
    happened; the body carries the measured values, the date and the run, so
    no two refreshes read alike.
    """
    import textwrap

    tiers, ach_new = reached_today.get("tiers", []), reached_today.get("achievements", [])
    delta = {k: v for k, v in (result.get("delta") or {}).items() if v}
    subject_of = result["subject"]
    if tiers:
        head = "reach " + ", ".join(f"{t} on {name}" for t, name in tiers[:2]) + (" and more" if len(tiers) > 2 else "")
    elif ach_new:
        head = "earn " + ", ".join(ach_new[:2]) + (f" and {len(ach_new) - 2} more" if len(ach_new) > 2 else "")
    elif delta:
        top = sorted(delta.items(), key=lambda kv: -kv[1])[:3]
        head = "refresh the case, " + ", ".join(f"{k} +{v:,}" for k, v in top)
    else:
        head = f"refresh the case for {subject_of}"
    subject = f"chore(trophies): \U0001F3C6 {head}"
    if len(subject) > 72:
        subject = subject[:69].rstrip(", ") + "..."
    lines = []
    para = (f"Measured {subject_of} on {today.isoformat()}" + (f" in run {run_id}" if run_id else "") + ". "
            f"The case stands at {planned['earned']} of {planned['total']} achievements, with "
            + ", ".join(f"{k} at {v}" for k, v in planned["tiers"].items()) + ".")
    lines += textwrap.wrap(para, 72) + [""]
    if tiers:
        lines += textwrap.wrap("Newly reached: " + ", ".join(f"{t} on {name}" for t, name in tiers) + ".", 72) + [""]
    if ach_new:
        lines += textwrap.wrap("Newly earned: " + ", ".join(ach_new) + ".", 72) + [""]
    if delta:
        lines += textwrap.wrap("Moved this week: " + ", ".join(f"{k} +{v:,}" for k, v in sorted(delta.items())) + ".", 72) + [""]
    svgs = [c for c in changed if c.endswith(".svg")]
    other = [c for c in changed if not c.endswith(".svg")]
    what = f"This run rewrote {len(svgs)} image{'s' if len(svgs) != 1 else ''}"
    if other:
        what += " and " + ", ".join(other)
    what += (". Nothing is fetched when the README is viewed, so every value the case shows has to be "
             "committed; the bot commits so the refresh never counts toward the subject's own trophies.")
    lines += textwrap.wrap(what, 72)
    return subject + "\n\n" + "\n".join(lines) + "\n"

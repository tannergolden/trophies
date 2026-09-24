# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The commit scanner behind every "heavy" achievement.

Counting commits is one GraphQL field. Knowing that a commit message starts
with `feat:`, that it was signed, or that it was authored at 3 a.m. means
reading the commits themselves, a hundred at a time. So this runs under a
page budget per run, remembers what it has read in the ledger keyed by the
branch head, and only re-reads a repository whose head moved. A big account
is fully scanned within about a week of daily runs and cheap thereafter.

Timestamps use `author.date`, which GitHub keeps in the author's own offset,
so "between midnight and 5 a.m." means the author's midnight, not UTC's.

A refresh commit, the one this kit writes, is recognised by its scope,
`chore(trophies):`, and counted only as a refresh: it adds nothing to the
commit total, the active days, the streak or any craft statistic. That is
what lets the commit carry a person's name as its author without that
person earning a trophy for it.
"""
from __future__ import annotations

import re
from collections import Counter

from .calendar import parse_time

CONVENTIONAL = re.compile(r"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([^)]*\))?!?:\s", re.I)
EMOJI = re.compile(r"^(?:[\U0001F300-\U0001FAFF☀-➿⭐✅❌]|:[a-z0-9_+-]+:)")
SEMVER = re.compile(r"^v?\d+\.\d+\.\d+(?:[-+].*)?$")
REFRESH = re.compile(r"^chore\(trophies\):")

STATS = ("total", "conventional", "emoji", "signed", "coauthored", "revert", "onefile", "fix", "test", "docs",
         "night", "early", "lunch", "midnight", "heavy", "sweeping", "refresh")

HISTORY = """
query($owner:String!,$name:String!,$first:Int!,$after:String,$author:CommitAuthor){ rateLimit{cost}
  repository(owner:$owner,name:$name){ defaultBranchRef{ target{ ... on Commit{ oid
    history(first:$first,after:$after,author:$author){ totalCount pageInfo{hasNextPage endCursor}
      nodes{ oid message committedDate author{ date user{login} name } signature{isValid}
             authors(first:2){totalCount} changedFilesIfAvailable additions deletions } } } } } } }"""


def empty_stats() -> dict:
    return {k: 0 for k in STATS} | {"days": [], "authors": {}, "max_lines": 0, "max_files": 0, "refresh_days": {}}


def classify(node: dict, stats: dict) -> None:
    """Fold one commit into `stats`."""
    msg = (node.get("message") or "").strip()
    first = msg.split("\n", 1)[0]
    if REFRESH.match(first):
        stats["refresh"] += 1
        when = (node.get("author") or {}).get("date") or node.get("committedDate")
        if when:
            day = parse_time(when).date().isoformat()
            rd = stats.setdefault("refresh_days", {})
            rd[day] = rd.get(day, 0) + 1
        return
    stats["total"] += 1
    if CONVENTIONAL.match(first):
        stats["conventional"] += 1
        kind = CONVENTIONAL.match(first).group(1).lower()
        if kind == "fix":
            stats["fix"] += 1
        elif kind == "test":
            stats["test"] += 1
        elif kind == "docs":
            stats["docs"] += 1
    if EMOJI.match(first):
        stats["emoji"] += 1
    if first.startswith("Revert "):
        stats["revert"] += 1
    if (node.get("signature") or {}).get("isValid"):
        stats["signed"] += 1
    if ((node.get("authors") or {}).get("totalCount") or 0) > 1:
        stats["coauthored"] += 1
    files = node.get("changedFilesIfAvailable")
    if files == 1:
        stats["onefile"] += 1
    if files is not None:
        stats["max_files"] = max(stats["max_files"], files)
        if files >= 50:
            stats["sweeping"] += 1
    lines = (node.get("additions") or 0) + (node.get("deletions") or 0)
    stats["max_lines"] = max(stats["max_lines"], lines)
    if lines >= 1000:
        stats["heavy"] += 1
    when = (node.get("author") or {}).get("date") or node.get("committedDate")
    if when:
        t = parse_time(when)
        if t.hour < 5:
            stats["night"] += 1
        elif 5 <= t.hour < 8:
            stats["early"] += 1
        elif t.hour == 12:
            stats["lunch"] += 1
        if t.hour == 0 and t.minute == 0:
            stats["midnight"] += 1
        day = t.date().isoformat()
        if not stats["days"] or stats["days"][-1] != day:
            stats["days"].append(day)
    login = ((node.get("author") or {}).get("user") or {}).get("login") or (node.get("author") or {}).get("name") or "?"
    stats["authors"][login] = stats["authors"].get(login, 0) + 1


def scan_repository(gh, owner: str, name: str, cache: dict, budget: dict, author_id: str | None = None,
                    page_size: int = 100) -> dict:
    """Read a repository's default-branch history into `cache[owner/name]`.

    `cache` is the ledger's scan section; `budget["pages"]` is decremented for
    every page read across the whole run. A repository whose recorded head
    still matches is returned as is. One whose head moved starts again; if the
    budget runs out mid-way the partial result is kept with `complete: False`
    and finished on a later run.
    """
    key = f"{owner}/{name}"
    entry = cache.get(key) or {}
    author = {"id": author_id} if author_id else None
    after = entry.get("cursor") if not entry.get("complete") else None
    head = None
    stats = entry.get("stats") if entry.get("cursor") else None
    while budget["pages"] > 0:
        data = gh.gql(HISTORY, owner=owner, name=name, first=page_size, after=after, author=author)
        ref = ((data.get("repository") or {}).get("defaultBranchRef") or {})
        target = ref.get("target") or {}
        head = target.get("oid")
        hist = target.get("history") or {}
        if head is None:
            cache[key] = {"head": None, "complete": True, "stats": empty_stats(), "total": 0}
            return cache[key]
        if entry.get("complete") and entry.get("head") == head:
            return entry  # nothing moved since last time
        if stats is None:
            stats = empty_stats()
        budget["pages"] -= 1
        for node in hist.get("nodes") or []:
            if node:
                classify(node, stats)
        info = hist.get("pageInfo") or {}
        cache[key] = {"head": head, "complete": not info.get("hasNextPage"), "cursor": info.get("endCursor"),
                      "stats": stats, "total": hist.get("totalCount", stats["total"])}
        if not info.get("hasNextPage"):
            cache[key]["cursor"] = None
            return cache[key]
        after = info.get("endCursor")
    return cache.get(key) or {"head": head, "complete": False, "stats": stats or empty_stats(), "total": 0}


def merge_stats(entries: list) -> dict:
    """Sum the per-repository stats of several scan entries."""
    out = empty_stats()
    days: set = set()
    authors: Counter = Counter()
    refresh_days: Counter = Counter()
    for e in entries:
        st = (e or {}).get("stats") or {}
        for k in STATS:
            out[k] += st.get(k, 0)
        out["max_lines"] = max(out["max_lines"], st.get("max_lines", 0))
        out["max_files"] = max(out["max_files"], st.get("max_files", 0))
        days.update(st.get("days", []))
        authors.update(st.get("authors", {}))
        refresh_days.update(st.get("refresh_days", {}))
    out["days"] = sorted(days)
    out["authors"] = dict(authors)
    out["refresh_days"] = dict(refresh_days)
    return out


def without_refreshes(days: dict, stats: dict):
    """The contribution calendar with this kit's own refresh commits taken back out.

    GitHub counts a refresh commit authored by the subject in the subject's
    own repository like any other. The scanner knows which days those fell
    on, so each day gives them back; a day left at zero disappears, which is
    what keeps a streak honest.
    """
    out = dict(days)
    for day, n in (stats.get("refresh_days") or {}).items():
        d = parse_time(day + "T00:00:00Z").date()
        if d in out:
            out[d] = max(0, out[d] - n)
            if out[d] == 0:
                del out[d]
    return out

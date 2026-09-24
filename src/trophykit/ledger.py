# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""The ledger: `.github/trophies.lock.json`.

Every number on a trophy is recomputed from GitHub on every run; the ledger
only adds what GitHub cannot say afterwards: the day each tier was first
reached (for the NEW ribbon), a daily history of the core values (for the
weekly change and the repository Reach achievements), and the commit
scanner's cache. Deleting it loses history, never correctness.

Its weekly snapshot is also a real commit, which keeps GitHub from switching
off the schedule after sixty quiet days.
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

from .catalogue import ach_state, measure

HISTORY_DAYS = 400
NEW_FOR_DAYS = 7


def load(path: Path) -> dict:
    if path.exists():
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    return {"version": 1, "reached": {}, "history": {}, "scan": {}, "snapshot": None}


def save(path: Path, ledger: dict) -> bool:
    """Write the ledger; returns True when the file changed."""
    text = json.dumps(ledger, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def update(ledger: dict, result: dict, cores: list, ach: list, today: dt.date) -> dict:
    """Fold a run into the ledger and return what the cards need from it.

    Returns {"new": {core key: bool}, "delta": {core key: int}, "reached": {...}}.
    """
    key = today.isoformat()
    reached = ledger.setdefault("reached", {})
    history = ledger.setdefault("history", {})
    new, delta = {}, {}
    for c in cores:
        m = measure(c, result["values"][c.key])
        stamp = f"{m['t']}.{m['stars']}"
        rec = reached.setdefault(c.key, {})
        if m["t"] and stamp not in rec:
            rec[stamp] = key
        since = rec.get(stamp)
        new[c.key] = bool(since) and (today - dt.date.fromisoformat(since)).days < NEW_FOR_DAYS and m["t"] > 0
        h = history.setdefault(c.key, {})
        # Sparse: a point is written only when the value moved, so a quiet
        # day leaves the ledger untouched and produces no commit.
        latest = max(h) if h else None
        if latest is None or h[latest] != result["values"][c.key]:
            h[key] = result["values"][c.key]
        for old in [d for d in h if (today - dt.date.fromisoformat(d)).days > HISTORY_DAYS]:
            del h[old]
        week_ago = (today - dt.timedelta(days=7)).isoformat()
        at_or_before = sorted(d for d in h if d <= week_ago)
        base = h[at_or_before[-1]] if at_or_before else None
        delta[c.key] = max(0, result["values"][c.key] - base) if base is not None else 0
    for a in ach:
        st = ach_state(a, result["curs"].get(a.slug))
        if st["earned"]:
            rec = reached.setdefault("ach:" + a.slug, {})
            rec.setdefault(str(st["k"]), key)
    return {"new": new, "delta": delta, "reached": reached}


def value_at(ledger: dict, key: str, day: dt.date):
    """The recorded value of a core key on `day`, from the sparse history."""
    h = ledger.get("history", {}).get(key, {})
    at_or_before = sorted(d for d in h if d <= day.isoformat())
    return h[at_or_before[-1]] if at_or_before else None


def snapshot_due(ledger: dict, today: dt.date) -> bool:
    """Once a week the ledger commits even if nothing else changed."""
    last = ledger.get("snapshot")
    return last is None or (today - dt.date.fromisoformat(last)).days >= 7


def mark_snapshot(ledger: dict, today: dt.date) -> None:
    ledger["snapshot"] = today.isoformat()

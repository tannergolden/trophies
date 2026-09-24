# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""`.github/trophies.yml`: the consumer's choices, with defaults for all of them.

Stdlib only, like the rest of the kit: PyYAML is used when it happens to be
installed and a small reader for the flat, two-level YAML this file needs
substitutes when it is not. Every key is validated; an unknown key or value
fails the run with the key named rather than being ignored.
"""
from __future__ import annotations

from pathlib import Path

from .catalogue import MODES

DEFAULTS = {
    "mode": "profile",       # profile | repository
    "subject": "",           # login or owner/name; empty means the repository's owner, or the repository
    "style": "trophy",       # trophy | crest | medallion | crystal | plaque
    "case": "both",          # night | day | both
    "theme": "picture",      # picture (<picture>, follows the system theme) | fragment (#gh-*-mode-only links, no longer honoured by GitHub)
    "banner": True,
    "streak": "current",     # current | longest (profile mode)
    "core": [],              # a subset of the mode's core keys, in order; empty means all
    "enamel": {},            # core key -> emblems color token
    "achievements": "all",   # all | none | a list of slugs
    "card": ["rank", "weekly", "new"],
    "ledger": True,
    "readme": "manage",      # manage | none
    "readme_path": "README.md",
    "out": "assets/trophies",
    "private": False,        # count private contributions (needs TROPHIES_TOKEN)
    "scan_pages": 30,        # commit-scanner budget per run, 100 commits a page
}
CHOICES = {
    "mode": set(MODES), "style": {"trophy", "crest", "medallion", "crystal", "plaque"}, "case": {"night", "day", "both"},
    "theme": {"fragment", "picture"}, "streak": {"current", "longest"}, "readme": {"manage", "none"},
}


class ConfigError(ValueError):
    pass


def _parse_scalar(s: str):
    s = s.strip()
    if s.startswith(("'", '"')) and s.endswith(s[0]) and len(s) >= 2:
        return s[1:-1]
    low = s.lower()
    if low in ("true", "yes", "on"):
        return True
    if low in ("false", "no", "off"):
        return False
    if low in ("", "null", "~"):
        return None
    try:
        return int(s)
    except ValueError:
        return s


def _parse_inline(s: str):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [_parse_scalar(x) for x in inner.split(",")] if inner else []
    if s.startswith("{") and s.endswith("}"):
        out = {}
        for pair in s[1:-1].split(","):
            if pair.strip():
                k, _, v = pair.partition(":")
                out[k.strip()] = _parse_scalar(v)
        return out
    return _parse_scalar(s)


def _strip_comment(line: str) -> str:
    out, quote = [], None
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
            out.append(ch)
        elif ch == "#":
            break
        else:
            out.append(ch)
    return "".join(out).rstrip()


def parse_yaml(text: str) -> dict:
    """Enough YAML for this file: `key: scalar`, inline lists and maps, and block lists or maps one level deep."""
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text) or {}
    except ImportError:
        pass
    data: dict = {}
    key = None
    for raw in text.splitlines():
        line = _strip_comment(raw)
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        body = line.strip()
        if indent == 0:
            k, sep, v = body.partition(":")
            if not sep:
                raise ConfigError(f"cannot read line: {raw!r}")
            key = k.strip()
            data[key] = _parse_inline(v) if v.strip() else None
        elif key is not None:
            if body.startswith("- "):
                if not isinstance(data.get(key), list):
                    data[key] = []
                data[key].append(_parse_inline(body[2:]))
            else:
                k, sep, v = body.partition(":")
                if not sep:
                    raise ConfigError(f"cannot read line: {raw!r}")
                if not isinstance(data.get(key), dict):
                    data[key] = {}
                data[key][k.strip()] = _parse_inline(v)
    return data


def load(path: Path | None) -> dict:
    cfg = dict(DEFAULTS)
    if path and path.exists():
        given = parse_yaml(path.read_text(encoding="utf-8"))
        for k, v in given.items():
            k = k.replace("-", "_")
            if k not in DEFAULTS:
                raise ConfigError(f"unknown key in {path}: {k}")
            if v is not None:
                cfg[k] = v
    for k, allowed in CHOICES.items():
        if cfg[k] not in allowed:
            raise ConfigError(f"{k}: {cfg[k]!r} is not one of {sorted(allowed)}")
    if isinstance(cfg["core"], str):
        cfg["core"] = [cfg["core"]]
    if isinstance(cfg["card"], str):
        cfg["card"] = [cfg["card"]]
    valid_keys = {c.key for c in MODES[cfg["mode"]]["core"]}
    for k in cfg["core"]:
        if k not in valid_keys:
            raise ConfigError(f"core: {k!r} is not a {cfg['mode']} trophy ({', '.join(sorted(valid_keys))})")
    for k in cfg["enamel"]:
        if k not in valid_keys:
            raise ConfigError(f"enamel: {k!r} is not a {cfg['mode']} trophy")
    for k in cfg["card"]:
        if k not in ("rank", "weekly", "new"):
            raise ConfigError(f"card: {k!r} is not one of rank, weekly, new")
    if cfg["achievements"] not in ("all", "none") and not isinstance(cfg["achievements"], list):
        raise ConfigError("achievements: expected all, none or a list of slugs")
    cfg["scan_pages"] = int(cfg["scan_pages"])
    return cfg

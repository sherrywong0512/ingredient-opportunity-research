#!/usr/bin/env python3
"""Check that URLs cited in reports/examples resolve.

Purpose: catch dead links and the format side of fabricated citations. It
cannot verify that a live URL supports the claim — that requires a reader.

Usage:
  python3 scripts/check_links.py                 # examples/*.md by default
  python3 scripts/check_links.py path/to/report.md

Classification (two-channel, to avoid false "dead" verdicts):
  ok          2xx after redirects (direct fetch)
  alive-blocked  direct fetch 4xx/5xx but the Wayback Machine holds a recent
              (< 2 years) snapshot — the site is likely bot-blocking our
              request (FDA/Reckitt return 404 to datacenter IPs); treated as
              alive, reported as a warning, never as dead
  dead        direct 4xx/5xx AND no recent Wayback snapshot
  blocked     403/429 (rate-limit / WAF) — not dead
  unreachable connection/DNS/timeout — not treated as dead

RFC 2606 placeholder domains (example.com/.org/.net) are skipped.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = sorted((ROOT / "examples").glob("*.md"))
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
RESERVED_DOMAINS = ("example.com", "example.org", "example.net")


def is_reserved(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return any(host == d or host.endswith("." + d) for d in RESERVED_DOMAINS)


def extract_urls(text: str) -> list[str]:
    # Allow parentheses inside URLs (common in academic PDF links); strip a
    # trailing ')' only when it is unbalanced (the markdown link closer).
    found = re.findall(r"https?://[^\s\]\}>\"'`]+", text)
    cleaned = []
    for url in found:
        url = url.rstrip(".,;:")
        while url.count(")") > url.count("("):
            url = url[:-1]
        cleaned.append(url)
    return sorted(set(cleaned))


def wayback_recent(url: str) -> bool:
    """True when the Wayback Machine has a snapshot within the last 2 years."""
    quoted = urllib.parse.quote(url, safe="")
    try:
        req = urllib.request.Request(
            f"http://archive.org/wayback/available?url={quoted}",
            headers={"User-Agent": "project-eval-linkcheck/1.0"},
        )
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        snap = data.get("archived_snapshots", {}).get("closest", {})
        ts = snap.get("timestamp", "")
        if not ts:
            return False
        return (date.today().year * 10000 + date.today().month * 100
                + date.today().day) - int(ts) < 2 * 366 * 10000
    except (OSError, ValueError, KeyError):
        return False


def check_url(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=12) as resp:
            return "ok" if resp.status < 400 else "http-other"
    except urllib.error.HTTPError as exc:
        code = exc.code
    except urllib.error.URLError:
        return "unreachable"
    except (OSError, ValueError):
        return "unreachable"
    if code in (403, 429):
        return "blocked"
    if code in (404, 410, 451):
        # Two-channel: recent Wayback snapshot => bot-blocked, not dead.
        return "alive-blocked" if wayback_recent(url) else "dead"
    if code >= 500:
        return "server-error"
    return "http-other"


def main() -> int:
    args = [ROOT / arg for arg in sys.argv[1:]]
    targets = args or [t for t in DEFAULT_TARGETS if t.name != "README.md"]
    seen: dict[str, str] = {}
    dead: list[tuple[str, str]] = []
    warnings: list[tuple[str, str, str]] = []
    ok = 0
    for target in targets:
        if not target.is_file():
            print(f"[SKIP] missing file: {target}")
            continue
        text = target.read_text(encoding="utf-8")
        for url in extract_urls(text):
            if is_reserved(url):
                print(f"[skip] {target.name}: reserved placeholder {url[:70]}")
                continue
            if url not in seen:
                seen[url] = check_url(url)
            status = seen[url]
            if status == "dead":
                dead.append((target.name, url))
            elif status == "ok":
                ok += 1
            else:
                warnings.append((target.name, url, status))
    for fname, url, status in warnings:
        print(f"[{status}] {fname}: {url[:80]}")
    for fname, url in dead:
        print(f"[DEAD] {fname}: {url[:80]}")
    print(f"\nchecked {len(seen)} unique URLs across {len(targets)} file(s)")
    print(f"ok: {ok} | warnings ({'alive-blocked/blocked/unreachable' }): {len(warnings)} | dead: {len(dead)}")
    if dead:
        print("FAIL: dead links (direct 4xx/5xx and no recent Wayback snapshot)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

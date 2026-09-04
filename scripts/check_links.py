#!/usr/bin/env python3
"""Check that URLs cited in reports/examples resolve.

Purpose: catch dead links and the format side of fabricated citations. It
cannot verify that a live URL supports the claim — that requires a reader.

Usage:
  python3 scripts/check_links.py                 # examples/*.md by default
  python3 scripts/check_links.py path/to/report.md

Classification:
  ok          2xx (after redirects)
  dead        404/410/451 — definitive dead link (fails the check)
  blocked     403/429 or connection refused — reachable but restricted or
              rate-limited; NOT treated as dead (CI on live links is flaky,
              so this script is a local tool, not a hard CI gate)
  unreachable DNS failure / timeout — likely environment or genuinely gone;
              reported as warning, not a hard failure
"""

from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = sorted((ROOT / "examples").glob("*.md"))
URL_RE = re.compile(r"https?://[^\s\)\]\}>\"']+")
# RFC 2606 reserved domains are used for placeholder citations (format demos);
# any path under them 404s by design, so skip them.
RESERVED_DOMAINS = ("example.com", "example.org", "example.net")
UA = {"User-Agent": "Mozilla/5.0 (compatible; project-eval-linkcheck/1.0)"}


def is_reserved(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return any(host == d or host.endswith("." + d) for d in RESERVED_DOMAINS)


def check_url(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=10) as resp:
            code = resp.status
    except urllib.error.HTTPError as exc:
        code = exc.code
    except urllib.error.URLError as exc:
        reason = getattr(exc, "reason", None)
        if isinstance(reason, TimeoutError) or "timed out" in str(reason).lower():
            return "unreachable"
        return "unreachable"
    except (OSError, ValueError):
        return "unreachable"
    if code in (403, 429):
        return "blocked"
    if code in (404, 410, 451):
        return "dead"
    if 200 <= code < 400:
        return "ok"
    return "http-other"


def main() -> int:
    targets = [ROOT / arg for arg in sys.argv[1:]] or DEFAULT_TARGETS
    if targets == DEFAULT_TARGETS:
        targets = [t for t in targets if t.name != "README.md"]
    seen: dict[str, str] = {}
    dead: list[tuple[str, str, str]] = []      # file, url, status
    warnings: list[tuple[str, str, str]] = []
    for target in targets:
        if not target.is_file():
            print(f"[SKIP] missing file: {target}")
            continue
        text = target.read_text(encoding="utf-8")
        urls = sorted(set(m.rstrip(".,;") for m in URL_RE.findall(text)))
        for url in urls:
            if is_reserved(url):
                print(f"[skip] {target.name}: reserved placeholder {url[:60]}")
                continue
            if url in seen:
                status = seen[url]
            else:
                status = check_url(url)
                seen[url] = status
            if status == "dead":
                dead.append((target.name, url, status))
            elif status in ("blocked", "unreachable", "http-other"):
                warnings.append((target.name, url, status))
            else:
                print(f"[ok]   {target.name}: {url[:80]}")
    for fname, url, status in warnings:
        print(f"[{status}] {fname}: {url[:80]}")
    for fname, url, status in dead:
        print(f"[DEAD] {fname}: {url[:80]}")
    print(f"\nchecked {len(seen)} unique URLs across {len(targets)} file(s)")
    print(f"dead: {len(dead)} | warnings (blocked/unreachable): {len(warnings)}")
    if dead:
        print("FAIL: definitive dead links found (404/410/451)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

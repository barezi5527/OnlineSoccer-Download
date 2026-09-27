#!/usr/bin/env python3
"""Baut docs/downloads.json aus den Release-Assets dieses Repositories.

Datenquelle ist ausschließlich die GitHub-REST-API. Es werden keine
Besucherdaten, IP-Adressen oder anderen personenbezogenen Informationen
erhoben – die ermittelten Zahlen sind die von GitHub selbst gemeldeten
Downloadzähler der Release-Assets.

Aufruf:  GH_TOKEN=<token> python3 build-downloads.py docs/downloads.json
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
REPO = os.environ["GITHUB_REPOSITORY"]
SCHEMA_VERSION = 1

CHECKSUM_ASSET = re.compile(r"^checksums\.(txt|sha256|sha256sum)$", re.IGNORECASE)
SHA256_LINE = re.compile(r"^([0-9a-fA-F]{64})\s+\*?(.+?)\s*$")
SEMVER = re.compile(r"(\d+)\.(\d+)\.(\d+)")


def api_get(path: str):
    request = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Authorization": f"Bearer {os.environ['GH_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "online-soccer-download-counter",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url, headers={"User-Agent": "online-soccer-download-counter"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_checksums(text: str) -> dict[str, str]:
    """Liest eine sha256sum-Datei im Format '<hash>  <Dateiname>'."""
    result: dict[str, str] = {}
    for line in text.splitlines():
        match = SHA256_LINE.match(line.strip())
        if match:
            result[match.group(2).strip()] = match.group(1).lower()
    return result


def version_of(tag: str) -> str:
    cleaned = tag.lstrip("vV")
    return cleaned if SEMVER.fullmatch(cleaned) else tag


def sort_key(release: dict) -> tuple:
    match = SEMVER.search(release["version"])
    if not match:
        return (0, 0, 0, release["tag"])
    major, minor, patch = (int(part) for part in match.groups())
    return (major, minor, patch, release["tag"])


def build_release(release: dict) -> dict:
    assets = release.get("assets", [])
    checksums: dict[str, str] = {}

    for asset in assets:
        if CHECKSUM_ASSET.match(asset["name"]):
            try:
                checksums.update(parse_checksums(fetch_text(asset["browser_download_url"])))
            except (urllib.error.URLError, TimeoutError, ValueError) as error:
                print(f"Warnung: {asset['name']} nicht lesbar: {error}", file=sys.stderr)

    apk = None
    others = []
    for asset in assets:
        entry = {
            "name": asset["name"],
            "size": asset["size"],
            "downloads": asset["download_count"],
        }
        if asset["name"].lower().endswith(".apk"):
            apk = {
                **entry,
                "sha256": checksums.get(asset["name"]),
                "downloadUrl": asset["browser_download_url"],
            }
        else:
            others.append(entry)

    result = {
        "tag": release["tag_name"],
        "version": version_of(release["tag_name"]),
        "title": release["name"] or release["tag_name"],
        "prerelease": bool(release["prerelease"]),
        "publishedAt": release["published_at"],
        "pageUrl": release["html_url"],
        "apk": apk,
        "otherAssets": others,
        "downloads": sum(asset["download_count"] for asset in assets),
    }
    return result


def main() -> int:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/downloads.json")
    releases = api_get(f"/repos/{REPO}/releases?per_page=100")
    published = [build_release(item) for item in releases if not item["draft"]]
    published.sort(key=sort_key, reverse=True)

    document = {
        "schema": SCHEMA_VERSION,
        "repository": REPO,
        "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "GitHub REST API – Downloadzähler der Release-Assets",
        "totalDownloads": sum(item["downloads"] for item in published),
        "releases": published,
    }

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"{target}: {len(published)} Release(s), {document['totalDownloads']} Downloads gesamt")
    for item in published:
        apk = item["apk"]
        count = apk["downloads"] if apk else item["downloads"]
        print(f"  {item['version']}: {count} Downloads ({item['tag']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

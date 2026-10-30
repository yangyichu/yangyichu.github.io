"""Fetch a Google Scholar author profile and publish stable JSON artifacts."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse


def parse_profile_html(html: str) -> dict[str, Any]:
    """Parse the public fields used by the site from a Scholar profile page."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    name_element = soup.select_one("#gsc_prf_in")
    if not name_element:
        raise RuntimeError("Scholar returned no public profile; it may be rate-limiting the runner")

    stat_values = [
        int(element.get_text(strip=True).replace(",", "") or 0)
        for element in soup.select(".gsc_rsb_std")
    ]
    years = [element.get_text(strip=True) for element in soup.select(".gsc_g_t")]
    yearly_counts = [
        int(element.get_text(strip=True).replace(",", "") or 0)
        for element in soup.select(".gsc_g_al")
    ]

    publications = []
    for row in soup.select(".gsc_a_tr"):
        title_link = row.select_one(".gsc_a_at")
        if not title_link:
            continue
        citation_for_view = parse_qs(
            urlparse(title_link.get("href", "")).query
        ).get("citation_for_view", [""])[0]
        citation_text = row.select_one(".gsc_a_c")
        citation_digits = "".join(
            character
            for character in (citation_text.get_text(" ", strip=True) if citation_text else "")
            if character.isdigit()
        )
        publications.append(
            {
                "author_pub_id": citation_for_view,
                "num_citations": int(citation_digits or 0),
                "bib": {"title": title_link.get_text(" ", strip=True)},
            }
        )

    return {
        "name": name_element.get_text(" ", strip=True),
        "citedby": stat_values[0] if stat_values else 0,
        "cites_per_year": dict(zip(years, yearly_counts)),
        "publications": publications,
    }


def fetch_author(scholar_id: str, attempts: int = 3) -> dict[str, Any]:
    """Fetch and parse a public author profile with bounded retries."""
    import requests

    last_error: Exception | None = None
    scholar_hosts = (
        "scholar.google.com",
        "scholar.google.co.uk",
        "scholar.google.com.au",
    )
    for attempt in range(1, attempts + 1):
        try:
            response = requests.get(
                f"https://{scholar_hosts[attempt - 1]}/citations",
                params={"user": scholar_id, "hl": "en", "pagesize": 100},
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "Chrome/141.0 Safari/537.36"
                    ),
                    "Accept-Language": "en-US,en;q=0.9",
                },
                timeout=30,
            )
            response.raise_for_status()
            return parse_profile_html(response.text)
        except Exception as exc:
            last_error = exc
            if attempt < attempts:
                time.sleep(2 ** (attempt - 1))

    raise RuntimeError(
        "Google Scholar could not be reached after "
        f"{attempts} attempts. Scholar may be rate-limiting the GitHub runner."
    ) from last_error


def normalize_author(author: dict[str, Any], scholar_id: str) -> dict[str, Any]:
    """Convert scholarly's publication list into the map consumed by the site."""
    normalized = dict(author)
    publications: dict[str, dict[str, Any]] = {}
    for publication in author.get("publications") or []:
        publication = dict(publication)
        publication_id = publication.get("author_pub_id")
        if publication_id:
            publications[str(publication_id)] = publication

    normalized["publications"] = publications
    normalized["scholar_id"] = scholar_id
    normalized["updated"] = datetime.now(timezone.utc).isoformat()
    normalized["citedby"] = int(normalized.get("citedby") or 0)
    return normalized


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    parser.add_argument(
        "--source-json",
        type=Path,
        help="Use a saved scholarly response instead of making a network request.",
    )
    parser.add_argument(
        "--source-html",
        type=Path,
        help="Parse a saved public Scholar profile page instead of downloading it.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        print(
            "GOOGLE_SCHOLAR_ID is required. Use the profile ID from the user= part "
            "of the public Google Scholar profile URL.",
            file=sys.stderr,
        )
        return 2

    if args.source_json:
        author = json.loads(args.source_json.read_text(encoding="utf-8"))
    elif args.source_html:
        author = parse_profile_html(args.source_html.read_text(encoding="utf-8"))
    else:
        author = fetch_author(scholar_id)

    author = normalize_author(author, scholar_id)
    if not author.get("name"):
        raise RuntimeError("The Scholar response did not contain an author name")

    write_json(args.output_dir / "gs_data.json", author)
    write_json(
        args.output_dir / "gs_data_shieldsio.json",
        {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(author["citedby"]),
        },
    )
    print(
        f"Wrote citation data for {author['name']} "
        f"({author['citedby']} citations, {len(author['publications'])} publications)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

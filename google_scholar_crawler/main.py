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


def fetch_author(scholar_id: str, attempts: int = 3) -> dict[str, Any]:
    """Fetch an author profile, retrying transient Scholar/network failures."""
    from scholarly import scholarly

    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            author = scholarly.search_author_id(scholar_id)
            if not author:
                raise RuntimeError(f"No Google Scholar profile found for ID {scholar_id!r}")
            return scholarly.fill(
                author, sections=["basics", "indices", "counts", "publications"]
            )
        except Exception as exc:  # scholarly raises several transport/parser errors
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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        print(
            "GOOGLE_SCHOLAR_ID is required. Add the profile ID from the user= part "
            "of your Google Scholar profile URL as a GitHub Actions secret.",
            file=sys.stderr,
        )
        return 2

    if args.source_json:
        author = json.loads(args.source_json.read_text(encoding="utf-8"))
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

#!/usr/bin/env python3
"""Validate and optionally rewrite docs/index.json for shuotou."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "index.json"
REQUIRED = ("date", "title", "one_liner", "source", "tags", "slug", "html")


def load() -> list[dict]:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("index.json must be a JSON array")
    return data


def check(items: list[dict]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for i, item in enumerate(items):
        prefix = f"[{i}]"
        for key in REQUIRED:
            if key not in item:
                errors.append(f"{prefix} missing field: {key}")
        slug = item.get("slug")
        if slug in seen:
            errors.append(f"{prefix} duplicate slug: {slug}")
        seen.add(slug)
        html = item.get("html")
        if html:
            path = ROOT / "docs" / html
            if not path.is_file():
                errors.append(f"{prefix} missing file: docs/{html}")
        tags = item.get("tags")
        if tags is not None and not isinstance(tags, list):
            errors.append(f"{prefix} tags must be a list")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check / sort shuotou index.json")
    parser.add_argument("--check", action="store_true", help="validate only")
    parser.add_argument("--write", action="store_true", help="sort by date desc and rewrite")
    args = parser.parse_args()
    if not args.check and not args.write:
        args.check = True

    items = load()
    errors = check(items)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    if args.write:
        items.sort(key=lambda x: str(x.get("date") or ""), reverse=True)
        INDEX.write_text(
            json.dumps(items, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {INDEX} ({len(items)} entries)")
    else:
        print(f"ok · {len(items)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

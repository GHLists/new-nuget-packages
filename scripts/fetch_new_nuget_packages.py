#!/usr/bin/env python3
"""Fetch packages newly created on nuget.org.

nuget.org's search API does not expose package creation dates, so this script
reads the [v3 catalog](https://api.nuget.org/v3/catalog0/index.json), the
cursed feed of every package operation nuget.org publishes. All package IDs
touched inside the requested window are collected, and each is checked against
its registration index, whose earliest ``published`` timestamp decides whether
the package was created inside the window (older packages only appear in the
catalog when they are updated).

The catalog is capped by the pages the API exposes, so the manifest records
``source_truncated`` whenever coverage of the window is incomplete.

The end of the last list is stored in the manifest so the next run resumes
where the previous one stopped.
"""

import argparse
import csv
import datetime as dt
import http.client
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CATALOG_INDEX_URL = "https://api.nuget.org/v3/catalog0/index.json"
REGISTRATION_URL = (
    "https://api.nuget.org/v3/registration5-semver1/{package}/index.json"
)
DEFAULT_USER_AGENT = (
    "new-nuget-packages/1.0 (https://github.com/GHLists/new-nuget-packages)"
)

MAX_PAGES = 12
WORKERS = 8
DESCRIPTION_LIMIT = 300
CSV_HEADER = (
    "created_at",
    "package",
    "version",
    "authors",
    "description",
)

TRANSIENT_ERRORS = (
    urllib.error.URLError,
    TimeoutError,
    json.JSONDecodeError,
    http.client.HTTPException,
    OSError,
)


class NotFound(Exception):
    pass


def iso(moment):
    moment = moment.astimezone(dt.timezone.utc)
    if moment.microsecond:
        fraction = f"{moment.microsecond:06d}".rstrip("0")
        return moment.strftime("%Y-%m-%dT%H:%M:%S") + f".{fraction}Z"
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_timestamp(value):
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    moment = dt.datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=dt.timezone.utc)
    return moment.astimezone(dt.timezone.utc)


def timestamp_filename(moment):
    moment = moment.astimezone(dt.timezone.utc)
    stamp = moment.strftime("%Y-%m-%dT%H-%M-%S")
    if moment.microsecond:
        stamp += "-" + f"{moment.microsecond:06d}".rstrip("0")
    return stamp + "Z"


def fetch_json(url, user_agent, retries=3, backoff=5.0):
    last_error = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": user_agent, "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise NotFound(url) from error
            last_error = error
        except TRANSIENT_ERRORS as error:
            last_error = error
        if attempt < retries:
            print(f"attempt {attempt} failed ({last_error}), retrying", file=sys.stderr)
            time.sleep(backoff * attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def clean_text(value, limit=DESCRIPTION_LIMIT):
    text = " ".join(str(value or "").split())
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "\u2026"
    return text


def collect_window_ids(user_agent, retries, since, until):
    """Return package IDs touched in the window and whether coverage is whole.

    A catalog page's commitTimeStamp is the newest item commit it holds, so
    any page with a stamp later than ``since`` may contain items inside the
    window; item-level stamps provide the precision. Coverage is proven by a
    page whose stamp is at or before ``since`` (all of its items are older).
    """
    index = fetch_json(CATALOG_INDEX_URL, user_agent, retries=retries)
    pages = index.get("items")
    if not isinstance(pages, list):
        raise RuntimeError("catalog index does not contain a page list")
    due = []
    covered = False
    for page in pages:
        if not isinstance(page, dict) or not page.get("@id"):
            continue
        try:
            stamp = parse_timestamp(page["commitTimeStamp"])
        except (KeyError, TypeError, ValueError):
            continue
        if stamp <= since:
            covered = True
        else:
            due.append((stamp, page["@id"]))
    due.sort()
    due = due[:MAX_PAGES]

    ids = set()
    for _, url in due:
        page = fetch_json(url, user_agent, retries=retries)
        for item in page.get("items") or []:
            if not isinstance(item, dict):
                continue
            if "PackageDetails" not in str(item.get("@type", "")):
                continue
            try:
                stamp = parse_timestamp(item["commitTimeStamp"])
            except (KeyError, TypeError, ValueError):
                continue
            if stamp <= since or stamp > until:
                continue
            package = item.get("nuget:id")
            if isinstance(package, str) and package:
                ids.add(package)
    return ids, covered


def package_row(package, user_agent, retries, since, until):
    """Fetch the registration index and build a row, or return a status.

    Statuses: ``ok`` (package created inside the window), ``old`` (package
    existed before the window), ``empty`` (no usable timestamps), ``missing``
    (no registration index).
    """
    url = REGISTRATION_URL.format(package=urllib.parse.quote(package.lower()))
    try:
        registration = fetch_json(url, user_agent, retries=retries)
    except NotFound:
        return "missing", None
    leafs = []
    for group in registration.get("items") or []:
        leafs.extend(group.get("items") or [])
    if not leafs:
        return "empty", None
    published = []
    for leaf in leafs:
        entry = leaf.get("catalogEntry") or {}
        value = entry.get("published")
        if value:
            try:
                published.append(parse_timestamp(value))
            except (TypeError, ValueError):
                continue
    if not published:
        return "empty", None
    first = min(published)
    if not (since < first <= until):
        return "old", None
    latest_entry = leafs[-1].get("catalogEntry") or {}
    authors = latest_entry.get("authors")
    if isinstance(authors, list):
        authors_text = "; ".join(str(name) for name in authors)
    else:
        authors_text = authors or ""
    row = {
        "created_at": iso(first),
        "package": package,
        "version": clean_text(latest_entry.get("version"), 20),
        "authors": clean_text(authors_text, 100),
        "description": clean_text(latest_entry.get("description")),
    }
    return "ok", row


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def read_manifest_text(path):
    """Read the manifest from disk, or fall back to the committed copy.

    The workflow checks out only ``scripts`` from the repository, so the
    manifest can be missing from the working tree even though it is committed.
    """
    manifest_path = Path(path)
    try:
        return manifest_path.read_text(encoding="utf-8")
    except OSError:
        pass
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{manifest_path.as_posix()}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout


def load_manifest(path):
    text = read_manifest_text(path)
    if text is None:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"manifest {path} is not valid JSON") from error
    if not isinstance(data, dict):
        raise RuntimeError(f"manifest {path} must contain a JSON object")
    version = data.get("state_version", 1)
    if version != 1:
        raise RuntimeError(f"manifest {path} has an unsupported state version")
    return data


def save_manifest(path, manifest):
    manifest_path = Path(path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = manifest_path.with_name(f".{manifest_path.name}.tmp")
    text = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, manifest_path)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        help="UTC start timestamp as ISO 8601 (default: end of the last list)",
    )
    parser.add_argument(
        "--until",
        help="UTC end timestamp as ISO 8601 (default: now)",
    )
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--manifest", default="latest.json")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--lookback-hours",
        type=float,
        default=1.0,
        help="window length when no previous list exists (default: 1)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    until = parse_timestamp(args.until) if args.until else now
    manifest = load_manifest(args.manifest)

    if args.since:
        since = parse_timestamp(args.since)
        if "window" in manifest:
            stored_window = parse_timestamp(manifest["window"])
            if since < stored_window:
                raise RuntimeError(
                    "backfill would move the window backwards; "
                    f"the manifest window is {iso(stored_window)}"
                )
    elif "window" in manifest:
        since = parse_timestamp(manifest["window"])
    else:
        since = until - dt.timedelta(hours=args.lookback_hours)

    ids, covered = collect_window_ids(args.user_agent, args.retries, since, until)
    truncated = not covered
    if truncated:
        print(
            "catalog coverage of the window is incomplete; some packages "
            "in this window may be missing",
            file=sys.stderr,
        )

    rows = []
    skipped = 0
    statuses = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {
            package: pool.submit(
                package_row, package, args.user_agent, args.retries, since, until
            )
            for package in sorted(ids)
        }
        for package, future in futures.items():
            try:
                status, row = future.result()
            except RuntimeError as error:
                print(f"failed to check {package}: {error}", file=sys.stderr)
                statuses[package] = "error"
                skipped += 1
                continue
            statuses[package] = status
            if status == "ok":
                rows.append(row)
            else:
                skipped += 1
    counts = {}
    for status in statuses.values():
        counts[status] = counts.get(status, 0) + 1
    print(f"checked {len(statuses)} packages: {counts}", file=sys.stderr)
    if skipped:
        print(f"skipped {skipped} packages without creation data", file=sys.stderr)

    rows.sort(key=lambda row: row["created_at"])
    manifest["window"] = iso(until)
    manifest["source_truncated"] = bool(truncated)
    if rows:
        output = (
            Path(args.output_dir)
            / f"new-nuget-packages-{timestamp_filename(until)}.csv"
        )
        write_csv(output, rows)
        manifest["list"] = {
            "path": output.as_posix(),
            "from": iso(since),
            "to": iso(until),
            "count": len(rows),
        }
        print(
            f"wrote {len(rows)} packages created between {iso(since)} "
            f"and {iso(until)} to {output}"
        )
    else:
        print(f"no new packages between {iso(since)} and {iso(until)}")
    save_manifest(args.manifest, manifest)
    return 0


if __name__ == "__main__":
    sys.exit(main())

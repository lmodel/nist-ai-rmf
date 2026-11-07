#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check what this repository is built from against what its sources serve.

Three things can change with no change in this repository. Each repository it vendors
modules from can publish a release, lmodel/iso42001 can publish its first, and the
crosswalk at NIST's AI Resource Center can change. The script asks GitHub for the
releases and compares the crosswalk's SHA-256 with its pin. The publications themselves
are the two vendoring repositories' watch.

It prints a Markdown report and exits 1 when something moved or a check could not finish.
Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "lmodel-nist-ai-rmf-upstream-check"

# The repository, and the release its modules are vendored from. tests/test_upstream.py
# holds the vendored files to their hashes.
VENDORED_FROM = {
    "lmodel/nist-ai-100-1": "v0.1.0",
    "lmodel/nist-ai-600-1": "v0.1.0",
}

# A repository whose first release this one waits for, and where its schema asset goes.
# Until that copy is there, scripts/build_crosswalk.py leaves the crosswalk's objects
# unchecked, so the check asks GitHub only while the copy is missing.
AWAITED = {"lmodel/iso42001": "tests/neighbours/iso42001.yaml"}

# The crosswalk's address and SHA-256, as compared on 2026-11-05. scripts/build_crosswalk.py
# holds the same pin, and the repository carries no copy.
CROSSWALK_URL = "https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf"
CROSSWALK_SHA256 = "170efdf7be08a988213b54fb8293f3ea67f0627aff6f0541052dfbb0744afed3"

# The hosts a request may reach, and the most it reads. The pinned file is far smaller.
ALLOWED_HOSTS = {"airc.nist.gov", "api.github.com"}
MAX_BYTES = 20 * 1024 * 1024


class _HttpsOnly(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only over https, and only to a host the script reads from."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
            raise urllib.error.URLError(f"refused a redirect to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _download(url: str) -> bytes:
    """A public file. It carries no token, and the address it starts from is held to the
    same rule as a redirect."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise urllib.error.URLError(f"refused to read {url}")
    opener = urllib.request.build_opener(_HttpsOnly)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with opener.open(req, timeout=120) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise urllib.error.URLError(f"{url} answered with more than {MAX_BYTES} bytes")
    return data


def _code(text: object) -> str:
    """Text a server chose, such as a tag name or an error that quotes a redirect target,
    as a code span on one line, so it cannot mention a person or add a link in the issue."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def _latest_release(repository: str) -> str | None:
    """The repository's latest release tag, or None when it has none."""
    url = f"https://api.github.com/repos/{repository}/releases/latest"
    try:
        return json.loads(_download(url))["tag_name"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def check_vendored() -> tuple[list[str], bool]:
    """Report any release the vendored modules are not from."""
    report, attention = [], False
    for repository, pinned in sorted(VENDORED_FROM.items()):
        latest = _latest_release(repository)
        if latest == pinned:
            report.append(
                f"- {repository}: vendored from `{pinned}`, its latest state."
            )
        elif latest is None:
            attention = True
            report.append(
                f"- **{repository} has no release now, and the modules here are from "
                f"`{pinned}`.** Find out why before you move a pin."
            )
        else:
            attention = True
            report.append(
                f"- **{repository} released {_code(latest)}, and the modules here are from "
                f"`{pinned}`.** Copy its modules and asset, move the pins, and run `just test`."
            )
    return report, attention


def check_awaited() -> tuple[list[str], bool]:
    """Report a first release whose schema asset is not copied here yet."""
    report, attention = [], False
    for repository, copy in sorted(AWAITED.items()):
        if (ROOT / copy).exists():
            report.append(f"- {repository}: its copy is at `{copy}`.")
            continue
        latest = _latest_release(repository)
        if latest is None:
            report.append(
                f"- {repository}: no release yet, so the crosswalk's objects go unchecked."
            )
        else:
            attention = True
            report.append(
                f"- **{repository} released {_code(latest)}.** Copy its schema asset to "
                f"`{copy}`, pin it in `tests/test_schema_rules.py`, and run "
                "`just build-crosswalk`."
            )
    return report, attention


def check_crosswalk() -> tuple[list[str], bool]:
    """Report whether the crosswalk is the pinned bytes."""
    if hashlib.sha256(_download(CROSSWALK_URL)).hexdigest() == CROSSWALK_SHA256:
        return [f"- {CROSSWALK_URL} matches its pin."], False
    return [
        f"- **{CROSSWALK_URL} now serves other bytes.** Read the change, move the pin in both "
        "scripts and run `just build-crosswalk`."
    ], True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for check in (check_vendored, check_awaited, check_crosswalk):
        try:
            found, moved = check()
        # OSError covers a refused or failed fetch, a timeout and URLError;
        # HTTPException a connection cut off mid-read; KeyError and ValueError
        # an answer that is not the JSON the check expects.
        except (OSError, http.client.HTTPException, KeyError, ValueError) as err:
            found, moved = [f"- **A check could not finish: {_code(err)}.**"], True
        lines += found
        attention = attention or moved
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())

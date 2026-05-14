"""Validate the NIST AI RMF Playbook JSON against the schema.

The published Playbook
(https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) is distributed
as a top-level JSON *array* with attribute keys that include spaces
("AI Actors", "Topic"). To validate it against the schema's
``PlaybookCollection`` class this script:

1. Renames ``AI Actors`` -> ``ai_actors`` and ``Topic`` -> ``topic`` on
   each entry.
2. Wraps the array in a ``{"entries": [...]}`` object so it matches
   the ``PlaybookCollection`` tree-root shape.
3. Invokes ``linkml-validate`` on the transformed payload.

The original JSON file is *not* modified - the transformation is
performed in-memory and written to a temporary file. This lets NIST
refresh the Playbook (twice a year, per the AI RMF update schedule)
without having to keep a hand-maintained copy in sync.

Usage::

    python -m scripts.validate_playbook \
        tests/data/third_party/nist/nist_ai_rmf_playbook.json

Or via Just::

    just validate-playbook
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_ANSI_GREEN = "\033[32m"
_ANSI_RED = "\033[31m"
_ANSI_RESET = "\033[0m"


def _colour(text: str, code: str) -> str:
    """Wrap *text* in an ANSI colour escape when stdout is a real terminal."""
    if os.isatty(sys.stdout.fileno()):
        return f"{code}{text}{_ANSI_RESET}"
    return text

REPO_ROOT = Path(__file__).resolve().parent.parent
# PlaybookCollection lives in the core module; use the core schema
# directly so we don't pull GAI imports we don't need.
DEFAULT_SCHEMA = REPO_ROOT / "src" / "nist_ai_rmf" / "schema" / "nist_ai_rmf_core.yaml"
DEFAULT_INPUT = (
    REPO_ROOT / "tests" / "data" / "third_party" / "nist" / "nist_ai_rmf_playbook.json"
)
TARGET_CLASS = "PlaybookCollection"

# Mapping from raw Playbook JSON keys to the schema's snake_case slot
# names. Add new entries here if NIST changes future Playbook releases.
KEY_RENAMES = {
    "AI Actors": "ai_actors",
    "Topic": "topic",
}


def transform_entry(entry: dict) -> dict:
    """Rename non-snake_case keys in a single Playbook entry."""
    return {KEY_RENAMES.get(k, k): v for k, v in entry.items()}


def load_and_transform(input_path: Path) -> dict:
    """Return the Playbook JSON wrapped as a ``PlaybookCollection`` payload."""
    with input_path.open() as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise SystemExit(
            f"Expected a JSON array at {input_path}, found {type(data).__name__}"
        )

    return {"entries": [transform_entry(e) for e in data]}


def run_linkml_validate(schema: Path, payload_path: Path) -> int:
    """Invoke linkml-validate and stream its output."""
    cmd = [
        "linkml-validate",
        "--schema",
        str(schema),
        "--target-class",
        TARGET_CLASS,
        str(payload_path),
    ]
    print(f"$ {' '.join(cmd)}", file=sys.stderr)
    result = subprocess.run(cmd, check=False)
    return result.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT,
        help=(
            "Path to the NIST AI RMF Playbook JSON "
            f"(default: {DEFAULT_INPUT.relative_to(REPO_ROOT)})"
        ),
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help=f"Path to the LinkML schema (default: {DEFAULT_SCHEMA.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--keep-transformed",
        type=Path,
        default=None,
        help=(
            "If given, write the transformed payload to this path "
            "instead of using a temporary file. Useful for debugging."
        ),
    )
    args = parser.parse_args(argv)

    if shutil.which("linkml-validate") is None:
        raise SystemExit(
            "linkml-validate not on PATH. Install dev dependencies with `uv sync --group dev`."
        )

    if not args.input.exists():
        raise SystemExit(f"Playbook JSON not found: {args.input}")
    if not args.schema.exists():
        raise SystemExit(f"Schema not found: {args.schema}")

    payload = load_and_transform(args.input)
    n_entries = len(payload["entries"])

    if args.keep_transformed is not None:
        args.keep_transformed.parent.mkdir(parents=True, exist_ok=True)
        args.keep_transformed.write_text(json.dumps(payload, indent=2))
        return run_linkml_validate(args.schema, args.keep_transformed)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", prefix="playbook-", delete=False
    ) as tmp:
        json.dump(payload, tmp, indent=2)
        tmp_path = Path(tmp.name)

    try:
        rc = run_linkml_validate(args.schema, tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)

    if rc == 0:
        print(_colour(
            f"OK: {n_entries} Playbook entries validated against {TARGET_CLASS}"
            f" \u2014 {n_entries} tests done.",
            _ANSI_GREEN,
        ))
    else:
        print(_colour(
            f"FAILED: Playbook validation exited with code {rc}.",
            _ANSI_RED,
        ))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())

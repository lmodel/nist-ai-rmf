#!/usr/bin/env python3
"""Write the AI RMF to ISO/IEC 42001 crosswalk as an SSSOM set, from its provider's PDF.

NIST's AI Resource Center lists this crosswalk, which Microsoft provided, and states no
licence for it. So the repository carries neither the PDF, which also quotes ISO's
headings, nor its pairs. This script reads the pinned PDF and writes the set under `tmp/`,
which git ignores. It stops when a subject is not one of the AI RMF's 72 subcategories, or
when lmodel/iso42001's copy is present and an object is not in it.

Usage::

    uv run python scripts/build_crosswalk.py [--pdf FILE] [--output FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "tests" / "upstream" / "ai-rmf-1.0.yaml"
ISO42001_COPY = ROOT / "tests" / "neighbours" / "iso42001.yaml"
OUTPUT = ROOT / "tmp" / "mappings" / "nist-ai-rmf-to-iso42001.sssom.tsv"
USER_AGENT = "lmodel-nist-ai-rmf-crosswalk"

# The address and SHA-256 of the PDF, as compared on 2026-11-05. The watch holds the same pin.
PDF_URL = "https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf"
PDF_SHA256 = "170efdf7be08a988213b54fb8293f3ea67f0627aff6f0541052dfbb0744afed3"
ALLOWED_HOSTS = {"airc.nist.gov"}
MAX_BYTES = 20 * 1024 * 1024

# The column the PDF prints a clause number in, in points from the left.
NUMBER_COLUMN = (250, 340)
SUBCATEGORY_COLUMN_ENDS = 80
SUBCATEGORY = re.compile(r"^\d+\.\d+$")
FUNCTIONS = {"Govern", "Map", "Measure", "Manage"}
NUMBER = re.compile(r"^(\d+(\.+\d+)*|B\.\d+(\.\d+)*)$")

# What the PDF prints that is not a clause number as ISO/IEC 42001 gives it.
MISPRINTED_NUMBERS = {"7..2": "7.2"}

# Rows that print a number with a heading the PDF gives it nowhere else, read from the PDF
# alone. A row keeps the number, and its comment says so. `check` proves each is still there.
HEADING_OF_ANOTHER = {
    ("GOVERN 3.2", "B.3.2"): "the heading it gives 9.3.2 elsewhere",
    ("MAP 1.4", "B.2.2"): "the heading it gives B.10.4 elsewhere",
    ("MAP 1.5", "6.1.1"): "a heading it gives this number nowhere else",
}

HEADER = f"""# curie_map:
#   iso42001: https://w3id.org/lmodel/iso42001/
#   nist_ai_100_1: https://w3id.org/lmodel/nist-ai-100-1/
#   semapv: https://w3id.org/semapv/vocab/
#   skos: http://www.w3.org/2004/02/skos/core#
# mapping_set_id: https://w3id.org/lmodel/nist-ai-rmf/mappings/nist-ai-rmf-to-iso42001
# mapping_set_title: AI RMF 1.0 to ISO/IEC 42001 crosswalk
# mapping_set_description: Every pair in the crosswalk Microsoft provided and NIST's AI Resource Center lists. It was written against ISO/IEC FDIS 42001, and nothing here compares it with the published text. The comment column names each row whose number and heading disagree within the document.
# license: {PDF_URL}
# mapping_provider: https://airc.nist.gov/airmf-resources/crosswalks/
# other: "mapping_source: {PDF_URL}"
# mapping_date: 2023-05-23
# subject_source: https://w3id.org/lmodel/nist-ai-100-1
# subject_source_version: "1.0"
# object_source: https://w3id.org/lmodel/iso42001
# object_source_version: ISO/IEC 42001:2023
"""
COLUMNS = (
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "mapping_justification",
    "comment",
)


def read_pairs(data: bytes) -> list[tuple[str, str, str]]:
    """Every (subcategory, number as printed, heading) in reading order."""
    import pdfplumber  # A development dependency, so the watch and the tests need none of it.

    pairs, subcategory = [], None
    with pdfplumber.open(io.BytesIO(data)) as pdf:
        for page in pdf.pages:
            lines = defaultdict(list)
            for word in page.extract_words(x_tolerance=1.5, y_tolerance=2):
                lines[round(word["top"] / 2)].append(word)
            for key in sorted(lines):
                words = sorted(lines[key], key=lambda w: w["x0"])
                if (
                    len(words) > 1
                    and words[0]["x0"] < SUBCATEGORY_COLUMN_ENDS
                    and words[0]["text"] in FUNCTIONS
                    and SUBCATEGORY.match(words[1]["text"])
                ):
                    subcategory = f"{words[0]['text'].upper()} {words[1]['text']}"
                for index, word in enumerate(words):
                    if (
                        subcategory
                        and NUMBER_COLUMN[0] < word["x0"] < NUMBER_COLUMN[1]
                        and NUMBER.match(word["text"])
                    ):
                        heading = " ".join(w["text"] for w in words[index + 1 :])
                        pairs.append((subcategory, word["text"], heading))
                        break
    return pairs


def object_of(number: str) -> tuple[str, str]:
    """The IRI and label of what a printed number names. Annex B holds the guidance for the
    Annex A control of the same number, so a B number names that control."""
    number = MISPRINTED_NUMBERS.get(number, number)
    if number.startswith("B."):
        control = "A." + number[2:]
        return (
            f"iso42001:AimsAnnexAControl#{control.lower().replace('.', '_')}",
            control,
        )
    return f"iso42001:AimsClause#clause_{number.replace('.', '_')}", number


def row_of(subcategory: str, number: str) -> dict[str, str]:
    """One SSSOM row for a pair."""
    object_id, object_label = object_of(number)
    notes = []
    if number.startswith("B."):
        notes.append(f"Cited as {number}, the guidance for this control.")
    if number in MISPRINTED_NUMBERS:
        notes.append(f"Printed as {number}.")
    if (subcategory, number) in HEADING_OF_ANOTHER:
        printed = HEADING_OF_ANOTHER[(subcategory, number)]
        notes.append(f"The row prints this number with {printed}; it keeps the number.")
    return {
        "subject_id": f"nist_ai_100_1:Subcategory#{subcategory.replace(' ', '_')}",
        "subject_label": subcategory,
        "predicate_id": "skos:relatedMatch",
        "object_id": object_id,
        "object_label": object_label,
        "mapping_justification": "semapv:ManualMappingCuration",
        "comment": " ".join(notes),
    }


def rows_of(pairs: list[tuple[str, str, str]]) -> list[dict[str, str]]:
    """One row per distinct pair, in the PDF's order: it repeats a row at least once."""
    seen, rows = set(), []
    for subcategory, number, _heading in pairs:
        if (subcategory, number) not in seen:
            seen.add((subcategory, number))
            rows.append(row_of(subcategory, number))
    return rows


def check(
    pairs: list[tuple[str, str, str]],
    rows: list[dict[str, str]],
    subcategories: set[str],
    objects: set[str] | None,
) -> list[str]:
    """What stops the set: a subject or object that does not exist, a subcategory with no
    row, or a listed misprint the PDF no longer holds. With no copy to read, `objects` is
    None and the objects go unchecked."""
    problems = []
    labels = {row["subject_label"] for row in rows}
    problems += [f"{s}: not a subcategory" for s in sorted(labels - subcategories)]
    problems += [f"{s}: has no row" for s in sorted(subcategories - labels)]
    problems += [
        f"{row['subject_label']}: {row['object_id']} is not in the copy"
        for row in rows
        if objects is not None and row["object_id"] not in objects
    ]
    headings = defaultdict(set)
    for _subcategory, number, heading in pairs:
        headings[number].add(heading)
    printed = {(s, n) for s, n, _h in pairs}
    for pair in HEADING_OF_ANOTHER:
        if pair not in printed:
            problems.append(f"{pair}: the listed row is gone from the PDF")
        elif len(headings[pair[1]]) < 2:
            problems.append(f"{pair}: the number now has one heading")
    return problems


def tsv(rows: list[dict[str, str]]) -> str:
    """The set as SSSOM's TSV form."""
    lines = ["\t".join(COLUMNS)]
    lines += ["\t".join(row[column] for column in COLUMNS) for row in rows]
    return HEADER + "\n".join(lines) + "\n"


def _download() -> bytes:
    parts = urllib.parse.urlsplit(PDF_URL)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise urllib.error.URLError(f"refused to read {PDF_URL}")
    req = urllib.request.Request(PDF_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise urllib.error.URLError(
            f"{PDF_URL} answered with more than {MAX_BYTES} bytes"
        )
    return data


def _subcategories() -> set[str]:
    framework = yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))
    return {
        subcategory["ai_rmf_subcategory_id"]
        for function in framework["ai_rmf_functions"]
        for category in function["ai_rmf_function_categories"]
        for subcategory in category["ai_rmf_category_subcategories"]
    }


def _objects() -> set[str] | None:
    if not ISO42001_COPY.exists():
        print(
            "No copy of lmodel/iso42001 in tests/neighbours/, so the objects go unchecked."
        )
        return None
    enums = yaml.safe_load(ISO42001_COPY.read_text(encoding="utf-8"))["enums"]
    return {
        f"iso42001:{enum}#{value}"
        for enum in ("AimsClause", "AimsAnnexAControl")
        for value in enums[enum]["permissible_values"]
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--pdf", type=Path, help="Read this copy instead of downloading"
    )
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args(argv)
    data = args.pdf.read_bytes() if args.pdf else _download()
    if hashlib.sha256(data).hexdigest() != PDF_SHA256:
        print("The PDF is not the pinned one. Read the change, then move the pin.")
        return 1
    pairs = read_pairs(data)
    rows = rows_of(pairs)
    problems = check(pairs, rows, _subcategories(), _objects())
    if problems:
        print("\n".join(problems))
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(tsv(rows), encoding="utf-8")
    print(f"Wrote {len(rows)} rows to {args.output}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

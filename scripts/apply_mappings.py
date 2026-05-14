"""Verify that the LinkML schemas reflect the SSSOM mapping TSV files.

The SSSOM TSV files under ``src/nist_ai_rmf/mappings/`` are the
authoritative source of cross-vocabulary mappings. This script reads
them and confirms that the corresponding ``exact_mappings`` /
``close_mappings`` / ``broad_mappings`` / ``narrow_mappings`` /
``related_mappings`` fields are present on the matching elements in
the LinkML schemas at ``src/nist_ai_rmf/schema/``.

This is a *verifier* (read-only) so that the hand-curated YAML
comments and formatting in the schemas are never disturbed. If a
mapping is in the TSV but missing from the schema (or vice versa) the
script prints a diff and exits non-zero.

Run via ``just verify-mappings`` (or directly:
``python scripts/apply_mappings.py``).
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "src" / "nist_ai_rmf" / "schema"
MAPPINGS_DIR = REPO_ROOT / "src" / "nist_ai_rmf" / "mappings"

# SSSOM subject prefix -> the schema YAML that *defines* those subjects.
# `nist_ai_rmf` CURIEs resolve to classes in the `nist_ai_rmf_core`
# module (the umbrella `nist_ai_rmf.yaml` is a pure import wrapper).
SUBJECT_TO_SCHEMA: dict[str, Path] = {
    "nist_ai_rmf": SCHEMA_DIR / "nist_ai_rmf_core.yaml",
    "nist_ai_rmf_gai": SCHEMA_DIR / "nist_ai_rmf_gai.yaml",
}

PREDICATE_TO_FIELD: dict[str, str] = {
    "skos:exactMatch": "exact_mappings",
    "skos:closeMatch": "close_mappings",
    "skos:broadMatch": "broad_mappings",
    "skos:narrowMatch": "narrow_mappings",
    "skos:relatedMatch": "related_mappings",
}

ELEMENT_SECTIONS = ("classes", "slots", "enums", "types")


def parse_sssom_tsv(path: Path) -> list[dict[str, str]]:
    """Return the SSSOM data rows (header comment lines are skipped)."""
    text_lines = [
        ln for ln in path.read_text().splitlines() if not ln.lstrip().startswith("#")
    ]
    reader = csv.DictReader(io.StringIO("\n".join(text_lines)), delimiter="\t")
    return [row for row in reader if row.get("subject_id")]


def expected_mappings(rows: list[dict[str, str]]) -> dict[str, dict[str, set[str]]]:
    """``{local_name: {field: {object_curie, ...}}}`` derived from TSV."""
    expected: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for row in rows:
        predicate = row["predicate_id"]
        if predicate not in PREDICATE_TO_FIELD:
            print(
                f"WARNING: unsupported predicate {predicate!r} (subject={row['subject_id']})",
                file=sys.stderr,
            )
            continue
        local = row["subject_id"].split(":", 1)[-1]
        field = PREDICATE_TO_FIELD[predicate]
        expected[local][field].add(row["object_id"])
    return expected


def actual_mappings(schema: dict, name: str) -> dict[str, set[str]]:
    """Read mapping fields off the schema element."""
    for section in ELEMENT_SECTIONS:
        element = (schema.get(section) or {}).get(name)
        if element is not None:
            return {
                field: set(element.get(field) or [])
                for field in PREDICATE_TO_FIELD.values()
            }
    return {}


def find_section(schema: dict, name: str) -> str | None:
    for section in ELEMENT_SECTIONS:
        if name in (schema.get(section) or {}):
            return section
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also fail when the schema has mappings that the TSV does not declare.",
    )
    args = parser.parse_args(argv)

    overall_missing: list[str] = []
    overall_extra: list[str] = []
    overall_unknown: list[str] = []

    for tsv in sorted(MAPPINGS_DIR.glob("*.sssom.tsv")):
        rows = parse_sssom_tsv(tsv)
        print(f"== {tsv.name} ({len(rows)} mappings) ==")

        per_schema: dict[Path, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            prefix = row["subject_id"].split(":", 1)[0]
            path = SUBJECT_TO_SCHEMA.get(prefix)
            if path is None:
                print(f"  WARN: unknown subject prefix {prefix!r}")
                continue
            per_schema[path].append(row)

        for schema_path, schema_rows in per_schema.items():
            schema = yaml.safe_load(schema_path.read_text())
            expected = expected_mappings(schema_rows)
            for name, fields in sorted(expected.items()):
                section = find_section(schema, name)
                if section is None:
                    msg = f"{schema_path.name}: element {name!r} not found in schema"
                    overall_unknown.append(msg)
                    print(f"  MISSING-ELEMENT: {msg}")
                    continue
                actual = actual_mappings(schema, name)
                for field, exp_set in fields.items():
                    act_set = actual.get(field, set())
                    missing = exp_set - act_set
                    extra = act_set - exp_set
                    if missing:
                        msg = (
                            f"{schema_path.name}: {section}.{name}.{field} "
                            f"missing: {sorted(missing)}"
                        )
                        overall_missing.append(msg)
                        print(f"  MISSING: {msg}")
                    if extra and args.strict:
                        msg = (
                            f"{schema_path.name}: {section}.{name}.{field} "
                            f"extra (not in TSV): {sorted(extra)}"
                        )
                        overall_extra.append(msg)
                        print(f"  EXTRA: {msg}")
            if not (overall_missing or overall_unknown):
                print(f"  OK: {schema_path.name}")

    print()
    print(f"Summary: missing={len(overall_missing)} extra={len(overall_extra)} unknown={len(overall_unknown)}")
    if overall_missing or overall_unknown:
        print(
            "\nApply the missing mappings to the schema YAML, "
            "or remove the rows from the SSSOM TSV.",
            file=sys.stderr,
        )
        return 1
    if overall_extra and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

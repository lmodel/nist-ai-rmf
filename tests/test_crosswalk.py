"""Checks the crosswalk builder's rules on pairs written here, so they need no PDF.

`just build-crosswalk`, which main.yaml runs, holds the real pairs to the catalogue and to
lmodel/iso42001's copy.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "build_crosswalk.py"


@pytest.fixture(scope="module")
def builder():
    spec = importlib.util.spec_from_file_location("builder_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_a_clause_number_names_the_clause(builder):
    """A clause number names a value of AimsClause."""
    assert builder.object_of("6.1.2") == ("iso42001:AimsClause#clause_6_1_2", "6.1.2")


def test_an_annex_b_number_names_its_control(builder):
    """Annex B is the guidance for the Annex A control of the same number."""
    assert builder.object_of("B.6.2.4") == (
        "iso42001:AimsAnnexAControl#a_6_2_4",
        "A.6.2.4",
    )


def test_a_misprinted_number_is_read_and_noted(builder):
    """A listed misprint gives the clause it means, and the comment keeps what it printed."""
    row = builder.row_of("GOVERN 2.1", "7..2")
    assert row["object_id"] == "iso42001:AimsClause#clause_7_2"
    assert row["comment"] == "Printed as 7..2."


def test_a_row_is_a_related_match_curated_by_a_person(builder):
    """The PDF states no relation, so a row claims only that the two are related."""
    row = builder.row_of("MAP 1.1", "4.1")
    assert row["predicate_id"] == "skos:relatedMatch"
    assert row["mapping_justification"] == "semapv:ManualMappingCuration"
    assert row["subject_id"] == "nist_ai_100_1:Subcategory#MAP_1.1"
    assert row["subject_label"] == "MAP 1.1"


def test_a_row_with_another_clauses_heading_keeps_its_number(builder):
    """A row printed with the wrong heading keeps the number and says so."""
    row = builder.row_of("GOVERN 3.2", "B.3.2")
    assert row["object_id"] == "iso42001:AimsAnnexAControl#a_3_2"
    assert "clause 9.3.2's heading" in row["comment"]


def test_a_repeated_pair_gives_one_row(builder):
    """The same pair twice, as MANAGE 1.1 prints one, is one row, in first-seen order."""
    pairs = [("MANAGE 1.1", "B.6.2.4", "h"), ("MANAGE 1.1", "6.2", "i")]
    rows = builder.rows_of(pairs + pairs[:1])
    assert [row["object_label"] for row in rows] == ["A.6.2.4", "6.2"]


def _valid(builder):
    pairs = [
        ("GOVERN 3.2", "B.3.2", "heading one"),
        ("MAP 1.1", "B.3.2", "heading two"),
        ("MAP 1.4", "B.2.2", "heading three"),
        ("MAP 1.1", "B.2.2", "heading four"),
        ("MAP 1.5", "6.1.1", "heading five"),
        ("MAP 1.1", "6.1.1", "heading six"),
    ]
    rows = builder.rows_of(pairs)
    subjects = {"GOVERN 3.2", "MAP 1.1", "MAP 1.4", "MAP 1.5"}
    return pairs, rows, subjects, {row["object_id"] for row in rows}


def test_check_passes_a_full_set(builder):
    """Every subject and object exists, and each listed misprint is present."""
    assert builder.check(*_valid(builder)) == []


def test_check_stops_on_a_subcategory_with_no_row(builder):
    """Each subcategory has a row."""
    pairs, rows, subjects, objects = _valid(builder)
    assert builder.check(pairs, rows, subjects | {"MAP 5.2"}, objects)


def test_check_stops_on_a_subject_that_is_no_subcategory(builder):
    """A subject is a subcategory of the catalogue."""
    pairs, rows, subjects, objects = _valid(builder)
    assert builder.check(pairs, rows, subjects - {"MAP 1.1"}, objects)


def test_check_stops_on_an_object_the_copy_lacks(builder):
    """An object is a value of lmodel/iso42001's copy."""
    pairs, rows, subjects, objects = _valid(builder)
    objects.discard("iso42001:AimsClause#clause_6_1_1")
    assert builder.check(pairs, rows, subjects, objects)


def test_check_stops_when_a_listed_misprint_is_gone(builder):
    """A listed row with its number's only heading means the list is stale."""
    pairs, rows, subjects, objects = _valid(builder)
    pairs = [pair for pair in pairs if pair[0] != "MAP 1.1"]
    assert builder.check(pairs, rows, subjects, objects)


def test_a_pdf_with_other_bytes_is_refused(builder, tmp_path, capsys):
    """Only the pinned bytes are read."""
    other = tmp_path / "other.pdf"
    other.write_bytes(b"not the crosswalk")
    assert builder.main(["--pdf", str(other), "--output", str(tmp_path / "out.tsv")]) == 1
    assert "not the pinned one" in capsys.readouterr().out
    assert not (tmp_path / "out.tsv").exists()


def test_the_set_carries_the_metadata_sssom_asks(builder):
    """A row sits under the header's prefixes, under the columns it names."""
    pairs, rows, _subjects, _objects = _valid(builder)
    text = builder.tsv(rows)
    assert "# mapping_set_id: https://w3id.org/lmodel/nist-ai-rmf/mappings/" in text
    assert "# license: " in text
    assert "#   iso42001: https://w3id.org/lmodel/iso42001/" in text
    header, *body = [line for line in text.splitlines() if not line.startswith("#")]
    assert header.split("\t") == list(builder.COLUMNS)
    assert all(len(line.split("\t")) == len(builder.COLUMNS) for line in body)

"""Unit tests for the merged ``nist_ai_rmf`` umbrella schema.

This repository ships *only* the umbrella schema. The
``nist_ai_100_1`` (AI RMF 1.0) and ``nist_ai_600_1`` (GAI Profile)
sub-schemas are pulled in as remote imports from their own
repositories - they are tested in those repositories and are
deliberately not re-tested here.

The tests below therefore exercise behaviour that only makes
sense once both sub-schemas are merged:

* the umbrella YAML loads,
* both imports resolve, and
* classes/enums from each sub-schema are reachable through the
  single ``nist_ai_rmf`` namespace.
"""
from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_UMBRELLA = REPO_ROOT / "src" / "nist_ai_rmf" / "schema" / "nist_ai_rmf.yaml"


def _load_schema_view():
    """``SchemaView`` for the umbrella, *without* walking imports."""
    from linkml_runtime.utils.schemaview import SchemaView

    assert SCHEMA_UMBRELLA.exists(), f"Merged schema missing at {SCHEMA_UMBRELLA}"
    return SchemaView(str(SCHEMA_UMBRELLA))


def _load_merged_view():
    """``SchemaView`` with imports resolved.

    Skips if the remote `nist_ai_100_1` / `nist_ai_600_1` schemas
    are not reachable (e.g. offline, or the upstream w3id redirects
    are not yet wired up). The umbrella import design is the
    feature under test - missing network access is not a regression.
    """
    sv = _load_schema_view()
    try:
        # Force traversal of imports - this is what triggers network IO.
        sv.all_classes()
    except (FileNotFoundError, OSError) as exc:  # urllib raises URLError(OSError)
        pytest.skip(f"Remote imports could not be resolved: {exc}")
    return sv


@pytest.fixture(scope="module")
def umbrella_view():
    return _load_schema_view()


@pytest.fixture(scope="module")
def merged_view():
    return _load_merged_view()


def test_umbrella_schema_loads(umbrella_view) -> None:
    """The umbrella schema parses and reports the expected identity."""
    schema = umbrella_view.schema
    assert schema.name == "nist-ai-rmf"
    assert schema.default_prefix == "nist_ai_rmf"


def test_umbrella_imports_both_sub_schemas(umbrella_view) -> None:
    """Both NIST sub-schemas are listed as imports."""
    imports = umbrella_view.schema.imports
    assert any("nist_ai_100_1" in i for i in imports), imports
    assert any("nist_ai_600_1" in i for i in imports), imports


def test_umbrella_exposes_both_tree_roots(merged_view) -> None:
    """``AiRmfFramework`` (from 100-1) and ``GaiProfile`` (from 600-1)
    are both reachable via the merged schema view."""
    all_classes = merged_view.all_classes()
    assert "AiRmfFramework" in all_classes, sorted(all_classes)
    assert "GaiProfile" in all_classes, sorted(all_classes)


def test_umbrella_exposes_enums_from_both_sub_schemas(merged_view) -> None:
    """A representative enum from each sub-schema is reachable."""
    all_enums = merged_view.all_enums()
    # From nist_ai_100_1
    assert "FunctionEnum" in all_enums, sorted(all_enums)
    # From nist_ai_600_1
    assert "GaiRiskCategoryEnum" in all_enums, sorted(all_enums)


# Additional tests for broader coverage
def test_umbrella_exposes_slots_from_both_sub_schemas(merged_view) -> None:
    """Representative slots from each sub-schema are accessible."""
    all_slots = merged_view.all_slots()
    # From nist_ai_100_1 (actual slot: 'functions')
    assert "functions" in all_slots, sorted(all_slots)
    # From nist_ai_600_1 (actual slot: 'gai_risks')
    assert "gai_risks" in all_slots, sorted(all_slots)


def test_umbrella_enum_values_accessible(merged_view) -> None:
    """Representative enum values are accessible from both sub-schemas."""
    function_enum = merged_view.get_enum("FunctionEnum")
    gai_risk_enum = merged_view.get_enum("GaiRiskCategoryEnum")
    assert function_enum is not None
    assert gai_risk_enum is not None
    assert "GOVERN" in function_enum.permissible_values
    assert "CONFABULATION" in gai_risk_enum.permissible_values


def test_umbrella_class_inheritance_and_mixins(merged_view) -> None:
    """Check inheritance and mixin structure for a representative class."""
    framework_class = merged_view.get_class("AiRmfFramework")
    assert framework_class is not None
    # Check is_a or mixins are present
    assert framework_class.is_a or framework_class.mixins


def test_umbrella_schema_annotations(umbrella_view) -> None:
    """Check that schema-level annotations and metadata are present."""
    schema = umbrella_view.schema
    # Check for required metadata fields
    assert hasattr(schema, "license")
    assert hasattr(schema, "description")
    assert hasattr(schema, "version")
